---
title_tag: "Upgrades | Self-Hosting Pulumi"
meta_desc: Best practices for staged rollouts, layered updates, and version pinning for self-hosted Pulumi Cloud deployments.
title: Upgrades
h1: Upgrade Pipeline
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Upgrades
    parent: administration-security-compliance-self-hosted-operations
    weight: 8
    identifier: administration-security-compliance-self-hosted-operations-upgrades
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

This page covers how to safely update your self-hosted Pulumi Cloud deployment. For version-specific changes, see the [Changelog](/docs/administration/self-hosting/changelog/).

## Staged rollouts

Deploy updates through staged environments:

1. **Staging/testing** - Deploy and run automated tests.
1. **Production** - Deploy after staging validation.

## Update process

The self-hosted installers deploy in layers, which should be updated in order:

1. **Infrastructure layer** (network, database, storage) - rarely changes
1. **Compute layer** (Kubernetes cluster, ECS cluster) - occasional updates
1. **Application layer** (API service, console, migrations) - most frequent updates

For application updates:

1. Update the `imageTag` configuration to the new version.
1. Run `pulumi up` on the application stack.
1. The installer runs database migrations before updating service containers.
1. New containers are rolled out with zero downtime.

## Version pinning

- Pin the `imageTag` to a specific version rather than using `latest`.
- Available tags are published at [Docker Hub: pulumi/service](https://hub.docker.com/r/pulumi/service/tags).
- Test new versions in a staging environment before promoting to production.
