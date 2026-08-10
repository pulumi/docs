---
title: Migrate from a Discovered Stack
title_tag: "Migrate from a Discovered Stack | Discovery & Governance"
h1: Migrate from a Discovered Stack
meta_desc: Migrate CloudFormation and ARM resources from a discovered stack to Pulumi IaC with Neo, import commands, or your own agent, verified by a zero-diff preview.
menu:
  insights:
    name: Migrate to Pulumi
    parent: insights-discovery-discovered-stacks
    weight: 10
aliases: []
pulumi_cloud_feature: insights-discovery
---

Migrating from a [discovered stack](/docs/insights/discovery/discovered-stacks/) means bringing its resources under Pulumi IaC management: a Pulumi program in your repository whose state matches the cloud exactly. The console is where you plan the migration, decide what to include, and track progress — the migration itself completes as code and CLI operations in your own repository.

A migration is done when three things are true:

1. Every discovered resource is either imported or deliberately resolved.
1. `pulumi preview` on the target stack reports no changes, proving the code matches the cloud state.
1. The program lands in your repository as the new source of record — from here on, changes to those resources happen through Pulumi IaC.

## Before you begin

- A discovered stack, created by a [Discovery scan](/docs/insights/discovery/accounts/) of the cloud account that holds your CloudFormation or ARM resources.
- A git repository where the generated Pulumi program will live.
- Cloud credentials that match the source account, ideally through a [Pulumi ESC environment](/docs/esc/).

## Start a migration

Every migration is different, and some get complex — it's worth knowing [all the migration tooling Pulumi already offers](/docs/iac/guides/migration/), since importing, coexistence, and conversion each have their place. The Migration tab is where you visualize and plan the work at a glance: start against an empty target, or select an existing stack that already holds migrated state to pick up where you left off.

From a discovered stack, the **Actions** menu offers two ways to bring the resources under Pulumi IaC management:

- **Migrate with Neo** (recommended): [Pulumi Neo](/docs/ai/) runs the whole workflow — it fetches the discovered resources, imports them, reconciles the preview, and opens a pull request with a migration report.
- **Generate Import Commands**: produce the corresponding [`pulumi import`](/docs/iac/guides/migration/import/) commands to run in your own terminal.

