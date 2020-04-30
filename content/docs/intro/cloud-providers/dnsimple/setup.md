---
title: DNSimple Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi DNSimple Provider.
---

The [Pulumi DNSimple provider]({{< prelref "./" >}}) uses the DNSimple SDK to manage and provision resources.

> Pulumi relies on the DNSimple SDK to authenticate requests from your computer to DNSimple. Your credentials are never sent
> to pulumi.com.

The [Pulumi DNSimple Provider]({{< prelref "./" >}}) needs to be configured with DNSimple credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `DNSIMPLE_TOKEN` and `DNSIMPLE_ACCOUNT`:

    ```bash
    $ export DNSIMPLE_TOKEN=XXXXXXXXXXXXXX
    $ export DNSIMPLE_ACCOUNT=YYYYYYYYYYYYYY
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set dnsimple:token XXXXXXXXXXXXXX --secret
    $ pulumi config set dnsimple:account YYYYYYYYYYYYYY --secret
    ```

Remember to pass `--secret` when setting `dnsimple:token` and `dnsimple:account` so that they are properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-dnsimple/blob/master/README.md).
