#!/bin/bash
# Analyze menu frontmatter and detect when section changes require updates
# Usage: ./analyze-menu.sh <source-file> <destination-file>
# Outputs JSON with menu analysis

set -e

SOURCE_FILE="$1"
DEST_FILE="$2"

if [ -z "$SOURCE_FILE" ] || [ -z "$DEST_FILE" ]; then
  echo "Error: Source and destination file paths required" >&2
  exit 1
fi

if [ ! -f "$SOURCE_FILE" ]; then
  echo "Error: Source file does not exist: $SOURCE_FILE" >&2
  exit 1
fi

# Extract menu section from frontmatter (iac, ai, esc, deployments, insights)
extract_menu_section() {
  local file="$1"

  # Extract lines between first two --- markers, find menu section
  awk '/^---$/{if(++count==2) exit} count==1 && /^[[:space:]]*menu:/{found=1} found' "$file" 2>/dev/null | \
    grep -E "^[[:space:]]*(iac|ai|esc|deployments|insights):" | \
    sed 's/[[:space:]]*\([^:]*\):.*/\1/' | head -1 || echo ""
}

# Detect section from file path
detect_section_from_path() {
  local file="$1"

  if echo "$file" | grep -q "content/docs/iac/"; then
    echo "iac"
  elif echo "$file" | grep -q "content/docs/ai/"; then
    echo "ai"
  elif echo "$file" | grep -q "content/docs/esc/"; then
    echo "esc"
  elif echo "$file" | grep -q "content/docs/deployments/"; then
    echo "deployments"
  elif echo "$file" | grep -q "content/docs/insights/"; then
    echo "insights"
  else
    echo "unknown"
  fi
}

SOURCE_MENU=$(extract_menu_section "$SOURCE_FILE")
SOURCE_PATH_SECTION=$(detect_section_from_path "$SOURCE_FILE")
DEST_PATH_SECTION=$(detect_section_from_path "$DEST_FILE")

# Determine if menu needs updating
NEEDS_UPDATE="false"
RECOMMENDATION=""

if [ -z "$SOURCE_MENU" ]; then
  RECOMMENDATION="No menu frontmatter found in source file"
elif [ "$SOURCE_PATH_SECTION" != "$DEST_PATH_SECTION" ]; then
  if [ "$SOURCE_MENU" != "$DEST_PATH_SECTION" ] && [ "$DEST_PATH_SECTION" != "unknown" ]; then
    NEEDS_UPDATE="true"
    RECOMMENDATION="Update menu from '$SOURCE_MENU' to '$DEST_PATH_SECTION' to match new location"
  elif [ "$DEST_PATH_SECTION" = "unknown" ]; then
    RECOMMENDATION="Cannot determine destination section from path"
  fi
else
  RECOMMENDATION="File staying in same section, no menu update needed"
fi

# Build JSON output
jq -n \
  --arg source_menu "$SOURCE_MENU" \
  --arg source_path_section "$SOURCE_PATH_SECTION" \
  --arg dest_path_section "$DEST_PATH_SECTION" \
  --arg needs_update "$NEEDS_UPDATE" \
  --arg recommendation "$RECOMMENDATION" \
  '{
    sourceMenu: $source_menu,
    sourcePathSection: $source_path_section,
    destPathSection: $dest_path_section,
    needsUpdate: ($needs_update == "true"),
    recommendation: $recommendation
  }'
