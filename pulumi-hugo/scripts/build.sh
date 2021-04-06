#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

yarn --cwd themes/default run build

hugo | grep -v -e 'WARN .* REF_NOT_FOUND'
