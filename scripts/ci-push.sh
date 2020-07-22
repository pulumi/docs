#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/find-or-make-bucket.sh
./scripts/run-pulumi.sh update
./scripts/make-s3-redirects.sh
