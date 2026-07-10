---
title_tag: "Protecting against undesired changes | Pulumi Operations"
meta_desc: Production hygiene for Pulumi. Protect critical resources from deletion and review previews before applying changes to important environments.
title: Protecting against undesired changes
h1: Protecting against undesired changes
menu:
    iac:
        name: Protecting against undesired changes
        parent: iac-operations-stack-management
        weight: 5
aliases:
- /docs/iac/operations/stack-management/production-hygiene/
---

By default, `pulumi up` reconciles your entire stack: the engine compares the program's desired state to the stack's current state and creates, updates, or deletes resources until the two match. This whole-stack model is safe and predictable for most changes. But some resources, such as production databases, object storage, and DNS zones, hold data or serve traffic that you can't afford to lose to an accidental delete or replace, and some environments warrant a closer look before any change lands.

This guide brings together the safeguards Pulumi provides for exactly those situations. Think of it as production hygiene: a set of guardrails you apply to the resources and environments that matter most, so a routine change to one part of a stack can never quietly take out something critical.

## Protect critical resources from deletion

The [`protect`](/docs/iac/concepts/resources/options/protect/) resource option marks a resource as protected. A protected resource cannot be deleted directly, and any deployment that would delete it (including a replacement) fails with an error instead. Apply it to stateful, hard-to-recreate resources such as databases and storage buckets.

Rather than hard-code `protect: true`, drive it from [stack configuration](/docs/iac/concepts/config/) so that production stacks protect the resource while development stacks can still be torn down freely:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const config = new pulumi.Config();
const shouldProtect = config.getBoolean("protect") ?? false;

const db = new Database("db", {}, { protect: shouldProtect });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
config = pulumi.Config()
should_protect = config.get_bool("protect") or False

db = Database("db", opts=ResourceOptions(protect=should_protect))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
conf := config.New(ctx, "")
shouldProtect := conf.GetBool("protect")

db, _ := NewDatabase(ctx, "db", &DatabaseArgs{}, pulumi.Protect(shouldProtect))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var config = new Config();
var shouldProtect = config.GetBoolean("protect") ?? false;

var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { Protect = shouldProtect });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var config = ctx.config();
var shouldProtect = config.getBoolean("protect").orElse(false);

var db = new Database("db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .protect(shouldProtect)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
config:
  protect:
    type: boolean
    default: false
resources:
  db:
    type: Database
    options:
      protect: ${protect}
```

{{% /choosable %}}

{{< /chooser >}}

Set the value per stack, so a production stack protects the database while a development stack leaves it deletable:

```bash
pulumi config set protect true --stack production
```

Child resources inherit `protect` from their [parent](/docs/iac/concepts/resources/options/parent/), so protecting a parent protects its children by default. When you genuinely need to remove a protected resource, unprotect it first, in one of two ways:

* Set `protect: false` and run `pulumi up`.
* Run [`pulumi state unprotect`](/docs/iac/cli/commands/pulumi_state_unprotect/) against the resource's URN.

Pulumi has no single flag to protect every resource in a stack. To apply `protect: true` across the board, use [stack transforms](/docs/iac/concepts/resources/options/transforms/#stack-transforms) to set the option on every resource as it's registered.

## Retain data on delete

Where `protect` refuses to delete a resource, [`retainOnDelete`](/docs/iac/concepts/resources/options/retainOnDelete/) takes the opposite approach: it lets Pulumi remove the resource from state without calling the provider's delete, leaving the underlying cloud resource in place. It's the right choice when you want to stop managing a resource with Pulumi, or hand it off, without destroying its data:

```typescript
const db = new Database("db", {}, { retainOnDelete: true });
```

Use `protect` for resources you never want deleted, and `retainOnDelete` for resources you may stop managing but want to preserve. A related option, [`deletedWith`](/docs/iac/concepts/resources/options/deletedwith/), skips a resource's own delete when another resource you name is being deleted anyway (for example, a resource inside a resource group that's torn down as a unit).

## Review previews before applying

[`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) shows exactly what an update would do without changing anything. Reading the preview before every apply to a critical environment is the single most effective habit for catching undesired changes, especially replacements, which show as a `+-` step and often imply data loss, and deletes, which show as a `-` step.

A few flags make previews more useful as a gate:

* `--diff` renders a rich, property-level diff of every change.
* `--refresh` refreshes state from the provider first, so the preview accounts for any out-of-band drift.
* `--expect-no-changes` exits with an error if any change is proposed, which is ideal for asserting that a protected environment is exactly in sync in CI.

## Lock in a reviewed plan with update plans

A preview tells you what *would* happen; an [update plan](/docs/iac/operations/stack-management/update-plans/) makes the next apply do *only* that. Save the operations from a preview and constrain a later update to them:

```bash
pulumi preview --save-plan=plan.json
pulumi up --plan=plan.json
```

If the update would perform any operation not in the saved plan, it fails instead. This is valuable in organizations with strict approval processes: the plan reviewed and approved is provably the plan applied.

{{% notes type="warning" %}}
Update plans capture the operations known at preview time. Values that are only computed during the apply (outputs of other resources, provider-assigned IDs) aren't fully known when the plan is generated, so a plan can't guarantee byte-for-byte identical inputs. Treat plans as a guardrail on *which* operations run, not a freeze of every value.
{{% /notes %}}

## Scope risky changes with targeted updates

When you must make a surgical change and want to be certain nothing else moves, [targeted updates](/docs/iac/operations/stack-management/targeted-updates/) limit an operation to specific resources with `--target`, `--target-replace`, and `--exclude`.

{{% notes type="warning" %}}
Targeted operations are an escape hatch. Because the engine reconciles only a subset of the stack, the deployed infrastructure can drift from what the program describes. Use them for one-off interventions and return to whole-stack operations as soon as you can.
{{% /notes %}}

## Catch drift

Undesired changes don't only come from your program. Someone can also modify a resource out of band, in the cloud console or another tool. [Drift detection](/docs/iac/operations/stack-management/drift/) surfaces that divergence: `pulumi refresh` updates state to match the provider, and a subsequent preview shows what your program would change back. Refreshing before a critical apply ensures the preview reflects reality, not a stale snapshot.

## Enforce guardrails with policy as code

The safeguards above are opt-in per resource or per run. [Policy as code](/docs/insights/policy/) makes them enforceable across every stack automatically. A policy pack can, for example, block the deletion of any resource tagged `environment: production`, require encryption on storage, or fail an update that violates your organization's standards, and it's evaluated on every `pulumi preview` and `pulumi up`. Wire policy packs into your pipeline so the rules apply consistently; see [policy in CI/CD](/docs/insights/policy/ci-cd/).

## Gate previews in CI/CD

The most durable place to enforce review is your pipeline. A common pattern is to run `pulumi preview` on every pull request, comment the resulting diff on the PR for reviewers, and require an approval before `pulumi up` runs against a protected environment. Pulumi's [continuous delivery](/docs/iac/operations/continuous-delivery/) integrations support this across platforms; the [GitHub Actions](/docs/iac/operations/continuous-delivery/github-actions/) guide shows a trunk-based workflow that previews on PRs and applies on merge.

## Putting it together

No single option makes a stack safe on its own. Production hygiene is layered. Use `protect` and `retainOnDelete` to guard individual resources, previews and update plans to give yourself a checkpoint before every apply, targeted updates and drift detection to keep surgical changes contained, and policy as code plus CI/CD gating to make the whole thing enforceable instead of optional. Start with `protect` on your most critical resources and a habit of reading previews, then layer on the heavier guardrails as the cost of a mistake grows.
