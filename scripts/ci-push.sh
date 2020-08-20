#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh
./scripts/sync-and-test-bucket.sh
./scripts/publish-sentry-release.sh
./scripts/run-pulumi.sh update
./scripts/make-s3-redirects.sh
