---
title: Venafi Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Venafi Provider.
---

The [Pulumi Venafi provider]({{< relref "./" >}}) uses the Venafi SDK to manage and provision resources.

> Pulumi relies on the Venafi SDK to authenticate requests from your computer to Venafi. Your credentials are never sent
> to pulumi.com.

The [Pulumi Venafi Provider]({{< relref "./" >}}) needs to be configured with Venafi credentials
before it can be used to create resources.

### Configuring Credentials

A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-venafi/blob/master/README.md). But here
are the most common setups

#### Venafi Trust Protection Platform

Once obtained, there are two ways to communicate your authorization tokens to Pulumi when talking to Venafi TPP:

1. Setting the environment variables `VENAFI_URL`, `VENAFI_TOKEN` and `VENAFI_ZONE`:

    ```bash
    $ export VENAFI_URL=XXXXXXXXXXXXXX
    $ export VENAFI_TOKEN=YYYYYYYYYYYYYY
    $ export VENAFI_ZONE=ZZZZZZZZZZZZZZ
    ```

2. Using `configuration`, if you prefer storing authorization tokens alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set venafi:url XXXXXXXXXXXXXX
    $ pulumi config set venafi:accessToken YYYYYYYYYYYYYY --secret
    $ pulumi config set venafi:zone ZZZZZZZZZZZZZZ
    ```

Remember to pass `--secret` when setting `venafi:accessToken` so that it is properly encrypted.

##### Generating an Access Token

To generate an access token for TPP Admin, make a `POST` request to the TPP Admin URL. An example would be as
follows:

```
https://TPP_URL/vedauth/authorize/oauth
{
    "client_id": "test-integration",
    "username": "tppadmin",
    "password": "Password123!",
    "scope": "certificate:manage,delete,discover,approve;configuration:manage,delete"
}
```

This will return a response as follows:

```
{
    "access_token": "IGDmq2Gxzjh66L06+8zh8w==",
    "expires": 1612807072,
    "identity": "local:{52f82d28-427b-4197-be56-13367d314799}",
    "refresh_token": "JpftLqgFY0XjPhcIeN/Mtw==",
    "refresh_until": 1636567072,
    "scope": "certificate:approve,delete,discover,manage;configuration:delete,manage",
    "token_type": "Bearer"
}
```

The `access_token` in the response is the value to use for `venafi:accessToken` or `VENAFI_TOKEN`.

##### Refreshing an Access Token

To refresh a specific token, we can make a `POST` request to the TPP Admin URL using the `refresh_token` from the oauth
request. An example would be:

```
https://TPP_URL/vedauth/Authorize/Token
{
    "client_id": "test-integration",
    "refresh_token": "JpftLqgFY0XjPhcIeN/Mtw=="
}
```

This will return a response as follows:

```
{
    "access_token": "Yyn2MbQ8XryCO4YVLR9pcw==",
    "expires": 1612809133,
    "refresh_token": "uuJF9ZbPphvJeJfAlLpTOw==",
    "refresh_until": 1636567072,
    "scope": "certificate:approve,delete,discover,manage;configuration:delete,manage",
    "token_type": "Bearer"
}
```

The `access_token` in the response is the value to use for `venafi:accessToken` or `VENAFI_TOKEN`.

#### Venafi as a Service

Once obtained, there are two ways to communicate your authorization tokens to Pulumi when talking to Venafi TPP:

1. Set the environment variables `VENAFI_API`, and `VENAFI_ZONE`:

    ```bash
    $ export VENAFI_API=XXXXXXXXXXXXXX
    $ export VENAFI_ZONE=YYYYYYYYYYYYYY
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set venafi:apiKey XXXXXXXXXXXXXX --secret
    $ pulumi config set venafi:zone YYYYYYYYYYYYYY
    ```

Remember to pass `--secret` when setting `venafi:apiKey` so that it is properly encrypted.
