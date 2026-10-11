#!/bin/bash

set -o errexit -o pipefail

# This script runs the bucket-removal script to clean up old buckets produced by PR, push,
# scheduled, and manually-triggered (workflow_dispatch) build-and-deploy.yml jobs.
#
# push, schedule, and workflow-dispatch buckets all draw from the same 10-bucket retention
# window (they're all deploy-path buckets competing to stay within buckets_to_retain of the
# live website bucket), so they're cleaned up together via the "deploy" pseudo-filter, not
# with one invocation per event: filtering to a single event first would hide the live
# bucket from the window whenever it happened to come from a different event, stalling that
# invocation's retention count at zero. See list-recent-buckets.sh for the full rationale.
if [ -z "${AWS_ACCESS_KEY_ID:-}" ] || [ -z "${AWS_SECRET_ACCESS_KEY:-}" ]; then
    echo "Missing secret tokens, possibly due to a forked PR. Exiting."
    exit
fi

source ./scripts/ci-login.sh

./scripts/remove-recent-buckets.sh deploy
./scripts/remove-recent-buckets.sh pr
