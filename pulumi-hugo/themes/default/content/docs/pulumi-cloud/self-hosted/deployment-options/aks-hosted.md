---
title_tag: AKS-Hosted Install | Self-Hosting Pulumi
meta_desc: Installer and installation instructions for deploying the self-hosted Pulumi Cloud in AKS.
title: AKS
h1: Pulumi Cloud self-hosted AKS install
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: deployment-options
        weight: 4
aliases:
  - /docs/guides/self-hosted/aks-hosted/
---

The [AKS-Hosted Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/aks-hosted) installer is used to deploy the self-hosted Pulumi Cloud in Azure Kubernetes Service (AKS)

## AKS-Hosted Deployment

The AKS-hosted installation of Pulumi deploys the following services:

* Active Directory application
* Virtual Network and Subnets
* Managed MySQL Server and DB for persistent state and automated replication and snapshotting
* Blob storage for checkpoints and policy packs

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy the Pulumi Cloud. In this case, one uses the Pulumi CLI with a self-managed backend (e.g., S3) to deploy all services listed above to stand up the self-hosted Pulumi Cloud. The installation package includes Pulumi project code so you can deploy the Pulumi Cloud by running `pulumi up`.

To this end, you need to set up the following:

* [Download and install the Pulumi CLI](/docs/install/) on your workstation
* [Login to Azure Blob Storage Backend](/docs/concepts/state#azure-blob-storage)

### Deployment Steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/aks-hosted/README.md) file provided with the installer package for detailed deployment steps.

## AKS-Hosted System Management and Maintenance

### Pulumi Cloud Updates

When deploying the Service, it is recommended to pin the Pulumi Cloud image tag to a specific version. See the [installer's README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/aks-hosted/README.md) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Sevice containers to use a different version, do the following:

* `pulumi login` to the self-managed (not self-hosted) backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database Maintenance

Currently, the installer deploys a single-server MySQL backend database server. Therefore, the customer should enable regular backups for the DB.

### Blob Storage Maintenance

The service automatically creates backups of checkpoint files. However, the customer may want to enable automated backup of the blob storage created by the installer.

### Updating the AKS Cluster Kubernetes Version

To update to a later version of Kubernetes, contact the Pulumi support team.
