---
title: Yandex Cloud Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi Yandex Cloud Provider.
---

The [Pulumi Yandex Cloud provider]({{< relref "./" >}}) uses the Yandex Cloud SDK to manage and provision resources.

> Pulumi relies on the Yandex Cloud SDK to authenticate requests from your computer to Yandex Cloud. Your credentials are never sent
> to pulumi.com.

The [Pulumi Yandex Cloud Provider]({{< relref "./" >}}) needs to be configured with Yandex Cloud credentials
before it can be used to create resources.

### Configuring The Provider

Once obtained, there are two ways to communicate your configuration to Pulumi:

1. Set the environment variables `YC_TOKEN` or `YC_SERVICE_ACCOUNT_KEY_FILE` and `YC_CLOUD_ID` and `YC_FOLDER_ID`:

    ```bash
    $ export YC_TOKEN=XXXXXX
    $ export YC_CLOUD_ID=YYYYYY
    $ export YC_FOLDER_ID=ZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set yandex:token XXXXXX --secret
    $ pulumi config set yandex:cloudId YYYYYY
    $ pulumi config set yandex:yandex:folderId ZZZZZZ
    ```

A full set of configuration parameters can be found listed on the [Project README](https://github.com/pulumi/pulumi-yandex/blob/master/README.md).
Remember to pass `--secret` when setting `token` so that it is properly encrypted.
