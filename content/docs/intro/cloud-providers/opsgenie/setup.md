---
title: Opsgenie Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Opsgenie Provider.
---

The [Pulumi Opsgenie provider]({{< relref "./" >}}) uses the Opsgenie SDK to manage and provision resources.

> Pulumi relies on the Opsgenie SDK to authenticate requests from your computer to Opsgenie. Your credentials are never sent
> to pulumi.com.

The [Pulumi Opsgenie Provider]({{< relref "./" >}}) needs to be configured with Opsgenie credentials
before it can be used to manage resources.

### Configuring Credentials

In order to communicate your configuration details to Pulumi:

1. Set the environment variables `OPSGENIE_API_KEY` and (an optional) `OPSGENIE_API_URL`:

    ```bash
    $ export OPSGENIE_API_KEY=XXXXXXXXXXXXXX
    $ export OPSGENIE_API_URL=YYYYYYYYYYYYYY
    ```

1. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set opsgenie:apiKey XXXXXXXXXXXXXX --secret
    $ pulumi config set opsgenie:apiUrl YYYYYYYYYYYYYY
    ```

If you are going to set `opsgenie:apiKey`, please remember to pass `--secret` so that it is properly encrypted. A full set
of configuration parameters can be found listed on the [Project README](https://github.com/pulumi/pulumi-opsgenie/blob/master/README.md).
