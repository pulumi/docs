#!/bin/bash
set -o nounset -o errexit -o pipefail

source ./scripts/common.sh

CHECK_TYPE=${1-local}

check_links_www() {
    echo "Checking all links on pulumi.com..."
    node scripts/check-links.js "https://www.pulumi.com" "site" 3
}

check_get_pulumi_links() {
    echo "Checking get.pulumi.com links..."
    # We only link to get.pulumi.com in /docs/get-started/install/ and /docs/get-started/install/versions.
    node scripts/check-links.js "${1}/docs/get-started/install/versions/" "page"
    node scripts/check-links.js "${1}/docs/get-started/install/" "page"
}

if [ $CHECK_TYPE = "local" ]; then
    check_get_pulumi_links "local"
fi

if [ $CHECK_TYPE = "www" ]; then
    check_links_www
fi

# This variation lets us check important links at a specified URL.
if [ $CHECK_TYPE = "url" ]; then
    base_url="$2"
    check_get_pulumi_links "$base_url"
fi
