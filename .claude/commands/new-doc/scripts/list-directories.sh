#!/bin/bash
# Directory Listing Script
# Usage: ./list-directories.sh <path>
#
# Lists subdirectories sorted by menu weight (not alphabetically)
# Outputs numbered list in left-nav order

set -e

if [ -z "$1" ]; then
  echo "Error: Path required"
  echo "Usage: $0 <path>"
  exit 1
fi

TARGET_PATH="$1"

if [ ! -d "$TARGET_PATH" ]; then
  echo "Error: Directory not found: $TARGET_PATH"
  exit 1
fi

# For each subdirectory, extract title and weight
for dir in $(ls -1 "$TARGET_PATH/" | grep -v "^_" | grep -v "^\."); do
  index_file="$TARGET_PATH/$dir/_index.md"
  if [ -f "$index_file" ]; then
    title=$(grep -m1 "^title:" "$index_file" | sed 's/title: *//' | tr -d '"')
    weight=$(grep -A10 "^menu:" "$index_file" | grep -m1 "weight:" | grep -oE '[0-9]+')
    echo "${weight:-999}|${title:-$dir}|$dir"
  else
    echo "999|$dir|$dir"
  fi
done | sort -n -t'|' -k1 | nl -w1 -s'. '
