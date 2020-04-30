---
title: MySQL Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi MySQL Provider.
---

The [Pulumi MySQL provider]({{< prelref "./" >}}) uses the MySQL SDK to manage and provision resources.

> Pulumi relies on the MySQL SDK to authenticate requests from your computer to MySQL. Your credentials are never sent
> to pulumi.com.

The [Pulumi MySQL Provider]({{< prelref "./" >}}) needs to be configured with MySQL credentials
before it can be used to manage resources.

### Configuring Credentials

In order to communicate your configuration details to Pulumi:

1. Set the environment variables `MYSQL_ENDPOINT` and `MYSQL_USERNAME`:

    ```bash
    $ export MYSQL_ENDPOINT=XXXXXXXXXXXXXX
    $ export MYSQL_USERNAME=YYYYYYYYYYYYYY
    ```

1. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set mysql:endpoint XXXXXXXXXXXXXX
    $ pulumi config set mysql:username YYYYYYYYYYYYYY
    ```

If you are going to set `mysql:password`, please remember to pass `--secret` so that it is properly encrypted. A full set
of configuration parameters can be found listed on the [Project README](https://github.com/pulumi/pulumi-mysql/blob/master/README.md).
