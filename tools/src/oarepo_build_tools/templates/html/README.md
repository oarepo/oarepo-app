# HTML Template for Dependency Graph Visualization

This directory contains the source files for the interactive OARepo dependency graph HTML report.

## Overview

When `render_graph()` is called, this directory is copied to the output location, where the build process runs automatically. The final output is a self-contained HTML report with bundled JavaScript libraries.

## Files in This Directory

### Source Files
- **styles.css** - CSS styling for the HTML report
- **graph.js** - JavaScript code for rendering the interactive dependency graph
- **dependency_graph.html.j2** - Jinja2 template for the HTML structure (located in parent `templates/` directory)

### Build Configuration
- **package.json** - NPM package configuration with dependencies (d3, d3-dag, esbuild)
- **build.js** - esbuild script that bundles libraries and copies assets to `dist/`
- **build.sh** - Shell script that orchestrates the build process

### Other Files
- **README.md** - This file
- **.gitignore** - Ignores build artifacts (node_modules, dist, etc.)

## How It Works

### Automatic Build Process

When you call `render_graph(output_directory, packages)` in Python:

1. **Copy**: All files from this directory are copied to `output_directory/`
2. **Generate**: `index.html` is created in `output_directory/` with the dependency data
3. **Build**: `build.sh` runs automatically in `output_directory/` to:
   - Install dependencies (d3, d3-dag) using pnpm
   - Bundle JavaScript libraries
   - Copy CSS and JS files to `dist/`
4. **Cleanup**: Build artifacts are removed from `output_directory/`:
   - `package.json`, `build.js`, `build.sh`
   - `node_modules/`, `pnpm-lock.yaml`
   - Original `styles.css` and `graph.js` (kept only in `dist/`)

### Final Output Structure

```
output/
├── index.html          # Main HTML report
└── dist/               # Bundled assets
    ├── d3.min.js
    ├── d3-dag.min.js
    ├── styles.css
    └── graph.js
```

## Prerequisites

The build process requires:
- **Node.js** >= 18.0.0
- **pnpm** >= 8.0.0

### Installing pnpm

If pnpm is not installed, the build will fail with instructions. Install it using:

```bash
# Using npm
npm install -g pnpm

# Using standalone script
curl -fsSL https://get.pnpm.io/install.sh | sh -

# On macOS using Homebrew
brew install pnpm
```

## Manual Testing

To test the build process manually without running the full Python code:

```bash
# 1. Copy this directory to a test location
cp -r . /tmp/test-build

# 2. Create a simple index.html
cd /tmp/test-build
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="dist/styles.css">
</head>
<body>
    <div class="container">
        <h1>Test Build</h1>
    </div>
    <script src="dist/d3.min.js"></script>
    <script src="dist/d3-dag.min.js"></script>
    <script src="dist/graph.js"></script>
</body>
</html>
EOF

# 3. Run the build
./build.sh

# 4. Open in browser
open index.html
```

## Library Versions

- **D3.js**: 7.9.0 - Data visualization library
- **d3-dag**: 1.1.2 - DAG layout algorithms (Sugiyama, etc.)
- **esbuild**: 0.20.0 - Fast JavaScript bundler

## Modifying the Template

If you need to modify the HTML template:

1. **CSS changes**: Edit `styles.css`
2. **JavaScript changes**: Edit `graph.js`
3. **HTML structure**: Edit `dependency_graph.html.j2` in the parent directory
4. **Build configuration**: Edit `package.json` or `build.js`

After making changes, the updated files will be automatically included the next time `render_graph()` is called.

## Troubleshooting

### Build fails with "pnpm: command not found"

Install pnpm using one of the methods in the Prerequisites section.

### Build fails with Node.js version error

Ensure you have Node.js 18 or higher:
```bash
node --version
```

### Libraries are outdated

To update library versions:

1. Edit `package.json` to change version numbers
2. Delete `pnpm-lock.yaml` if it exists in the source directory
3. The next build will use the new versions

## Development Notes

- The build process is designed to be self-contained and reproducible
- All dependencies are locked in `package.json` with specific versions
- The bundled output in `dist/` is optimized and minified
- The template uses Jinja2 to inject dependency data at generation time
- The JavaScript code expects global variables set by the template

## License

The bundled libraries maintain their original licenses:
- **D3.js**: ISC License
- **d3-dag**: MIT License