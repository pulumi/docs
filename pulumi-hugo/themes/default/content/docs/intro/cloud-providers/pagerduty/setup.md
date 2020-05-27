---
title: PagerDuty Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi PagerDuty Provider.
---

The [Pulumi PagerDuty provider]({{< relref "./" >}}) uses the PagerDuty SDK to manage and provision resources.

> Pulumi relies on the PagerDuty SDK to authenticate requests from your computer to PagerDuty. Your credentials are never sent
> to pulumi.com.

The [Pulumi PagerDuty Provider]({{< relref "./" >}}) needs to be configured with PagerDuty credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `PAGERDUTY_TOKEN`:

    ```bash
    $ export PAGERDUTY_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set pagerduty:token XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `pagerduty:token` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-pagerduty/blob/master/README.md).
