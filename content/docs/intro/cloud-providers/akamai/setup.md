---
title: Akamai Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Akamai Provider.
---

The [Pulumi Akamai provider]({{< relref "./" >}}) uses the Akamai SDK to manage and provision resources.

> Pulumi relies on the Akamai SDK to authenticate requests from your computer to Akamai. Your credentials are never sent
> to pulumi.com.

The [Pulumi Akamai Provider]({{< relref "./" >}}) needs to be configured with Akamai credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Create environment variables in the format:

    `AKAMAI{_SECTION_NAME}_*`

    For example, if you specify akamai:propertySection papi you would set the following ENV variables:

    `AKAMAI_PAPI_HOST`  
    `AKAMAI_PAPI_ACCESS_TOKEN`  
    `AKAMAI_PAPI_CLIENT_TOKEN`  
    `AKAMAI_PAPI_CLIENT_SECRET`

    If the section name is `default`, you can omit it, instead using:

    `AKAMAI_HOST`  
    `AKAMAI_ACCESS_TOKEN`  
    `AKAMAI_CLIENT_TOKEN`  
    `AKAMAI_CLIENT_SECRET`

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set akamai:edgerc XXXXXXXXXXXXXX
    $ pulumi config set akamai:propertySection YYYYYYYYYYYYYY
    ```

A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-akamai/blob/master/README.md).
