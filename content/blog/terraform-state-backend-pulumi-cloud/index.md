---
title: "Now in Public Beta: Store Terraform State in Pulumi Cloud"
date: 2026-03-05
allow_long_title: true
draft: false
meta_desc: "Pulumi Cloud now serves as a Terraform state backend with encrypted state, audit policies, and unified resource visibility — no workflow changes required."
meta_image: meta.png
authors:
    - claire-gaestel
tags:
    - releases
    - features
    - terraform
    - pulumi-cloud
    - iac

social:
    twitter: "Pulumi Cloud now stores Terraform state — which means Neo, our AI infrastructure agent, works across your entire cloud footprint. Terraform and Pulumi IaC, one agent, one control plane. Migrate your state in minutes, no code changes required."
    linkedin: "Pulumi Cloud can now serve as a Terraform state backend (public beta). But the real unlock? Neo, Pulumi's AI infrastructure agent, now works across your entire infrastructure — Terraform and Pulumi IaC alike. Ask Neo to find resources, trace dependencies, troubleshoot issues, or write infrastructure code, and it reasons over everything regardless of which IaC tool manages it. One agent, one control plane, every stack. Your team keeps using the Terraform or OpenTofu CLI while you get Neo, encrypted state, RBAC, audit policies, and unified resource visibility. Migration takes minutes."
---

Platform engineering teams managing infrastructure across Terraform and Pulumi now have a way to unify state management without rewriting a single line of HCL. Starting today, Pulumi Cloud can serve as a [Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/), letting you store and manage Terraform state alongside your Pulumi stacks. Your team continues using the Terraform or OpenTofu CLI for day-to-day operations while gaining the benefits of Pulumi Cloud: [Pulumi Neo](/docs/ai)-our infrastructure agent- over all your infrastructure, encrypted state storage, update history, state locking, role-based access control, audit policies, and unified resource visibility through [Insights](/docs/pulumi-cloud/insights/)..

<!--more-->

This feature is now available in **public beta**.

## Why this matters

Most organizations adopting Pulumi are not starting from scratch. They have years of Terraform deployments spread across teams, and migrating everything to a new IaC tool overnight is not realistic. We have heard from customers who are excited about the power of Pulumi Cloud but have had to manage migration projects before they can fully benefit from centralized visibility and governance.

The Terraform state backend in Pulumi Cloud changes that equation. Instead of requiring a full code conversion before teams see value, you can migrate your state in minutes and immediately unlock Pulumi Cloud capabilities for your existing Terraform infrastructure — including Neo, Pulumi's AI infrastructure agent. Once your Terraform state is in Pulumi Cloud, Neo can reason about those resources the same way it does for Pulumi IaC stacks: finding resources, troubleshooting issues, understanding dependencies, and writing infrastructure code PRs. Teams that prefer Terraform can keep using it, while platform engineers get a single AI-powered control plane across the entire infrastructure estate.

## What you get

When you store Terraform state in Pulumi Cloud, your Terraform-managed resources get the following added functionality:

**Agentic infrastructure with Neo.** [Neo](/docs/ai/), Pulumi's AI infrastructure agent, works across your entire cloud footprint — Terraform and Pulumi IaC alike. Once your Terraform state is in Pulumi Cloud, you can ask Neo to find resources across both tools, trace dependencies that span Terraform and Pulumi stacks, troubleshoot configuration issues, and generate new infrastructure code informed by your existing resources. This means platform teams get a single AI-powered interface regardless of which IaC tool manages each piece of infrastructure.

**Encrypted state with update history.** State is encrypted in transit and at rest. Every change is tracked as a versioned checkpoint visible in the [stack activity tab](/docs/deployments/projects-and-stacks/#stack-activity), giving you full rollback capability. This is a common concern for teams currently storing state in S3 buckets.

**Automatic state locking.** Pulumi Cloud prevents concurrent Terraform operations from corrupting state, without requiring you to configure DynamoDB tables or other external locking mechanisms.

**Role-based access control.** Control who can read or modify each stack using [teams and RBAC](/docs/administration/access-identity/rbac/), applying the same access policies you use for Pulumi stacks.

**Unified resource visibility.** View Terraform-managed resources alongside Pulumi-managed resources in [Resource Search](/docs/insights/discovery/search/). Each Terraform resource appears in the console using a `pulumi:terraform:<tf-type>` naming convention, so you can search and filter using the attribute names you already know.

**Audit policies.** Run [audit (detective) policy packs](/docs/insights/policy/policy-groups/) against your Terraform-managed stacks, including Pulumi's [pre-built compliance packs](/docs/insights/policy/policy-packs/pre-built-packs/) for CIS, PCI, and more. Pulumi Cloud performs a best-effort schema mapping from Terraform resource shapes to Pulumi provider equivalents, so existing policy packs work without modification in most cases.

**Stack outputs and references.** Terraform root module outputs are automatically mapped to Pulumi [stack outputs](/docs/iac/concepts/stacks/#outputs), making them available via [stack references](/docs/iac/concepts/stacks/#stackreferences) and the [`pulumi-stacks` ESC provider](/docs/esc/integrations/infrastructure/pulumi-iac/pulumi-stacks/). This is useful for sharing foundational infrastructure like VPC IDs or DNS zones between Terraform and Pulumi stacks, and for incremental migrations where legacy infrastructure stays in Terraform while new stacks are written in Pulumi.

## How it works

Pulumi Cloud implements the [Terraform remote backend API](https://developer.hashicorp.com/terraform/language/backend/remote). You point the Terraform CLI at Pulumi Cloud using the standard `backend "remote"` configuration block, and no changes to your Terraform code or workflow are required.

Each Terraform workspace maps to a Pulumi stack. The workspace name follows the convention `<project>_<stack>`. For example, `networking_prod` creates a stack named `prod` in the `networking` project.

## Get started

Migration from S3, Azure Blob, GCS, local backends, or HCP Terraform (Terraform Cloud) takes minutes and is documented in the [Terraform state backend guide](/docs/iac/get-started/terraform/terraform-state-backend/). From S3, Azure Blob, GCS, or local state, back up your state, update your backend block to point to Pulumi Cloud, set `TF_TOKEN_api_pulumi_com`, and run `terraform init -migrate-state`. From HCP Terraform, export state manually and push it to Pulumi Cloud.

Each Terraform resource stored in Pulumi Cloud counts as a resource under management, the same as a Pulumi-managed resource. See the [pricing page](/pricing/) for details.

{{< blog/cta-button "Store Terraform State in Pulumi Cloud" "/docs/iac/get-started/terraform/terraform-state-backend/" >}}

If you have questions or feedback, join us in the [Pulumi Community Slack](https://slack.pulumi.com/) or open an issue on [GitHub](https://github.com/pulumi/pulumi).
