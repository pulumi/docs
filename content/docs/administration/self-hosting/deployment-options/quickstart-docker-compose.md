---
title_tag: Try Self-Hosted Pulumi Cloud with Docker Compose
meta_desc: Evaluate self-hosted Pulumi Cloud in about ten minutes with the all-in-one Docker Compose stack.
title: Docker Compose
h1: Try Self-Hosted Pulumi Cloud with Docker Compose
meta_image: /images/docs/meta-images/docs-meta.png
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
---

The fastest way to try self-hosted Pulumi Cloud is the all-in-one Docker Compose stack. It runs the API, the web Console, a migrated MySQL database, and OpenSearch on a single host with working defaults, so you can evaluate the full platform in about ten minutes. Use it for evaluation and testing; for production, see the [production deployment options](/docs/administration/self-hosting/deployment-options/).

## Prerequisites

- [Docker Engine](https://docs.docker.com/engine/install/) with the Docker Compose plugin (v2).
- A host with at least 2 CPU cores, 8 GB of memory, and 20 GB of free disk.
- Ports `3000` (Console), `8080` (API), and `9200`/`5601` (OpenSearch) available on the host.
- A Pulumi license key.

{{% notes "info" %}}
Self-hosted Pulumi Cloud requires a license key set in `PULUMI_LICENSE_KEY`. [Get an evaluation license](/product/self-hosted/#self-hosted-trial) to get started.
{{% /notes %}}

## Run the all-in-one stack

1. Clone the installer and change into the quickstart directory:

    ```bash
    git clone https://github.com/pulumi/pulumi-self-hosted-installers.git
    cd pulumi-self-hosted-installers/quickstart-docker-compose
    ```

1. Set your license key:

    ```bash
    export PULUMI_LICENSE_KEY=<your-license-key>
    ```

1. Start the stack:

    ```bash
    ./scripts/run-ee.sh -f ./all-in-one/docker-compose.yml
    ```

    This starts every component with working defaults, including a MySQL container that is migrated automatically. Checkpoint data is stored under `$HOME/pulumi-self-hosted-installers/data` by default; override it with `PULUMI_DATA_PATH`.

1. Open the Console at [http://localhost:3000](http://localhost:3000) and create the first account. The first user to register becomes an administrator.

1. Point the CLI at your instance and follow the prompt to create an access token:

    ```bash
    pulumi login http://localhost:8080
    ```

1. Verify the connection:

    ```bash
    pulumi whoami
    ```

To stop the stack, press `Ctrl+C`, then remove the containers with `docker compose -f ./all-in-one/docker-compose.yml down`. Delete the data directory to discard evaluation state.

## Advanced configuration

The `run-ee.sh` script honors the following environment variables; unset variables fall back to working defaults:

- `PULUMI_DATA_PATH`: persistent path for checkpoint objects. Defaults to `$HOME/pulumi-self-hosted-installers/data`.
- `PULUMI_LOCAL_DATABASE_NAME`: the database hostname. Default is `pulumi-db`.
- `PULUMI_LOCAL_DATABASE_PORT`: the database port. Default is `3306`.

Other settings — identity providers, object storage, encryption keys — are configured in the `environment` blocks of `./all-in-one/docker-compose.yml`. See [Components](/docs/administration/self-hosting/components/) for the full set of variables each container accepts.

### Bring your own database

To run against an existing MySQL 8.0 instance instead of the bundled database, start the service with the base `docker-compose.yml` and point it at a database reachable as `pulumi-db:3306` on the `pulumi-ee` network. This path requires the `migrations` folder to apply the schema; contact [sales@pulumi.com](mailto:sales@pulumi.com) to obtain it.

## Updating

For evaluation, pin the `latest` image tag in the compose file and re-run `run-ee.sh` to pull newer service images. If you pinned a specific version, update the tag and re-run the script.
