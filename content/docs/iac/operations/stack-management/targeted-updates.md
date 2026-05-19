---
title_tag: "Targeted updates | Pulumi Guides"
meta_desc: Learn how to use --target, --exclude, and --target-replace to limit which resources Pulumi operates on, and what trade-offs each approach involves.
title: Targeted updates
h1: Targeted updates
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Targeted updates
        parent: iac-operations-stack-management
        weight: 10
aliases:
- /docs/iac/guides/basics/targeted-updates/
---

By default, `pulumi up`, `pulumi preview`, `pulumi refresh`, and `pulumi destroy` operate on the entire stack. The Pulumi engine compares the program's desired state to the stack's current state and reconciles every resource in one pass. This is the recommended workflow because it keeps the program and the deployed infrastructure in sync.

Sometimes you need finer control. You might want to deploy one new resource without touching anything else, force the replacement of a single resource, or run a wide update while skipping a resource that's in a maintenance window. Targeted update flags let you narrow the set of resources an operation touches.

{{% notes type="warning" %}}
Targeted operations are an escape hatch. Because the engine reconciles only a subset of the stack, the deployed infrastructure can drift from what the program describes. Use targeted operations for one-off interventions and return to whole-stack operations as soon as you can.
{{% /notes %}}

## The flags at a glance

| Flag | Available on | What it does |
| - | - | - |
| `--target` | `up`, `preview`, `refresh`, `destroy` | Restricts the operation to only the resources whose URNs match. |
| `--target-dependents` | `up`, `preview`, `refresh`, `destroy` | Also includes resources that depend on a targeted resource. |
| `--target-replace` | `up`, `preview` | Shorthand for `--target <URN> --replace <URN>`. Restricts the operation to the named resource and forces its replacement. |
| `--exclude` | `up`, `preview`, `refresh`, `destroy` | Operates on the whole stack except the resources whose URNs match. |
| `--exclude-dependents` | `up`, `preview`, `refresh` | Also excludes resources that depend on an excluded resource. |
| `--replace` | `up`, `preview` | Forces replacement of the named resources, but does not restrict the operation to them. The rest of the stack is still reconciled. |

All flags that accept a URN can be passed multiple times.

## Specifying resources

Targeted flags accept resource URNs. A URN identifies one resource uniquely and looks like this:

```text
urn:pulumi:dev::my-project::aws:s3/bucket:Bucket::my-bucket
```

The segments are: stack name, project name, resource type, and resource name. To list the URNs in a stack, run:

```bash
pulumi stack --show-urns
```

### Wildcards

Both `--target` and `--exclude` accept wildcards in URN patterns:

- `*` matches any characters within a single URN segment (it does not cross `:` separators).
- `**` matches any characters across segments.

Quote wildcard patterns so your shell doesn't expand them. A few examples:

```bash
# Match every resource whose name is "my-bucket", in any project or stack.
pulumi up --target 'urn:pulumi:**::**::**::my-bucket'

# Match every S3 bucket in the stack.
pulumi up --target 'urn:pulumi:dev::my-project::aws:s3/bucket:Bucket::*'

# Exclude every resource under the "drafts" component.
pulumi up --exclude 'urn:pulumi:**::**::**::drafts' --exclude-dependents
```

URNs without wildcards must match a resource's URN character-for-character. Short resource names alone are not accepted.

## How targeting interacts with the dependency graph

By default, `--target` operates only on the resources whose URNs you list. Resources that depend on a targeted resource — or that a targeted resource depends on — are left in their existing state.

When a targeted resource needs an input from a non-targeted resource (for example, the ID of a VPC it lives in), the engine uses the value stored in the stack's state from the last update. This means your targeted update sees the *recorded* state of the wider stack, not what the program would produce if it ran end-to-end.

`--target-dependents` opts you into pulling dependent resources into the operation. For example, if you target a VPC and pass `--target-dependents`, every subnet, security group, and instance whose declaration depends on the VPC is also included.

`pulumi destroy` treats dependents more strictly than the other commands. If a targeted resource has dependents and you don't pass `--target-dependents`, the operation fails: deleting the resource would leave the stack in an inconsistent state. Pass `--target-dependents` to destroy the resource and its dependents together.

## When to use `--target` vs. `--exclude`

Use `--target` when you want to operate on a *small* number of resources and leave the rest of the stack alone. Use `--exclude` when you want to operate on *most* of the stack but skip a few resources.

For example, deploying a single new resource is straightforward with `--target`:

```bash
pulumi up --target 'urn:pulumi:dev::my-project::aws:s3/bucket:Bucket::new-bucket'
```

