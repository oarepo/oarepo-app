"""Report pinned dependencies in pyproject.toml that have a newer release on PyPI."""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Annotated

import tomli
import typer
from packaging.requirements import Requirement
from packaging.version import InvalidVersion, Version

# ---------------------------------------------------------------------------
# pyproject.toml parsing
# ---------------------------------------------------------------------------


def collect_pinned_dependencies(pyproject_path: Path) -> dict[str, tuple[str, str]]:
    """Return all completely-pinned dependencies from *pyproject_path*.

    A dependency is "completely pinned" when it carries exactly one version
    specifier that uses the ``==`` operator with no wildcard
    (e.g. ``package==1.2.3`` but not ``package==1.2.*``).

    Returns a mapping of *package name* → ``(group_label, pinned_version)``.
    When the same package appears in multiple groups the last occurrence wins.
    """
    data = tomli.loads(pyproject_path.read_text(encoding="utf-8"))
    result: dict[str, tuple[str, str]] = {}

    def _process(group_label: str, deps: list) -> None:
        for dep in deps:
            if not isinstance(dep, str):
                # PEP 735 dependency-groups may contain dicts (include-group)
                continue
            try:
                req = Requirement(dep)
            except Exception as exc:
                print(
                    f"Warning: could not parse dependency {dep!r} in {group_label}: {exc}",
                    file=sys.stderr,
                )
                continue
            specs = list(req.specifier)
            if len(specs) == 1 and specs[0].operator == "==" and "*" not in specs[0].version:
                result[req.name] = (group_label, specs[0].version)

    project = data.get("project", {})

    # [project.dependencies]
    _process("[project.dependencies]", project.get("dependencies", []))

    # [project.optional-dependencies.<group>]
    for group, deps in project.get("optional-dependencies", {}).items():
        _process(f"[project.optional-dependencies.{group}]", deps)

    # [dependency-groups.<group>]  (PEP 735)
    for group, deps in data.get("dependency-groups", {}).items():
        _process(f"[dependency-groups.{group}]", deps)

    return result


# ---------------------------------------------------------------------------
# PyPI version lookup
# ---------------------------------------------------------------------------


def get_latest_pypi_version(package_name: str) -> Version | None:
    """Return the latest version of *package_name* on PyPI, or ``None`` on error.

    Uses the PyPI JSON API ``/pypi/{name}/json`` endpoint.  The ``version``
    field in ``info`` reflects the latest non-yanked release.
    """
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
        return Version(data["info"]["version"])
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            print(f"error: {package_name!r} not found on PyPI.", file=sys.stderr)
        else:
            print(
                f"error: HTTP {exc.code} while fetching {package_name!r} from PyPI.",
                file=sys.stderr,
            )
    except InvalidVersion as exc:
        print(
            f"error: could not parse PyPI version for {package_name!r}: {exc}",
            file=sys.stderr,
        )
    except Exception as exc:
        print(
            f"error: unexpected error fetching {package_name!r}: {exc}",
            file=sys.stderr,
        )
    return None


# ---------------------------------------------------------------------------
# Typer command
# ---------------------------------------------------------------------------


def diff_pyproject_to_pypi(
    pyproject: Annotated[
        Path,
        typer.Argument(
            help="Path to the pyproject.toml to inspect.",
        ),
    ] = Path("pyproject.toml"),
) -> None:
    """Report pinned dependencies that have a newer release on PyPI.

    Reads every completely-pinned dependency (``package==x.y.z``) from all
    dependency groups in PYPROJECT and checks PyPI for a higher version.
    Outdated packages are printed to stdout; errors go to stderr.
    """
    if not pyproject.exists():
        print(f"error: {pyproject} not found.", file=sys.stderr)
        raise typer.Exit(1)

    pinned = collect_pinned_dependencies(pyproject)
    if not pinned:
        print("No completely-pinned dependencies found.", file=sys.stderr)
        return

    outdated: list[tuple[str, str, str, str]] = []  # (name, group, pinned, latest)

    for package_name, (group, pinned_str) in pinned.items():
        try:
            pinned_version = Version(pinned_str)
        except InvalidVersion:
            print(
                f"error: cannot parse pinned version {pinned_str!r} for {package_name!r}.",
                file=sys.stderr,
            )
            continue

        latest = get_latest_pypi_version(package_name)
        if latest is None:
            continue

        if latest > pinned_version:
            outdated.append((package_name, group, str(pinned_version), str(latest)))

    if not outdated:
        return

    outdated.sort()
    name_w = max(len(row[0]) for row in outdated)
    ver_w = max(len(row[2]) for row in outdated)

    for name, group, pinned_ver, latest_ver in outdated:
        print(f"{name:<{name_w}}  {pinned_ver:>{ver_w}}  →  {latest_ver}  ({group})")
