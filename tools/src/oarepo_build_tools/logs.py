"""CHANGELOG.json management."""

from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from packaging.version import InvalidVersion, Version
from rich import print

from oarepo_build_tools.constants import LOG_PACKAGES
from oarepo_build_tools.python import parse_uv_lock

_CHANGELOG_FILENAME = "CHANGELOG.json"


# ─── filtering ────────────────────────────────────────────────────────────────


def _matches_log_group(normalised_name: str) -> dict | None:
    """Return the first LOG_PACKAGES group whose patterns match *normalised_name*.

    Returns None if no group matches.
    """
    for group in LOG_PACKAGES:
        includes: list[str] = group.get("include", [])
        excludes: list[str] = group.get("exclude", [])
        if includes and not any(re.search(p, normalised_name) for p in includes):
            continue
        if any(re.search(p, normalised_name) for p in excludes):
            continue
        return group
    return None


def _collect_logged_packages(all_packages: dict[str, str]) -> dict[str, dict]:
    """Filter *all_packages* through LOG_PACKAGES and apply each group's version mapper.

    Returns {package_name: {"version": mapped_version, "breaking": False, "changes": []}}.
    Commits are left empty and will be filled in by a later step.
    """
    result: dict[str, dict] = {}
    for name, version in all_packages.items():
        group = _matches_log_group(name)
        if group is None:
            continue
        result[name] = {"version": version, "breaking": False, "changes": []}
    return result


# ─── breaking-change detection ───────────────────────────────────────────────


def _major_version(version_str: str) -> int | None:
    """Return the major version number from *version_str*, or None if unparseable."""
    try:
        return Version(version_str).major
    except InvalidVersion:
        return None


def _detect_breaking_changes(entry: dict, previous_entry: dict | None) -> None:
    """Mutate *entry* in place, marking packages and the entry as breaking.

    A package is considered breaking when its major version is higher than in
    *previous_entry*.  If any package is breaking the top-level entry flag is
    also set to True.  When there is no previous entry nothing is marked.
    """
    if previous_entry is None:
        return

    previous_packages: dict[str, dict] = previous_entry.get("packages", {})

    for name, pkg in entry["packages"].items():
        prev_pkg = previous_packages.get(name)
        if prev_pkg is None:
            continue  # new package — not a breaking change by definition

        new_major = _major_version(pkg["version"])
        old_major = _major_version(prev_pkg["version"])
        pkg["previous_version"] = prev_pkg["version"]

        if new_major is None or old_major is None:
            continue  # unparseable version — skip

        if new_major > old_major:
            pkg["breaking"] = True
            entry["breaking"] = True


# ─── commit fetching ──────────────────────────────────────────────────────────


