---
title: GKE-Hosted Install
menu:
    userguides:
        parent: self_hosted
        identifier: self_hosted_gke_hosted_install
        weight: 40
meta_desc: Installer for deploying the self-hosted Pulumi Service on Google Kubernetes Engine (GKE).
---

The [GKE-Hosted Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/gke-hosted) installer is used to deploy the self-hosted Pulumi Service in Google Kubernetes Engine (GKE).

## GKE-Hosted Deployment

The GKE-hosted installation of Pulumi deploys the following services:

* Virtual Network and Subnets
* SQL Server and DB for persistent state and automated replication and snapshotting
* Buckets for checkpoints and policy packs

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy the Pulumi Service. In this case, one uses the Pulumi CLI with a self-managed backend (e.g. GCP storage bucket) to deploy all services listed above to stand up the self-hosted Pulumi Service. The installation package includes Pulumi project code so that you can deploy the Service by running `pulumi up`.

To this end, you need to set up the following:

* [Download and install the Pulumi CLI]({{<relref "docs/get-started/install">}}) on your workstation
* [Login to GCP Storage Backend]({{<relref "docs/intro/concepts/state#logging-into-the-google-cloud-storage-backend">}})

### Deployment Steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/gke-hosted/README.md) file provided with the installer package for detailed deployment steps.

## GKE-Hosted System Management and Maintenance

### Pulumi Service Updates

When deploying the Service, it is recommended to pin the Pulumi Service image tag to a specific version. See the installer's [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/gke-hosted/README.md) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Sevice containers to use a different version, do the following:

* `pulumi login` to the self-managed (not self-hosted) backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database Maintenance

Currently, the installer deploys a single-server MySQL backend database server. By default, GCP provides 7 days of backups.

### Bucket Maintenance

The service automatically creates backups of checkpoint files. However, the customer may want to enable automated backup of the buckets created by the installer.

### Updating the GKE Cluster Kubernetes Version

To update to a later version of Kubernetes, contact the Pulumi support team.
