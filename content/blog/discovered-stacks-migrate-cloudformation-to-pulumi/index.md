---
title: "Migrate CloudFormation to Pulumi with Discovered Stacks"
# TODO: Update this date before publishing!
date: 2099-01-01
draft: false
meta_desc: "Migrate a CloudFormation stack to Pulumi with Discovered Stacks: verify every resource, import with a zero-diff preview, and track it all in Pulumi Cloud."
feature_image: feature.png
category: tutorials
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

With [Discovered Stacks](/docs/insights/discovery/discovered-stacks/), Pulumi Cloud does the bookkeeping for a CloudFormation migration: every resource in the stack gets an explicit migration status, and the migration is done when the code provably matches the cloud. In this tutorial, we take one real CloudFormation stack from discovered to migrated, end to end.

<!--more-->

## What we're migrating

Our example is `payments-api`, a CloudFormation stack with 61 resources: a VPC, an Aurora ledger database behind an RDS Proxy, an assets S3 bucket, a DynamoDB ledger table, a charge-processing Lambda, an SNS/SQS/Kinesis payment-events pipeline, and the IAM roles, KMS keys, and secrets that wire them together. The plan has five steps:

1. Find the stack in Pulumi Cloud.
1. Verify that Pulumi sees exactly what CloudFormation sees.
1. Run the migration.
1. Resolve the stragglers, so every resource is accounted for.
1. Confirm the quality gate: a zero-diff `pulumi preview`.

We'll use [Pulumi Neo](/docs/ai/) to do the heavy lifting, but nothing here depends on it. The same flow works with your own coding agent or entirely by hand, because migration status is derived from actual stack state — however the work gets done, the console shows the same progress.

## Step 1: Find your stack in Pulumi Cloud

Discovered Stacks builds on [Pulumi Insights Discovery](/docs/insights/discovery/), so the only prerequisite is an [Insights account](/docs/insights/discovery/accounts/) that has scanned the AWS account holding your CloudFormation stacks.

Once a scan has run, open the **Stacks** page and turn on **Show Discovered Stacks**. Your CloudFormation stacks appear alongside your Pulumi stacks — same list, same filters — marked with a chip that identifies them as discovered. The project name comes from the CloudFormation stack (`payments-api`), and the stack name encodes the account and region it was found in — so the same template deployed to two regions shows up as two distinct discovered stacks.

## Step 2: Verify before you migrate

Before touching anything, open the stack and check the math. CloudFormation reports 61 resources in `payments-api`; the discovered stack shows 61 rows. Each row has two type columns: the **origin type** (`AWS::S3::Bucket`) and the **Pulumi type** it maps to (`aws:s3/bucket:Bucket`). Drill into any resource and you'll see **Origin Properties** — the resource as CloudFormation reports it — next to the properties in Pulumi's model.

Every row also carries a migration status. Compared against an empty target stack — nothing migrated yet — the breakdown for `payments-api` looks like this:

- **54 Ready**: mapped to a Pulumi type and confirmed to exist. These are importable right now.
- **2 Not found**: mapped, but Discovery couldn't confirm their current state — worth a look before importing.
- **5 No exact match**: no direct Pulumi type. We'll see why in step 5.

Notice what you've done so far: zero migration work. You've confirmed that Pulumi sees exactly what CloudFormation sees, with a reconciled count and a named status for every resource. If you stopped here, that visibility alone would be worth the visit.

![The Migration tab of the discovered payments-api stack compared against an empty target: a status summary of 54 Ready, 2 Not found, and 5 No exact match above a resource table with Name, Type, and Status columns.](discovered-stack-migration-start.png)

## Step 3: Start the migration

From the discovered stack's **Actions** menu, select **Migrate with Neo**. Neo asks where the code should live — a git repository, a target project and stack, a language — and then works through the migration:

