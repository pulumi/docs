#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci-login.sh

./scripts/build-site.sh
./scripts/sync-and-test-bucket.sh update

# Write the redirect objects into the new bucket before CloudFront is pointed at it.
# Hand-maintained redirects in scripts/redirects have no built object, so if this ran
# after run-pulumi.sh update they would return 404 until it finished. The script reads
# the bucket from the metadata file written above, not from the live origin.
./scripts/make-s3-redirects.sh

./scripts/generate-search-index.sh

node ./scripts/await-in-progress.js

./scripts/run-pulumi.sh update
