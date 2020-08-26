#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh
./scripts/sync-and-test-bucket.sh

if [ -n "${SENTRY_AUTH_TOKEN:-}" ]; then
  echo "Publishing Sentry release..."
  ./scripts/publish-sentry-release.sh
else
  echo "Sentry auth token not found. Will skip publishing release to Sentry."
fi

if [ -n "${PULUMI_STACK_NAME:-}" ]; then
  ./scripts/run-pulumi.sh update
  ./scripts/make-s3-redirects.sh
else
  echo "PULUMI_STACK_NAME is not set. Will skip running the update."
fi
