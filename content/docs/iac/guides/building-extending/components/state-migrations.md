---
title: State migrations
title_tag: Component state migrations | Pulumi Docs
meta_desc: Use state migration callbacks to evolve a Pulumi component’s internal resources while preserving existing cloud infrastructure.
menu:
  iac:
    identifier: iac-guides-components-state-migrations
    parent: iac-guides-components
    weight: 40
---

State migrations let you evolve a [component's](/docs/iac/concepts/components/) internal resources while preserving the infrastructure it already manages. Attach a migration callback to the component to translate its saved [state](/docs/iac/concepts/state-and-backends/) and the state of its children into the representation expected by the new implementation. Pulumi runs the migration before calculating resource changes.

{{% notes type="info" %}}
The state migrations API is **experimental** and may change.

Share feedback in the [component state migrations discussion](https://github.com/pulumi/pulumi/discussions/24799).

{{% /notes %}}

## When to use a state migration

Use a state migration when a component upgrade needs to translate its children's saved properties or reorganize resources that already represent the same physical infrastructure. Keep the migration in the component implementation so consumers can upgrade the component without editing their stack state manually.

For simpler changes, use the corresponding resource option:

| Change | Mechanism |
| --- | --- |
| Rename a resource or change its parent while retaining compatible state | [Aliases](/docs/iac/concepts/resources/options/aliases/) |
| Transform resource inputs or options as the program registers resources | [Transforms](/docs/iac/concepts/resources/options/transforms/) |
| Bring an existing cloud resource under Pulumi management | [Import](/docs/iac/guides/migration/import/) |
| Translate saved properties or merge state entries during a component upgrade | State migrations |

A migration rewrites state only. It does not create, import, update, or delete cloud resources. After the migration, Pulumi compares the updated program with the migrated state and performs any remaining provider operations normally. An incorrect translation can still lead to an unwanted update or replacement, so review the preview before applying it.

## Write a migration callback

A component state migration is a pure function that transforms the saved state of a component and its children into the state expected by a new component version. It returns the updated state records and successor mappings for any changed URNs, or no result if no migration is needed.

The [option reference](/docs/iac/concepts/resources/options/statemigrations/#callback-api) explains the callback API. The state entries use the [checkpoint resource format](https://pulumi-developer-docs.readthedocs.io/latest/docs/references/deployment-schema.html#pulumi-resource-state), including fields such as `urn`, `type`, `id`, `parent`, `provider`, `inputs`, and `outputs`.

Return the **complete** migrated subtree, including the component and unchanged descendants. For every resource in the callback's input, do exactly one of the following:

- Return it under the same URN, with any desired state changes.
- Omit its old URN and map that URN to a successor present in the returned state.

Several old URNs can map to one successor. A resource cannot both remain in the result and have a successor mapping, and a mapping cannot point to a resource outside the result. Express state renames through successors rather than adding aliases to returned checkpoint entries.

Write callbacks that recognize the old representation and return no result when it's already migrated. Keep earlier callbacks when publishing later migrations so users can upgrade from older component versions. Reject unexpected state rather than guessing how to translate it.

### Preserve identity and secrets

For managed custom resources, a successor must preserve the physical ID, provider reference, extension reference, ownership, and lifecycle flags. When merging resources, preserve `protect` and `retainOnDelete` if either predecessor has them. Provider resource entries must remain unchanged. A migration cannot introduce a new managed physical object by inventing an ID.

The returned state must form a valid subtree, with unique URNs and resolvable structural references. When changing a resource type, update both its `type` field and the type in its URN. Preserve fields you are not intentionally translating, and copy maps before editing them.

{{% notes type="warning" %}}
Callbacks receive decrypted secret values inside their serialized secret envelopes. Preserve those envelopes and do not log state or include secret values in errors. Treat a callback as a pure state transformation: do not register resources, invoke providers, perform other Pulumi runtime operations, or wait for unresolved outputs.
{{% /notes %}}

## Example: upgrade a versioned bucket component

Consider a storage component with these two direct children:

- `aws:s3/bucketV2:BucketV2`, representing an S3 bucket.
- `aws:s3/bucketVersioningV2:BucketVersioningV2`, managing versioning for that same bucket.

The updated component registers one `aws:s3/bucket:Bucket` with inline versioning. Both old state entries have the same physical bucket ID and provider reference, which allows them to name the same successor.

The migration preserves the component and other descendants, converts the bucket's type and properties, and removes the separate versioning entry. Both old URNs map to the new bucket URN:

| Prior state entry | Returned state entry | Successor mapping |
| --- | --- | --- |
| Component | Unchanged component | None |
| `BucketV2` | `Bucket` with the same physical ID | Old bucket URN → new bucket URN |
| `BucketVersioningV2` | Omitted | Versioning URN → new bucket URN |

### Translate the saved state

The callbacks below implement this migration. Each translates both inputs and outputs. Each uses the separate versioning resource's outputs as the source of versioning settings and converts the bucket's plural singleton lists to the new resource's singular objects. These conversions are specific to the two AWS resource schemas, they are not a general conversion between arbitrary resource types.

{{< chooser language "typescript,python,go" >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3-state-migration" language="typescript" file="migration.ts" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3-state-migration" language="python" file="migration.py" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="aws-s3-state-migration" language="go" file="migration.go" >}}
```

{{% /choosable %}}

{{< /chooser >}}

### Register the migration

The component constructor attaches the callback and registers the new bucket as its child.

{{< chooser language "typescript,python,go" >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3-state-migration" language="typescript" file="component.ts" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3-state-migration" language="python" file="component.py" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="aws-s3-state-migration" language="go" file="component.go" >}}
```

{{% /choosable %}}

{{< /chooser >}}

The migration does not issue a provider delete for the omitted versioning entry. The new bucket resource takes responsibility for that configuration.

## How migrations run

1. During `pulumi preview` or `pulumi up`, Pulumi finds the component's prior state by URN or alias. If there is no prior state, it skips the callbacks.
1. Pulumi supplies the component itself first, followed by its descendants in snapshot order. This is the subtree defined by parent relationships, not every resource that depends on it.
1. Callbacks run in the order supplied. Each receives the state produced by earlier callbacks. A callback that returns no result leaves its input unchanged and allows later callbacks to run.
1. Pulumi validates the result and uses successor mappings to rewrite structural references and serialized resource references, including references from outside the subtree. Ordinary string values are not rewritten.
1. Pulumi diffs later resource registrations against the migrated state.

A preview evaluates the migration without saving it. An update persists the migration before proceeding with the affected resources. If a later operation fails, the migration may already be saved and callbacks must handle that state on the next run.

Migrations do not run during standalone refresh or destroy operations, including those using `--run-program`.

## Unit test a migration

Think of a migration as a `state[] → state[]` transformation, with successor mappings alongside the returned state. Unit testing it means supplying an array of prior state records, calling the callback directly, and comparing the returned array with the expected state. This can be tested without the Pulumi runtime, provider mocks, running stack, or cloud credentials.

These test sketches call the S3 migration directly with inline arrays of JSON-compatible state records. The expected array keeps the component and combines the bucket and versioning entries into one bucket entry with inline versioning. The sketches omit imports and the URN definitions; `...` comments stand for the remaining checkpoint fields, including parents, IDs, providers, and inputs. Include those fields in a runnable test.

{{< chooser language "typescript,python,go" >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3-state-migration" language="typescript" file="test-sketch.ts.txt" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3-state-migration" language="python" file="test-sketch.py.txt" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="aws-s3-state-migration" language="go" file="test-sketch.go.txt" >}}
```

{{% /choosable %}}

{{< /chooser >}}

The successor assertions check that both the old bucket and the versioning resource map to the new inline bucket’s URN. You can pass the migrated state back into the callback and assert that it returns no changes. Use a preview and update to verify how the engine and provider apply the complete component upgrade.

For a runnable TypeScript example, see the [AWSX VPC state migration](https://github.com/pulumi/examples/tree/master/aws-ts-awsx-vpc-state-migration). It upgrades a VPC from legacy AWSX to modern AWSX and then to plain AWS resources, preserving the existing AWS resource IDs. It includes migration callbacks, tests, and instructions for running each version against the same stack.

## Restrictions

State-changing migrations require a full update. Pulumi rejects them in these situations:

- Targeted or excluded updates, including `--target`, `--exclude`, and `--replace`.
- Generating or applying an update plan. Apply the migration without a saved plan before returning to a plan-based workflow.
- Pending operations in the snapshot. Resolve them with `pulumi refresh` before migrating.
- Resources pending deletion in the subtree. Complete the unfinished deletion with the migration returning no changes before retrying.
- Persisted snippet references that would need to change. Update or remove those snippets first.

A callback that returns no result can remain attached when using update plans or targeted updates, the restrictions on state-changing results do not require removing an already-applied migration.
