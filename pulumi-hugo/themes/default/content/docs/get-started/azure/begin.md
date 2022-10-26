---
title: Before You Begin | Azure
h1: Before You Begin
linktitle: Before You Begin
meta_desc: This page provides an overview on how to get started with Pulumi when starting an Azure project.
weight: 2
menu:
  getstarted:
    parent: azure
    identifier: azure-begin

aliases: [
  "/docs/quickstart/azure/begin/",
  "/docs/quickstart/azure/install-pulumi/",
  "/docs/quickstart/azure/install-language-runtime/",
  "/docs/quickstart/azure/configure/",
  "/docs/get-started/azure/install-pulumi/",
  "/docs/get-started/azure/install-language-runtime/",
  "/docs/get-started/azure/configure/"
]
---

Before you get started using Pulumi, let's run through a few quick steps to ensure your environment is set up correctly.

### Install Pulumi

{{< install-pulumi >}}
{{% notes "info" %}}
All Windows examples in this tutorial assume you are running in PowerShell.
{{% /notes %}}
{{< /install-pulumi >}}

Next, install the required language runtime, if you have not already.

### Install Language Runtime

#### Choose Your Language

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}
{{< install-node >}}
{{% /choosable %}}

{{% choosable language python %}}
{{< install-python >}}
{{% /choosable %}}

{{% choosable language go %}}
{{< install-go >}}
{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}
{{< install-dotnet >}}
{{% /choosable %}}

{{% choosable language java %}}
{{< install-java >}}
{{% /choosable %}}

{{% choosable language yaml %}}
{{< install-yaml >}}
{{% /choosable %}}

Finally, configure Pulumi with Microsoft Azure.

### Configure Pulumi to access your Microsoft Azure account

Pulumi requires cloud credentials to manage and provision resources. Pulumi can authenticate to Azure using a user account or service principal that has **Programmatic access** with rights to deploy and manage your Azure resources.

{{% notes type="info" %}}
Pulumi relies on the Azure SDK to authenticate requests from your computer to Azure. Your credentials are never sent to pulumi.com.
{{% /notes %}}

In this guide, you will need a user account with permissions to create and populate Blob storage containers and provide anonymous access to a Blob file.

When developing locally, we recommend that you install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) and then authorize access with a user account.

```bash
az login
```

After successfully logging in, you are ready to go.

{{% notes type="info" %}}
The Azure CLI, and thus Pulumi, will use the default subscription for the account. You can change the active subscription with the [`az account set`](https://docs.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest#az_account_set) command.
{{% /notes %}}

For additional information on authenticating with Azure, or to login with a service principal, see [Azure Setup](/registry/packages/azure-native/installation-configuration/).

Next, you'll create a new Pulumi project.

{{< get-started-stepper >}}
