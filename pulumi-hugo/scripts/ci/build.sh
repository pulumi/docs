#!/bin/bash

set -o errexit -o pipefail

source ./scripts/ci/common.sh

# URLs to Pulumi utility services.
export PULUMI_CONVERT_URL="${PULUMI_CONVERT_URL:-$(pulumi stack output --stack pulumi/tf2pulumi-service/production url)}"
export PULUMI_AI_WS_URL=${PULUMI_AI_WS_URL:-$(pulumi stack output --stack pulumi/pulumigpt-api/corp websocketUri)}

printf "Running Hugo...\n\n"
export REPO_THEME_PATH="themes/default/"
export HUGO_BASEURL="http://$(origin_bucket_prefix)-$(build_identifier).s3-website.$(aws_region).amazonaws.com"
hugo --minify --templateMetrics --buildDrafts --buildFuture -e "preview" | grep -v -e 'WARN .* REF_NOT_FOUND'

printf "Done!\n\n"
