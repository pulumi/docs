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

The [Pulumi Google Cloud Platform Provider]({{< relref "/docs/intro/cloud-providers/gcp" >}}) needs to be configured with Google credentials
before it can be used to create resources.

When developing locally, we recommend that you use `gcloud login` to configure your account credentials. First, install the [Google Cloud SDK](https://cloud.google.com/sdk/install), which includes the `gcloud` command line tool. Then, execute the following:

```bash
$ gcloud auth login
$ gcloud config set project <YOUR_GCP_PROJECT_HERE>
$ gcloud auth application-default login
```

For more detailed setup information, please refer to our <a href="{{< relref "/docs/intro/cloud-providers/gcp/setup" >}}" target="_blank">GCP provider setup guide</a>

Next, we'll create a new project.

{{< get-started-stepper >}}
