---
title: Migrate from a Discovered Stack
title_tag: "Migrate from a Discovered Stack | Pulumi Insights"
h1: Migrate from a Discovered Stack
meta_desc: Migrate CloudFormation and ARM resources from a discovered stack to Pulumi IaC with Neo, import commands, or your own agent, verified by a zero-diff preview.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: Migrate to Pulumi
    parent: insights-discovery-discovered-stacks
    weight: 10
aliases: []
---

Migrating from a [discovered stack](/docs/insights/discovery/discovered-stacks/) means bringing its resources under Pulumi management: a Pulumi program in your repository whose state matches the cloud exactly. The console is where you plan the migration, decide what to include, and track progress — the migration itself completes as code and CLI operations in your own repository.

A migration is done when three things are true:

1. Every discovered resource is either imported or deliberately resolved.
1. `pulumi preview` on the target stack reports no changes, proving the code matches the cloud state.
1. The program lands in your repository as the new source of record — from here on, changes to those resources happen through Pulumi.

## Before you begin

- A discovered stack, created by an [Insights account scan](/docs/insights/discovery/accounts/) of the cloud account that holds your CloudFormation or ARM resources.
- A git repository where the generated Pulumi program will live.
- Cloud credentials that match the source account, ideally through a [Pulumi ESC environment](/docs/esc/).

## Start a migration

From a discovered stack, the **Actions** menu offers two ways in:

- **Migrate with Neo** (recommended): [Pulumi Neo](/docs/ai/) runs the whole workflow — it fetches the discovered resources, imports them, reconciles the preview, and opens a pull request with a migration report.
- **Generate Import Commands**: produce the corresponding [`pulumi import`](/docs/iac/guides/migration/import/) commands to run in your own terminal.

