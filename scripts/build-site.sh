#!/bin/bash

set -o errexit -o pipefail

export NODE_ENV="production"

# We use the Git SHA to name our CSS and JS bundles uniquely. In most cases, we'll get the
# SHA from GitHub Actions, but in case we don't, just fall back to Git.
export GIT_SHA=${GITHUB_SHA:=$(git rev-list HEAD | head -1)}

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process.
export CSS_BUNDLE="public/css/styles.${GIT_SHA}.css"
export JS_BUNDLE="public/js/bundle.min.${GIT_SHA}.js"

printf "Copying prebuilt docs...\n\n"
make copy_static_prebuilt

printf "Building web components...\n\n"
make build_components

printf "Running Hugo...\n\n"
if [ "$1" == "preview" ]; then
    hugo --minify --templateMetrics --buildDrafts --buildFuture -e ${GIT_SHA}
else
    hugo --minify --templateMetrics -e production
fi

printf "Compiling the JavaScripts...\n\n"
yarn run tsc --outFile ${JS_BUNDLE}

printf "Compiling Sass and running PostCSS...\n\n"
yarn run --silent node-sass assets/sass/styles.scss | yarn run postcss --config assets/config --output ${CSS_BUNDLE}

printf "Building the search index...\n\n"
make build_search_index

printf "Done!\n\n"
