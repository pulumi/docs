#!/bin/bash

# Runs typedoc on various Pulumi repos and copies them to 
# the /libraries folder.

set -o nounset -o errexit -o pipefail

PULUMI_AWS_DOCS=`mktemp -d`
PULUMI_DOCS=`mktemp -d`
PULUMI_CLOUD_DOCS=`mktemp -d`

# pulumi-aws
echo -e "\033[0;95mrunning typedoc on pulumi-aws\033[0m"
pushd .
cd ../pulumi-aws/pack
typedoc . --mode modules --readme none --out $PULUMI_AWS_DOCS
popd

# pulumi-fabric
echo -e "\033[0;95mrunning typedoc on pulumi\033[0m"
pushd .
cd ../pulumi/sdk/nodejs
typedoc . --mode modules --readme none --out $PULUMI_DOCS
popd


# pulumi-framework
echo -e "\033[0;95mrunning typedoc on pulumi-cloud\033[0m"
pushd .
cd ../pulumi-cloud/api
typedoc . --mode modules --readme none --out $PULUMI_CLOUD_DOCS
popd

echo "Finished running typedoc. Copying into /libraries."
mkdir -p ./libraries/

# Purge existing
rm -rf ./libraries/pulumi-aws/
rm -rf ./libraries/pulumi/
rm -rf ./libraries/pulumi-cloud/

mkdir ./libraries/pulumi-aws/
mkdir ./libraries/pulumi/
mkdir ./libraries/pulumi-cloud/

# Copy updated
cp -R $PULUMI_AWS_DOCS/   ./libraries/pulumi-aws/
cp -R $PULUMI_DOCS/       ./libraries/pulumi/
cp -R $PULUMI_CLOUD_DOCS/ ./libraries/pulumi-cloud/

# Cleanup
rm -rf $PULUMI_AWS_DOCS
rm -rf $PULUMI_DOCS
rm -rf $PULUMI_CLOUD_DOCS

echo "Done"