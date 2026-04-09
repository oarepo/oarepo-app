"""Build dependency tree of packages.

Note: this command modifies the local repository!
"""

import hashlib
import json
import re
import subprocess
from graphlib import TopologicalSorter
from pathlib import Path

import typer
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.version import Version
from rich import print

from oarepo_build_tools.git import switch_branch
from oarepo_build_tools.python import (
    get_latest_oarepo_version,
)

# Constants for dependency graph generation
DEPGRAPH_INITIAL_NODES_REGEXP = r"^oarepo-.*"
DEPGRAPH_EXCLUDE_NODES_REGEXP = r"^oarepo-invenio-typing-stubs"
DEPGRAPH_FILTER_REGEXP = [
    (r"^oarepo-.*", r"^oarepo-.*"),
    (r"^oarepo-.*", r"^invenio-.*"),
]
DEPGRAPH_STYLE = {
    r"^oarepo-.*": "#90EE90",  # light green
    r"^invenio-.*": "#D3D3D3",  # light gray
}


def clamp(value: int, min_val: int = 0, max_val: int = 255) -> int:
    """Clamp a value between min and max."""
    return max(min_val, min(max_val, value))


def perturb_color(base_color_hex: str, package_name: str) -> str:
    """Perturb a base color using MD5 hash of package name.

    Args:
        base_color_hex: Base color in hex format (e.g., "#90EE90")
        package_name: Package name to use for perturbation

    Returns:
        Perturbed color in hex format
    """
    # Parse base color
    # Remove '#' if present
    base_color = base_color_hex.lstrip("#")

    # Parse base color to RGB
    r = int(base_color[0:2], 16)
    g = int(base_color[2:4], 16)
    b = int(base_color[4:6], 16)

    # Get MD5 hash of package name
    hash_bytes = hashlib.md5(package_name.encode()).digest()

    # Use first 3 bytes to perturb RGB values
    # Each byte / 4 - 32 gives range of approximately -32 to +31
    r_offset = (hash_bytes[0] // 4) - 32
    g_offset = (hash_bytes[1] // 4) - 32
    b_offset = (hash_bytes[2] // 4) - 32

    # Apply perturbations and clamp
    r_new = clamp(r + r_offset)
    g_new = clamp(g + g_offset)
    b_new = clamp(b + b_offset)

    # Convert back to hex
    return f"#{r_new:02x}{g_new:02x}{b_new:02x}"


def get_node_color(node_name: str, compiled_styles: list[tuple]) -> str:
    """Get perturbed color for a node based on style patterns.

    Args:
        node_name: Name of the node
        compiled_styles: List of (compiled_regex, base_color_hex) tuples

    Returns:
        Color in hex format (perturbed if match found, white otherwise)
    """
    # Find matching style
    for pattern, base_color in compiled_styles:
        if pattern.match(node_name):
            return perturb_color(base_color, node_name)

    # Default to white if no match
    return "#FFFFFF"


def find_cycles(nodes: set, edges: list[tuple]) -> tuple[set[str], list[list[str]]]:
    """Find all cycles in the dependency graph using standard library.

    Args:
        nodes: Set of all nodes
        edges: List of (src, dst) tuples

    Returns:
        Tuple of (nodes_in_cycles, list_of_cycles)
        where each cycle is a list of node names forming the cycle
    """
    # Build adjacency map
    graph = {}
    for node in nodes:
        graph[node] = []
    for src, dst in edges:
        if src in graph:
            graph[src].append(dst)
        else:
            graph[src] = [dst]

    # Try topological sort to detect cycles
    try:
        ts = TopologicalSorter(graph)
        ts.prepare()
        # No cycles if this succeeds
        return set(), []
    except Exception:
        # Cycles exist, find them using DFS
        pass

    # DFS to find cycles
    def find_all_cycles_dfs():
        cycles = []
        visited = set()
        rec_stack = []
        rec_stack_set = set()

        def dfs(node):
            if node in rec_stack_set:
                # Found a cycle
                cycle_start = rec_stack.index(node)
                cycle = rec_stack[cycle_start:]
                cycles.append(cycle[:])
                return

            if node in visited:
                return

            visited.add(node)
            rec_stack.append(node)
            rec_stack_set.add(node)

            for neighbor in graph.get(node, []):
                dfs(neighbor)

            rec_stack.pop()
            rec_stack_set.remove(node)

        for node in nodes:
            if node not in visited:
                dfs(node)

        return cycles

    all_cycles = find_all_cycles_dfs()

    # Get all nodes that are part of any cycle
    nodes_in_cycles = set()
    for cycle in all_cycles:
        nodes_in_cycles.update(cycle)

    # Sort cycles by length (smallest first)
    all_cycles.sort(key=len)

    return nodes_in_cycles, all_cycles


def get_all_package_dependencies(
    packages: dict[str, str], python_path: str
) -> dict[str, dict]:
    """Get all dependencies for all packages in a single call.

    Args:
        packages: Dict mapping package names to versions
        python_path: Path to Python interpreter

    Returns:
        Dict mapping package names to their version and dependencies
        Example: {"package": {"version": "1.2.3", "dependencies": ["oarepo-app>=1.0.0,<2.0.0"]}}
    """
    try:
        # Get the path to the helper script
        helper_script = Path(__file__).parent / "dependency_tree_helper.py"

        # Pass package dict via stdin
        packages_json = json.dumps(packages)
        result = subprocess.run(
            [python_path, str(helper_script)],
            input=packages_json,
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            print("Error analyzing dependencies:")
            print(f"STDERR: {result.stderr}")
            print(f"STDOUT: {result.stdout}")
            return {}

        return json.loads(result.stdout) if result.stdout.strip() else {}
    except Exception as e:
        print(f"Exception analyzing dependencies: {e}")
        return {}


def build_dot_dependency_graph(
    packages: dict[str, dict],
    initial_nodes_pattern: str = DEPGRAPH_INITIAL_NODES_REGEXP,
    exclude_nodes_pattern: str = DEPGRAPH_EXCLUDE_NODES_REGEXP,
    filter_patterns: list[tuple[str, str]] = DEPGRAPH_FILTER_REGEXP,
    style_patterns: dict[str, str] = DEPGRAPH_STYLE,
    explicit_initial_nodes: set[str] | None = None,
) -> str:
    """Build a DOT format dependency digraph.

    Args:
        packages: Dict mapping package names to their dependencies structure
        initial_nodes_pattern: Regex pattern for initial nodes to include (e.g., "^oarepo")
        exclude_nodes_pattern: Regex pattern for nodes to exclude completely (e.g., "^oarepo-invenio-typing-stubs")
        filter_patterns: List of tuples (package_pattern, dependency_pattern) to filter edges.
                        An edge is included if package matches first pattern and dependency matches second.
        style_patterns: Dict mapping regex patterns to DOT style attributes for nodes
        explicit_initial_nodes: If provided, use these specific nodes as starting points instead of pattern matching

    Returns:
        DOT format string representing the dependency graph
    """
    initial_pattern = re.compile(initial_nodes_pattern, re.IGNORECASE)
    exclude_pattern = re.compile(exclude_nodes_pattern, re.IGNORECASE)
    # Compile filter patterns as list of tuples
    compiled_filters = [
        (re.compile(pkg_pattern, re.IGNORECASE), re.compile(dep_pattern, re.IGNORECASE))
        for pkg_pattern, dep_pattern in filter_patterns
    ]
    # Compile style patterns
    compiled_styles = [
        (re.compile(pattern, re.IGNORECASE), style)
        for pattern, style in style_patterns.items()
    ]

    # Find all initial nodes (e.g., oarepo-* packages), excluding nodes that match exclude pattern
    if explicit_initial_nodes is not None:
        # Use explicitly provided initial nodes
        initial_nodes = explicit_initial_nodes & set(
            packages.keys()
        )  # Only include nodes that exist in packages
    else:
        # Use pattern matching to find initial nodes
        initial_nodes = set()
        for pkg_name in packages:
            if initial_pattern.match(pkg_name) and not exclude_pattern.match(pkg_name):
                initial_nodes.add(pkg_name)

    # Collect all nodes and edges
    nodes_to_process = set(initial_nodes)
    processed_nodes = set()
    all_nodes = set(initial_nodes)
    edges = set()  # Use set to avoid duplicates

    # BFS to find all dependencies
    while nodes_to_process:
        current_node = nodes_to_process.pop()
        if current_node in processed_nodes:
            continue

        processed_nodes.add(current_node)

        # Get dependencies of current node
        if current_node in packages:
            dependencies = packages[current_node].get("dependencies", [])
            for dep_str in dependencies:
                # Parse dependency string to get package name (without version specs)
                # Format is "package>=1.0,<2.0" or just "package"
                try:
                    req = Requirement(dep_str)
                    dep_name = req.name.lower()
                except Exception:
                    continue

                # Skip excluded nodes
                if exclude_pattern.match(dep_name):
                    continue

                # Apply filter: check if any tuple matches (package_pattern, dependency_pattern)
                should_include = False
                for pkg_pattern, dep_pattern in compiled_filters:
                    if pkg_pattern.match(current_node) and dep_pattern.match(dep_name):
                        should_include = True
                        break

                if should_include:
                    # Only include dependency if it exists in packages dict
                    if dep_name in packages:
                        all_nodes.add(dep_name)
                        edges.add(
                            (current_node, dep_name)
                        )  # Add to set instead of list

                        # Add to process queue if not yet processed
                        if dep_name not in processed_nodes:
                            nodes_to_process.add(dep_name)

    # Detect cycles
    nodes_in_cycles, cycles = find_cycles(all_nodes, list(edges))

    if cycles:
        print(f"⚠️  Found {len(cycles)} cycle(s) in dependency graph:")
        for i, cycle in enumerate(cycles[:5], 1):  # Show first 5 cycles
            cycle_str = " → ".join(cycle) + f" → {cycle[0]}"
            print(f"   Cycle {i} (length {len(cycle)}): {cycle_str}")
        if len(cycles) > 5:
            print(f"   ... and {len(cycles) - 5} more cycles")

    # Generate DOT format
    dot_lines = ["digraph dependencies {"]
    dot_lines.append("  rankdir=TB;")
    dot_lines.append("  node [shape=box];")
    dot_lines.append("  ranksep=1.0;")  # Add spacing between ranks
    dot_lines.append("")

    # Store node colors for edge coloring
    node_colors = {}

    # Add nodes with labels and styles
    for node in sorted(all_nodes):
        # Escape special characters in node names
        safe_node = node.replace("-", "_").replace(".", "_")

        # Get perturbed color for this node
        node_color = get_node_color(node, compiled_styles)
        node_colors[node] = node_color

        # Check if this package has been version-adjusted
        is_adjusted = node in packages and "adjusted" in packages[node]

        # Create node label with version info if adjusted
        node_label = node
        if is_adjusted:
            original_version = packages[node]["version"]
            adjusted_version = packages[node]["adjusted"]
            node_label = f"{node}\\n{original_version} → {adjusted_version}"

        # Mark nodes in cycles with a warning icon and red color
        # (this takes precedence over adjustment for background color)
        if node in nodes_in_cycles:
            if is_adjusted:
                # Show both cycle warning and version adjustment
                original_version = packages[node]["version"]
                adjusted_version = packages[node]["adjusted"]
                node_label = f"{node}\\n{original_version} → {adjusted_version}\\n⚠️ dep"
            else:
                node_label = f"{node}\\n⚠️ dep"
            node_style = ', fillcolor="#FF6B6B", style=filled'
        else:
            node_style = f', fillcolor="{node_color}", style=filled'

        # Add orange, thicker border for adjusted packages
        if is_adjusted:
            node_style += ', color="#FF8C00", penwidth=3.0'

        dot_lines.append(f'  {safe_node} [label="{node_label}"{node_style}];')

    dot_lines.append("")

    # Add edges with colors based on dependency (target) node
    # constraint=true ensures edges always flow downward in the hierarchy
    for src, dst in sorted(edges):
        safe_src = src.replace("-", "_").replace(".", "_")
        safe_dst = dst.replace("-", "_").replace(".", "_")
        # Color arrow based on dependency (dst) node color
        edge_color = node_colors.get(dst, "#000000")  # default to black
        dot_lines.append(
            f'  {safe_src} -> {safe_dst} [color="{edge_color}", dir=both, arrowtail=dot, constraint=true];'
        )

    dot_lines.append("}")

    return "\n".join(dot_lines)


def parse_version(version_str: str) -> tuple[int, int, int]:
    """Parse a version string into major, minor, patch components.

    Args:
        version_str: Version string like "1.2.3" or "1.2.3+local" or "1.2.3b1.dev0+local"

    Returns:
        Tuple of (major, minor, patch)
    """
    try:
        # Use packaging library to properly parse PEP 440 versions
        v = Version(version_str)
        return (v.major, v.minor, v.micro)
    except Exception:
        # Fallback to simple parsing if packaging fails
        # Strip local version identifier (anything after +)
        base_version = version_str.split("+")[0]
        # Strip pre-release/dev identifiers
        base_version = re.split(r"[a-z]", base_version, 1, re.IGNORECASE)[0]
        parts = base_version.rstrip(".").split(".")
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0
        return (major, minor, patch)


def bump_major_version(version_str: str) -> str:
    """Bump the major version: X.Y.Z -> (X+1).0.0

    Preserves local version identifiers if present (e.g., 1.2.3+local -> 2.0.0+local)

    Args:
        version_str: Version string like "1.2.3" or "1.2.3+local"

    Returns:
        Bumped version like "2.0.0" or "2.0.0+local"
    """
    try:
        # Use packaging library to properly handle PEP 440 versions
        v = Version(version_str)
        new_version = f"{v.major + 1}.0.0"
        # Preserve local version identifier if present
        if v.local:
            new_version += f"+{v.local}"
        return new_version
    except Exception:
        # Fallback to simple parsing
        major, _, _ = parse_version(version_str)
        # Preserve local version if present
        if "+" in version_str:
            local = version_str.split("+", 1)[1]
            return f"{major + 1}.0.0+{local}"
        return f"{major + 1}.0.0"


def version_satisfies_spec(version_str: str, spec_str: str) -> bool:
    """Check if a version satisfies a version specifier.

    Args:
        version_str: Version string like "2.0.0"
        spec_str: Specifier string like ">=1.0.0,<2.0.0"

    Returns:
        True if version satisfies the specifier, False otherwise
    """
    try:
        if not spec_str or spec_str.strip() == "":
            return True
        spec_set = SpecifierSet(spec_str)
        return Version(version_str) in spec_set
    except Exception:
        # If we can't parse, assume it's satisfied
        return True


def apply_version_adjustments(
    packages: dict[str, dict], upgraded_packages: set[str]
) -> dict[str, dict]:
    """Apply version adjustments based on upgraded packages.

    First, bump major version for all packages in upgraded_packages.
    Then, iteratively adjust packages whose dependencies don't satisfy their specifiers.

    Args:
        packages: Dict mapping package names to their info (version, dependencies)
        upgraded_packages: Set of package names to upgrade

    Returns:
        Updated packages dict with "adjusted" field where applicable
    """
    # First pass: adjust all upgraded packages
    for pkg_name in upgraded_packages:
        if pkg_name in packages:
            original_version = packages[pkg_name]["version"]
            adjusted_version = bump_major_version(original_version)
            packages[pkg_name]["adjusted"] = adjusted_version
            print(
                f"  ⬆️  {pkg_name}: {original_version} -> {adjusted_version} (upgraded)"
            )

    # Iteratively adjust packages whose dependencies don't match
    changed = True
    iteration = 0
    while changed:
        changed = False
        iteration += 1
        print(f"\n🔄 Adjustment iteration {iteration}...")

        for pkg_name, pkg_info in packages.items():
            # Skip if already adjusted
            if "adjusted" in pkg_info:
                continue

            # Check each dependency
            needs_adjustment = False
            for dep_str in pkg_info.get("dependencies", []):
                # Parse dependency string to get package name and version spec
                # Format can be "package>=1.0,<2.0" or just "package"
                try:
                    req = Requirement(dep_str)
                    dep_name = req.name.lower()
                    version_spec = str(req.specifier) if req.specifier else ""
                except Exception:
                    continue

                # Only check dependencies on packages that were adjusted
                if dep_name in packages and "adjusted" in packages[dep_name]:
                    # The dependency was adjusted, check if new version satisfies spec
                    dep_version = packages[dep_name]["adjusted"]

                    # Check if dependency version satisfies the spec
                    if version_spec and not version_satisfies_spec(
                        dep_version, version_spec
                    ):
                        needs_adjustment = True
                        print(
                            f"  ⚠️  {pkg_name} depends on {dep_name}{version_spec}, but {dep_name} is at {dep_version}"
                        )
                        break

            if needs_adjustment:
                original_version = pkg_info["version"]
                adjusted_version = bump_major_version(original_version)
                packages[pkg_name]["adjusted"] = adjusted_version
                print(
                    f"  ⬆️  {pkg_name}: {original_version} -> {adjusted_version} (dependency conflict)"
                )
                changed = True

    return packages


def generate_svg_from_dot(dot_content: str, output_path: Path) -> bool:
    """Generate SVG from DOT content.

    Args:
        dot_content: DOT format graph string
        output_path: Path where SVG should be saved

    Returns:
        True if successful, False otherwise
    """
    # Write DOT content to temporary file
    dot_path = output_path.with_suffix(".dot")
    dot_path.write_text(dot_content)

    try:
        subprocess.run(
            ["dot", "-Tsvg", str(dot_path), "-o", str(output_path)],
            check=True,
            capture_output=True,
        )
        print(f"✅ SVG graph saved to: {output_path}")
        return True
    except FileNotFoundError:
        print("⚠️  'dot' command not found. Install graphviz to generate SVG output.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Failed to generate SVG: {e.stderr.decode()}")
        return False


def filter_adjusted_packages(packages: dict[str, dict]) -> dict[str, dict]:
    """Filter packages to only those with adjusted versions.

    Args:
        packages: Dict mapping package names to their info

    Returns:
        Filtered dict containing only adjusted packages
    """
    return {
        pkg_name: pkg_info
        for pkg_name, pkg_info in packages.items()
        if "adjusted" in pkg_info
    }


def generate_dependency_table(packages: dict[str, dict]) -> str:
    """Generate a markdown table of package dependencies.

    Args:
        packages: Dict mapping package names to their info

    Returns:
        Markdown table as a string
    """
    lines = ["| Package | Version | Adjusted Version | Dependencies |"]
    lines.append("|---------|---------|------------------|--------------|")

    for pkg_name in sorted(packages.keys()):
        pkg_info = packages[pkg_name]
        version = pkg_info.get("version", "N/A")
        adjusted = pkg_info.get("adjusted", "-")
        dependencies = pkg_info.get("dependencies", [])

        # Format dependencies list
        if dependencies:
            deps_str = "<br>".join(dependencies)
        else:
            deps_str = "-"

        lines.append(f"| {pkg_name} | {version} | {adjusted} | {deps_str} |")

    return "\n".join(lines)


def generate_markdown_report(
    report_path: Path,
    svg_adjusted_path: Path | None,
    svg_all_path: Path,
    packages: dict[str, dict],
) -> None:
    """Generate a markdown report with dependency graphs and tables.

    Args:
        report_path: Path where the markdown report should be saved
        svg_adjusted_path: Path to the adjusted packages SVG (or None if not generated)
        svg_all_path: Path to the all packages SVG
        packages: Dict mapping package names to their info
    """
    lines = ["# Dependency Report", ""]

    # Add SVG images
    if svg_adjusted_path and svg_adjusted_path.exists():
        lines.append("## Adjusted Packages Dependency Graph")
        lines.append("")
        lines.append(f"![Adjusted Packages]({svg_adjusted_path.name})")
        lines.append("")

    lines.append("## All Packages Dependency Graph")
    lines.append("")
    lines.append(f"![All Packages]({svg_all_path.name})")
    lines.append("")

    # Add dependency table
    lines.append("## Dependency Table")
    lines.append("")
    lines.append(generate_dependency_table(packages))
    lines.append("")

    # Add adjusted packages section if any
    adjusted_packages = {
        pkg_name: pkg_info
        for pkg_name, pkg_info in packages.items()
        if "adjusted" in pkg_info
    }

    if adjusted_packages:
        lines.append("## Adjusted Packages Summary")
        lines.append("")
        lines.append(f"Total adjusted packages: {len(adjusted_packages)}")
        lines.append("")
        lines.append("| Package | Original Version | Adjusted Version |")
        lines.append("|---------|------------------|------------------|")
        for pkg_name in sorted(adjusted_packages.keys()):
            pkg_info = adjusted_packages[pkg_name]
            version = pkg_info.get("version", "N/A")
            adjusted = pkg_info.get("adjusted", "N/A")
            lines.append(f"| {pkg_name} | {version} | {adjusted} |")
        lines.append("")

    report_path.write_text("\n".join(lines))
    print(f"✅ Markdown report saved to: {report_path}")


def build_dependency_tree(
    major_version: int = typer.Argument(
        default=14,
        help="Major version of oarepo (corresponds to the InvenioRDM major version).",
    ),
    oarepo_version: str | None = typer.Option(
        None,
        "--oarepo-version",
        help="Use this exact oarepo version instead of looking up the latest.",
    ),
    directory: str = typer.Option(
        ".",
        help="Repository directory to operate in.",
    ),
    upgraded_packages: str | None = typer.Option(
        None,
        "--upgraded-packages",
        help="Comma-separated list of packages whose major version will be upgraded.",
    ),
    print_json: bool = typer.Option(
        False,
        "--print-json/--no-print-json",
        help="Whether to print JSON output to console.",
    ),
) -> None:
    """Set up the repository for the given oarepo major version."""
    dot_output = Path("dependencies.dot")
    report_file = Path("dependency_report.md")

    if oarepo_version:
        latest_oarepo_version = oarepo_version
        print(
            f"📦 Using supplied version: [bold green]{latest_oarepo_version}[/bold green]"
        )
    else:
        print(
            f"🔍 Searching for latest [bold]oarepo[/bold] [cyan]{major_version}.x[/cyan] release …"
        )
        latest_oarepo_version = get_latest_oarepo_version(major_version)
        print(f"📦 Latest version: [bold green]{latest_oarepo_version}[/bold green]")

    # now we have a lockfile with pinned versions, including upgraded packages
    # we now sync the lockfile with the local environment
    print("📦 Installing dependencies …")
    subprocess.run(
        ["uv", "sync", "--extra", "production", "--prerelease", "allow", "-U"],
        check=True,
        cwd=directory,
    )
    # Now we extract the dependency graph using the uv pip tree. We care only about
    # direct dependencies, not transitive ones.
    print("📊 Extracting dependency graph …")

    # list all installed packages
    installed_packages = {
        x["name"]: x["version"]
        for x in json.loads(
            subprocess.check_output(
                [
                    "uv",
                    "pip",
                    "list",
                    "-p",
                    f"{directory}/.venv/bin/python",
                    "--format",
                    "json",
                ],
                cwd=directory,
                text=True,
            )
        )
    }

    python_path = f"{directory}/.venv/bin/python"

    print("🔍 Analyzing package dependencies (including extras)...")
    packages = get_all_package_dependencies(installed_packages, python_path)

    # Apply version adjustments if upgraded_packages is specified
    if upgraded_packages:
        upgraded_set = set(
            pkg.strip() for pkg in upgraded_packages.split(",") if pkg.strip()
        )
        if upgraded_set:
            print(
                f"\n📦 Applying version adjustments for upgraded packages: {', '.join(sorted(upgraded_set))}"
            )
            packages = apply_version_adjustments(packages, upgraded_set)

    if print_json:
        print("\n📋 Final package information:")
        print(json.dumps(packages, indent=2))

    # Generate SVG for adjusted packages only (if any exist)
    svg_adjusted_path = None
    adjusted_packages_dict = filter_adjusted_packages(packages)
    if adjusted_packages_dict:
        print("\n🎨 Building DOT dependency graph for adjusted packages...")
        # Use filtered dict containing only adjusted packages
        dot_graph_adjusted = build_dot_dependency_graph(
            adjusted_packages_dict,
            explicit_initial_nodes=set(adjusted_packages_dict.keys()),
        )
        svg_adjusted_path = Path("dependencies_adjusted.svg")
        generate_svg_from_dot(dot_graph_adjusted, svg_adjusted_path)

    # Generate SVG for all packages
    print("\n🎨 Building DOT dependency graph for all packages...")
    dot_graph_all = build_dot_dependency_graph(packages)

    dot_path = Path(dot_output)
    dot_path.write_text(dot_graph_all)
    print(f"✅ DOT graph saved to: {dot_path}")

    svg_all_path = dot_path.with_suffix(".svg")
    generate_svg_from_dot(dot_graph_all, svg_all_path)

    # Generate markdown report
    print("\n📝 Generating markdown report...")
    generate_markdown_report(report_file, svg_adjusted_path, svg_all_path, packages)
