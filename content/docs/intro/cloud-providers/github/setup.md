---
title: GitHub Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi GitHub Provider.
---

The [Pulumi GitHub provider]({{< relref "./" >}}) uses the GitHub SDK to manage and provision resources.

> Pulumi relies on the GitHub SDK to authenticate requests from your computer to GitHub. Your credentials are never sent
> to pulumi.com.

The [Pulumi GitHub Provider]({{< relref "./" >}}) needs to be configured with GitHub credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variable `GITHUB_TOKEN`:

    ```bash
    $ export GITHUB_TOKEN=XXXXXXXXXXXXXX
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set github:token XXXXXXXXXXXXXX --secret
    ```

Remember to pass `--secret` when setting `github:token` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-github/blob/master/README.md).
