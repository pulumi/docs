#!/bin/bash

set -o errexit -o pipefail

export NODE_ENV=production

# In most cases, we'll get the SHA from GitHub Actions, but in case we don't,
# just fall back to Git.
export GIT_SHA=${GITHUB_SHA:=$(git rev-list HEAD | head -1)}

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process.
export CSS_BUNDLE="public/css/styles.${GIT_SHA}.css"
export JS_BUNDLE="public/js/bundle.min.${GIT_SHA}.js"

# Run the Hugo build.
printf "Running Hugo...\n\n"
hugo --minify --cleanDestinationDir --templateMetrics --templateMetricsHints

printf "\nCompiling the JavaScripts...\n\n"
npx tsc --outFile ${JS_BUNDLE}

printf "Compiling the Sass...\n\n"
npx node-sass assets/sass/styles.scss --output-style compressed > ${CSS_BUNDLE}

printf "Running PostCSS...\n\n"
npx postcss-cli ${CSS_BUNDLE} --config assets/config --replace

printf "Done!\n\n"
