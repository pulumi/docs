#!/bin/bash

set -o errexit -o pipefail

# In most cases, we'll get the SHA from GitHub Actions, but in case we don't,
# just fall back to Git.
export GIT_SHA=${GITHUB_SHA:=$(git rev-list HEAD | head -1)}

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process.
export CSS_BUNDLE="public/css/styles.${GIT_SHA}.css"
export JS_BUNDLE="public/js/bundle.min.${GIT_SHA}.js"

# Run Hugo, TypeScript, and the Sass things, recompiling on changes.
npx concurrently \
    "hugo server --buildDrafts --buildFuture --renderToDisk" \
    "npx tsc --watch --outFile ${JS_BUNDLE}" \
    "npx node-sass assets/sass/styles.scss --watch | npx postcss-cli --config assets/config -o ${CSS_BUNDLE}"
