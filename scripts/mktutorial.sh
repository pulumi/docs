#!/bin/bash
TUTORIAL_OUT=$(mktemp -d)
go run ./tools/mktutorial/*.go https://github.com/pulumi/examples $TUTORIAL_OUT
cp $TUTORIAL_OUT/shortcodes/* ./layouts/shortcodes/
for cloud in "aws" "azure" "gcp" "kubernetes"; do
    cp $TUTORIAL_OUT/tutorials/$cloud/* ./content/docs/reference/tutorials/$cloud/
done
rm -rf $TUTORIAL_OUT
