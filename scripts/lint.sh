#!/bin/bash

set -o errexit -o pipefail

node ./scripts/lint/lint-markdown.js
./scripts/prettier.sh --check . --cache
