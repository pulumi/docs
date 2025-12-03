---
title_tag: Get Started with Google Cloud
meta_desc: This page provides an overview and guide on how to get started with Google Cloud.
title: Google Cloud
h1: Get started with Pulumi & Google Cloud
menu:
    iac:
        name: Google Cloud
        identifier: gcp-get-started
        parent: iac-get-started
        weight: 3
    clouds:
        parent: google-cloud
        identifier: google-cloud-get-started
        weight: 3
aliases:
    - /docs/get-started/gcp/
    - /docs/quickstart/gcp/
    - /docs/clouds/get-started/gcp
    - /docs/clouds/gcp/get-started/
---

{{< cloud-intro "Google Cloud" >}}

**Infrastructure as code (IaC)** lets you deploy, change, and manage infrastructure safely, consistently,
and repeatably using code rather than a graphical user interface.

Complete this step-by-step tutorial to deploy a Google Cloud Storage-based website using IaC.

## Before you begin

Make sure you have the <a href="https://cloud.google.com/sdk/docs/install" target="_blank">gcloud CLI</a> installed and signed in to the account and project you plan to use (for example, `gcloud auth login` and `gcloud config set project <your-project-id>`). Then choose your language and ensure you've performed any prerequisites:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* <a href="https://nodejs.org/en/download" target=_blank>Node.js</a> and <a href="https://www.npmjs.com/package/npm" target=_blank>npm</a> installed locally

{{% /choosable %}}

{{% choosable language "python" %}}

* <a href="https://www.python.org/downloads/" target=_blank>Python</a> and <a href="https://pip.pypa.io/en/stable/installation/">pip</a>, <a href="https://python-poetry.org/docs/" target=_blank>Poetry</a> or <a href="https://docs.astral.sh/uv/getting-started/installation/" target=_blank>uv</a> installed locally

{{% /choosable %}}

{{% choosable language "go" %}}

* <a href="https://go.dev/doc/install" target=_blank>Go</a> installed locally

{{% /choosable %}}

{{% choosable language "csharp" %}}

* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target=_blank>.NET</a> installed locally

{{% /choosable %}}

{{% choosable language "java" %}}

* <a href="https://www.oracle.com/java/technologies/downloads/" target=_blank>Java 11+</a> and <a href="https://maven.apache.org/install.html" target=_blank>Maven 3.6.1+</a> installed locally

{{% /choosable %}}

{{% choosable language "yaml" %}}

* A text editor

{{% /choosable %}}

{{< get-started-stepper >}}
