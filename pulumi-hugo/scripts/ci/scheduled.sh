#!/bin/bash

set -o errexit -o pipefail

# This script runs the bucket-removal script to clean up old buckets produced by PR and push jobs.

# See if we have the requisite credentials. If not, we might be in a fork, so exit.
if [ -z "${AWS_ACCESS_KEY_ID:-}" ] || [ -z "${AWS_SECRET_ACCESS_KEY:-}" ]; then
    echo "Missing secret tokens, possibly due to a forked PR. Exiting."
    exit
fi

./scripts/ci/remove-buckets.sh push
./scripts/ci/remove-buckets.sh pr
