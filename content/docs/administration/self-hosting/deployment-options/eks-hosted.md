---
title_tag: EKS-Hosted Install | Self-Hosting Pulumi
meta_desc: Installer and installation instructions for deploying the self-hosted Pulumi Cloud in EKS.
title: EKS
h1: Pulumi Cloud self-hosted EKS install
menu:
  administration:
        name: EKS
        parent: administration-security-compliance-self-hosted-deployment-options
        weight: 3
        identifier: administration-security-compliance-self-hosted-deployment-options-eks
aliases:
  - /docs/guides/self-hosted/eks-hosted/
  - /docs/pulumi-cloud/self-hosted/deployment-options/eks-hosted/
  - /docs/pulumi-cloud/admin/self-hosted/deployment-options/eks-hosted/
pulumi_cloud_feature: self-hosting
---

The [EKS-hosted installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted) deploys the self-hosted Pulumi Cloud in Amazon Elastic Kubernetes Service (EKS).

## Prerequisites

You must provide and manage the following:

* An Amazon Route 53 hosted zone.

## EKS-hosted deployment

The EKS-hosted installation of Pulumi deploys the following services:

* EKS - Managed Amazon Elastic Kubernetes Service cluster.
* RDS Aurora - Managed MySQL database for persistent state, with automated replication and snapshotting.
* S3 - Object storage for checkpoints and policy packs.
* CloudWatch Logs - Centralized logging for all cluster pods.
* Route 53 - Managed DNS records.
* ALB - Managed application load balancing and TLS termination.
* ACM - Managed public TLS certificates.

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy Pulumi Cloud. You use the Pulumi CLI with a DIY backend (for example, S3) to deploy all services listed above. The installation package is a set of Pulumi projects, and you deploy each one by running `pulumi up` from its folder.

Before you start, set up the following:

* [Download and install the Pulumi CLI](/docs/install/) on your workstation.
* [Log in to an S3-compatible backend](/docs/iac/operations/stack-management/using-a-diy-backend/#aws-s3).

### Deployment steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted/README.md) file provided with the installer package for detailed deployment steps.

## EKS-hosted system management and maintenance

### Pulumi Cloud updates

When deploying the service, it is recommended to pin the Pulumi Cloud image tag to a specific version. See the installer's [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted/README.md) file to set the `imageTag` configuration property for the installer to use.

When you're ready to update the Pulumi Cloud containers to a different version, run the following from the installer's `90-pulumi-service` project folder:

1. `pulumi login` to the DIY backend you chose when installing the self-hosted service.
1. `pulumi config set imageTag {image tag}` to set the version you want to use.
1. `pulumi up` to deploy the updates.

### Database maintenance

The installer configures the RDS backend database for replication and automated backups, so the customer doesn't need to perform additional database maintenance.

### Blob storage maintenance

The service automatically creates backups of checkpoint files. However, the customer may want to enable AWS Backup to periodically backup the S3 buckets created by the installer.
The buckets will have names of the form:

* `{baseName}-checkpoints-XXX`
* `{baseName}-policypacks-XXX`
* `{baseName}-events-XXX`

### Updating the EKS cluster Kubernetes version

The Kubernetes version of the EKS cluster is set by the `clusterVersion` configuration property of the installer's `05-eks-cluster` project. To update the cluster to a new version, run the following from the `05-eks-cluster` project folder:

1. `pulumi login` to the DIY backend you chose when installing the self-hosted service.
1. `pulumi config set clusterVersion {version}` to set the Kubernetes version you want to use.
1. `pulumi up` to update the cluster.

{{% notes type="info" %}}
AWS requires moving one Kubernetes release at a time. For example, to move from 1.19 to 1.21, perform the steps twice: once to move to 1.20, and then, after that update completes, again to move to 1.21.
{{% /notes %}}
