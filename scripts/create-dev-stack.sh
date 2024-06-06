#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# This script creates and configures a dev stack in the `pulumi` organization.
#
# Usage:
#
#   ./scripts/create-dev-stack.sh                         # Creates a new dev stack. Prompts for stack name.
#   ./scripts/create-dev-stack.sh stackname               # Same as above, but uses the passed-in argument for the stack name.
#   STACK_NAME=stackname ./scripts/create-dev-stack.sh    # Same as above, but uses the STACK_NAME environment variable instead.

stack_name="${STACK_NAME:=$1}"

if [ -z "$stack_name" ]; then
    echo
    echo "This script assumes you're logged into Pulumi Cloud and that you belong"
    echo "to the 'pulumi' organization. The stack will be created in that organization"
    echo "automatically, so you should omit the qualifying prefix 'pulumi/' from the name."
    echo
    read -p "What would you like to name this stack (e.g., 'christian')? " stack_name
fi

echo
echo "Creating pulumi/${stack_name}..."
echo

pulumi -C infrastructure stack init "pulumi/${stack_name}"
pulumi -C infrastructure config set aws:region us-west-2
pulumi -C infrastructure config set certificateArn "arn:aws:acm:us-east-1:372027080554:certificate/54d0431c-2cf9-4c40-bd3c-324cfb8b7d32"
pulumi -C infrastructure config set addSecurityHeaders true
pulumi -C infrastructure config set doEdgeRedirects true
pulumi -C infrastructure config set doAIAnswersRewrites true
pulumi -C infrastructure config set pathToOriginBucketMetadata "../origin-bucket-metadata.json"
pulumi -C infrastructure config set registryStack "pulumi/registry/testing"
pulumi -C infrastructure config set websiteDomain "www-${stack_name}.pulumi-dev.io"
pulumi -C infrastructure config set websiteLogsBucketName "www-${stack_name}.pulumi-dev.io-logs"

echo
echo "Done! The stack has been created and is now active:"
echo
pulumi -C infrastructure stack ls | grep -v "production" | grep -v "staging" | grep -v "testing"

echo
echo "To deploy, first open the dev-stacks environment:"
echo
echo '    eval "$(pulumi env open pulumi/dev-stacks --format shell)"'
echo
echo "Then run 'make deploy-dev-stack' (see ./scripts/deploy-dev-stack.sh for more options):"
echo
echo "    STACK_NAME=pulumi/${stack_name} make deploy-dev-stack"
echo
echo "Once deployed, your dev-stack site will be available at https://www-${stack_name}.pulumi-dev.io."
echo
echo "Don't forget to commit your stack configuration file:"
echo
echo "    git add infrastructure/Pulumi.${stack_name}.yaml"
echo "    git commit -m \"Add a dev stack for ${stack_name}\""
echo "    gh pr create"
