"""CHANGELOG.json management."""

from __future__ import annotations

import json
import re
import subprocess
import time
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


# ─── subprocess retrying ──────────────────────────────────────────────────────

_RETRY_DELAYS: tuple[int, ...] = (5, 30, 60)


def call_with_retries(
    cmd: list[str],
    *,
    retry_delays: tuple[int, ...] = _RETRY_DELAYS,
    **kwargs,
) -> subprocess.CompletedProcess:
    """Run *cmd* via :func:`subprocess.run`, retrying on timeout or non-zero exit.

    Waits *retry_delays* seconds between successive attempts.  On each failed
    attempt a warning is printed.  Only after the final attempt is an error
    surfaced:

    * :class:`subprocess.TimeoutExpired` – re-raised after the last timed-out attempt.
    * A :class:`subprocess.CompletedProcess` with a non-zero ``returncode`` –
      returned to the caller so it can raise or handle as appropriate.

    :exc:`FileNotFoundError` (binary not found) is **not** retried and
    propagates immediately.
    """
    last_result: subprocess.CompletedProcess | None = None
    last_timeout: subprocess.TimeoutExpired | None = None

    for attempt, pre_delay in enumerate([0, *retry_delays]):
        if pre_delay:
            print(f"  [dim]↳[/dim] ⏳ retrying in [yellow]{pre_delay}s[/yellow] …")
            time.sleep(pre_delay)

        try:
            result = subprocess.run(cmd, **kwargs)
        except subprocess.TimeoutExpired as exc:
            last_timeout = exc
            last_result = None
            print(f"  [dim]↳[/dim] ⚠️  attempt {attempt + 1} timed out")
            continue

        last_timeout = None
        last_result = result

        if result.returncode == 0:
            return result

        print(
            f"  [dim]↳[/dim] ⚠️  attempt {attempt + 1} failed (exit {result.returncode})"
        )

    if last_timeout is not None:
        raise last_timeout
    assert last_result is not None
    return last_result


# ─── tag reading ─────────────────────────────────────────────────────────────

# In-process cache so repeated calls for the same repo cost only one round-trip.
_tag_cache: dict[tuple[str, str], dict[Version, str]] = {}


def _normalise_tag(tag: str) -> Version | None:
    """Convert a raw git tag string to a :class:`Version`, or ``None`` if unparseable.

    Normalisation steps applied before parsing:

    1. Strip a leading ``v`` or ``V``.
    2. Lowercase the remainder.
    """
    normalised = tag.lower().lstrip("v")
    try:
        return Version(normalised)
    except InvalidVersion:
        return None


def read_tags(github_organization: str, github_repo: str) -> dict[Version, str]:
    """Return a mapping of normalised version → original tag name for *github_organization*/*github_repo*.

    Uses ``gh api --paginate`` so the full tag list is returned regardless of
    how many pages the repository has.  Results are cached in-process so that
    multiple packages from the same organisation share a single API call.

    When multiple raw tags normalise to the same :class:`Version` the longest
    original tag string wins (e.g. ``v1.2.3`` is preferred over ``1.2.3``).
    Tags that cannot be parsed as a PEP 440 version are silently ignored.
    """
    cache_key = (github_organization, github_repo)
    if cache_key in _tag_cache:
        return _tag_cache[cache_key]

    try:
        result = subprocess.run(
            [
                "gh",
                "api",
                "--paginate",
                f"repos/{github_organization}/{github_repo}/tags",
                "--jq",
                ".[].name",
            ],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except FileNotFoundError:
        print(
            f"  [dim]↳[/dim] ⚠️  [yellow]gh[/yellow] CLI not found — "
            f"cannot read tags for [cyan]{github_repo}[/cyan]"
        )
        _tag_cache[cache_key] = {}
        return {}
    except subprocess.TimeoutExpired:
        print(
            f"  [dim]↳[/dim] ⚠️  gh CLI timed out reading tags for [cyan]{github_repo}[/cyan]"
        )
        _tag_cache[cache_key] = {}
        return {}

    if result.returncode != 0:
        print(
            f"  [dim]↳[/dim] ⚠️  failed to read tags for [cyan]{github_repo}[/cyan]: "
            f"{result.stderr.strip()}"
        )
        _tag_cache[cache_key] = {}
        return {}

    mapping: dict[Version, str] = {}
    for raw_tag in result.stdout.splitlines():
        raw_tag = raw_tag.strip()
        if not raw_tag:
            continue
        version = _normalise_tag(raw_tag)
        if version is None:
            continue
        # Keep the longest original tag string when two tags share a Version.
        if version not in mapping or len(raw_tag) > len(mapping[version]):
            mapping[version] = raw_tag

    _tag_cache[cache_key] = mapping
    return mapping


def find_tag(desired_tag: str, all_tags: dict[Version, str]) -> str | None:
    """Return the actual repository tag that matches *desired_tag*.

    *desired_tag* is normalised with :func:`_normalise_tag` and looked up in
    *all_tags*.  Returns *desired_tag* unchanged when no match is found, which
    lets the caller's API call fail gracefully.
    """
    version = _normalise_tag(desired_tag)
    if version is None:
        return None
    return all_tags.get(version, desired_tag)


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

    all_tags = read_tags(github_organization, github_repo)

    previous_tag = find_tag(previous_tag, all_tags)
    current_tag = find_tag(current_tag, all_tags)

    if previous_tag == current_tag:
        return []

    if previous_tag is None:
        print(
            f"  [dim]↳[/dim] ⚠️  [yellow]gh[/yellow] {previous_tag} not found in repository {github_repo} — skipping commits for [cyan]{name}[/cyan]"
        )
        return []

    if current_tag is None:
        print(
            f"  [dim]↳[/dim] ⚠️  [yellow]gh[/yellow] {current_tag} not found in repository {github_repo} — skipping commits for [cyan]{name}[/cyan]"
        )
        return []

    try:
        result = call_with_retries(
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
            f"([dim]{previous_tag}…{current_tag}[/dim]): {result.stderr.strip()}\n"
            f"gh api repos/{github_organization}/{github_repo}/compare/{previous_tag}...{current_tag}",
        )
        raise subprocess.CalledProcessError(
            result.returncode, result.args, result.stdout, result.stderr
        )

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

        # do not log changes for oarepo-app neither for oarepo-invenio-typing-stubs
        if name in ("oarepo-app", "oarepo-invenio-typing-stubs"):
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
        "version": "unknown",
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


def render_changelog_md(changelog: list, directory: Path) -> None:
    """Render *changelog* to CHANGELOG.md using the bundled Jinja2 template."""
    from jinja2 import Environment, FileSystemLoader

    template_dir = Path(__file__).parent / "templates"

    def _format_datetime(iso_str: str) -> str:
        try:
            dt = datetime.fromisoformat(iso_str)
            return dt.strftime(f"%B {dt.day}, %Y at %H:%M UTC")
        except ValueError, TypeError:
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


def get_two_latest_log_entries(changelog_path: Path) -> tuple[dict, dict | None]:
    """
    Returns the latest and the second latest entries from the changelog.
    The first entry is the latest, the second is the second latest.
    """
    changelog = _read_changelog(changelog_path)
    if len(changelog) >= 2:
        return tuple(changelog[:2])
    return changelog[0], None


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
