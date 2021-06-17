#!/bin/bash
set -e
TUTORIAL_OUT=$(mktemp -d)
pushd ./tools/mktutorial
go run *.go https://github.com/pulumi/examples $TUTORIAL_OUT
popd
for cloud in "aws" "azure" "gcp" "kubernetes"; do
    mkdir -p ./content/docs/packages/providers/$cloud/examples/
    cp $TUTORIAL_OUT/tutorials/$cloud/* ./content/docs/packages/providers/$cloud/examples/
done
rm -rf $TUTORIAL_OUT
