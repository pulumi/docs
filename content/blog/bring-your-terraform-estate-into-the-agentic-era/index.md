---
title: "Bring Your Terraform Estate Into the Agentic Era"
date: 2026-08-04
draft: false
meta_desc: "Pulumi Cloud as a Terraform backend and HCL in Pulumi IaC are now GA, plus native Terraform module support — bring the IaC you already have."
feature_image: feature.png
authors:
    - daniel-perlovsky
tags:
    - infrastructure-as-code
    - terraform
    - hcl
    - pulumi-cloud
category: product
schema_type: auto
related_posts:
    - terraform-to-pulumi-cloud-hands-on
    - terraforms-data-model-on-pulumis-engine
    - compatibility-testing-pulumi-hcl

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Pulumi Cloud is now a GA backend for Terraform state, HCL just went GA as a native Pulumi language, and Terraform modules import without a rewrite.

        You don't have to rip out Terraform to build for the agentic era. Here's what shipped.
    linkedin: |
        Last December, Joe Duffy laid out Pulumi's vision to support all of your infrastructure as code, including Terraform and HCL. Today that vision ships.

        Pulumi Cloud is now a GA backend for Terraform state — remote plans and applies, manual approvals, RBAC, and Neo code reviews all work against your Terraform stacks. HCL is GA as a first-class Pulumi language, and Terraform modules now import natively into Pulumi programs.

        None of this requires rewriting what you already have. And if you're mid-transition, there's still a credit escape hatch, a free IaC modernization workshop, and an ROI calculation walkthrough with our team.

        Here's the full breakdown of what shipped today.
    bluesky: |
        Teams running Terraform don't have to rip it out to move into the agentic infrastructure era. Pulumi Cloud is now GA as a Terraform state backend, HCL is GA as a native Pulumi language, and Terraform modules import without changes.

        Here's what shipped today.
---

At Pulumi, we are building the platform for [agentic infrastructure](/what-is/what-is-agentic-infrastructure/). Pulumi Cloud provides the guardrails and enterprise readiness needed to safely move fast in this new era. While we are seeing extraordinary adoption — over 40% of our users now manage infrastructure using AI agents — we know many organizations are at different phases in their AI journey and have to balance building for the future with maintaining their existing infrastructure as code (IaC) solutions like Terraform.

Today, [we are launching](/releases/terraform-state-backend-modules-hcl/) three ways that Pulumi lets you avoid trading off building for the future against building for today. You don't have to rip out Terraform to enter the agentic era. Pulumi Cloud brings agentic infrastructure to the IaC estate you already have.

<!--more-->

## What we're shipping today

Last December, our CEO [Joe Duffy laid out his vision](/blog/all-iac-including-terraform-and-hcl/) to make Pulumi the platform for all of your infrastructure as code. The capabilities we are launching today make that promise a reality. Pulumi is now fully interoperable with Terraform and OpenTofu and enables organizations to build upon their existing IaC estate rather than starting from scratch as they work toward the agentic infrastructure future.

### Pulumi Cloud as a Terraform backend

We are excited to announce the general availability of [Pulumi Cloud as the backend to your Terraform state](/docs/iac/get-started/terraform/terraform-state-backend/), enabling organizations to seamlessly lift and shift their existing Terraform estates.

We recognize there is lots of infrastructure that works as is, and switching over to a new management paradigm may not always be possible. Pulumi Cloud support for the Terraform state backend lets organizations maintain their existing Terraform deployment patterns while also unlocking the power of Pulumi Cloud. The following common patterns for running Terraform are now supported:

- **Plans and applies run remotely by default** for new Terraform stacks, following the behavior of HCP Terraform and Terraform Enterprise. When you run a Terraform operation, it executes on a Pulumi-hosted runner rather than your local machine. You get full visibility into these operations both on your local CLI and in the Pulumi Cloud console.
- **Production deployments may be gated with manual approvals** before applying a Terraform plan.

With this release, stacks with Terraform state are first-class entities in Pulumi Cloud. They get access to all of the capabilities that organizations need to scale in this new AI-first era.

