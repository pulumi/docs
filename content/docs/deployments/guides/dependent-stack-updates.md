---
title_tag: "Triggering Dependent Stack Updates | Pulumi Deployments"
meta_desc: Learn the recommended way to trigger downstream stack updates when an upstream stack changes, without duplicate fires or re-trigger loops.
title: "Triggering Dependent Stack Updates"
h1: "Triggering Dependent Stack Updates"
aliases:
  - /docs/deployments/guides/post-automation/
  - /docs/pulumi-cloud/deployments/using/post-automation/
  - /docs/deployments/deployments/using/post-automation/
menu:
  deployments:
    name: Dependent Stack Updates
    parent: deployments-guides
    identifier: deployments-guides-dependent-stack-updates
    weight: 50
pulumi_cloud_feature: webhooks
---

When you split your infrastructure across multiple stacks, an upstream stack often exposes outputs that downstream stacks consume through a [stack reference](/docs/iac/concepts/stacks/#stackreferences) — for example, a `network` stack whose VPC ID feeds a `database` stack, which in turn feeds a `compute` stack. A stack reference reads the *current* outputs of the upstream stack, but it does not re-run the downstream stack on its own. When the upstream stack changes, you need a way to cascade an update to the stacks that depend on it.

The supported way to do this is with Pulumi Deployments: configure the downstream stack to run automatically when the upstream stack's update succeeds. This page covers the recommended pattern, how to keep it from firing duplicate or looping deployments, and why to avoid rolling your own webhook.

## The recommended pattern

Trigger each downstream stack from the upstream stack's `update_succeeded` event, using a [deployment webhook destination](#deployment-webhook-destinations) for each upstream → downstream edge.

If you'd rather update a set of dependent stacks together, in order, as one release, use [Pulumi Delivery](/docs/delivery/). A Delivery `Stacks` resource [orders stack updates by their stack references](/docs/delivery/concepts/stacks-and-jobs/#stacks), so you don't wire up a webhook per edge.

These dependencies usually follow one of two patterns:

- **Layered infrastructure within an environment:** stacks in the same environment build on one another — a `network` stack feeds a `database` stack and a `cluster` stack, which in turn feed an `app` stack. Updating a lower layer cascades to the layers above it.
- **Promoting a change across environments:** the same layer flows from one environment to the next — updating `network/dev` promotes to `network/staging`, which promotes to `network/prod`.

Both patterns are directed acyclic graphs.

Every stack you want to deploy automatically must be configured with [deployment settings](/docs/deployments/concepts/settings/), since the trigger runs the target stack through Pulumi Deployments.

The examples on this page use the [Pulumi Service provider](/registry/packages/pulumiservice/) and Pulumi IaC to manage these webhooks declaratively, which is the recommended approach — your dependency wiring lives in code, is reviewed, and stays in sync with the rest of your infrastructure. You can also configure the same webhooks through the [Pulumi Cloud console](/docs/deployments/concepts/webhooks/) or the [REST API](/docs/reference/cloud-rest-api/webhooks/) if you prefer.

{{% notes type="warning" %}}
Manage the webhooks and deployment settings in a **separate stack** from the infrastructure they orchestrate. The orchestration wiring and the infrastructure have different lifecycles — you don't want a change to (or a `pulumi destroy` of) your application infrastructure to also tear down the webhooks that keep your dependent stacks up to date, and vice versa.
{{% /notes %}}

### Deployment webhook destinations

A [deployment webhook destination](/docs/deployments/concepts/webhooks/#deployment-webhooks) lets you pick one or more event types on a stack (for example, `update_succeeded`) and deliver the event to a destination — in this case, the Create Deployment API of another stack. In the example below, an update to the `network` stack triggers the `database` stack, and an update to the `database` stack triggers the `compute` stack.

{{< chooser language "typescript,python,go,csharp,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as pulumiservice from "@pulumi/pulumiservice";

const databaseWebhook = new pulumiservice.Webhook("databaseWebhook", {
    organizationName: "org",
    projectName: "network",
    stackName: "prod",
    format: pulumiservice.WebhookFormat.PulumiDeployments,
    payloadUrl: "database/prod",
    active: true,
    displayName: "deploy-database",
    filters: [pulumiservice.WebhookFilters.UpdateSucceeded],
});
const computeWebhook = new pulumiservice.Webhook("computeWebhook", {
    organizationName: "org",
    projectName: "database",
    stackName: "prod",
    format: pulumiservice.WebhookFormat.PulumiDeployments,
    payloadUrl: "compute/prod",
    active: true,
    displayName: "deploy-compute",
    filters: [pulumiservice.WebhookFilters.UpdateSucceeded],
});
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using PulumiService = Pulumi.PulumiService;

return await Deployment.RunAsync(() =>
{
    var databaseWebhook = new PulumiService.Webhook("databaseWebhook", new()
    {
        OrganizationName = "org",
        ProjectName = "network",
        StackName = "prod",
        Format = PulumiService.WebhookFormat.PulumiDeployments,
        PayloadUrl = "database/prod",
        Active = true,
        DisplayName = "deploy-database",
        Filters = new[]
        {
            PulumiService.WebhookFilters.UpdateSucceeded,
        },
    });

    var computeWebhook = new PulumiService.Webhook("computeWebhook", new()
    {
        OrganizationName = "org",
        ProjectName = "database",
        StackName = "prod",
        Format = PulumiService.WebhookFormat.PulumiDeployments,
        PayloadUrl = "compute/prod",
        Active = true,
        DisplayName = "deploy-compute",
        Filters = new[]
        {
            PulumiService.WebhookFilters.UpdateSucceeded,
        },
    });

});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_pulumiservice as pulumiservice

database_webhook = pulumiservice.Webhook("databaseWebhook",
    organization_name="org",
    project_name="network",
    stack_name="prod",
    format=pulumiservice.WebhookFormat.PULUMI_DEPLOYMENTS,
    payload_url="database/prod",
    active=True,
    display_name="deploy-database",
    filters=[pulumiservice.WebhookFilters.UPDATE_SUCCEEDED])
compute_webhook = pulumiservice.Webhook("computeWebhook",
    organization_name="org",
    project_name="database",
    stack_name="prod",
    format=pulumiservice.WebhookFormat.PULUMI_DEPLOYMENTS,
    payload_url="compute/prod",
    active=True,
    display_name="deploy-compute",
    filters=[pulumiservice.WebhookFilters.UPDATE_SUCCEEDED])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-pulumiservice/sdk/go/pulumiservice"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := pulumiservice.NewWebhook(ctx, "databaseWebhook", &pulumiservice.WebhookArgs{
			OrganizationName: pulumi.String("org"),
			ProjectName:      pulumi.String("network"),
			StackName:        pulumi.String("prod"),
			Format:           pulumiservice.WebhookFormatPulumiDeployments,
			PayloadUrl:       pulumi.String("database/prod"),
			Active:           pulumi.Bool(true),
			DisplayName:      pulumi.String("deploy-database"),
			Filters: pulumiservice.WebhookFiltersArray{
				pulumiservice.WebhookFiltersUpdateSucceeded,
			},
		})
		if err != nil {
			return err
		}
		_, err = pulumiservice.NewWebhook(ctx, "computeWebhook", &pulumiservice.WebhookArgs{
			OrganizationName: pulumi.String("org"),
			ProjectName:      pulumi.String("database"),
			StackName:        pulumi.String("prod"),
			Format:           pulumiservice.WebhookFormatPulumiDeployments,
			PayloadUrl:       pulumi.String("compute/prod"),
			Active:           pulumi.Bool(true),
			DisplayName:      pulumi.String("deploy-compute"),
			Filters: pulumiservice.WebhookFiltersArray{
				pulumiservice.WebhookFiltersUpdateSucceeded,
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: dependent-stacks-demo
runtime: yaml
description: Trigger dependent stack updates with deployment webhooks
resources:
  databaseWebhook:
    type: pulumiservice:Webhook
    properties:
      organizationName: org
      projectName: network
      stackName: prod
      format: pulumi_deployments
      payloadUrl: database/prod
      active: true
      displayName: deploy-database
      filters:
      - update_succeeded
  computeWebhook:
    type: pulumiservice:Webhook
    properties:
      organizationName: org
      projectName: database
      stackName: prod
      format: pulumi_deployments
      payloadUrl: compute/prod
      active: true
      displayName: deploy-compute
      filters:
      - update_succeeded
```

{{% /choosable %}}

{{% choosable language hcl %}}

`Pulumi.yaml`:

```yaml
name: dependent-stacks-demo
runtime: hcl
description: Trigger dependent stack updates with deployment webhooks
```

`main.tf`:

```hcl
terraform {
  required_providers {
    pulumiservice = {
      source = "pulumi/pulumiservice"
    }
  }
}

resource "pulumiservice_webhook" "database_webhook" {
  organization_name = "org"
  project_name      = "network"
  stack_name        = "prod"
  format            = "pulumi_deployments"
  payload_url       = "database/prod"
  active            = true
  display_name      = "deploy-database"
  filters           = ["update_succeeded"]
}

resource "pulumiservice_webhook" "compute_webhook" {
  organization_name = "org"
  project_name      = "database"
  stack_name        = "prod"
  format            = "pulumi_deployments"
  payload_url       = "compute/prod"
  active            = true
  display_name      = "deploy-compute"
  filters           = ["update_succeeded"]
}
```

The `pulumi/` prefix on the source selects the native Pulumi provider. Run `pulumi install` after you add the `required_providers` block.

{{% /choosable %}}

{{< /chooser >}}

## Avoiding duplicate fires and re-trigger loops

The most common problems people hit when cascading deployments are the same stack deploying several times for a single upstream change, or two stacks re-triggering each other indefinitely. The supported pattern avoids both when you follow these rules:

- **Filter on a single terminal event.** Trigger on `update_succeeded` only. A single deployment emits several events over its lifecycle — `deployment_queued`, `deployment_started`, and finally `update_succeeded` — so subscribing to more than one event kind (or to lifecycle events instead of the terminal one) causes the downstream stack to fire multiple times per upstream change.
- **Target the downstream stack's deployment directly.** Use the built-in **Deployment** webhook destination, which calls the Create Deployment API of a specific stack. This is a directed edge with a known endpoint, unlike a generic HTTP webhook pointed at custom automation that runs `pulumi up` and can fan out to more work than you intended.
- **Keep the dependency graph acyclic.** Never let stack A trigger stack B while stack B triggers stack A, whether directly or through a longer chain. A cycle means each update triggers the next one forever. Model your stacks as a directed acyclic graph (DAG).

## What to avoid: the naive webhook workaround

A tempting shortcut is to attach a generic webhook to the upstream stack that points at a custom endpoint — a serverless function or a CI job — which then shells out to `pulumi up` on the downstream stack. Avoid this. In practice it tends to:

- **Fire far more often than intended,** because a generic webhook that isn't narrowly filtered receives every event kind for the stack, so one upstream change can kick off many downstream runs.
- **Re-trigger in loops,** because custom automation has no built-in awareness of the dependency graph and nothing stops a downstream update from triggering the upstream one again.
- **Duplicate deployment logic outside Pulumi,** reimplementing credentials, source configuration, and settings that [deployment settings](/docs/deployments/concepts/settings/) already manage.

Use a [deployment webhook destination](#deployment-webhook-destinations) instead. It runs the target stack through Pulumi Deployments with its saved settings, so the trigger stays scoped to one deployment per upstream change.

## Triggering with custom or one-off settings

A deployment webhook runs the target stack with its existing [deployment settings](/docs/deployments/concepts/settings/) and cannot override them. When you need to trigger a downstream deployment with custom or one-off settings — a different branch, environment variables, or pre-run commands — use the [REST API trigger](/docs/deployments/concepts/triggers/#rest-api) instead, which accepts settings in the request body.

## Related

- [Deployment triggers](/docs/deployments/concepts/triggers/) — every way a deployment can be initiated.
- [Deployment webhooks](/docs/deployments/concepts/webhooks/#deployment-webhooks) — the webhook and event-filtering reference.
- [Deployment settings](/docs/deployments/concepts/settings/) — required on any stack you deploy automatically.
- [Stack references](/docs/iac/concepts/stacks/#stackreferences) — how downstream stacks consume upstream outputs.
- [Pulumi Delivery](/docs/delivery/) — update dependent stacks in order as part of a release.
