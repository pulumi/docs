#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh
./scripts/sync-and-test-bucket.sh update

node ./scripts/await-in-progress.js

./scripts/run-pulumi.sh update
# ./scripts/update-search-index.sh production

./scripts/make-s3-redirects.sh
