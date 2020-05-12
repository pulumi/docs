---
title: Before you begin | Azure
h1: Before you begin
linktitle: Before you begin
meta_desc: This page provides an overview on how to get started with Pulumi when starting an Azure project.
weight: 10000

aliases: ["/docs/quickstart/azure/begin/"]
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

<a data-track="previous-step" class="btn" href="/docs/get-started/azure/">&lt; PREVIOUS STEP</a>
<a data-track="next-step" class="btn" href="/docs/get-started/azure/create-project/">CREATE A NEW PROJECT &gt;</a>