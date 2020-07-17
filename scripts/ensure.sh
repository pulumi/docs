#!/bin/bash

# Make sure the Node version matches what's in .nvmrc (and in our GitHub Actions workflows).
current_version="$(node -v)"
required_version="$(cat .nvmrc)"

if [ ! $(echo ${current_version} | grep ${required_version}) ]; then
    printf "\nIt looks like you're running Node %s, but this project uses Node %s.\n" ${current_version} ${required_version}
    printf "If you're using nvm, try running nvm use.\n\n"
    exit 1
fi

yarn install
yarn --cwd components install
yarn --cwd infrastructure install
