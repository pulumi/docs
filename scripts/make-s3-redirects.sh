#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# Create an S3 object for each of the items in the redirect list so it returns a 301
# redirect (instead of serving the HTML with a meta-redirect). This ensures the right HTTP
# response code is returned for search engines and enables better support for URL anchors.

build_dir="public"
destination_bucket="$(cat "$(origin_bucket_metadata_filepath)" | jq -r ".bucket")"
redirects_file="./redirects.txt"
aws s3 cp "s3://${destination_bucket}/redirects.txt" "$redirects_file"

echo "Processing S3 redirects for ${destination_bucket}..."
IFS="|"
while read key location; do
    echo "Redirecting $key to $location"
    aws s3api put-object --key "$key" --website-redirect-location "$location" --bucket "$destination_bucket" --acl public-read
done < "$redirects_file"

rm "$redirects_file"
