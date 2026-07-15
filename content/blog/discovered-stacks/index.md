---
title: "Discovered Stacks: One Model for All Your Infrastructure"
# TODO: Update this date before publishing! Currently set to far future to prevent premature publication.
date: 2099-01-01
draft: false
meta_desc: "Pulumi Cloud now models your Discovered CloudFormation stacks and ARM deployments as stacks — with a seamless path to Pulumi IaC."
meta_image: meta.png
feature_image: feature.png
authors:
    - alejandro-cotroneo
tags:
    - features
    - insights
    - pulumi-cloud
canonical_url: /docs/insights/discovery/discovered-stacks/
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter:
    linkedin:
    bluesky:
---

Today we're launching **Discovered Stacks**: Pulumi Cloud now models your AWS CloudFormation stacks and Azure Resource Manager deployments as stacks, right alongside your Pulumi IaC stacks — same pages, same navigation, same model. And when you're ready to bring them under Pulumi management, migration is built in, with every resource tracked until the code provably matches the cloud.

<!--more-->

<!-- TODO: hero screenshot — Stacks page listing discovered stacks alongside IaC stacks, chip visible. -->

## Why: your infrastructure doesn't live in one tool

Almost nobody's cloud estate is a single technology. There's the CloudFormation that came with the AWS account, the ARM templates from the Azure team, the Terraform from an acquisition, and the Pulumi you're standardizing on. Each tool has its own console, its own grouping, its own idea of state — and no single place shows you everything you run.

That fragmentation is also why migrations stall. Moving a stack to Pulumi has never been the hard part; *knowing where you stand* is. The tracking lives in a spreadsheet, the spreadsheet goes stale the day it's written, and six months later nobody can say which of the 800 resources made it across and which were quietly forgotten.

## Nothing gets lost

Discovered Stacks starts from the failure mode that matters most: a resource silently falling through the cracks. When [Pulumi Insights](/docs/insights/) scans your accounts, every CloudFormation stack and ARM deployment becomes a discovered stack, and every resource in it appears as a row with an explicit migration status — ready to import, pending verification, unmapped, migrated. The source count always reconciles against the statuses.

Each resource shows its **origin type** (`AWS::S3::Bucket`) next to its **Pulumi type** (`aws:s3/bucket:Bucket`), with the origin properties side by side with Pulumi's view — so you can verify that Pulumi sees exactly what your source tool sees before you change anything. Decisions you make along the way — *this resource was deleted, that policy is covered by its parent role* — are recorded by ignoring the resource: it stays visible to your whole team, deliberately excluded rather than quietly forgotten. The spreadsheet is retired.

<!-- TODO: screenshot — resource list with origin type, Pulumi type, and status columns. -->

## Migration on your terms

When you're ready to migrate, the console is where you plan and build confidence — and the work completes in your world, as code in your repository. **Migrate with Neo** hands the job to [Pulumi Neo](/docs/ai/), which imports the resources, reconciles the generated program, and opens a pull request for review. Prefer determinism? **Generate Code** and **Generate Import Commands** give you the raw materials, and the same API lets your own agents drive the flow.

Two things hold regardless of the path. Progress is *derived, never declared*: a resource shows as migrated when it actually exists in the target Pulumi stack, not when someone checks a box. And the quality gate is a **zero-diff `pulumi preview`** — the migration is done when the code demonstrably matches your cloud.

Hosted Terraform stacks get the same treatment through a new **Migration** tab, with statuses derived from the Terraform state file.

## Try it

Open the **Stacks** page in [Pulumi Cloud](https://app.pulumi.com/), turn on **Show Discovered Stacks**, and your CloudFormation and ARM estates appear next to your IaC. From there:

- Read the [Discovered Stacks documentation](/docs/insights/discovery/discovered-stacks/).
- Follow the [step-by-step migration tutorial](/blog/migrate-cloudformation-to-pulumi-discovered-stacks/) to take a CloudFormation stack all the way to Pulumi.

We'd love to hear how it works on your estate — reach out through [Pulumi feedback](https://github.com/pulumi/pulumi-cloud-requests) or your customer success team.
