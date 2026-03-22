#!/usr/bin/env python3
"""Mirror packages from official PyPI to the CESNET GitLab package registry.

Compares the versions available on PyPI against those already present on the
CESNET registry and uploads any that are missing.

Required environment variables:
    TWINE_USERNAME  – GitLab deploy-token username (or "__token__" for PATs)
    TWINE_PASSWORD  – GitLab deploy-token value / personal access token

Usage:
    TWINE_USERNAME=... TWINE_PASSWORD=... oarepo-app-build upload-old-packages
    TWINE_USERNAME=... TWINE_PASSWORD=... oarepo-app-build upload-old-packages invenio-rdm
"""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
import urllib.request
from pathlib import Path
from typing import Annotated

import typer
from packaging.version import InvalidVersion, Version
from rich import print

from oarepo_build_tools.constants import CESNET_PYPI_UPLOAD_URL as CESNET_UPLOAD_URL
from oarepo_build_tools.python import get_available_versions

# ---------------------------------------------------------------------------
# Version discovery
# ---------------------------------------------------------------------------


def get_pypi_versions(package_name: str) -> dict[str, str]:
    """Return all versions of *package_name* published on official PyPI.

    Returns a mapping of *normalized* version string → *original* version
    string (as used in the PyPI JSON API URL).  Normalization ensures
    accurate comparison with the versions extracted from CESNET filenames.
    Entries that cannot be parsed as PEP 440 versions are skipped.
    """
    print(f"📦 Fetching [bold]{package_name}[/bold] versions from PyPI …")
    url = f"https://pypi.org/pypi/{package_name}/json"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read())

    result: dict[str, str] = {}
    for raw in data["releases"].keys():
        try:
            result[str(Version(raw))] = raw
        except InvalidVersion:
            pass
    return result


# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------


def download_distributions(package_name: str, version: str, dest: Path) -> list[Path]:
    """Download the wheel and sdist for *version* of *package_name* from PyPI into *dest*.

    Uses the PyPI JSON API to obtain the exact download URLs so that no build
    system is invoked and no dependency resolution is performed.  Both the
    wheel (if present) and the source distribution (if present) are fetched.
    """
    url = f"https://pypi.org/pypi/{package_name}/{version}/json"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read())

    files: list[Path] = []
    for file_info in data.get("urls", []):
        filename = file_info["filename"]
        file_url = file_info["url"]
        dest_file = dest / filename
        print(f"    [dim]↳[/dim] {filename} … ", end="")
        urllib.request.urlretrieve(file_url, dest_file)
        files.append(dest_file)

    return files


# ---------------------------------------------------------------------------
# Upload
# ---------------------------------------------------------------------------


def upload(twine: Path, files: list[Path], env: dict[str, str]) -> None:
    """Upload *files* to the CESNET registry via twine."""
    subprocess.run(
        [
            str(twine),
            "upload",
            "--verbose",
            "--repository-url",
            CESNET_UPLOAD_URL,
            "--non-interactive",
            *(str(f) for f in files),
        ],
        env=env,
        check=True,
    )


# ---------------------------------------------------------------------------
# Typer command
# ---------------------------------------------------------------------------


def upload_old_packages(
    package_name: Annotated[
        str,
        typer.Argument(
            help="PyPI package name to mirror to the CESNET registry.",
        ),
    ] = "oarepo",
) -> None:
    """Mirror missing versions of a PyPI package to the CESNET registry.

    Compares versions available on PyPI against those already present on the
    CESNET registry and uploads any that are missing.

    Credentials are read from the TWINE_USERNAME and TWINE_PASSWORD
    environment variables.
    """
    username = os.environ.get("TWINE_USERNAME")
    password = os.environ.get("TWINE_PASSWORD")
    if not username or not password:
        print(
            "[bold red]✗[/bold red] TWINE_USERNAME and TWINE_PASSWORD "
            "environment variables must be set."
        )
        raise typer.Exit(1)

    # Pass credentials to twine via the environment so they never appear in
    # the process argument list.
    twine_env = {**os.environ, "TWINE_USERNAME": username, "TWINE_PASSWORD": password}

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        venv = tmp / "venv"

        # ── Bootstrap a throw-away venv with twine ────────────────────────
        print("🔧 Creating temporary virtualenv …")
        subprocess.run(
            ["uv", "venv", str(venv)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        twine = venv / "bin" / "twine"

        print("📥 Installing twine into temporary venv …")
        subprocess.run(
            [
                "uv",
                "pip",
                "install",
                "twine",
                "--python",
                str(venv / "bin" / "python"),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # ── Compare version sets ───────────────────────────────────────────
        pypi_versions = get_pypi_versions(package_name)  # dict: normalized → original
        print(
            f"🔍 Fetching [bold]{package_name}[/bold] versions from CESNET registry …"
        )
        cesnet_versions = {str(v) for v in get_available_versions(package_name)}
        missing = pypi_versions.keys() - cesnet_versions

        if not missing:
            print(
                f"✅ Nothing to do – all [bold]{package_name}[/bold] versions "
                "are already on the CESNET registry."
            )
            return

        print(f"\n🚀 [bold]{len(missing)}[/bold] version(s) to upload:\n")
        for v in sorted(missing, key=Version):
            print(f"  [cyan]{v}[/cyan]")
        print()

        # ── Download & upload each missing version ─────────────────────────
        errors: list[str] = []

        for version in sorted(missing, key=Version):
            original_version = pypi_versions[version]
            dist_dir = tmp / f"dist-{version}"
            dist_dir.mkdir()

            print(f"[bold blue][{version}][/bold blue] downloading … ", end="")
            files = download_distributions(package_name, original_version, dist_dir)

            if not files:
                msg = f"[{version}] no distribution files found on PyPI – skipping."
                print("[yellow]no files found, skipping.[/yellow]")
                errors.append(msg)
                continue

            names = [f.name for f in files]
            print(f"got {names}. uploading … ", end="")

            try:
                upload(twine, files, twine_env)
                print("[green]done.[/green]")
            except subprocess.CalledProcessError as exc:
                msg = f"[{version}] upload failed: {exc}"
                print("[bold red]FAILED.[/bold red]")
                errors.append(msg)

        # ── Summary ────────────────────────────────────────────────────────
        if errors:
            print(f"\n[bold red]✗ {len(errors)} error(s) occurred:[/bold red]")
            for e in errors:
                print(f"  [red]{e}[/red]")
            raise typer.Exit(1)

        print("\n🎉 [bold green]All done.[/bold green]")
