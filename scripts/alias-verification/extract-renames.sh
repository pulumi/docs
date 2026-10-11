#!/bin/bash

# Extract Renames Script
# Extracts all renamed and deleted files from the current branch compared to master
# This makes the verification process repeatable

set -euo pipefail

OUTPUT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RENAMES_FILE="$OUTPUT_DIR/renames.txt"
DELETES_FILE="$OUTPUT_DIR/deletes.txt"

echo "Extracting renames and deletes from current branch vs origin/master..."

# Extract renames
git diff --name-status --diff-filter=R origin/master...HEAD > "$RENAMES_FILE"
RENAME_COUNT=$(wc -l < "$RENAMES_FILE")

# Extract deletes
git diff --name-status --diff-filter=D origin/master...HEAD > "$DELETES_FILE"
DELETE_COUNT=$(wc -l < "$DELETES_FILE")

echo "✓ Extracted $RENAME_COUNT renames to: $RENAMES_FILE"
echo "✓ Extracted $DELETE_COUNT deletes to: $DELETES_FILE"
