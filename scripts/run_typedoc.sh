#!/bin/bash

# Runs typedoc on various Pulumi repos and copies them to 
# the /libraries folder.

set -o nounset -o errexit -o pipefail

PULUMI_AWS_DOCS=`mktemp -d -t "typedoc-aws"`
PULUMI_FABRIC_DOCS=`mktemp -d -t "typedoc-fabric"`
PULUMI_FRAMEWORK_DOCS=`mktemp -d -t "typedoc-framework"`

# pulumi-aws
echo -e "\033[0;95mrunning typedoc on pulumi-aws\033[0m"
pushd .
cd ../pulumi-aws/pack
typedoc . --mode modules --readme none --out $PULUMI_AWS_DOCS
popd

# pulumi-fabric
echo -e "\033[0;95mrunning typedoc on pulumi-fabric\033[0m"
pushd .
cd ../pulumi-fabric/sdk/nodejs
typedoc . --mode modules --readme none --out $PULUMI_FABRIC_DOCS
popd


# pulumi-framework
echo -e "\033[0;95mrunning typedoc on pulumi-framework\033[0m"
pushd .
cd ../pulumi-framework/api
typedoc . --mode modules --readme none --out $PULUMI_FRAMEWORK_DOCS
popd

echo "Finished running typedoc. Copying into /libraries."
mkdir -p ./libraries/

# Purge existing
rm -rf ./libraries/pulumi-aws/
rm -rf ./libraries/pulumi-fabric/
rm -rf ./libraries/pulumi-framework/

mkdir ./libraries/pulumi-aws/
mkdir ./libraries/pulumi-fabric/
mkdir ./libraries/pulumi-framework/

# Copy updated
cp -R $PULUMI_AWS_DOCS/       ./libraries/pulumi-aws/
cp -R $PULUMI_FABRIC_DOCS/    ./libraries/pulumi-fabric/
cp -R $PULUMI_FRAMEWORK_DOCS/ ./libraries/pulumi-framework/

# Cleanup
rm -rf $PULUMI_AWS_DOCS
rm -rf $PULUMI_FABRIC_DOCS
rm -rf $PULUMI_FRAMEWORK_DOCS

echo "Done"