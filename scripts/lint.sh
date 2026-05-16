#!/bin/bash

set -o errexit -o pipefail

source ./scripts/mise-env.sh

node ./scripts/lint/lint-markdown.js
yarn prettier --check . --cache
