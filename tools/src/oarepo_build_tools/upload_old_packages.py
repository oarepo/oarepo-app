"""Mirror packages from official PyPI to the CESNET GitLab package registry.

Compares the versions available on PyPI against those already present on the
CESNET registry and uploads any that are missing.

Required environment variables:
    TWINE_USERNAME  - GitLab deploy-token username (or "__token__" for PATs)
    TWINE_PASSWORD  - GitLab deploy-token value / personal access token

Usage:
    TWINE_USERNAME=... TWINE_PASSWORD=... oarepo-app-build upload-old-packages
    TWINE_USERNAME=... TWINE_PASSWORD=... oarepo-app-build upload-old-packages invenio-rdm
"""

from __future__ import annotations

import contextlib
import json
import os
import subprocess
import tempfile
import urllib.request
from pathlib import Path
from typing import Annotated

import typer
from oarepo_build_tools.constants import CESNET_PYPI_UPLOAD_URL as CESNET_UPLOAD_URL
from oarepo_build_tools.python import get_available_versions
from packaging.version import InvalidVersion, Version
from rich import print as rich_print

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
    rich_print(f"📦 Fetching [bold]{package_name}[/bold] versions from PyPI …")
    url = f"https://pypi.org/pypi/{package_name}/json"
    with urllib.request.urlopen(url) as resp:  # noqa: S310 - url is hardcoded https://pypi.org/
        data = json.loads(resp.read())

    result: dict[str, str] = {}
    for raw in data["releases"]:
        with contextlib.suppress(InvalidVersion):
            result[str(Version(raw))] = raw
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
    with urllib.request.urlopen(url) as resp:  # noqa: S310 - url is hardcoded https://pypi.org/
        data = json.loads(resp.read())

    files: list[Path] = []
    for file_info in data.get("urls", []):
        filename = file_info["filename"]
        file_url = file_info["url"]
        dest_file = dest / filename
        rich_print(f"    [dim]↳[/dim] {filename} … ", end="")
        urllib.request.urlretrieve(file_url, dest_file)  # noqa: S310 - file_url comes from PyPI JSON API, always https://files.pythonhosted.org/
        files.append(dest_file)

    return files


# ---------------------------------------------------------------------------
# Upload
# ---------------------------------------------------------------------------


def upload(twine: Path, files: list[Path], env: dict[str, str]) -> None:
    """Upload *files* to the CESNET registry via twine."""
    subprocess.run(  # noqa: S603
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
        rich_print("[bold red]✗[/bold red] TWINE_USERNAME and TWINE_PASSWORD environment variables must be set.")
        raise typer.Exit(1)

    # Pass credentials to twine via the environment so they never appear in
    # the process argument list.
    twine_env = {**os.environ, "TWINE_USERNAME": username, "TWINE_PASSWORD": password}

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        venv = tmp / "venv"

        # ── Bootstrap a throw-away venv with twine ────────────────────────
        rich_print("🔧 Creating temporary virtualenv …")
        subprocess.run(  # noqa: S603
            ["uv", "venv", str(venv)],  # noqa: S607
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        twine = venv / "bin" / "twine"

        rich_print("📥 Installing twine into temporary venv …")
        subprocess.run(  # noqa: S603
            [  # noqa: S607
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
        rich_print(f"🔍 Fetching [bold]{package_name}[/bold] versions from CESNET registry …")
        cesnet_versions = {str(v) for v in get_available_versions(package_name)}
        missing = pypi_versions.keys() - cesnet_versions

        if not missing:
            rich_print(
                f"✅ Nothing to do - all [bold]{package_name}[/bold] versions are already on the CESNET registry."
            )
            return

        rich_print(f"\n🚀 [bold]{len(missing)}[/bold] version(s) to upload:\n")
        for v in sorted(missing, key=Version):
            rich_print(f"  [cyan]{v}[/cyan]")
        rich_print()

        # ── Download & upload each missing version ─────────────────────────
        errors: list[str] = []

        for version in sorted(missing, key=Version):
            original_version = pypi_versions[version]
            dist_dir = tmp / f"dist-{version}"
            dist_dir.mkdir()

            rich_print(f"[bold blue][{version}][/bold blue] downloading … ", end="")
            files = download_distributions(package_name, original_version, dist_dir)

            if not files:
                msg = f"[{version}] no distribution files found on PyPI - skipping."
                rich_print("[yellow]no files found, skipping.[/yellow]")
                errors.append(msg)
                continue

            names = [f.name for f in files]
            rich_print(f"got {names}. uploading … ", end="")

            try:
                upload(twine, files, twine_env)
                rich_print("[green]done.[/green]")
            except subprocess.CalledProcessError as exc:
                msg = f"[{version}] upload failed: {exc}"
                rich_print("[bold red]FAILED.[/bold red]")
                errors.append(msg)

        # ── Summary ────────────────────────────────────────────────────────
        if errors:
            rich_print(f"[bold red]✗ {len(errors)} error(s) occurred:[/bold red]")
            for e in errors:
                rich_print(f"  [red]{e}[/red]")
            raise typer.Exit(1)

        rich_print("\n🎉 [bold green]All done.[/bold green]")
