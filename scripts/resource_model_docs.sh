#!/bin/bash
set -o nounset -o errexit -o pipefail

echo "Building AWS resource docs..."
pushd ../pulumi-aws
make ensure && make build
popd

echo "Removing the providers/aws dir..."
rm -rf ./content/docs/reference/providers/aws

echo "Copying generated AWS provider docs to providers/aws..."
cp -r ~/go/src/github.com/pulumi/pulumi-aws/sdk/docs/ ./content/docs/reference/providers/aws/
