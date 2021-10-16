#!/bin/bash

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

ensure_cloned "aws-apigateway"
./scripts/gen_resource_docs.sh "aws-apigateway" true "" "/schema.yaml"
./scripts/gen_package_metadata.sh "aws-apigateway" "/schema.yaml" "" "Pulumi" "" "" true

ensure_cloned "aws-miniflux"
./scripts/gen_resource_docs.sh "aws-miniflux" true "" "/schema.json"
./scripts/gen_package_metadata.sh "aws-miniflux" "/schema.json" "" "Christian Nunciato" "" "infrastructure" true

ensure_cloned "aws-quickstart-aurora-postgres"
./scripts/gen_resource_docs.sh "aws-quickstart-aurora-postgres" true "" "/schema.yaml"
./scripts/gen_package_metadata.sh "aws-quickstart-aurora-postgres" "/schema.yaml" "" "Pulumi" "" "" true

ensure_cloned "aws-quickstart-redshift"
./scripts/gen_resource_docs.sh "aws-quickstart-redshift" true "" "/schema.yaml"
./scripts/gen_package_metadata.sh "aws-quickstart-redshift" "/schema.yaml" "" "Pulumi" "" "" true

ensure_cloned "aws-quickstart-vpc"
./scripts/gen_resource_docs.sh "aws-quickstart-vpc" true "" "/schema.yaml"
./scripts/gen_package_metadata.sh "aws-quickstart-vpc" "/schema.yaml" "" "Pulumi" "" "" true

ensure_cloned "aws-s3-replicated-bucket"
./scripts/gen_resource_docs.sh "aws-s3-replicated-bucket" true "" "/schema.json"
./scripts/gen_package_metadata.sh "aws-s3-replicated-bucket" "/schema.json" "" "Lee Zen" "" "" true

ensure_cloned "azure-quickstart-acr-geo-replication"
./scripts/gen_resource_docs.sh "azure-quickstart-acr-geo-replication" true "" "/schema.json"
./scripts/gen_package_metadata.sh "azure-quickstart-acr-geo-replication" "/schema.json" "" "Ian Wahbe" "" "" true

#The schema.json for this component is in the default location of `provider/cmd/resource-pkg`.
ensure_cloned "gcp-global-cloudrun"
./scripts/gen_resource_docs.sh "gcp-global-cloudrun"
./scripts/gen_package_metadata.sh "gcp-global-cloudrun" "" "" "Paul Stack" "" "" true

ensure_cloned "run-my-darn-container"
./scripts/gen_resource_docs.sh "run-my-darn-container" true "" "/schema.json"
./scripts/gen_package_metadata.sh "run-my-darn-container" "/schema.json" "" "Lee Briggs" "" "infrastructure" true
