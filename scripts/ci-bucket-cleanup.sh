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

# The AWS credentials from ci-login.sh expire after two hours, so give both invocations below
# a single shared deadline comfortably inside that window. Each invocation stops starting new
# removals once the deadline passes and exits non-zero if it had to skip any. Run both before
# reporting failure so that a slow "deploy" pass doesn't prevent the "pr" pass from running.
export BUCKET_CLEANUP_DEADLINE="$(( $(date +%s) + ${BUCKET_CLEANUP_TIME_BUDGET_SECONDS:-5400} ))"

status=0
./scripts/remove-recent-buckets.sh deploy || status=1
./scripts/remove-recent-buckets.sh pr || status=1
exit "$status"
