#!/bin/bash

# Runs typedoc on various Pulumi repos and copies them to 
# the /libraries folder.

# NOTE: typedoc needs to be installed globally (see README.md) rather than
# in a local node_modules folder. This is because typedoc does not correctly
# support relative paths within a TypeScript file. (So, you can point it at a folder,
# but if those .ts files use a path like "..\", typedoc will fail to resolve as intended.)

set -o nounset -o errexit -o pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TYPEDOC="$SCRIPT_DIR/../node_modules/.bin/typedoc"

PULUMI_DOCS=`mktemp -d`

# pulumi
echo -e "\033[0;95mrunning typedoc on pulumi\033[0m"
pushd .
cd ../pulumi/sdk/nodejs
$TYPEDOC --json $PULUMI_DOCS/pulumi.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-aws
echo -e "\033[0;95mrunning typedoc on pulumi-aws\033[0m"
pushd .
cd ../pulumi-aws/sdk/nodejs
$TYPEDOC --json $PULUMI_DOCS/pulumi-aws.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-cloud
echo -e "\033[0;95mrunning typedoc on pulumi-cloud\033[0m"
pushd .
cd ../pulumi-cloud/api
$TYPEDOC --json $PULUMI_DOCS/pulumi-cloud.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-cloud-aws
echo -e "\033[0;95mrunning typedoc on pulumi-cloud-aws\033[0m"
pushd .
cd ../pulumi-cloud/aws
$TYPEDOC --json $PULUMI_DOCS/pulumi-cloud-aws.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-cloud-azure
echo -e "\033[0;95mrunning typedoc on pulumi-cloud-azure\033[0m"
pushd .
cd ../pulumi-cloud/azure
$TYPEDOC --json $PULUMI_DOCS/pulumi-cloud-azure.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-azure
echo -e "\033[0;95mrunning typedoc on pulumi-azure\033[0m"
pushd .
cd ../pulumi-azure/sdk/nodejs
$TYPEDOC --json $PULUMI_DOCS/pulumi-azure.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-kubernetes
echo -e "\033[0;95mrunning typedoc on pulumi-kubernetes\033[0m"
pushd .
cd ../pulumi-kubernetes/sdk/nodejs
$TYPEDOC --json $PULUMI_DOCS/pulumi-kubernetes.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-gcp
echo -e "\033[0;95mrunning typedoc on pulumi-gcp\033[0m"
pushd .
cd ../pulumi-gcp/sdk/nodejs
$TYPEDOC --json $PULUMI_DOCS/pulumi-gcp.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-aws-infra
echo -e "\033[0;95mrunning typedoc on pulumi-aws-infra\033[0m"
pushd .
cd ../pulumi-aws-infra/nodejs/aws-infra
$TYPEDOC --json $PULUMI_DOCS/pulumi-aws-infra.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-azure-serverless
echo -e "\033[0;95mrunning typedoc on pulumi-azure-serverless\033[0m"
pushd .
cd ../pulumi-azure-serverless/nodejs/azure-serverless
$TYPEDOC --json $PULUMI_DOCS/pulumi-azure-serverless.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-docker
echo -e "\033[0;95mrunning typedoc on pulumi-docker\033[0m"
pushd .
cd ../pulumi-docker/docker
$TYPEDOC --json $PULUMI_DOCS/pulumi-docker.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-openstack
echo -e "\033[0;95mrunning typedoc on pulumi-openstack\033[0m"
pushd .
cd ../pulumi-openstack/sdk/nodejs
$TYPEDOC --json $PULUMI_DOCS/pulumi-openstack.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# pulumi-vsphere
echo -e "\033[0;95mrunning typedoc on pulumi-vsphere\033[0m"
pushd .
cd ../pulumi-vsphere/sdk/nodejs
$TYPEDOC --json $PULUMI_DOCS/pulumi-vsphere.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd

# eks
echo -e "\033[0;95mrunning typedoc on eks\033[0m"
pushd .
cd ../eks/nodejs/eks
$TYPEDOC --json $PULUMI_DOCS/eks.docs.json --mode modules --includeDeclarations --excludeExternals --excludePrivate
popd


echo "Finished running typedoc. Generating update docs..."
TSC_DOCGEN="go run ./tools/tscdocgen/*.go"
PKG_DOCS=./reference/pkg/nodejs/@pulumi

$TSC_DOCGEN $PULUMI_DOCS/pulumi.docs.json $PKG_DOCS/pulumi
$TSC_DOCGEN $PULUMI_DOCS/pulumi-aws.docs.json $PKG_DOCS/aws
$TSC_DOCGEN $PULUMI_DOCS/pulumi-cloud.docs.json $PKG_DOCS/cloud
$TSC_DOCGEN $PULUMI_DOCS/pulumi-cloud-aws.docs.json $PKG_DOCS/cloud-aws
$TSC_DOCGEN $PULUMI_DOCS/pulumi-cloud-azure.docs.json $PKG_DOCS/cloud-azure
$TSC_DOCGEN $PULUMI_DOCS/pulumi-azure.docs.json $PKG_DOCS/azure
$TSC_DOCGEN $PULUMI_DOCS/pulumi-kubernetes.docs.json $PKG_DOCS/kubernetes
$TSC_DOCGEN $PULUMI_DOCS/pulumi-gcp.docs.json $PKG_DOCS/gcp
$TSC_DOCGEN $PULUMI_DOCS/pulumi-aws-infra.docs.json $PKG_DOCS/aws-infra
$TSC_DOCGEN $PULUMI_DOCS/pulumi-azure-serverless.docs.json $PKG_DOCS/azure-serverless
$TSC_DOCGEN $PULUMI_DOCS/pulumi-docker.docs.json $PKG_DOCS/docker
$TSC_DOCGEN $PULUMI_DOCS/pulumi-openstack.docs.json $PKG_DOCS/openstack
$TSC_DOCGEN $PULUMI_DOCS/pulumi-vsphere.docs.json $PKG_DOCS/vsphere
$TSC_DOCGEN $PULUMI_DOCS/eks.docs.json $PKG_DOCS/eks

echo "Done"
