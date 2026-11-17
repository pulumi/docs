---
title: Concepts
title_tag: Pulumi Delivery concepts
h1: How Pulumi Delivery works
meta_desc: How Pulumi Delivery models a release pipeline as a Pulumi program, and how pipelines, runs, stages, stacks, jobs, artifacts, sources, and releases relate.
menu:
  delivery:
    name: Concepts
    parent: delivery-home
    identifier: delivery-concepts
    weight: 10
aliases: []
---

In many organizations, delivery logic lives in standalone pipeline files and manual console steps, spread across tools that run separately from your infrastructure, secrets, and policies. Pulumi Delivery lets you define how a change moves from development through staging to production in the same language you write your infrastructure in, whether that's TypeScript, Python, Go, C#, Java, YAML, or HCL.

Because the pipeline is a Pulumi program, it's versioned and reviewed with your code. You can build it with loops, functions, and conditionals, and it gets previews and a history like any stack.

{{% notes type="info" %}}
Pulumi Delivery is in public preview. Behavior, the SDK, and the REST API routes under `/api/preview/` can change before general availability.

Pulumi Delivery needs Pulumi CLI v3.277.0 or later.
{{% /notes %}}

## An example pipeline

This pipeline deploys an app from the `acme/shop` repository to `dev`, runs its tests, and then waits for someone to approve the release before it deploys to `prod`:

<!-- TODO(launch): Once a Delivery `pulumi new` template is published, align this example with the template's source and variable names. -->

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as delivery from "@pulumi/delivery";

const repo = new delivery.GitHubSource("repo", {
    repository: "acme/shop",
    branch: "main",
    trigger: { paths: ["app/**", "delivery/**"] },
});

const pipeline = new delivery.Pipeline("shop");

const dev = new delivery.Stage("dev", { pipeline });
new delivery.Stacks("dev", {
    stage: dev,
    stacks: { app: { stack: "shop-app/dev", source: repo, directory: "app" } },
});
new delivery.Job("test", {
    stage: dev,
    source: repo,
    directory: "app",
    command: "npm ci && npm test",
});

const prod = new delivery.Stage("prod", { pipeline, from: [dev], when: delivery.approval() });
new delivery.Stacks("prod", {
    stage: prod,
    stacks: { app: { stack: "shop-app/prod", source: repo, directory: "app" } },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_delivery as delivery

repo = delivery.GitHubSource(
    "repo",
    repository="acme/shop",
    branch="main",
    trigger={"paths": ["app/**", "delivery/**"]},
)

pipeline = delivery.Pipeline("shop")

dev = delivery.Stage("dev", pipeline=pipeline)
delivery.Stacks(
    "dev",
    stage=dev,
    stacks={"app": {"stack": "shop-app/dev", "source": repo, "directory": "app"}},
)
delivery.Job(
    "test",
    stage=dev,
    source=repo,
    directory="app",
    command="npm ci && npm test",
)

prod = delivery.Stage(
    "prod", pipeline=pipeline, from_=[dev], when=delivery.RuleArgs(kind="approval")
)
delivery.Stacks(
    "prod",
    stage=prod,
    stacks={"app": {"stack": "shop-app/prod", "source": repo, "directory": "app"}},
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-delivery/sdk/go/delivery"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		repo, err := delivery.NewGitHubSource(ctx, "repo", &delivery.GitHubSourceArgs{
			Repository: pulumi.String("acme/shop"),
			Branch:     pulumi.String("main"),
			Trigger: delivery.SourceTriggerArgs{
				Paths: pulumi.StringArray{pulumi.String("app/**"), pulumi.String("delivery/**")},
			},
		})
		if err != nil {
			return err
		}

		pipeline, err := delivery.NewPipeline(ctx, "shop", nil)
		if err != nil {
			return err
		}

		dev, err := delivery.NewStage(ctx, "dev", &delivery.StageArgs{Pipeline: pipeline})
		if err != nil {
			return err
		}
		_, err = delivery.NewStacks(ctx, "dev", &delivery.StacksArgs{
			Stage: dev,
			Stacks: delivery.StacksEntryMap{
				"app": delivery.StacksEntryArgs{Stack: pulumi.String("shop-app/dev"), Source: repo, Directory: pulumi.String("app")},
			},
		})
		if err != nil {
			return err
		}
		_, err = delivery.NewJob(ctx, "test", &delivery.JobArgs{
			Stage:     dev,
			Source:    repo,
			Directory: pulumi.String("app"),
			Command:   pulumi.String("npm ci && npm test"),
		})
		if err != nil {
			return err
		}

		prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
			Pipeline: pipeline,
			From:     delivery.StageArray{dev},
			When:     delivery.RuleArgs{Kind: pulumi.String("approval")},
		})
		if err != nil {
			return err
		}
		_, err = delivery.NewStacks(ctx, "prod", &delivery.StacksArgs{
			Stage: prod,
			Stacks: delivery.StacksEntryMap{
				"app": delivery.StacksEntryArgs{Stack: pulumi.String("shop-app/prod"), Source: repo, Directory: pulumi.String("app")},
			},
		})
		return err
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Delivery.Delivery;
using Pulumi.Delivery.Delivery.Inputs;

