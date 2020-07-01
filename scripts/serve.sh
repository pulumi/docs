#!/bin/bash

set -o errexit -o pipefail

# We use the Git SHA to name our CSS and JS bundles uniquely.
export GIT_SHA="$(git rev-list HEAD | head -1)"

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process, and we write to the static
# folder rather than public (which we do for production builds) in order to be able to
# use LiveReload in development.
export CSS_BUNDLE="static/css/styles.${GIT_SHA}.css"
export JS_BUNDLE="static/js/bundle.min.${GIT_SHA}.js"

watch_hugo() {
    hugo server --buildDrafts --buildFuture --renderToDisk
}

watch_js() {
    rm -f static/js/bundle.min.*.js && \
        yarn run tsc --watch --preserveWatchOutput --outFile "${JS_BUNDLE}"
}

watch_css() {
    yarn run chokidar 'assets/sass/**/*.scss' \
        -c "yarn run --silent node-sass assets/sass/styles.scss | yarn run postcss --config assets/config --output ${CSS_BUNDLE}"
}

# Build once, to make sure we have a working site to begin with.
rm -rf public && mkdir -p public public/js public/css
rm -f static/js/bundle.min.*.js && yarn run tsc --outFile "${JS_BUNDLE}"
cp ${JS_BUNDLE} public/js/
yarn run --silent node-sass assets/sass/styles.scss | yarn run --silent postcss --config assets/config --output ${CSS_BUNDLE}

# Export these functions to make them visible to Concurrently.
export -f watch_hugo
export -f watch_js
export -f watch_css




# Run Hugo, TypeScript, and the Sass things, recompiling on changes.
yarn run concurrently "watch_hugo" "watch_js" "watch_css"
