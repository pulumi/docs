#!/bin/bash

ensure_cloned() {
    local pkg=$1
    pushd ../
    if [ ! -d "${pkg}" ] ; then
        echo "${pkg} doesn't exist. Cloning..."
        git clone "https://github.com/pulumi-${pkg}" "${pkg}"
    fi
    popd
}

ensure_cloned "aws-apigateway"
./scripts/gen_resource_docs.sh "aws-apigateway" "" "/schema.json"
./scripts/gen_package_metadata.sh "aws-apigateway" "/schema.json" "" "Pulumi" "" "" true

ensure_cloned "aws-miniflux"
./scripts/gen_resource_docs.sh "aws-miniflux" "" "/schema.json"
./scripts/gen_package_metadata.sh "aws-miniflux" "/schema.json" "" "Christian Nunciato" "" "infrastructure" true

ensure_cloned "aws-quickstart-aurora-postgres"
./scripts/gen_resource_docs.sh "aws-quickstart-aurora-postgres" "" "/schema.json"
./scripts/gen_package_metadata.sh "aws-quickstart-aurora-postgres" "/schema.json" "" "Pulumi" "" "" true

ensure_cloned "aws-quickstart-redshift"
./scripts/gen_resource_docs.sh "aws-quickstart-redshift" "" "/schema.json"
./scripts/gen_package_metadata.sh "aws-quickstart-redshift" "/schema.json" "" "Pulumi" "" "" true

ensure_cloned "aws-quickstart-vpc"
./scripts/gen_resource_docs.sh "aws-quickstart-vpc" "" "/schema.json"
./scripts/gen_package_metadata.sh "aws-quickstart-vpc" "/schema.json" "" "Pulumi" "" "" true

ensure_cloned "aws-s3-replicated-bucket"
./scripts/gen_resource_docs.sh "aws-s3-replicated-bucket" "" "/schema.json"
./scripts/gen_package_metadata.sh "aws-s3-replicated-bucket" "/schema.json" "" "Lee Zen" "" "" true

ensure_cloned "azure-quickstart-acr-geo-replication"
./scripts/gen_resource_docs.sh "azure-quickstart-acr-geo-replication" "" "/schema.json"
./scripts/gen_package_metadata.sh "azure-quickstart-acr-geo-replication" "/schema.json" "" "Ian Wahbe" "" "" true

ensure_cloned "gcp-global-cloudrun"
./scripts/gen_resource_docs.sh "gcp-global-cloudrun" "" "/schema.json"
./scripts/gen_package_metadata.sh "gcp-global-cloudrun" "/schema.json" "" "Paul Stack" "" "" true

ensure_cloned "run-my-darn-container"
./scripts/gen_resource_docs.sh "run-my-darn-container" "" "/schema.json"
./scripts/gen_package_metadata.sh "run-my-darn-container" "/schema.json" "" "Lee Briggs" "" "infrastructure" true
