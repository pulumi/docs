---
title: Azure Setup
meta_desc: This page provides an overview of how to setup and configure credentials
           for the Pulumi Azure Provider.
aliases: ["/docs/reference/clouds/azure/setup/"]
---

The [Pulumi Azure provider]({{< relref "./" >}}) uses the Azure SDK to manage and provision resources.

> Pulumi relies on the Azure SDK to authenticate requests from your computer to Azure. Your credentials are never sent
> to pulumi.com.

We recommend using the [Azure CLI 2.0](https://github.com/Azure/azure-cli), instead of the legacy
[Azure xPlat CLI](https://github.com/Azure/azure-xplat-cli).  We support both, but we recommend upgrading.
The below instructions assume that you are using the Azure CLI 2.0.

## Credentials

Pulumi can authenticate to Azure using a Service Principal or the Azure CLI.

If you're running the Pulumi CLI locally, in a developer scenario, we recommend using the Azure CLI.  For team
environments, particularly in CI, a Service Principal is recommended.

> **Note:** Authenticating using the CLI will not work for Service Principal logins (e.g.,
> `az login --service-principal`).  For such cases, authenticate using the Service Principal method instead.

## CLI Authentication

Simply login to the Azure CLI and Pulumi will automatically use your credentials:

```bash
$ az login
To sign in, use a web browser to open the page https://aka.ms/devicelogin and enter the code XXXFAKEXXX to authenticate.
```

Do as instructed to login.  After completed, `az login` will return and you are ready to go.

For most cases `az login` should suffice, but in certain scenarios such as
working with AKS you may hit issues with Bearer tokens not being refreshed
during an operation. To work around this, login using the device code flag:

```bash
$ az login --use-device-code
```

> **Note:** If you're using Government, China, or German Clouds, you'll need to configure the Azure CLI to work
> with that cloud.  Do so by running `az cloud set --name <Cloud>`, where `<Cloud>` is one of `AzureUSGovernment`,
> `AzureChinaCloud`, or `AzureGermanCloud`.

The Azure CLI, and thus Pulumi, will use the Default Subscription by default, however it is possible to override the
subscription, by simply setting your subscription ID to the `id` output from `az account list`'s output:

```bash
$ az account list
```

Pick out the `<id>` from the list and run:

```bash
$ az account set --subscription=<id>
```

## Service Principal Authentication

A Service Principal is an application in Azure Active Directory with three authorization tokens: a client ID, a client
secret, and a tenant ID.  (These are often simply called `appId`, `password`, and `tenant`, respectively.)  Using a
Service Principal is the recommended way to connect Pulumi to Azure in a team or CI setting.

### Configuring Authorization Tokens

Once obtained, there are two ways to communicate your authorization tokens to Pulumi:

1. Set the environment variables `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, `ARM_TENANT_ID`, and `ARM_SUBSCRIPTION_ID` respectively

2. Set them using configuration

    ```bash
    $ pulumi config set azure:clientId <clientID>
    $ pulumi config set azure:clientSecret <clientSecret> --secret
    $ pulumi config set azure:tenantId <tenantID>
    $ pulumi config set azure:subscriptionId <subscriptionId>
    ```

### Creating a Service Principal

To use a Service Principal, you must first create one.  This can be done using the Azure CLI, the Azure Cloud Shell, or the Azure Portal.
Please refer to the Azure documentation for detailed instructions:

* [Using the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest)
* [Using the Azure Cloud Shell](https://shell.azure.com/)
* [Using the Azure Portal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal?view=azure-cli-latest)

After creating a Service Principal, you will obtain three important tokens, mapping to the three shown earlier:

* `appId` is the client ID
* `password` is the client secret
* `tenant` is the tenant ID

For example, a common Service Principal as displayed by the Azure CLI looks something like this:

```json
{
  "appId": "WWWWWWWW-WWWW-WWWW-WWWW-WWWWWWWWWWWW",
  "displayName": "ServicePrincipalName",
  "name": "http://ServicePrincipalName",
  "password": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  "tenant": "YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY"
}
```

You also need to obtain a Subscription ID. To retrieve your current Subscription ID, you can use:

```bash
$ az account show --query id -o tsv
```

To list all available subscriptions, you can use:

```bash
$ az account list --query '[].{subscriptionName:name,subscriptionId:id}' -o tsv
```

The environment variables would then be set as such:

```bash
$ export ARM_CLIENT_ID="WWWWWWWW-WWWW-WWWW-WWWW-WWWWWWWWWWWW"
$ export ARM_CLIENT_SECRET="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
$ export ARM_TENANT_ID="YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY"
$ export ARM_SUBSCRIPTION_ID="ZZZZZZZZ-ZZZZ-ZZZZ-ZZZZ-ZZZZZZZZZZZZ"
```

Or configuration variables, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

```bash
$ pulumi config set azure:clientId "WWWWWWWW-WWWW-WWWW-WWWW-WWWWWWWWWWWW"
$ pulumi config set azure:clientSecret "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" --secret
$ pulumi config set azure:tenantId "YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY"
$ pulumi config set azure:subscriptionId "ZZZZZZZZ-ZZZZ-ZZZZ-ZZZZ-ZZZZZZZZZZZZ"
```

Remember to pass `--secret` when setting `clientSecret` so that it is properly encrypted.
