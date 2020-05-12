---
title: Before you begin | GCP
h1: Before you begin
linktitle: Before you begin
meta_desc: This page provides an overview on how to get started with Pulumi when starting an GCP project.
weight: 10000

aliases: ["/docs/quickstart/gcp/begin/"]
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

Next, we'll configure GCP.

### Configure GCP

<a href="{{< relref "/docs/intro/cloud-providers/gcp/setup" >}}" target="_blank">Configure Google Cloud</a> so the Pulumi CLI can connect to Google Cloud. If you have previously configured the <a href="https://cloud.google.com/sdk/gcloud/" target="_blank">Google Cloud CLI</a>, `gcloud`, Pulumi will respect and use your configuration settings.

Next, we'll create a new project.

<a data-track="previous-step" class="btn" href="/docs/get-started/gcp/">&lt; PREVIOUS STEP</a>
<a data-track="next-step" class="btn" href="/docs/get-started/gcp/create-project/">CREATE A NEW PROJECT &gt;</a>