---
title: "Migrate CloudFormation and ARM with Discovered Stacks"
date: 2026-07-30
meta_desc: "Pulumi Cloud now discovers your CloudFormation stacks and ARM deployments as Pulumi IaC stacks, with a built-in migration path."
authors:
    - alejandro-cotroneo
editions:
    - essentials
    - pro
    - enterprise-plus
---

Pulumi Cloud now discovers your AWS CloudFormation stacks and Azure Resource Manager deployments as [discovered stacks](/docs/insights/discovery/discovered-stacks/). When [Pulumi Discovery](/docs/insights/) scans your cloud accounts, every stack and deployment appears with its resources, each mapped to its Pulumi shape and carrying a migration status computed from live state so it never gets stale.

When you're ready to bring them under Pulumi management, the migration path is built in: hand it to [Neo](/docs/ai/), generate import commands from the console, or drive the same flow from your own agent through the REST API. Progress is derived from real state, and the migration is done when a zero-diff `pulumi preview` proves the code matches the cloud. Pulumi-hosted Terraform stacks get the same treatment through a new **Migration** tab.

Read the [announcement blog post](/blog/discovered-stacks/) or the [Discovered Stacks documentation](/docs/insights/discovery/discovered-stacks/) to learn more, and follow the [step-by-step migration tutorial](/blog/discovered-stacks-migrate-cloudformation-to-pulumi/) to take a CloudFormation stack all the way to Pulumi.
