#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci/common.sh

# Check out the docs repo @ master.
rm -rf temp-docs && mkdir temp-docs

# Use this pulumi-hugo branch's themes/default content to run a full build of the website.
pushd temp-docs
    git clone https://github.com/pulumi/docs.git .
    HUGO_MODULE_REPLACEMENTS="github.com/pulumi/pulumi-hugo/themes/default -> $(pwd)/../themes/default" \
        make ensure ensure_tools build
popd

rm -rf temp-docs
