---
title_tag: ECS-Hosted Install | Self-Hosting Pulumi
meta_desc: Installer and installation instructions for deploying the self-hosted Pulumi Cloud in ECS.
title: ECS
h1: Pulumi Cloud self-hosted ECS install
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: deployment-options
        weight: 2
aliases:
  - /docs/guides/self-hosted/ecs-hosted/
---

The [ECS-Hosted Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/ecs-hosted) is used to deploy the self-hosted Pulumi Cloud in Amazon Elastic Container Service. You can choose between using a TypeScript or Golang installer.

## Prerequisites

The customer is required to provide and manage the following:

* AWS VPC with
  * At least 2 public subnets available.
  * At least 2 private subnets available.
  * At least 2 isolated subnets available.
    * An "isolated" subnet means it can only route traffic within the subnet. So there is no NAT gateway.
* Route53 hosted zone.
* ACM Certiciate that covers FQDNs of the following form, where `{subdomain}` is optional:
  * `{subdomain}.{zoneDomainName}`
  * `api.{subdomain}.{zoneDomainName}`
  * `app.{subdomain}.{zoneDomainName}`
* KMS key to be used the self-hosted Pulumi Cloud for encryption/decryption purposes.

## ECS-Hosted Deployment

The ECS-hosted installation of Pulumi deploys the following services:

* ECS - Managed ECS Cluster
* Fargate - Managed Container Service
* RDS Aurora - Managed MySQL DB for persistent state and automated replication and snapshotting.
* S3 - Object storage for checkpoints and policy packs.
* CloudWatch Logs - Centralized logging for all cluster pods.
* Route53 - Managed DNS records.
* NLB - Managed L4/application traffic and TLS termination.
* ACM - Managed Public TLS certificates.

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy the Pulumi Cloud. In this case, one uses the pulumi CLI with a self-managed backend (e.g., S3) to deploy all services listed above to stand up the self-hosted Pulumi Cloud. The installation package includes the Pulumi project code so you can deploy the service by running `pulumi up`.

To this end, you need to set up the following:

* [Download and install the Pulumi CLI](/docs/install/) on your workstation
* [Login to S3-compatible backend](/docs/concepts/state#aws-s3)

### Deployment Steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/ecs-hosted) file provided with the installer package for detailed deployment steps.

## ECS-Hosted System Management and Maintenance

### Pulumi Cloud Updates

When deploying the Pulumi Cloud, it is recommended to pin the image tag to a specific version. See the [installer's README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/ecs-hosted) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Sevice containers to use a different version, do the following:

* `pulumi login` to the self-managed (not self-hosted) backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database Maintenance

The installer configures the RDS backend database for replication and checkpointing. So no additional maintenance is needed by the customer.

### Blob Storage Maintenance

The service automatically creates backups of checkpoint (i.e. state) files. However the customer may want to enable AWS Backup to periodically backup the S3 buckets created by the installer.
The buckets will have names of the form:

* `pulumi-checkpoint-XXX`
* `pulumi-policy-XXX`
