#!/bin/bash

set -o errexit -o pipefail

# This script tests the IndexNow API with a single URL submission
# to verify that the API is working correctly

echo "Testing IndexNow API with a single URL submission..."
node ./scripts/search/test-indexnow-api.js