---
title: vSphere Setup
meta_desc: This page provides an overview on how to setup use Pulumi and the vSphere SDK to
           manage and provision resources.
aliases: ["/docs/reference/clouds/vsphere/setup/"]
---

The [Pulumi vSphere provider]({{< relref "./" >}}) uses the vSphere SDK to manage and provision resources.

> Pulumi relies on the vSphere SDK to authenticate requests from your computer to vSphere. Your credentials are never sent
> to pulumi.com.

The [Pulumi vSphere Provider]({{< relref "./" >}}) needs to be configured with vSphere credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `VSPHERE_USER`, `VSPHERE_PASSWORD` and `VSPHERE_SERVER`:

    ```bash
    $ export VSPHERE_USER=XXXXXXXXXXXX
    $ export VSPHERE_PASSWORD=YYYYYYYYYYYY
    $ export VSPHERE_SERVER=ZZZZZZZZZZZZ
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set vsphere:user XXXXXXXXXXXX
    $ pulumi config set vsphere:password YYYYYYYYYYYY --secret
    $ pulumi config set vsphere:vsphereServer ZZZZZZZZZZZZ
    ```

Remember to pass `--secret` when setting `password` so that it is properly encrypted.
