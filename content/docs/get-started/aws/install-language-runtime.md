---
title: Install Language Runtime | AWS
h1: Install Language Runtime
linktitle: Install Language Runtime
meta_desc: This page provides an overview of how to install the different languages supported
           by Pulumi when starting an AWS project.
weight: 3
no_on_this_page: true
menu:
  getstarted:
    parent: aws
    identifier: aws-install-language-runtime

aliases: ["/docs/quickstart/aws/install-language-runtime/"]
---

## Choose Your Language

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

{{< get-started-stepper >}}
