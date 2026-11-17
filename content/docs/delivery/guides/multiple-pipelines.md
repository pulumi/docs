---
title_tag: Connecting Pulumi Delivery pipelines
meta_desc: Pass artifacts from an upstream Pulumi Delivery pipeline to a downstream one, and run several pipelines from a single monorepo.
title: Connecting pipelines
h1: Connecting pipelines
menu:
  delivery:
    name: Connecting pipelines
    parent: delivery-guides
    weight: 30
aliases: []
---

Most organizations manage more than one IaC pipeline. With Pulumi Delivery, you can connect them through [artifacts](/docs/delivery/concepts/stages-and-gates/#artifacts) and [pipeline sources](/docs/delivery/concepts/sources-and-triggers/#pipeline-sources).

## Passing artifacts between pipelines

In this example, an upstream pipeline publishes an `Artifact` from a pipeline stage:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as delivery from "@pulumi/delivery";

const repo = new delivery.GitHubSource("repo", {
    repository: "acme/platform",
    branch: "main",
    trigger: true,
});

const pipeline = new delivery.Pipeline("platform");

const prod = new delivery.Stage("prod", { pipeline });

const cluster = new delivery.Stacks("cluster", {
    stage: prod,
    stacks: { cluster: { stack: "platform-cluster/prod", source: repo, directory: "cluster" } },
});

new delivery.Artifact("clusterEndpoint", {
    stage: prod,
    value: cluster.outputs.apply((o) => o["cluster"]["endpoint"]),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_delivery as delivery

repo = delivery.GitHubSource(
    "repo", repository="acme/platform", branch="main", trigger=True
)

pipeline = delivery.Pipeline("platform")

prod = delivery.Stage("prod", pipeline=pipeline)

cluster = delivery.Stacks(
    "cluster",
    stage=prod,
    stacks={
        "cluster": {
            "stack": "platform-cluster/prod",
            "source": repo,
            "directory": "cluster",
        }
    },
)

delivery.Artifact(
    "clusterEndpoint",
    stage=prod,
    value=cluster.outputs.apply(lambda o: o["cluster"]["endpoint"]),
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
			Repository: pulumi.String("acme/platform"),
			Branch:     pulumi.String("main"),
			Trigger:    pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		pipeline, err := delivery.NewPipeline(ctx, "platform", nil)
		if err != nil {
			return err
		}

		prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{Pipeline: pipeline})
		if err != nil {
			return err
		}

		cluster, err := delivery.NewStacks(ctx, "cluster", &delivery.StacksArgs{
			Stage: prod,
			Stacks: delivery.StacksEntryMap{
				"cluster": delivery.StacksEntryArgs{Stack: pulumi.String("platform-cluster/prod"), Source: repo, Directory: pulumi.String("cluster")},
			},
		})
		if err != nil {
			return err
		}

		_, err = delivery.NewArtifact(ctx, "clusterEndpoint", &delivery.ArtifactArgs{
			Stage: prod,
			Value: cluster.Outputs.ApplyT(func(o map[string]map[string]interface{}) interface{} {
				return o["cluster"]["endpoint"]
			}),
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
        Repository = "acme/platform",
        Branch = "main",
        Trigger = true,
    });

    var pipeline = new Pipeline("platform");

    var prod = new Stage("prod", new StageArgs { Pipeline = pipeline });

    var cluster = new Stacks("cluster", new StacksArgs
    {
        Stage = prod,
        Stacks = { ["cluster"] = new StacksEntryArgs { Stack = "platform-cluster/prod", Source = repo, Directory = "cluster" } },
    });

    new Artifact("clusterEndpoint", new ArtifactArgs
    {
        Stage = prod,
        Value = cluster.Outputs.Apply(o => o["cluster"]["endpoint"]),
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
                .repository("acme/platform")
                .branch("main")
                .trigger(true)
                .build());

            var pipeline = new Pipeline("platform");

            var prod = new Stage("prod", StageArgs.builder().pipeline(pipeline).build());

            var cluster = new Stacks("cluster", StacksArgs.builder()
                .stage(prod)
                .stacks(Map.of("cluster", StacksEntryArgs.builder()
                    .stack("platform-cluster/prod")
                    .source(repo)
                    .directory("cluster")
                    .build()))
                .build());

            new Artifact("clusterEndpoint", ArtifactArgs.builder()
                .stage(prod)
                .value(cluster.outputs().applyValue(o -> (Object) o.get("cluster").get("endpoint")))
                .build());
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
name: platform-delivery
runtime: yaml

resources:
  repo:
    type: delivery:GitHubSource
    properties:
      repository: acme/platform
      branch: main
      trigger: true
  platform:
    type: delivery:Pipeline

  prod:
    type: delivery:Stage
    properties:
      pipeline: ${platform}
  cluster:
    type: delivery:Stacks
    properties:
      stage: ${prod}
      stacks:
        cluster:
          stack: platform-cluster/prod
          source: ${repo}
          directory: cluster
  clusterEndpoint:
    type: delivery:Artifact
    properties:
      stage: ${prod}
      value: ${cluster.outputs["cluster"]["endpoint"]}
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
  repository = "acme/platform"
  branch     = "main"
  trigger    = true
}

resource "delivery_pipeline" "platform" {}

resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.platform
}

resource "delivery_stacks" "cluster" {
  stage = delivery_stage.prod
  stacks = {
    cluster = { stack = "platform-cluster/prod", source = delivery_git_hub_source.repo, directory = "cluster" }
  }
}

resource "delivery_artifact" "clusterEndpoint" {
  stage = delivery_stage.prod
  value = delivery_stacks.cluster.outputs["cluster"]["endpoint"]
}
```

{{% /choosable %}}

{{< /chooser >}}

Downstream pipelines can read these artifacts with `PipelineSource`:

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

const platform = new delivery.PipelineSource("platform", {
    pipeline: "platform-delivery/main",
    stage: "prod",
    trigger: true,
});

const dev = new delivery.Stage("dev", { pipeline });

new delivery.Stacks("app", {
    stage: dev,
    stacks: {
        app: {
            stack: "shop-app/dev",
            source: repo,
            directory: "app",
            config: { clusterEndpoint: platform.artifacts.apply((a) => String(a["clusterEndpoint"])) },
        },
    },
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

platform = delivery.PipelineSource(
    "platform",
    pipeline="platform-delivery/main",
    stage="prod",
    trigger=True,
)

dev = delivery.Stage("dev", pipeline=pipeline)

delivery.Stacks(
    "app",
    stage=dev,
    stacks={
        "app": {
            "stack": "shop-app/dev",
            "source": repo,
            "directory": "app",
            "config": {
                "clusterEndpoint": platform.artifacts.apply(
                    lambda a: str(a["clusterEndpoint"])
                )
            },
        },
    },
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

		platform, err := delivery.NewPipelineSource(ctx, "platform", &delivery.PipelineSourceArgs{
			Pipeline: pulumi.String("platform-delivery/main"),
			Stage:    pulumi.String("prod"),
			Trigger:  pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		dev, err := delivery.NewStage(ctx, "dev", &delivery.StageArgs{Pipeline: pipeline})
		if err != nil {
			return err
		}

		_, err = delivery.NewStacks(ctx, "app", &delivery.StacksArgs{
			Stage: dev,
			Stacks: delivery.StacksEntryMap{
				"app": delivery.StacksEntryArgs{
					Stack:     pulumi.String("shop-app/dev"),
					Source:    repo,
					Directory: pulumi.String("app"),
					Config: pulumi.StringMap{
						"clusterEndpoint": pulumi.Sprintf("%v", platform.Artifacts.MapIndex(pulumi.String("clusterEndpoint"))),
					},
				},
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

    var platform = new PipelineSource("platform", new PipelineSourceArgs
    {
        Pipeline = "platform-delivery/main",
        Stage = "prod",
        Trigger = true,
    });

    var dev = new Stage("dev", new StageArgs { Pipeline = pipeline });

    new Stacks("app", new StacksArgs
    {
        Stage = dev,
        Stacks =
        {
            ["app"] = new StacksEntryArgs
            {
                Stack = "shop-app/dev",
                Source = repo,
                Directory = "app",
                Config =
                {
                    ["clusterEndpoint"] = platform.Artifacts.Apply(artifacts => artifacts["clusterEndpoint"].ToString()!),
                },
            },
        },
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

            var platform = new PipelineSource("platform", PipelineSourceArgs.builder()
                .pipeline("platform-delivery/main")
                .stage("prod")
                .trigger(true)
                .build());

            var dev = new Stage("dev", StageArgs.builder().pipeline(pipeline).build());

            new Stacks("app", StacksArgs.builder()
                .stage(dev)
                .stacks(Map.of(
                    "app", StacksEntryArgs.builder()
                        .stack("shop-app/dev")
                        .source(repo)
                        .directory("app")
                        .config(platform.artifacts().applyValue(artifacts -> Map.of(
                            "clusterEndpoint", String.valueOf(artifacts.get("clusterEndpoint")))))
                        .build()))
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
  platform:
    type: delivery:PipelineSource
    properties:
      pipeline: platform-delivery/main
      stage: prod
      trigger: true

  dev:
    type: delivery:Stage
    properties:
      pipeline: ${shop}
  app:
    type: delivery:Stacks
    properties:
      stage: ${dev}
      stacks:
        app:
          stack: shop-app/dev
          source: ${repo}
          directory: app
          config:
            clusterEndpoint: ${platform.artifacts["clusterEndpoint"]}
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

resource "delivery_pipeline_source" "platform" {
  pipeline = "platform-delivery/main"
  stage    = "prod"
  trigger  = true
}

resource "delivery_stage" "dev" {
  pipeline = delivery_pipeline.shop
}

resource "delivery_stacks" "app" {
  stage = delivery_stage.dev
  stacks = {
    app = {
      stack     = "shop-app/dev"
      source    = delivery_git_hub_source.repo
      directory = "app"
      config = {
        clusterEndpoint = delivery_pipeline_source.platform.artifacts["clusterEndpoint"]
      }
    }
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

With `trigger: true` on the `PipelineSource`, the downstream pipeline starts a run whenever the upstream stage deploys a new release.

Pipelines must belong to the same Pulumi organization, and the [service principal](/docs/administration/concepts/access-tokens/#how-team-tokens-are-identified) of each downstream pipeline must have read access to the upstream pipeline stack. This is because downstream runs read upstream artifacts as the downstream pipeline's service principal, not as the person who started the run. If the artifact is secret, pass it in `environment` instead of `config`.

## Patterns for monorepos

It's also common to keep several pipelines in one repository. Give each pipeline its own program directory and stack, and set its source's `trigger` paths so it runs only when its own files change.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
// delivery/shop/index.ts
import * as delivery from "@pulumi/delivery";

new delivery.GitHubSource("repo", {
    repository: "acme/monorepo",
    branch: "main",
    trigger: { paths: ["shop/**", "delivery/shop/**"] },
});

new delivery.Pipeline("shop");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# delivery/shop/__main__.py
import pulumi_delivery as delivery

delivery.GitHubSource(
    "repo",
    repository="acme/monorepo",
    branch="main",
    trigger={"paths": ["shop/**", "delivery/shop/**"]},
)

delivery.Pipeline("shop")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// delivery/shop/main.go
package main

import (
	"github.com/pulumi/pulumi-delivery/sdk/go/delivery"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := delivery.NewGitHubSource(ctx, "repo", &delivery.GitHubSourceArgs{
			Repository: pulumi.String("acme/monorepo"),
			Branch:     pulumi.String("main"),
			Trigger: delivery.SourceTriggerArgs{
				Paths: pulumi.StringArray{pulumi.String("shop/**"), pulumi.String("delivery/shop/**")},
			},
		})
		if err != nil {
			return err
		}

		_, err = delivery.NewPipeline(ctx, "shop", nil)
		return err
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// delivery/shop/Program.cs
using Pulumi;
using Pulumi.Delivery.Delivery;
using Pulumi.Delivery.Delivery.Inputs;

return await Deployment.RunAsync(() =>
{
    new GitHubSource("repo", new GitHubSourceArgs
    {
        Repository = "acme/monorepo",
        Branch = "main",
        Trigger = new SourceTriggerArgs { Paths = { "shop/**", "delivery/shop/**" } },
    });

    new Pipeline("shop");
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// delivery/shop/src/main/java/myproject/App.java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.delivery.delivery.*;
import com.pulumi.delivery.delivery.inputs.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            new GitHubSource("repo", GitHubSourceArgs.builder()
                .repository("acme/monorepo")
                .branch("main")
                .trigger(SourceTriggerArgs.builder()
                    .paths("shop/**", "delivery/shop/**")
                    .build())
                .build());

            new Pipeline("shop");
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# delivery/shop/Pulumi.yaml
name: shop-delivery
runtime: yaml

resources:
  repo:
    type: delivery:GitHubSource
    properties:
      repository: acme/monorepo
      branch: main
      trigger:
        paths:
          - shop/**
          - delivery/shop/**
  shop:
    type: delivery:Pipeline
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
# delivery/shop/main.tf
terraform {
  required_providers {
    delivery = {
      source = "pulumi/delivery"
    }
  }
}

resource "delivery_git_hub_source" "repo" {
  repository = "acme/monorepo"
  branch     = "main"
  trigger = {
    paths = ["shop/**", "delivery/shop/**"]
  }
}

resource "delivery_pipeline" "shop" {}
```

{{% /choosable %}}

{{< /chooser >}}

## Next steps

- Read more about [artifacts](/docs/delivery/concepts/stages-and-gates/#artifacts) and [pipeline sources](/docs/delivery/concepts/sources-and-triggers/#pipeline-sources).
- Check the [limits](/docs/delivery/limits/) on pipelines and runs.
