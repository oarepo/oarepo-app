from pathlib import Path

import typer
from packaging.version import Version
from rich import print

from oarepo_build_tools.constants import (
    OAREPO_EXCLUDED_PACKAGES,
    OAREPO_INCLUDED_PACKAGES,
)
from oarepo_build_tools.git import switch_branch
from oarepo_build_tools.logs import create_log_entry
from oarepo_build_tools.python import (
    get_available_versions,
    get_oarepo_app_version,
    set_pyproject_version,
    update_versions,
)
from oarepo_build_tools.upload_old_packages import upload_old_packages

app = typer.Typer()


@app.callback()
def callback() -> None:
    """oarepo-app build tools."""


def get_latest_oarepo_version(major_version: int) -> str:
    versions: list[Version] = get_available_versions("oarepo")

    candidates = [v for v in versions if v.major == major_version]

    if not candidates:
        print(
            f"[bold red]✗[/bold red] No oarepo releases found for major version [cyan]{major_version}[/cyan]."
        )
        raise typer.Exit(1)

    return str(max(candidates))


@app.command()
def setup(
    major_version: int = typer.Argument(
        default=14,
        help="Major version of oarepo (corresponds to the InvenioRDM major version).",
    ),
    directory: str = typer.Option(
        ".",
        help="Repository directory to operate in.",
    ),
) -> None:
    """Set up the repository for the given oarepo major version."""
    print(
        f"🔍 Searching for latest [bold]oarepo[/bold] [cyan]{major_version}.x[/cyan] release …"
    )
    latest_oarepo_version = get_latest_oarepo_version(major_version)
    print(f"📦 Latest version: [bold green]{latest_oarepo_version}[/bold green]")

    root = Path(directory).resolve()
    print(f"🌿 Switching to branch [cyan]temporary-{latest_oarepo_version}[/cyan] …")
    switch_branch(root, f"temporary-{latest_oarepo_version}")
    print("🔄 Updating dependency versions …")
    update_versions(
        root, OAREPO_INCLUDED_PACKAGES, OAREPO_EXCLUDED_PACKAGES, latest_oarepo_version
    )
    create_log_entry(root)

    print("🏷️  Computing [bold]oarepo-app[/bold] version …")
    oarepo_app_version = get_oarepo_app_version(latest_oarepo_version)
    print(f"  [dim]↳[/dim] version: [bold green]{oarepo_app_version}[/bold green]")
    set_pyproject_version(root / "pyproject.toml", oarepo_app_version)
    print("  [dim]↳[/dim] ✅ updated [cyan]pyproject.toml[/cyan]")


app.command()(upload_old_packages)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
