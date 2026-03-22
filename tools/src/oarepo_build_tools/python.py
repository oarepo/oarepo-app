"""Helpers for querying Python package indices and managing dependency versions."""

from __future__ import annotations

import os
import re
import subprocess
import tomllib
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable

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


def relax_pinned_requirement(dep: str) -> str:
    """Change an exact pin (``==X.Y.Z``) to ``>=X.Y.Z,<(X+1).0.0``.

    The upper bound keeps the dependency within the same major version so that
    ``uv lock`` cannot silently pull in a breaking major bump.
    Any specifier that does not use ``==`` is returned unchanged.
    """
    req = Requirement(dep)
    pinned = [s for s in req.specifier if s.operator == "=="]
    if not pinned:
        return dep
    version = Version(pinned[0].version)
    next_major = version.major + 1
    return _rebuild_requirement(req, f">={version},<{next_major}.0.0")


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


def _apply_to_dep_list(
    deps: list[str],
    includes: list[str],
    excludes: list[str],
    transform: Callable[[str], str],
) -> tuple[list[str], bool]:
    """Apply *transform* to each dependency in *deps* that passes the filter.

    Returns the (possibly modified) list and a boolean indicating whether
    anything changed.
    """
    updated: list[str] = []
    changed = False

    for dep in deps:
        try:
            req = Requirement(dep)
        except Exception:
            updated.append(dep)
            continue

        if is_package_included(req.name, includes, excludes):
            new_dep = transform(dep)
            if new_dep != dep:
                changed = True
            updated.append(new_dep)
        else:
            updated.append(dep)

    return updated, changed


def _transform_pyproject_deps(
    pyproject_path: Path,
    includes: list[str],
    excludes: list[str],
    transform: Callable[[str], str],
) -> bool:
    """Read *pyproject_path*, apply *transform* to matching deps, write back.

    Handles both ``[project].dependencies`` and
    ``[project.optional-dependencies]``.  Returns True if the file changed.
    """
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)

    changed = False
    project = data.get("project", {})

    if "dependencies" in project:
        new_deps, c = _apply_to_dep_list(
            project["dependencies"], includes, excludes, transform
        )
        if c:
            project["dependencies"] = new_deps
            changed = True

    for extra_name, extra_deps in project.get("optional-dependencies", {}).items():
        new_deps, c = _apply_to_dep_list(extra_deps, includes, excludes, transform)
        if c:
            project["optional-dependencies"][extra_name] = new_deps
            changed = True

    if changed:
        pyproject_path.write_bytes(tomli_w.dumps(data).encode())

    return changed


def relax_pyproject_deps(
    pyproject_path: Path,
    includes: list[str],
    excludes: list[str],
) -> bool:
    """Relax matching ``==`` pins to ``>=`` in *pyproject_path*.

    Returns True if the file was modified.
    """
    return _transform_pyproject_deps(
        pyproject_path, includes, excludes, relax_pinned_requirement
    )


def pin_pyproject_deps(
    pyproject_path: Path,
    includes: list[str],
    excludes: list[str],
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

    return _transform_pyproject_deps(pyproject_path, includes, excludes, _pin)


# ─── uv lock helpers ─────────────────────────────────────────────────────────


def run_uv_lock(directory: Path) -> None:
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


def get_oarepo_app_version(oarepo_version: str) -> str:
    """Compute the next unused oarepo-app version derived from *oarepo_version*.

    The version has the form ``x.y.z.N`` where ``x.y.z`` is the release of
    *oarepo_version* (capped at three segments) and ``N`` starts at 1 and is
    incremented until a version not already published on CESNET PyPI is found.
    Any pre-release, dev, or post markers are copied verbatim from
    *oarepo_version*.
    """
    oarepo_v = Version(oarepo_version)
    existing = set(get_available_versions("oarepo-app"))

    base_release = ".".join(str(x) for x in oarepo_v.release[:3])
    epoch = f"{oarepo_v.epoch}!" if oarepo_v.epoch else ""
    pre = f"{oarepo_v.pre[0]}{oarepo_v.pre[1]}" if oarepo_v.pre is not None else ""
    post = f".post{oarepo_v.post}" if oarepo_v.post is not None else ""
    dev = f".dev{oarepo_v.dev}" if oarepo_v.dev is not None else ""

    n = 1
    while True:
        candidate = Version(f"{epoch}{base_release}.{n}{pre}{post}{dev}")
        if candidate not in existing:
            return str(candidate)
        n += 1


def set_pyproject_version(pyproject_path: Path, version: str) -> None:
    """Set ``[project].version`` in *pyproject_path* to *version*."""
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
    data.setdefault("project", {})["version"] = version
    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


# ─── update_versions ─────────────────────────────────────────────────────────


def update_versions(
    directory: Path,
    includes: list[str],
    excludes: list[str],
    oarepo_version: str,
) -> None:
    """Update pinned dependency versions in *directory*/pyproject.toml.

    Steps:
    1. Relax every matching ``==X.Y`` pin to ``>=X.Y`` so that uv is free
       to resolve a newer compatible release.
    2. Run ``uv lock`` to produce an updated lock file.
    3. Read the resolved versions from ``uv.lock`` and re-pin each matching
       dependency to ``==<resolved>``.
    """
    root = directory.resolve()
    lock_path = root / "uv.lock"
    pyproject_path = root / "pyproject.toml"

    # ── Step 1: relax == to >= ───────────────────────────────────────────────
    # 1a: pin the bare `oarepo` package unconditionally to the target version,
    #     bypassing the includes/excludes filter entirely.
    # 1b: relax every other matching package to >=X.Y.Z,<(X+1).0.0, excluding
    #     `oarepo` so it is not touched again.
    print(
        "[bold blue]Step 1/3[/bold blue] 🔓 Relaxing [yellow]==[/yellow] pins to [green]>=[/green] …"
    )
    oarepo_changed = _transform_pyproject_deps(
        pyproject_path,
        includes=["^oarepo$"],
        excludes=[],
        transform=lambda dep: _rebuild_requirement(
            Requirement(dep), f"=={oarepo_version}"
        ),
    )
    others_changed = _transform_pyproject_deps(
        pyproject_path,
        includes=includes,
        excludes=excludes + ["^oarepo$"],
        transform=relax_pinned_requirement,
    )
    if oarepo_changed or others_changed:
        print("  [dim]↳[/dim] ✏️  [yellow]modified[/yellow] pyproject.toml")

    # ── Step 2: uv lock ──────────────────────────────────────────────────────
    print("[bold blue]Step 2/3[/bold blue] 🔒 Running [cyan]uv lock[/cyan] …")
    run_uv_lock(root)

    # ── Step 3: pin to resolved versions ────────────────────────────────────
    print("[bold blue]Step 3/3[/bold blue] 📌 Pinning to resolved versions …")
    resolved = parse_uv_lock(lock_path)
    if pin_pyproject_deps(pyproject_path, includes, excludes, resolved):
        print("  [dim]↳[/dim] 📌 [green]pinned[/green] pyproject.toml")

    print("🎉 [bold green]Done.[/bold green]")
