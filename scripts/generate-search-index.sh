#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

node ./scripts/search/main.js

# Fetch the name of the bucket from the metadata file.
destination_bucket="$(cat "$(origin_bucket_metadata_filepath)" | jq -r ".bucket")"

# Upload the `search-index.json` file to S3 where it can be accessed by the update search index cron.
aws s3 cp "./public/search-index.json" "s3://${destination_bucket}/search-index.json" --acl public-read --region "$(aws_region)"
