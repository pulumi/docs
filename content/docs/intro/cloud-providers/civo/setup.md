---
title: Civo Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Civo Provider.
---

The [Pulumi Civo provider]({{< relref "./" >}}) uses the Civo SDK to manage and provision resources.

> Pulumi relies on the Civo SDK to authenticate requests from your computer to Civo. Your credentials are never sent
> to pulumi.com.

The [Pulumi Civo Provider]({{< relref "./" >}}) needs to be configured with Civo credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `CIVO_TOKEN`:

    ```bash
    $ export CIVO_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set civo:token XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `civo:token` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-civo/blob/master/README.md).
