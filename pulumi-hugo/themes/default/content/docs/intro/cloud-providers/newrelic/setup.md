---
title: New Relic Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi New Relic Provider.
---

The [Pulumi New Relic provider]({{< relref "./" >}}) uses the New Relic SDK to manage and provision resources.

> Pulumi relies on the New Relic SDK to authenticate requests from your computer to New Relic. Your credentials are never sent
> to pulumi.com.

The [Pulumi New Relic Provider]({{< relref "./" >}}) needs to be configured with New Relic credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `NEWRELIC_API_KEY`:

    ```bash
    $ export NEWRELIC_API_KEY=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set newrelic:apiKey XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `newrelic:apiKey` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-newrelic/blob/master/README.md).
