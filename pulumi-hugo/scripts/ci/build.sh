#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci/common.sh

# URL to the Pulumi conversion service.
export PULUMI_CONVERT_URL="${PULUMI_CONVERT_URL:-$(pulumi stack output --stack pulumi/tf2pulumi-service/production url)}"

printf "Running Hugo...\n\n"
export REPO_THEME_PATH="themes/default/"
export HUGO_BASEURL="http://$(origin_bucket_prefix)-$(build_identifier).s3-website.$(aws_region).amazonaws.com"
hugo --minify --templateMetrics --buildDrafts --buildFuture -e "preview" | grep -v -e 'WARN .* REF_NOT_FOUND'

printf "Done!\n\n"
