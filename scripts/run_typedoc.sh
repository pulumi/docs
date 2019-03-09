#!/bin/bash

# Runs typedoc on various Pulumi repos and copies them to
# the /libraries folder.

# NOTE: typedoc needs to be installed globally (see README.md) rather than
# in a local node_modules folder. This is because typedoc does not correctly
# support relative paths within a TypeScript file. (So, you can point it at a folder,
# but if those .ts files use a path like "..\", typedoc will fail to resolve as intended.)

set -o errexit -o pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

TOOL_TYPEDOC="$SCRIPT_DIR/../node_modules/.bin/typedoc"
TOOL_APIDOCGEN="go run ./tools/tscdocgen/*.go"

PULUMI_DOC_TMP=`mktemp -d`
PULUMI_DOC_BASE=./reference/pkg/nodejs/@pulumi

# Generates API documentation for a given package. The arguments are:
#     * $1 - the simple name of the package
#     * $2 - the package root directory (to run `make ensure` for dependency updates)
#     * $3 - the package source directory, relative to the root, optionally empty if the same
# If the PKGS envvar is set, only packages in that list (space delimited) are regenerated.
generate_docs() {
    GENPKG=""
    if [ -z "$PKGS" ]; then
        GENPKG=$1
    else
        for PKG in $PKGS; do
            if [ "$PKG" == "$1" ]; then
                GENPKG=$1
            fi
        done
    fi

    if [ ! -z "$GENPKG" ]; then
        echo -e "\033[0;95m$1\033[0m"
        echo -e "\033[0;93mGenerating typedocs\033[0m"
        pushd ../$2
        if [ -z "$NOBUILD" ]; then
            make ensure && make build && make install
        fi
        if [ ! -z "$3" ]; then
            cd $3
        fi
        $TOOL_TYPEDOC --json $PULUMI_DOC_TMP/$1.docs.json \
            --mode modules --includeDeclarations --excludeExternals --excludePrivate
        popd
        echo -e "\033[0;93mGenerating pulumi.io API docs\033[0m"
        $TOOL_APIDOCGEN $PULUMI_DOC_TMP/$1.docs.json $PULUMI_DOC_BASE/$1
    fi
}

generate_docs "pulumi" "pulumi/sdk/nodejs"
generate_docs "aws" "pulumi-aws" "sdk/nodejs"
generate_docs "awsx" "pulumi-awsx/nodejs/awsx"
generate_docs "azure" "pulumi-azure" "sdk/nodejs"
generate_docs "azure-serverless" "pulumi-azure-serverless/nodejs/azure-serverless"
generate_docs "cloud" "pulumi-cloud/api"
generate_docs "cloud-aws" "pulumi-cloud/aws"
generate_docs "cloud-azure" "pulumi-cloud/azure"
generate_docs "cloudflare" "pulumi-cloudflare" "sdk/nodejs"
generate_docs "docker" "pulumi-docker" "sdk/nodejs"
generate_docs "eks" "pulumi-eks/nodejs/eks"
generate_docs "kubernetes" "pulumi-kubernetes" "sdk/nodejs"
generate_docs "gcp" "pulumi-gcp" "sdk/nodejs"
generate_docs "openstack" "pulumi-openstack" "sdk/nodejs"
generate_docs "vsphere" "pulumi-vsphere" "sdk/nodejs"
generate_docs "f5bigip" "pulumi-f5bigip" "sdk/nodejs"
generate_docs "packet" "pulumi-packet" "sdk/nodejs"
generate_docs "random" "pulumi-random" "sdk/nodejs"

echo "Done"
