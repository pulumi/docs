---
title_tag: GKE-Hosted Install | Self-Hosting Pulumi
meta_desc: Installer and installation instructions for deploying the self-hosted Pulumi Cloud on Google Kubernetes Engine (GKE).
title: GKE
h1: Pulumi Cloud self-hosted GKE install
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: deployment-options
        weight: 4
aliases:
  - /docs/guides/self-hosted/gke-hosted/
---

The [GKE-Hosted Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/gke-hosted) installer is used to deploy the self-hosted Pulumi Cloud in Google Kubernetes Engine (GKE).

## GKE-Hosted Deployment

The GKE-hosted installation of Pulumi deploys the following services:

* Virtual Network and Subnets
* SQL Server and DB for persistent state and automated replication and snapshotting
* Buckets for checkpoints and policy packs

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy the Pulumi Cloud. In this case, one uses the Pulumi CLI with a self-managed backend (e.g. Google Cloud storage bucket) to deploy all services listed above to stand up the self-hosted Pulumi Cloud. The installation package includes Pulumi project code so that you can deploy the Service by running `pulumi up`.

To this end, you need to set up the following:

* [Download and install the Pulumi CLI](/docs/install/) on your workstation
* [Login to Google Cloud Storage Backend](/docs/concepts/state#google-cloud-storage)

### Deployment Steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/gke-hosted/README.md) file provided with the installer package for detailed deployment steps.

## GKE-Hosted System Management and Maintenance

### Pulumi Cloud Updates

When deploying the Pulumi Cloud, it is recommended to pin the image tag to a specific version. See the [installer's README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/gke-hosted/README.md) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Sevice containers to use a different version, do the following:

* `pulumi login` to the self-managed (not self-hosted) backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database Maintenance

Currently, the installer deploys a single-server MySQL backend database server. By default, Google Cloud provides 7 days of backups.

### Bucket Maintenance

The service automatically creates backups of checkpoint files. However, the customer may want to enable automated backup of the buckets created by the installer.

### Updating the GKE Cluster Kubernetes Version

To update to a later version of Kubernetes, contact the Pulumi support team.
