#!/bin/bash

request_and_format_sitemap() {
    curl https://www.pulumi.com/sitemap.xml > sitemap.xml && xmllint --format sitemap.xml > temp_sitemap.xml && mv temp_sitemap.xml sitemap.xml
}

parse_urls() {
    cat sitemap.xml | grep -e loc | sed 's|<loc>\(.*\)<\/loc>$|\1|g' | sed 's/www.pulumi.com/www-reg-staging.pulumi-dev.io/g' > site_urls.txt
}

request_urls() {
    cat site_urls.txt | xargs -I {} curl -L -s -o /dev/null -w "%{http_code} %{url_effective}\n" {} | grep -v '200\|301'
}

request_and_format_sitemap
parse_urls
request_urls
