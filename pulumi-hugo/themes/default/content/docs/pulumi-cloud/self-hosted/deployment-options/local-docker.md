---
title_tag: Local-Docker Install | Self-Hosting Pulumi
meta_desc: Installer and installation instructions for deploying the self-hosted Pulumi Cloud in docker.
title: Local-Docker
h1: Pulumi Cloud self-hosted local-Docker install
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: deployment-options
        weight: 6
aliases:
  - /docs/guides/self-hosted/local-docker/
---

The [Local-Docker Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/local-docker) is generally meant to be used where an on-premise solution is needed or where the cloud-based installation solutions (i.e. EKS, ECS, AKS) are not possible.

## Prerequisites

The customer is required to provide and manage the following:

* Docker environment running on a server with
  * At least 2 CPU cores,
  * At least 8 GB memory,
  * At least 20GB SSD storage space.
* MySQL 8.0 database with
  * At least 20GB SSD storage space,
  * A database user with the folling grants:
    * `GRANT ALL PRIVILEGES ON 'pulumi'.* TO 'pulumi'@'%'`
    * `GRANT CREATE USER ON *.* TO 'pulumi'@'%' WITH GRANT OPTION`
* Object storage (e.g. Minio) with
  * At least 200GB SSD storage space.

## Local-Docker Deployment

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy the Pulumi Cloud. In this case, one uses the Pulumi CLI with a self-managed backend (e.g. an s3-compatible object store) from the Docker environment server to deploy the Service containers.

To this end, you need to set up the following:

* [Download and install the Pulumi CLI](/docs/install/) on the Docker server
* [Login to S3-compatible backend](/docs/concepts/state#aws-s3)
  * The assumption here is that you would use a bucket in the object store you are using for the self-hosted Pulumi Cloud. You can use a different state backend if you prefer.
  * It is NOT recommended to use the `local` backend option since you want to make sure this state file is backed up and secured.

### Deployment Steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/local-docker/README.md) file provided with the installer package for detailed deployment steps.

## Local-Docker System Management and Maintenance

### Pulumi Cloud Updates

When deploying the Pulumi Cloud, it is recommended to pin the image tag to a specific version. See the [installer's README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/local-docker/README.md) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Sevice containers to use a different version, do the following:

* `pulumi login` to the self-managed (not self-hosted) backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database Maintenance

The customer should perform standard DB maintenance for their MySQL database.

### Blob Storage Maintenance

The customer should perform standard storage maintenance for their blob storage.
