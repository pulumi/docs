#!/bin/bash

set -o errexit -o pipefail

# Essentially we follow what scripts/ci-push.sh does, but without assuming role into the
# prod account as we do in CI. This script assumes you've exported read/write credentials
# for the production AWS account into your current shell and that you have write access to
# the pulumi/www.pulumi.com/production stack. Also assumes you've installed Node, Yarn,
# Go, Hugo, Pulumi, and the AWS CLI; see the build-and-deploy workflow for the versions we
# currently use in CI.
# https://github.com/pulumi/docs/blob/master/.github/workflows/build-and-deploy.yml

echo "Your environment info --"
echo
echo "Tools":
echo "node $(node -v)"
echo "yarn $(yarn -v)"
go version
hugo version
aws --version
echo
echo "Git SHA:"
git rev-parse HEAD
echo
echo "Pulumi:"
pulumi whoami -v
echo
echo "AWS:"
aws sts get-caller-identity
echo

read -e -p "You should see that:

* You have the latest Git commit from https://github.com/pulumi/docs master
* You're logged into https://app.pulumi.com and have access to the pulumi organization
* You're logged into the production AWS account

Do these look right? [y/n]? " yesno_identity

if [[ "$yesno_identity" != [Yy]* ]]; then
    echo "Ok, exiting."
    exit
fi

exit

# Select the production stack.
pulumi -C infrastructure stack select pulumi/production

# Ensure you can build the resource docs. (We build a Go binary and output to '${GOPATH}/bin', then call it by name.)
export PATH="${GOPATH}/bin:$PATH"

# Build the full site.
./scripts/build-site.sh

# Create a new bucket, populate it, test it, and drop off an origin-bucket-metadata.json
# file. (The Pulumi program needs this file in order to run the deployment.)
./scripts/sync-and-test-bucket.sh

echo
read -e -p "The bucket is ready. Please take a moment to verify it at the bucket URL above.

Proceed with deployment? [y/n] " yesno_deploy

if [[ "$yesno_deploy" != [Yy]* ]]; then
    echo "Ok, exiting."
    exit
fi

# Run a preview and pause to confirm before running the update.
pulumi -C infrastructure up

# Once the update completes, update all redirects to use proper 301s.
./scripts/make-s3-redirects.sh
