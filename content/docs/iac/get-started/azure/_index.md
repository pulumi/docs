---
title: Azure
title_tag: Get started with Pulumi and Azure
h1: Get started with Pulumi and Azure
meta_desc: This page provides an overview and guide on how to get started with Azure.
menu:
    iac:
        name: Azure
        parent: iac-get-started
        identifier: azure-get-started
        weight: 2
    clouds:
        parent: azure
        identifier: azure-get-started
        weight: 2
aliases:
    - /docs/get-started/azure/
    - /docs/quickstart/azure/
    - /docs/clouds/azure/get-started/
---

**Infrastructure as code (IaC)** lets you deploy, change, and manage infrastructure safely, consistently,
and repeatably using code rather than a graphical user interface.

Complete this step-by-step tutorial to deploy an Azure Blob Storage-based website using IaC.

## Before you begin

First, choose your language and ensure you've performed any prerequisites:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* An <a href="https://azure.microsoft.com/free" target="_blank">Azure account</a>
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> and <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installed locally

{{% /choosable %}}

{{% choosable language "python" %}}

* An <a href="https://azure.microsoft.com/free" target="_blank">Azure account</a>
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> and <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> or <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installed locally

{{% /choosable %}}

{{% choosable language "go" %}}

* An <a href="https://azure.microsoft.com/free" target="_blank">Azure account</a>
* <a href="https://go.dev/doc/install" target="_blank">Go</a> installed locally

{{% /choosable %}}

{{% choosable language "csharp" %}}

* An <a href="https://azure.microsoft.com/free" target="_blank">Azure account</a>
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installed locally

{{% /choosable %}}

{{% choosable language "java" %}}

* An <a href="https://azure.microsoft.com/free" target="_blank">Azure account</a>
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> and <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installed locally

{{% /choosable %}}

{{% choosable language "yaml" %}}

* <a href="https://azure.microsoft.com/free" target="_blank">An Azure account</a>

{{% /choosable %}}

{{< get-started-stepper >}}
