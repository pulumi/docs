---
title: Before you begin | AWS
h1: Before you begin
linktitle: Before you begin
meta_desc: This page provides an overview on how to get started with Pulumi when starting an AWS project.
weight: 10000

aliases: ["/docs/quickstart/aws/begin/"]
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

Next, we'll configure AWS.

### Configure AWS

<a href="{{< relref "/docs/intro/cloud-providers/aws/setup" >}}" target="_blank">Configure AWS</a> so the Pulumi CLI can connect to AWS. If you have previously configured the <a href="https://aws.amazon.com/cli/" target="_blank">AWS CLI</a>, `aws`, Pulumi will respect and use your configuration settings.

If you have multiple AWS profiles set up, specify a different profile using one of the following ways:

* Set `AWS_PROFILE`as an <a href="{{< relref "/docs/intro/cloud-providers/aws/setup#environment-variables" >}}" target="_blank">environment variable</a>, or
* After creating your project in the next step, run `pulumi config set aws:profile <profilename>`. See <a href="{{< relref "/docs/intro/cloud-providers/aws#configuration" >}}" target="_blank">AWS Configuration</a> for more configuration options.

Next, we'll create a new project.

<a data-track="previous-step" class="btn" href="/docs/get-started/aws/">&lt; PREVIOUS STEP</a>
<a data-track="next-step" class="btn" href="/docs/get-started/aws/create-project/">CREATE A NEW PROJECT &gt;</a>
