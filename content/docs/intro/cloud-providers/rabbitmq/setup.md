---
title: RabbitMQ Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi RabbitMQ Provider.
---

The [Pulumi RabbitMQ provider]({{< relref "./" >}}) uses the RabbitMQ SDK to manage and provision resources.

> Pulumi relies on the RabbitMQ SDK to authenticate requests from your computer to RabbitMQ. Your credentials are never sent
> to pulumi.com.

The [Pulumi RabbitMQ Provider]({{< relref "./" >}}) needs to be configured with RabbitMQ credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `RABBITMQ_ENDPOINT`, `RABBITMQ_USERNAME` and `RABBITMQ_PASSWORD`:

    ```bash
    $ export RABBITMQ_ENDPOINT=XXXXXXXXXXXXXX
    $ export RABBITMQ_USERNAME=YYYYYYYYYYYYYY
    $ export RABBITMQ_PASSWORD=ZZZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set rabbitmq:endpoint XXXXXXXXXXXXXX
    $ pulumi config set rabbitmq:username YYYYYYYYYYYYYY --secret
    $ pulumi config set rabbitmq:password ZZZZZZZZZZZZZZ --secret
    ```

Remember to pass `--secret` when setting `rabbitmq:username` and `rabbitmq:password` so that they are properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-rabbitmq/blob/master/README.md).
