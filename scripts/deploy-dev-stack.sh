#!/bin/bash

#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# This script runs a full site build, deploys to a unique S3 bucket, and runs Pulumi to deploy the specified stack.
#
# Usage:
#
#   ./scripts/deploy-dev-stack.sh                               # Runs a full build. Prompts for stack name and before update.
#   ./scripts/deploy-dev-stack.sh pulumi/stackname              # Runs a full build, skipping the prompt for stack name.
#   STACK_NAME=pulumi/stackname ./scripts/deploy-dev-stack.sh   # Same as above.
#   SKIP_BUILD=true ./scripts/deploy-dev-stack.sh               # Skips the build step and goes straight to deployment, but still prompts before update.
#   SKIP_PREVIEW=true ./scripts/deploy-dev-stack.sh             # Skips the preview before updating. (Is the same as passing --yes.)

echo
echo "Listing available stacks for this project..."
echo
pulumi -C infrastructure stack ls | grep -v "production" | grep -v "staging" | grep -v "testing"

stack_name="${STACK_NAME:=$1}"

if [ -z "$stack_name" ]; then
    echo
    read -p "Which stack would you like to deploy? " stack_name
fi

if [[ "$stack_name" == *production* || "$stack_name" == *staging* || "$stack_name" == *testing* ]]; then
    echo
    echo "Refusing to deploy the $stack_name stack with this script. Exiting."
    exit 0
fi

echo
echo "Selecting the $stack_name stack..."
pulumi -C infrastructure stack select "$stack_name"

if [[ -z "$SKIP_BUILD" || "$SKIP_BUILD" == false ]]; then
    echo
    echo "Running a build and deploying to S3..."

    # This environment variable doesn't actually correspond to any real environment; it just populates a variable
    # we use to name the S3 bucket. (In GHA, we use it to target a GHA environment, but in this context, it has no effect.)
    DEPLOYMENT_ENVIRONMENT="dev" ./scripts/on-demand-build-sync-test.sh
else
    echo
    echo "Skipping build..."
fi

echo
echo "Deploying..."
echo

if [[ "$SKIP_PREVIEW" == true ]]; then
    pulumi -C infrastructure up --skip-preview
else
    pulumi -C infrastructure up
fi

echo "Done!"
echo
echo "https://$(pulumi -C infrastructure stack output websiteDomain)"
echo