def _fetch_package_changes(name: str, pkg: dict, group: dict) -> list[dict]:
    """Fetch commits between the previous and current version tags for *pkg*.

    Uses the ``gh`` CLI to call the GitHub compare API.  Returns a list of
    ``{"commit": sha, "message": first_line}`` dicts sorted by committer date
    descending.  Returns ``[]`` when there is no previous version, the tags are
    identical, or any error occurs.
    """
    previous_version: str | None = pkg.get("previous_version")
    if previous_version is None:
        return []

    current_version: str = pkg["version"]
    version_tag = group["version_tag"]
    github_organization: str = group["github_organization"]
    github_repo: str = group["github_repo"](name)

    previous_tag = version_tag(previous_version)
    current_tag = version_tag(current_version)

    if previous_tag == current_tag:
        return []

    try:
        result = subprocess.run(
            [
                "gh",
                "api",
                f"repos/{github_organization}/{github_repo}/compare/{previous_tag}...{current_tag}",
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except FileNotFoundError:
        print(
            f"  [dim]↳[/dim] ⚠️  [yellow]gh[/yellow] CLI not found — skipping commits for [cyan]{name}[/cyan]"
        )
        return []
    except subprocess.TimeoutExpired:
        print(f"  [dim]↳[/dim] ⚠️  gh CLI timed out for [cyan]{name}[/cyan]")
        return []

    if result.returncode != 0:
        print(
            f"  [dim]↳[/dim] ⚠️  compare failed for [cyan]{name}[/cyan] "
            f"([dim]{previous_tag}…{current_tag}[/dim]): {result.stderr.strip()}"
        )
        return []

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        print(f"  [dim]↳[/dim] ⚠️  JSON parse error for [cyan]{name}[/cyan]: {exc}")
        return []

    raw_commits = data.get("commits", [])

    commits_with_dates = [
        {
            "sha": c.get("sha", ""),
            "message": c.get("commit", {}).get("message", ""),
            "date": c.get("commit", {}).get("committer", {}).get("date", ""),
        }
        for c in raw_commits
    ]

    # Sort by committer date descending (ISO-8601 strings sort lexicographically)
    commits_with_dates.sort(key=lambda c: c["date"], reverse=True)

    return [
        {
            "commit": c["sha"],
            "message": c["message"].split("\n")[0],
        }
        for c in commits_with_dates
    ]


def _populate_all_changes(entry: dict) -> None:
    """Populate the ``changes`` list and ``github_url`` for every package in *entry* in place.

    Calls ``_fetch_package_changes`` for each package that has a
    ``previous_version`` set (i.e. after ``_detect_breaking_changes`` has run).
    Also sets ``github_url`` to the GitHub compare UI link between the two versions.
    """
    for name, pkg in entry["packages"].items():
        group = _matches_log_group(name)
        if group is None:
            continue

        previous_version: str | None = pkg.get("previous_version")
        if previous_version is not None:
            version_tag = group["version_tag"]
            github_organization: str = group["github_organization"]
            github_repo: str = group["github_repo"](name)
            previous_tag = version_tag(previous_version)
            current_tag = version_tag(pkg["version"])
            pkg["github_url"] = (
                f"https://github.com/{github_organization}/{github_repo}"
                f"/compare/{previous_tag}...{current_tag}"
            )

        changes = _fetch_package_changes(name, pkg, group)
        pkg["changes"] = changes
        if changes:
            print(f"  [dim]↳[/dim] [cyan]{name}[/cyan]: {len(changes)} commit(s)")


# ─── entry building ───────────────────────────────────────────────────────────


def _build_entry(oarepo_version: str, packages: dict[str, dict]) -> dict:
    """Assemble a single CHANGELOG entry dict."""
    return {
        "version": oarepo_version,
        "breaking": False,
        "packages": packages,
    }


# ─── CHANGELOG.json I/O ───────────────────────────────────────────────────────


def _read_changelog(path: Path) -> list:
    """Read an existing CHANGELOG.json and return its parsed list, or [] if absent."""
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def _write_changelog(path: Path, changelog: list) -> None:
    """Serialise *changelog* to *path* as pretty-printed JSON."""
    path.write_text(
        json.dumps(changelog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ─── markdown rendering ───────────────────────────────────────────────────────


def _render_changelog_md(changelog: list, directory: Path) -> None:
    """Render *changelog* to CHANGELOG.md using the bundled Jinja2 template."""
    from jinja2 import Environment, FileSystemLoader

    template_dir = Path(__file__).parent

    def _format_datetime(iso_str: str) -> str:
        try:
            dt = datetime.fromisoformat(iso_str)
            return dt.strftime(f"%B {dt.day}, %Y at %H:%M UTC")
        except (ValueError, TypeError):
            return iso_str

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    def _github_anchor(text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"\s+", "-", text)
        return text

    env.filters["format_datetime"] = _format_datetime
    env.filters["github_anchor"] = _github_anchor

    template = env.get_template("CHANGELOG.md.jinja")
    md_path = directory / "CHANGELOG.md"
    md_path.write_text(template.render(changelog=changelog), encoding="utf-8")


# ─── public API ───────────────────────────────────────────────────────────────


def create_log_entry(directory: Path) -> None:
    """Append a new entry to CHANGELOG.json for the current state of *directory*/uv.lock.

    Packages are filtered through LOG_PACKAGES; the ``changes`` list for each
    package is left empty — commits will be populated in a later step.
    """
    lock_path = directory / "uv.lock"
    changelog_path = directory / _CHANGELOG_FILENAME

    print("[bold blue]📋[/bold blue] Creating log entry …")

    all_packages = parse_uv_lock(lock_path)
    oarepo_version = all_packages.get("oarepo", "unknown")
    print(f"  [dim]↳[/dim] oarepo version: [bold green]{oarepo_version}[/bold green]")

    packages = _collect_logged_packages(all_packages)
    print(f"  [dim]↳[/dim] {len(packages)} packages matched LOG_PACKAGES")

    entry = _build_entry(oarepo_version, packages)
    entry["created"] = datetime.now(timezone.utc).isoformat()

    changelog = _read_changelog(changelog_path)
    previous_entry = changelog[0] if changelog else None
    _detect_breaking_changes(entry, previous_entry)

    print("[bold blue]🔍[/bold blue] Fetching commit logs …")
    _populate_all_changes(entry)

    breaking_packages = [n for n, p in entry["packages"].items() if p.get("breaking")]
    if breaking_packages:
        print(
            f"  [dim]↳[/dim] 💥 [bold red]breaking[/bold red]: {', '.join(breaking_packages)}"
        )

    changelog.insert(0, entry)
    _write_changelog(changelog_path, changelog)
    print(
        f"  [dim]↳[/dim] ✅ written to [cyan]{changelog_path.relative_to(directory)}[/cyan]"
    )

    print("[bold blue]📝[/bold blue] Rendering CHANGELOG.md …")
    _render_changelog_md(changelog, directory)
    print("  [dim]↳[/dim] ✅ written to [cyan]CHANGELOG.md[/cyan]")
