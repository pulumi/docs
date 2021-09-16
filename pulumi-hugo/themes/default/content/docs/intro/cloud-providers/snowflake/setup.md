---
title: Snowflake Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Snowflake Provider.
---

The [Pulumi Snowflake provider]({{< relref "./" >}}) uses the Snowflake SDK to manage and provision resources.

> Pulumi relies on the Snowflake SDK to authenticate requests from your computer to Snowflake. Your credentials are never sent
> to pulumi.com.

The [Pulumi Snowflake Provider]({{< relref "./" >}}) needs to be configured with Snowflake credentials
before it can be used to create resources.

### Authentication against Snowflake

The Snowflake provider support multiple ways to authenticate:

* Password
* OAuth Access Token
* OAuth Refresh Token
* Browser Auth
* Private Key

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_REGION` and `SNOWFLAKE_USERNAME` with the correct combination of authentication variables:

    ```bash
    $ export SNOWFLAKE_ACCOUNT=XXXXXXXXXXXXXX
    $ export SNOWFLAKE_REGION=YYYYYYYYYYYYYY
    $ export SNOWFLAKE_USERNAME=ZZZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set snowflake:account XXXXXXXXXXXXXX
    $ pulumi config set snowflake:region YYYYYYYYYYYYYY
    $ pulumi config set snowflake:username ZZZZZZZZZZZZZZ
    ```

Remember to pass `--secret` when setting any secret keys so that they are properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-cloudamqp/blob/master/README.md).
