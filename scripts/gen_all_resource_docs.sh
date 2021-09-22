#!/bin/bash

# A script to generate the schema-based resource docs for all of the providers for which we can generate
# a Pulumi schema.

# Pass true to the script as the first argument to indicate that you
# also this script to commit each provider's docs changes automatically.
GIT_COMMIT=${1:-}

# Pass an output dir for package metadata as the second argument to
# additionally generate the package metadata for each package. Package
# metadata will not be generated if an output dir is not passed.
PKG_METADATA_OUT_DIR=${2:-}

# Adding a new repo to this list? Ensure that the repo's `Makefile` has a target called
# `generate_schema`.
REPOS=(
    "aiven"
    "akamai"
    "alicloud"
    "auth0"
    "aws"
    "azure"
    "azure-native"
    "azuread"
    "azuredevops"
    "civo"
    "cloudamqp"
    "cloudflare"
    "cloudinit"
    "consul"
    "datadog"
    "digitalocean"
    "dnsimple"
    "docker"
    "equinix-metal"
    "eks"
    "fastly"
    "f5bigip"
    "gcp"
    "google-native"
    "github"
    "gitlab"
    "hcloud"
    "kafka"
    "kubernetes"
    "keycloak"
    "kong"
    "linode"
    "mailgun"
    "mongodbatlas"
    "mysql"
    "newrelic"
    "ns1"
    "okta"
    "openstack"
    "opsgenie"
    "packet"
    "pagerduty"
    "postgresql"
    "rabbitmq"
    "rancher2"
    "random"
    "signalfx"
    "spotinst"
    "splunk"
    "vsphere"
    "wavefront"
    "tls"
    "vault"
    "venafi"
    "yandex"
)

branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" = "master" ]; then
    echo "Cannot generate docs while in the master branch. Please create a new branch and then try again."
    exit 1
fi

for REPO in "${REPOS[@]}" ; do \
    ./scripts/gen_resource_docs.sh "${REPO}" true

    if [ -n "${PKG_METADATA_OUT_DIR:-}" ]; then
      ./scripts/gen_package_metadata.sh "${PKG_METADATA_OUT_DIR}" "${REPO}"
    fi

    if [ "${GIT_COMMIT:-}" == "true" ]; then
      git add "./content/docs/reference/pkg/${REPO}/*"
      git add "./content/docs/reference/pkg/${REPO}/**/*"
      git commit -am "Generate resource docs for pulumi-${REPO}"
    fi
done

if [ "${GIT_COMMIT:-}" == "true" ]; then
  while true; do
      read -r -p "Push commits to origin?" yn
      case $yn in
          [Yy]* )
              echo "Pushing ${branch} to origin..."
              git push origin "${branch}"
              break
              ;;
          [Nn]* ) echo "Exiting. You said No."; exit;;
          * ) echo "Please answer yes or no.";;
      esac
  done
fi
