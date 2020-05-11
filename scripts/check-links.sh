#!/bin/bash
set -o nounset -o errexit -o pipefail

BUILD_TYPE=${1-schedule}
HTTP_SERVER_PORT=8888

check_links() {
    # We exclude some links:
	#     - Our generated API docs have lots of broken links
	#     - Our available versions page includes links to private repos
	#     - GitHub Edit Links may be broken, because the page might not yet exist!
	#     - Our LinkedIn page, for some reason, returns an HTTP error (despite being valid)
	#     - Our Visual Studio Marketplace link for the Azure Pipelines task extension,
	#       although valid and publicly available, is reported as a broken link.
	#     - A number of synthetic illustrative links come from our examples/tutorials.
    ./node_modules/.bin/blc http://localhost:$HTTP_SERVER_PORT --recursive --follow \
        --exclude "/docs/reference/pkg" \
        --exclude "/docs/get-started/install/versions" \
        --exclude "https://api.pulumi.com/" \
        --exclude "https://github.com/pulls?" \
        --exclude "https://github.com/pulumi/docs/edit/master" \
        --exclude "https://github.com/pulumi/docs/issues/new" \
        --exclude "https://www.linkedin.com/" \
        --exclude "https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task" \
        --exclude "https://blog.mapbox.com/" \
        --exclude "https://www.youtube.com/" \
        --exclude "https://apps.twitter.com/" \
        --exclude "https://www.googleapis.com/" \
        --exclude "https://us-central1-/" \
        --exclude "https://www.mysql.com/" \
        --exclude "https://ksonnet.io/" \
        --exclude "https://www.latlong.net/" \
        --exclude "https://media.amazonwebservices.com/architecturecenter/AWS_ac_ra_web_01.pdf" \
        --exclude "https://www.packet.com/"
}

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
if [ $BUILD_TYPE = "pull_request" ]
then
    echo "Checking only get.pulumi.com links"
    retry check_get_pulumi_links
else 
    echo "Checking all links"
    retry check_links
fi

# Kill the server process.
kill $HTTP_SERVER_PID
