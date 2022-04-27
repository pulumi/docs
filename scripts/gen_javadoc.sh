#!/usr/bin/env bash

set -euo pipefail
REPO=~/pulumi-java
SRC=$REPO/sdk/java/pulumi/build/docs/javadoc
DEST=./static-prebuilt/docs/reference/pkg/java

(cd "$REPO/sdk/java" && gradle javadoc)
rm -rf "$DEST"
cp -r "$SRC" "$DEST"
