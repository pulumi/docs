---
title_tag: "Migrating from Terraform Enterprise to Pulumi"
meta_desc: How teams running self-managed Terraform Enterprise move to self-hosted Pulumi Cloud — the same on-prem operating model, with a phased migration path.
title: From Terraform Enterprise
h1: Migrating from Terraform Enterprise to Self-Hosted Pulumi Cloud
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: From Terraform Enterprise
        parent: iac-comparisons-terraform
        weight: 3
aliases:
    - /docs/iac/comparisons/terraform/migrating-from-terraform-enterprise/
---

Terraform Enterprise teams run infrastructure as code on their own infrastructure for data control, network isolation, and compliance. [Self-hosted Pulumi Cloud](/product/self-hosted/) offers the same operating model: the complete Pulumi Cloud platform — state, secrets, RBAC, policy, and deployments — running in your own cloud account or data center, including fully air-gapped networks. This guide is for teams evaluating a move from Terraform Enterprise to Pulumi without giving up self-management.

## What you get with self-hosted Pulumi Cloud

Self-hosted Pulumi Cloud runs the same platform as the [SaaS](https://app.pulumi.com/), so teams evaluate features once and choose the deployment topology that fits their compliance posture:

- **The full platform in your environment.** State management, secrets, role-based access control, [policy enforcement](/docs/insights/policy/), and [deployments](/docs/deployments/) all run on infrastructure you operate.
- **Data you control.** State and secrets live in a MySQL database and an object store within your own network. Encryption keys can be managed locally or through AWS KMS or Azure Key Vault.
- **Air-gapped operation.** Run with no egress to the public internet, including environments that require FedRAMP.
- **Your identity provider.** Integrate GitHub Enterprise, GitLab, SAML SSO, and others.

For a feature-by-feature comparison of the two tools, see [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/).

## How migration works

You don't rewrite everything at once. Pulumi is designed to adopt incrementally, and these paths combine:

1. **Run side by side.** Pulumi programs can [reference existing Terraform state](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#referencing-terraform-state) and read its outputs, so you keep existing infrastructure in Terraform while adopting Pulumi for new work.
1. **Store Terraform state in Pulumi.** [Pulumi Cloud can act as a Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/), giving you encrypted state, history, locking, RBAC, and audit policies while you continue to run Terraform day-to-day.
1. **Convert HCL.** [`pulumi convert --from terraform`](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) translates Terraform HCL into a Pulumi program in the language of your choice, preserving names, modules, and structure where possible.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) brings already-provisioned resources under Pulumi management and generates the corresponding code.

For a complete walkthrough including bulk conversion and state migration, see [Migrating from Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/).

## Pricing

Self-hosted Pulumi Cloud is available with the Business Critical edition. See [pricing](/pricing/) for what each edition includes, and [contact us](/contact/) to discuss licensing and an evaluation for your environment.

## Get started

1. [Install self-hosted Pulumi Cloud](/docs/administration/self-hosting/install/) and deploy it yourself — evaluate with Docker Compose in minutes, then go to production on AWS, Azure, Google Cloud, or Kubernetes.
1. [Get an evaluation license](/product/self-hosted/#self-hosted-trial), or talk to us about a guided rollout.
