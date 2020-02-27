---
title: HashiCorp Vault Setup
meta_desc: This page provides an overview on how to configure the Pulumi Vault Provider.
---

The [Pulumi Vault provider]({{< relref "./" >}}) uses the Vault SDK to manage resources.

> Pulumi relies on the Vault SDK to authenticate requests from your computer to HashiCorp Vault. Your credentials are never sent
> to pulumi.com.

### Configuring The Provider

Once obtained, there are two ways to communicate your configuration tokens to Pulumi:

1. Set the environment variables `VAULT_ADDR` and `VAULT_TOKEN`:

    ```bash
    $ export VAULT_ADDR=XXXXXX
    $ export VAULT_TOKEN=YYYYYY
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set vault:address XXXXXX
    $ pulumi config set vault:token YYYYYY --secret
    ```

A full set of configuration parameters can be found listed on the [Project README](https://github.com/pulumi/pulumi-vault/blob/master/README.md).
Remember to pass `--secret` when setting `token` so that it is properly encrypted.
