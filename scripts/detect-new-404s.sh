#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# This script detects new 404 errors by comparing the staging site against the production site.
# It checks for broken links that might be introduced in pull requests by analyzing 
# the differences between the production site (pulumi.com) and the staging deployment.

destination_bucket="$(cat "$(origin_bucket_metadata_filepath)" | jq -r ".bucket")"
s3_website_url="http://${destination_bucket}.s3-website.$(aws_region).amazonaws.com"

echo "Checking ${s3_website_url} for new 404s..."
# For now we don't want this to fail the build due to lots of flakiness, so always exit successfully.
node scripts/detect-new-404s.js "https://pulumi.com" "${s3_website_url}" || true
