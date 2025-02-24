#!/bin/bash

# This script downloads the search indexes for registry and docs from pulumi.com then combines
# the two indexes and pushes them to Algolia.
node ./scripts/search/update-search-index.js "$1"
