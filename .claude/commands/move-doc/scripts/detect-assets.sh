#!/bin/bash
# Detect co-located assets (images) in the same directory as a markdown file
# Usage: ./detect-assets.sh <source-file-path>
# Outputs JSON with asset information

set -e

SOURCE_FILE="$1"

if [ -z "$SOURCE_FILE" ]; then
  echo "Error: Source file path required" >&2
  exit 1
fi

if [ ! -f "$SOURCE_FILE" ]; then
  echo "Error: Source file does not exist: $SOURCE_FILE" >&2
  exit 1
fi

SOURCE_DIR=$(dirname "$SOURCE_FILE")

# Find image assets in same directory (png, jpg, jpeg, gif, svg)
# Exclude hidden files
ASSETS=$(find "$SOURCE_DIR" -maxdepth 1 -type f \
  \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" -o -name "*.svg" \) \
  -not -name ".*" 2>/dev/null || true)

# Build JSON output
if [ -n "$ASSETS" ]; then
  jq -n \
    --arg source_file "$SOURCE_FILE" \
    --arg source_dir "$SOURCE_DIR" \
    --argjson assets "$(echo "$ASSETS" | jq -R . | jq -s .)" \
    '{
      sourceFile: $source_file,
      sourceDir: $source_dir,
      assets: $assets,
      assetCount: ($assets | length)
    }'
else
  jq -n \
    --arg source_file "$SOURCE_FILE" \
    --arg source_dir "$SOURCE_DIR" \
    '{
      sourceFile: $source_file,
      sourceDir: $source_dir,
      assets: [],
      assetCount: 0
    }'
fi
