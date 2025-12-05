---
title_tag: Get Started with Kubernetes
meta_desc: This page provides an overview and guide on how to get started with Kubernetes.
title: Kubernetes
h1: Get Started with Kubernetes
menu:
    iac:
        name: Kubernetes
        identifier: kubernetes-get-started
        parent: iac-get-started
        weight: 4
    clouds:
        identifier: kubernetes-get-started
        parent: kube
        weight: 4
aliases:
    - /docs/get-started/kubernetes/
    - /docs/quickstart/kubernetes/
    - /docs/clouds/kubernetes/get-started/
---

**Infrastructure as code (IaC)** lets you deploy, change, and manage infrastructure safely, consistently,
and repeatably using code rather than a graphical user interface.

Complete this step-by-step tutorial to deploy an [NGINX](https://www.nginx.com/) web server on Kubernetes using IaC.

## Before you begin

You need access to a Kubernetes cluster (local or cloud-based) and kubectl installed and configured. Choose your language and ensure you've performed any prerequisites:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Access to a Kubernetes cluster (local or cloud-based)
* kubectl installed and configured
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> and <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installed locally

{{% /choosable %}}

{{% choosable language "python" %}}

* Access to a Kubernetes cluster (local or cloud-based)
* kubectl installed and configured
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> and <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> or <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installed locally

{{% /choosable %}}

{{% choosable language "go" %}}

* Access to a Kubernetes cluster (local or cloud-based)
* kubectl installed and configured
* <a href="https://go.dev/doc/install" target="_blank">Go</a> installed locally

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Access to a Kubernetes cluster (local or cloud-based)
* kubectl installed and configured
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installed locally

{{% /choosable %}}

{{% choosable language "java" %}}

* Access to a Kubernetes cluster (local or cloud-based)
* kubectl installed and configured
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> and <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installed locally

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Access to a Kubernetes cluster (local or cloud-based)
* kubectl installed and configured
* A text editor

{{% /choosable %}}

Before you begin, watch this overview of how to deploy Kubernetes infrastructure with Pulumi:

<div class="rounded-md shadow border border-gray-300 w-3/4 mx-auto my-4" style="position: relative; padding-bottom: 40.25%; height: 0; overflow: hidden;">
    <iframe
        src="//www.youtube.com/embed/2P8JLgAc5QI?rel=0"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
        allowfullscreen=""
        title="Getting Started with Kubernetes and Pulumi: Deploy Amazon EKS in 5 minutes">
    </iframe>
</div>

{{< get-started-stepper >}}
