---
title_tag: Pulumi Delivery stages and gates
meta_desc: Order promotion between environments with Pulumi Delivery stages, hold a release at a gate until someone approves it, and publish artifacts from a stage.
title: Stages and gates
h1: Stages and gates
menu:
  delivery:
    name: Stages and gates
    parent: delivery-concepts
    weight: 20
aliases: []
---

Stages give a pipeline its shape. Each stage is a step that a release moves through, commonly one environment such as `dev` or `prod`.

## Ordering stages with `from`

A stage with no `from` is an entry stage. Every other stage lists its upstream stages:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const dev = new delivery.Stage("dev", { pipeline });
const staging = new delivery.Stage("staging", { pipeline, from: [dev] });
const prod = new delivery.Stage("prod", { pipeline, from: [staging] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
dev = delivery.Stage("dev", pipeline=pipeline)
staging = delivery.Stage("staging", pipeline=pipeline, from_=[dev])
prod = delivery.Stage("prod", pipeline=pipeline, from_=[staging])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
dev, err := delivery.NewStage(ctx, "dev", &delivery.StageArgs{Pipeline: pipeline})
if err != nil {
	return err
}
staging, err := delivery.NewStage(ctx, "staging", &delivery.StageArgs{Pipeline: pipeline, From: delivery.StageArray{dev}})
if err != nil {
	return err
}
prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{Pipeline: pipeline, From: delivery.StageArray{staging}})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var dev = new Stage("dev", new StageArgs { Pipeline = pipeline });
var staging = new Stage("staging", new StageArgs { Pipeline = pipeline, From = { dev } });
var prod = new Stage("prod", new StageArgs { Pipeline = pipeline, From = { staging } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var dev = new Stage("dev", StageArgs.builder().pipeline(pipeline).build());
var staging = new Stage("staging", StageArgs.builder().pipeline(pipeline).from(dev).build());
var prod = new Stage("prod", StageArgs.builder().pipeline(pipeline).from(staging).build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  dev:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
  staging:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${dev}
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stage" "dev" {
  pipeline = delivery_pipeline.pipeline
}

resource "delivery_stage" "staging" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.dev]
}

resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
}
```

{{% /choosable %}}

{{< /chooser >}}

A stage with several upstream stages waits until the same release has succeeded in each of them. Stage names must be unique within a pipeline.

A stage deploys one run at a time. When a newer run reaches a stage while an older run is still waiting for it, or waiting at its gate, the newer run takes its place. A run that has already entered the stage keeps it until it finishes.

<!-- TODO(launch): Say what happens to the older run when a newer one takes its place (canceled, or skips the stage). -->

{{% notes %}}
Pulumi Delivery doesn't detect cycles between stages. A run in a cycle waits until you cancel it.
{{% /notes %}}

## Gates

A gate is a rule on a stage that defines when a pipeline can progress. A release can't enter the stage until the rule passes.

Pulumi Delivery supports two kinds of gates, _manual_ and _approval_, and you can combine them into one rule. Both are set in the stage's `when` property. Anyone with permission to approve the pipeline's runs can continue a manual gate. An approval gate names the people or teams who must approve and how many approvals it needs, shows them a preview of the changes, and lets them reject the release.

<!-- TODO(launch): Reconcile who can continue a manual gate: this paragraph says permission to approve runs, and the REST API section says write access to the pipeline stack. -->

### Manual gates

Manual gates pause the pipeline and wait for a person to continue them. You can use the gate's `description` property to help that person decide whether to do so:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.manual({ description: "Check the staging dashboards first." }),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(kind="manual", description="Check the staging dashboards first."),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
	Pipeline: pipeline,
	From:     delivery.StageArray{staging},
	When: delivery.RuleArgs{
		Kind:        pulumi.String("manual"),
		Description: pulumi.String("Check the staging dashboards first."),
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var prod = new Stage("prod", new StageArgs
{
    Pipeline = pipeline,
    From = { staging },
    When = new RuleArgs { Kind = "manual", Description = "Check the staging dashboards first." },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var prod = new Stage("prod", StageArgs.builder()
    .pipeline(pipeline)
    .from(staging)
    .when(RuleArgs.builder()
        .kind("manual")
        .description("Check the staging dashboards first.")
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
      when:
        kind: manual
        description: Check the staging dashboards first.
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
  when = {
    kind        = "manual"
    description = "Check the staging dashboards first."
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Gates can be continued from the run page in the Pulumi Cloud console or with the REST API. See [Continuing a gate with the REST API](#continuing-a-gate-with-the-rest-api) for details.

### Approval gates

<!-- TODO(launch): Replace the next sentence with the pulumi-cloud shortcode for "delivery-approvals" once pulumi/marketing-web adds a hidden `delivery-approvals` feature (min_edition: pro). -->

Approval gates (available in the Pro and Enterprise editions) pause the pipeline until a set number of specified users or team members allow it to continue. List them in `approvers` as Pulumi usernames or team names, and set `count` to the number of approvals required (one by default):

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.approval({ approvers: ["platform-leads"], count: 2 }),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(kind="approval", approvers=["platform-leads"], count=2),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
	Pipeline: pipeline,
	From:     delivery.StageArray{staging},
	When: delivery.RuleArgs{
		Kind:      pulumi.String("approval"),
		Approvers: pulumi.StringArray{pulumi.String("platform-leads")},
		Count:     pulumi.Int(2),
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var prod = new Stage("prod", new StageArgs
{
    Pipeline = pipeline,
    From = { staging },
    When = new RuleArgs { Kind = "approval", Approvers = { "platform-leads" }, Count = 2 },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var prod = new Stage("prod", StageArgs.builder()
    .pipeline(pipeline)
    .from(staging)
    .when(RuleArgs.builder()
        .kind("approval")
        .approvers("platform-leads")
        .count(2)
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
      when:
        kind: approval
        approvers:
          - platform-leads
        count: 2
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
  when = {
    kind      = "approval"
    approvers = ["platform-leads"]
    count     = 2
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Before approving, an approver sees a preview of the stack updates the stage will make. The preview doesn't cover jobs, because they run arbitrary commands. It can also be incomplete: a stack whose preview shows "Not available" might still change when the stage runs.

### Combining rules

You can also build composite rules that combine manual and approval gates. In the following example, the pipeline is paused until `<your-colleague>` approves _and_ someone continues the `dashboards` check:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.allOfOutput({
        rules: [
            delivery.approvalOutput({ approvers: ["<your-colleague>"] }),
            delivery.manualOutput({ name: "dashboards", description: "Check the dashboards first." }),
        ],
    }),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(
        kind="all",
        rules=[
            delivery.RuleArgs(kind="approval", approvers=["<your-colleague>"]),
            delivery.RuleArgs(kind="manual", name="dashboards", description="Check the dashboards first."),
        ],
    ),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
	Pipeline: pipeline,
	From:     delivery.StageArray{staging},
	When: delivery.RuleArgs{
		Kind: pulumi.String("all"),
		Rules: delivery.RuleArray{
			delivery.RuleArgs{
				Kind:      pulumi.String("approval"),
				Approvers: pulumi.StringArray{pulumi.String("<your-colleague>")},
			},
			delivery.RuleArgs{
				Kind:        pulumi.String("manual"),
				Name:        pulumi.String("dashboards"),
				Description: pulumi.String("Check the dashboards first."),
			},
		},
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var prod = new Stage("prod", new StageArgs
{
    Pipeline = pipeline,
    From = { staging },
    When = new RuleArgs
    {
        Kind = "all",
        Rules =
        {
            new RuleArgs { Kind = "approval", Approvers = { "<your-colleague>" } },
            new RuleArgs { Kind = "manual", Name = "dashboards", Description = "Check the dashboards first." },
        },
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var prod = new Stage("prod", StageArgs.builder()
    .pipeline(pipeline)
    .from(staging)
    .when(RuleArgs.builder()
        .kind("all")
        .rules(
            RuleArgs.builder()
                .kind("approval")
                .approvers("<your-colleague>")
                .build(),
            RuleArgs.builder()
                .kind("manual")
                .name("dashboards")
                .description("Check the dashboards first.")
                .build())
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${pipeline}
      from:
        - ${staging}
      when:
        kind: all
        rules:
          - kind: approval
            approvers:
              - <your-colleague>
          - kind: manual
            name: dashboards
            description: Check the dashboards first.
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.pipeline
  from     = [delivery_stage.staging]
  when = {
    kind = "all"
    rules = [
      {
        kind      = "approval"
        approvers = ["<your-colleague>"]
      },
      {
        kind        = "manual"
        name        = "dashboards"
        description = "Check the dashboards first."
      },
    ]
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Composite rules can be of type `all` or `any`. `all`-type rules require that every rule in the rules list be satisfied, as in the previous example. `any`-type rules require at least one of them to be. You can nest rules up to three levels deep, counting the rules themselves: an `all` rule that contains an `any` rule that contains an approval is the deepest a gate can go.

Every rule takes an optional `name`, and names must be unique within a gate. An approval rule's name defaults to `approval` and a manual rule's to `manual`, so name each rule when a gate has two of the same kind.

## Continuing a gate with the REST API

Any credential with write access to the pipeline stack can continue a manual gate. To do it from another system, such as a deployment hook:

1. Read the run with `GET /api/preview/stacks/<org>/<project>/<stack>/delivery/runs/<run-number>`.
1. In `stages`, find the stage. If `stages[].gate.status` is `open`, note `stages[].gate.id`.
1. Send `POST .../delivery/runs/<run-number>/gates/<gate-id>/continue` with a JSON body:

    ```bash
    curl -X POST \
        -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{}' \
        https://api.pulumi.com/api/preview/stacks/acme/shop-delivery/main/delivery/runs/<run-number>/gates/<gate-id>/continue
    ```

A gate with one manual rule takes an empty JSON object. For a gate with several manual rules, pass the rule's name in `condition`, as in `{"condition": "dashboards"}`.

<!-- TODO(launch): Once the Delivery REST API is publicly documented, link this example to its API reference page. -->

## Artifacts

Artifacts are to pipelines what stack outputs are to stacks. An _artifact_ is a named value that a stage publishes once the release reaches it, such as a cluster endpoint, a database ID, or a container image tag. Other pipelines in your organization read it with a [`PipelineSource`](/docs/delivery/concepts/sources-and-triggers/#pipeline-sources). Artifacts are how one pipeline hands values to another without either one reaching into the other's stacks.

### Publishing an artifact

An `Artifact` resource names the stage that publishes it:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
new delivery.Artifact("clusterEndpoint", {
    stage: prod,
    value: cluster.outputs.apply(o => o["cluster"]["endpoint"]),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
delivery.Artifact(
    "clusterEndpoint",
    stage=prod,
    value=cluster.outputs.apply(lambda o: o["cluster"]["endpoint"]),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
_, err = delivery.NewArtifact(ctx, "clusterEndpoint", &delivery.ArtifactArgs{
	Stage: prod,
	Value: cluster.Outputs.ApplyT(func(o map[string]map[string]interface{}) interface{} {
		return o["cluster"]["endpoint"]
	}),
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
new Artifact("clusterEndpoint", new ArtifactArgs
{
    Stage = prod,
    Value = cluster.Outputs.Apply(o => o["cluster"]["endpoint"]),
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
new Artifact("clusterEndpoint", ArtifactArgs.builder()
    .stage(prod)
    .value(cluster.outputs().applyValue(o -> (Object) o.get("cluster").get("endpoint")))
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  clusterEndpoint:
    type: delivery:Artifact
    properties:
      stage: ${prod}
      value: ${cluster.outputs["cluster"]["endpoint"]}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_artifact" "clusterEndpoint" {
  stage = delivery_stage.prod
  value = delivery_stacks.cluster.outputs["cluster"]["endpoint"]
}
```

