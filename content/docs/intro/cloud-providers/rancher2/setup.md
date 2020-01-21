---
title: Rancher2 Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Rancher2 Provider.
---

The [Pulumi Rancher2 provider]({{< relref "./" >}}) uses the Rancher2 SDK to manage and provision resources.

> Pulumi relies on the Rancher2 SDK to authenticate requests from your computer to Rancher2. Your credentials are never sent
> to pulumi.com.

The [Pulumi Rancher2 Provider]({{< relref "./" >}}) needs to be configured with Rancher2 credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `RANCHER_URL`, `RANCHER_ACCESS_KEY` and `RANCHER_SECRET_KEY`:

    ```bash
    $ export RANCHER_URL=XXXXXXXXXXXXXX
    $ export RANCHER_ACCESS_KEY=YYYYYYYYYYYYYY
    $ export RANCHER_SECRET_KEY=ZZZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set rancher2:apiUrl XXXXXXXXXXXXXX
    $ pulumi config set rancher2:accessKey YYYYYYYYYYYYYY --secret
    $ pulumi config set rancher2:secretKey ZZZZZZZZZZZZZZ --secret
    ```

Remember to pass `--secret` when setting `rancher2:accessKey` and `rancher2:secretKey` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-rancher2/blob/master/README.md).
