#!/bin/bash

set -o errexit -o pipefail

node ./scripts/lint/lint-markdown.js
node ./scripts/lint/check-concepts-links.js
./scripts/prettier.sh --check . --cache
