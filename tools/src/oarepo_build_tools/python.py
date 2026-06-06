"""Helpers for querying Python package indices and managing dependency versions."""

from __future__ import annotations

import os
import re
import subprocess
import tomllib
import urllib.error
import urllib.request
from copy import replace
from typing import TYPE_CHECKING

import tomli_w
from oarepo_build_tools.constants import CESNET_PYPI_URL
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.utils import parse_sdist_filename, parse_wheel_filename
from packaging.version import Version
from rich import print as rich_print

if TYPE_CHECKING:
    from pathlib import Path


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
        with urllib.request.urlopen(url) as resp:  # noqa: S310 - index_url is always https (default: CESNET_PYPI_URL)
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
        except Exception:  # noqa: BLE001, S110
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
    project.get("optional-dependencies", {}).pop("ccmm", None)
    project.get("optional-dependencies", {}).pop("oaipmh-harvester", None)
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
    for source_extra, target_extra in [
        ("development", "production"),
        ("ccmm-development", "ccmm"),
        ("oaipmh-harvester-development", "oaipmh-harvester"),
    ]:
        development_dependencies = optional_dependencies.get(source_extra, [])
        production_dependencies = [_pin(dep) for dep in development_dependencies]
        optional_dependencies[target_extra] = production_dependencies
    new_data = tomli_w.dumps(data).encode()
    pyproject_path.write_bytes(new_data)
    return original_data != new_data


def unpin_development_major_versions(pyproject_path: Path) -> None:
    """Unpin major versions of oarepo dependencies in *pyproject_path*."""
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
        project = data.get("project", {})
    optional_dependencies = project.get("optional-dependencies", {})
    for extra_name in ["development", "ccmm-development", "oaipmh-harvester-development", "tests"]:
        development_deps = optional_dependencies.get(extra_name, [])
        for idx, dep in enumerate(development_deps):
            req = Requirement(dep)
            if "oarepo" in _normalise_package_name(
                req.name
            ):  # Apply only to oarepo packages, others use different versioning schemes
                # always suppose that the first specifier is the >= specifier
                first_specifier = next(rs for rs in req.specifier if rs.operator == ">=")
                development_deps[idx] = _rebuild_requirement(req, f">={first_specifier.version}")

    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


def pin_development_major_versions(pyproject_path: Path, resolved: dict[str, str]) -> None:
    """Pin major versions of oarepo dependencies in *pyproject_path*."""
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
        project = data.get("project", {})
    optional_dependencies = project.get("optional-dependencies", {})
    for extra_name in ["development", "ccmm-development", "oaipmh-harvester-development", "tests"]:
        development_deps = optional_dependencies.get(extra_name, [])
        for idx, dep in enumerate(development_deps):
            req = Requirement(dep)
            if "oarepo" in _normalise_package_name(
                req.name
            ):  # Apply only to oarepo packages, others use different versioning schemes
                if req.name not in resolved:
                    raise ValueError(f"Dependency {dep} not found in resolved dependencies")
                resolved_version = resolved[req.name].split("+")[0]  # strip local version label (not valid with >=)
                next_major_version = str(int(resolved_version.split(".")[0]) + 1)
                development_deps[idx] = _rebuild_requirement(req, f">={resolved_version},<{next_major_version}.0.0")

    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


# ─── uv lock helpers ─────────────────────────────────────────────────────────


