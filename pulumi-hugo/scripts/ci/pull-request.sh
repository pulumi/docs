#!/bin/bash

set -o errexit -o pipefail

# See if we have the requisite credentials. If not, we might be in a fork. In that case,
# run a PR build, but skip all the deployment stuff.
if [ -z "${AWS_ACCESS_KEY_ID:-}" ] || [ -z "${AWS_SECRET_ACCESS_KEY:-}" ] || [ -z "${PULUMI_ACCESS_TOKEN:-}" ]; then
    echo "Missing secret tokens, possibly due to a forked PR."
    echo "Running a build, but will skip the sync to S3 and Pulumi preview."
    ./scripts/ci/build.sh
    exit
fi

aws sts get-caller-identity

./scripts/ci/build.sh
./scripts/ci/sync.sh
