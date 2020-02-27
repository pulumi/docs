---
title: Linode SDK Setup
meta_desc: This page provides an overview on how to setup the Linode SDK for Pulumi.
aliases: ["/docs/reference/clouds/linode/setup/"]
---

The [Pulumi Linode provider]({{< relref "./" >}}) uses the Linode SDK to manage and provision resources.

> Pulumi relies on the Linode SDK to authenticate requests from your computer to Linode. Your credentials are never sent
> to pulumi.com.
The [Pulumi Linode Provider]({{< relref "./" >}}) needs to be configured with Linode credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `PACKET_AUTH_TOKEN`:

    ```bash
    $ export LINODE_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set linode:token XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `token` so that it is properly encrypted.