def run_uv_lock(
    directory: Path,
    extra_options: list[str] | None = None,
) -> None:
    """Run ``uv lock`` inside *directory* to regenerate the lock file."""
    # clean the cache first to avoid stale lock file issues
    subprocess.run(["uv", "cache", "clean"], check=False)  # noqa: S607

    lock_file_path = directory / "uv.lock"
    if lock_file_path.exists():
        lock_file_path.unlink()

    lock_command = ["uv", "lock", "--prerelease=allow"]
    if extra_options:
        lock_command.extend(extra_options)

    # and lock the dependencies
    subprocess.run(  # noqa: S603
        lock_command,
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

    return {_normalise_package_name(pkg["name"]): pkg["version"] for pkg in data.get("package", []) if "version" in pkg}


# ─── oarepo-app versioning ────────────────────────────────────────────────────


def get_oarepo_app_version(  # noqa: C901 TODO: refactor into smaller helpers
    changelog_path: Path,
    pyproject_path: Path,
    release_candidate: str = "public",
) -> str:
    """Compute the next unused oarepo-app version derived from the current version and a list of changes.

    To do so, read the CHANGELOG.json and compare the first two records. For each,
    check the version of the packages to get the level of change:

    1. If the major version has changed, we need to do a major bump of oarepo-app.
    2. If the minor version has changed, we need to do a minor bump of oarepo-app.
    3. If the patch version has changed, we need to do a patch bump of oarepo-app.
    4. If the package was not present in the previous dump and is present now, we need to do a major bump of oarepo-app.
    5. If the package was present in the previous dump and is not present now, we need to do a major bump of oarepo-app.

    The *release_candidate* parameter controls whether and how an RC suffix is applied:

    - ``"public"``   - no RC; current behaviour (default).
    - ``"patch-rc"`` - ensure at least a patch bump, then append ``rc1``.
    - ``"minor-rc"`` - ensure at least a minor bump, then append ``rc1``.
    - ``"major-rc"`` - ensure at least a major bump, then append ``rc1``.
    - ``"inc-rc"``   - keep the current base release, increment the existing RC
                       number (or start at ``rc1`` if there is none).

    For the ``*-rc`` modes the "current versioning mechanism" is applied first to
    determine the required bump level.  If the changelog already demands a higher
    bump than the one requested, the higher bump wins (e.g. requesting
    ``patch-rc`` when a major bump is required yields ``<major+1>.0.0rc1``).
    """
    major_needed = False
    minor_needed = False
    patch_needed = False

    rich_print("[bold blue]🔢[/bold blue] Computing oarepo-app version bump …")

    from .logs import get_two_latest_log_entries

    current, previous = get_two_latest_log_entries(changelog_path)
    if not previous:
        major_needed = True
        rich_print("  [dim]↳[/dim] no previous changelog entry — [bold red]major[/bold red] bump required")
    else:
        current_packages = set(current["packages"])
        previous_packages = set(previous["packages"])
        if current_packages != previous_packages:
            added = current_packages - previous_packages
            removed = previous_packages - current_packages
            if added:
                rich_print(
                    f"  [dim]↳[/dim] new packages: "
                    f"[cyan]{', '.join(sorted(added))}[/cyan] → "
                    "[bold red]major[/bold red] bump"
                )
            if removed:
                rich_print(
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
                    rich_print(
                        f"  [dim]↳[/dim] [cyan]{pkg}[/cyan]: "
                        f"[dim]{previous_version}[/dim] → "
                        f"[bold green]{current_version}[/bold green] "
                        "([bold red]major[/bold red])"
                    )
                    major_needed = True
                elif current_version.minor != previous_version.minor:
                    rich_print(
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
                    rich_print(
                        f"  [dim]↳[/dim] [cyan]{pkg}[/cyan]: "
                        f"[dim]{previous_version}[/dim] → "
                        f"[bold green]{current_version}[/bold green] "
                        "(patch)"
                    )
                    patch_needed = True

    current_oarepo_app_version = Version(get_pyproject_version(pyproject_path))
    # Base release tuple - strips any RC/pre-release suffix.
    base_major, base_minor, base_micro = current_oarepo_app_version.release

    if release_candidate == "public":
        # ── original behaviour ────────────────────────────────────────────────
        if major_needed:
            rich_print(
                f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → [bold red]major[/bold red] bump"
            )
            new_version = replace(
                current_oarepo_app_version,
                release=(base_major + 1, 0, 0),
            )
        elif minor_needed:
            rich_print(f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → [yellow]minor[/yellow] bump")
            new_version = replace(
                current_oarepo_app_version,
                release=(base_major, base_minor + 1, 0),
            )
        elif patch_needed:
            rich_print(f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → patch bump")
            new_version = replace(
                current_oarepo_app_version,
                release=(base_major, base_minor, base_micro + 1),
            )
        else:
            rich_print(
                f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → "
                "no changes detected, keeping current version"
            )
            new_version = current_oarepo_app_version
        rich_print(f"  [dim]↳[/dim] ✅ new version: [bold green]{new_version}[/bold green]")
        return str(new_version)

    # ── release-candidate modes ───────────────────────────────────────────────
    # Map the changelog analysis to a numeric bump level so we can compare it
    # with the minimum level requested by the caller.
    #   0 = no change, 1 = patch, 2 = minor, 3 = major
    bump_level = 3 if major_needed else 2 if minor_needed else 1 if patch_needed else 0

    if release_candidate == "inc-rc":
        # Keep the same base release; just increment the RC counter.
        if current_oarepo_app_version.pre and current_oarepo_app_version.pre[0] == "rc":
            rc_num = current_oarepo_app_version.pre[1] + 1
        else:
            rc_num = 1
        new_release = (base_major, base_minor, base_micro)
        rich_print(f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → [cyan]inc-rc[/cyan] → rc{rc_num}")
    else:
        # Determine the minimum bump level implied by the RC mode.
        min_level = {"patch-rc": 1, "minor-rc": 2, "major-rc": 3}[release_candidate]
        effective_level = max(bump_level, min_level)
        rc_num = 1

        if effective_level == 3:
            new_release = (base_major + 1, 0, 0)
            bump_label = "[bold red]major[/bold red]"
        elif effective_level == 2:
            new_release = (base_major, base_minor + 1, 0)
            bump_label = "[yellow]minor[/yellow]"
        else:  # 1
            new_release = (base_major, base_minor, base_micro + 1)
            bump_label = "patch"

        rich_print(
            f"  [dim]↳[/dim] current [dim]{current_oarepo_app_version}[/dim] → "
            f"{bump_label} bump + [cyan]{release_candidate}[/cyan]"
        )

    new_version_str = f"{new_release[0]}.{new_release[1]}.{new_release[2]}rc{rc_num}"
    rich_print(f"  [dim]↳[/dim] ✅ new version: [bold green]{new_version_str}[/bold green]")
    return new_version_str


def get_pyproject_version(pyproject_path: Path) -> str:
    """Get the version from the pyproject.toml file."""
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
    try:
        return data.get("project", {})["version"]
    except KeyError:
        raise KeyError(f"Version not found in pyproject.toml in {pyproject_path}") from None


def set_pyproject_version(pyproject_path: Path, version: str) -> None:
    """Set ``[project].version`` in *pyproject_path* to *version*."""
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
    data.setdefault("project", {})["version"] = version
    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


def extract_oarepo_packages(pyproject_path: Path) -> dict[str, tuple[str, str, str]]:
    """Extract OARepo packages from the pyproject.toml file."""
    with pyproject_path.open("rb") as fh:
        data = tomllib.load(fh)
        project = data.get("project", {})
    optional_dependencies = project.get("optional-dependencies", {})
    oarepo_github = data.get("tool", {}).get("oarepo", {}).get("github", {})
    packages = {}
    for extra_name in ["development", "ccmm-development", "oaipmh-harvester-development"]:
        development_deps = optional_dependencies.get(extra_name, [])
        for dep in development_deps:
            req = Requirement(dep)
            try:
                org, repo, branch = find_package_on_github(oarepo_github, req.name)
            except KeyError:
                continue
            packages[req.name] = (org, repo, branch)
    return packages


def find_package_on_github(oarepo_github: dict, name: str) -> tuple[str, str, str]:
    """Find a package on GitHub based on the pyproject.toml configuration.

    Sections are matched in alphabetical key order (first match wins).

    Each section must have an ``org`` field and one of:
    - ``include``: a regex pattern string matched against the package name.
      The repo name is the package name itself.
    - ``package`` + ``repository``: an exact package name and the corresponding
      GitHub repository name (used when they differ).

    An optional ``exclude`` field (regex pattern string) vetoes a match even
    when ``include`` would otherwise match.

    An optional section-level ``branch`` field sets the branch (default: ``"main"``).

    Args:
        oarepo_github: The "tool.oarepo.github" section from the pyproject.toml.
        name: The package name to search for.

    Returns:
        A tuple of (org, repo, branch) if found, otherwise raises KeyError.

    """
    for _key in sorted(oarepo_github):
        section = oarepo_github[_key]
        org = section["org"]
        branch = section.get("branch", "main")
        if "package" in section:
            if section["package"] == name:
                repo = section.get("repository", name)
                return org, repo, branch
        else:
            includes = section.get("include", "")
            excludes = section.get("exclude", "")
            if includes and re.match(includes, name) and (not excludes or not re.match(excludes, name)):
                return org, name, branch
    raise KeyError(name)


def clone_oarepo_packages(
    local_packages_dir: Path,
    oarepo_packages_map: dict[str, tuple[str, str, str]],
    upgraded_packages: list[str] | None = None,
) -> dict[str, Path]:
    """Clone OARepo packages from GitHub into *local_packages_dir*.

    Args:
        local_packages_dir: The directory to clone the packages into.
        oarepo_packages_map: A mapping of package names to (org, repo, branch) tuples.
        upgraded_packages: Optional list of packages to upgrade, in GitHub PR/branch format.

    Returns:
        A dictionary mapping package names to the local path of the cloned package.

    """
    upgraded_packages = upgraded_packages or []
    upgraded_packages_map: dict[str, str] = {}
    for pkg in upgraded_packages:
        org, repo, branch = parse_github_pr_branch_identification(pkg)
        upgraded_packages_map[f"{org}/{repo}"] = branch

    cloned_packages = {}
    for name, (org, repo, branch) in oarepo_packages_map.items():
        org_with_repo = f"{org}/{repo}"
        package_path = local_packages_dir / name
        cloned_packages[name] = package_path
        if package_path.exists():
            continue

        subprocess.check_call(  # noqa: S603
            [  # noqa: S607
                "gh",
                "repo",
                "clone",
                org_with_repo,
                package_path,
                "--",
                "--depth",
                "1",
            ]
        )
        current_package_version = get_pyproject_version(package_path / "pyproject.toml")
        subprocess.call(  # noqa: S603
            ["git", "switch", upgraded_packages_map.get(org_with_repo, branch)],  # noqa: S607
            cwd=package_path,
        )
        if org_with_repo in upgraded_packages_map:
            set_original_package_version(package_path / "pyproject.toml", current_package_version)
    return cloned_packages


def _resolve_pr_branch(org: str, repo: str, pr_number: str) -> str:
    """Resolve a GitHub PR number to its head branch name using the ``gh`` CLI."""
    result = subprocess.check_output(  # noqa: S603
        [  # noqa: S607
            "gh",
            "pr",
            "view",
            pr_number,
            "--repo",
            f"{org}/{repo}",
            "--json",
            "headRefName",
            "--jq",
            ".headRefName",
        ],
        text=True,
    )
    return result.strip()


def parse_github_pr_branch_identification(pkg: str) -> tuple[str, str, str]:
    """Parse the GitHub identification and return a tuple of (org, repo, branch_name).

    *pkg* can be:
        * org/repo#pr
        * org/repo@branch
        * github pr url
        * github branch url
    """
    # https://github.com/org/repo/pull/123
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+)/pull/(\d+)/?$", pkg)
    if m:
        org, repo, pr_number = m.groups()
        return org, repo, _resolve_pr_branch(org, repo, pr_number)

    # https://github.com/org/repo/tree/some/branch/name
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+)/tree/(.+?)/?$", pkg)
    if m:
        org, repo, branch = m.groups()
        return org, repo, branch

    # org/repo#123
    m = re.match(r"([^/]+)/([^@#/]+)#(\d+)$", pkg)
    if m:
        org, repo, pr_number = m.groups()
        return org, repo, _resolve_pr_branch(org, repo, pr_number)

    # org/repo@branch
    m = re.match(r"([^/]+)/([^@#/]+)@(.+)$", pkg)
    if m:
        org, repo, branch = m.groups()
        return org, repo, branch

    raise ValueError(
        f"Cannot parse GitHub PR/branch identification: {pkg!r}. "
        "Expected one of: 'org/repo#<pr>', 'org/repo@<branch>', "
        "a GitHub PR URL (…/pull/<n>), or a GitHub branch URL (…/tree/<branch>)."
    )


def set_original_package_version(pyproject_path: Path, version: str) -> None:
    data = tomllib.loads(pyproject_path.read_text())
    tool = data.setdefault("tool", {})
    oarepo_tool = tool.setdefault("oarepo", {})
    oarepo_tool["original_version"] = version
    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


def unpin_versions_in_oarepo_packages(path: Path) -> None:
    """Load pyproject.toml from *path* and unpin all dependency versions.

    That is, remove ``<abc`` from requirement version specifiers.
    """
    pyproject_path = path / "pyproject.toml"
    data = tomllib.loads(pyproject_path.read_text())
    project = data.get("project", {})
    tool = data.setdefault("tool", {})
    oarepo_tool = tool.setdefault("oarepo", {})
    original_dependencies = oarepo_tool.setdefault("original-dependencies", {})
    original_dependencies["__main__"] = project.get("dependencies", {})
    project["dependencies"] = unpin_upper_bound_in_dependencies(
        project.get("dependencies", {}),
    )
    optional_dependencies = project.get("optional-dependencies", {})
    for optional_name, optional_deps in optional_dependencies.items():
        original_dependencies[optional_name] = optional_deps
        optional_dependencies[optional_name] = unpin_upper_bound_in_dependencies(
            optional_deps,
        )
    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


def pin_upper_bound_in_dependencies(
    package_name: str,
    dependencies: list[str],
    original_dependencies: list[str],
    versions: dict[str, str],
) -> tuple[list[str], bool]:
    """Replace unpinned versions with range-pinned versions.

    Returns a tuple of the pinned dependencies and a boolean indicating whether
    a major version bump is needed (the pinned dependencies differ from the original in the major version).
    """
    deps = []
    major_version_needed = False
    dependencies_by_name: dict[str, Requirement] = {r.name: r for r in map(Requirement, original_dependencies)}
    original_dependencies_by_name: dict[str, Requirement] = {r.name: r for r in map(Requirement, original_dependencies)}
    for dep_name, r in dependencies_by_name.items():
        if r.name not in versions:
            deps.append(str(r))
            continue
        original_r = original_dependencies_by_name[dep_name]
        if "invenio" not in r.name:
            deps.append(str(original_r))
            continue

        lower_bound = versions[r.name]
        if "+" in lower_bound:
            lower_bound = lower_bound.split("+")[0]
        upper_bound = f"{(1 + int(lower_bound.split('.', maxsplit=1)[0]))}.0.0"
        deps.append(f"{r.name}>={lower_bound},<{upper_bound}")
        if not original_r.specifier.contains(lower_bound):
            rich_print(
                f"  ⬆️  {package_name} needs upgrade: {dep_name}"
                f" with specifier{original_r.specifier} (bumped to {lower_bound})"
            )
            major_version_needed = True
    return deps, major_version_needed


def unpin_upper_bound_in_dependencies(dependencies: list[str]) -> list[str]:
    """Unpin upper bounds in dependency version specifiers (remove <abc)."""
    deps = []
    for dep in dependencies:
        r = Requirement(dep)
        filtered_specifiers = [s for s in r.specifier if not s.operator.startswith("<")]
        deps.append(
            _rebuild_requirement(
                r,
                str(SpecifierSet(filtered_specifiers, prereleases=r.specifier.prereleases)),
            )
        )
    return deps


def update_pyproject_source_map(pyproject_path: Path, oarepo_packages_to_path: dict[str, Path]):
    """Update the source map in pyproject.toml for OARepo packages."""
    data = tomllib.loads(pyproject_path.read_text())
    # update the tool.uv.sources
    sources = data.setdefault("tool", {}).setdefault("uv", {}).setdefault("sources", {})
    for oarepo_name, path in oarepo_packages_to_path.items():
        sources[oarepo_name] = {
            "path": str(path),
            "editable": True,
        }
    data["tool"]["uv"]["sources"] = sources
    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


def delete_pyproject_source_map(pyproject_path, oarepo_packages_to_path: dict[str, Path]):
    """Delete the source map in pyproject.toml for OARepo packages."""
    data = tomllib.loads(pyproject_path.read_text())
    sources = data.setdefault("tool", {}).setdefault("uv", {}).setdefault("sources", {})
    for oarepo_name in oarepo_packages_to_path:
        sources.pop(oarepo_name, None)
    data["tool"]["uv"]["sources"] = sources
    pyproject_path.write_bytes(tomli_w.dumps(data).encode())


def propagate_resolved_versions(
    oarepo_packages_to_path: dict[str, Path], resolved: dict[str, str]
) -> dict[str, tuple[str, bool]]:
    """Propagate resolved versions from uv.lock to pyproject.toml for OARepo packages.

    Returns a dict of package names -> (original version, major_bump_needed) that need a major bump
    due to version conflicts.
    Note that this list is not exhaustive - it only includes packages that have direct version
    conflicts, but not transitive ones.
    """
    packages_with_major_bump_needed = {}
    for package_name, package_path in oarepo_packages_to_path.items():
        pyproject_path = package_path / "pyproject.toml"
        data = tomllib.loads(pyproject_path.read_text())
        project = data.get("project", {})
        tool = data.setdefault("tool", {})
        oarepo_tool = tool.setdefault("oarepo", {})
        current_version = project.get("version", "0.0.0")
        original_version = oarepo_tool.get("original_version", None)
        original_dependencies = oarepo_tool.setdefault("original-dependencies", {})

        need_major_bump = (
            original_version is not None and original_version.split(".")[0] != current_version.split(".")[0]
        )

        project["dependencies"], dependencies_need_major_bump = pin_upper_bound_in_dependencies(
            package_name,
            project.get("dependencies", {}),
            original_dependencies["__main__"],
            resolved,
        )
        need_major_bump = need_major_bump or dependencies_need_major_bump
        optional_dependencies = project.get("optional-dependencies", {})
        for optional_name, optional_deps in optional_dependencies.items():
            optional_dependencies[optional_name], optional_need_major_bump = pin_upper_bound_in_dependencies(
                package_name,
                optional_deps,
                original_dependencies.get(optional_name, None),
                resolved,
            )
            need_major_bump = need_major_bump or optional_need_major_bump
        pyproject_path.write_bytes(tomli_w.dumps(data).encode())
        if need_major_bump:
            if original_version is None:
                bumped_version = f"{1 + int(current_version.split('.', 1)[0])}.0.0"
                packages_with_major_bump_needed[package_name] = (bumped_version, True)
            else:
                bumped_version = original_version
                packages_with_major_bump_needed[package_name] = (bumped_version, False)
    return packages_with_major_bump_needed


# ─── update_versions ─────────────────────────────────────────────────────────


def update_versions(
    directory: Path,
    upgrade_major_versions: bool,
    upgraded_packages: list[str] | None = None,
) -> dict[str, tuple[str, bool]]:
    """Update pinned dependency versions in *directory*/pyproject.toml.

    Steps:
    1. Remove the production section from pyproject.toml.
    2. Run ``uv lock`` to produce an updated lock file.
    3. Read the resolved versions from ``uv.lock`` and pin each matching
       dependency inside the "production" section of pyproject.toml to ``==<resolved>``.
    4. If a dependency is in development dependencies but not in the "production" section,
       add it to the "production" section.
    5. Return a dict of packages that were either already bumped (were part of upgraded_packages)
       or need a major bump due to version conflicts.
       The dict contains both upgraded_packages and packages that have version conflicts
       with invenio packages. The value is a tuple of the "bumped" version and a boolean
       indicating whether the package needs to be bumped (True) or was already bumped (False).
    """
    upgraded_packages = upgraded_packages or []
    root = directory.resolve()
    lock_path = root / "uv.lock"
    pyproject_path = root / "pyproject.toml"
    local_packages_dir = root / ".local-packages"

    # ── Step 1: remove production section ─────────────────────────────────────
    rich_print("[bold blue]Step 1/3[/bold blue] 🗑️  Removing production section from pyproject.toml …")
    remove_production_section(pyproject_path)

    if upgrade_major_versions:
        unpin_development_major_versions(pyproject_path)
        # map from package name to (github_repo, github_branch)
        oarepo_packages_map = extract_oarepo_packages(pyproject_path)
        oarepo_packages_to_path = clone_oarepo_packages(local_packages_dir, oarepo_packages_map, upgraded_packages)
        for path in oarepo_packages_to_path.values():
            unpin_versions_in_oarepo_packages(path)
        update_pyproject_source_map(pyproject_path, oarepo_packages_to_path)

    # Print the updated pyproject.toml
    rich_print("  [dim]↳[/dim] ✅ updated [cyan]pyproject.toml[/cyan]")
    rich_print(pyproject_path.read_text())

    # ── Step 2: uv lock ──────────────────────────────────────────────────────
    rich_print("[bold blue]Step 2/3[/bold blue] 🔒 Running [cyan]uv lock[/cyan] …")
    run_uv_lock(root)

    # ── Step 3: pin to resolved versions ────────────────────────────────────
    rich_print("[bold blue]Step 3/3[/bold blue] 📌 Pinning to resolved versions …")

    resolved = parse_uv_lock(lock_path)
    if pin_pyproject_deps(pyproject_path, resolved):
        rich_print("  [dim]↳[/dim] 📌 [green]pinned[/green] pyproject.toml")

    pin_development_major_versions(pyproject_path, resolved)
    upgraded_packages_with_versions: dict[str, tuple[str, bool]] = {}
    if upgrade_major_versions:
        upgraded_packages_with_versions = propagate_resolved_versions(oarepo_packages_to_path, resolved)
        # ── Cleanup: remove the temporary local-path source overrides ──────
        delete_pyproject_source_map(pyproject_path, oarepo_packages_to_path)
    rich_print("🎉 [bold green]Done.[/bold green]")
    return upgraded_packages_with_versions


def get_latest_oarepo_version(major_version: int) -> str:
    versions: list[Version] = get_available_versions("oarepo")

    candidates = [v for v in versions if v.major == major_version]

    if not candidates:
        raise ValueError(f"No oarepo releases found for major version {major_version}.")

    return str(max(candidates))
