#!/bin/bash

set -o errexit -o pipefail

# This script uses the list-recent-buckets script to find buckets that can be safely
# deleted, then deletes them. See that script for details, but in general, a bucket is
# deletable if and only if:
#
# * It's not currently serving the website AND some number of buckets behind the one
#   currently serving the website, or
# * It's associated with a PR that's been closed.

source ./scripts/common.sh

echo "Finding deletable $1 buckets..."

buckets_to_remove="$(./scripts/list-recent-buckets.sh "$1" --only-deletables)"

if [ -z "$buckets_to_remove" ]; then
    echo "None found."
    exit
fi

echo
echo "Buckets to remove:"
echo "$buckets_to_remove"
echo

# Each bucket is a full copy of the site (100k+ objects), and the AWS CLI deletes one object
# per request, 10 requests at a time by default. That is slow enough that a day's worth of
# buckets can take longer than the 2-hour lifetime of the AWS session credentials that
# ci-login.sh configures, at which point every request fails with ExpiredToken. Raise the
# CLI's S3 concurrency for this script only, using a throwaway config file so we never touch
# the caller's real AWS configuration.
aws_config_tmp="$(mktemp)"
trap 'rm -f "$aws_config_tmp"' EXIT
if [ -f "${AWS_CONFIG_FILE:-$HOME/.aws/config}" ]; then
    cat "${AWS_CONFIG_FILE:-$HOME/.aws/config}" > "$aws_config_tmp"
fi
export AWS_CONFIG_FILE="$aws_config_tmp"
aws configure set s3.max_concurrent_requests "${BUCKET_CLEANUP_CONCURRENCY:-100}" --profile "${AWS_PROFILE:-default}"
aws configure set s3.max_queue_size 10000 --profile "${AWS_PROFILE:-default}"

# Stop starting new removals once we are past the deadline (epoch seconds), so a run ends
# cleanly before the credentials expire instead of dying in the middle of a bucket. Whatever
# is left is picked up by the next scheduled run. ci-bucket-cleanup.sh sets the deadline so
# that all of its invocations share one budget; if it's unset, give this invocation its own.
deadline="${BUCKET_CLEANUP_DEADLINE:-$(( $(date +%s) + ${BUCKET_CLEANUP_TIME_BUDGET_SECONDS:-5400} ))}"

region="$(aws_region)"

for bucket in $buckets_to_remove; do
    if [ "$(date +%s)" -ge "$deadline" ]; then
        echo "Time budget exhausted; leaving the remaining buckets for the next run."
        break
    fi

    echo "Removing ${bucket}..."

    # Delete metadata.json last, rather than letting "rb --force" delete objects in arbitrary
    # order. list-recent-buckets.sh only treats a bucket as deletable if it can read its
    # metadata.json, so a removal that is interrupted after that file is gone would leave a
    # half-empty bucket that is never cleaned up. --only-show-errors keeps the log to
    # failures instead of one line per deleted object.
    aws s3 rm "s3://${bucket}" --recursive --exclude "metadata.json" --only-show-errors --region "$region"
    aws s3 rm "s3://${bucket}/metadata.json" --only-show-errors --region "$region"
    aws s3 rb "s3://${bucket}" --region "$region"
    echo
done

echo "Done!"
