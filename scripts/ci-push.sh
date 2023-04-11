#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh


if [[ "$GITHUB_WORKFLOW" == "Build and deploy" ]]; then
    # Wait for in-progress jobs to complete before proceeding.
    ./scripts/build-site.sh
    ./scripts/sync-and-test-bucket.sh
    node ./scripts/await-in-progress.js
    ./scripts/run-pulumi.sh update
elif [[ "$GITHUB_WORKFLOW" == "Build and deploy new account" ]]; then
    # temporarily setting site to build in preview mode, to prevent search bots from indexing
    # until we cut over DNS to start routing to the new account.
    ./scripts/build-site.sh preview
    ./scripts/sync-and-test-bucket.sh
    node ./scripts/await-in-progress.js
    ./scripts/run-pulumi.sh update
else
    echo "the workflow, ${GITHUB_WORKFLOW}, is not recognized"
    exit 1
fi
./scripts/make-s3-redirects.sh
