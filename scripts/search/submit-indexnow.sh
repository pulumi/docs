#!/bin/bash

set -o errexit -o pipefail

# This script submits URLs to IndexNow API to trigger immediate crawling by search engines
# It uses the indexnow.js Node.js script to handle the submission process

source ./scripts/common.sh

echo "Submitting URLs to IndexNow..."
node ./scripts/search/indexnow.js "$1"