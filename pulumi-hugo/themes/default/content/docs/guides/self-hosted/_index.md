---
title: Self-Hosted Pulumi Service
menu:
    userguides:
        identifier: self_hosted
        weight: 6
meta_desc: Pulumi Enterprise Edition gives you the option to self-host Pulumi within your organization's infrastructure.
---

<div class="note note-info" role="alert">
    <p>
        Self-hosting is only available with the <strong>Pulumi Enterprise Edition</strong>.
    </p>
</div>

This guide walks you through the components that are required to get the Pulumi Service running in your own environment.

There are two services that need to be hosted for the purposes of remote state management and a management UI for users. To store user data, and the state for your [stacks]({{< relref "/docs/intro/concepts/stack" >}}), the following components are also needed:

* MySQL 5.6 DB server with at least 20GB storage space for data
* Minimum 50GB SSD for object storage

> **Note**: You are responsible for the safe backup and storage of the object storage volume, as well as your DB’s data volume.

## Self-Hosted vs. Managed Pulumi Service

The self-hosted version of the Pulumi Service also offers some features that are not available with the managed version (i.e. [app.pulumi.com](https://app.pulumi.com)). The self-hosted installation of Pulumi provides full control of your data -- a requirement for enterprises in certain industries with specific security compliance requirements.

If you are unsure about whether a self-hosted version of the Pulumi Service is right for your organization, [contact us]({{< relref "about#contact" >}}) to learn more.

## Deployment Topology

Pulumi can be installed in almost any on-premise or cloud provider environment. The self-hosted install can be integrated with your preferred identity provider as well, such as:

* GitHub Enterprise
* GitLab Enterprise
* SAML SSO
* Email/password identity

Here are some examples of deployment topologies:

{{< figure src="/images/docs/guides/self-hosted/on-prem-internet-config.png" caption="Internet-Accessible Deployment" >}}

{{< figure src="/images/docs/guides/self-hosted/on-prem-intranet-config.png" caption="Intranet-Only Deployment" >}}

## Components

| Component | Repository |
| --------- | ---------- |
| [API]({{< relref "api" >}}) | [https://hub.docker.com/r/pulumi/service/](https://hub.docker.com/r/pulumi/service/) |
| [Console]({{< relref "console" >}}) |	[https://hub.docker.com/r/pulumi/console/](https://hub.docker.com/r/pulumi/console/) |
| Migrations | [https://hub.docker.com/r/pulumi/migrations/](https://hub.docker.com/r/pulumi/migrations/) |

> **Note**: The above container image repositories are private.

## Quickstart

The above Docker container images can be run using any OCI-compatible container orchestrator. We provide sample docker-compose files that can help you get started with your self-evaluation quickly.

> **Note**: docker-compose is not required to run these containers. We recommend that you choose a container orchestrator with which your IT team has experience.

In addition to the environment variables that each container exposes, the following can be set when using either of the quickstart solutions below. These are used by the `run-ee.sh` script provided to you as part of the self-evaluation package. If any of these variables are not set when you run `run-ee.sh`, the default values will be used.

`PULUMI_DATA_PATH`: The persistent path where the service should store the checkpoint objects. Default uses `/tmp/pulumi-ee/data`.

`PULUMI_LOCAL_DATABASE_NAME`: The database instance’s hostname. Default is `pulumi-db`.

`PULUMI_LOCAL_DATABASE_PORT`: The database instance’s port. Default is `3306`.

For example, `PULUMI_DATA_PATH=/my/persistent/dir LOCAL_DATABASE_NAME=my-db LOCAL_DATABASE_PORT=3306 ./scripts/run-ee.sh`.

Regardless of the quickstart option you choose below, `run-ee.sh` will be the way to start the necessary containers. There will be at most 3 containers (including the DB) for the system to be considered complete.

### Quickstart Option #1 - Using the all-in-one approach

If you would like to use Pulumi’s all-in-one solution, you just need to run the run-ee.sh like this: `run-ee.sh -f ./all-in-one/docker-compose.yml`. This will start all of the necessary components using working defaults, including a DB container that is migrated using our DB scripts.

> **Note**: Values for the environment variables used by the each of the containers in this approach should be set in the `./all-in-one/docker-compose.yml` file.

### Quickstart Option #2 - Provide your own Database

The service is tested against a MySQL version 5.6 instance. It is assumed that you have a DB instance called `pulumi-db` running at port `3306` and accessible within a network called `pulumi-ee`. If your DB instance uses a different port, be sure to update

> **Note**: You will need the `migrations` folder downloaded locally, which contains the DB scripts that need to be applied against your DB instance. Your Pulumi sales contact should be able to provide you with this.
