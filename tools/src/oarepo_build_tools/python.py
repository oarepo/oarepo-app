"""Helpers for querying Python package indices and managing dependency versions."""

from __future__ import annotations

import os
import re
import subprocess
import tomllib
import urllib.error
import urllib.request
from copy import replace
from pathlib import Path

import tomli_w
from packaging.requirements import Requirement
from packaging.utils import parse_sdist_filename, parse_wheel_filename
from packaging.version import Version
from rich import print

from oarepo_build_tools.constants import CESNET_PYPI_URL

# ─── PyPI version querying ────────────────────────────────────────────────────


def get_available_versions(
    package: str,
    index_url: str = CESNET_PYPI_URL,
) -> list[Version]:
    """Return all versions of *package* available on *index_url*.

    Fetches the PEP 503 simple index page directly and parses every
    distribution filename listed there.  This is more reliable than
    ``pip index versions``, which may truncate long version lists.
    Returns an empty list when the package is not yet present on the index.
    """
    url = f"{index_url.rstrip('/')}/{package}/"
    try:
        with urllib.request.urlopen(url) as resp:
            content = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return []  # package not yet present on the index
        raise

    filenames = re.findall(
        r'href="[^"]*?([^/"]+\.(?:whl|tar\.gz|zip))(?:#[^"]*)?[^"]*"',
        content,
    )

    seen: set[Version] = set()
    versions: list[Version] = []
    for filename in filenames:
        try:
            if filename.endswith(".whl"):
                _, version, _, _ = parse_wheel_filename(filename)
            elif filename.endswith((".tar.gz", ".zip")):
                _, version = parse_sdist_filename(filename)
            else:
                continue
            if version not in seen:
                seen.add(version)
                versions.append(version)
        except Exception:
            pass

    return versions


# ─── Dependency string helpers ────────────────────────────────────────────────


def _normalise_package_name(name: str) -> str:
    """Normalise a package name to lowercase with dashes (PEP 503)."""
    return re.sub(r"[-_.]+", "-", name).lower()


def _rebuild_requirement(req: Requirement, specifier_str: str) -> str:
    """Reconstruct a PEP 508 string from *req*, replacing its specifier."""
    extras = f"[{','.join(sorted(req.extras))}]" if req.extras else ""
    marker = f" ; {req.marker}" if req.marker else ""
    return f"{req.name}{extras}{specifier_str}{marker}"


def pin_requirement_to_version(dep: str, resolved_version: str) -> str:
    """Replace the specifier of *dep* with ``==resolved_version``."""
    req = Requirement(dep)
    return _rebuild_requirement(req, f"=={resolved_version}")


# ─── Include / exclude filtering ─────────────────────────────────────────────


def is_package_included(
    package_name: str,
    includes: list[str],
    excludes: list[str],
) -> bool:
    """Return True when *package_name* passes the include/exclude filters.

    The name is normalised before matching.  An empty *includes* list means
    "match everything"; each entry in *excludes* is a veto.
    """
    normalised = _normalise_package_name(package_name)
    if includes and not any(re.match(pat, normalised) for pat in includes):
        return False
    return not any(re.match(pat, normalised) for pat in excludes)


# ─── pyproject.toml processing ───────────────────────────────────────────────


def remove_production_section(pyproject_path: Path) -> None:
    """Remove the production section from *pyproject_path*."""
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
        project = data.get("project", {})
    project.get("optional-dependencies", {}).pop("production", None)
    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


def pin_pyproject_deps(
    pyproject_path: Path,
    resolved: dict[str, str],
) -> bool:
    """Pin matching dependencies to their resolved versions from the lock file.

    Returns True if the file was modified.
    """

    def _pin(dep: str) -> str:
        req = Requirement(dep)
        version = resolved.get(_normalise_package_name(req.name))
        if version is None:
            return dep
        return pin_requirement_to_version(dep, version)

    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
        project = data.get("project", {})
    original_data = tomli_w.dumps(data).encode()
    optional_dependencies = project.get("optional-dependencies", {})
    development_dependencies = optional_dependencies.get("development", None)
    production_dependencies = [_pin(dep) for dep in development_dependencies]
    optional_dependencies["production"] = production_dependencies
    new_data = tomli_w.dumps(data).encode()
    pyproject_path.write_bytes(new_data)
    return original_data != new_data


