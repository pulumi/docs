#!/bin/bash

set -o nounset -o errexit -o pipefail

# This script provides a shortcut way to regenerate API docs for all
# Pulumi-managed components in the registry.
# WARNING: The list of components within might be outdated.
# The proper way to address this is to implement https://github.com/pulumi/registry/issues/105.

ensure_cloned() {
    local pkg=$1
    # Go one-level outside the docs repo.
    cd ../
    if [ ! -d "pulumi-${pkg}" ] ; then
        echo "${pkg} doesn't exist. Cloning..."
        git clone "https://github.com/pulumi/pulumi-${pkg}"
    fi
    # Go back to the docs repo.
    cd docs
}

component="aws-apigateway"
ensure_cloned "${component}"
./scripts/gen_resource_docs.sh "${component}" true "" "/schema.yaml"
./scripts/gen_package_metadata.sh "${component}" "/schema.yaml" "" "Pulumi" "" "" true

component="aws-miniflux"
ensure_cloned "${component}"
./scripts/gen_resource_docs.sh "${component}" true "" "/schema.json"
./scripts/gen_package_metadata.sh "${component}" "/schema.json" "" "Christian Nunciato" "" "infrastructure" true

component="aws-quickstart-aurora-postgres"
ensure_cloned "${component}"
./scripts/gen_resource_docs.sh "${component}" true "" "/schema.yaml"
./scripts/gen_package_metadata.sh "${component}" "/schema.yaml" "" "Pulumi" "AWS QuickStart Aurora Postgres" "" true

component="aws-quickstart-redshift"
ensure_cloned "${component}"
./scripts/gen_resource_docs.sh "${component}" true "" "/schema.yaml"
./scripts/gen_package_metadata.sh "${component}" "/schema.yaml" "" "Pulumi" "" "" true

component="aws-quickstart-vpc"
ensure_cloned "${component}"
./scripts/gen_resource_docs.sh "${component}" true "" "/schema.yaml"
./scripts/gen_package_metadata.sh "${component}" "/schema.yaml" "" "Pulumi" "" "" true

component="aws-s3-replicated-bucket"
ensure_cloned "${component}"
./scripts/gen_resource_docs.sh "${component}" true "" "/schema.json"
./scripts/gen_package_metadata.sh "${component}" "/schema.json" "" "Lee Zen" "" "" true

component="azure-quickstart-acr-geo-replication"
ensure_cloned "${component}"
./scripts/gen_resource_docs.sh "${component}" true "" "/schema.json"
./scripts/gen_package_metadata.sh "${component}" "/schema.json" "" "Ian Wahbe" "Azure QuickStart ACR Geo Replication" "" true

# The schema.json for this component is in the default location of /provider/cmd/resource-{pkg}
# so there is no need to specify the path for the schema.
component="gcp-global-cloudrun"
ensure_cloned "${component}"
./scripts/gen_resource_docs.sh "${component}"
./scripts/gen_package_metadata.sh "${component}" "" "" "Paul Stack" "GCP Global CloudRun" "" true

component="run-my-darn-container"
ensure_cloned "${component}"
./scripts/gen_resource_docs.sh "${component}" true "" "/schema.json"
./scripts/gen_package_metadata.sh "${component}" "/schema.json" "" "Lee Briggs" "" "infrastructure" true
