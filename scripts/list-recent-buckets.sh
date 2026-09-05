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
#
#   # List all buckets
#   ./scripts/list-recent-buckets.sh
#
#   # List all buckets prefixed with "-pr-" (to filter pull_request builds)
#   ./scripts/list-recent-buckets.sh pr
#
#   # List all buckets prefixed with "-push-" (to filter push builds)
#   ./scripts/list-recent-buckets.sh push
#
#   # List all buckets prefixed with "-schedule-" or "-workflow-dispatch-", etc.
#   ./scripts/list-recent-buckets.sh schedule
#   ./scripts/list-recent-buckets.sh workflow-dispatch
#
#   # List every deploy-path bucket (push, schedule, workflow-dispatch, ... -- everything
#   # except PR previews) as one combined, correctly-ranked retention window. Prefer this
#   # over the individual event filters above when checking what's safe to delete: push,
#   # schedule, and workflow-dispatch buckets all draw from the same 10-bucket retention
#   # window, and filtering to a single event first can hide the live bucket from that
#   # window when the live bucket happened to come from a different event.
#   ./scripts/list-recent-buckets.sh deploy
#
#   # List only the buckets that can be safely deleted
#   ./scripts/list-recent-buckets.sh [push | schedule | workflow-dispatch | deploy | pr] --only-deletables

source ./scripts/common.sh

bucket_prefix="$1"

# "deploy" is a virtual filter, not a real bucket-name prefix: it means "every deploy-path
# bucket, regardless of which event produced it". We pass no prefix to get_recent_buckets so
# the query returns push, schedule, workflow-dispatch, *and* pr buckets together (AWS has no
# server-side "not pr" filter), then skip the pr ones below when doing the retention count,
# so the live bucket is never missing from the window just because it came from an event
# this invocation didn't ask for individually.
if [ "$bucket_prefix" == "deploy" ]; then
    query_prefix=""
    listing_description="every deploy-path bucket (all events except PR previews)"
else
    query_prefix="$bucket_prefix"
    listing_description="the prefix $(origin_bucket_prefix)-${bucket_prefix}"
fi

buckets=$(get_recent_buckets $query_prefix)
buckets_as_array=($buckets)
bucket_count=${#buckets_as_array[@]}
only_deletables=false

# Any bucket-prefix filter can be flagged as deletable -- "pr" gets the closed-PR check
# below, and every deploy-path filter (push, schedule, workflow-dispatch, deploy) gets the
# beyond-the-currently-served-bucket check. Listing with no filter at all isn't deletable,
# since "all buckets" isn't a coherent retention policy -- guard on $1 being non-empty, not
# just non-"pr", or an unfiltered listing would apply the deploy-path retention rule to PR
# preview buckets too.
if [[ -n "$1" && "$2" == "--only-deletables" ]]; then
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
    maybe_echo "No recent buckets matching ${listing_description} were found."
    exit
fi

# Check if WEBSITE_URL is set
if [ -z "$WEBSITE_URL" ]; then
  echo "WEBSITE_URL is not set."
  exit 1
fi

# Query for the bucket currently serving pulumi.com.
currently_deployed_bucket="$(curl -s ${WEBSITE_URL}/metadata.json | jq -r '.bucket' || echo '')"

maybe_echo "Found ${bucket_count} recent buckets matching ${listing_description}:"

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
    metadata="$(aws s3 cp "s3://${bucket}/metadata.json" --region $(aws_region) 2>/dev/null - || echo '')"

    if [ ! -z "$metadata" ]; then
        bucket_url="$(echo $metadata | jq -r '.url')"
        bucket_name="$(echo $metadata | jq -r '.bucket')"
        bucket_timestamp="$(echo $metadata | jq -r '.timestamp / 1000 | strftime("%Y-%m-%d %H:%M:%S UTC")')"
        bucket_commit="$(echo $metadata | jq -r '.commit')"

        maybe_echo "Bucket URL:  ${bucket_url}"
        maybe_echo "Bucket Name: ${bucket_name}"
        maybe_echo "Synced At:   ${bucket_timestamp}"
        maybe_echo "Commit:      https://github.com/pulumi/docs/commit/${bucket_commit}"

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

        # A PR-preview bucket in the "deploy" listing's combined result set (see the
        # query_prefix note above) has its own closed-PR retention rule below and must not
        # be counted toward, or offered up under, the deploy-path beyond-current-website
        # check: mixing the two would let stale PR previews eat into the 10-bucket deploy
        # retention window, and vice versa.
        is_pr_bucket=false
        if [[ "$bucket_name" == "$(origin_bucket_prefix)-pr-"* ]]; then
            is_pr_bucket=true
        fi

        # For deploy-path buckets (anything other than PR previews), indicate whether they
        # can be safely deleted based on how far behind the live website bucket they are.
        # This covers push, schedule, and workflow-dispatch builds alike -- they all share
        # the same origin_bucket_prefix()-<event>-<sha>[-<uniquifier>] shape and the same
        # single currently-deployed-bucket check above. Requiring a non-empty $1 keeps an
        # unfiltered listing (all buckets, PR previews included) from applying this rule to
        # buckets whose real retention rule is the closed-PR check below.
        if [ -n "$1" ] && [ "$1" != "pr" ] && [ "$is_pr_bucket" == false ]; then
            if [ "$buckets_beyond_current" -gt "$buckets_to_retain" ]; then
                maybe_echo
                maybe_echo "❌ This bucket is ${buckets_beyond_current} buckets behind the current website, so it can safely be deleted."
                maybe_echo "   aws s3 rb s3://${bucket_name} --region $(aws_region) --force"

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
                "https://api.github.com/repos/pulumi/docs/pulls/${pr_number}" || echo "{}")"

            pr_state="$(echo $pr_metadata | jq -r '.state')"

            if [ "$pr_state" == "closed" ]; then
                maybe_echo
                maybe_echo "❌ This bucket's PR state is ${pr_state} (https://github.com/pulumi/docs/pull/${pr_number}), so it can safely be deleted."
                maybe_echo "   aws s3 rb s3://${bucket_name} --region $(aws_region) --force"

                deletables+=($bucket_name)
            fi
        fi

        # If the current website bucket exists in this batch, note it, and increment the
        # counter that'll determine whether an older bucket can be safely deleted. A PR
        # bucket encountered here (only possible in "deploy" mode's combined listing) is
        # skipped: it draws from the closed-PR retention rule, not this 10-bucket window,
        # and counting it here would shrink that window for the deploy-path buckets it's
        # actually meant to protect.
        if [ "$website_bucket_identified" == true ] && [ "$is_pr_bucket" == false ]; then
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
maybe_echo "   make ensure && ./scripts/run-browser-tests.sh \"<bucket-url>\""
maybe_echo
maybe_echo "📌 To pin the website to one of these buckets, run:"
maybe_echo "   pulumi -C infrastructure config set originBucketNameOverride \"<bucket-name>\""
maybe_echo "   pulumi -C infrastructure up"
maybe_echo
maybe_echo "❌ To delete one of these buckets, run:"
maybe_echo "   aws s3 rb \"s3://<bucket-name>\" --region $(aws_region) --force"
maybe_echo

if [ ${#deletables} -gt 0 ]; then
    maybe_echo "💥 To delete all buckets identified above as deletable, run:"

    for deletable in ${deletables[@]}; do
        if [ $only_deletables == true ]; then
            echo "$deletable"
        else
            echo "   aws s3 rb \"s3://${deletable}\" --region $(aws_region) --force"
        fi
    done

    maybe_echo
fi
