#!/bin/bash

set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔧 Building d3 and elkjs libraries..."
echo ""

# Check if pnpm is installed
if ! command -v pnpm &> /dev/null; then
    echo "❌ pnpm is not installed!"
    echo ""
    echo "Please install pnpm first:"
    echo "  npm install -g pnpm"
    echo "  or"
    echo "  curl -fsSL https://get.pnpm.io/install.sh | sh -"
    exit 1
fi

echo "📦 Installing dependencies with pnpm..."
pnpm install

echo ""
echo "🏗️  Building libraries..."
pnpm run build

echo ""
echo "✅ Build completed successfully!"
echo "   Libraries are available in: $SCRIPT_DIR/dist/"
