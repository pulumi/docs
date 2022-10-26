---
title: Before You Begin | GCP
h1: Before You Begin
linktitle: Before You Begin
meta_desc: This page provides an overview on how to get started with Pulumi and Google Cloud.
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

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

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

{{% choosable language java %}}
{{< install-java >}}
{{% /choosable %}}

{{% choosable language yaml %}}
{{< install-yaml >}}
{{% /choosable %}}

Finally, configure Pulumi with Google Cloud.

### Configure Pulumi to access your Google Cloud account

Pulumi requires cloud credentials to manage and provision resources. You must use an IAM user or service account that has **Programmatic access** with rights to deploy and manage your Google Cloud resources.

In this guide, you will need an IAM user account with permissions that can create and populate a Cloud Storage bucket, such as those in the predefined Storage Admin (`roles/storage.admin`) or the Storage Legacy Bucket Owner (`roles/storage.legacyBucketOwner`) roles.

{{% configure-gcp %}}

For additional information on setting and using Google Cloud credentials, see [Google Cloud Setup](/registry/packages/gcp/installation-configuration/).

Next, you'll create a new Pulumi project.

{{< get-started-stepper >}}
