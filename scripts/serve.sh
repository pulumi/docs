#!/usr/bin/env bash

set -o errexit -o pipefail

source ./scripts/common.sh

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process, and we write to the static
# folder rather than public (which we do for production builds) in order to be able to
# use LiveReload in development.
export ASSET_BUNDLE_ID="$(build_identifier)"
export CSS_BUNDLE="static/css/styles.${ASSET_BUNDLE_ID}.css"
export JS_BUNDLE="static/js/bundle.min.${ASSET_BUNDLE_ID}.js"

# Relative paths to those same files, read by Hugo templates.
export REL_CSS_BUNDLE="/css/styles.${ASSET_BUNDLE_ID}.css"
export REL_JS_BUNDLE="/js/bundle.min.${ASSET_BUNDLE_ID}.js"

# URL to the Pulumi conversion service.
export PULUMI_CONVERT_URL="${PULUMI_CONVERT_URL:-$(pulumi stack output --stack pulumi/tf2pulumi-service/production-www url)}"

# Default to building future content unless explicitly disabled
BUILD_FUTURE_FLAG="--buildFuture"
if [ "${BUILD_FUTURE:-true}" = "false" ]; then
    BUILD_FUTURE_FLAG=""
fi

HUGO_BASEURL=http://localhost:1313 hugo server --renderToMemory --disableFastRender --buildDrafts ${BUILD_FUTURE_FLAG}
