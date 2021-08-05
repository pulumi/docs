---
title: Minio Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Minio Provider.
---

The [Pulumi Minio provider]({{< relref "./" >}}) uses the Minio SDK to manage and provision resources.

> Pulumi relies on the Minio SDK to authenticate requests from your computer to Minio. Your credentials are never sent
> to pulumi.com.

The [Pulumi Minio Provider]({{< relref "./" >}}) needs to be configured with Minio credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `MAILGUN_API_KEY`, `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY`:

    ```bash
    $ export MINIO_ENDPOINT=XXXXXXXXXXXXXX
    $ export MINIO_ACCESS_KEY=YYYYYYYYYYYYYY
    $ export MINIO_SECRET_KEY=ZZZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set minio:minioServer XXXXXXXXXXXXXX --secret
    $ pulumi config set minio:minioAccessKey YYYYYYYYYYYYYY --secret
    $ pulumi config set minio:minioSecretKey ZZZZZZZZZZZZZZ --secret
    ```

Remember to pass `--secret` when setting `minio:minioAccessKey` and `minio:minioSecretKey` so that they are properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-minio/blob/master/README.md).
