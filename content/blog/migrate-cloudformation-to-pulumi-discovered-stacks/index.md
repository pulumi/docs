---
title: "Migrate CloudFormation to Pulumi with Discovered Stacks"
# TODO: Update this date before publishing! Currently set to far future to prevent premature publication.
date: 2099-01-01
draft: false
meta_desc: "Migrate a CloudFormation stack to Pulumi with Discovered Stacks: verify every resource, import with a zero-diff preview, and track it all in Pulumi Cloud."
meta_image: meta.png
feature_image: feature.png
authors:
    - alejandro-cotroneo
tags:
    - tutorials
    - insights
    - import
    - aws
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter:
    linkedin:
    bluesky:
---

Migrating a CloudFormation stack to Pulumi used to mean a converted template, a pile of `pulumi import` commands, and a spreadsheet to track which resources made it across. With [Discovered Stacks](/docs/insights/discovery/discovered-stacks/), Pulumi Cloud does the bookkeeping: every resource in the stack gets an explicit migration status, and the migration is done when the code provably matches the cloud. In this tutorial, we take one real CloudFormation stack from discovered to migrated, end to end.

<!--more-->

## What we're migrating

Our example is `payments-api`, a CloudFormation stack with 32 resources: an S3 bucket, a DynamoDB table, a few Lambda functions, and the IAM roles and policies that wire them together. The plan has five steps:

1. Find the stack in Pulumi Cloud.
1. Verify that Pulumi sees exactly what CloudFormation sees.
1. Run the migration.
1. Check the quality gate: a zero-diff `pulumi preview`.
1. Resolve the stragglers, so every resource is accounted for.

We'll use [Pulumi Neo](/docs/ai/) to do the heavy lifting, but nothing here depends on it. The same flow works with your own coding agent or entirely by hand, because migration status is derived from actual stack state — however the work gets done, the console shows the same progress.

## Step 1: Find your stack in Pulumi Cloud

Discovered Stacks builds on [Pulumi Insights Discovery](/docs/insights/discovery/), so the only prerequisite is an [Insights account](/docs/insights/discovery/accounts/) that has scanned the AWS account holding your CloudFormation stacks.

Once a scan has run, open the **Stacks** page and turn on **Show Discovered Stacks**. Your CloudFormation stacks appear alongside your Pulumi stacks — same list, same filters — marked with a chip that identifies them as discovered. The project name comes from the CloudFormation stack (`payments-api`), and the stack name encodes the account and region it was found in — so the same template deployed to two regions shows up as two distinct discovered stacks.

<!-- TODO: screenshot — Stacks page with Show Discovered Stacks on, payments-api visible with the discovered chip. 1px border. -->

## Step 2: Verify before you migrate

Before touching anything, open the stack and check the math. CloudFormation reports 32 resources in `payments-api`; the discovered stack shows 32 rows. Each row has two type columns: the **origin type** (`AWS::S3::Bucket`) and the **Pulumi type** it maps to (`aws:s3/bucket:Bucket`). Drill into any resource and you'll see **Origin Properties** — the resource as CloudFormation reports it — next to the properties in Pulumi's model.

Every row also carries a migration status. For `payments-api`, the breakdown looks like this:

- **26 Ready**: mapped to a Pulumi type and confirmed to exist. These are importable right now.
- **2 Not found**: mapped, but Discovery couldn't confirm their current state. Something to look into.
- **3 No exact match**: no direct Pulumi type. We'll see why in step 5.
- **1 Not applicable**: the CloudFormation stack construct itself, which has no cloud resource of its own.

Notice what you've done so far: zero migration work. You've confirmed that Pulumi sees exactly what CloudFormation sees, with a reconciled count and a named status for every resource. If you stopped here, that visibility alone would be worth the visit.

<!-- TODO: screenshot — payments-api resource list showing origin type, Pulumi type, and status columns with the breakdown visible. -->

## Step 3: Run the migration

From the discovered stack's **Actions** menu, select **Migrate with Neo**. Neo asks where the code should live — a git repository, a target project and stack, a language — and then works through the migration:

1. Fetches the discovered resources and their statuses through the [Discovered Stacks API](/docs/insights/discovery/discovered-stacks/migrate/#use-the-api).
1. Imports the Ready resources in batches with `pulumi import --generate-code`, building up a Pulumi program as it goes.
1. Runs `pulumi preview` after each batch and reconciles the generated code against the real cloud state.
1. Opens a pull request with the program and a migration report.

Because `pulumi import` writes state as it runs, the console updates live: statuses flip from `Ready` to `Migrated` batch by batch, without anyone marking a checkbox.

Prefer more control? The same menu offers **Generate Code** and **Generate Import Commands** for a deterministic, do-it-yourself path — and the API that Neo uses is the same one your own agent or scripts can drive. The statuses don't care who does the work.

<!-- TODO: screenshot — Actions menu on a discovered stack showing Migrate with Neo / Generate Code / Generate Import Commands. -->

## Step 4: The quality gate

The pull request is where the migration earns trust. The bar is a **zero-diff `pulumi preview`**: the generated program, run against the live cloud, proposes no changes.

```text
Resources:
    27 unchanged
```

A clean preview means the code matches reality — not approximately, provably. If the preview shows a diff, the code gets fixed until it doesn't; the cloud is never modified to make the code look right. And notably, there's no `pulumi up` in this story: importing already synced the state to Pulumi Cloud, so the first `up` you run is for the first real change you make after the migration.

The PR's migration report summarizes the rest: status counts before and after, the full resource mapping table, and the resources that need a human decision — which brings us to the last step.

## Step 5: Resolve the stragglers

Five resources didn't import: 2 Not found and 3 No exact match. This is where most migrations historically lose the plot — those rows end up in a spreadsheet, the spreadsheet goes stale, and nobody remembers why resource 31 was skipped. Discovered Stacks replaces that with a single, visible decision: **ignore**. An ignored resource stays in the list, deliberately excluded from the migration rather than quietly forgotten.

Working through ours:

- **Not found #1** turns out to be deleted — the import fails with "resource does not exist." It gets ignored; there's nothing left to migrate.
- **Not found #2** had an imperfect type mapping. Importing with the corrected type works; the origin row is ignored in favor of the imported resource.
- **Two No exact match rows** are inline IAM policies, which Pulumi models as part of their parent role. The roles are already migrated, so each policy is ignored — its contents already live on the role.
- **The last No exact match row** is a CDK-generated custom resource whose Lambda handler just empties buckets on stack deletion. Pulumi doesn't need it, so it's ignored too.

Final accounting: 32 discovered resources — 26 **Migrated**, 5 ignored, 1 **Not applicable**. Every row resolved, and every skip a deliberate decision the whole team can see instead of a forgotten spreadsheet row.

<!-- TODO: screenshot — resource list after migration: Migrated statuses plus ignored rows visible. -->

## Where you end up

The `payments-api` program now lives in your repository, reviewed and merged like any other code. The discovered stack remains as the migration record, and because progress is derived from real state, it's still accurate if you come back next week — or if a teammate picks up where you left off. Migration doesn't have to be all-or-nothing either: for a larger stack, land the Ready resources today and return for the rest whenever you're ready.

The same flow works for Azure Resource Manager deployments, which Discovery models as discovered stacks too. And for Pulumi-hosted Terraform stacks, a **Migration** tab offers the identical experience, with statuses derived from the Terraform state.

To go deeper:

- [Discovered Stacks documentation](/docs/insights/discovery/discovered-stacks/)
- [Migrate from a Discovered Stack](/docs/insights/discovery/discovered-stacks/migrate/)
- [Migrating from AWS CloudFormation](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/)
