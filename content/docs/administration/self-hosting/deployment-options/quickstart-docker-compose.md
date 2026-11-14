---
title_tag: Quickstart Docker Compose | Self-Hosting Pulumi
meta_desc: Quickstart Docker Compose installer for testing of the self-hosted Pulumi Cloud.
title: Docker Compose
h1: Pulumi Cloud self-hosted Docker Compose install
menu:
  administration:
        name: Docker Compose
        parent: administration-security-compliance-self-hosted-deployment-options
        weight: 1
        identifier: administration-security-compliance-self-hosted-deployment-options-quickstart-docker-compose
aliases:
  - /docs/guides/self-hosted/quickstart-docker-compose/
  - /docs/pulumi-cloud/self-hosted/deployment-options/quickstart-docker-compose/
  - /docs/pulumi-cloud/admin/self-hosted/deployment-options/quickstart-docker-compose/
pulumi_cloud_feature: self-hosting
---

The Pulumi Cloud Docker container images can be run using any OCI-compatible container orchestrator. We provide sample Docker Compose files in the [Quickstart Docker Compose Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/quickstart-docker-compose) that can help you get started with your self-evaluation quickly. The commands on this page use paths relative to that installer's `quickstart-docker-compose` directory.

> **Note**: Docker Compose is not required to run these containers. We recommend that you choose a container orchestrator with which your IT team has experience.

Besides the environment variables that each container exposes, you can set the following when using either of the quickstart options below. The `run-ee.sh` script provided to you as part of the self-evaluation package reads them, and uses the default value for any variable you don't set.

`PULUMI_DATA_PATH`: The persistent path where the service should store the checkpoint objects. Default uses `${HOME}/pulumi-self-hosted-installers/data`.

`PULUMI_LOCAL_DATABASE_HOST`: The database instance’s hostname. Default is `pulumi-db`.

`PULUMI_LOCAL_DATABASE_PORT`: The database instance’s port. Default is `3306`.

For example:

```bash
PULUMI_DATA_PATH=/my/persistent/dir PULUMI_LOCAL_DATABASE_HOST=my-db PULUMI_LOCAL_DATABASE_PORT=3306 ./scripts/run-ee.sh
```

Regardless of the quickstart option you choose below, `run-ee.sh` is the way to start the necessary containers.

## Quickstart Docker Compose deployment options

The [Quickstart Docker Compose Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/quickstart-docker-compose) is used to deploy a test system using Docker.

### Option 1: Use the all-in-one approach

To use Pulumi’s all-in-one solution, run `run-ee.sh` with the all-in-one Docker Compose file:

```bash
run-ee.sh -f ./all-in-one/docker-compose.yml
```

This starts all components using working defaults, including a DB container that is migrated using our DB scripts.

{{% notes type="info" %}}
Environment variables should be set in the `./all-in-one/docker-compose.yml` file.
{{% /notes %}}

### Option 2: Provide your own database

The service is tested against a MySQL version 8.0 instance. This option assumes that you have a DB instance called `pulumi-db` running at port `3306` and accessible within a network called `pulumi-self-hosted-installers`. If your instance uses a different hostname or port, set `PULUMI_LOCAL_DATABASE_HOST` and `PULUMI_LOCAL_DATABASE_PORT` as described above.

{{% notes type="info" %}}
You will need the `migrations` folder downloaded locally, which contains the DB scripts that need to be applied against your DB instance.
Your Pulumi sales contact should be able to provide you with this.
{{% /notes %}}

Once the scripts are applied, run `run-ee.sh` without the `-f` flag. By default, it uses the `docker-compose.yml` file at the root of the `quickstart-docker-compose` directory, which is the bring-your-own-database configuration.

## Quickstart Docker Compose system management and maintenance

Because the quickstart option is meant for testing, it needs no real maintenance or management other than perhaps updating the service containers to newer versions.

### Update the Pulumi Cloud containers

The installer's all-in-one Docker Compose file pins each image to a digest (for example, `pulumi/service:latest@sha256:...`), so Docker uses the pinned image and ignores the `latest` tag. Re-running `run-ee.sh` on its own does not pull newer images from Docker Hub.

To update the containers, update the image version in the Docker Compose file and re-run the `run-ee.sh` script.
