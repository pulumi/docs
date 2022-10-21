#!/bin/bash
set -o nounset -o errexit -o pipefail

source ./scripts/common.sh

echo "Checking links..."

base_url="$1"
start_from_url="${2-""}"
this_path="scripts/link-checker"
pages_to_check=$(node "$this_path/get-pages-to-check.js" "$base_url" "$start_from_url")
page_count="$(echo "$pages_to_check" | wc -l)"
logfile="$this_path/pages-with-broken-links.txt"

rm -f "$logfile"
index=0

for url in $pages_to_check
do
    index="$((index+1))"

    echo "-------------------------------------------------------------------------------------------------------------"
    echo "Checking $url ($index of ${page_count// }) ..."
    echo "-------------------------------------------------------------------------------------------------------------"
    echo ""

    node "$this_path/check-links.js" "$url" "page" 1 || echo -e "$url" >> "$logfile"
done
