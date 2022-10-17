---
title: BYO-Infra-Hosted Install
menu:
    userguides:
        parent: self_hosted
        identifier: self_hosted_byo_infra_hosted_install
        weight: 40
meta_desc: Installer for deploying the self-hosted Pulumi Service on your own K8s, MySQL and S3-compatible infrastructure.
---

The [BYO-Infrastructure Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/byo-infra) installer is used to deploy the self-hosted Pulumi Service on your own K8s, MySQL and S3-compatible infrastructure.

## BYO-Infra Deployment

The BYO infrastructure installer uses Pulumi to deploy the following services on your infrastructure:

* Ingress Controller
* Pulumi API and Console applications

Prerequisites and configuration for the your infrastructure can be found in the [BYO-Infrastructure Installer README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/byo-infra/README.md)  

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy the Pulumi Service. In this case, one uses the Pulumi CLI with a self-managed backend (e.g. S3 storage bucket) to deploy all services listed above to stand up the self-hosted Pulumi Service. The installation package includes Pulumi project code so that you can deploy the Service by running `pulumi up`.

To this end, you need to set up the following:

* [Download and install the Pulumi CLI]({{<relref "docs/get-started/install">}}) on your workstation
* [Choose a self-managed storage backend]({{<relref "docs/intro/concepts/state">}})

### Deployment Steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/byo-infra/README.md) file provided with the installer package for detailed deployment steps.

## BYO Infrastructure Hosted System Management and Maintenance

### Pulumi Service Updates

When deploying the Service, it is recommended to pin the Pulumi Service image tag to a specific version. See the installer's [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/byo-infra/README.md) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Sevice containers to use a different version, do the following:

* `pulumi login` to the self-managed (not self-hosted) backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database Maintenance

It is highly recommended to deploy your MySQL server in a redundant configuration with checkpoints or at least periodic backups enabled.

### Bucket Maintenance

It is highly recommended to enable automatic backups for your S3-compatible storage buckets.