# ─── uv lock helpers ─────────────────────────────────────────────────────────


def run_uv_lock(directory: Path, extra_options: list[str] | None = None) -> None:
    """Run ``uv lock`` inside *directory* to regenerate the lock file."""
    # clean the cache first to avoid stale lock file issues
    subprocess.run(["uv", "cache", "clean"])

    lock_file_path = directory / "uv.lock"
    if lock_file_path.exists():
        lock_file_path.unlink()

    # and lock the dependencies
    subprocess.run(
        ["uv", "lock", "--prerelease=allow"],
        cwd=directory,
        check=True,
        env={**os.environ, "UV_EXTRA_INDEX_URL": CESNET_PYPI_URL},
    )


def parse_uv_lock(lock_path: Path) -> dict[str, str]:
    """Parse a ``uv.lock`` file and return a mapping of package name → version.

    Package names are normalised (lowercase, dashes) so they can be matched
    against normalised names extracted from dependency strings.
    """
    with lock_path.open("rb") as fh:
        data = tomllib.load(fh)

    return {
        _normalise_package_name(pkg["name"]): pkg["version"]
        for pkg in data.get("package", [])
        if "version" in pkg
    }


# ─── oarepo-app versioning ────────────────────────────────────────────────────


def get_oarepo_app_version(changelog_path: Path, pyproject_path: Path) -> str:
    """Compute the next unused oarepo-app version derived from the current version
    and a list of changes.

    To do so, read the CHANGELOG.json and compare the first two records. For each,
    check the version of the packages to get the level of change:

    1. If the major version has changed, we need to do a major bump of oarepo-app.
    2. If the minor version has changed, we need to do a minor bump of oarepo-app.
    3. If the patch version has changed, we need to do a patch bump of oarepo-app.
    4. If the package was not present in the previous dump and is present now, we need to do a major bump of oarepo-app.
    5. If the package was present in the previous dump and is not present now, we need to do a major bump of oarepo-app.
    """
    major_needed = False
    minor_needed = False
    patch_needed = False

    print("[bold blue]🔢[/bold blue] Computing oarepo-app version bump …")

    from .logs import get_two_latest_log_entries

    current, previous = get_two_latest_log_entries(changelog_path)
    if not previous:
        major_needed = True
        print(
            "  [dim]↳[/dim] no previous changelog entry — "
            "[bold red]major[/bold red] bump required"
        )
    else:
        current_packages = set(current["packages"])
        previous_packages = set(previous["packages"])
        if current_packages != previous_packages:
            added = current_packages - previous_packages
            removed = previous_packages - current_packages
            if added:
                print(
                    f"  [dim]↳[/dim] new packages: "
                    f"[cyan]{', '.join(sorted(added))}[/cyan] → "
                    "[bold red]major[/bold red] bump"
                )
            if removed:
                print(
                    f"  [dim]↳[/dim] removed packages: "
                    f"[cyan]{', '.join(sorted(removed))}[/cyan] → "
                    "[bold red]major[/bold red] bump"
                )
            major_needed = True
        else:
            for pkg, current_rec in current["packages"].items():
                previous_rec = previous["packages"][pkg]
                current_version = Version(current_rec["version"])
                previous_version = Version(previous_rec["version"])
                if current_version == previous_version:
                    continue
                if current_version.major != previous_version.major:
                    print(
                        f"  [dim]↳[/dim] [cyan]{pkg}[/cyan]: "
                        f"[dim]{previous_version}[/dim] → "
                        f"[bold green]{current_version}[/bold green] "
                        "([bold red]major[/bold red])"
                    )
                    major_needed = True
                elif current_version.minor != previous_version.minor:
                    print(
                        f"  [dim]↳[/dim] [cyan]{pkg}[/cyan]: "
                        f"[dim]{previous_version}[/dim] → "
                        f"[bold green]{current_version}[/bold green] "
                        "([yellow]minor[/yellow])"
                    )
                    minor_needed = True
                elif (
                    current_version.micro != previous_version.micro
                    or current_version.dev != previous_version.dev
                    or current_version.pre != previous_version.pre
                ):
                    print(
                        f"  [dim]↳[/dim] [cyan]{pkg}[/cyan]: "
                        f"[dim]{previous_version}[/dim] → "
                        f"[bold green]{current_version}[/bold green] "
                        "(patch)"
                    )
                    patch_needed = True

    current_oarepo_app_version = Version(get_pyproject_version(pyproject_path))
    if major_needed:
        print(
            f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → "
            "[bold red]major[/bold red] bump"
        )
        new_version = replace(
            current_oarepo_app_version,
            release=(current_oarepo_app_version.major + 1, 0, 0),
        )
    elif minor_needed:
        print(
            f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → "
            "[yellow]minor[/yellow] bump"
        )
        new_version = replace(
            current_oarepo_app_version,
            release=(
                current_oarepo_app_version.major,
                current_oarepo_app_version.minor + 1,
                0,
            ),
        )
    elif patch_needed:
        print(
            f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → "
            "patch bump"
        )
        new_version = replace(
            current_oarepo_app_version,
            release=(
                current_oarepo_app_version.major,
                current_oarepo_app_version.minor,
                current_oarepo_app_version.micro + 1,
            ),
        )
    else:
        print(
            f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → "
            "no changes detected, keeping current version"
        )
        new_version = current_oarepo_app_version
    print(f"  [dim]↳[/dim] ✅ new version: [bold green]{new_version}[/bold green]")
    return str(new_version)


