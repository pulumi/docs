---
title: Discovered Stacks
title_tag: "Discovered Stacks | Pulumi Insights"
h1: Discovered Stacks
meta_desc: Discovered Stacks model your CloudFormation stacks and ARM deployments as Pulumi stacks, with a seamless path to Pulumi IaC.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: Discovered Stacks
    parent: insights-discovery
    identifier: insights-discovery-discovered-stacks
    weight: 45
aliases: []
---

Discovered Stacks bring the infrastructure you manage outside of Pulumi into the same stack model that Pulumi IaC uses. When [Pulumi Insights Discovery](/docs/insights/discovery/) scans your cloud accounts, it recognizes AWS CloudFormation stacks and Azure Resource Manager (ARM) deployments and represents each one as a discovered stack in Pulumi Cloud, preserving the grouping the source tool already gave them.

A discovered stack looks and navigates like any other Pulumi stack: it appears on the Stacks page, lists its resources, and shows per-resource detail. Every resource also carries a [migration status](#migration-statuses), so a discovered stack doubles as a live, auditable record of how far along you are in [migrating it to Pulumi](/docs/insights/discovery/discovered-stacks/migrate/).

<!-- TODO: screenshot — Stacks page with the "Show Discovered Stacks" toggle on, discovered stacks listed alongside IaC stacks with the chip visible. Capture from an org with the flag enabled; add 1px border. -->

## Sources

Discovered stacks are created automatically — whenever a scanned account contains resources managed by a supported external IaC provider, Discovery groups those resources into discovered stacks with no additional setup:

- **AWS CloudFormation**: each CloudFormation stack becomes a discovered stack. For CDK applications, the synthesized CloudFormation stacks are discovered.
- **Azure Resource Manager**: each ARM or Bicep deployment becomes a discovered stack, preserving deployment-level grouping.

Pulumi-hosted Terraform stacks are not represented as discovered stacks — their state is already authoritative in Pulumi Cloud — but they share the same migration experience through the **Migration** tab. See [Migrate from a Discovered Stack](/docs/insights/discovery/discovered-stacks/migrate/#terraform-stacks).

To set up scanning, see [Create and manage Insights accounts](/docs/insights/discovery/accounts/).

## Naming

Discovered stacks are named automatically, so the same source stack found in different accounts, regions, or resource groups produces distinct, recognizable names. The **project** name is inferred from the source stack, and the **stack** name combines the Insights account name with the scope the source was found in:

- **CloudFormation**: `<account>-<region>` — the Insights account name and the AWS region.
- **Azure Resource Manager**: `<account>-<resource-group>` — the Insights account name and the resource group.

## Discovered stacks in the console

On the **Stacks** page, turn on **Show Discovered Stacks** to list discovered stacks alongside your IaC stacks. They support the same filtering, sorting, and click-through, and are marked with a chip that identifies them as discovered. Tabs that only apply to IaC stacks, such as deployments and updates, are hidden.

Because a discovered stack's resources come from an external source, each resource carries two type identifiers:

- **Pulumi type**: how the resource is represented in Pulumi's model, such as `aws:s3/bucket:Bucket`.
- **Origin type**: the type in the source system, such as `AWS::S3::Bucket` for CloudFormation or `Microsoft.Storage/storageAccounts` for ARM.

The resource list shows both columns, and the resource detail page shows **Origin Properties** — the properties as reported by the source — alongside the properties in Pulumi's model, so you can compare the two representations directly.

<!-- TODO: screenshot — discovered stack resource list showing Pulumi type, origin type, and migration status columns. -->

## Migration statuses

Every resource in a discovered stack has a migration status computed by Pulumi Cloud. Statuses are derived from the discovered state and, when a target Pulumi stack exists, from a comparison against that stack's state — they are never set by hand.

| Status | Meaning | Recommended next step |
| --- | --- | --- |
| `Ready` | The resource maps to a Pulumi type, and Discovery confirmed it exists in the cloud. | Import it. This is the bulk of a typical migration. |
| `Pending` | The resource maps to a Pulumi type, but Discovery could not confirm its current state. It may have been deleted, or the mapping may be imperfect. | Verify the resource still exists, then import it or ignore it. |
| `Unmapped` | No Pulumi type mapping was found. Common examples are CloudFormation custom resources and inline IAM policies that Pulumi models as part of their parent resource. | Review it. Many unmapped resources are covered by the migration of a parent resource; ignore them once the parent is migrated. |
| `NotApplicable` | The resource is a container or wrapper construct, such as `AWS::CloudFormation::Stack` or `Microsoft.Resources/deployments`, with no cloud resource of its own to migrate. | None. |
| `Migrated` | The resource was found in the target Pulumi stack. It is under Pulumi management. | None. |
| `PulumiOnly` | The resource exists in the target Pulumi stack but has no discovered counterpart — typically a pre-existing resource, or one created with a corrected type mapping. | Review it; usually no action is needed. |

The status breakdown is visible at the stack level, and every source resource appears as a row with an explicit status — the count of discovered resources always reconciles against the statuses, so nothing silently disappears during a migration.

## Ignoring resources

Statuses are computed, but one decision is yours to make: excluding a resource from the migration. **Ignore** a resource when it has nothing left to import on its own — it was deleted, it is an inline definition covered by its parent's migration, or it has no Pulumi equivalent you need. Ignored resources stay visible in the list but are excluded from the migration accounting, and the decision persists for everyone looking at the stack.

Together with the computed statuses, this keeps the record complete: every resource is either migrated or deliberately ignored — never quietly forgotten.

<!-- TODO: confirm the Ignore action's label and placement in the shipped UI, and how ignored resources are displayed. -->

## Next steps

- [Migrate from a Discovered Stack](/docs/insights/discovery/discovered-stacks/migrate/)
- [Create and manage Insights accounts](/docs/insights/discovery/accounts/)
- [Migrating from AWS CloudFormation](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/)