Both paths work against the same resource data and statuses — and all of it is exposed through a [REST API](#use-the-api). So you can run the whole flow locally — reading resources and their statuses, driving the imports, and recording decisions — and the console reflects the progress. A reusable Pulumi agent skill that packages this workflow will be published.

## Set up your local project

**Migrate with Neo** scaffolds and wires up the project for you, so you can skip this section. If you chose **Generate Import Commands**, or you're driving the migration with your own agent, you first connect a local Pulumi project to the stack you created in the console — the import commands assume that project already exists.

```bash
# Create a stack
pulumi stack init <stackName>
```

Set cloud credentials the way you would for any Pulumi program — a [Pulumi ESC environment](/docs/esc/) is the most reliable. With the project attached, run the generated import commands and continue below.

## How a migration works

Whether Neo runs it or you do, a migration follows the same arc:

1. **Triage.** Fetch the discovered resources and review the status breakdown. Resources marked **Ready** are importable now; **Not found** and **No exact match** resources get resolved along the way (see [below](#resolve-not-found-and-no-exact-match-resources)).
1. **Import.** Bring resources into the target stack with `pulumi import --generate-code`, appending the generated code to your program. `pulumi import` writes state as it goes, so migration statuses in the console update live as resources land in the target stack.
1. **Reconcile.** Run `pulumi preview` and fix the code until it reports no changes. A clean preview is the quality gate: it proves the program matches the actual cloud state. Never run `pulumi up` to make a diff go away — that changes the cloud to match the code, when the goal is the opposite. Freshly imported code often shows a diff on the first preview even when nothing in the cloud changed; see [Tips for a clean migration](#tips-for-a-clean-migration) for the common ones and how to clear them.

{{% notes "info" %}}
No `pulumi up` is required to complete a migration. `pulumi import` already syncs the imported state to Pulumi Cloud; from then on, you use `pulumi up` for ordinary changes to the now-managed resources.
{{% /notes %}}

## Resolve Not found and No exact match resources

Some resources need a decision before the accounting is complete. Resolve each one by importing it or by [marking it resolved](/docs/insights/discovery/discovered-stacks/#resolving-resources) — either way, the outcome shows up in the console and persists across sessions.

**Not found** resources are mapped but unconfirmed — sometimes deleted, sometimes simply a type whose live state Discovery doesn't verify (a log group, for example), in which case the resource is really there. Attempting the import is usually the fastest way to find out which:

- **The resource was deleted.** The import fails because the resource does not exist. Mark it resolved — there is nothing left to migrate.
- **The type mapping is imperfect.** Some source types have more than one valid Pulumi mapping. Import with the corrected type and resolve the origin resource in its favor.
- **The resource is fine.** The import succeeds and the status flips to **Migrated** on its own after the corresponding `pulumi preview`.

**No exact match** resources have no direct Pulumi type. Most fall into a handful of familiar patterns:

- **Inline definitions**, such as an IAM policy that Pulumi models as a property of its parent role. Once the parent is migrated, mark the child resolved.
- **Implicit links**, such as a secret-to-target attachment that Pulumi expresses through the target's configuration. Mark it resolved once the target resource is migrated.
- **Custom resources**, such as CloudFormation `Custom::*` types backed by a Lambda function. Review what the handler does and decide whether to replace it with a Pulumi equivalent or mark it resolved.

## Tips for a clean migration

These apply whether Neo drives the migration or you do. They're the difference between a preview that goes clean in one pass and one that fights you.

### Import in small, verifiable batches

Import a coherent group of resources, get its preview clean, then move to the next — rather than importing everything at once. Grouping by the source construct works well: for CDK stacks, the construct path; for CloudFormation, the logical stack or a resource-type prefix. Keeping batches to roughly 20 resources keeps each preview easy to read.

Import the **Ready** resources first. A single resource that can't be imported — a deleted resource, or one whose import ID is wrong — aborts an entire `pulumi import --file` batch, so keep unconfirmed **Not found** resources out of the bulk import and handle them one at a time.

### Clear a noisy preview

Work through the first preview by the shape of each change:

- **A property the cloud has but your code doesn't set** — add it to the code with the real value.
- **A property your code sets that the cloud never returns** — usually a provider default for a write-only or delete-time field (for example `recoveryWindowInDays` on a Secrets Manager secret, or `confirmationTimeoutInMinutes` on an SNS subscription). These can never match the imported state, so silence them with [`ignoreChanges`](/docs/iac/concepts/resources/options/ignorechanges/):

  ```typescript
  new aws.secretsmanager.Secret("db-secret", { /* ...imported inputs... */ }, {
      ignoreChanges: ["recoveryWindowInDays"],
  });
  ```

- **A value mismatch** — query the cloud for the real value and set it in code.

Generated code is occasionally invalid — for instance an empty nested block the provider rejects. When a block has no real value in the cloud, removing it is usually the fix. Reserve `ignoreChanges` for genuinely provider-managed fields; don't use it to hide a value you can set correctly.

### Link an imported resource to its origin

Importing a **Not found** resource can produce a new **Existing** entry while the original stays **Not found** — and this is the common case, not an edge one. Because the origin's state was never confirmed, the console can't automatically match the imported resource back to it (importing with a corrected type does the same thing). [Mark the origin resolved](/docs/insights/discovery/discovered-stacks/#resolving-resources) and link it to the **Existing** entry: that pairs the source with the resource you migrated it into — with a comment, if you want to record why — and keeps the accounting clean.

### Reorganize the generated code safely

Generated code is flat — every resource at the top level, with hardcoded IDs and no cross-references. Restructuring it (grouping resources into a [component](/docs/iac/concepts/components/), splitting files, replacing literal IDs with references) is worthwhile, but do it *after* the preview is clean, and re-run `pulumi preview` after each change so the zero-diff never breaks.

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

A clean preview after the move — no replacements or deletions — confirms the alias worked.

## Migrate incrementally

You do not have to migrate a discovered stack in one sitting. Select a subset of resources, land it, and come back later — statuses are computed from the actual target stack state and your resolutions persist, so the picture is current whenever you return, for you and for anyone else looking at the same stack. A large migration becomes a sequence of small, reviewable pull requests instead of one risky cutover.

## Terraform stacks

Pulumi-hosted Terraform stacks are not discovered stacks — Pulumi Cloud already holds their state — but they get the same migration experience through a **Migration** tab on the stack. Origin types show the Terraform types, such as `aws_s3_bucket`, and statuses are derived from the state conversion. The workflow from there is identical: triage, import, zero-diff preview, pull request.

## Use the API

The migration data is available through the Pulumi Cloud REST API, which is what Neo and other agents use. The API is in preview and may change.

List a discovered stack's resources, including migration statuses. Pass `compareTo` to compute statuses against a target Pulumi stack:

```bash
GET /api/preview/insights/{org}/discovered-stacks/{project}/{stack}/resources?compareTo={targetProject}/{targetStack}
```

Each resource's `migrationStatus` field carries the raw status token — `Ready`, `NotFound`, `NoMatch`, `Migrated`, `PulumiOnly`, or `NotApplicable` — corresponding to the **Ready**, **Not found**, **No exact match**, **Migrated**, **Existing**, and **Not applicable** labels shown in the console.

For a Pulumi-hosted **Terraform** stack, the equivalent endpoint returns the converted resources and their statuses:

```bash
GET /api/preview/insights/{org}/stacks/{project}/{stack}/migration?compareTo={targetProject}/{targetStack}
```

Decisions are written back through the same API — [marking a resource resolved](/docs/insights/discovery/discovered-stacks/#resolving-resources), with an optional comment and a link to the target-stack resource — so an agent can drive an entire migration end to end without the console:

```bash
PUT /api/preview/insights/{org}/discovered-stacks/{project}/{stack}/migration
```

## Next steps

- [Discovered Stacks](/docs/insights/discovery/discovered-stacks/)
- [Migrating from AWS CloudFormation](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/)
- [The `pulumi import` guide](/docs/iac/guides/migration/import/)
