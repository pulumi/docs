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

# Stop starting new removals once we are past the deadline (epoch seconds), so a run ends
# cleanly before the AWS session credentials from ci-login.sh expire (they last two hours)
# instead of dying in the middle of a bucket. ci-bucket-cleanup.sh sets the deadline so that
# all of its invocations share one budget; if it's unset, give this invocation its own.
deadline="${BUCKET_CLEANUP_DEADLINE:-$(( $(date +%s) + ${BUCKET_CLEANUP_TIME_BUDGET_SECONDS:-5400} ))}"

skipped=0

for bucket in $buckets_to_remove; do
    if [ "$(date +%s)" -ge "$deadline" ]; then
        echo "Time budget exhausted; not removing ${bucket}."
        skipped=$((skipped + 1))
        continue
    fi

    echo "Removing ${bucket}..."

    # Use s5cmd rather than the AWS CLI for the deletes (see sync-and-test-bucket.sh for why).
    # It removes up to 1,000 keys per DeleteObjects request, where the CLI sends one request
    # per object. Each bucket is a full copy of the site, so that's the difference between
    # seconds and minutes per bucket.
    #
    # metadata.json is deleted last, rather than letting "rb --force" delete objects in
    # arbitrary order. list-recent-buckets.sh only treats a bucket as deletable if it can read
    # its metadata.json, so a removal that is interrupted (for example by expired credentials)
    # after that file is gone would leave a half-empty bucket that is never cleaned up. With
    # errexit set, a failure at any step stops the script with metadata.json still in place,
    # and the bucket is picked up again on the next run.
    s5cmd --log error rm --exclude "metadata.json" "s3://${bucket}/*"
    s5cmd --log error rm "s3://${bucket}/metadata.json"
    s5cmd --log error rb "s3://${bucket}"
    echo
done

if [ "$skipped" -gt 0 ]; then
    # Fail loudly rather than quietly falling behind: the failed workflow run is how
    # maintainers find out the cleanup can't keep up. The skipped buckets are still intact and
    # are retried on the next run.
    echo "Skipped ${skipped} bucket(s) because the time budget ran out." >&2
    exit 1
fi

echo "Done!"
