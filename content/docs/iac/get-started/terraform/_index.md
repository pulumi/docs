---
title: Pulumi for Terraform Users
title_tag: Pulumi for Terraform Users
h1: Pulumi for Terraform Users
meta_desc: A comprehensive guide for Terraform users to learn Pulumi through coexistence patterns and integration strategies.
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
This guide is for existing Terraform users to understand how Pulumi works and how it can integrate into your existing Terraform workflows.

This step-by-step tutorial focuses on coexistence patterns that let you leverage Pulumi's powerful features while maintaining your existing investments into Terraform.

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
* Docker installed locally (for containerization examples)
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

{{< get-started-stepper >}}
