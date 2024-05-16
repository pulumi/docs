#!/bin/bash

set -o errexit -o pipefail

source ./scripts/programs/common.sh

programs_dir="static/programs"

# Delete install artifacts, but leave existing go.mod files.
git clean -fdX "${programs_dir}/*"

# Fix up go.mod files.
clean_gomods

pushd "$programs_dir"
    for dir in */; do
        project="$(basename $dir)"

        echo
        echo "***"
        echo "* $project"
        echo "***"
        echo

        pushd "$project"

            if [[ "$project" == *"-go" && -e "go.mod" ]]; then
                go get -u
                go mod tidy
            fi

        popd
    done
popd

clean_gomods
