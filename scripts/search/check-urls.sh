#!/bin/bash
set -o nounset -o errexit -o pipefail

source ./scripts/common.sh

index="$1"
base_url="$2"

mkdir -p public

echo "Downloading the '$index' index..."
algolia objects browse "$index" \
    --admin-api-key "$ALGOLIA_APP_ADMIN_KEY" \
    --application-id "$ALGOLIA_APP_ID" > ./public/search-index.json

node "./scripts/search/check-urls.js" "$base_url"
