#!/bin/bash

set -o errexit -o pipefail

# See if we have the requisite credentials. If not, we might be in a fork. In that case,
# run a PR build, but skip all the deployment stuff.
if [ -z "${AWS_ACCESS_KEY_ID:-}" ] || [ -z "${AWS_SECRET_ACCESS_KEY:-}" ] || [ -z "${PULUMI_ACCESS_TOKEN:-}" ]; then
    echo "Missing secret tokens, possibly due to a forked PR."
    echo "Running a build, but will skip the sync to S3 and Pulumi preview."
    ./scripts/build-site.sh preview
    exit
fi

source ./scripts/ci-login.sh

./scripts/build-site.sh preview
./scripts/sync-and-test-bucket.sh preview

./scripts/generate-search-index.sh

./scripts/run-pulumi.sh preview
./scripts/make-s3-redirects.sh

# Temporarily disable 404 detection (too many false positives)
# ./scripts/detect-new-404s.sh

# Run Lighthouse performance audit on the preview deployment, but only when the
# PR contains changes that could meaningfully affect performance scores (layouts,
# CSS/JS bundles, Hugo config, etc.). Content-only changes are skipped.
performance_paths=(
    "^layouts/"
    "^theme/"
    "^assets/"
    "^static/js/"
    "^static/css/"
    "^static/fonts/"
    "^static/icons/"
    "^static/images/"
    "^static/logos/"
    "^config/"
    "^hugo\."
)
performance_pattern="$(IFS="|"; echo "${performance_paths[*]}")"
changed_files="$(git diff --name-only origin/master...HEAD 2>/dev/null || true)"

if echo "$changed_files" | grep -qE "$performance_pattern"; then
    echo "Performance-relevant files changed. Running Lighthouse audit..."
    ./scripts/run-lighthouse-pr.sh || true
else
    echo "No performance-relevant file changes detected. Skipping Lighthouse audit."
fi
