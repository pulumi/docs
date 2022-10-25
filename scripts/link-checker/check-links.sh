#!/bin/bash
set -o nounset -o errexit -o pipefail

source ./scripts/common.sh

echo "Checking links..."

base_url="$1"
this_path="scripts/link-checker"

node "$this_path/check-links.js" "$base_url" 2
