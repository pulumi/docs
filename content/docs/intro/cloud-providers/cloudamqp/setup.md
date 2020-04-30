---
title: CloudAMQP Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi CloudAMQP Provider.
---

The [Pulumi CloudAMQP provider]({{< prelref "./" >}}) uses the CloudAMQP SDK to manage and provision resources.

> Pulumi relies on the CloudAMQP SDK to authenticate requests from your computer to CloudAMQP. Your credentials are never sent
> to pulumi.com.

The [Pulumi CloudAMQP Provider]({{< prelref "./" >}}) needs to be configured with CloudAMQP credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `CLOUDAMQP_APIKEY`:

    ```bash
    $ export CLOUDAMQP_APIKEY=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set cloudamqp:apikey XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `cloudamqp:apikey` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-cloudamqp/blob/master/README.md).
