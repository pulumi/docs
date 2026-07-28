---
title_tag: Configure access | Azure
title: Configure access to Azure
linkTitle: Configure access
h1: "Configure access to Azure"
meta_desc: This page provides an overview on how to get started with Pulumi when starting an Azure project.
weight: 3
menu:
    iac:
        name: Configure access
        parent: azure-get-started
        weight: 3
        identifier: azure-get-started.configure
aliases:
    - /docs/quickstart/azure/configure/
    - /docs/clouds/azure/get-started/configure/
---

The Pulumi CLI needs access to your Azure account to manage cloud resources. For this tutorial, you'll need an Azure account with rights to deploy and manage resources such as storage accounts and blob containers.

If you've previously <a href="https://learn.microsoft.com/en-us/cli/azure/install-azure-cli" target="_blank">installed</a> and <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli" target="_blank">configured</a> the Azure CLI, Pulumi will respect and use those settings, which you can test with the CLI directly:

```bash
$ az account show

{
  "environmentName": "AzureCloud",
  "id": "0282...",
  "name": "My Subscription",
  "state": "Enabled",
  "tenantId": "7061...",
  "user": { "name": "you@example.com", "type": "user" }
}
```

If your subscription details are printed, you're configured correctly.

The Azure CLI is convenient, but not required. You can also configure Pulumi with environment variables — for example, by <a href="https://learn.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli" target="_blank">creating a service principal</a>:

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

For additional configuration options, see [Azure Setup](/registry/packages/azure-native/installation-configuration/).

{{< get-started-stepper >}}
