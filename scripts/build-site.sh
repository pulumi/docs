#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# URLs to Pulumi utility services.
export PULUMI_CONVERT_URL="${PULUMI_CONVERT_URL:-$(pulumi stack output --stack pulumi/tf2pulumi-service/production-www url)}"
export PULUMI_AI_WS_URL=${PULUMI_AI_WS_URL:-$(pulumi stack output --stack pulumi/pulumigpt-api/corp websocketUri)}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INFRA_PATH="$SCRIPT_DIR/../infrastructure"
# Read Copilot API URL from Pulumi config, ignoring any errors.
# If the config value is not set Copilot will not be available.
export PULUMI_COPILOT_URL=${PULUMI_COPILOT_URL:-$(pulumi --cwd "$INFRA_PATH" config get copilotUrl 2>/dev/null || echo "")}
printf "Copilot URL: $PULUMI_COPILOT_URL\n"
export PULUMI_ATLAS_URL=${PULUMI_ATLAS_URL:-$(pulumi --cwd "$INFRA_PATH" config get atlasUrl 2>/dev/null || echo "")}
printf "Atlas URL: $PULUMI_ATLAS_URL\n"

printf "Compiling theme JavaScript and CSS...\n\n"
export ASSET_BUNDLE_ID="$(build_identifier)"

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process.
export CSS_BUNDLE="static/css/styles.${ASSET_BUNDLE_ID}.css"
export JS_BUNDLE="static/js/bundle.min.${ASSET_BUNDLE_ID}.js"

# Relative paths to those same files, read by Hugo templates.
export REL_CSS_BUNDLE="/css/styles.${ASSET_BUNDLE_ID}.css"
export REL_JS_BUNDLE="/js/bundle.min.${ASSET_BUNDLE_ID}.js"

printf "Copying prebuilt docs...\n\n"
make copy_static_prebuilt

printf "Running Hugo...\n\n"
if [ "$1" == "preview" ]; then
    export HUGO_BASEURL="http://$(origin_bucket_prefix)-$(build_identifier).s3-website.$(aws_region).amazonaws.com"
    GOGC=3 hugo --minify --buildFuture --templateMetrics -e "preview"
else
    if [ "$DEPLOYMENT_ENVIRONMENT" == "testing" ]; then
        export HUGO_BASEURL="https://www.pulumi-test.io"
        GOGC=3 hugo --minify --buildFuture --templateMetrics -e "preview"
    else
        GOGC=3 hugo --minify --templateMetrics -e "production"
    fi
fi

# Generate docs JSON.
node scripts/content/generate-docs-content.js

# Purge unused CSS.
yarn run minify-css

printf "Done!\n\n"
