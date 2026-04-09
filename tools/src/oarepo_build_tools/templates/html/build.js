import * as esbuild from "esbuild";
import { fileURLToPath } from "url";
import { dirname, join } from "path";
import { mkdir, copyFile } from "fs/promises";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const distDir = join(__dirname, "dist");

// Ensure dist directory exists
await mkdir(distDir, { recursive: true });

console.log("📦 Building JavaScript bundle...\n");

// Bundle graph.js together with d3 and d3-dag into a single IIFE bundle
console.log("  Building bundle.js...");
await esbuild
  .build({
    entryPoints: [join(__dirname, "graph.js")],
    bundle: true,
    minify: true,
    format: "iife",
    outfile: join(distDir, "bundle.js"),
    allowOverwrite: true,
    logLevel: "warning",
  })
  .catch(() => process.exit(1));

// Copy CSS file
console.log("  Copying styles.css...");
await copyFile(
  join(__dirname, "styles.css"),
  join(distDir, "styles.css"),
).catch((err) => {
  console.error("  ⚠️  Failed to copy styles.css:", err.message);
  process.exit(1);
});

console.log("\n✅ Build completed successfully!");
console.log(`   Output directory: ${distDir}`);
console.log("   Files created:");
console.log("     - bundle.js");
console.log("     - styles.css");
