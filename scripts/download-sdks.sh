#!/bin/bash

# Download all flavors of the build from s3 and place them in releases
# usage download-sdks.sh <version>
set -o nounset -o errexit -o pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" 

for OS in linux windows darwin; do
    if [ "${OS}" = "windows" ]; then
        EXT="zip"
    else
        EXT="tar.gz"
    fi

    aws s3 cp s3://eng.pulumi.com/releases/sdk/pulumi-$1-${OS}.x64.${EXT} "$DIR/../releases/"
done
