---
title: Auth0 Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Auth0 Provider.
---

The [Pulumi Auth0 provider]({{< relref "./" >}}) uses the Auth0 SDK to manage and provision resources.

> Pulumi relies on the Auth0 SDK to authenticate requests from your computer to Auth0. Your credentials are never sent
> to pulumi.com.

The [Pulumi Auth0 Provider]({{< relref "./" >}}) needs to be configured with Auth0 credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `AUTH0_DOMAIN`, `AUTH0_CLIENT_ID` and `AUTH0_CLIENT_SECRET`:

    ```bash
    $ export AUTH0_DOMAIN=XXXXXXXXXXXXXX
    $ export AUTH0_CLIENT_ID=YYYYYYYYYYYYYY
    $ export AUTH0_CLIENT_SECRET=ZZZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set auth0:domain XXXXXXXXXXXXXX
    $ pulumi config set auth0:clientId YYYYYYYYYYYYYY --secret
    $ pulumi config set auth0:clientSecret ZZZZZZZZZZZZZZ --secret
    ```

Remember to pass `--secret` when setting `auth0:clientId` and `auth0:clientSecret` so that it is properly encrypted. A
full set of configuration parameters can be found listed on the
[Project README](https://github.com/pulumi/pulumi-auth0/blob/master/README.md).
