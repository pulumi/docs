#!/bin/bash

# Alias Verification Script
# Checks if renamed files have proper aliases pointing to their old locations
#
# Usage: ./verify-aliases.sh [renames_file]
#   If no file provided, uses ./renames.txt

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RENAMES_FILE="${1:-$SCRIPT_DIR/renames.txt}"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

if [[ ! -f "$RENAMES_FILE" ]]; then
    echo "ERROR: Renames file not found: $RENAMES_FILE" >&2
    echo "Run ./extract-renames.sh first" >&2
    exit 1
fi

# Counters
CORRECT=0
MISSING=0
SUSPICIOUS=0
TOTAL_CONTENT=0

# Output files
CORRECT_LOG="$SCRIPT_DIR/aliases-correct.txt"
MISSING_LOG="$SCRIPT_DIR/aliases-missing.txt"
SUSPICIOUS_LOG="$SCRIPT_DIR/aliases-suspicious.txt"

> "$CORRECT_LOG"
> "$MISSING_LOG"
> "$SUSPICIOUS_LOG"

# Function to convert file path to URL path
path_to_url() {
    local filepath="$1"
    # Remove content/ prefix
    local url="${filepath#content}"
    # Remove .md extension
    url="${url%.md}"
    # For _index.md files, remove _index
    url="${url%/_index}"
    # Ensure trailing slash
    if [[ ! "$url" =~ /$ ]]; then
        url="${url}/"
    fi
    echo "$url"
}

echo "Verifying aliases for renamed content files..."
echo ""

# Process each rename
while read -r line; do
    # Parse the line (format: "R### <tab> old_path <tab> new_path")
    similarity=$(echo "$line" | awk '{print $1}')
    old_path=$(echo "$line" | cut -f2)
    new_path=$(echo "$line" | cut -f3)
    # Skip non-content files
    if [[ ! "$old_path" =~ ^content/docs/ ]]; then
        continue
    fi

    ((TOTAL_CONTENT++))

    # Convert old path to expected URL
    expected_alias=$(path_to_url "$old_path")

    # Check if new file exists
    new_file="$REPO_ROOT/$new_path"
    if [[ ! -f "$new_file" ]]; then
        echo "⚠️  WARNING: New file doesn't exist: $new_file" >&2
        continue
    fi

    # Extract aliases from frontmatter using awk
    aliases=$(awk '
        BEGIN { in_frontmatter=0; in_aliases=0; }
        /^---$/ {
            if (in_frontmatter == 0) {
                in_frontmatter=1;
            } else {
                exit;
            }
            next;
        }
        in_frontmatter && /^aliases:/ {
            in_aliases=1;
            next;
        }
        in_frontmatter && in_aliases && /^[^ ]/ {
            in_aliases=0;
        }
        in_frontmatter && in_aliases && /^[ ]*-/ {
            sub(/^[ ]*- /, "");
            print;
        }
    ' "$new_file")

    # Check if expected alias is present
    if [[ -z "$aliases" ]]; then
        ((MISSING++))
        printf "❌ MISSING: %s\n   OLD: %s → EXPECTED ALIAS: %s\n\n" "$new_path" "$old_path" "$expected_alias" >> "$MISSING_LOG"
    elif echo "$aliases" | grep -Fq "$expected_alias"; then
        ((CORRECT++))
        echo "✓ $new_path" >> "$CORRECT_LOG"
    else
        ((SUSPICIOUS++))
        printf "⚠️  SUSPICIOUS: %s\n   OLD: %s → EXPECTED ALIAS: %s\n   HAS: %s\n\n" "$new_path" "$old_path" "$expected_alias" "$(echo "$aliases" | tr '\n' ' ')" >> "$SUSPICIOUS_LOG"
    fi

    # Progress indicator every 50 files
    if (( TOTAL_CONTENT % 50 == 0 )); then
        echo "Processed $TOTAL_CONTENT files..." >&2
    fi

done < "$RENAMES_FILE"

# Print summary
echo "=== VERIFICATION SUMMARY ==="
echo "Total content files renamed: $TOTAL_CONTENT"
echo ""
echo "✓ CORRECT:    $CORRECT"
echo "❌ MISSING:    $MISSING"
echo "⚠️  SUSPICIOUS: $SUSPICIOUS"
echo ""

if [[ $MISSING -eq 0 && $SUSPICIOUS -eq 0 ]]; then
    echo "🎉 ALL ALIASES VERIFIED! All $CORRECT files have correct aliases."
    exit 0
else
    echo "❌ ISSUES FOUND - Details in:"
    [[ $CORRECT -gt 0 ]] && echo "  ✓ $CORRECT_LOG"
    [[ $MISSING -gt 0 ]] && echo "  ❌ $MISSING_LOG"
    [[ $SUSPICIOUS -gt 0 ]] && echo "  ⚠️  $SUSPICIOUS_LOG"
    exit 1
fi
