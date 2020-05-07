#!/bin/bash
set -o nounset -o errexit -o pipefail

HTTP_SERVER_PORT=8888

check_get_pulumi_links() {
    # We only link to get.pulumi.com in /docs/get-started/install/ and /docs/get-started/install/versions
    npx blc http://localhost:$HTTP_SERVER_PORT/docs/get-started/install/versions/ --follow \
        --exclude-internal \
        --exclude "https://www*"

    npx blc http://localhost:$HTTP_SERVER_PORT/docs/get-started/install/ --follow \
        --exclude-internal \
        --exclude "https://www*"
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
