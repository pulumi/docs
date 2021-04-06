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
        rm -rf _vendor
        rm -rf node_modules
        rm -rf static/js
        rm -rf static/css
        rm -rf components/node_modules
        rm -rf components/dist
        rm -rf components/www
    popd
done
