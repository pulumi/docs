#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# URL to the Pulumi conversion service.
export PULUMI_CONVERT_URL="${PULUMI_CONVERT_URL:-$(pulumi stack output --stack pulumi/tf2pulumi-service/production url)}"

printf "Compiling theme JavaScript and CSS...\n\n"
export ASSET_BUNDLE_ID="$(build_identifier)"

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process.
export CSS_BUNDLE="static/css/styles.${ASSET_BUNDLE_ID}.css"
export JS_BUNDLE="static/js/bundle.min.${ASSET_BUNDLE_ID}.js"

# Relative paths to those same files, read by Hugo templates.
export REL_CSS_BUNDLE="/css/styles.${ASSET_BUNDLE_ID}.css"
export REL_JS_BUNDLE="/js/bundle.min.${ASSET_BUNDLE_ID}.js"

export REPO_THEME_PATH="themes/default/"
export LOCAL_THEME_PATH="_vendor/$(hugo_theme_path)/"

# Themes are expected to manage their own dependencies and to expose `ensure`, `test`, and `build` scripts.
pushd $LOCAL_THEME_PATH
    yarn run ensure
    yarn run test
    yarn run build
popd

printf "Running Hugo...\n\n"
if [ "$1" == "preview" ]; then
    export HUGO_BASEURL="http://$(origin_bucket_prefix)-$(build_identifier).s3-website.$(aws_region).amazonaws.com"
    GOGC=5 hugo --minify --templateMetrics --buildDrafts --buildFuture -e "preview"
else
    GOGC=5 hugo --minify --templateMetrics -e production
fi

printf "Done!\n\n"