1. Fetches the discovered resources and their statuses through the [Discovered Stacks API](/docs/insights/discovery/discovered-stacks/migrate/#use-the-api).
1. Imports the Ready resources in batches with `pulumi import --generate-code`, building up a Pulumi program as it goes.
1. Runs `pulumi preview` after each batch and reconciles the generated code against the real cloud state.
1. Opens a pull request with the program and a migration report.

Because `pulumi import` writes state as it runs, the console updates live: statuses flip from `Ready` to `Migrated` batch by batch, without anyone marking a checkbox.

Prefer more control? The same menu offers **Generate Import Commands** for a deterministic, do-it-yourself path — and the API that Neo uses is the same one your own agent or scripts can drive.

## Step 4: Resolve the stragglers

The PR's migration report flags what needs a human decision: alongside the status counts and the full resource mapping table, it lists the rows Neo couldn't import automatically. Seven needed a closer look: 2 Not found and 5 No exact match. This is where most migrations historically lose the plot — those rows end up in a spreadsheet, the spreadsheet goes stale, and nobody remembers why resource 31 was skipped. Discovered Stacks replaces that with a single, visible decision: **mark it resolved**. A resolved resource stays in the list, deliberately handled rather than quietly forgotten.

Working through ours:

- **The 2 Not found rows** are CloudWatch log groups. Discovery couldn't confirm their state, but they're live so the import succeeded so the resources were resolved without further inspection.
- **Three No exact match rows** are inline IAM policies, which Pulumi models as part of their parent role. The roles are already migrated, so each policy is marked resolved — its contents already live on the role.
- **One** is a Secrets Manager target attachment; Pulumi expresses that link through the database's own configuration, so it's marked resolved once the database is migrated.
- **The last** is a CDK-generated custom resource that strips the rules from the VPC's default security group. Pulumi models that directly as an `aws.ec2.DefaultSecurityGroup`, so there's nothing to import — it's marked resolved.

![The same Migration tab compared against the migrated Pulumi stack: every resource now reads Migrated, with Resolved chips on the seven rows that took a manual decision and a Next step column that explains each — imported to Pulumi, captured on the parent role, or nothing left to do.](discovered-stack-migration-end.png)

That accounts for every row: 54 imported directly, the 2 Not found log groups imported after a quick check, and the 5 No exact match resolved. 61 discovered resources, nothing left in a spreadsheet.

## Step 5: The quality gate

With every resource imported or resolved, the migration earns its trust in one final check: a **zero-diff `pulumi preview`**. The generated program, run against the live cloud, proposes no changes.

```text
Resources:
    56 unchanged
```

A clean preview means the code matches reality. If it shows a diff, the code gets fixed until it doesn't; the cloud is never modified to make the code look right. And notably, there's no `pulumi up` in this story: importing already synced the state to Pulumi Cloud, so the first `up` you run is for the first real change you make after the migration.

That zero-diff preview isn't just the finish line — it's a checkpoint you can build on. Imported code is faithful, but it's rarely the code you'd write by hand: generated names, repeated blocks, configuration hard-coded inline. Now that it provably matches the cloud, it's the moment to make the refactors you actually want — pull settings into stack config, split the program into modules, collapse repetition into loops, group related resources into components. The preview is your safety net for all of it: rerun it after each change, and a clean zero-diff confirms you reshaped the code without touching the infrastructure. When a refactor does shift a resource's identity — a new name or parent — the preview says so at once, and an [alias](/docs/iac/concepts/resources/options/aliases/) keeps it a no-op. Either way, you're iterating against a bar that never moves.

## Where you end up

The `payments-api` program now lives in your repository, reviewed and merged like any other code. The discovered stack remains as the migration record, and because progress is derived from real state, it's still accurate if you come back next week — or if a teammate picks up where you left off. Migration doesn't have to be all-or-nothing either: for a larger stack, land the Ready resources today and return for the rest whenever you're ready.

The same flow works for Azure Resource Manager deployments, which Discovery models as discovered stacks too. And for Pulumi-hosted Terraform stacks, a **Migration** tab offers the identical experience, with statuses derived from the Terraform state.

To go deeper:

- [Discovered Stacks documentation](/docs/insights/discovery/discovered-stacks/)
- [Migrate from a Discovered Stack](/docs/insights/discovery/discovered-stacks/migrate/)
- [Migrating from AWS CloudFormation](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/)
