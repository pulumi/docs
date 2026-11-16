#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

printf "Compiling theme JavaScript and CSS...\n\n"
export ASSET_BUNDLE_ID="$(build_identifier)"
export CSS_BUNDLE_ID="${ASSET_BUNDLE_ID}"

# Paths to the CSS and JS bundles we'll generate below. Note that environment variables
# are read by some templates during the Hugo build process.
export CSS_BUNDLE="static/css/styles.${ASSET_BUNDLE_ID}.css"
export JS_BUNDLE="static/js/bundle.min.${ASSET_BUNDLE_ID}.js"

# Relative paths to those same files, read by Hugo templates.
export REL_CSS_BUNDLE="/css/styles.${ASSET_BUNDLE_ID}.css"
export REL_JS_BUNDLE="/js/bundle.min.${ASSET_BUNDLE_ID}.js"

printf "Copying prebuilt docs...\n\n"
make copy_static_prebuilt

# Generate OpenGraph meta images. Ephemeral: written into the gitignored
# assets/images/generated/ (cached in CI via actions/cache), not committed.
# Must run before Hugo so templates can resolve the cards.
printf "Generating meta images...\n\n"
node scripts/generate-meta-images.mjs

printf "Running Hugo...\n\n"
# Hugo previously ran under GOGC=3, which collects once the heap grows 3% over
# live heap. That capped memory but cost 1.7-3x in wall time, since every
# allocation-heavy operation (image processing above all) drags a full GC behind
# it. GOMEMLIMIT expresses the actual intent -- "do not exhaust the runner" --
# as a soft ceiling, letting Go collect at its normal rate until the build
# approaches the limit.
#
# CI only: this script is the local build path too (`make build`,
# scripts/laptop-deploy.sh), and 12GiB is sized for the CI runner's 16GB shared
# with the Node and Pulumi steps -- on a 16GB laptop it would be no ceiling at
# all. An explicit GOMEMLIMIT always wins, so a memory-constrained machine can
# set its own.
if [ -n "${CI:-}" ]; then
    export GOMEMLIMIT="${GOMEMLIMIT:-12GiB}"
fi

# --gc prunes cache entries the build no longer references, which is what bounds
# the growth of the cached resources/ tree (nothing else reclaims superseded
# entries). The guard below is on the non-preview branches, so this covers every
# non-preview build under CI: the two deploy workflows, plus any CI job that runs
# `make build` (pulumi-cli-docs.yml does). That is fine because all of them build
# the full site and so reference the same set of entries. PR preview builds are
# the ones deliberately excluded -- they share the same cache namespace, and a
# build pruning against a narrower view could drop entries the others still need.
hugo_gc=()
if [ -n "${CI:-}" ]; then
    hugo_gc=(--gc)
fi

if [ "${1:-}" == "preview" ]; then
    export HUGO_BASEURL="http://$(origin_bucket_prefix)-$(build_identifier).s3-website.$(aws_region).amazonaws.com"
    hugo --minify --buildFuture --templateMetrics -e "preview"
else
    if [ "$DEPLOYMENT_ENVIRONMENT" == "testing" ]; then
        export HUGO_BASEURL="https://www.pulumi-test.io"
        hugo "${hugo_gc[@]}" --minify --buildFuture --templateMetrics -e "preview"
    else
        hugo "${hugo_gc[@]}" --minify --templateMetrics -e "production"
    fi
fi

# Add the version selector to the live SDK reference pages (build-time, no commit churn).
printf "Injecting live SDK version selectors...\n\n"
./scripts/versioned-docs/inject-live-sdk-selectors.sh public || true

# Generate docs JSON.
node scripts/content/generate-docs-content.js

# Purge unused CSS.
yarn run minify-css

# Derive the shared, stable archive theme bundle from the just-built (and purged) docs CSS.
# Versioned CLI archives reference this single contract URL (/css/versioned-docs-archive.css)
# instead of vendoring a frozen per-version copy of the fingerprinted site CSS, so the entire
# CLI back-catalog re-themes whenever the site does. snapshot-cli-docs.sh rewrites archive
# CSS references to this path; the name is un-fingerprinted on purpose (a permanent contract).
printf "Deriving versioned-docs archive theme bundle...\n\n"
if [ -f "public/css/bundle.${CSS_BUNDLE_ID}.css" ]; then
    cp "public/css/bundle.${CSS_BUNDLE_ID}.css" "public/css/versioned-docs-archive.css"
else
    echo "WARNING: docs CSS bundle public/css/bundle.${CSS_BUNDLE_ID}.css not found; archive theme bundle not refreshed" >&2
fi

# Inline critical CSS for the homepage.
node scripts/inline-critical-css.js

printf "Done!\n\n"
