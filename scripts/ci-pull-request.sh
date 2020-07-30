#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh preview
./scripts/bucketize.sh preview
./scripts/run-pulumi.sh preview
