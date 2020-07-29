#!/bin/bash

set -o errexit -o pipefail

# This script lists the 20 most recent S3 buckets populated from docs-site build jobs. It
# works by querying S3 for buckets with names matching our origin-bucket naming prefix,
# then fetches the metadata files we generate with each build, outputting their results.
#
# Note that these buckets are not limited to those whose content has already been merged;
# this includes everything, including buckets for open PRs and those that failed to build.
# Commit links should help to identify buckets whose contents have been merged, however,
# and in general, the presence of a metadata file implies the bucket was built and tested
# successfully.

source ./scripts/common.sh

buckets="$(aws s3api list-buckets \
    --query "reverse(sort_by(Buckets,&CreationDate))[:20].{id:Name,date:CreationDate}|[?starts_with(id,'$(origin_bucket_prefix)')]" \
    --output json | jq -r '.[].id')"

as_array=($buckets)
bucket_count=${#as_array[@]}

if [ "$bucket_count" == "0" ]; then
    echo "No recent $(origin_bucket_prefix)-* buckets found."
    exit
fi

echo "Found ${bucket_count} recent $(origin_bucket_prefix)-* buckets:"

for bucket in $buckets; do
    echo
    echo "Fetching metadata for ${bucket}..."
    metadata="$(aws s3 cp "s3://${bucket}/metadata.json" - || true)"

    if [ ! -z "$metadata" ]; then
        echo
        echo "Bucket URL:  $(echo $metadata | jq -r '.url')"
        echo "Bucket Name: $(echo $metadata | jq -r '.bucket')"
        echo "Synced:      $(echo $metadata | jq -r '.timestamp / 1000 | strftime("%Y-%m-%d %H:%M:%S UTC")')"
        echo "Commit:      https://github.com/pulumi/docs/commit/$(echo $metadata | jq -r '.commit')"
    else
        echo "Missing metadata file. This bucket may not have been built and tested successfully."
    fi

    echo
    echo "---"
done

echo
echo "To run browser tests on one of these buckets, run:"
echo "nvm use && make ensure && CYPRESS_BASE_URL=\"<s3-bucket-url>\" yarn run cypress run --headless"
echo
echo "To pin the website to one of these buckets, run:"
echo "pulumi -C infrastructure config set originBucketNameOverride <bucket-name>"
echo "pulumi -C infrastrcuture preview"
echo
