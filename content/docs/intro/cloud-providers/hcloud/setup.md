---
title: Hetzner Cloud Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Hetzner Cloud Provider.
---

The [Pulumi Hetzner Cloud provider]({{< relref "./" >}}) uses the Hetzner Cloud SDK to manage and provision resources.

> Pulumi relies on the Hetzner Cloud SDK to authenticate requests from your computer to Hetzner Cloud. Your credentials are never sent
> to pulumi.com.

The [Pulumi Hetzner Cloud Provider]({{< relref "./" >}}) needs to be configured with Hetzner Cloud credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `HCLOUD_TOKEN`:

    ```bash
    $ export HCLOUD_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set hcloud:token XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `hcloud:token` so that it is properly encrypted. A
full set of configuration parameters can be found listed on the
[Project README](https://github.com/pulumi/pulumi-hcloud/blob/master/README.md).
