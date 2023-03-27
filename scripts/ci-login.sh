#!/bin/bash

set -o errexit -o pipefail

if [[ "$GITHUB_WORKFLOW" == "Build and deploy" ]]; then
    echo "Assuming the production CI role..."
    eval $(assume-role -duration "2h0m0s" "arn:aws:iam::058607598222:role/ContinuousIntegrationRole")
    echo "Selecting the pulumi/production stack"
    pulumi login
    pulumi -C infrastructure stack select pulumi/production
elif [[ "$GITHUB_WORKFLOW" == "Build and deploy new account" ]]; then
    echo "Assuming the production CI role in new AWS account..."
    # change this ARN to reference CI Role in new account.
    eval $(assume-role -duration "2h0m0s" "arn:aws:iam::058607598222:role/ContinuousIntegrationRole")
    # uncomment below when migration is complete and update stack selection to select the production stack
    # that manages the new environment.
    # pulumi login
    # pulumi -C infrastructure stack select pulumi/production
else
    echo "the workflow, ${GITHUB_WORKFLOW}, is not recognized"
    exit 1
fi

