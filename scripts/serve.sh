#!/bin/bash

set -o errexit -o pipefail

# In most cases, we'll get the SHA from GitHub Actions, but in case we don't,
# just fall back to Git.
export GIT_SHA="${GITHUB_SHA:=$(git rev-list HEAD | head -1)}"

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process, and we write to the static
# folder rather than public, as we do for production builds, in order to be able to keep
# using livereload.
export CSS_BUNDLE="static/css/styles.${GIT_SHA}.css"
export JS_BUNDLE="static/js/bundle.min.${GIT_SHA}.js"

watch_hugo() {
    hugo server --buildDrafts --buildFuture --renderToDisk
}

watch_js() {
    yarn run --silent tsc --watch --preserveWatchOutput --outFile "${JS_BUNDLE}"
}

watch_css() {
    yarn run --silent chokidar 'assets/sass/**/*.scss' \
        -c "yarn run --silent node-sass assets/sass/styles.scss | yarn run --silent postcss --config assets/config --output ${CSS_BUNDLE}"
}

# Build once, because node-sass doesn't do that automatically.
yarn run --silent node-sass assets/sass/styles.scss | yarn run --silent postcss --config assets/config --output ${CSS_BUNDLE}

export -f watch_hugo
export -f watch_js
export -f watch_css

# Run Hugo, TypeScript, and the Sass things, recompiling on changes.
yarn run --silent concurrently "watch_hugo" "watch_js" "watch_css"
