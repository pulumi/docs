---
title: AWS
title_tag: Get started with Pulumi and AWS
h1: Get started with Pulumi and AWS
meta_desc: This page provides an overview and guide on how to get started with AWS.
menu:
    iac:
        name: AWS
        parent: iac-get-started
        weight: 1
        identifier: aws-get-started
    clouds:
        parent: aws
        identifier: aws-get-started
        weight: 1

aliases:
    - /docs/quickstart/aws/
    - /docs/get-started/aws/
    - /docs/aws/
    - /docs/clouds/aws/get-started/
---

**Infrastructure as code (IaC)** lets you deploy, change, and manage infrastructure safely, consistently,
and repeatably using code rather than a graphical user interface.

Complete this step-by-step tutorial to deploy an AWS S3 bucket-based website using IaC.

## Before you begin

First, choose your language and ensure you've performed any prerequisites:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript,javascript" %}}

* An <a href="https://aws.amazon.com/free" target=_blank>AWS account</a>
* <a href="https://nodejs.org/en/download" target=_blank>Node.js</a> and <a href="https://www.npmjs.com/package/npm" target=_blank>npm</a> installed locally

{{% /choosable %}}

{{% choosable language "python" %}}

* An <a href="https://aws.amazon.com/free" target="_blank">AWS account</a>
* <a href="https://www.python.org/downloads/" target=_blank>Python</a> and <a href="https://pip.pypa.io/en/stable/installation/">pip</a>, <a href="https://python-poetry.org/docs/" target=_blank>Poetry</a> or <a href="https://docs.astral.sh/uv/getting-started/installation/" target=_blank>uv</a> installed locally

{{% /choosable %}}

{{% choosable language "go" %}}

* An <a href="https://aws.amazon.com/free" target="_blank">AWS account</a>
* <a href="https://go.dev/doc/install" target=_blank>Go</a> installed locally

{{% /choosable %}}

{{% choosable language "csharp" %}}

* An <a href="https://aws.amazon.com/free" target="_blank">AWS account</a>
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target=_blank>.NET</a> installed locally

{{% /choosable %}}

{{% choosable language "java" %}}

* An <a href="https://aws.amazon.com/free" target="_blank">AWS account</a>
* <a href="https://www.oracle.com/java/technologies/downloads/" target=_blank>Java 11+</a> and <a href="https://maven.apache.org/install.html" target=_blank>Maven 3.6.1+</a> installed locally

{{% /choosable %}}

{{% choosable language "yaml" %}}

* <a href="https://aws.amazon.com/free" target="_blank">An AWS account</a>

{{% /choosable %}}

{{< get-started-stepper >}}
