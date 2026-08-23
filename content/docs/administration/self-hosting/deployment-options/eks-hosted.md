---
title_tag: EKS-Hosted Install | Self-Hosting Pulumi
meta_desc: Installer and installation instructions for deploying the self-hosted Pulumi Cloud in EKS.
title: EKS
h1: Pulumi Cloud self-hosted EKS install
menu:
  administration:
        name: EKS
        parent: administration-self-hosting-deployment-options
        weight: 3
        identifier: administration-self-hosting-deployment-options-eks
aliases:
  - /docs/guides/self-hosted/eks-hosted/
  - /docs/pulumi-cloud/self-hosted/deployment-options/eks-hosted/
  - /docs/pulumi-cloud/admin/self-hosted/deployment-options/eks-hosted/
pulumi_cloud_feature: self-hosting
---

{{< self-hosting-trial-note />}}

The [EKS-Hosted Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted) installer is used to deploy the self-hosted Pulumi Cloud in Amazon Elastic Kubernetes Service (EKS).

## Prerequisites

The customer is required to provide and manage the following:

* Route53 hosted zone.

## EKS-Hosted Deployment

The EKS-hosted installation of Pulumi deploys the following services:

* EKS - Managed Amazon Elastic Kubernetes Service Cluster
* RDS Aurora - Managed MySQL DB for persistent state and automated replication and snapshotting.
* S3 - Object storage for checkpoints and policy packs.
* CloudWatch Logs - Centralized logging for all cluster pods.
* Route53 - Managed DNS records.
* ALB - Managed L4/application traffic and TLS termination.
* ACM - Managed Public TLS certificates.

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy Pulumi Cloud. In this case, use the Pulumi CLI with a DIY backend (e.g. S3) to deploy all services listed above to stand up the self-hosted Pulumi Cloud. The installation package includes Pulumi project code so that you can deploy the service by running `pulumi up`.

To this end, you need to set up the following:

* [Download and install the Pulumi CLI](/docs/install/) on your workstation
* [Login to S3-compatible backend](/docs/iac/concepts/state-and-backends/#logging-into-and-out-of-state-backends)

### Deployment Steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted/README.md) file provided with the installer package for detailed deployment steps.

{{< self-hosted-first-admin-note />}}

## EKS-Hosted System Management and Maintenance

### Pulumi Cloud Updates

{{< self-hosting-schema-v2-note />}}

When deploying the service, it is recommended to pin the Pulumi Cloud image tag to a specific version. See the installer's [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted/README.md) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Cloud containers to use a different version, do the following:

* `pulumi login` to the DIY backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database Maintenance

The installer configures the RDS backend database for replication and checkpointing. So no additional maintenance is needed by the customer.

### Blob Storage Maintenance

The service automatically creates backups of checkpoint files. However, the customer may want to enable AWS Backup to periodically backup the S3 buckets created by the installer.
The buckets will have names of the form:

* `pulumi-checkpoint-XXX`
* `pulumi-policy-XXX`

### Supported Kubernetes versions

| Installer version | Released | Kubernetes |
| :-- | :-- | :-- |
| 4.0 | March 2026 | 1.34.0 |
| 3.1 | February 2025 | 1.31.0 |
| 3.0 | December 2024 | 1.30.3 |
| 2.1 | November 2024 | 1.30.3 |
| 1.0 | October 2024 | 1.30.3 |

### Updating the EKS cluster Kubernetes version

Set `clusterVersion` in the `05-eks-cluster` project's stack configuration to the version you want, then run `pulumi up` in that project.

{{% notes type="info" %}}
AWS upgrades the EKS control plane one minor release at a time. To move from 1.31 to 1.34, repeat the step for each intervening release, waiting for each upgrade to finish before starting the next.
{{% /notes %}}

If you are still running an EKS installer released before October 2024, contact [Pulumi support](/support/) to plan a migration to the current installer before changing the Kubernetes version.
