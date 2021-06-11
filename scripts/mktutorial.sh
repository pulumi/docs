#!/bin/bash
set -e
TUTORIAL_OUT=$(mktemp -d)
pushd ./tools/mktutorial
go run *.go https://github.com/pulumi/examples $TUTORIAL_OUT
popd
for cloud in "aws" "azure" "gcp" "kubernetes"; do
    mkdir -p ./content/docs/tutorials/$cloud
    cp $TUTORIAL_OUT/tutorials/$cloud/* ./content/docs/tutorials/$cloud/
done
rm -rf $TUTORIAL_OUT
