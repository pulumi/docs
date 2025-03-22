#!/usr/bin/env bash

set -o errexit -o pipefail

source ./scripts/common.sh

# TODO: Explain what this does.

destination_bucket="$(cat "$(origin_bucket_metadata_filepath)" | jq -r ".bucket")"
s3_website_url="http://${destination_bucket}.s3-website.$(aws_region).amazonaws.com"

echo "Checking ${s3_website_url} for new 404s..."
# For now we don't want this to fail the build due to lots of flakiness, so always exit successfully.
node scripts/detect-new-404s.js "https://pulumi.com" "${s3_website_url}" || true
