---
title_tag: Configure access | Azure
title: Configure access
h1: "Get started with Pulumi and Azure"
meta_desc: This page provides an overview on how to get started with Pulumi when starting an Azure project.
weight: 3
menu:
    iac:
        name: Configure access
        parent: azure-get-started
        weight: 3

aliases:
    - /docs/quickstart/azure/configure/
    - /docs/clouds/azure/get-started/configure/
---

## Configure access to Azure

Pulumi's CLI needs access to your Azure account to manage cloud resources.

If you've already <a href="https://learn.microsoft.com/en-us/cli/azure/install-azure-cli" target="_blank">installed</a> and <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli" target="_blank">configured</a> the Azure CLI, Pulumi will respect and use your configuration settings.

You must use an Azure account that has rights to deploy and manage resources, such as storage accounts and blob containers.

### Testing access

To test that your Azure access is configured properly, run:

{{% choosable os "linux,macos" %}}

```bash
$ az account show
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> az account show
```

{{% /choosable %}}

If your Azure subscription details are printed, you are good to go. If not, read on:

```json
{
  "environmentName": "AzureCloud",
  "id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "isDefault": true,
  "name": "My Subscription",
  "state": "Enabled",
  "tenantId": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "user": {
    "name": "user@example.com",
    "type": "user"
  }
}
```

### Alternative approaches

If you don't have the Azure CLI installed, or you plan on using Pulumi in a CI/CD pipeline, you can <a href="https://learn.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli" target="_blank">create a service principal</a> and set the following environment variables on your workstation:

{{% choosable os "linux,macos" %}}

```bash
$ export ARM_CLIENT_ID="<YOUR_CLIENT_ID>"
$ export ARM_CLIENT_SECRET="<YOUR_CLIENT_SECRET>"
$ export ARM_TENANT_ID="<YOUR_TENANT_ID>"
$ export ARM_SUBSCRIPTION_ID="<YOUR_SUBSCRIPTION_ID>"
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:ARM_CLIENT_ID = "<YOUR_CLIENT_ID>"
> $env:ARM_CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"
> $env:ARM_TENANT_ID = "<YOUR_TENANT_ID>"
> $env:ARM_SUBSCRIPTION_ID = "<YOUR_SUBSCRIPTION_ID>"
```

{{% /choosable %}}

{{% notes type="info" %}}
Consider using [Pulumi ESC's Azure login support](/docs/esc/integrations/dynamic-login-credentials/azure-login) for dynamic,
short-lived Azure credentials via OpenID Connect (OIDC) instead of long-lived static credentials. This is a security best practice.
{{% /notes %}}

For detailed information on Pulumi's use of Azure credentials, see [Azure Setup](/registry/packages/azure-native/installation-configuration/).

{{< get-started-stepper >}}