{{% /choosable %}}

{{< /chooser >}}

The value can be any structured value, such as a string, number, list, or map, and it can be secret. An artifact can't hold a file or binary data. It usually comes from the outputs of a stack update or a job in the same stage, as in this example, where `cluster` is a `Stacks` resource.

Other pipelines see an artifact once the release reaches its stage and the value is known. Because it belongs to a stage, a downstream pipeline that reads the `prod` stage only ever sees values from releases that `prod` deployed.

### Reading artifacts from other pipelines

A downstream pipeline can read an upstream pipeline's artifacts through a `PipelineSource`:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const platform = new delivery.PipelineSource("platform", {
    pipeline: "platform-delivery/main",
    stage: "prod",
    trigger: true,
});

const clusterEndpoint = platform.artifacts["clusterEndpoint"];
```

{{% /choosable %}}
{{% choosable language python %}}

```python
platform = delivery.PipelineSource(
    "platform",
    pipeline="platform-delivery/main",
    stage="prod",
    trigger=True,
)

cluster_endpoint = platform.artifacts["clusterEndpoint"]
```

{{% /choosable %}}
{{% choosable language go %}}

```go
platform, err := delivery.NewPipelineSource(ctx, "platform", &delivery.PipelineSourceArgs{
	Pipeline: pulumi.String("platform-delivery/main"),
	Stage:    pulumi.String("prod"),
	Trigger:  pulumi.Bool(true),
})
if err != nil {
	return err
}

