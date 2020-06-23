#!/bin/bash
set -o nounset -o errexit -o pipefail

source ./scripts/common.sh

CHECK_TYPE=${1-local}

check_links_www() {
    # We exclude some links:
	#     - Our generated API docs have lots of broken links
	#     - Our available versions page includes links to private repos
	#     - GitHub Edit Links may be broken, because the page might not yet exist!
	#     - Our LinkedIn page, for some reason, returns an HTTP error (despite being valid)
	#     - Our Visual Studio Marketplace link for the Azure Pipelines task extension,
	#       although valid and publicly available, is reported as a broken link.
	#     - A number of synthetic illustrative links come from our examples/tutorials.
    npx blc https://www.pulumi.com --recursive --follow --get \
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
        --exclude "https://www.packet.com/" \
        --exclude "https://www.random.org" \
        --exclude "https://mbrdna.com" \
        --exclude "https://media.amazonwebservices.com/architecturecenter/AWS_ac_ra_web_01.pdf" \
        --exclude "https://kubernetes-charts-incubator.storage.googleapis.com" \
        --exclude "https://kubernetes-charts.storage.googleapis.com" \
        --exclude "http://web-lb-23139b7-1806442625.us-east-1.elb.amazonaws.com" \
        --exclude "https://ruby-app-7a54c5f5e006d5cf33c2-zgms4nzdba-uc.a.run.app" \
        --exclude "https://hello-a28eea2-q1wszdxb2b-ew.a.run.app" \
        --exclude "https://ruby-420a973-q1wszdxb2b-ew.a.run.app" \
        --exclude "https://280f2167f1.execute-api.us-east-1.amazonaws.com" \
        --exclude "http://my-bucket-1234567.s3-website.us-west-2.amazonaws.com"
}

check_links_local() {
    # We only link to get.pulumi.com in /docs/get-started/install/ and /docs/get-started/install/versions
    npx blc http://localhost:$HTTP_SERVER_PORT/docs/get-started/install/versions/ --follow \
        --exclude-internal \
        --exclude "https://www*"

    npx blc http://localhost:$HTTP_SERVER_PORT/docs/get-started/install/ --follow \
        --exclude-internal \
        --exclude "https://www*"
}

if [ $CHECK_TYPE = "local" ]; then

    # Start an HTTP server listening at the root of the built website.
    HTTP_SERVER_PORT=8888
    yarn run http-server public --port $HTTP_SERVER_PORT &>/dev/null &
    HTTP_SERVER_PID=$!

    # Run the link checker once the HTTP server is listening.
    while ! nc -z localhost $HTTP_SERVER_PORT; do sleep 0.1; done

    echo "Checking only get.pulumi.com links"
    retry check_links_local 3 15

    # Kill the server process.
    kill $HTTP_SERVER_PID
fi

if [ $CHECK_TYPE = "www" ]; then

    echo "Checking all links on pulumi.com"
    retry check_links_www 3 15 || post_to_slack "ops-notifications" "Eek! :scream_cat: There are broken links on pulumi.com. See the GitHub Actions log for details. https://github.com/${GITHUB_REPOSITORY}/runs/${GITHUB_RUN_ID}"
fi
