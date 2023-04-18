---
title: Before You Begin | AWS
h1: Before You Begin
linktitle: Before You Begin
meta_desc: This page provides an overview on how to get started with Pulumi when starting an AWS project.
weight: 2
menu:
  getstarted:
    parent: aws
    identifier: aws-begin

aliases: [
  "/docs/quickstart/aws/begin/",
  "/docs/quickstart/aws/install-pulumi/",
  "/docs/quickstart/aws/install-language-runtime/",
  "/docs/quickstart/aws/configure/",
  "/docs/get-started/aws/install-pulumi/",
  "/docs/get-started/aws/install-language-runtime/",
  "/docs/get-started/aws/configure/"
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

{{% choosable language "java" %}}
{{< install-java >}}
{{% /choosable %}}

{{% choosable language "yaml" %}}
{{< install-yaml >}}
{{% /choosable %}}

### Configure Pulumi to access your AWS account

Pulumi requires cloud credentials to manage and provision resources. You must use an IAM user account that has **Programmatic access** with rights to deploy and manage resources handled through Pulumi.

If you have previously <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html" target="_blank">installed</a> and <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html" target="_blank">configured</a> the AWS CLI, Pulumi will respect and use your configuration settings.

If you do not have the AWS CLI installed or plan on using Pulumi from within a CI/CD pipeline, <a href="https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys" target="_blank">retrieve your access key ID and secret access key</a> and then set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables on your workstation.

{{< chooser os "linux,macos,windows" >}}
{{% choosable os linux %}}

```bash
$ export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
$ export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```

{{% /choosable %}}

{{% choosable os macos %}}

```bash
$ export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
$ export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:AWS_ACCESS_KEY_ID = "<YOUR_ACCESS_KEY_ID>"
> $env:AWS_SECRET_ACCESS_KEY = "<YOUR_SECRET_ACCESS_KEY>"
```

{{% /choosable %}}
{{< /chooser >}}

For additional information on setting and using AWS credentials, see [AWS Setup](/registry/packages/aws/installation-configuration/).

Next, you'll create a new Pulumi project.

{{< get-started-stepper >}}
