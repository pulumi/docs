#!/bin/bash
set -o nounset -o errexit -o pipefail

source ./scripts/common.sh

echo "Checking links..."

# Get required arguments
base_url="$1"
max_retries=2

# Optional section filter (defaults to empty - check all)
section_filter=""
if [ "$#" -gt 1 ]; then
    section_filter="$2"
fi

# Print information about what we're checking
echo "Base URL: $base_url"
if [ -n "$section_filter" ]; then
    echo "Section filter: $section_filter"
fi
echo "Max retries: $max_retries"

# Run the link checker
node "./scripts/link-checker/check-links.js" "$base_url" "$max_retries" "$section_filter"
