#!/bin/bash
# Detect potentially orphaned menu entries in menus.yml after file moves
# Usage: ./check-orphaned-menus.sh <old-url>
# Outputs JSON with orphaned menu analysis

set -e

OLD_URL="$1"
MENUS_FILE="config/_default/menus.yml"

if [ -z "$OLD_URL" ]; then
  echo "Error: Old URL path required" >&2
  exit 1
fi

if [ ! -f "$MENUS_FILE" ]; then
  jq -n \
    --arg error "menus.yml file not found at $MENUS_FILE" \
    '{
      found: false,
      error: $error
    }'
  exit 0
fi

# Convert URL to likely identifier format
# /docs/iac/guides/ai-integration/ → iac-guides-ai-integration
url_to_identifier() {
  echo "$1" | sed 's|^/docs/||' | sed 's|/$||' | sed 's|/|-|g'
}

POTENTIAL_IDENTIFIER=$(url_to_identifier "$OLD_URL")

# Search for identifier in menus.yml
FOUND_IN_MENUS=$(grep -n "identifier: $POTENTIAL_IDENTIFIER" "$MENUS_FILE" 2>/dev/null || echo "")

if [ -n "$FOUND_IN_MENUS" ]; then
  LINE_NUM=$(echo "$FOUND_IN_MENUS" | cut -d: -f1)

  # Extract the menu entry context (3 lines: name, parent, identifier)
  # Handle potential variations in line order
  CONTEXT=$(sed -n "$((LINE_NUM-2)),$((LINE_NUM+2))p" "$MENUS_FILE")

  # Check if any files still reference this identifier as a parent
  REFS=$(grep -r "parent: $POTENTIAL_IDENTIFIER" content/docs/ --include="*.md" 2>/dev/null || echo "")

  # Count references (grep -c would fail if no matches, so use wc)
  if [ -n "$REFS" ]; then
    REF_COUNT=$(echo "$REFS" | grep -c "parent:" || echo "0")
  else
    REF_COUNT=0
  fi

  IS_ORPHANED="false"
  if [ "$REF_COUNT" -eq "0" ]; then
    IS_ORPHANED="true"
  fi

  # Build JSON output
  jq -n \
    --arg identifier "$POTENTIAL_IDENTIFIER" \
    --arg line_num "$LINE_NUM" \
    --arg context "$CONTEXT" \
    --arg ref_count "$REF_COUNT" \
    --arg is_orphaned "$IS_ORPHANED" \
    --arg menus_file "$MENUS_FILE" \
    '{
      found: true,
      identifier: $identifier,
      lineNumber: $line_num,
      context: $context,
      referenceCount: ($ref_count | tonumber),
      isOrphaned: ($is_orphaned == "true"),
      menusFile: $menus_file
    }'
else
  jq -n \
    --arg identifier "$POTENTIAL_IDENTIFIER" \
    '{
      found: false,
      identifier: $identifier,
      message: "No matching menu entry found in menus.yml"
    }'
fi
