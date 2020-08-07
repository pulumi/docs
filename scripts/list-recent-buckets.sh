#!/bin/bash

set -o errexit -o pipefail

# This script lists the 50 most recent S3 buckets populated from docs-site build jobs. It
# works by querying S3 for buckets with names matching our origin-bucket naming prefix,
# then fetches the metadata files we generate with each build, outputting their results.
#
# For buckets built by `pull_request` and `push` jobs, the script will also tell you
# whether a given bucket can be safely deleted.
#
# Usage:
#   ./scripts/list-recent-buckets.sh            # List all buckets
#   ./scripts/list-recent-buckets.sh pr         # List all buckets prefixed with "-pr-" (to filter pull_request builds)
#   ./scripts/list-recent-buckets.sh push       # List all buckets prefixed with "-push-" (to filter push builds)

source ./scripts/common.sh

bucket_prefix="$1"
buckets=$(get_recent_buckets $bucket_prefix)
buckets_as_array=($buckets)
bucket_count=${#buckets_as_array[@]}

if [ "$bucket_count" == "0" ]; then
    echo "No recent buckets matching the prefix $(origin_bucket_prefix)-${bucket_prefix} were found."
    exit
fi

# Query for the bucket currently serving pulumi.com.
currently_deployed_bucket="$(curl -s https://www.pulumi.com/metadata.json | jq -r '.bucket' || echo '')"

echo "Found ${bucket_count} recent buckets matching the prefix $(origin_bucket_prefix)${bucket_prefix}:"
echo

# Variables used for determining whether a push-built bucket is safe to delete.

# The number of buckets beyond the currently deployed one that should be retained.
buckets_to_retain=10

# A counter for tracking how many builds behind the current website a given bucket is.
buckets_beyond_current=0

# A flag denoting whether the current website bucket exists in the current result set.
website_bucket_identified=false

for bucket in $buckets; do
    echo
    echo "Fetching metadata for ${bucket}..."
    metadata="$(aws s3 cp "s3://${bucket}/metadata.json" - || echo '')"

    if [ ! -z "$metadata" ]; then
        bucket_url="$(echo $metadata | jq -r '.url')"
        bucket_name="$(echo $metadata | jq -r '.bucket')"
        bucket_timestamp="$(echo $metadata | jq -r '.timestamp / 1000 | strftime("%Y-%m-%d %H:%M:%S UTC")')"
        bucket_commit="$(echo $metadata | jq -r '.commit')"

        echo "Bucket URL:  ${bucket_url}"
        echo "Bucket Name: ${bucket_name}"
        echo "Synced At:   ${bucket_timestamp}"
        echo "Commit:      https://github.com/pulumi/docs/commit/${bucket_commit}"

        # Call out whether this bucket is the one currently serving pulumi.com.
        if [ "$bucket_name" == "$currently_deployed_bucket" ]; then
            echo
            echo "*"
            echo "*"
            echo "* ☝️  Head's up!"
            echo "*    This bucket (${bucket_name}) is currently serving pulumi.com."
            echo "*    https://www.pulumi.com/metadata.json"
            echo "*"
            echo "*"

            website_bucket_identified=true
        fi

        # For push or pull_request buckets, indicate whether they can be safely deleted.
        if [ "$1" == "push" ]; then
            if [ "$buckets_beyond_current" -gt "$buckets_to_retain" ]; then
                echo
                echo "⭐️ This bucket is ${buckets_beyond_current} buckets behind the current website, so it can safely be deleted."
                echo "   aws s3 rb s3://${bucket_name} --force"
            fi
        elif [ "$1" == "pr" ]; then
            associated_pr="$(get_pr_for_commit $bucket_commit)"

            if [ ! -z "$associated_pr" ]; then
                pr_number="$(echo $associated_pr | jq -r '.[0].number')"
                pr_state="$(echo $associated_pr | jq -r '.[0].state')"

                if [ "$pr_state" == "closed" ]; then
                    echo
                    echo "⭐️ This bucket's PR has been closed (https://github.com/pulumi/docs/pull/${pr_number}), so it can safely be deleted."
                    echo "   aws s3 rb s3://${bucket_name} --force"
                fi
            fi
        fi

        # If the current website bucket exists in this batch, note it, and increment the
        # counter that'll determine whether an older bucket can be safely deleted.
        if [ "$website_bucket_identified" == true ]; then
            buckets_beyond_current=$((buckets_beyond_current+1))
        fi
    else
        echo "Missing metadata file. This bucket may not have been built and tested successfully."
    fi
done

echo
echo "---"
echo
echo "To run browser tests on one of these buckets, run:"
echo "nvm use && make ensure && ./scripts/run-browser-tests.sh \"<bucket-url>\""
echo
echo "To pin the website to one of these buckets, run:"
echo "pulumi -C infrastructure config set originBucketNameOverride \"<bucket-name>\""
echo "pulumi -C infrastructure up"
echo
echo "To delete one of these buckets, run:"
echo "aws s3 rb \"s3://<bucket-name>\" --force"
echo
