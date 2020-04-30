---
title: SignalFx Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi SignalFx Provider.
---

The [Pulumi SignalFx provider]({{< prelref "./" >}}) uses the SignalFx SDK to manage and provision resources.

> Pulumi relies on the SignalFx SDK to authenticate requests from your computer to SignalFx. Your credentials are never sent
> to pulumi.com.

The [Pulumi SignalFx Provider]({{< prelref "./" >}}) needs to be configured with SignalFx credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `SFX_AUTH_TOKEN`:

    ```bash
    $ export SFX_AUTH_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set signalfx:authToken XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `signalfx:authToken` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-signalfx/blob/master/README.md).
