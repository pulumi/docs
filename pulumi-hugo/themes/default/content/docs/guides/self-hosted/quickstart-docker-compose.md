---
title: Quickstart Docker Compose Install
menu:
    userguides:
        parent: self_hosted
        identifier: self_hosted_quickstart_docker_compose_install
        weight: 10
meta_desc: Quickstart Docker compose installer for testing of the self-hosted Pulumi service.
---

The Pulumi Service Docker container images can be run using any OCI-compatible container orchestrator. We provide sample docker-compose files that can help you get started with your self-evaluation quickly.

> **Note**: docker-compose is not required to run these containers. We recommend that you choose a container orchestrator with which your IT team has experience.

In addition to the environment variables that each container exposes, the following can be set when using either of the quickstart solutions below. These are used by the `run-ee.sh` script provided to you as part of the self-evaluation package. If any of these variables are not set when you run `run-ee.sh`, the default values will be used.

`PULUMI_DATA_PATH`: The persistent path where the service should store the checkpoint objects. Default uses `/tmp/pulumi-ee/data`.

`PULUMI_LOCAL_DATABASE_NAME`: The database instance’s hostname. Default is `pulumi-db`.

`PULUMI_LOCAL_DATABASE_PORT`: The database instance’s port. Default is `3306`.

For example, `PULUMI_DATA_PATH=/my/persistent/dir LOCAL_DATABASE_NAME=my-db LOCAL_DATABASE_PORT=3306 ./scripts/run-ee.sh`.

Regardless of the quickstart option you choose below, `run-ee.sh` will be the way to start the necessary containers. There will be at most 3 containers (including the DB) for the system to be considered complete.

## Quickstart Docker Compose Deployment Options

The [Quickstart Docker Compose Installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/quickstart-docker-compose) is used to deploy a test system using Docker.

### Option #1 - Using the all-in-one approach

If you would like to use Pulumi’s all-in-one solution, you just need to run `run-ee.sh` like this: `run-ee.sh -f ./all-in-one/docker-compose.yml`. This will start all components using working defaults, including a DB container that is migrated using our DB scripts.

{{% notes "info" %}}
Environment variables should be set in the `./all-in-one/docker-compose.yml` file.
{{% /notes %}}

### Option #2 - Provide your own Database

The service is tested against a MySQL version 5.6 instance. It is assumed that you have a DB instance called `pulumi-db` running at port `3306` and accessible within a network called `pulumi-ee`.

{{% notes "info" %}}
You will need the `migrations` folder downloaded locally, which contains the DB scripts that need to be applied against your DB instance.
Your Pulumi sales contact should be able to provide you with this.
{{% /notes %}}

## Quickstart Docker Compose System Management and Maintenance

Since the quickstart option is meant to be used for testing purposes, there is no real maintenance or management needed other than perhaps updating the service containers with the latest versions.

### Updating the Pulumi Service Containers

For testing purposes, it is recommended to use the `latest` image tag in the docker compose file and re-run the `run-ee.sh` script when there are newer versions of the service image pushed to docker hub.

If you specified a specific image version in the docker compose file, then simply update the version tag and re-run the `run-ee.sh` script.
