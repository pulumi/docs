---
title: NS1 Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi NS1 Provider.
---

The [Pulumi NS1 provider]({{< relref "./" >}}) uses the NS1 SDK to manage and provision resources.

> Pulumi relies on the NS1 SDK to authenticate requests from your computer to NS1. Your credentials are never sent
> to pulumi.com.

The [Pulumi NS1 Provider]({{< relref "./" >}}) needs to be configured with NS1 credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `NS1_APIKEY`:

    ```bash
    $ export NS1_APIKEY=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set ns1:apikey XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `ns1:apiKey` so that it is properly encrypted. A
full set of configuration parameters can be found listed on the
[Project README](https://github.com/pulumi/pulumi-ns1/blob/master/README.md).
