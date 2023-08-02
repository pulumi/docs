#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh
./scripts/sync-and-test-bucket.sh update

node ./scripts/await-in-progress.js

./scripts/run-pulumi.sh update
if [[ "$DEPLOYMENT_ENVIRONMENT" != "testing" ]]; then
    ./scripts/update-search-index.sh production
fi
./scripts/make-s3-redirects.sh
