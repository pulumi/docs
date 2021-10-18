---
title: Before You Begin | Kubernetes
h1: Before You Begin
linktitle: Before You Begin
meta_desc: This page provides an overview on how to get started with Pulumi when starting an Kubernetes project.
weight: 2
menu:
  getstarted:
    parent: kubernetes
    identifier: kubernetes-begin

aliases: [
  "/docs/quickstart/kubernetes/begin/",
  "/docs/quickstart/kubernetes/install-pulumi/",
  "/docs/quickstart/kubernetes/install-language-runtime/",
  "/docs/quickstart/kubernetes/configure/",
  "/docs/get-started/kubernetes/install-pulumi/",
  "/docs/get-started/kubernetes/install-language-runtime/",
  "/docs/get-started/kubernetes/configure/"
]
---

Before we get started using Pulumi, let's run through a few quick steps to ensure our environment is setup correctly.

### Install Pulumi

{{< install-pulumi >}}
{{% notes "info" %}}
All Windows examples in this tutorial assume you are running in PowerShell.
{{% /notes %}}
{{< /install-pulumi >}}

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

Next, we'll configure Kubernetes.

### Configure Kubernetes

<a href="{{< relref "/registry/packages/kubernetes/installation-configuration" >}}" target="_blank">Configure Kubernetes</a> so the Pulumi CLI can connect to a Kubernetes cluster. If you have previously configured the <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">kubectl CLI</a>, `kubectl`, Pulumi will respect and use your configuration settings.

Next, we'll create a new Pulumi project.

{{< get-started-stepper >}}
