#!/bin/bash

# Run the script that updates the Algolia search index. The value passed into this script denotes
# the name of the index to be updated (e.g., 'preview' or 'production').
node ./scripts/search/main.js "$1"
