---
title: AzureDevOps Setup
meta_desc: This page provides an overview on how to configure credentials for the Pulumi AzureDevOps Provider.
---

The [Pulumi AzureDevOps provider]({{< relref "./" >}}) uses the AzureDevOps SDK to manage and provision resources.

> Pulumi relies on the AzureDevOps SDK to authenticate requests from your computer to AzureDevOps. Your credentials are never sent
> to pulumi.com.

The [Pulumi AzureDevOps Provider]({{< relref "./" >}}) needs to be configured with AzureDevOps credentials
before it can be used to create resources.

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
The default web browser has been opened at https://login.microsoftonline.com/common/oauth2/authorize. Please continue
the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow
with `az login --use-device-code`.
```

Do as instructed to login.  After completed, `az login` will return and you are ready to go.

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

1. Set the environment variables `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET` and `ARM_TENANT_ID` respectively

2. Set them using configuration

    ```bash
    $ pulumi config set azuread:clientId <clientID>
    $ pulumi config set azuread:clientSecret <clientSecret> --secret
    $ pulumi config set azuread:tenantId <tenantID>
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
```

Or configuration variables, if you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

```bash
$ pulumi config set azuread:clientId "WWWWWWWW-WWWW-WWWW-WWWW-WWWWWWWWWWWW"
$ pulumi config set azuread:clientSecret "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" --secret
$ pulumi config set azuread:tenantId "YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY"
```

Remember to pass `--secret` when setting `clientSecret` so that it is properly encrypted.
