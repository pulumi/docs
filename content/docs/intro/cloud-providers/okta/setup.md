---
title: Okta Setup
meta_desc: This page provides an overview on how to configure the Pulumi Okta Provider.
---

The [Pulumi Okta provider]({{< prelref "./" >}}) uses the Okta SDK to manage resources.

> Pulumi relies on the Okta SDK to authenticate requests from your computer to Okta. Your credentials are never sent
> to pulumi.com.

### Configuring The Provider

Once obtained, there are two ways to communicate your configuration tokens to Pulumi:

1. Set the environment variables `OKTA_ORG_NAME`, `OKTA_BASE_URL` and `OKTA_API_KEY`:

    ```bash
    $ export OKTA_ORG_NAME=XXXXXX
    $ export OKTA_BASE_URL=YYYYYY
    $ export OKTA_API_KEY=ZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set okta:orgName XXXXXX
    $ pulumi config set okta:baseUrl YYYYYY
    $ pulumi config set okta:apiKey ZZZZZZ
    ```

Remember to pass `--secret` when setting `apiKey` so that it is properly encrypted.
