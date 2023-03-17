#!/bin/bash

set -o errexit -o pipefail

if [[ "$GITHUB_WORKFLOW" == "Build and deploy new account" ]]; then
    echo "Assuming the production CI role in new AWS account..."
    # change this ARN to reference CI Role in new account.
    eval $(assume-role -duration "2h0m0s" "arn:aws:iam::058607598222:role/ContinuousIntegrationRole")
    # pulumi login
    # pulumi -C infrastructure stack select pulumi/production
else
    echo "Assuming the production CI role..."
    eval $(assume-role -duration "2h0m0s" "arn:aws:iam::058607598222:role/ContinuousIntegrationRole")
    echo "Selecting the pulumi/production stack"
    pulumi login
    pulumi -C infrastructure stack select pulumi/production
fi

