---
title: HashiCorp Nomad Setup
meta_desc: This page provides an overview on how to configure the Pulumi Nomad Provider.
---

The [Pulumi Nomad provider]({{< relref "./" >}}) uses the Nomad SDK to manage resources.

> Pulumi relies on the Nomad SDK to authenticate requests from your computer to HashiCorp Nomad. Your credentials are never sent
> to pulumi.com.

### Configuring The Provider

Once obtained, there are two ways to communicate your configuration tokens to Pulumi:

1. Set the environment variables `NOMAD_ADDR` and `NOMAD_TOKEN`:

    ```bash
    $ export NOMAD_ADDR=XXXXXX
    $ export NOMAD_TOKEN=YYYYYY
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set nomad:address  XXXXXX
    $ pulumi config set nomad:secretId YYYYYY --secret
    ```

A full set of configuration parameters can be found listed on the [Project README](https://github.com/pulumi/pulumi-nomad/blob/master/README.md).
Remember to pass `--secret` when setting `secretId` so that it is properly encrypted.