But updating a stack with a hundred resources while skipping a single database under maintenance is much cleaner with `--exclude`:

```bash
pulumi up --exclude 'urn:pulumi:dev::my-project::aws:rds/instance:Instance::primary-db'
```

If you instead used `--target` for that update, you would have to enumerate every resource you wanted to include.

## Replacing a single resource

`--target-replace` is shorthand for `--target <URN> --replace <URN>`. It restricts the update to the named resource and forces Pulumi to delete and recreate it rather than updating it in place. Use it when you need to force a recreation of one resource without rolling the rest of the stack forward:

```bash
pulumi up --target-replace 'urn:pulumi:dev::my-project::aws:ec2/instance:Instance::web-server'
```

This is different from `--replace`, which forces replacement of the named resource but still reconciles the rest of the stack at the same time.

## Per-command behavior

The flags work the same way across `up`, `preview`, `refresh`, and `destroy`, with a few differences worth knowing:

- **`pulumi preview`** is the safest way to experiment with targeting. It shows you what an `up` with the same flags would change, without applying anything. Preview a targeted update before running it.
- **`pulumi refresh`** with `--target` updates the state of only the listed resources from the cloud provider. This is useful when you suspect drift in one resource and don't want to wait for a full-stack refresh.
- **`pulumi destroy`** with `--target` requires `--target-dependents` whenever the targeted resource has dependents in the stack. Without it, destroy aborts rather than leave dangling references in state.

## Limitations and trade-offs

Targeted operations are useful, but they introduce risks that whole-stack operations don't have:

- **Drift between code and infrastructure.** A targeted update applies only what its flags allow. Changes elsewhere in your program are deferred until the next full update. If the deferred changes are forgotten, the deployed stack will not match what the program describes.
- **Stale inputs.** When a targeted resource references a non-targeted resource, the engine uses the value in state from the last full update. If the non-targeted resource has changed in a way that the program now describes differently, the targeted resource may end up with stale input values.
- **Skipped dependents.** Without `--target-dependents`, a downstream resource keeps its old configuration even when an upstream resource changes. The next full update will surface those deferred changes.
- **Interaction with `--refresh`.** Passing `--refresh` alongside `--target` only refreshes the targeted resources before the update. Other resources are not refreshed, even if their state is stale.
- **Interaction with update plans.** A plan generated from a targeted preview only describes operations on the targeted resources. Applying that plan to a full `pulumi up` will fail because the plan and the program's full goal state will not match. Generate plans from full-stack previews when you intend to apply them to full-stack updates. See [Update plans](/docs/iac/operations/stack-management/update-plans/) for more.

If you find yourself reaching for targeted operations regularly, consider splitting the stack into smaller stacks instead. Smaller stacks give you the same locality without the drift risk — whole-stack operations on a smaller stack are safer than targeted operations on a large one. See [Organizing projects and stacks](/docs/iac/guides/basics/organizing-projects-stacks/) for guidance.

## Examples

### Deploy a single new resource

You've added one new bucket to a large program and want to deploy only it:

```bash
pulumi up --target 'urn:pulumi:dev::my-project::aws:s3/bucket:Bucket::reports'
```

Pulumi will create the bucket and leave the rest of the stack untouched.

### Destroy a component and everything under it

A component groups a feature's resources together. To tear the whole feature down in one command, target the component and pass `--target-dependents`:

```bash
pulumi destroy \
  --target 'urn:pulumi:dev::my-project::myorg:feature:Drafts::drafts' \
  --target-dependents
```

Every child of the `drafts` component is destroyed alongside the component itself.

### Skip a stateful resource during a wide update

You're rolling out application changes across a stack but the primary database is in a maintenance window. Exclude it from the update:

```bash
pulumi up \
  --exclude 'urn:pulumi:dev::my-project::aws:rds/instance:Instance::primary-db'
```

Every other resource is reconciled. Run the same update without `--exclude` once the maintenance window closes to bring the database back in sync with the program.

### Force recreation of one resource

A configuration value is baked into a resource at creation time and an in-place update won't pick it up. Force the resource to be replaced without disturbing anything else:

```bash
pulumi up --target-replace 'urn:pulumi:dev::my-project::aws:ec2/instance:Instance::web-server'
```

## See also

- [`pulumi up`](/docs/iac/cli/commands/pulumi_up/), [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/), [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/), and [`pulumi destroy`](/docs/iac/cli/commands/pulumi_destroy/) command references.
- [Update plans](/docs/iac/operations/stack-management/update-plans/) for constraining an update to a pre-approved set of operations.
- [Organizing projects and stacks](/docs/iac/guides/basics/organizing-projects-stacks/) for splitting infrastructure when targeted operations become routine.
