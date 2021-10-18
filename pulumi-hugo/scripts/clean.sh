#!/bin/bash

set -o errexit -o pipefail

yarn cache clean
hugo mod clean

rm -rf _vendor
rm -rf public
rm -rf node_modules

for dir in themes/* ; do
    pushd $dir
        hugo mod clean
        rm -rf resources
        rm -rf node_modules
        rm -rf static/js
        rm -rf static/css
    popd
done