clusterEndpoint := platform.Artifacts.MapIndex(pulumi.String("clusterEndpoint"))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var platform = new PipelineSource("platform", new PipelineSourceArgs
{
    Pipeline = "platform-delivery/main",
    Stage = "prod",
    Trigger = true,
});

var clusterEndpoint = platform.Artifacts.Apply(artifacts => artifacts["clusterEndpoint"]);
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var platform = new PipelineSource("platform", PipelineSourceArgs.builder()
    .pipeline("platform-delivery/main")
    .stage("prod")
    .trigger(true)
    .build());

var clusterEndpoint = platform.artifacts().applyValue(artifacts -> artifacts.get("clusterEndpoint"));
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  platform:
    type: delivery:PipelineSource
    properties:
      pipeline: platform-delivery/main
      stage: prod
      trigger: true

variables:
  clusterEndpoint: ${platform.artifacts["clusterEndpoint"]}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_pipeline_source" "platform" {
  pipeline = "platform-delivery/main"
  stage    = "prod"
  trigger  = true
}

locals {
  cluster_endpoint = delivery_pipeline_source.platform.artifacts["clusterEndpoint"]
}
```

{{% /choosable %}}

{{< /chooser >}}

Pipeline sources return the artifacts of the latest release the specified stage deployed, including the artifacts that earlier stages published for that release.

### Secret artifacts

If any artifact is secret, the whole `artifacts` map is secret. A `Stacks` entry's `config` rejects secret values, so pass a secret artifact to a stack update or job in [`environment`](/docs/delivery/guides/cloud-credentials/#passing-credentials-through-the-pipeline) instead.

## Next steps

- Configure the [stacks and jobs](/docs/delivery/concepts/stacks-and-jobs/) each stage runs.
- Pass artifacts between pipelines in [Connecting pipelines](/docs/delivery/guides/multiple-pipelines/).