Both paths work against the same resource data and statuses, all exposed through a REST API: you can [list a stack's resources and their statuses](#list-resources-and-statuses), drive the imports, and [write back your resolutions](#write-back-resolutions) — so the whole flow can run locally or be driven by your own agent, with the console reflecting progress throughout.

## Set up your local project

**Migrate with Neo** scaffolds and wires up the project for you, so you can skip this section. If you're driving the migration with your own agent, create a new stack to hold the program that will control the imported resources.

```bash
# Create a stack
pulumi stack init <stackName>
```

Set cloud credentials the way you would for any Pulumi program — a [Pulumi ESC environment](/docs/esc/) is the most reliable. With the project attached, run the generated import commands and continue below.

## How a migration works

Whether Neo performs the migration or you do, a migration follows the same steps:

1. **Triage.** Review the status breakdown. Resources marked **Ready** are importable now; **Not found** and **No exact match** resources [get resolved along the way](#resolve-not-found-and-no-exact-match-resources).
1. **Import.** Bring resources into the target stack with `pulumi import`, which generates resource code you append to your program.
1. **Reconcile.** Run `pulumi preview` and fix the code until it reports no changes. A clean preview is the quality gate: it proves the program matches the actual cloud state. Freshly imported code often shows a diff on the first preview even when nothing in the cloud changed; see [Tips for a clean migration](#tips-for-a-clean-migration) for the common ones and how to clear them.

{{% notes "info" %}}
No `pulumi up` is required to complete a migration. `pulumi import` already syncs the imported state to your state file in Pulumi Cloud. Once all of your resources have been imported with a clean diff, you use `pulumi up` for future changes to the resources which are now managed by Pulumi IaC.
{{% /notes %}}

## Resolve Not found and No exact match resources

Some resources need a decision or validation before the accounting is complete. When Neo drives the migration, it makes these decisions and annotates each resource with the call it made. Resolve each one by importing it or by [marking it resolved](/docs/insights/discovery/discovered-stacks/#resolving-resources) — either way, the outcome shows up in the console and persists across sessions.

**Not found** resources are mapped but unconfirmed — sometimes deleted, sometimes a type whose live state Discovery doesn't verify (a log group, for example), in which case the resource is really there. Attempting the import is the fastest way to find out which:

- **The resource was deleted.** The import fails because the resource does not exist. Mark it resolved — there is nothing left to migrate.
- **The type mapping is imperfect.** Some source types have more than one valid Pulumi mapping. Import with the corrected type and resolve the origin resource in its favor.
- **The resource is fine.** The import succeeds and the status flips to **Migrated** on its own after the corresponding `pulumi preview`.

**No exact match** resources have no direct Pulumi type. Most fall into a handful of familiar patterns:

- **Inline definitions**, such as an IAM policy that Pulumi models as a property of its parent role. Once the parent is migrated, mark the child resolved.
- **Implicit links**, such as a secret-to-target attachment that Pulumi expresses through the target's configuration. Mark it resolved once the target resource is migrated.
- **Custom resources**, such as CloudFormation `Custom::*` types backed by a Lambda function. Review what the handler does and decide whether to replace it with a Pulumi equivalent or mark it resolved.

## Tips for a clean migration

### Import in small, verifiable batches

Import a coherent group of resources, get its preview clean, then move to the next — rather than importing everything at once. Grouping by the source construct works well: for CloudFormation, the logical stack or a resource-type prefix. Keeping batches to roughly 20 resources keeps each preview readable.

Import the **Ready** resources first. A single resource that can't be imported — a deleted resource, or one whose import ID is wrong — aborts an entire batch, so keep unconfirmed **Not found** resources out of the bulk import and handle them one at a time.

### Clear a noisy preview

Work through the first preview by the shape of each change:

- **A property the cloud has but your code doesn't set** — add it to the code with the real value.
- **A property your code sets that the cloud never returns** — a provider default for a write-only or delete-time field (for example `recoveryWindowInDays` on a Secrets Manager secret, or `confirmationTimeoutInMinutes` on an SNS subscription). These can never match the imported state, so silence them with [`ignoreChanges`](/docs/iac/concepts/resources/options/ignorechanges/):

  ```typescript
  new aws.secretsmanager.Secret("db-secret", { /* ...imported inputs... */ }, {
      ignoreChanges: ["recoveryWindowInDays"],
  });
  ```

- **A value mismatch** — query the cloud for the real value and set it in code.

Generated code is occasionally invalid — for instance an empty nested block the provider rejects. When a block has no real value in the cloud, remove it. Reserve `ignoreChanges` for genuinely provider-managed fields; don't use it to hide a value you can set correctly.

### Link an imported resource to its origin

When a resource can't be matched automatically to the counterpart you migrated it into, [annotate and link them](/docs/insights/discovery/discovered-stacks/#resolving-resources) — a comment plus a link to the migrated resource keeps a record of the decisions you made.

### Reorganize the generated code safely

Generated code is flat — every resource at the top level, with hardcoded IDs and no cross-references. Restructuring it (grouping resources into a [component](/docs/iac/concepts/components/), splitting files, replacing literal IDs with references) is worthwhile. Do it *after* the preview is clean, and re-run `pulumi preview` after each change so the zero-diff never breaks.

Moving a resource under a component changes its [URN](/docs/iac/concepts/resources/names/), which Pulumi reads as delete-and-recreate — destructive for a real resource. Preserve identity with an [alias](/docs/iac/concepts/resources/options/aliases/) to the resource's previous URN:

```typescript
class Messaging extends pulumi.ComponentResource {
    constructor(name: string, opts?: pulumi.ComponentResourceOptions) {
        super("demo:index:Messaging", name, {}, opts);

        // Was `new aws.sns.Topic("events", ...)` at the top level before the refactor.
        new aws.sns.Topic("events", { /* ...imported inputs... */ }, {
            parent: this,
            aliases: [`urn:pulumi:${pulumi.getStack()}::${pulumi.getProject()}::aws:sns/topic:Topic::events`],
        });
    }
}
```

## Terraform stacks

[Pulumi-hosted Terraform stacks](/docs/iac/get-started/terraform/terraform-state-backend/) are not discovered stacks, but they get the same migration experience through a **Migration** tab on the stack. Origin types show the Terraform types, such as `aws_s3_bucket`, and statuses are derived from the state conversion.

## Use the API

The migration data is available through the Pulumi Cloud REST API, which is what Neo and other agents use.

### List resources and statuses

List a discovered stack's resources, including migration statuses. Pass `compareTo` to compute statuses against a target Pulumi stack:

```bash
GET /api/preview/insights/{org}/discovered-stacks/{project}/{stack}/resources?compareTo={targetProject}/{targetStack}
```

Each resource's `migrationStatus` field carries the raw status token — `Ready`, `NotFound`, `NoMatch`, `Migrated`, `PulumiOnly`, or `NotApplicable` — corresponding to the **Ready**, **Not found**, **No exact match**, **Migrated**, **Existing**, and **Not applicable** labels shown in the console.

### List Terraform stack resources

For a Pulumi-hosted **Terraform** stack, the equivalent endpoint returns the converted resources and their statuses:

```bash
GET /api/preview/insights/{org}/stacks/{project}/{stack}/migration?compareTo={targetProject}/{targetStack}
```

### Write back resolutions

Decisions are written back through the same API — [marking a resource resolved](/docs/insights/discovery/discovered-stacks/#resolving-resources), with an optional comment and a link to the target-stack resource — so an agent can drive an entire migration end to end without the console:

```bash
PUT /api/preview/insights/{org}/discovered-stacks/{project}/{stack}/migration
```

## Next steps

- [Discovered Stacks](/docs/insights/discovery/discovered-stacks/)
- [Migrating from AWS CloudFormation](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/)
- [The `pulumi import` guide](/docs/iac/guides/migration/import/)
