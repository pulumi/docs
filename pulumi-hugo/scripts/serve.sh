#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# Prep Go projects so they're immediately runnable.
unsuffix_gomods

# Just run Hugo.
HUGO_BASEURL=http://localhost:1313 hugo serve --buildDrafts --buildFuture | grep -v -e 'WARN .* REF_NOT_FOUND'
