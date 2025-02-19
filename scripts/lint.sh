#!/bin/bash

set -o errexit -o pipefail

yarn run lint-markdown
yarn prettier --check .
# shellcheck disable=SC2046 # Intended splitting of file names
yarn tsc --project tsconfig.scripts.json --noEmit
