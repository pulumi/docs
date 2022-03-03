---
title: Pulumi API
menu:
    userguides:
        parent: self_hosted_components
        identifier: self_hosted_api_service
        weight: 1
meta_desc: Pulumi API is one of the components required for self-hosting the Pulumi Service. Self-hosting is available as part of the Pulumi Business Critical Edition.
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. [Contact us]({{< relref "/contact.md" >}}) if you would like to evaluate Self-Hosted Pulumi Service.

To manage your state with a self-managed backend, such as a cloud storage bucket, see [State and Backends]({{< relref "/docs/intro/concepts/state" >}}).
{{% /notes %}}

The Pulumi API is one of the components required for self-hosting the Pulumi Service in your organization's environment. It provides the necessary APIs for both the CLI and the [Console]({{< relref "console" >}}).

## Prerequisites

* Provide a server or virtual machine to install and run the Pulumi components (see Minimum System Requirements below).
* Provide a persistent volume for the service to store checkpoint objects.
* Provider a persistent volume for the MySQL data (optional if you are providing your own DB.)
* If you are providing your own DB instance, ensure that it is accessible within the same Docker network that the service and the UI containers will be running in.
    * The default DB endpoint is `pulumi-db:3306`. If you wish to change this, set `PULUMI_LOCAL_DATABASE_NAME` and `PULUMI_LOCAL_DATABASE_PORT` accordingly (see Script Variables.)
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

{{% notes type="info" %}}
The container image repository is private. [Contact us]({{< relref "/contact.md" >}}) if you would like to evaluate Self-Hosted Pulumi Service.
{{% /notes %}}

The API service is a Go-based application. This is a single binary application that has all of the dependencies it needs in order to run.

### Server

