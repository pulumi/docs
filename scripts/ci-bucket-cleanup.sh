#!/bin/bash

set -o errexit -o pipefail

# This script runs the bucket-removal script to clean up old buckets produced by PR, push,
# scheduled, and manually-triggered (workflow_dispatch) build-and-deploy.yml jobs. push,
# schedule, and workflow-dispatch buckets share the same origin_bucket_prefix()-<event>-<sha>
# naming shape and the same currently-deployed-bucket retention check, so they're each
# passed through individually here (list-recent-buckets.sh filters by exact prefix match).
if [ -z "${AWS_ACCESS_KEY_ID:-}" ] || [ -z "${AWS_SECRET_ACCESS_KEY:-}" ]; then
    echo "Missing secret tokens, possibly due to a forked PR. Exiting."
    exit
fi

source ./scripts/ci-login.sh

./scripts/remove-recent-buckets.sh push
./scripts/remove-recent-buckets.sh schedule
./scripts/remove-recent-buckets.sh workflow-dispatch
./scripts/remove-recent-buckets.sh pr
