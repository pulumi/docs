---
title: Aiven Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Aiven Provider.
---

The [Pulumi Aiven provider]({{< relref "./" >}}) uses the Aiven SDK to manage and provision resources.

> Pulumi relies on the Aiven SDK to authenticate requests from your computer to Aiven. Your credentials are never sent
> to pulumi.com.

The [Pulumi Aiven Provider]({{< relref "./" >}}) needs to be configured with Aiven credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `AIVEN_API_TOKEN`:

    ```bash
    $ export AIVEN_API_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set aiven:apiToken XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `aiven:apiToken` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-aiven/blob/master/README.md).
