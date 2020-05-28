---
title: Before You Begin | GCP
h1: Before You Begin
linktitle: Before You Begin
meta_desc: This page provides an overview on how to get started with Pulumi when starting an GCP project.
weight: 2
menu:
  getstarted:
    parent: gcp
    identifier: gcp-begin

aliases: [
  "/docs/quickstart/gcp/begin/",
  "/docs/quickstart/gcp/install-pulumi/",
  "/docs/quickstart/gcp/install-language-runtime/",
  "/docs/quickstart/gcp/configure/",
  "/docs/get-started/gcp/install-pulumi/",
  "/docs/get-started/gcp/install-language-runtime/",
  "/docs/get-started/gcp/configure/"
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

Next, we'll configure GCP.

### Configure GCP

<a href="{{< relref "/docs/intro/cloud-providers/gcp/setup" >}}" target="_blank">Configure Google Cloud</a> so the Pulumi CLI can connect to Google Cloud. If you have previously configured the <a href="https://cloud.google.com/sdk/gcloud/" target="_blank">Google Cloud CLI</a>, `gcloud`, Pulumi will respect and use your configuration settings.

Next, we'll create a new project.

{{< get-started-stepper >}}