return await Deployment.RunAsync(() =>
{
    var repo = new GitHubSource("repo", new GitHubSourceArgs
    {
        Repository = "acme/shop",
        Branch = "main",
        Trigger = new SourceTriggerArgs { Paths = { "app/**", "delivery/**" } },
    });

    var pipeline = new Pipeline("shop");

    var dev = new Stage("dev", new StageArgs { Pipeline = pipeline });
    new Stacks("dev", new StacksArgs
    {
        Stage = dev,
        Stacks = { ["app"] = new StacksEntryArgs { Stack = "shop-app/dev", Source = repo, Directory = "app" } },
    });
    new Job("test", new JobArgs
    {
        Stage = dev,
        Source = repo,
        Directory = "app",
        Command = "npm ci && npm test",
    });

    var prod = new Stage("prod", new StageArgs
    {
        Pipeline = pipeline,
        From = { dev },
        When = new RuleArgs { Kind = "approval" },
    });
    new Stacks("prod", new StacksArgs
    {
        Stage = prod,
        Stacks = { ["app"] = new StacksEntryArgs { Stack = "shop-app/prod", Source = repo, Directory = "app" } },
    });
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.delivery.delivery.*;
import com.pulumi.delivery.delivery.inputs.*;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var repo = new GitHubSource("repo", GitHubSourceArgs.builder()
                .repository("acme/shop")
                .branch("main")
                .trigger(SourceTriggerArgs.builder().paths("app/**", "delivery/**").build())
                .build());

            var pipeline = new Pipeline("shop");

            var dev = new Stage("dev", StageArgs.builder().pipeline(pipeline).build());
            new Stacks("dev", StacksArgs.builder()
                .stage(dev)
                .stacks(Map.of("app", StacksEntryArgs.builder().stack("shop-app/dev").source(repo).directory("app").build()))
                .build());
            new Job("test", JobArgs.builder()
                .stage(dev)
                .source(repo)
                .directory("app")
                .command("npm ci && npm test")
                .build());

            var prod = new Stage("prod", StageArgs.builder()
                .pipeline(pipeline)
                .from(dev)
                .when(RuleArgs.builder().kind("approval").build())
                .build());
            new Stacks("prod", StacksArgs.builder()
                .stage(prod)
                .stacks(Map.of("app", StacksEntryArgs.builder().stack("shop-app/prod").source(repo).directory("app").build()))
                .build());
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
name: shop-delivery
runtime: yaml

resources:
  repo:
    type: delivery:GitHubSource
    properties:
      repository: acme/shop
      branch: main
      trigger:
        paths:
          - app/**
          - delivery/**
  shop:
    type: delivery:Pipeline

  dev:
    type: delivery:Stage
    properties:
      pipeline: ${shop}
  devApp:
    type: delivery:Stacks
    properties:
      stage: ${dev}
      stacks:
        app:
          stack: shop-app/dev
          source: ${repo}
          directory: app
  test:
    type: delivery:Job
    properties:
      stage: ${dev}
      source: ${repo}
      directory: app
      command: npm ci && npm test

  prod:
    type: delivery:Stage
    properties:
      pipeline: ${shop}
      from:
        - ${dev}
      when:
        kind: approval
  prodApp:
    type: delivery:Stacks
    properties:
      stage: ${prod}
      stacks:
        app:
          stack: shop-app/prod
          source: ${repo}
          directory: app
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
terraform {
  required_providers {
    delivery = {
      source = "pulumi/delivery"
    }
  }
}

resource "delivery_git_hub_source" "repo" {
  repository = "acme/shop"
  branch     = "main"
  trigger = {
    paths = ["app/**", "delivery/**"]
  }
}

resource "delivery_pipeline" "shop" {}

resource "delivery_stage" "dev" {
  pipeline = delivery_pipeline.shop
}

resource "delivery_stacks" "dev" {
  stage = delivery_stage.dev
  stacks = {
    app = { stack = "shop-app/dev", source = delivery_git_hub_source.repo, directory = "app" }
  }
}

resource "delivery_job" "test" {
  stage     = delivery_stage.dev
  source    = delivery_git_hub_source.repo
  directory = "app"
  command   = "npm ci && npm test"
}

resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.shop
  from     = [delivery_stage.dev]
  when     = { kind = "approval" }
}

resource "delivery_stacks" "prod" {
  stage = delivery_stage.prod
  stacks = {
    app = { stack = "shop-app/prod", source = delivery_git_hub_source.repo, directory = "app" }
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Each part of the program maps to a concept on this page:

- The `GitHubSource` is a [source](#sources-and-releases). Its `trigger` starts a run when a commit to `main` changes `app/` or `delivery/`.
- The `Pipeline` resource declares the pipeline. The pipeline stack's config says where the [pipeline program](#pipeline-program) itself lives: the `delivery` directory of the same repository.
- The two `Stage` resources are the pipeline's [stages](#stages). `prod` lists `dev` in `from`, so a release reaches `prod` only after `dev` succeeds, and its `when` gate holds the release until someone approves it.
- Each `Stacks` resource updates the [stacks](#stacks) for its stage, and the `Job` runs the app's tests in `dev`, as a [job](#jobs).

Each push that matches the trigger starts a [run](#runs), which takes the pushed code (the [release](#sources-and-releases)) through `dev` and then `prod`.

## Pipeline program

The pipeline lives in a repository as a Pulumi project, and it declares exactly one `Pipeline` resource. You work with it in two ways:

- **Register it** with `pulumi delivery register`. Pulumi Cloud stores the pipeline and listens for changes. One registered, its triggers start runs in Pulumi Cloud.
- **Run it locally** with `pulumi up`. This is how you can iterate on your pipeline program from your local branch without needing to push your changes.

### Register the pipeline

To register the pipeline, run `pulumi delivery register` in the pipeline's project directory.

Registering doesn't start a run. The command writes the pipeline's location in your repository to the stack's `delivery:source` config. Commit the updated config file so that Pulumi Cloud can find the program. Once registered, a push to the repository's default branch updates the pipeline.

### Run the pipeline locally

Run `pulumi up` on the pipeline stack to start a run from your checked out branch. The pipeline program runs on your machine, and the stack updates and jobs run in Pulumi Cloud at the latest pushed commit of their sources. The command waits for the run to end and prints a link to it in the Pulumi Cloud console. A stack update or job that hasn't changed since your last `pulumi up` doesn't run again.

## Stages

A _stage_ is a phase of the pipeline, for example an environment like `dev`. A stage runs once its upstream stages have succeeded and its _gate_, if it has one, has passed. A gate is a rule in the stage's `when` property, such as a required approval. See [Gates](/docs/delivery/concepts/stages-and-gates/#gates).

## Stacks

A `Stacks` resource updates one or more existing stacks in a stage. Each entry runs `pulumi up` on one target stack at the commit the run pinned for its source. The entries in one `Stacks` resource start together, and stack references between them decide the order, so stacks that depend on each other belong in the same one. See [Stacks](/docs/delivery/concepts/stacks-and-jobs/#stacks).

## Jobs

A `Job` runs a shell command in a stage, such as a test suite or a script. A job can publish outputs for resources in the same stage or a later stage to read. See [Jobs](/docs/delivery/concepts/stacks-and-jobs/#jobs).

## Agents

An `Agent` runs one of your [custom agents](/docs/ai/agents/custom/) in a stage and returns a structured response that later steps can use. Separately, a _decision gate_ uses TypeSafe's Jev model to evaluate a stage's stack preview and decide whether a release can enter the stage, based on the risk tolerance you define. See [Agents](/docs/delivery/concepts/agents/) and [Decision gates](/docs/delivery/concepts/stages-and-gates/#decision-gates).

## Runs

A _run_ takes one release through the stages. Each run gets its own _run stack_ where Pulumi Cloud executes the pipeline program. A run moves forward in _passes_. A pass is one execution of the pipeline program on the run stack, and each pass makes as much progress as the stages and gates allow.

## Sources and releases

A _source_ is a repository and branch. When a run is created, the pipeline fetches the code from each source and pins the run to one commit from each, so that every stage of the run works from the same code. A _release_ is what a run deploys: one commit for each repository source, and one upstream release for each [pipeline source](/docs/delivery/concepts/sources-and-triggers/#pipeline-sources). Releases are numbered in order.

A _trigger_ on a source controls whether a change starts a run. See [Sources and triggers](/docs/delivery/concepts/sources-and-triggers/).

## Artifacts

An _artifact_ is a named value that a stage publishes for a release once the release reaches it, such as a cluster endpoint or an image tag. Other pipelines read a stage's artifacts with a `PipelineSource`, which is how one pipeline hands values to the next. See [Artifacts](/docs/delivery/concepts/stages-and-gates/#artifacts).

## Next steps

- Register and deploy your first pipeline with [Get started](/docs/delivery/get-started/).
- Read about [sources and triggers](/docs/delivery/concepts/sources-and-triggers/).
- Order environments and add approvals with [stages and gates](/docs/delivery/concepts/stages-and-gates/).
- Configure [stacks and jobs](/docs/delivery/concepts/stacks-and-jobs/).
- Add an [agent](/docs/delivery/concepts/agents/) to a stage.
