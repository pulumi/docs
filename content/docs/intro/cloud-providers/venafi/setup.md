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

1. Set the environment variables `VENAFI_URL`, `VENAFI_USER`, `VENAFI_PASS` and `VENAFI_ZONE`:

    ```bash
    $ export VENAFI_URL=WWWWWWWWWWWWWW
    $ export VENAFI_USER=XXXXXXXXXXXXXX
    $ export VENAFI_PASS=YYYYYYYYYYYYYY
    $ export VENAFI_ZONE=ZZZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set venafi:url WWWWWWWWWWWWWW
    $ pulumi config set venafi:tppUsername XXXXXXXXXXXXXX --secret
    $ pulumi config set venafi:tppPassword YYYYYYYYYYYYYY --secret
    $ pulumi config set venafi:zone ZZZZZZZZZZZZZZ
    ```

Remember to pass `--secret` when setting `venafi:tppPassword` so that it is properly encrypted.

#### Venafi Cloud

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
