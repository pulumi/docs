---
title: EKS-Hosted Install
menu:
    userguides:
        parent: self_hosted
        identifier: self_hosted_eks_hosted_install
        weight: 30
meta_desc: Installer for deploying the self-hosted Pulumi service in EKS.
---

The [EKS-Hosted Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted) installer is used to deploy the self-hosted Pulumi service in Amazon Elastic Kuberenetes Service (EKS).

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

This installer uses Pulumi to deploy the Pulumi service. In this case, one uses the pulumi CLI with a self-managed backend (e.g. S3) to deploy all services listed above to stand up the self-hosted Pulumi Service. The installation package includes Pulumi project code so that you can deploy the service by running `pulumi up`.

To this end, you need to set up the following:

* [Download and install the Pulumi CLI]({{<relref "docs/get-started/install">}}) on your workstation
* [Login to S3-compatible backend]({{<relref "docs/intro/concepts/state#logging-into-the-aws-s3-backend">}})

### Deployment Steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted/README.md) file provided with the installer package for detailed deployment steps.

## EKS-Hosted System Management and Maintenance

### Pulumi Service Updates

When deploying the service, it is recommended to pin the Pulumi Service image tag to a specific version. See the installer's [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted/README.md) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Sevice containers to use a different version, do the following:

* `pulumi login` to the self-managed (not self-hosted) backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database Maintenance

The installer configures the RDS backend database for replication and checkpointing. So no additional maintenance is needed by the customer.

### Blob Storage Maintenance

The service automatically creates backups of checkpoint files. However, the customer may want to enable AWS Backup to periodically backup the S3 buckets created by the installer.  
The buckets will have names of the form:

* `pulumi-checkpoint-XXX`
* `pulumi-policy-XXX`

### Updating the EKS Cluster Kubernetes Version

If your EKS-hosted installation was deployed on Kubernetes version 1.19 or later, you can update the `clusterConfig:ClusterVersion` configuration property to the desired version.  
Then, rerun the `npm run install -- update --` command to update the cluster with the new version.

{{% notes type="info" %}}
AWS requires moving one Kubernetes release at a time. So if moving from 1.19 to 1.21, perform the steps twice: once to move to 1.20 and wait for that to complete before moving to 1.21.
{{% /notes %}}

{{% notes type="info" %}}
If running the Pulumi Service with Kubernetes version 1.18, please refer to the installation package README for details on how to upgrade to V2.0 of the EKS installer before upgrading the Kubernetes version.
{{% /notes %}}
