---
title_tag: Pulumi Delivery sources and triggers
meta_desc: Declare the repositories and upstream pipelines that make up a Pulumi Delivery release, and control which changes start a run.
title: Sources and triggers
h1: Sources and triggers
menu:
  delivery:
    name: Sources and triggers
    parent: delivery-concepts
    weight: 10
aliases: []
---

A source tells Pulumi Delivery where a release's code comes from. Every stack update and job checks out a source. A _release_ is the set of commits, one per source, that a run deploys. A trigger on a source decides whether a change to it starts a new run.

## Repository sources

Delivery has one source resource per version control provider. Each takes a `repository` and a `branch`:

| Resource | `repository` format |
| --- | --- |
| `GitHubSource` | `owner/repo` |
| `GitLabSource` | `group/subgroup/repo`, the full path |
| `BitbucketSource` | `workspace/repo` |
| `AzureDevOpsSource` | `org/project/repo` |

Pulumi Cloud uses your organization's [version control integration](/docs/integrations/version-control/) to interact with your source code provider. You'll need to give that integration access to every repository you use in your pipelines, including the repository containing the pipeline program itself.

When a run is created, Pulumi Delivery fetches the code from each source and pins the run to one commit from each. Every stage of the run uses those pinned commits, so the code stays the same as the release moves through the pipeline, even if new commits land in the meantime.

Declare sources directly, not inside code that waits for a stack or job output. A source that appears only after a stack update or job finishes is too late to be pinned, and the run fails.

## Pipeline sources

A `PipelineSource` reads the release that a stage of another pipeline deployed. It's how a downstream pipeline picks up values, such as a cluster endpoint, that an upstream pipeline published as [artifacts](/docs/delivery/concepts/stages-and-gates/#artifacts).

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const platform = new delivery.PipelineSource("platform", {
    pipeline: "platform-delivery/main",
    stage: "prod",
    trigger: true,
});
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
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var platform = new PipelineSource("platform", PipelineSourceArgs.builder()
    .pipeline("platform-delivery/main")
    .stage("prod")
    .trigger(true)
    .build());
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
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_pipeline_source" "platform" {
  pipeline = "platform-delivery/main"
  stage    = "prod"
  trigger  = true
}
```

{{% /choosable %}}

{{< /chooser >}}

To learn more, see [Connecting pipelines](/docs/delivery/guides/multiple-pipelines/).

## Triggers

A _trigger_ on a source decides whether a change to that source starts a new run.

To start a run on every push to the branch, set `trigger: true`. To start a run only when a push changes certain files, set `trigger` to `{ paths: [...] }` with a list of glob patterns:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const app = new delivery.GitHubSource("app", {
    repository: "acme/shop",
    branch: "main",
    trigger: { paths: ["src/**", "delivery/**"] },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
app = delivery.GitHubSource(
    "app",
    repository="acme/shop",
    branch="main",
    trigger={"paths": ["src/**", "delivery/**"]},
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
app, err := delivery.NewGitHubSource(ctx, "app", &delivery.GitHubSourceArgs{
	Repository: pulumi.String("acme/shop"),
	Branch:     pulumi.String("main"),
	Trigger: delivery.SourceTriggerArgs{
		Paths: pulumi.StringArray{pulumi.String("src/**"), pulumi.String("delivery/**")},
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var app = new GitHubSource("app", new GitHubSourceArgs
{
    Repository = "acme/shop",
    Branch = "main",
    Trigger = new SourceTriggerArgs { Paths = { "src/**", "delivery/**" } },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var app = new GitHubSource("app", GitHubSourceArgs.builder()
    .repository("acme/shop")
    .branch("main")
    .trigger(SourceTriggerArgs.builder()
        .paths("src/**", "delivery/**")
        .build())
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  app:
    type: delivery:GitHubSource
    properties:
      repository: acme/shop
      branch: main
      trigger:
        paths:
          - src/**
          - delivery/**
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_git_hub_source" "app" {
  repository = "acme/shop"
  branch     = "main"
  trigger = {
    paths = ["src/**", "delivery/**"]
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

On a `PipelineSource`, `trigger: true` starts a run whenever the named upstream stage deploys a new release.

A source without a `trigger` is still part of the release, but changes to it never start a run.

## Other ways to start a run

You can also start a run from **Start a run** in the Pulumi Cloud console, or through the REST API. To [run a pipeline locally](/docs/delivery/concepts/#run-locally), run `pulumi up` on the pipeline stack.

To start a run through the REST API:

```bash
curl -X POST \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{}' \
    https://api.pulumi.com/api/preview/stacks/acme/shop-delivery/main/delivery/dispatch
```

<!-- TODO(launch): Once the Delivery REST API is publicly documented, link this example to its API reference page. -->

## Next steps

- Order environments and add approvals with [stages and gates](/docs/delivery/concepts/stages-and-gates/).
- Pass values between pipelines in [Connecting pipelines](/docs/delivery/guides/multiple-pipelines/).
