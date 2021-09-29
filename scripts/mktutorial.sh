#!/bin/bash
set -e
TUTORIAL_OUT=$(mktemp -d)
pushd ./tools/mktutorial
go run *.go https://github.com/pulumi/examples $TUTORIAL_OUT
popd
for cloud in "aws" "azure" "gcp" "kubernetes"; do
    mkdir -p ./content/registry/packages/$cloud
    mkdir -p ./content/registry/packages/$cloud/how-to-guides
    cp $TUTORIAL_OUT/tutorials/$cloud/* ./content/registry/packages/$cloud/how-to-guides/
done
rm -rf $TUTORIAL_OUT
