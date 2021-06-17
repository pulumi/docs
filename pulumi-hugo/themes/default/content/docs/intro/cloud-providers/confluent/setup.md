---
title: Confluent Cloud Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Confluent Cloud Provider.
---

The [Pulumi Confluent Cloud provider]({{< relref "./" >}}) uses the Confluent Cloud SDK to manage and provision resources.

> Pulumi relies on the Confluent Cloud SDK to authenticate requests from your computer to Confluent Cloud. Your credentials are never sent
> to pulumi.com.

The [Pulumi Confluent Cloud Provider]({{< relref "./" >}}) needs to be configured with Confluent Cloud credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `CONFLUENT_CLOUD_USERNAME` and `CONFLUENT_CLOUD_PASSWORD`:

    ```bash
    $ export CONFLUENT_CLOUD_USERNAME=XXXXXXXXXXXXXX
    $ export CONFLUENT_CLOUD_PASSWORD=YYYYYYYYYYYYYY
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set confluent:username XXXXXXXXXXXXXX
    $ pulumi config set confluent:password YYYYYYYYYYYYYY --secret
    ```

Remember to pass `--secret` when setting `confluent:password` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-confluent/blob/master/README.md).
