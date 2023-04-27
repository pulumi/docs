#!/bin/bash

set -o errexit -o pipefail

echo "Assuming the production CI role in AWS account..."
eval $(assume-role -duration "2h0m0s" "arn:aws:iam::388588623842:role/ContinuousIntegrationRole")

echo "Selecting the pulumi/www-production stack"
pulumi login
pulumi -C infrastructure stack select pulumi/www-production

