---
title_tag: Local-Docker Install | Self-Hosting Pulumi
meta_desc: Installer and installation instructions for deploying the self-hosted Pulumi Cloud in Docker.
title: Local-Docker
h1: Pulumi Cloud self-hosted local-Docker install
menu:
  administration:
        name: Local-Docker
        parent: administration-security-compliance-self-hosted-deployment-options
        weight: 6
        identifier: administration-security-compliance-self-hosted-deployment-options-local-docker
aliases:
  - /docs/guides/self-hosted/local-docker/
  - /docs/pulumi-cloud/self-hosted/deployment-options/local-docker/
  - /docs/pulumi-cloud/admin/self-hosted/deployment-options/local-docker/
pulumi_cloud_feature: self-hosting
---

The [Local-Docker Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/local-docker) is generally meant to be used where an on-premise solution is needed or where the cloud-based installation solutions (i.e. EKS, ECS, AKS) are not possible.

## Prerequisites

You need to provide and manage the following:

* Docker environment running on a server with
  * At least 2 CPU cores,
  * At least 8 GB memory,
  * At least 20 GB SSD storage space.
* MySQL 8.0 database with
  * At least 20 GB SSD storage space,
  * A database user with the following grants:
    * `GRANT ALL PRIVILEGES ON 'pulumi'.* TO 'pulumi'@'%'`
    * `GRANT CREATE USER ON *.* TO 'pulumi'@'%' WITH GRANT OPTION`
* Object storage (for example, MinIO) with
  * At least 200 GB SSD storage space.

## Local-Docker deployment

### Pulumi deploying Pulumi

This installer uses Pulumi to deploy Pulumi Cloud. In this case, you use the Pulumi CLI with a DIY backend (for example, an S3-compatible object store) from the Docker environment server to deploy the service containers.

To this end, you need to set up the following:

* [Download and install the Pulumi CLI](/docs/install/) on the Docker server
* [Log in to an S3-compatible backend](/docs/iac/operations/stack-management/using-a-diy-backend/#aws-s3)
  * This assumes you use a bucket in the object store you are using for the self-hosted Pulumi Cloud. You can use a different state backend if you prefer.
  * It is NOT recommended to use the `local` backend option since you want to make sure this state file is backed up and secured.

### Deployment steps

See the [README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/local-docker/README.md) file provided with the installer package for detailed deployment steps.

## Local-Docker system management and maintenance

### Pulumi Cloud updates

When deploying Pulumi Cloud, it is recommended to pin the image tag to a specific version. See the [installer's README](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/local-docker/README.md) file to set the `imageTag` configuration property for the installer to use.

When ready to update the Pulumi Cloud containers to use a different version, do the following:

* `pulumi login` to the self-managed (not self-hosted) backend as chosen above when installing the self-hosted service.
* `pulumi config set imageTag {image tag}` to set the version you want to use.
* `pulumi up` to deploy the updates.

### Database maintenance

Perform standard database maintenance for your MySQL database.

### Blob storage maintenance

Perform standard storage maintenance for your blob storage.
