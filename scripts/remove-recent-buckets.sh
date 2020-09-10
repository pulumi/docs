#!/bin/bash

set -o errexit -o pipefail

# This script uses the list-recent-buckets script to find buckets that can be safely
# deleted, then deletes them. See that script for details, but in general, a bucket is
# deletable if and only if:
#
# * It's not currently serving the website AND some number of buckets behind the one
#   currently serving the website, or
# * It's associated with a PR that's been closed.

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

for bucket in $buckets_to_remove; do
    echo "Removing ${bucket}..."
    aws s3 rb "s3://${bucket}" --force
    echo
done

echo "Done!"
