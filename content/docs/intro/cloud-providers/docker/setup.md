---
title: Docker Setup
meta_desc: This page provides an overview on how to configure the Pulumi Docker Provider.
---

The [Pulumi Docker provider]({{< prelref "./" >}}) uses the Docker SDK to manage resources.

> Pulumi relies on the Docker SDK to authenticate requests from your computer to Docker. Your credentials are never sent
> to pulumi.com.

### Configuring The Provider

Once obtained, there are two ways to communicate your configuration tokens to Pulumi:

1. Set the environment variable `DOCKER_HOST`:

    ```bash
    $ export DOCKER_HOST=tcp://127.0.0.1:2376/
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set docker:host tcp://127.0.0.1:2376/
    ```
