---
title: Before You Begin | GCP
h1: Before You Begin
linktitle: Before You Begin
meta_desc: This page provides an overview on how to get started with Pulumi when starting an Google Cloud project.
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

Before you get started using Pulumi, let's run through a few quick steps to ensure your environment is setup correctly.

### Install Pulumi

{{< install-pulumi >}}
{{% notes "info" %}}
All Windows examples in this tutorial assume you are running in PowerShell.
{{% /notes %}}
{{< /install-pulumi >}}

Next, install the required language runtime, if you have not already.

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

Finally, configure Pulumi with Google Cloud.

### Configure Pulumi to access your Google Cloud account

Pulumi requires cloud credentials to manage and provision resources. You must use an IAM user or service account that has **Programmatic access** with rights to deploy and manage resources handled through Pulumi. 

In this guide, you will need an IAM user account with permissions that can create and populate a Cloud Storage bucket, such as those in the predefined Storage Admin (`roles/storage.admin`) or the Storage Legacy Bucket Owner (`roles/storage.legacyBucketOwner`) roles.

When developing locally, we recommend that you install the [Google Cloud SDK](https://cloud.google.com/sdk/install) and login with the `gcloud` CLI tool as shown below.

{{< chooser os "linux,macos,windows" >}}
{{% choosable os linux %}}

```bash
$ gcloud auth login
$ gcloud config set project <YOUR_GCP_PROJECT_HERE>
$ gcloud auth application-default login
```

{{% /choosable %}}
{{% choosable os macos %}}

```bash
$ gcloud auth login
$ gcloud config set project <YOUR_GCP_PROJECT_HERE>
$ gcloud auth application-default login
```

{{% /choosable %}}
{{% choosable os windows %}}

```bat
> gcloud auth login
> gcloud config set project <YOUR_GCP_PROJECT_HERE>
> gcloud auth application-default login
```

{{% /choosable %}}
{{< /chooser >}}

For additional information on how to setup Pulumi to work with Google Cloud, see [Google Cloud Setup]({{< relref "/docs/intro/cloud-providers/gcp/setup" >}}).

Next, you'll create a new project.

{{< get-started-stepper >}}
