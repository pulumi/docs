#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh
./scripts/sync-and-test-bucket.sh
./scripts/publish-sentry-release.sh

# Wait for in-progress jobs to complete before proceeding.
node ./scripts/await-in-progress.js

./scripts/run-pulumi.sh update
./scripts/make-s3-redirects.sh
