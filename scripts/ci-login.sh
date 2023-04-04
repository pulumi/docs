#!/bin/bash

set -o errexit -o pipefail

# if being run by the new account workflow, then assume role in new account.
if [[ "$GITHUB_WORKFLOW" == "Build and deploy new account" ]]; then
    echo "Assuming the production CI role in **NEW** AWS account..."
    eval $(assume-role -duration "2h0m0s" "arn:aws:iam::388588623842:role/ContinuousIntegrationRole")

    pulumi login
    pulumi -C infrastructure stack select pulumi/www-production
else
    echo "Assuming the production CI role..."
    eval $(assume-role -duration "2h0m0s" "arn:aws:iam::058607598222:role/ContinuousIntegrationRole")
    echo "Selecting the pulumi/production stack"
    pulumi login
    pulumi -C infrastructure stack select pulumi/production
fi

