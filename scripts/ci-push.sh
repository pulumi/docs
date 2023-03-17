#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh
./scripts/sync-and-test-bucket.sh

if [[ "$GITHUB_WORKFLOW" == "Build and deploy" ]]; then
    # Wait for in-progress jobs to complete before proceeding.
    node ./scripts/await-in-progress.js
    ./scripts/run-pulumi.sh update
fi
./scripts/make-s3-redirects.sh
