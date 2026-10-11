#!/bin/bash
set -o nounset -o errexit -o pipefail

source ./scripts/common.sh

echo "Checking links..."

base_url="$1"
node "./scripts/link-checker/check-links.js" "$base_url" 2
