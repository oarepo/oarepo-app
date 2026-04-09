"""Build dependency tree of packages.

Note: this command modifies the local repository!

Prerequisites for HTML report generation:
    The interactive HTML report automatically builds JavaScript libraries (d3, d3-dag)
    during execution. Requires:
        - Node.js >= 18.0.0
        - pnpm >= 8.0.0

    If pnpm is not installed, run:
        npm install -g pnpm
"""

import hashlib
import json
import re
import shutil
import subprocess
from graphlib import TopologicalSorter
from pathlib import Path

import typer
from jinja2 import Environment, FileSystemLoader
from oarepo_build_tools.python import (
    get_latest_oarepo_version,
)
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.version import Version
from rich import print

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
        Updated packages dict with "bumped" field where applicable
    """
    # First pass: adjust all upgraded packages
    for pkg_name in upgraded_packages:
        if pkg_name in packages:
            original_version = packages[pkg_name]["version"]
            bumped_version = bump_major_version(original_version)
            packages[pkg_name]["bumped"] = bumped_version
            print(f"  ⬆️  {pkg_name}: {original_version} -> {bumped_version} (upgraded)")

    # Iteratively adjust packages whose dependencies don't match
    changed = True
    iteration = 0
    while changed:
        changed = False
        iteration += 1
        print(f"\n🔄 Adjustment iteration {iteration}...")

        for pkg_name, pkg_info in packages.items():
            # Skip if already bumped
            if "bumped" in pkg_info:
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

                # Only check dependencies on packages that were bumped
                if dep_name in packages and "bumped" in packages[dep_name]:
                    # The dependency was bumped, check if new version satisfies spec
                    dep_version = packages[dep_name]["bumped"]

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
                bumped_version = bump_major_version(original_version)
                packages[pkg_name]["bumped"] = bumped_version
                print(
                    f"  ⬆️  {pkg_name}: {original_version} -> {bumped_version} (dependency conflict)"
                )
                changed = True

    return packages


def render_graph(output_directory: str | Path, packages: dict[str, dict]) -> None:
    """Generate an interactive HTML report with dependency graph visualization.

    Creates a self-contained HTML file (index.html) with an interactive dependency
    graph using D3.js and a custom layered layout algorithm. The report includes:

    1. Interactive dependency graph with toggle between all/bumped packages
       - Uses d3-dag Sugiyama layout algorithm
       - Color-coded nodes (red=bumped, blue=normal)
       - Hover tooltips with package details
       - Automatic layer-based positioning

    2. Summary cards showing total and bumped package counts

    3. Table of bumped packages (if any) with original and bumped versions

    4. Complete dependency table showing all package relationships

    The build process:
    1. Copies html template directory to output directory
    2. Generates index.html with data in output directory
    3. Runs build.sh to bundle JavaScript libraries
    4. Cleans up build artifacts (package.json, build scripts, node_modules)

    Args:
        output_directory: Directory where output should be created.
                         Will be created if it doesn't exist.
        packages: Dict mapping package names to their info with structure:
                 {
                     "package-name": {
                         "version": "1.2.3",
                         "dependencies": ["dep>=1.0.0"],
                         "bumped": "2.0.0"  # optional
                     }
                 }

    Raises:
        subprocess.CalledProcessError: If build.sh fails to execute
        FileNotFoundError: If html template directory doesn't exist

    Example:
        >>> packages = {
        ...     "oarepo-model": {
        ...         "version": "1.5.0",
        ...         "dependencies": ["oarepo-runtime>=1.0.0"],
        ...         "bumped": "2.0.0"
        ...     }
        ... }
        >>> render_graph("output", packages)
        ✅ Interactive HTML report saved to: output/index.html
    """
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Apply same filtering logic as DOT graph
    initial_pattern = re.compile(DEPGRAPH_INITIAL_NODES_REGEXP, re.IGNORECASE)
    exclude_pattern = re.compile(DEPGRAPH_EXCLUDE_NODES_REGEXP, re.IGNORECASE)
    compiled_filters = [
        (re.compile(pkg_pattern, re.IGNORECASE), re.compile(dep_pattern, re.IGNORECASE))
        for pkg_pattern, dep_pattern in DEPGRAPH_FILTER_REGEXP
    ]
    compiled_styles = [
        (re.compile(pattern, re.IGNORECASE), style)
        for pattern, style in DEPGRAPH_STYLE.items()
    ]

    # Find initial nodes (oarepo-* packages), excluding specified patterns
    initial_nodes = set()
    for pkg_name in packages:
        if initial_pattern.match(pkg_name) and not exclude_pattern.match(pkg_name):
            initial_nodes.add(pkg_name)

    # BFS to find all dependencies (same logic as DOT graph)
    nodes_to_process = set(initial_nodes)
    processed_nodes = set()
    all_nodes = set(initial_nodes)
    edges = set()

    while nodes_to_process:
        current_node = nodes_to_process.pop()
        if current_node in processed_nodes:
            continue

        processed_nodes.add(current_node)

        if current_node in packages:
            dependencies = packages[current_node].get("dependencies", [])
            for dep_str in dependencies:
                try:
                    req = Requirement(dep_str)
                    dep_name = req.name.lower()
                except Exception:
                    continue

                if exclude_pattern.match(dep_name):
                    continue

                # Apply filter patterns
                should_include = False
                for pkg_pattern, dep_pattern in compiled_filters:
                    if pkg_pattern.match(current_node) and dep_pattern.match(dep_name):
                        should_include = True
                        break

                if should_include and dep_name in packages:
                    all_nodes.add(dep_name)
                    edges.add((current_node, dep_name))
                    if dep_name not in processed_nodes:
                        nodes_to_process.add(dep_name)

    # Detect cycles
    nodes_in_cycles, cycles = find_cycles(all_nodes, list(edges))

    # Prepare data for bumped packages table
    bumped_packages = [
        {
            "name": pkg_name,
            "version": pkg_info.get("version", "N/A"),
            "bumped": pkg_info.get("bumped", "N/A"),
        }
        for pkg_name, pkg_info in sorted(packages.items())
        if "bumped" in pkg_info and pkg_name in all_nodes
    ]

    # Prepare dependency data for table
    all_dependencies = []
    for src, dst in sorted(edges):
        version_spec = "-"
        if src in packages:
            for dep_str in packages[src].get("dependencies", []):
                try:
                    req = Requirement(dep_str)
                    if req.name.lower() == dst:
                        version_spec = str(req.specifier) if req.specifier else "-"
                        break
                except Exception:
                    pass
        src_info = packages.get(src, {})
        dst_info = packages.get(dst, {})
        all_dependencies.append(
            {
                "source": src,
                "source_version": src_info.get("version", ""),
                "source_bumped": src_info.get("bumped", ""),
                "target": dst,
                "target_version": dst_info.get("version", ""),
                "target_bumped": dst_info.get("bumped", ""),
                "spec": version_spec,
            }
        )

    # Prepare node data with colors and styling
    nodes_data = []
    for pkg_name in sorted(all_nodes):
        pkg_info = packages.get(pkg_name, {})
        is_bumped = "bumped" in pkg_info
        in_cycle = pkg_name in nodes_in_cycles

        # Get perturbed color
        node_color = get_node_color(pkg_name, compiled_styles)

        # Build label
        version = pkg_info.get("version", "N/A")
        label = pkg_name
        if is_bumped:
            bumped_version = pkg_info.get("bumped", "N/A")
            label = f"{pkg_name}\n{version} → {bumped_version}"
        else:
            label = f"{pkg_name}\n{version}"
        if in_cycle:
            label += "\n⚠️ dep"

        nodes_data.append(
            {
                "id": pkg_name,
                "label": label,
                "version": pkg_info.get("version", "N/A"),
                "bumped": pkg_info.get("bumped", ""),
                "is_bumped": is_bumped,
                "in_cycle": in_cycle,
                "color": node_color,
                "border_color": "#FF8C00" if is_bumped else "#333",
                "border_width": 3 if is_bumped else 1.5,
            }
        )

    # Prepare edge data with colors based on target node
    node_colors = {node["id"]: node["color"] for node in nodes_data}
    edges_data = []
    for src, dst in edges:
        edges_data.append(
            {
                "source": src,
                "target": dst,
                "color": node_colors.get(dst, "#999"),
            }
        )

    # Prepare bumped-only filtered data
    bumped_node_ids = set(n["id"] for n in nodes_data if n["is_bumped"])
    nodes_data_bumped = [n for n in nodes_data if n["is_bumped"]]
    edges_data_bumped = [
        e
        for e in edges_data
        if e["source"] in bumped_node_ids and e["target"] in bumped_node_ids
    ]

    # Step 1: Copy html template directory to output directory
    template_html_dir = Path(__file__).parent / "templates" / "html"

    if not template_html_dir.exists():
        raise FileNotFoundError(
            f"HTML template directory not found: {template_html_dir}"
        )

    print("📁 Copying HTML template to output directory...")

    # Copy all files from html directory to output directory
    for item in template_html_dir.iterdir():
        if item.name.startswith("."):
            continue  # Skip hidden files like .gitignore

        dest_path = output_dir / item.name

        if item.is_file():
            shutil.copy2(item, dest_path)
        elif item.is_dir() and item.name != "node_modules" and item.name != "dist":
            # Don't copy node_modules or dist if they exist
            shutil.copytree(item, dest_path, dirs_exist_ok=True)

    print("   ✓ HTML template copied")

    # Step 2: Generate index.html in output directory
    print("📝 Generating index.html...")

    template_dir = Path(__file__).parent / "templates"
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("dependency_graph.html.j2")
    html_content = template.render(
        nodes_all=nodes_data,
        edges_all=edges_data,
        nodes_bumped=nodes_data_bumped,
        edges_bumped=edges_data_bumped,
        bumped_packages=bumped_packages,
        dependencies=all_dependencies,
    )

    index_path = output_dir / "index.html"
    index_path.write_text(html_content)
    print("   ✓ index.html created")

    # Step 3: Run build.sh in output directory to bundle JavaScript
    build_script = output_dir / "build.sh"

    if not build_script.exists():
        print(f"⚠️  Warning: build.sh not found at {build_script}")
        print("   Skipping JavaScript build")
        return

    print("🔨 Building JavaScript libraries...")

    try:
        result = subprocess.run(
            ["bash", "build.sh"],
            cwd=output_dir,
            check=True,
            capture_output=True,
            text=True,
        )
        if result.stdout:
            # Print build output with indentation
            for line in result.stdout.strip().split("\n"):
                if line.strip():
                    print(f"   {line}")
    except subprocess.CalledProcessError as e:
        print("❌ Build failed!")
        if e.stdout:
            print(f"   STDOUT: {e.stdout}")
        if e.stderr:
            print(f"   STDERR: {e.stderr}")
        raise

    # Step 4: Clean up build artifacts
    print("🧹 Cleaning up build artifacts...")

    artifacts_to_remove = [
        "package.json",
        "build.js",
        "build.sh",
        "node_modules",
        "pnpm-lock.yaml",
        ".pnpm-store",
        "styles.css",  # Original, now in dist/
        "graph.js",  # Original, now in dist/
    ]

    for artifact in artifacts_to_remove:
        artifact_path = output_dir / artifact
        if artifact_path.exists():
            if artifact_path.is_file():
                artifact_path.unlink()
            elif artifact_path.is_dir():
                shutil.rmtree(artifact_path)

    print("   ✓ Build artifacts removed")
    print("\n✅ Interactive HTML report completed!")
    print(f"   Location: {index_path}")
    print(f"   Assets: {output_dir / 'dist'}")


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

    # Generate interactive HTML report
    print("\n🌐 Generating interactive HTML report...")
    output_dir = Path("output")
    render_graph(output_dir, packages)
