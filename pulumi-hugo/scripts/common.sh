#!/bin/bash

BUILD_IDENTIFIER="$(git rev-parse HEAD)"
export REPO_THEME_PATH="themes/default/"

# Bundle filenames are exported for use with Hugo and theme scripts.
export CSS_BUNDLE="static/css/styles.${BUILD_IDENTIFIER}.css"
export JS_BUNDLE="static/js/bundle.min.${BUILD_IDENTIFIER}.js"
export REL_CSS_BUNDLE="/css/styles.${BUILD_IDENTIFIER}.css"
export REL_JS_BUNDLE="/js/bundle.min.${BUILD_IDENTIFIER}.js"
