---
title: Pulumi for Terraform Users
title_tag: Pulumi for Terraform Users
h1: Pulumi for Terraform Users
meta_desc: A comprehensive guide for Terraform users to learn Pulumi through coexistence patterns and integration strategies.
menu:
    iac:
        name: Terraform Users
        parent: iac-get-started
        weight: 50
        identifier: terraform-get-started

aliases:
---

**Use Pulumi alongside your existing Terraform infrastructure** rather than replacing it entirely.
This step-by-step tutorial is for existing Terraform users and focuses on coexistence patterns that let you adopt Pulumi's features while keeping your existing investments in Terraform.

## What you'll learn

Each step below is a page in this guide, and the buttons at the bottom of every page walk you through them in order:

1. [Install and configure Pulumi](/docs/iac/get-started/terraform/begin/) alongside your existing Terraform setup
1. [First look](/docs/iac/get-started/terraform/first-look/): create the same resources with Terraform HCL and with a Pulumi program
1. **Coexistence**: [reference existing Terraform state files](/docs/iac/get-started/terraform/reference-state/) from Pulumi
1. **Module reuse**: [import and use Terraform modules directly](/docs/iac/get-started/terraform/terraform-modules/)
1. **Provider sharing**: [use any Terraform provider](/docs/iac/get-started/terraform/terraform-providers/) in Pulumi programs
1. **Selective conversion**: [convert specific HCL](/docs/iac/get-started/terraform/convert-hcl/) to Pulumi when beneficial
1. **Orchestration**: [manage both tools in unified workflows](/docs/iac/get-started/terraform/orchestrate/)
1. **State management**: [store Terraform state in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/)
1. **Remote execution**: [run Terraform plans and applies on Pulumi Cloud](/docs/iac/get-started/terraform/terraform-remote-execution/)

## Overview of examples

You'll build a containerized web application managed by Pulumi that integrates with ECS infrastructure managed by Terraform.
Starting with state referencing, you'll progressively add complexity while learning integration patterns that work in real-world scenarios.

## Prerequisites

* Basic Terraform knowledge and existing Terraform infrastructure
* AWS account with appropriate permissions
* Docker installed locally (for containerization examples)
* Git for version control

## Time estimate

**30-45 minutes** to complete all sections

{{< get-started-stepper >}}
