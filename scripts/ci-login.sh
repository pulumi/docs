#!/bin/bash

set -o errexit -o pipefail

echo "Assuming the production CI role..."
eval $(assume-role "arn:aws:iam::058607598222:role/ContinuousIntegrationRole")

echo "Selecting the pulumi/production stack"
pulumi login
pulumi -C infrastructure stack select pulumi/production
