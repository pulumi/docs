---
title: "Provider Upgrade Game Days with Pulumi"
date: 2026-07-09
meta_desc: "Run a provider upgrade game day with Pulumi: pin dependencies, build a canary stack, scan preview JSON, batch rollouts, and recover safely."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - day-2-operations
    - providers
social:
    twitter: |
        Provider upgrades should feel like game days, not fire drills.

        Use Pulumi previews, canary stacks, and rollout gates to catch risky replacements before prod changes.
    linkedin: |
        Cloud provider upgrades can quietly change defaults, replacement behavior, and generated diffs.

        This guide shows a practical Pulumi game day for upgrading providers safely: pin dependencies, run a canary, mine preview JSON for destructive changes, batch stacks by risk, and keep a recovery path ready.
    bluesky: |
        Provider upgrades should feel like game days, not fire drills.

        Here is a Pulumi workflow for canaries, preview gates, and safer batch rollouts.
---

[Pulumi](/docs/) provider upgrades are not dependency chores. They are production-change rehearsals. A new AWS, Azure, Google Cloud, Kubernetes, or SaaS provider can bring security fixes and new resources, but it can also expose drift, change defaults, or reveal that an old property now forces replacement.

A better upgrade starts with a canary stack and a clear rollback path. This post walks through a concrete game day for upgrading a provider across many Pulumi stacks without turning one dependency bump into an all-hands incident.

<!--more-->

## The game day scenario

Imagine a platform team owns a shared AWS baseline used by application stacks. The baseline creates:

1. An ECS service behind an Application Load Balancer.
2. An RDS instance with deletion protection enabled.
3. CloudWatch log groups with retention policies.
4. IAM roles and policies for deploy-time automation.

The team needs to upgrade `@pulumi/aws` to pick up new resources and fixes. The risky part is not the package install. The risky part is discovering whether the new provider interprets existing state differently.

## Step 1: Pin the upgrade in package and lock files

Most Pulumi provider versions are inferred from your language package dependencies and lockfile. Keep that boring on purpose. Make one dependency change, commit the package and lockfile changes on a branch, and let every preview use the same provider version.

```bash
npm install @pulumi/aws@6.66.0 --save-exact
```

Avoid scattering one-off provider versions through resource options. The `version` resource option exists, but [Pulumi documents it as an override](/docs/iac/concepts/resources/options/version/) that should not be used directly during normal operations. For fleet upgrades, exact package pins and lockfiles are auditable in a single commit and reversible with one revert.

## Step 2: Build an upgrade canary stack

Create a canary that looks boringly representative. It should contain the resource classes most likely to hurt if replaced: databases, load balancers, identity bindings, private endpoints, and anything with external DNS.

The canary should also make the risk obvious in code. For example, protect stateful resources and name them explicitly:

```typescript
import * as aws from "@pulumi/aws";

const logs = new aws.cloudwatch.LogGroup("app", {
    retentionInDays: 30,
});

const database = new aws.rds.Instance("orders", {
    allocatedStorage: 100,
    engine: "postgres",
    engineVersion: "16.3",
    instanceClass: "db.m7g.large",
    deletionProtection: true,
    skipFinalSnapshot: false,
}, {
    protect: true,
});

export const databaseEndpoint = database.endpoint;
export const logGroupName = logs.name;
```

The goal is not to test every resource in the estate. The goal is to force dangerous changes to show up in a small, reviewable preview before they appear in production.

## Step 3: Turn previews into a risk report

Baseline drift before changing the provider, then run a diff preview with the upgraded dependency and save the machine-readable output. Avoid running `pulumi refresh --yes` after the provider bump because refresh writes provider-normalized state before reviewers see the diff. If you need live cloud reads during the game day, use preview refresh so the state file is not updated.

```bash
pulumi stack select platform/canary
pulumi preview --refresh --diff --json > preview-provider-upgrade.json
```

Then mine the preview for operations that deserve human review:

```bash
jq -r '
  .steps[]?
  | select(.op == "replace" or .op == "delete" or .op == "delete-replaced")
  | [.op, .urn] | @tsv
' preview-provider-upgrade.json
```

For a provider upgrade, a clean result is not "no diff." A useful result is specific: maybe IAM policy JSON normalizes, log group tags update in place, and the protected RDS instance has no replacement. That gives reviewers something concrete to approve.

If the report shows a replacement on a protected database or load balancer, stop the rollout. Investigate the property that triggered replacement before touching production stacks.

## Step 4: Batch by blast radius, not alphabetically

Once the canary is clean, a sensible rollout order is to batch by risk:

1. Ephemeral development stacks.
2. Shared non-production stacks.
3. Low-traffic production stacks.
4. Stateful production stacks.
5. Shared network, identity, and data-plane stacks.

Each batch should use the same lockfile and the same preview gate. If a batch introduces a new replacement or delete operation, pause the rollout and keep the remaining stacks on the old provider.

## Step 5: Keep recovery boring

Before the first production batch, export a checkpoint for the stack and keep the dependency rollback as a separate commit:

```bash
pulumi stack select platform/prod
pulumi stack export --file platform-prod-before-provider-upgrade.json
```

If the upgrade produces an unexpected plan, roll back the dependency change and preview again. If state has already changed and you need to restore a checkpoint, use `pulumi stack import` deliberately and only after reviewing the exported state.

```bash
pulumi stack import --file platform-prod-before-provider-upgrade.json
```

The safest recovery rarely involves state import. Stop before `pulumi up`, revert the lockfile, and confirm the old provider still previews cleanly. Reserve state import for controlled recovery, not as a routine undo button.

## Conclusion

Provider upgrades get dangerous when they are treated like ordinary dependency bumps. Treat them like game days instead: pin one version, rehearse on a canary, turn preview JSON into a risk report, batch by blast radius, and keep rollback boring. Pulumi gives you the preview and state tools; the discipline is using them before production is on the line.
