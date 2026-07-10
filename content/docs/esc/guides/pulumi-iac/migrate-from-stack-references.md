---
title_tag: Migrate from stack references to pulumi-stacks
title: Migrate from stack references to pulumi-stacks
h1: Migrate from stack references to the pulumi-stacks provider
meta_desc: Replace Pulumi StackReference resources with the ESC pulumi-stacks provider, feeding another stack's outputs into your program as ordinary configuration.
menu:
  esc:
    parent: esc-guides-pulumi-iac
    identifier: esc-guides-migrate-stack-references
    weight: 20
---

[Stack references](/docs/iac/concepts/stacks/#stackreferences) let one stack read another stack's outputs through the `StackReference` resource in your program. The ESC [`pulumi-stacks` provider](/docs/esc/providers/iac/pulumi-stacks/) does the same job from an environment instead: it reads another stack's outputs and exposes them to your program as ordinary [stack configuration](/docs/iac/concepts/config/). Your consuming program no longer instantiates a `StackReference` — it just reads config — and the cross-stack wiring lives in ESC, where it can be composed, pinned, and shared like any other configuration.

This guide shows how to migrate one consumer from `StackReference` to `pulumi-stacks`, then how to work through a chain of stacks safely.

{{< notes type="info" >}}
**This guide is for existing Pulumi IaC users** who already read outputs across stacks. If you haven't used ESC with Pulumi IaC before, read [Use with Pulumi IaC](/docs/esc/guides/pulumi-iac/) first.
{{< /notes >}}

## Prerequisites

- [Pulumi CLI](/docs/install/) installed
- A [Pulumi account](https://app.pulumi.com/signup) — ESC requires the [Pulumi Cloud backend](/docs/iac/concepts/state-and-backends/)
- Two stacks where one reads the other's outputs via `StackReference`

## The starting point

Suppose an application stack reads networking details from a `vpc-infra` stack using a `StackReference`:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const infra = new pulumi.StackReference("acmecorp/vpc-infra/prod");
const vpcId = infra.requireOutput("vpcId");
const publicSubnetIds = infra.requireOutput("publicSubnetIds");

// ... use vpcId and publicSubnetIds to create resources
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi

infra = pulumi.StackReference("acmecorp/vpc-infra/prod")
vpc_id = infra.require_output("vpcId")
public_subnet_ids = infra.require_output("publicSubnetIds")

# ... use vpc_id and public_subnet_ids to create resources
```

{{% /choosable %}}
{{% choosable language go %}}

```go
infra, err := pulumi.NewStackReference(ctx, "acmecorp/vpc-infra/prod", nil)
if err != nil {
    return err
}
vpcId := infra.RequireOutput(pulumi.String("vpcId"))
publicSubnetIds := infra.RequireOutput(pulumi.String("publicSubnetIds"))

// ... use vpcId and publicSubnetIds to create resources
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var infra = new StackReference("acmecorp/vpc-infra/prod");
var vpcId = infra.RequireOutput("vpcId");
var publicSubnetIds = infra.RequireOutput("publicSubnetIds");

// ... use vpcId and publicSubnetIds to create resources
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var infra = new StackReference("acmecorp/vpc-infra/prod");
Output<Object> vpcId = infra.requireOutput("vpcId");
Output<Object> publicSubnetIds = infra.requireOutput("publicSubnetIds");

// ... use vpcId and publicSubnetIds to create resources
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  infra:
    type: pulumi:pulumi:StackReference
    properties:
      name: acmecorp/vpc-infra/prod

variables:
  vpcId: ${infra.outputs["vpcId"]}
  publicSubnetIds: ${infra.outputs["publicSubnetIds"]}
```

{{% /choosable %}}

{{< /chooser >}}

The producer stack, `vpc-infra`, exports those values as [stack outputs](/docs/iac/concepts/stacks/#stack-outputs); nothing about the producer changes in this migration.

## Read the outputs through pulumi-stacks

Create (or edit) the environment that your application stack imports and add a `pulumi-stacks` block that pulls in the producer's outputs, then map them into `pulumiConfig`:

```yaml
# acmecorp/app/prod
values:
  stackRefs:
    fn::open::pulumi-stacks:
      stacks:
        vpcInfra:
          stack: vpc-infra/prod
  pulumiConfig:
    vpcId: ${stackRefs.vpcInfra.vpcId}
    publicSubnetIds: ${stackRefs.vpcInfra.publicSubnetIds}
```

The `stack` property takes the project-qualified stack name (`<project>/<stack>`); the outputs are read with no additional tokens or credentials. Confirm they resolve:

```bash
pulumi env open acmecorp/app/prod
```

If the application stack doesn't already import this environment, add it to `Pulumi.prod.yaml`:

```yaml
environment:
  - app/prod
```

## Update the consuming program

With the outputs arriving as configuration, replace the `StackReference` in your program with ordinary config reads:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const vpcId = config.require("vpcId");
const publicSubnetIds = config.requireObject<string[]>("publicSubnetIds");

// ... use vpcId and publicSubnetIds to create resources
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi

config = pulumi.Config()
vpc_id = config.require("vpcId")
public_subnet_ids = config.require_object("publicSubnetIds")

# ... use vpc_id and public_subnet_ids to create resources
```

{{% /choosable %}}
{{% choosable language go %}}

```go
conf := config.New(ctx, "")
vpcId := conf.Require("vpcId")
var publicSubnetIds []string
conf.RequireObject("publicSubnetIds", &publicSubnetIds)

// ... use vpcId and publicSubnetIds to create resources
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var config = new Pulumi.Config();
var vpcId = config.Require("vpcId");
var publicSubnetIds = config.RequireObject<string[]>("publicSubnetIds");

// ... use vpcId and publicSubnetIds to create resources
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var config = ctx.config();
var vpcId = config.require("vpcId");
var publicSubnetIds = config.requireObject("publicSubnetIds", List.class);

// ... use vpcId and publicSubnetIds to create resources
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
config:
  vpcId:
    type: string
  publicSubnetIds:
    type: array
    items:
      type: string
```

{{% /choosable %}}

{{< /chooser >}}

Use the accessor that matches each output's type: a string accessor (`require` / `Require`) for `vpcId`, an object accessor (`requireObject` / `RequireObject`) for the `publicSubnetIds` list, and a secret accessor (`requireSecret` / `RequireSecret`) for any value that was secret in the producer stack.

## Verify the migration is a no-op

The whole point is that the resources don't change — only where their inputs come from. Preview before applying:

```bash
pulumi preview --stack prod
```

The values feeding your resources are the same, so the plan should show no changes. Once you see a clean preview, run `pulumi up`, then delete the now-unused `StackReference` code.

{{< notes type="info" >}}
`StackReference.requireOutput` marks secret outputs as secret automatically. When you map an output that was secret through `pulumiConfig`, wrap it in [`fn::secret`](/docs/esc/concepts/secrets/) so it stays encrypted as it flows into your stack.
{{< /notes >}}

## Migrate a chain at scale

Real projects often have a chain of stacks — networking feeds a cluster, which feeds an application. Migrate it incrementally rather than all at once, and let each step prove itself with a no-op preview:

1. **Start at the end of the chain.** Begin with a stack that only *consumes* outputs and isn't referenced by anything downstream. Migrating a leaf consumer can't break anything upstream, so it's the safest place to validate your environment structure.

1. **Get one consumer working end to end.** Move that stack's `StackReference` reads into a `pulumi-stacks` block, verify a no-op preview, and deploy. Now you have a proven pattern to repeat.

1. **Work backward through the chain.** Move to the next stack up — the one whose outputs the stack you just migrated consumes. A stack can be both a producer (still exporting outputs) and a consumer (now reading its own upstream inputs through `pulumi-stacks`); migrating its consumer side doesn't affect the stacks that read *its* outputs.

1. **Keep every step a no-op.** For each stack, the switch should change only the source of its inputs, never its resources. If a preview shows a diff, reconcile it before deploying. Promoting to production as a series of no-ops means you can stop at any point with a working system.

Because the producer's outputs are unchanged throughout, you can run `StackReference` and `pulumi-stacks` side by side during the transition and cut each consumer over independently.

## Next steps

- [`pulumi-stacks` provider reference](/docs/esc/providers/iac/pulumi-stacks/) - Full input and output schema
- [Adopt ESC for config and secrets](/docs/esc/guides/pulumi-iac/adopt-esc-for-config-and-secrets/) - Move stack-file config and secrets into ESC with the same incremental approach
- [Importing environments](/docs/esc/concepts/imports/) - Compose cross-stack outputs with other configuration
- [Stack references](/docs/iac/concepts/stacks/#stackreferences) - The `StackReference` model you're migrating from
