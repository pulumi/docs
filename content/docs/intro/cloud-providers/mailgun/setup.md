---
title: Mailgun Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Mailgun Provider.
---

The [Pulumi Mailgun provider]({{< relref "./" >}}) uses the Mailgun SDK to manage and provision resources.

> Pulumi relies on the Mailgun SDK to authenticate requests from your computer to Mailgun. Your credentials are never sent
> to pulumi.com.

The [Pulumi Mailgun Provider]({{< relref "./" >}}) needs to be configured with Mailgun credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `MAILGUN_API_KEY`:

    ```bash
    $ export MAILGUN_API_KEY=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set mailgun:apiKey XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `mailgun:apiKey` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-mailgun/blob/master/README.md).
