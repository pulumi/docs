---
title: Fastly Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Fastly Provider.
---

The [Pulumi Fastly provider]({{< prelref "./" >}}) uses the Fastly SDK to manage and provision resources.

> Pulumi relies on the Fastly SDK to authenticate requests from your computer to Fastly. Your credentials are never sent
> to pulumi.com.

The [Pulumi Fastly Provider]({{< prelref "./" >}}) needs to be configured with Fastly credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `FASTLY_API_KEY`:

    ```bash
    $ export FASTLY_API_KEY=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set fastly:apiKey XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `fastly:apiKey` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-fastly/blob/master/README.md).
