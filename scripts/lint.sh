#!/bin/bash

set -o errexit -o pipefail

node ./scripts/lint/lint-markdown.js
./scripts/hugo-version.sh --check > /dev/null
./scripts/prettier.sh --check . --cache
