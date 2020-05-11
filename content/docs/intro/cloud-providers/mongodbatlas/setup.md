---
title: MongoDB Atlas Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi MongoDB Atlas Provider.
---

The [Pulumi MongoDB Atlas provider]({{< relref "./" >}}) uses the MongoDB Atlas SDK to manage and provision resources.

> Pulumi relies on the MongoDB Atlas SDK to authenticate requests from your computer to MongoDB Atlas. Your credentials are never sent
> to pulumi.com.

The [Pulumi MongoDB Atlas Provider]({{< relref "./" >}}) needs to be configured with MongoDB Atlas credentials
before it can be used to manage resources.

### Configuring Credentials

In order to communicate your configuration details to Pulumi:

1. Set the environment variables `MONGODB_ATLAS_PUBLIC_KEY` and `MONGODB_ATLAS_PRIVATE_KEY`:

    ```bash
    $ export MONGODB_ATLAS_PUBLIC_KEY=XXXXXXXXXXXXXX
    $ export MONGODB_ATLAS_PRIVATE_KEY=YYYYYYYYYYYYYY
    ```

1. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set mongodbatlas:publicKey XXXXXXXXXXXXXX --secret
    $ pulumi config set mongodbatlas:privateKey YYYYYYYYYYYYYY --secret
    ```

If you are going to set `mongodbatlas:privateKey` and `mongodbatlas:publicKey`, please remember to pass `--secret` so that they is properly encrypted. A full set
of configuration parameters can be found listed on the [Project README](https://github.com/pulumi/pulumi-mongodbatlas/blob/master/README.md).