This container runs an HTTP server which provides the APIs needed by the Console and the CLI. By default, this container will serve using port `8080` over standard HTTP. If [TLS](#tls-environment-variables) is configured the server will instead serve over port `8443` using HTTPS.

## Environment Variables for Core Infrastructure

The core infrastructure components to successfully run the API service are the database, object storage, and encryption services.
Depending on your requirements, you can configure additional (optional) identity services as well as enhanced security
between the API and the database.

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_LICENSE_KEY | The license key value. A JWT string.<br><br>**Note**: Be sure to enclose the value in single-quotes. |
| PULUMI_DATABASE_ENDPOINT | The database server endpoint in the format `host:port`. This should be a MySQL 5.6 server. |
| PULUMI_DATABASE_NAME | The name of the database on the database server. |
| PULUMI_API_DOMAIN | The internet or network-local domain using which the API service can be reached, e.g. `pulumiapi.acmecorp.com`. Default is `localhost:8080`. |
| PULUMI_CONSOLE_DOMAIN | The internet or network-local domain using which the Console can be reached, e.g. `pulumiconsole.acmecorp.com`. Default is `localhost:3000`. |

## Object storage

The service saves the state of every stack, that uses it as the backend, to a persistent object storage. If your org uses policy
packs, then anytime a user publishes a policy pack, it gets uploaded to the same object storage service as well. Both the
state (checkpoint) and the policy pack must use different buckets on the same object storage service.

### Local storage

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_LOCAL_OBJECTS | Folder path for persisting state for stacks. Ensure that this path is highly available, and backed-up regularly. Only use this if you want the service to persist objects to a local path. |
| PULUMI_POLICY_PACK_LOCAL_HTTP_OBJECTS | Folder path for persisting published policy packs. Ensure that this path is highly available, and backed-up regularly. Only use this if you want the service to persist policy packs to a local path. |

### AWS S3

{{% notes type="info" %}}
If you are using an S3-compatible object storage such as Minio, for example, you must also configure
the [AWS](#cloud-provider-authentication) credentials as applicable for your Minio configuration.
If your Minio configuration doesn't require a region, you should still specify the `AWS_REGION` with
any valid AWS region name. For example, `us-west-2`.
{{% /notes %}}

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_CHECKPOINT_BLOB_STORAGE_ENDPOINT | The storage endpoint for persisting stack state/checkpoint. The value takes the format: `s3://<bucket-name>`. The `s3://` scheme also supports query-params. See the GoCloud docs for an [example](https://gocloud.dev/howto/blob/#s3-compatible) of the query-params. |
| PULUMI_POLICY_PACK_BLOB_STORAGE_ENDPOINT | The storage endpoint for persisting published policy packs. The value takes the format: `s3://<bucket-name>`. Similar to `PULUMI_CHECKPOINT_BLOB_STORAGE_ENDPOINT`, this also supports query-params. |

### Azure Storage

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_CHECKPOINT_BLOB_STORAGE_ENDPOINT | The storage endpoint for persisting stack state/checkpoint. The value takes the format: `azblob://<blob-container>`. |
| PULUMI_POLICY_PACK_BLOB_STORAGE_ENDPOINT | The storage endpoint for persisting published policy packs. The value takes the format: `azblob://<blob-container>`. |
| AZURE_STORAGE_ACCOUNT | The name of the Azure storage account where the blob containers for checkpoint and policy pack have been created. See [Cloud Provider Authentication](#azure) for additional configuration options for Azure. |
| AZURE_STORAGE_KEY | (Optional) The primary or secondary storage key for the storage account. You only need to specify this if you are _not_ using Azure MSI. |

## Encryption services

The service supports using a master key available in a local-path or in a remote key management service.
You only need to configure one of the support services.

### Local keys

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_LOCAL_KEYS | Folder path that contains a random 32-byte key. Ensure that this path is highly available, and backed-up regularly. |

### AWS KMS

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_KMS_KEY | ARN for the AWS KMS customer master key resource. |

### Azure KeyVault

{{% notes type="info" %}}
When you need to create a new version of a key, do not disable the previous version. All versions of the key must remain
active. The API service never has access to the private key material of the key you create in Azure KeyVault. It only
uses the public key for encryption. The API will request KeyVault to decrypt a cipher text.  
{{% /notes %}}

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_AZURE_KV_URI | Azure KeyVault URI. For example, `https://<vault-name>.vault.azure.net`. |
| PULUMI_AZURE_KV_KEY_NAME | The name of the key in KeyVault. The key must be an RSA key type. We recommend a key size of 2048 for most cases. The key operations must support `Encrypt` and `Decrypt`. Otherwise, the service will fail to start. |
| PULUMI_AZURE_KV_KEY_VERSION | The version of the key that the service should use. Note: All previous versions of the key must remain enabled. |

## Cloud Provider Authentication

These settings are required if you are running the Pulumi Service on one of these clouds or using one of their services.

### AWS

For more information about authenticating with AWS services, see the AWS SDK [docs](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_environment.html).

| Variable Name | Description |
| ------------- | ----------- |
| AWS_REGION | The region where the dependent AWS services used by Pulumi Service have been created. For example, the KMS key must exist in this region. Similarly, if you are using RDS, then there must be a writable cluster in this region. |
| AWS_ACCESS_KEY_ID | The AWS access key ID. |
| AWS_SECRET_ACCESS_KEY | The AWS secret key. |
| AWS_PROFILE | The AWS profile. |
| AWS_ROLE_ARN | The AWS role ARN to assume using the base access keys. |

### Azure

{{% notes type="info" %}}
Many of Azure's services support using Managed System Identity (MSI). As such, the Pulumi Service can also be configured
to use MSI to connect to all dependent Azure services (such as Azure KeyVault and Azure Storage). However,
if you would like to use a self-managed Service Principal (aka AAD client credentials) instead, you must specify the
Azure Storage account key using the `AZURE_STORAGE_KEY` env var.
{{% /notes %}}

| Variable Name | Description |
| ------------- | ----------- |
| AZURE_CLIENT_ID | Client ID of the Azure Managed System Identity or the self-managed Service Principal (SP) that should be used for both Azure KeyVault and Storage. The MSI or the SP must have access to Key Management operations (`Get`, `Encrypt` and `Decrypt`) of the KeyVault you plan to use. |
| AZURE_CLIENT_SECRET | (Optional) Client secret of the Azure SP. |
| AZURE_TENANT_ID | (Optional) Tenant ID of the Azure SP. |
| AZURE_SUBSCRIPTION_ID | (Optional) Subscription ID of the Azure AP. |
| AZURE_STORAGE_DOMAIN | (Optional) The custom domain for your storage domain, if any. If this is not provided, the default Azure public domain "blob.core.windows.net" will be used. |

## Other Environment Variables {#other-env-vars}

| Variable Name | Description |
| ------------- | ----------- |
| GITHUB_OAUTH_ENDPOINT | Used for GitHub API calls. |
| GITLAB_OAUTH_ENDPOINT | Used for GitLab API calls. |
| PULUMI_DATABASE_USER_NAME | Name of the database user the Pulumi Service connects as. Leave default unless you are having trouble connecting to your database.
| PULUMI_DATABASE_USER_PASSWORD | Password of the database user the Pulumi Service connects as. Leave default unless you are having trouble connecting to your database.
| PULUMI_DISABLE_EMAIL_LOGIN | When `true` the API will disallow logins using the email/password identity. To hide the email login option from the Console refer to the [email identity configuration]({{< relref "/docs/guides/self-hosted/components/console#email-identity" >}}) for the Console. |
| PULUMI_DISABLE_EMAIL_SIGNUP | When `true` the API will disallow signups using the email/password identity. To hide the email signup option from the Console refer to the [email identity configuration]({{< relref "/docs/guides/self-hosted/components/console#email-identity" >}}) for the Console. |
| RECAPTCHA_SECRET_KEY | reCAPTCHA secret key for self-service password reset. Create a [site key and a secret key from Google](https://www.google.com/recaptcha/admin). |
| SAML_CERTIFICATE_PUBLIC_KEY | Public key used by the [IdP]({{< relref "/docs/reference/glossary#idp" >}}) to sign SAML assertions. Learn how to [set SAML_CERTIFICATE_PUBLIC_KEY]({{< relref "/docs/guides/self-hosted/saml-sso" >}}). |
| SAML_CERTIFICATE_PRIVATE_KEY | Private key used by Pulumi to validate the SAML assertions sent by the IdP. Learn how to [set SAML_CERTIFICATE_PRIVATE_KEY]({{< relref "/docs/guides/self-hosted/saml-sso" >}}). |

## TLS Environment Variables

### API Service

The service is configurable to serve the API using TLS. The following environment variables are _all_ required in order to enable TLS. The values of the environment variables may either be a filepath or the actual value of the entity. If these variables are set, the service will be served over HTTPS (i.e using TLS) using port `8443`. If the following variables are not set the service will default to serving over HTTP using port `8080`.

| Variable Name       | Description                                                                                               |
|---------------------|-----------------------------------------------------------------------------------------------------------|
| API_TLS_CERTIFICATE | The TLS certificate. The certificate must be supplied in X.509 format and must be PEM encoded.            |
| API_TLS_PRIVATE_KEY | The private key associated with the TLS certificate. The private key must be PEM encoded.                 |
| API_MIN_TLS_VERSION | The minimum version of TLS to use when serving the API (must be in \<major>.\<minor> format, e.g. `1.2`). |

> _Note: Self-signed certificates may be used to configure TLS in the event the need for a trusted entity is not necessary. A self-signed cert and private key may be generated using OpenSSL. The following command uses OpenSSL to generate a self-signed certificate. This example will output two files, the certificate (cert.pem) and the private key (key.pem) used to sign it._

>
```
openssl \
  req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem \
  -days { days_unitl_expiration } -nodes -subj "/CN={ common_name }"
```

### Database Connections

#### API Service

The service is configurable to enable connections to the backend SQL database over TLS. The following environment variables are _all_ required to connect to the database using TLS. If these variables are set the service will establish connections to the database using TLS, otherwise the service will default to connecting without TLS. The same ports will be used for communication to the database regardless of whether TLS is configured or not.

| Variable Name            | Description                                                                                                   |
|--------------------------|---------------------------------------------------------------------------------------------------------------|
| DATABASE_CA_CERTIFICATE  | The CA certificate used to establish TLS connections with the database. This certificate must be PEM encoded. This must be set to the value of the certificate itself and _not_ a filepath to the location of the certificate file. |
| DATABASE_MIN_TLS_VERSION | The minimum TLS version to use for database connections (must be in \<major>.\<minor> format, e.g. `1.2`).    |

#### Migrations

The database migrations container is configurable to enable connections to the database over TLS. To use TLS, the following environment variable must be set. The default is to not use TLS.

| Variable Name            | Description                                                                                                   |
|--------------------------|---------------------------------------------------------------------------------------------------------------|
| DATABASE_CA_CERTIFICATE  | The CA certificate used to establish TLS connections with the database. This certificate must be PEM encoded. This must be set to the value of the certificate itself and _not_ a filepath to the location of the certificate file. |
| MYSQL_ROOT_USERNAME      | The root username to log in to the MySQL database. Defaults to `root`. |
| MYSQL_ROOT_PASSWORD      | The root user password to log in to the MySQL database. |
| MYSQL_ALLOW_EMPTY_PASSWORD    | Set to `true` to allow the container to be started with a blank password for the root user. |
| PULUMI_DATABASE_ENDPOINT      | The database server endpoint in the format `host:port`. This should be a MySQL 5.6 server. |
| PULUMI_DATABASE_PING_ENDPOINT | The database server endpoint to ping for availability before login. |
| RUN_MIGRATIONS_EXTERNALLY     | Request for migrations to be run against an external database. |
