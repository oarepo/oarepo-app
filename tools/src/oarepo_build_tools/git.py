import re
import subprocess
from pathlib import Path


def sanitize_branch_name(name: str) -> str:
    """
    Produce a valid git branch name from an arbitrary string.

    PEP 440 version strings can contain characters such as '+' (local version
    separator) that are not universally safe in branch names or shell contexts.
    Replace them – and any other non-alphanumeric characters except '-' and '.'
    – with '-', then collapse runs of dashes.
    """
    result = re.sub(r"[^a-zA-Z0-9.\-]", "-", name)
    result = re.sub(r"-{2,}", "-", result)
    return result.strip("-")


def switch_branch(directory: str | Path, branch_name: str) -> str:
    """
    Switch to *branch_name* inside *directory*, creating the branch if needed.

    The branch name is sanitised first so that characters such as '+' (common
    in PEP 440 version strings) are replaced with '-'.
    """
    directory = Path(directory)
    safe_name = sanitize_branch_name(branch_name)

    # Check whether the branch already exists locally.
    result = subprocess.run(
        ["git", "branch", "--list", safe_name],
        cwd=directory,
        capture_output=True,
        text=True,
        check=True,
    )

    if result.stdout.strip():
        # Branch exists – just check it out.
        subprocess.run(
            ["git", "checkout", safe_name],
            cwd=directory,
            check=True,
        )
    else:
        # Create the branch and switch to it.
        subprocess.run(
            ["git", "checkout", "-b", safe_name],
            cwd=directory,
            check=True,
        )

    return safe_name
