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

You can find information in the [New Relic](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/) docs
regarding how to create the specific keys. Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `NEWRELIC_API_KEY`, `NEW_RELIC_API_KEY` and `NEW_RELIC_ADMIN_API_KEY`:

    ```bash
    $ export NEW_RELIC_ACCOUNT_ID=XXXXXXXXXXXXXX
    $ export NEW_RELIC_API_KEY=YYYYYYYYYYYYYY
    $ export NEW_RELIC_ADMIN_API_KEY=ZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set newrelic:accountId XXXXXXXXXXXXXX
    $ pulumi config set newrelic:apiKey YYYYYYYYYYYYYY --secret
    $ pulumi config set newrelic:adminApiKey ZZZZZZZZZZZZ --secret
    ```

Remember to pass `--secret` when setting `newrelic:apiKey` and `newrelic:adminApiKey` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-newrelic/blob/master/README.md).
