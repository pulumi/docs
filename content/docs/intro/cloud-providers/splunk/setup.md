---
title: Splunk Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Splunk Provider.
---

The [Pulumi Splunk provider]({{< relref "./" >}}) uses the Splunk SDK to manage and provision resources.

> Pulumi relies on the Splunk SDK to authenticate requests from your computer to Splunk. Your credentials are never sent
> to pulumi.com.

The [Pulumi Splunk Provider]({{< relref "./" >}}) needs to be configured with Splunk credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables for `SPLUNK_URL`, `SPLUNK_USERNAME` and `SPLUNK_PASSWORD`:

    ```bash
    $ export SPLUNK_URL=XXXXXXXXXXXXXX
    $ export SPLUNK_USERNAME=YYYYYYYYYYYYYY
    $ export SPLUNK_PASSWORD=ZZZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set splunk:url XXXXXXXXXXXXXX
    $ pulumi config set splunk:username YYYYYYYYYYYYYY
    $ pulumi config set splunk:password ZZZZZZZZZZZZZZ --secret
    ```

Remember to pass `--secret` when setting `splunk:password` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-splunk/blob/master/README.md).
