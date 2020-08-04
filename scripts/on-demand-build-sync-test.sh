#!/bin/bash

#!/bin/bash

set -o errexit -o pipefail

# This script runs a full site build, creates an S3 bucket for it, pushes to that bucket,
# tests it, and tags the bucket as being associated with the current Git SHA. It is
# intended to be used for local development with dev stacks, but can be used in any
# context that requires a full build with a corresponding bucket.

source ./scripts/common.sh

# In CI contexts, this identifier (defined in common.sh) will be set automatically based
# on the environment, but when running builds manually, we need to set it ourselves.
export BUILD_IDENTIFIER="$(git_sha_short)-$(current_time_in_ms)"

./scripts/build-site.sh
./scripts/sync-and-test-bucket.sh
./scripts/make-s3-redirects.sh
