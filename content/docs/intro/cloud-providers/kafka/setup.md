---
title: Kafka Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Kafka Provider.
---

The [Pulumi Kafka provider]({{< relref "./" >}}) uses the Kafka SDK to manage and provision resources.

> Pulumi relies on the Kafka SDK to authenticate requests from your computer to Kafka. Your credentials are never sent
> to pulumi.com.

The [Pulumi Kafka Provider]({{< relref "./" >}}) needs to be configured with Kafka credentials
before it can be used to create resources.

### Configuring Credentials

In order to communicate your configuration details to Pulumi:

1. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set kafka:bootstrapServers ["127.0.0.1:9092"]
    ```

A full set of configuration parameters can be found listed on the [Project README](https://github.com/pulumi/pulumi-kafka/blob/master/README.md).