- **[Manage access to your Terraform stacks at scale](/docs/administration/access-identity/rbac/)** using tag-based access control, team role assignments, and user role assignments.
- [**Take advantage of Neo code reviews**](/docs/ai/neo/code-reviews/). On every pull request, leverage what Pulumi Cloud knows about your running infrastructure and get clear feedback on whether it's safe to merge changes to your Terraform and OpenTofu projects.
- [**Run preventive policies**](/docs/insights/policy/) after a Terraform plan to block non-compliant resources before deployment.
- **[Configure your Terraform deployments with Pulumi ESC](/docs/esc/)**, which is natively available to Pulumi Cloud-backed Terraform projects, to securely inject OIDC credentials at apply time and expose outputs to downstream stacks and services.

Learn more in [Using Pulumi Cloud as a Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/).

### Reuse your Terraform modules

Pulumi programs, regardless of language, now support [importing Terraform modules](/docs/iac/get-started/terraform/terraform-modules/) natively. Organizations can leverage their existing reusable artifacts as is, without having to make a single change. This enables organizations to focus on new infrastructure projects and lets them build those projects in the language of their choice, regardless of what their existing IaC estate is.

In addition, Pulumi Cloud's private registry can now host Terraform modules alongside Pulumi packages. This enables you to consolidate all of your IaC building blocks in a single source of truth rather than managing disparate solutions and making sure your teams know where to look. Terraform modules hosted in Pulumi Cloud provide maximum interoperability and can be used in both Pulumi and Terraform programs.

Learn more in [Using Terraform modules in Pulumi](/docs/iac/get-started/terraform/terraform-modules/).

### Build in HCL natively

[HashiCorp Configuration Language (HCL)](/docs/iac/languages-sdks/hcl/) is now generally available as a first-class language in Pulumi IaC. Like any other Pulumi language, it has full access to the entirety of the Pulumi ecosystem, including thousands of providers. Thanks to our Terraform bridge, if there's a Terraform provider out there, it just works. Best of all, HCL in Pulumi is 100% [OpenTofu](https://github.com/opentofu/opentofu) compatible with no syntactical differences.

We recognize there are many teams out there that prefer to work in HCL over general-purpose languages but want to leverage the modern Pulumi IaC engine, or want to be able to use the reusable components their partner teams rely on — regardless of whether those teams work in Terraform or Pulumi.

Learn more in the [HCL language reference](/docs/iac/languages-sdks/hcl/).

## You are still covered until your HashiCorp renewal

We stand by the promise we made last December, and the last thing we want is for you to pay for two IaC solutions. To set your team up for long-term success and ensure your transition to Pulumi is as smooth as possible, we are continuing to offer three things:

- **An escape hatch for your current contract.** We know paying for two IaC solutions at once is a non-starter, so we're letting you apply credits purchased from HashiCorp toward your Pulumi usage until your next renewal, avoiding double pay.
- **A free IaC modernization workshop.** Our professional services cloud architects host a free IaC modernization workshop to review where you're at with your IaC already and share best practices for adopting the Pulumi platform at scale, learned from working with world-class organizations like BMW and Supabase. You will leave this session trained up and equipped to succeed with the next phase of your IaC journey.
- **A return on investment (ROI) calculation.** We will show you how the move to Pulumi will not only be spend-neutral thanks to the escape hatch, but how much value and savings you should expect to see, given our experience helping innovators like Snowflake accelerate their time to market — going from code to cloud in weeks to hours.

These ensure there's no financial penalty for switching, a clear ROI, and no learning curve. We have always been proud to work with customers of all sizes in all industries, so these offers are available to you whether you're a Global 2000, a startup, or somewhere in between.

## Get started today

The agentic infrastructure era is already here, and we want you to bring your IaC to it. [Get started with Pulumi free](https://app.pulumi.com/signup) and provision your first stack in minutes.

If you'd like to get started with the new Terraform/OpenTofu and HCL capabilities, or take advantage of the financial flexibility options, please [get in touch](/contact/?form=sales).
