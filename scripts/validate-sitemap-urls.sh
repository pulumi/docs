#!/bin/bash

SITEMAP=/tmp/sitemap.xml
URL_LIST=/tmp/site_urls.txt
URL_RESPONSES=/tmp/url_responses.txt
ERROR_LIST=/tmp/error_urls.txt

request_and_format_sitemap() {
    echo "Requesting pulumi.com sitemap..."
    curl https://www.pulumi.com/sitemap.xml > $SITEMAP && xmllint --format $SITEMAP > /tmp/sitemap2.xml && mv /tmp/sitemap2.xml $SITEMAP
    echo "done\n"
}

parse_urls() {
    echo "Building URL list..."
    cat $SITEMAP | grep -e loc | sed 's|<loc>\(.*\)<\/loc>$|\1|g' | sed 's/www.pulumi.com/www-reg-staging.pulumi-dev.io/g' > $URL_LIST
}

request_urls() {
    cat $URL_LIST | xargs -I {} curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" {} | tee $URL_RESPONSES
    cat $URL_RESPONSES | grep -v '200\|301' > $ERROR_LIST
    cat $URL_RESPONSES | grep -c '200' | echo "Number of 200 responses: $1"
    cat $URL_RESPONSES | grep -c '301' | echo "Number of 301 responses: $1"
    echo "THe following URLs returned errors:"
    cat $ERROR_LIST
}

cleanup() {
    rm $URL_LIST $SITEMAP $URL_RESPONSES $ERROR_LIST
}

request_and_format_sitemap
parse_urls
request_urls
cleanup
