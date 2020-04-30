---
title: Datadog Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Datadog Provider.
---

The [Pulumi Datadog provider]({{< prelref "./" >}}) uses the Datadog SDK to manage and provision resources.

> Pulumi relies on the Datadog SDK to authenticate requests from your computer to Datadog. Your credentials are never sent
> to pulumi.com.

The [Pulumi Datadog Provider]({{< prelref "./" >}}) needs to be configured with Datadog credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `DATADOG_API_KEY` and `DATADOG_APP_KEY`:

    ```bash
    $ export DATADOG_API_KEY=XXXXXXXXXXXXXX
    $ export DATADOG_APP_KEY=YYYYYYYYYYYYYY
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set datadog:apiKey XXXXXXXXXXXXXX --secret
    $ pulumi config set datadog:appKey YYYYYYYYYYYYYY --secret
    ```

Remember to pass `--secret` when setting `datadog:apiKey` and `datadog:appKey` so that they are properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-datadog/blob/master/README.md).
