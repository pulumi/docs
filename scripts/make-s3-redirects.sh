#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# Create an S3 object for each of the items in the redirect list so it returns a 301
# redirect (instead of serving the HTML with a meta-redirect). This ensures the right HTTP
# response code is returned for search engines and enables better support for URL anchors.

build_dir="$1"
destination_bucket="$2"
redirects_file="./redirects.txt"

# aws s3 cp "s3://${destination_bucket}/redirects.txt" "$redirects_file" --region "$(aws_region)"

echo "Processing S3 redirects for ${destination_bucket}..."
node scripts/make-s3-redirects.js "${destination_bucket}" "${build_dir}/redirects.txt" "$(aws_region)"

echo "Processing custom redirects in scripts/redirects..."
ls -l "./scripts/redirects/" | tail -n +2 | awk '{print $9}' | while read line; do
    redirect_file="./scripts/redirects/$line"
    node scripts/make-s3-redirects.js "${destination_bucket}" "${redirect_file}" "$(aws_region)"
done
