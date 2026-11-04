---
title_tag: ECS-Hosted Install | Self-Hosting Pulumi
meta_desc: Installer and installation instructions for deploying the self-hosted Pulumi Cloud in ECS.
title: ECS
h1: Pulumi Cloud self-hosted ECS install
menu:
  administration:
        name: ECS
        parent: administration-security-compliance-self-hosted-deployment-options
        weight: 2
        identifier: administration-security-compliance-self-hosted-deployment-options-ecs
aliases:
  - /docs/guides/self-hosted/ecs-hosted/
  - /docs/pulumi-cloud/self-hosted/deployment-options/ecs-hosted/
  - /docs/pulumi-cloud/admin/self-hosted/deployment-options/ecs-hosted/
pulumi_cloud_feature: self-hosting
---

The [ECS-Hosted Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/ecs-hosted) is used to deploy the self-hosted Pulumi Cloud in Amazon Elastic Container Service. You can choose between using a TypeScript or Golang installer.

## Prerequisites

You must provide and manage the following:

* AWS VPC with
  * At least 2 public subnets available.
  * At least 2 private subnets available.
  * At least 2 isolated subnets available.
    * An "isolated" subnet means it can only route traffic within the subnet. So there is no NAT gateway.
* Route53 hosted zone.
* ACM certificate that covers FQDNs of the following form, where `{subdomain}` is optional:
  * `{subdomain}.{zoneDomainName}`
  * `api.{subdomain}.{zoneDomainName}`
  * `app.{subdomain}.{zoneDomainName}`
* KMS key that the self-hosted Pulumi Cloud uses for encryption and decryption.

## ECS-hosted deployment

The ECS-hosted installation of Pulumi deploys the following services:

* ECS - Managed ECS Cluster
* Fargate - Managed Container Service
* RDS Aurora - Managed MySQL DB for persistent state and automated replication and snapshotting.
* S3 - Object storage for checkpoints and policy packs.
* CloudWatch Logs - Optional centralized logging for the service containers. Logging is off by default.
* Route53 - Managed DNS records.
* ALB - Managed application traffic and TLS termination, using the ACM certificate you provide.

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy Pulumi Cloud. You use the Pulumi CLI with a DIY backend (for example, S3) to deploy all the services listed above and stand up the self-hosted Pulumi Cloud. The installation package includes the Pulumi project code, so you can deploy the service by running `pulumi up`.

Before you deploy, set up the following:

* [Download and install the Pulumi CLI](/docs/install/) on your workstation
* [Log in to an S3-compatible backend](/docs/iac/operations/stack-management/using-a-diy-backend/#aws-s3)

### Deployment steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/ecs-hosted) file provided with the installer package for detailed deployment steps.

## ECS-hosted system management and maintenance

### Pulumi Cloud updates

When deploying Pulumi Cloud, it is recommended to pin the image tag to a specific version. See the [installer's README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/ecs-hosted) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Cloud containers to use a different version, do the following:

* `pulumi login` to the self-managed (not self-hosted) backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database maintenance

The installer configures the RDS backend database for replication and checkpointing. So no additional maintenance is needed by the customer.

### Blob storage maintenance

The service automatically creates backups of checkpoint (state) files. However, you may want to enable AWS Backup to periodically back up the S3 buckets that the installer creates.
The buckets have names of the form:

* `pulumi-checkpoints-XXX`
* `pulumi-policypacks-XXX`
* `pulumi-service-metadata-XXX`
