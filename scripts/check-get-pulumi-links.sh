#!/bin/bash
set -o nounset -o errexit -o pipefail

HTTP_SERVER_PORT=8888

check_get_pulumi_links() {
    # We only want to check the links to https://get.pulumi.com* and since broken-link-checker only
    # allows the * wildcard and the ability to exclude (instead of include) URLs, we exclude all 
    # http URLs and all those that start with any letter except "g". Finally we exclude gi* and go*
    # for github, gist, gitlab, godoc, etc.
    ./node_modules/.bin/blc http://localhost:$HTTP_SERVER_PORT --recursive --follow \
        --exclude-internal \
        --exclude "http://*" \
        --exclude "https://a*" \
        --exclude "https://b*" \
        --exclude "https://c*" \
        --exclude "https://d*" \
        --exclude "https://e*" \
        --exclude "https://f*" \
        --exclude "https://h*" \
        --exclude "https://i*" \
        --exclude "https://j*" \
        --exclude "https://k*" \
        --exclude "https://l*" \
        --exclude "https://m*" \
        --exclude "https://n*" \
        --exclude "https://o*" \
        --exclude "https://p*" \
        --exclude "https://q*" \
        --exclude "https://r*" \
        --exclude "https://s*" \
        --exclude "https://t*" \
        --exclude "https://u*" \
        --exclude "https://v*" \
        --exclude "https://w*" \
        --exclude "https://x*" \
        --exclude "https://y*" \
        --exclude "https://z*" \
        --exclude "https://gi*" \
        --exclude "https://go*"
}

retry() {
    local n=1
    local max=3
    local delay=15
    while true; do
    "$@" && break || {
        if [[ $n -lt $max ]]; then
            ((n++))
            echo "Command failed. Attempt $n/$max:"
            sleep $delay;
        else
            echo "The command has failed after $n attempts." >&2
            exit 1
        fi
    }
    done
}

# Start an HTTP server listening at the root of the built website.
yarn run http-server public --port $HTTP_SERVER_PORT &>/dev/null &
HTTP_SERVER_PID=$!

# Run the link checker once the HTTP server is listening.
while ! nc -z localhost $HTTP_SERVER_PORT; do sleep 0.1; done
# Re-run the link checker up to three times, to handle the occasional transient failure.
retry check_get_pulumi_links

# Kill the server process.
kill $HTTP_SERVER_PID
