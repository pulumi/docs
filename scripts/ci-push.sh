#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh
./scripts/sync-and-test-bucket.sh update

./scripts/generate-search-index.sh

node ./scripts/await-in-progress.js

./scripts/run-pulumi.sh update
./scripts/make-s3-redirects.sh