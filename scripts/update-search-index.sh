#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# Run the script that updates the Algolia search index. The value passed into this script denotes
# the name of the index to be updated (e.g., 'preview' or 'production').
node ./scripts/search/main.js "$1"

# Fetch the name of the bucket from the metadata file.
destination_bucket="$(cat "$(origin_bucket_metadata_filepath)" | jq -r ".bucket")"

# Upload the `search-index.json` file to S3 where it can be accessed by the update search index cron.
aws s3 cp "./public/search-index-docs.json" "s3://${destination_bucket}/search-index.json" --acl public-read --region "$(aws_region)"

# Upload the `search-index-settings.json` file to S3 where it can be accessed by the update search index cron.
aws s3 cp "./public/search-index-settings.json" "s3://${destination_bucket}/search-index-settings.json" --acl public-read --region "$(aws_region)"
