---
title: Before you begin | Kubernetes
h1: Before you begin
linktitle: Before you begin
meta_desc: This page provides an overview on how to get started with Pulumi when starting an Kubernetes project.
weight: 10000
block_external_search_index: true
exclude_from_pulumi_search_index: true

aliases: ["/docs/quickstart/kubernetes/begin/"]
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

Next, we'll configure Kubernetes.

### Configure Kubernetes

<a href="{{< relref "/docs/intro/cloud-providers/kubernetes/setup" >}}" target="_blank">Configure Kubernetes</a> so the Pulumi CLI can connect to a Kubernetes cluster. If you have previously configured the <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">kubectl CLI</a>, `kubectl`, Pulumi will respect and use your configuration settings.

Next, we'll create a new project.

<a data-track="previous-step" class="btn" href="/docs/get-started/kubernetes/">&lt; PREVIOUS STEP</a>
<a data-track="next-step" class="btn" href="/docs/get-started/kubernetes/create-project/">CREATE A NEW PROJECT &gt;</a>
