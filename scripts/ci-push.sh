#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh
./scripts/bucketize.sh
./scripts/run-pulumi.sh update
./scripts/make-s3-redirects.sh
