#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# URLs to Pulumi utility services.
export PULUMI_CONVERT_URL="${PULUMI_CONVERT_URL:-$(pulumi stack output --stack pulumi/tf2pulumi-service/production url)}"
export PULUMI_AI_WS_URL=${PULUMI_AI_WS_URL:-$(pulumi stack output --stack pulumi/pulumigpt-api/corp websocketUri)}

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

printf "Copying prebuilt docs...\n\n"
make copy_static_prebuilt

REGISTRY_COMMIT="$(go mod graph | grep pulumi/registry/themes/default | sed 's/.*-//')"

# In the testing environment this is done by the pulumi/registry repo. Once this moves to prod,
# we can remove this altogether, since API docs generation will no longer be done here.
if [[ "$DEPLOYMENT_ENVIRONMENT" != "testing" ]]; then
    printf "Generating API docs from registry commit %s...\n\n" "${REGISTRY_COMMIT}"
    pushd tools/resourcedocsgen
    go build -o "${GOPATH}/bin/resourcedocsgen" .
    resourcedocsgen docs registry --commitSha "${REGISTRY_COMMIT}" --logtostderr
    popd
fi

printf "Running Hugo...\n\n"
if [ "$1" == "preview" ]; then
    export HUGO_BASEURL="http://$(origin_bucket_prefix)-$(build_identifier).s3-website.$(aws_region).amazonaws.com"
    GOGC=3 hugo --minify --buildFuture --templateMetrics -e "preview"
else
    GOGC=3 hugo --minify --buildFuture --templateMetrics -e production
fi

# Purge unused CSS.
yarn run minify-css

printf "Done!\n\n"
