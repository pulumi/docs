#!/bin/bash
set -e
TUTORIAL_OUT=$(mktemp -d)
pushd ./tools/mktutorial
go run *.go https://github.com/pulumi/examples $TUTORIAL_OUT
popd
cp $TUTORIAL_OUT/shortcodes/* ./layouts/shortcodes/
for cloud in "aws" "azure" "gcp" "kubernetes"; do
    cp $TUTORIAL_OUT/tutorials/$cloud/* ./content/docs/tutorials/$cloud/
done
rm -rf $TUTORIAL_OUT
