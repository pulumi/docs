---
title: Packet.net Setup
meta_desc: This page provides an overview of how to setup the Packet.net SDK to manage and provision resources.
aliases: ["/docs/reference/clouds/packet/setup/"]
---

The [Pulumi Packet provider]({{< relref "./" >}}) uses the Packet.net SDK to manage and provision resources.

> Pulumi relies on the Packet.net SDK to authenticate requests from your computer to Packet.net. Your credentials are never sent
> to pulumi.com.

The [Pulumi Packet.net Provider]({{< relref "./" >}}) needs to be configured with Packet.net credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `PACKET_AUTH_TOKEN`:

    ```bash
    $ export PACKET_AUTH_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set packet:authToken XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `authToken` so that it is properly encrypted.
