#!/bin/bash

set -o errexit -o pipefail

# This script packages our JS source files and sourcemaps as a Sentry release.
# https://docs.sentry.io/product/releases/

source ./scripts/common.sh

build_dir="public"
source_dir="assets"

# Make a folder to contain the source files and maps we upload to Sentry.
release_dir="sentry-release"
rm -rf "${release_dir}"
mkdir -p "${release_dir}" "${release_dir}/assets"

# Copy the files into that folder.
cp -R "assets/js" "${release_dir}/assets/"
find "${source_dir}" -name "*.js" -o -name "*.ts" -exec cp {} "${release_dir}/" \;
find "${build_dir}" -name "*.js.map" -exec cp {} "${release_dir}/" \;

# Create a new Sentry release and finalize it.
export SENTRY_ORG="pulumi"
export SENTRY_PROJECT="docs"
yarn run sentry-cli releases new "$(build_identifier)"
yarn run sentry-cli releases files "$(build_identifier)" upload-sourcemaps "${release_dir}"
yarn run sentry-cli releases finalize "$(build_identifier)"
