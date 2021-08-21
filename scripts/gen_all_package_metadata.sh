#!/bin/bash

# A script to generate the schema-based resource docs for all of the providers for which we can generate
# a Pulumi schema.

# Pass any value to the script as the first to indicate that you
# also this script to commit each provider's docs changes automatically.
GIT_COMMIT=${1:-}

source ./scripts/packages.sh

branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" = "master" ]; then
    echo "Cannot generate docs while in the master branch. Please create a new branch and then try again."
    exit 1
fi

for PKG in "${PKGS[@]}" ; do \
    ./scripts/gen_package_metadata.sh "${PKG}" true
done
