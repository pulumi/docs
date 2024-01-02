#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh
source ./scripts/programs/common.sh

# Check for Go, Hugo, Node, and Yarn.
if [[ -z "$(which go)" ]]; then
    echo "This project requires Go."
    echo "See the README for the complete list of prerequisities and "
    echo "https://golang.org/doc/install for help installing Go."
    exit 1
fi

if [[ -z "$(which hugo)" ]]; then
    echo "This project requires Hugo."
    echo "See the README for the complete list of prerequisities and "
    echo "https://gohugo.io/getting-started/quick-start for help installing Hugo."
    exit 1
fi

if [[ -z "$(which node)" ]]; then
    echo "This project requires Node.js."
    echo "See the README for the complete list of prerequisities and "
    echo "https://nodejs.org/en/download for help installing Node.js."
    exit 1
fi

if [[ -z "$(which yarn)" ]]; then
    echo "This project requires the Yarn package manager."
    echo "See the README for the complete list of prerequisities and "
    echo "https://yarnpkg.com/getting-started/install for help installing Yarn."
    exit 1
fi

echo "Installing Node.js modules..."
yarn install
yarn --cwd ./themes/default/theme install
yarn --cwd ./themes/default/theme/stencil install

# Prep Go projects so they're immediately runnable.
unsuffix_gomods
