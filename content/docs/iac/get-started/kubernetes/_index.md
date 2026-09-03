---
title_tag: Get started with Pulumi and Kubernetes
meta_desc: Deploy an NGINX web server to Kubernetes with Pulumi in TypeScript, Python, Go, C#, Java, YAML, or HCL. Works with any cluster, including a local one.
title: Kubernetes
h1: Get Started with Pulumi and Kubernetes
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
    - /docs/iac/get-started/kubernetes/deploy-changes/
    - /docs/iac/get-started/kubernetes/review-project/
---

**Infrastructure as code (IaC)** lets you deploy, change, and manage infrastructure safely, consistently,
and repeatably using code rather than a graphical user interface.

Complete this step-by-step tutorial to deploy an [NGINX](https://www.nginx.com/) web server on Kubernetes using IaC.

## Before you begin

You need access to a Kubernetes cluster (local or cloud-based) and kubectl installed and configured.

Don't have a cluster yet? Spin one up locally with [kind](https://kind.sigs.k8s.io/), [minikube](https://minikube.sigs.k8s.io/docs/start/), or Docker Desktop's built-in Kubernetes, or provision a managed cluster on AWS, Azure, or Google Cloud with one of Pulumi's [Kubernetes cluster templates](/templates/kubernetes/).

Choose your language and ensure you've performed any prerequisites:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" / >}}

{{% choosable language "typescript" %}}

* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> and <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installed locally

{{% /choosable %}}

{{% choosable language "python" %}}

* <a href="https://www.python.org/downloads/" target="_blank">Python</a> and <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> or <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installed locally

{{% /choosable %}}

{{% choosable language "go" %}}

* <a href="https://go.dev/doc/install" target="_blank">Go</a> installed locally

{{% /choosable %}}

{{% choosable language "csharp" %}}

* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installed locally

{{% /choosable %}}

{{% choosable language "java" %}}

* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> and <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installed locally

{{% /choosable %}}

{{% choosable language "yaml" %}}

* A text editor

{{% /choosable %}}

{{% choosable language "hcl" %}}

* A text editor
* The [Pulumi CLI](/docs/install/) v3.256.0 or later; [Pulumi HCL](/docs/iac/languages-sdks/hcl/) needs no separate language runtime

{{% /choosable %}}

{{< get-started-stepper >}}
