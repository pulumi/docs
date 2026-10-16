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

region="$(aws_region)"
metadata_backup="$(mktemp)"
trap 'rm -f "$metadata_backup"' EXIT

# remove_bucket empties and deletes the given bucket. If it can't, it returns non-zero with
# the bucket's metadata.json in place, so the bucket is picked up again on the next run.
#
# It's called as an "if" condition so that one bad bucket doesn't stop the rest of the run,
# which also means errexit doesn't apply inside it: every step has to check for itself.
remove_bucket() {
    local bucket="$1"

    # list-recent-buckets.sh only treats a bucket as deletable if it can read its
    # metadata.json, so a bucket that loses that file and then can't be removed is never
    # cleaned up. Keep a copy to put back if that happens.
    aws s3 cp "s3://${bucket}/metadata.json" "$metadata_backup" --region "$region" --only-show-errors || return 1

    # Use s5cmd rather than the AWS CLI for the deletes (see sync-and-test-bucket.sh for why).
    # It removes up to 1,000 keys per DeleteObjects request, where the CLI sends one request
    # per object. Each bucket is a full copy of the site, so that's the difference between
    # seconds and minutes per bucket.
    #
    # metadata.json is deleted last, rather than letting "rb --force" delete objects in
    # arbitrary order, so a removal that is interrupted (for example by expired credentials)
    # partway through the objects stops with that file still in place.
    s5cmd --log error rm --exclude "metadata.json" "s3://${bucket}/*" || return 1
    s5cmd --log error rm "s3://${bucket}/metadata.json" || return 1

    if s5cmd --log error rb "s3://${bucket}"; then
        return 0
    fi

    # s5cmd's rm can exit 0 and still leave objects behind. In production it left hundreds of
    # ordinary keys in contiguous runs, and it also silently skips any key that ends in "/"
    # (it treats those as directories). Fall back to the AWS CLI, which deletes whatever is
    # left before removing the bucket. On a bucket s5cmd has emptied, that's one short
    # listing. The pause gives S3 a moment in case it's just slow to see the bucket as empty.
    echo "Retrying the removal of ${bucket} with the AWS CLI..."
    sleep 10
    if aws s3 rb "s3://${bucket}" --force --region "$region"; then
        return 0
    fi

    # Still there. Show what's keeping it, before metadata.json goes back in: object versions
    # or delete markers mean versioning was turned on for the bucket, and neither tool
    # removes those.
    echo "Objects left in ${bucket}:" >&2
    aws s3api list-object-versions --bucket "$bucket" --max-items 10 --region "$region" \
        --query '{Versions: Versions[].Key, DeleteMarkers: DeleteMarkers[].Key}' --output json >&2 || true

    aws s3 cp "$metadata_backup" "s3://${bucket}/metadata.json" --acl public-read --region "$region" --only-show-errors
    return 1
}

skipped=0
failed=0

for bucket in $buckets_to_remove; do
    if [ "$(date +%s)" -ge "$deadline" ]; then
        echo "Time budget exhausted; not removing ${bucket}."
        skipped=$((skipped + 1))
        continue
    fi

    echo "Removing ${bucket}..."

    if ! remove_bucket "$bucket"; then
        echo "Couldn't remove ${bucket}; it will be retried on the next run." >&2
        failed=$((failed + 1))
    fi
    echo
done

# Fail loudly rather than quietly falling behind: the failed workflow run is how maintainers
# find out the cleanup can't keep up. The buckets left behind are retried on the next run.
if [ "$failed" -gt 0 ]; then
    echo "Failed to remove ${failed} bucket(s); see the errors above." >&2
fi

if [ "$skipped" -gt 0 ]; then
    echo "Skipped ${skipped} bucket(s) because the time budget ran out." >&2
fi

if [ "$failed" -gt 0 ] || [ "$skipped" -gt 0 ]; then
    exit 1
fi

echo "Done!"
