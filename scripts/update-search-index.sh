#!/bin/bash

curl "https://gist.githubusercontent.com/aaronkao/b79fb2d89aeeff928485bec93f0212c5/raw/b10bd372e08427a1e74d32153dbc06fc150f95c4/youtube-search-index.json" \
    -o "./public/search-youtube.json"

# Run the script that updates the Algolia search index. The value passed into this script denotes
# the name of the index to be updated (e.g., 'preview' or 'production').
node ./scripts/search/main.js "$1"
