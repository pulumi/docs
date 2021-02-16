#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

export NODE_ENV="production"

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process.
export ASSET_BUNDLE_ID="$(build_identifier)"
export CSS_BUNDLE="public/css/styles.${ASSET_BUNDLE_ID}.css"
export JS_BUNDLE="public/js/bundle.min.${ASSET_BUNDLE_ID}.js"

# Relative paths to those same files, read by Hugo templates.
export REL_CSS_BUNDLE="/css/styles.${ASSET_BUNDLE_ID}.css"
export REL_JS_BUNDLE="/js/bundle.min.${ASSET_BUNDLE_ID}.js"

# URL to the Pulumi conversion service.
export PULUMI_CONVERT_URL="${PULUMI_CONVERT_URL:-$(pulumi stack output --stack pulumi/tf2pulumi-service/production url)}"

printf "Building web components...\n\n"
make build_components

printf "Running Hugo...\n\n"
if [ "$1" == "preview" ]; then
    GOGC=5 hugo --minify --templateMetrics --buildDrafts --buildFuture -e "preview"
else
    GOGC=5 hugo --minify --templateMetrics -e production
fi

printf "Compiling the JavaScripts...\n\n"
yarn run tsc --outFile ${JS_BUNDLE}

printf "Compiling Sass and running PostCSS...\n\n"
yarn run --silent node-sass assets/sass/styles.scss | yarn run postcss --config assets/config --output ${CSS_BUNDLE}

printf "Building the search index...\n\n"
make build_search_index

printf "Done!\n\n"
