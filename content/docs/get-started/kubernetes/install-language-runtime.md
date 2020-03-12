---
title: Install Language Runtime | Kubernetes
h1: Install Language Runtime
linktitle: Install Language Runtime
meta_desc: This page provides an overview of how to install the different languages supported
           by Pulumi when starting a Kubernetes project.
weight: 3
no_on_this_page: true
menu:
  getstarted:
    parent: kubernetes
    identifier: kubernetes-install-language-runtime

aliases: ["/docs/quickstart/kubernetes/install-language-runtime/"]
---

## Choose Your Language

{{< chooser language "javascript,typescript,python,csharp" / >}}

{{% choosable language "javascript,typescript" %}}
{{< install-node >}}
{{% /choosable %}}

{{% choosable language python %}}
{{< install-python >}}
{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}
{{< install-dotnet >}}
{{% /choosable %}}

Next, we'll configure Kubernetes.

{{< get-started-stepper >}}
