#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# This script destroys a dev stack in the `pulumi` organization.
#
# Usage:
#
#   ./scripts/destroy-dev-stack.sh                         # Destroys a dev stack. Prompts for stack name.
#   ./scripts/destroy-dev-stack.sh stackname               # Same as above, but uses the passed-in argument for the stack name.
#   STACK_NAME=stackname ./scripts/destroy-dev-stack.sh    # Same as above, but uses the STACK_NAME environment variable instead.

stack_name="${STACK_NAME:=$1}"

if [ -z "$stack_name" ]; then
    echo
    echo "This script assumes you're logged into Pulumi Cloud and that you belong"
    echo "to the 'pulumi' organization."
    echo
    echo "Available stacks:"
    echo
    pulumi -C infrastructure stack ls | grep -v "production" | grep -v "staging" | grep -v "testing"
    echo
    read -p "Which stack do you want to destroy? " stack_name
fi

if [[ "$stack_name" == *production* || "$stack_name" == *staging* || "$stack_name" == *testing* ]]; then
    echo
    echo "Refusing to deploy the $stack_name stack with this script. Exiting."
    exit 0
fi

echo
echo "Selecting the $stack_name stack..."
pulumi -C infrastructure stack select "$stack_name"

echo
echo "Destroying ${stack_name}..."

echo
echo "Emptying the contents of potentially non-empty buckets..."
echo
stack_name_only=$(echo $stack_name | sed -e 's/\(pulumi\/\)//')

pushd infrastructure
    for resource_name in "website-logs-bucket" "uploads-bucket" "fallback-bucket"; do
        if [[ "$(pulumi stack --show-urns | grep 'website-logs-bucket')" != "" ]]; then
            resource_id=$(pulumi stack export | jq -r -C ".deployment.resources[] | select(.urn == \"urn:pulumi:${stack_name_only}::www.pulumi.com::aws:s3/bucket:Bucket::${resource_name}\").id" || true)

            if [[ "$resource_id" != "" ]]; then
                echo "Emptying ${resource_name}..."
                aws s3 rm --recursive "s3://${resource_id}"
            fi
        fi
    done
popd

pulumi -C infrastructure refresh --yes

echo
echo "Unprotecting protected resources..."
echo
pulumi -C infrastructure state unprotect --yes "urn:pulumi:${stack_name_only}::www.pulumi.com::aws:route53/record:Record::www-${stack_name_only}.pulumi-dev.io" || true
pulumi -C infrastructure state unprotect --yes "urn:pulumi:${stack_name_only}::www.pulumi.com::aws:cloudfront/distribution:Distribution::cdn" || true
pulumi -C infrastructure state unprotect --yes "urn:pulumi:${stack_name_only}::www.pulumi.com::aws:s3/bucket:Bucket::website-logs-bucket" || true

echo
echo "Destroying..."
echo
pulumi -C infrastructure destroy --yes --continue-on-error

echo
echo "Done! The stack has been destroyed. If you're an administrator of this stack, you may now remove it with 'pulumi stack rm'".
