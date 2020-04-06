#!/bin/bash

# A script to generate the schema-based resource docs for all of the providers for which we can generate
# a Pulumi schema.

# Adding a new repo to this list? Ensure that the repo's `Makefile` has a target called
# `generate_schema`.
REPOS=(
    # "aiven"
    "alicloud"
    "aws"
    "azure"
    "azuread"
    "cloudamqp"
    "cloudflare"
    "consul"
    "datadog"
    "digitalocean"
    "dnsimple"
    "fastly"
    "f5bigip"
    "gcp"
    # "gitlab"
    "kafka"
    "keycloak"
    "linode"
    # "mailgun"
    "mysql"
    "newrelic"
    "okta"
    "openstack"
    "packet"
    "postgresql"
    "rabbitmq"
    "rancher2"
    "signalfx"
    "spotinst"
    "vsphere"
    "tls"
    "vault"
)

branch=$(git rev-parse --abbrev-ref HEAD)
if [ $branch = "master" ]; then
    echo "Cannot generate docs while in the master branch. Please create a new branch and then try again."
    exit 1
fi

for REPO in "${REPOS[@]}" ; do \
    ./scripts/gen_resource_docs.sh $REPO

    git add .
    git commit -am "Generate resource docs for pulumi-${REPO}"
done

echo "Pushing ${branch} to origin..."
git push origin ${branch}
