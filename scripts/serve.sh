#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process, and we write to the static
# folder rather than public (which we do for production builds) in order to be able to
# use LiveReload in development.
export CSS_BUNDLE="static/css/styles.$(build_identifier).css"
export JS_BUNDLE="static/js/bundle.min.$(build_identifier).js"

# Relative paths to those same files, read by Hugo templates.
export REL_CSS_BUNDLE="/css/styles.$(build_identifier).css"
export REL_JS_BUNDLE="/js/bundle.min.$(build_identifier).js"

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

# Export these functions to make them visible to Concurrently.
export -f watch_hugo
export -f watch_js
export -f watch_css

# Run the CSS and JS builds once, to make sure we start with a working site.
rm -f static/css/styles.*.css
rm -f static/js/bundle.min.*.js
mkdir -p public public/js public/css
yarn run tsc --outFile "${JS_BUNDLE}"
cp ${JS_BUNDLE} public/js/
yarn run --silent node-sass assets/sass/styles.scss | yarn run --silent postcss --config assets/config --output ${CSS_BUNDLE}

printf "Copying prebuilt docs...\n\n"
make copy_static_prebuilt

printf "Building web components...\n\n"
make build_components

printf "Watching Hugo, assets/js, and assets/sass for changes...\n\n"
yarn run concurrently "watch_hugo" "watch_js" "watch_css"
