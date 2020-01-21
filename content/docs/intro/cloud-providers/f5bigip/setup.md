---
title: F5 Big IP Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi F5 Big IP Provider.
---

The [Pulumi F5 Big IP provider]({{< relref "./" >}}) uses the F5 Big IP SDK to manage and provision resources.

> Pulumi relies on the F5 Big IP SDK to authenticate requests from your computer to the resources. Your credentials are never sent
> to pulumi.com.

The [Pulumi F5 Big IP Provider]({{< relref "./" >}}) needs to be configured with F5 Big IP credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `BIGIP_HOST`, `BIGIP_USER` and `BIGIP_PASSWORD`:

    ```bash
    $ export BIGIP_HOST=XXXXXXXXXXXXXX
    $ export BIGIP_USER=YYYYYYYYYYYYYY
    $ export BIGIP_PASSWORD=ZZZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set f5bigip:address XXXXXXXXXXXXXX
    $ pulumi config set f5bigip:username YYYYYYYYYYYYYY
    $ pulumi config set f5bigip:password ZZZZZZZZZZZZZZ --secret
    ```

Remember to pass `--secret` when setting `f5bigip:password` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-f5bigip/blob/master/README.md).
