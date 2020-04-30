---
title: Pulumi API
menu:
    userguides:
        parent: self_hosted
        identifier: self_hosted_api_service
        weight: 1
meta_desc: Pulumi API is one of the components required for self-hosting Pulumi. Self-hosting is available as part of the Enterprise Edition.
---

<div class="note note-info" role="alert">
    <p>
        Self-hosting is only available with the <strong>Pulumi Enterprise Edition</strong>.
    </p>
</div>

The Pulumi API is one of the components required for self-hosting Pulumi in your organization's environment. It provides the necessary APIs for both the CLI and the [Console]({{< prelref "console" >}}).

## Prerequisites

* Provide a server or virtual machine to install and run the Pulumi components (see Minimum System Requirements below).
* Provide a persistent volume for the service to store checkpoint objects.
* Provider a persistent volume for the MySQL data (optional if you are providing your own DB.)
* If you are providing your own DB instance, ensure that it is accessible within the same Docker network that the service and the UI containers will be running in.
    * The default DB endpoint is `pulumi-db:3306`. If you wish to change this, please set `PULUMI_LOCAL_DATABASE_NAME` and `PULUMI_LOCAL_DATABASE_PORT` accordingly (see Script Variables.)
    * If you do not create this network prior to running `run-ee.sh`, it will create only a bridged network on your local host. Ensure that the DB can be accessed by the API service container.
* Provide an external load balancer with TLS termination.

## Minimum System Requirements

| Type | Properties | Notes |
| ---- | ---------- | ----- |
| Compute | 2 CPU cores w/ 8 GB memory | |
| Storage | 20GB SSD |  For MySQL data.<br><br>**Note**: By default, the installation uses a single data path via `PULUMI_DATA_PATH` to map both the SQL data volume and the object storage path. Specify a volume for the `db` container as required. |
| Storage | 200GB SSD |  For Object Storage.<br><br>**Note**: By default, the installation uses a single data path via `PULUMI_DATA_PATH` to map both the SQL data volume and the object storage path. A dedicated path can be set via env var `PULUMI_LOCAL_OBJECTS` for the `api` container. |

> **Note**: The storage recommendations for the Object Storage can be lesser than 200GB depending on your organization size and the expected usage.

## What's In The Container?

The API service is a Go-based application. This is a single binary application that has all of the dependencies it needs in order to run.

## Primary Environment Variables

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_LICENSE_KEY | The license key value. A JWT string.<br><br>**Note**: Be sure to enclose the value in single-quotes. |
| PULUMI_DATABASE_ENDPOINT | The database server endpoint in the format `host:port`. This should be a MySQL 5.6 server. |
| PULUMI_DATABASE_NAME | The name of the database on the database server. |
| PULUMI_API_DOMAIN | The internet or network-local domain using which the service can be reached. Default is `localhost:8080`. |
| PULUMI_CONSOLE_DOMAIN | The internet or network-local domain using which the Console can be reached. Default is `localhost:3000`. |
| PULUMI_LOCAL_OBJECTS | Folder path for persisting state for stacks. Ensure that this path is highly available, and backed-up regularly. |

### Other Environment Variables

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_OBJECTS_BUCKET | S3 bucket name for persisting state for stacks.<br><br>**Note**:Only used if hosted on AWS. |
| RECAPTCHA_SECRET_KEY | reCAPTCHA secret key for self-service password reset. Create a site key and a secret key from Google [here](https://www.google.com/recaptcha/admin). |
| SAML_CERTIFICATE_PUBLIC_KEY | Public key used by the [IdP]({{< prelref "../saml/sso#terminology" >}}) to sign SAML assertions. |
| SAML_CERTIFICATE_PRIVATE_KEY | Private key used by Pulumi to validate the SAML assertions sent by the IdP. |
| GITHUB_OAUTH_ENDPOINT | Used for GitHub API calls. |
| GITLAB_OAUTH_ENDPOINT | Used for GitLab API calls. |
