---
title: AzureDevOps Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi AzureDevOps Provider.
---

The [Pulumi AzureDevOps provider]({{< relref "./" >}}) uses the AzureDevOps SDK to manage and provision resources.

> Pulumi relies on the AzureDevOps SDK to authenticate requests from your computer to AzureDevOps. Your credentials are never sent
> to pulumi.com.

The [Pulumi AzureDevOps Provider]({{< relref "./" >}}) needs to be configured with AzureDevOps credentials
before it can be used to create resources.

### Configuring Credentials

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `AZDO_ORG_SERVICE_URL` and `AZDO_PERSONAL_ACCESS_TOKEN`:

    ```bash
    $ export AZDO_ORG_SERVICE_URL=XXXXXXXXXXXXXX
    $ export AZDO_PERSONAL_ACCESS_TOKEN=YYYYYYYYYYYYYY
    ```

2. Set them using configuration, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

    ```bash
    $ pulumi config set azuredevops:orgServiceUrl XXXXXXXXXXXXXX --secret
    $ pulumi config set azuredevops:personalAccessToken YYYYYYYYYYYYYY --secret
    ```

Remember to pass `--secret` when setting `azuredevops:personalAccessToken` so that it is properly encrypted. A full set of configuration parameters
can be found listed on the [Project README](https://github.com/pulumi/pulumi-azuredevops/blob/master/README.md).
