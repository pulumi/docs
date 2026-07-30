---
title: "Discovered Stacks: One Place for All Your Infrastructure"
# TODO: Update this date before publishing! Currently set to far future to prevent premature publication.
date: 2099-01-01
draft: false
meta_desc: "Discovered Stacks: Pulumi Cloud now models your CloudFormation and ARM deployments as Pulumi IaC stacks, with a built-in migration path."
feature_image: feature.png
category: product
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
    twitter: |
        Every migration to IaC starts with a spreadsheet tracking which resources made it across. It's stale the day it's written — six months later nobody can say which of 800 actually migrated, and which were quietly forgotten.

        Here's what replaces it.
    linkedin: |
        Almost nobody's cloud estate is one tool. There's the CloudFormation that came with the AWS account, the ARM templates from the Azure team, the Terraform from an acquisition, and the Pulumi you're standardizing on.

        That fragmentation is why migrations stall. Moving a stack to Pulumi was never the hard part — knowing where you stand is. The tracking lives in a spreadsheet, the spreadsheet goes stale the day it's written, and six months later nobody can say which of 800 resources made it across and which were quietly forgotten.

        Today we're launching Discovered Stacks: Pulumi Cloud now models your CloudFormation stacks and ARM deployments as stacks, right alongside your Pulumi IaC. Every resource carries a migration status computed from live state on both ends — never a stale line someone forgot to update.

        We wrote up how it works.
    bluesky: |
        Six months into a migration, can you say which of 800 resources actually made it to IaC — and which were quietly forgotten? The spreadsheet tracking it went stale the day it was written.

        The spreadsheet is retired for good.
---

Today we're launching **Discovered Stacks**: Pulumi Cloud now models your AWS CloudFormation stacks and Azure Resource Manager deployments as stacks, right alongside your Pulumi IaC stacks. And when you're ready to bring them under Pulumi management, migration is built in, with every resource tracked until the code provably matches the cloud.

<!--more-->

## Why: your infrastructure doesn't live in one tool

Almost nobody's cloud estate is a single technology. There's the CloudFormation that came with the AWS account, the ARM templates from the Azure team, the Terraform from an acquisition, and the Pulumi you're standardizing on. Each tool has its own console, its own grouping, its own idea of state, and no single place shows you everything you run.

That fragmentation is also why migrations stall. Moving a stack to Pulumi has never been the hard part; *knowing where you stand* is. The tracking lives in a spreadsheet, the spreadsheet goes stale the day it's written, and six months later nobody can say which of the 800 resources made it across and which were quietly forgotten.

## Nothing gets lost

Discovered Stacks gives you confidence that your migration plan or governance efforts will include all resources. This catches a common failure mode where resources are missed by your existing migration scripts or automations. When [Pulumi Insights](/docs/insights/) scans your accounts, every CloudFormation stack and ARM deployment becomes a discovered stack, and every resource in it appears as a row with an explicit migration status: ready to migrate, requiring review before migration, or already migrated. Every status is computed from live state on both ends — what Pulumi manages and what the source tool reports — so it's never a stale annotation someone forgot to update.

Each resource shows its **origin type** (`AWS::S3::Bucket`) next to its **Pulumi type** (`aws:s3/bucket:Bucket`), with the origin properties side by side with Pulumi's view, so you can verify that Pulumi sees exactly what your source tool sees before you change anything. Decisions you make along the way (*this resource was deleted, that policy is covered by its parent role*) are recorded by marking the resource resolved: it stays visible to your whole team, deliberately handled rather than quietly forgotten. The spreadsheet is retired.

![The Resources grid of a discovered CloudFormation stack in Pulumi Cloud: each row pairs the Pulumi type (aws:sns:Topic) with its origin type (AWS::SNS::Topic), a Managed By column reading CloudFormation, and a provider link out to the resource in the AWS console.](resources-list.png)

## Migration on your terms

When you're ready to migrate, the console is where you plan and build confidence. **Migrate with Neo** hands the job to [Pulumi Neo](/docs/ai/), which imports the resources, reconciles the generated program, and opens a pull request for review. If you prefer local development, **Generate Import Commands** gives you the raw materials, and the same API lets your own agents drive the flow.

Two things hold regardless of the path. Progress is *derived*: a resource shows as migrated when it actually exists in the target Pulumi stack, not when someone checks a box. And the quality gate is a **zero-diff `pulumi preview`** — the migration is done when the code demonstrably matches your cloud.

Terraform stacks whose state you [store in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/) get the same treatment through a new **Migration** tab, with statuses derived from the Terraform state.

## Try it

Open the **Stacks** page in [Pulumi Cloud](https://app.pulumi.com/), turn on **Show Discovered Stacks**, and your CloudFormation and ARM estates appear next to your IaC. From there:

- Read the [Discovered Stacks documentation](/docs/insights/discovery/discovered-stacks/).
- Follow the [step-by-step migration tutorial](/blog/discovered-stacks-migrate-cloudformation-to-pulumi/) to take a CloudFormation stack all the way to Pulumi.

We'd love to hear how it works on your estate — reach out through [Pulumi feedback](https://github.com/pulumi/pulumi-cloud-requests) or your customer success team.
