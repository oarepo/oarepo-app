#!/usr/bin/env python3
"""Helper script for extracting package dependencies.

This script is called by dependency_tree.py to analyze package dependencies
using importlib.metadata. It reads a dict of package names and versions from
stdin and outputs dependency information as JSON.
"""

import json
import sys
from importlib.metadata import metadata

from packaging.requirements import Requirement


def should_exclude_extra(extra_name):
    """Check if an extra should be excluded from dependency analysis.

    Args:
        extra_name: Name of the extra dependency group

    Returns:
        True if the extra should be excluded
    """
    excluded_prefixes = ("elasticsearch", "sqlite", "mysql")
    return any(extra_name.lower().startswith(prefix) for prefix in excluded_prefixes)


def parse_requirement(requirement):
    """Parse a requirement string to extract package name and version specifiers.

    Args:
        requirement: Requirement string like "package[extra]>=1.0,<2.0; extra=='tests'"

    Returns:
        Tuple of (package_name, version_specifiers)
        Example: ("oarepo-app", ">=1.0,<2.0")
    """
    try:
        req = Requirement(requirement)
        pkg_name = req.name.lower()
        version_spec = str(req.specifier) if req.specifier else ""
        return pkg_name, version_spec
    except Exception:
        return "", ""


def main():
    """Main function to process package dependencies."""
    # Read package info from stdin (dict of package name -> version)
    packages_input = json.load(sys.stdin)
    result = {}

    for pkg_name, pkg_version in packages_input.items():
        try:
            m = metadata(pkg_name)
            reqs = m.get_all("Requires-Dist") or []

            # Use dict to track version specs per package and combine them
            dependencies_dict = {}
            for req in reqs:
                if not req.strip():
                    continue

                # Use Requirement.marker to detect extras instead of regex
                try:
                    req_obj = Requirement(req)
                    # Check if this requirement has a marker with an extra condition
                    if req_obj.marker:
                        marker_str = str(req_obj.marker)
                        if "extra" in marker_str.lower():
                            # Extract extra name from marker and check if should exclude
                            # Markers like: extra == "tests" or extra == 'dev'
                            for excluded_prefix in ("elasticsearch", "sqlite", "mysql"):
                                if excluded_prefix in marker_str.lower():
                                    req_obj = None
                                    break
                            if req_obj is None:
                                continue
                except Exception:
                    # If we can't parse, skip this requirement
                    continue

                pkg_name_parsed, version_spec = parse_requirement(req)
                if pkg_name_parsed:
                    # Combine version specs for the same package
                    if pkg_name_parsed not in dependencies_dict:
                        dependencies_dict[pkg_name_parsed] = version_spec
                    elif version_spec:
                        # Append version spec if it's not already there
                        existing = dependencies_dict[pkg_name_parsed]
                        if version_spec not in existing:
                            dependencies_dict[pkg_name_parsed] = (
                                existing + "," + version_spec
                                if existing
                                else version_spec
                            )

            # Format as list of "package>=1.0,<2.0" strings
            dependencies = [
                f"{pkg}{spec}" if spec else pkg
                for pkg, spec in sorted(dependencies_dict.items())
            ]

            result[pkg_name] = {
                "version": pkg_version,
                "dependencies": dependencies,
            }
        except Exception as e:
            result[pkg_name] = {"version": pkg_version, "dependencies": []}

    print(json.dumps(result))


if __name__ == "__main__":
    main()
