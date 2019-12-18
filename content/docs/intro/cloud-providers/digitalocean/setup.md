---
title: DigitalOcean Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi DigitalOcean Provider.
aliases: ["/docs/reference/clouds/digitalocean/setup/"]
---

The [Pulumi DigitalOcean provider]({{< relref "./" >}}) uses the DigitalOcean SDK to manage and provision resources.

> Pulumi relies on the DigitalOcean SDK to authenticate requests from your computer to DigitalOcean. Your credentials are never sent
> to pulumi.com.

The [Pulumi DigitalOcean Provider]({{< relref "./" >}}) needs to be configured with DigitalOcean credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `DIGITALOCEAN_TOKEN`:

    ```bash
    $ export DIGITALOCEAN_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set digitalocean:token XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `token` so that it is properly encrypted.
