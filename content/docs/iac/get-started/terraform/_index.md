---
title: Pulumi for Terraform Users
title_tag: Get started with Pulumi for Terraform Users
h1: Get started with Pulumi for Terraform Users
meta_desc: This page provides a comprehensive guide for Terraform users to learn Pulumi through coexistence patterns and integration strategies.
menu:
    iac:
        name: Terraform Users
        parent: iac-get-started
        weight: 5
        identifier: terraform-get-started

aliases:
    - /docs/iac/get-started/terraform/
---

**Use Pulumi alongside your existing Terraform infrastructure** rather than replacing it entirely.
This guide focuses on coexistence patterns that let you leverage Pulumi's powerful features while maintaining your existing Terraform workflows.

Complete this step-by-step tutorial to learn how to integrate Pulumi with your Terraform infrastructure using a containerized web application example.

## What you'll learn

Through progressive examples, you'll discover how to:

* Reference existing Terraform state files from Pulumi
* Use any Terraform provider in Pulumi programs
* Import and use Terraform modules directly
* Convert HCL code to Pulumi when beneficial
* Orchestrate both Terraform and Pulumi deployments together

## Prerequisites

* Basic Terraform knowledge and existing Terraform infrastructure
* AWS account with appropriate permissions
* Docker installed locally for containerization examples
* Git for version control

## Time estimate

**30-45 minutes** to complete all sections

## Overview of examples

You'll build a containerized web application managed by Pulumi that integrates with ECS infrastructure managed by Terraform.
Starting with simple state referencing, you'll progressively add complexity while learning integration patterns that work in real-world scenarios.

The examples demonstrate:

1. **Coexistence**: Reading Terraform state from Pulumi
2. **Provider sharing**: Using Terraform providers in Pulumi
3. **Module reuse**: Leveraging existing Terraform modules
4. **Selective conversion**: Converting specific HCL when advantageous
5. **Orchestration**: Managing both tools in unified workflows

## Before you begin

Choose your preferred Pulumi language:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript,javascript" %}}

* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> and <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installed locally

{{% /choosable %}}

{{% choosable language "python" %}}

* <a href="https://www.python.org/downloads/" target="_blank">Python</a> and <a href="https://pip.pypa.io/en/stable/installation/">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> or <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installed locally

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

* No additional language runtime required

{{% /choosable %}}

{{< get-started-stepper >}}