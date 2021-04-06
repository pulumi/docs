#!/bin/bash

set -o errexit -o pipefail

# This script lists the 100 most recent S3 buckets populated from preview build jobs. It
# works by querying S3 for buckets with names matching our bucket naming prefix,
# then fetches the metadata files we generate with each build, outputting their results.
#
# For buckets built by `pull_request` and `push` jobs, the script will also tell you
# whether a given bucket can be safely deleted.
#
# Usage:
#
#   # List all buckets
#   ./scripts/ci/list-buckets.sh
#
#   # List all buckets prefixed with "-pr-" (to filter pull_request builds)
#   ./scripts/ci/list-buckets.sh pr
#
#   # List all buckets prefixed with "-push-" (to filter push builds)
#   ./scripts/ci/list-buckets.sh push
#
#   # List only the buckets that can be safely deleted
#   ./scripts/ci/list-buckets.sh [push | pr] --only-deletables

source ./scripts/ci/common.sh

bucket_prefix="$1"
buckets=$(get_recent_buckets $bucket_prefix)
buckets_as_array=($buckets)
bucket_count=${#buckets_as_array[@]}
only_deletables=false

# Only pr and push buckets can be flagged as deletable.
if [[ ( "$1" == "pr" || "$1" == "push" )  && "$2" == "--only-deletables" ]]; then
    only_deletables=true
fi

# maybe_echo suppresses output to make lists more scriptable. There's probably a Bashier
# way to do this, but hey, it works.
maybe_echo() {
    if [ $only_deletables == false ]; then
        echo "$1"
    fi
}

if [ "$bucket_count" == "0" ]; then
    maybe_echo "No recent buckets matching the prefix $(origin_bucket_prefix)-${bucket_prefix} were found."
    exit
fi

# Query for the bucket currently serving pulumi.com.
currently_deployed_bucket="$(curl -s https://www.pulumi.com/metadata.json | jq -r '.bucket' || echo '')"

maybe_echo "Found ${bucket_count} recent buckets matching the prefix $(origin_bucket_prefix)-${bucket_prefix}:"

# Variables used for determining whether a push-built bucket is safe to delete.

# The number of buckets beyond the currently deployed one that should be retained.
buckets_to_retain=10

# A counter for tracking how many builds behind the current website a given bucket is.
buckets_beyond_current=0

# A flag denoting whether the current website bucket exists in the current result set.
website_bucket_identified=false

# The array of deletable buckets, if any.
deletables=()

for bucket in $buckets; do
    maybe_echo
    maybe_echo "Fetching metadata for ${bucket}..."
    metadata="$(aws s3 cp "s3://${bucket}/metadata.json" 2>/dev/null - || echo '')"

    if [ ! -z "$metadata" ]; then
        bucket_url="$(echo $metadata | jq -r '.url')"
        bucket_name="$(echo $metadata | jq -r '.bucket')"
        bucket_timestamp="$(echo $metadata | jq -r '.timestamp / 1000 | strftime("%Y-%m-%d %H:%M:%S UTC")')"
        bucket_commit="$(echo $metadata | jq -r '.commit')"

        maybe_echo "Bucket URL:  ${bucket_url}"
        maybe_echo "Bucket Name: ${bucket_name}"
        maybe_echo "Synced At:   ${bucket_timestamp}"
        maybe_echo "Commit:      https://github.com/pulumi/$(repo_name)/commit/${bucket_commit}"

        # Call out whether this bucket is the one currently serving pulumi.com.
        if [ "$bucket_name" == "$currently_deployed_bucket" ]; then
            maybe_echo
            maybe_echo "*"
            maybe_echo "*"
            maybe_echo "* ☝️  Head's up!"
            maybe_echo "*    This bucket (${bucket_name}) is currently serving pulumi.com."
            maybe_echo "*    https://www.pulumi.com/metadata.json"
            maybe_echo "*"
            maybe_echo "*"

            website_bucket_identified=true
        fi

        # For push or pull_request buckets, indicate whether they can be safely deleted.
        if [ "$1" == "push" ]; then
            if [ "$buckets_beyond_current" -gt "$buckets_to_retain" ]; then
                maybe_echo
                maybe_echo "❌ This bucket is ${buckets_beyond_current} buckets behind the current website, so it can safely be deleted."
                maybe_echo "   aws s3 rb s3://${bucket_name} --force"

                deletables+=($bucket_name)
            fi
        elif [ "$1" == "pr" ]; then

            # Parse the bucket name for the PR number. A bit gross, but more reliable than
            # asking GitHub for the PR associated with a commit, because commits are often
            # removed when squashed or rebased.
            pr_number="$(echo $bucket_name | sed "s/^$(origin_bucket_prefix)-pr-\([0-9]*\)-.*$/\1/")"
            pr_metadata="$(curl \
                -s \
                -f \
                -H "Authorization: token ${GITHUB_TOKEN}" \
                "https://api.github.com/repos/pulumi/$(repo_name)/pulls/${pr_number}" || echo "{}")"

            pr_state="$(echo $pr_metadata | jq -r '.state')"

            if [ "$pr_state" == "closed" ]; then
                maybe_echo
                maybe_echo "❌ This bucket's PR state is ${pr_state} (https://github.com/pulumi/$(repo_name)/pull/${pr_number}), so it can safely be deleted."
                maybe_echo "   aws s3 rb s3://${bucket_name} --force"

                deletables+=($bucket_name)
            fi
        fi

        # If the current website bucket exists in this batch, note it, and increment the
        # counter that'll determine whether an older bucket can be safely deleted.
        if [ "$website_bucket_identified" == true ]; then
            buckets_beyond_current=$((buckets_beyond_current+1))
        fi
    else
        maybe_echo "Missing metadata file. This bucket may not have been built and tested successfully."
    fi
done

maybe_echo
maybe_echo "---"
maybe_echo
maybe_echo "✅ To run browser tests on one of these buckets, run:"
maybe_echo "   nvm use && make ensure && ./scripts/run-browser-tests.sh \"<bucket-url>\""
maybe_echo
maybe_echo "📌 To pin the website to one of these buckets, run:"
maybe_echo "   pulumi -C infrastructure config set originBucketNameOverride \"<bucket-name>\""
maybe_echo "   pulumi -C infrastructure up"
maybe_echo
maybe_echo "❌ To delete one of these buckets, run:"
maybe_echo "   aws s3 rb \"s3://<bucket-name>\" --force"
maybe_echo

if [ ${#deletables} -gt 0 ]; then
    maybe_echo "💥 To delete all buckets identified above as deletable, run:"

    for deletable in ${deletables[@]}; do
        if [ $only_deletables == true ]; then
            echo "$deletable"
        else
            echo "   aws s3 rb \"s3://${deletable}\" --force"
        fi
    done

    maybe_echo
fi
