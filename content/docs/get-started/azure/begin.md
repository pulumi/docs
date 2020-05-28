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

Before we get started using Pulumi, let's run through a few quick steps to ensure our environment is setup correctly.

### Install Pulumi

{{< install-pulumi >}}

Next, we'll install the required language runtime.

### Install Language Runtime

#### Choose Your Language

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language "javascript,typescript" %}}
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

Next, we'll configure Azure.

### Configure Azure

<a href="{{< relref "/docs/intro/cloud-providers/azure/setup" >}}" target="_blank">Configure Azure</a> so the Pulumi CLI can connect to Azure. If you have previously configured the <a href="https://docs.microsoft.com/en-us/cli/azure/" target="_blank">Azure CLI</a>, `az`, Pulumi will respect and use your configuration settings.

Next, we'll create a new project.

{{< get-started-stepper >}}
