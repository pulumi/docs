---
title: Migrate from a Discovered Stack
title_tag: "Migrate from a Discovered Stack | Pulumi Insights"
h1: Migrate from a Discovered Stack
meta_desc: Migrate CloudFormation and ARM resources from a discovered stack to Pulumi IaC with Neo, generated code, or your own agent, verified by a zero-diff preview.
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

1. Every discovered resource is either imported or deliberately ignored.
1. `pulumi preview` on the target stack reports no changes, proving the code matches the cloud state.
1. The program lands in your repository as the new source of record — from here on, changes to those resources happen through Pulumi.

## Before you begin

- A discovered stack, created by an [Insights account scan](/docs/insights/discovery/accounts/) of the cloud account that holds your CloudFormation or ARM resources.
- A git repository where the generated Pulumi program will live.
- Cloud credentials that match the source account, ideally through a [Pulumi ESC environment](/docs/esc/).

## Start a migration

From a discovered stack, the **Actions** menu offers three ways in:

<!-- TODO: verify the shipped Actions menu labels (Migrate with Neo / Generate Code / Generate Import Commands) match the UI before publishing. -->

- **Migrate with Neo** (recommended): [Pulumi Neo](/docs/ai/) runs the whole workflow — it fetches the discovered resources, imports them, reconciles the preview, and opens a pull request with a migration report.
- **Generate Code**: produce a Pulumi program from the discovered resource state, which you integrate and verify yourself.
- **Generate Import Commands**: produce the corresponding [`pulumi import`](/docs/iac/guides/migration/import/) commands to run in your own terminal.

All three paths work against the same resource data and statuses, so you can also drive a migration with your own coding agent or entirely by hand — the console reflects progress the same way regardless of who does the work.

## How a migration works

Whether Neo runs it or you do, a migration follows the same arc:

1. **Triage.** Fetch the discovered resources and review the status breakdown. Resources marked `Ready` are importable now; `Pending` and `Unmapped` resources get resolved along the way (see [below](#resolve-pending-and-unmapped-resources)).
1. **Import.** Bring resources into the target stack with `pulumi import --generate-code`, appending the generated code to your program. `pulumi import` writes state as it goes, so migration statuses in the console update live as resources land in the target stack.
1. **Reconcile.** Run `pulumi preview` and fix the code until it reports no changes. A clean preview is the quality gate: it proves the program matches the actual cloud state. Never run `pulumi up` to make a diff go away — that changes the cloud to match the code, when the goal is the opposite.
1. **Review.** Open a pull request with the program and a migration report: status counts, the resource mapping table, and any resources that were ignored and why.

{{% notes "info" %}}
No `pulumi up` is required to complete a migration. `pulumi import` already syncs the imported state to Pulumi Cloud; from then on, you use `pulumi up` for ordinary changes to the now-managed resources.
{{% /notes %}}

## Resolve Pending and Unmapped resources

Some resources need a decision before the accounting is complete. Resolve each one by importing it or by [ignoring it](/docs/insights/discovery/discovered-stacks/#ignoring-resources) — either way, the outcome shows up in the console and persists across sessions.

**`Pending` resources** are mapped but unconfirmed. Attempting the import is usually the fastest way to find out why:

- **The resource was deleted.** The import fails because the resource does not exist. Ignore it — there is nothing left to migrate.
- **The type mapping is imperfect.** Some source types have more than one valid Pulumi mapping. Import with the corrected type; the imported resource then appears as `PulumiOnly`, and you ignore the origin resource in its favor.
- **The resource is fine.** The import succeeds and the status flips to `Migrated` on its own.

**`Unmapped` resources** have no direct Pulumi type. Most fall into known patterns:

- **Inline definitions**, such as an IAM policy that Pulumi models as a property of its parent role. Once the parent is migrated, ignore the child.
- **Implicit links**, such as a secret-to-target attachment that Pulumi expresses through the target's configuration. Ignore it once the target resource is migrated.
- **Custom resources**, such as CloudFormation `Custom::*` types backed by a Lambda function. Review what the handler does and decide whether to replace it with a Pulumi equivalent or ignore it.

## Migrate incrementally

You do not have to migrate a discovered stack in one sitting. Select a subset of resources, land it, and come back later — statuses are computed from the actual target stack state and ignore decisions persist, so the picture is current whenever you return, for you and for anyone else looking at the same stack. A large migration becomes a sequence of small, reviewable pull requests instead of one risky cutover.

## Terraform stacks

Pulumi-hosted Terraform stacks are not discovered stacks — Pulumi Cloud already holds their state — but they get the same migration experience through a **Migration** tab on the stack. Origin types show the Terraform types, such as `aws_s3_bucket`, and statuses are derived from the state conversion. The workflow from there is identical: triage, import, zero-diff preview, pull request.

## Use the API

The migration data is available through the Pulumi Cloud REST API, which is what Neo and other agents use. The API is in preview and may change.

List a discovered stack's resources, including migration statuses. Pass `compareTo` to compute statuses against a target Pulumi stack:

```bash
GET /api/preview/insights/{org}/discovered-stacks/{project}/{stack}/resources?compareTo={targetProject}/{targetStack}
```

## Next steps

- [Discovered Stacks](/docs/insights/discovery/discovered-stacks/)
- [Migrating from AWS CloudFormation](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/)
- [The `pulumi import` guide](/docs/iac/guides/migration/import/)