def get_pyproject_version(pyproject_path: Path) -> str:
    """Get the version from the pyproject.toml file."""
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
    return data["project"]["version"]


def set_pyproject_version(pyproject_path: Path, version: str) -> None:
    """Set ``[project].version`` in *pyproject_path* to *version*."""
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
    data.setdefault("project", {})["version"] = version
    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


# ─── update_versions ─────────────────────────────────────────────────────────


def update_versions(
    directory: Path,
) -> None:
    """Update pinned dependency versions in *directory*/pyproject.toml.

    Steps:
    1. Remove the production section from pyproject.toml.
    2. Run ``uv lock`` to produce an updated lock file.
    3. Read the resolved versions from ``uv.lock`` and pin each matching
       dependency inside the "production" section of pyproject.toml to ``==<resolved>``.
    4. If a dependency is in development dependencies but not in the "production" section,
       add it to the "production" section.
    """
    root = directory.resolve()
    lock_path = root / "uv.lock"
    pyproject_path = root / "pyproject.toml"

    # ── Step 1: remove production section ─────────────────────────────────────
    print(
        "[bold blue]Step 1/3[/bold blue] 🗑️  Removing production section from pyproject.toml …"
    )
    remove_production_section(pyproject_path)

    # ── Step 2: uv lock ──────────────────────────────────────────────────────
    print("[bold blue]Step 2/3[/bold blue] 🔒 Running [cyan]uv lock[/cyan] …")
    run_uv_lock(root)

    # ── Step 3: pin to resolved versions ────────────────────────────────────
    print("[bold blue]Step 3/3[/bold blue] 📌 Pinning to resolved versions …")
    resolved = parse_uv_lock(lock_path)
    if pin_pyproject_deps(pyproject_path, resolved):
        print("  [dim]↳[/dim] 📌 [green]pinned[/green] pyproject.toml")

    print("🎉 [bold green]Done.[/bold green]")
