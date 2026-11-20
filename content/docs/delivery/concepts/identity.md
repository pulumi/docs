---
title_tag: Pulumi Delivery pipeline identity
meta_desc: Learn which identity a Pulumi Delivery pipeline runs as, what it can access, and how to run a pipeline as your own service principal or as a team.
title: Pipeline identity
h1: Pipeline identity
menu:
  delivery:
    name: Pipeline identity
    parent: delivery-concepts
    weight: 40
aliases: []
---

Every Pulumi Delivery pipeline runs as one identity in Pulumi Cloud. Each stack update, job, and pass of a run acts with that identity's permissions, no matter who or what started the run. The person who starts a run, approves a gate, or pushes a commit doesn't lend the run their own access.

A pipeline runs as one of these:

| Identity | When | Access Delivery grants for you |
| --- | --- | --- |
| A [service principal that Delivery generates](#the-generated-service-principal) | The default, when the program names nothing | The pipeline stack, its target stacks, and its upstream pipelines |
| A [service principal you manage](#running-as-your-own-service-principal) | The `Pipeline` sets `servicePrincipal.userId` | The pipeline stack only |
| A [team](#running-as-a-team) | The `Pipeline` sets `servicePrincipal.teamName` | The pipeline stack only |
| The [organization's admin](#the-free-edition) | Organizations on the Free edition | None needed |

## The Free edition

An organization on the Free edition has a single member, its admin, so its pipelines run as that admin, with the admin's access. There's nothing to set up: no service principal is created, there's no **Identities** tab, and the program can't set `servicePrincipal`.

Moving between editions changes what a pipeline runs as:

- **From Free to another edition.** A pipeline registered on the Free edition has no identity of its own yet. Register it again to give it one.
- **From another edition to Free.** Pipelines run as the organization's admin from then on, in place of the service principal or team they ran as before. Review what your pipelines deploy before you move.

## The generated service principal

When you register a pipeline whose program names no identity, Delivery creates a [service principal](/docs/administration/concepts/rbac/service-principals/) for it, named `Delivery <project> <stack>` after the pipeline stack. It has no role and doesn't follow your organization's default role, so it can reach only what it's granted.

Each time you register the pipeline, Delivery grants the service principal:

- Stack Write on the pipeline stack.
- Stack Write on every stack that a `Stacks` resource targets.
- Stack Read on the pipeline stack of every upstream pipeline that a `PipelineSource` reads.

These grants are made with the permissions of the person who registers, so that person must be able to change who has access to each of those stacks. Where they can't, registration warns and continues, and the pipeline fails at that stack until a stack admin grants the access or someone with enough access registers the pipeline again.

Delivery doesn't grant anything else. Grant these yourself:

- **ESC environments.** The service principal needs Environment Open on every environment that the pipeline stack and its target stacks import. See [cloud credentials](/docs/delivery/guides/cloud-credentials/#using-short-lived-credentials-with-pulumi-esc).
- **Stacks read through stack references.** Give the service principal Stack Read on each of them.
- **Target stacks added by a push.** A push updates the pipeline definition but doesn't grant access. Register the pipeline again, or grant Stack Write on the new target.

To grant access, open the stack's or environment's [access settings](/docs/administration/concepts/rbac/entities/#entity-access), select **Add Principal**, choose **Service Principal**, and pick the pipeline's service principal.

The generated service principal belongs to its pipeline. It appears on the organization's **Service Principals** tab with the type **Delivery pipeline**. You can't rename or delete it, and no other pipeline can run as it. Deleting the pipeline stack deletes it, along with its access.

## Running as your own service principal

To decide the pipeline's access yourself, create a [service principal](/docs/administration/concepts/rbac/service-principals/#creating-a-service-principal), give it the access the pipeline needs, and name it in the `Pipeline` resource. The value is the service principal's ID or its login (`service-principal:<ID>`), not its display name. To find the login, navigate to **Settings** > **Access management**, select the **Service Principals** tab, and open the service principal: the login is the last part of the page's address.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const pipeline = new delivery.Pipeline("shop", {
    servicePrincipal: { userId: "service-principal:0b6f1c2e-5d3a-4f7b-9c1d-2e8a7b6c5d4f" },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
pipeline = delivery.Pipeline(
    "shop",
    service_principal={"user_id": "service-principal:0b6f1c2e-5d3a-4f7b-9c1d-2e8a7b6c5d4f"},
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
pipeline, err := delivery.NewPipeline(ctx, "shop", &delivery.PipelineArgs{
	ServicePrincipal: &delivery.PipelineServicePrincipalArgs{
		UserId: pulumi.String("service-principal:0b6f1c2e-5d3a-4f7b-9c1d-2e8a7b6c5d4f"),
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var pipeline = new Pipeline("shop", new PipelineArgs
{
    ServicePrincipal = new PipelineServicePrincipalArgs
    {
        UserId = "service-principal:0b6f1c2e-5d3a-4f7b-9c1d-2e8a7b6c5d4f",
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var pipeline = new Pipeline("shop", PipelineArgs.builder()
    .servicePrincipal(PipelineServicePrincipalArgs.builder()
        .userId("service-principal:0b6f1c2e-5d3a-4f7b-9c1d-2e8a7b6c5d4f")
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  shop:
    type: delivery:Pipeline
    properties:
      servicePrincipal:
        userId: service-principal:0b6f1c2e-5d3a-4f7b-9c1d-2e8a7b6c5d4f
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_pipeline" "shop" {
  service_principal = {
    user_id = "service-principal:0b6f1c2e-5d3a-4f7b-9c1d-2e8a7b6c5d4f"
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Then register the pipeline. Registration gives the service principal Stack Write on the pipeline stack and nothing else. Delivery doesn't grant a service principal you manage access to target stacks, upstream pipelines, or environments, so grant it:

- Stack Write on every target stack.
- Stack Read on the pipeline stack of every upstream pipeline.
- Environment Open on every environment those stacks import.

A stack update that the service principal can't reach fails and says which stack is missing the grant.

If the service principal is deleted, the pipeline's work fails until you name another identity and register again. The pipeline never falls back to another identity.

## Running as a team

{{< pulumi-cloud "teams" />}}

A pipeline can run as a [team](/docs/administration/concepts/rbac/teams/), with the team's roles and access. Name the team in the `Pipeline` resource:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const pipeline = new delivery.Pipeline("shop", {
    servicePrincipal: { teamName: "platform" },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
pipeline = delivery.Pipeline(
    "shop",
    service_principal={"team_name": "platform"},
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
pipeline, err := delivery.NewPipeline(ctx, "shop", &delivery.PipelineArgs{
	ServicePrincipal: &delivery.PipelineServicePrincipalArgs{
		TeamName: pulumi.String("platform"),
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var pipeline = new Pipeline("shop", new PipelineArgs
{
    ServicePrincipal = new PipelineServicePrincipalArgs
    {
        TeamName = "platform",
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var pipeline = new Pipeline("shop", PipelineArgs.builder()
    .servicePrincipal(PipelineServicePrincipalArgs.builder()
        .teamName("platform")
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  shop:
    type: delivery:Pipeline
    properties:
      servicePrincipal:
        teamName: platform
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_pipeline" "shop" {
  service_principal = {
    team_name = "platform"
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Set `userId` or `teamName`, not both.

Registration gives the team write access to the pipeline stack, unless the team already has it. Delivery grants a team nothing else, because access given to a team reaches every member of the team. If the team doesn't already have it, give the team:

- Write access to every stack that a `Stacks` resource targets.
- Read access to the pipeline stack of every upstream pipeline that a `PipelineSource` reads.
- Environment Open on every environment those stacks import.

Grant these from each stack's or environment's [access settings](/docs/administration/concepts/rbac/entities/#entity-access), as you would for any team.

In an organization on the permissive [permission mode](/docs/administration/concepts/rbac/permission-modes/), a pipeline that runs as a team also gets the organization-wide default permissions, as [team access tokens](/docs/administration/concepts/access-tokens/#team-access-tokens) do. In a restricted organization, it gets only the team's roles and access.

If the team is deleted, the pipeline's work fails until you name another identity and register again.

## Who can choose the identity

You set or change what a pipeline runs as by running `pulumi delivery register` yourself, and the checks below apply to you. A push can't do it: a pushed commit that changes the identity fails until someone registers the pipeline.

To add a service principal or a team to a pipeline, you need:

- Permission to change who has access to the pipeline stack (the `stack_access:update` scope, which Stack Admin includes).
- Every permission the service principal or team holds, on the same stacks and environments. You can't use a pipeline to reach something you can't reach yourself.
- For a team, permission to manage the team (the `team:update` scope).

Changing the identity of a pipeline that already has one, including back to the generated service principal, also requires permission to change who has access to the pipeline stack.

The pipeline's **Settings** > **Identities** tab lists the service principals and teams the pipeline has been registered with, and who added each one. Anyone who can update the pipeline stack can start runs as these identities, and anyone who can push to the branch that holds the pipeline program can change what those runs deploy. Protect that branch as you would the stacks the pipeline can reach.

## Credentials in stack updates and jobs

Each stack update and job gets a temporary `PULUMI_ACCESS_TOKEN` that acts as the pipeline's identity, with that identity's permissions. The token is revoked when the stack update or job finishes. It can't create other access tokens, and it can't approve, cancel, or retry runs.

A target stack's own [deployment settings](/docs/deployments/concepts/settings/) play no part in a Delivery run, including its [**Run as**](/docs/deployments/concepts/settings/pulumi-cloud-role/) setting.

## Run stacks

Access to a [run stack](/docs/delivery/concepts/#runs) follows its pipeline stack: whoever can read or update the pipeline stack can read or update its run stacks, and access can't be granted on a run stack alone. Deleting the pipeline stack deletes its run stacks.

## Next steps

- Create a [service principal](/docs/administration/concepts/rbac/service-principals/) for a pipeline.
- Give each stage [cloud credentials](/docs/delivery/guides/cloud-credentials/).
- Grant access on a single stack or environment with [entity access](/docs/administration/concepts/rbac/entities/#entity-access).
