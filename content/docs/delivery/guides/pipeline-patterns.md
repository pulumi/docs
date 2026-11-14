---
title_tag: Pulumi Delivery pipeline patterns
meta_desc: Common patterns for Pulumi Delivery pipelines, including helper functions that reduce duplication and smoke tests after each deployment.
title: Pipeline patterns
h1: Pipeline patterns
menu:
  delivery:
    name: Pipeline patterns
    parent: delivery-guides
    weight: 20
aliases: []
---

<!-- TODO(launch): Once a Delivery `pulumi new` template is published, align these examples with the template's source and variable names. When Get started is restored, link it from this intro. -->

This page shows common patterns for building pipelines with Pulumi Delivery. The examples run a `smoke.sh` script from the repository's `delivery` directory, shown in [Running smoke tests after deployment](#running-smoke-tests-after-deployment).

## Reducing duplication with helper functions

When your environments differ by only a few values, you can write functions in your language of choice to extract common functionality and avoid repetition. In this example, a function defines the `Stacks` and `Job` resources for each stage of the pipeline:

{{< chooser language "typescript,python,go,csharp,java,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as delivery from "@pulumi/delivery";

const repo = new delivery.GitHubSource("repo", {
    repository: "acme/shop",
    branch: "main",
    trigger: { paths: ["app/**", "delivery/**"] },
});

const pipeline = new delivery.Pipeline("shop", {
    program: { source: repo, directory: "delivery" },
});

function deploy(stage: delivery.Stage, name: string, region: string) {
    const app = new delivery.Stacks(name, {
        stage,
        stacks: { app: { stack: `shop-app/${name}`, source: repo, directory: "app" } },
    });
    new delivery.Job(`smoke-${name}`, {
        stage,
        source: repo,
        directory: "delivery",
        command: "sh smoke.sh",
        environment: {
            ENDPOINT: app.outputs.apply(o => String(o["app"]["endpoint"])),
            EXPECTED_REGION: region,
        },
    });
}

const dev = new delivery.Stage("dev", { pipeline });
deploy(dev, "dev", "eu-central-1");

const staging = new delivery.Stage("staging", { pipeline, from: [dev] });
deploy(staging, "staging", "eu-west-1");

const prod = new delivery.Stage("prod", { pipeline, from: [staging], when: delivery.approval() });
deploy(prod, "prod", "us-west-2");
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

pipeline = delivery.Pipeline("shop", program={"source": repo, "directory": "delivery"})


def deploy(stage: delivery.Stage, name: str, region: str):
    app = delivery.Stacks(
        name,
        stage=stage,
        stacks={"app": {"stack": f"shop-app/{name}", "source": repo, "directory": "app"}},
    )
    delivery.Job(
        f"smoke-{name}",
        stage=stage,
        source=repo,
        directory="delivery",
        command="sh smoke.sh",
        environment={
            "ENDPOINT": app.outputs.apply(lambda o: str(o["app"]["endpoint"])),
            "EXPECTED_REGION": region,
        },
    )


dev = delivery.Stage("dev", pipeline=pipeline)
deploy(dev, "dev", "eu-central-1")

staging = delivery.Stage("staging", pipeline=pipeline, from_=[dev])
deploy(staging, "staging", "eu-west-1")

prod = delivery.Stage("prod", pipeline=pipeline, from_=[staging], when=delivery.RuleArgs(kind="approval"))
deploy(prod, "prod", "us-west-2")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"fmt"

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

		pipeline, err := delivery.NewPipeline(ctx, "shop", &delivery.PipelineArgs{
			Program: &delivery.ProgramSourceArgs{Source: repo, Directory: pulumi.String("delivery")},
		})
		if err != nil {
			return err
		}

		deploy := func(stage *delivery.Stage, name string, region string) error {
			app, err := delivery.NewStacks(ctx, name, &delivery.StacksArgs{
				Stage: stage,
				Stacks: delivery.StacksEntryMap{
					"app": delivery.StacksEntryArgs{Stack: pulumi.String("shop-app/" + name), Source: repo, Directory: pulumi.String("app")},
				},
			})
			if err != nil {
				return err
			}
			_, err = delivery.NewJob(ctx, "smoke-"+name, &delivery.JobArgs{
				Stage:     stage,
				Source:    repo,
				Directory: pulumi.String("delivery"),
				Command:   pulumi.String("sh smoke.sh"),
				Environment: pulumi.StringMap{
					"ENDPOINT": app.Outputs.ApplyT(func(o map[string]map[string]interface{}) string {
						return fmt.Sprint(o["app"]["endpoint"])
					}).(pulumi.StringOutput),
					"EXPECTED_REGION": pulumi.String(region),
				},
			})
			return err
		}

		dev, err := delivery.NewStage(ctx, "dev", &delivery.StageArgs{Pipeline: pipeline})
		if err != nil {
			return err
		}
		if err := deploy(dev, "dev", "eu-central-1"); err != nil {
			return err
		}

		staging, err := delivery.NewStage(ctx, "staging", &delivery.StageArgs{Pipeline: pipeline, From: delivery.StageArray{dev}})
		if err != nil {
			return err
		}
		if err := deploy(staging, "staging", "eu-west-1"); err != nil {
			return err
		}

		prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
			Pipeline: pipeline,
			From:     delivery.StageArray{staging},
			When:     delivery.RuleArgs{Kind: pulumi.String("approval")},
		})
		if err != nil {
			return err
		}
		return deploy(prod, "prod", "us-west-2")
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

    var pipeline = new Pipeline("shop", new PipelineArgs
    {
        Program = new ProgramSourceArgs { Source = repo, Directory = "delivery" },
    });

    void Deploy(Stage stage, string name, string region)
    {
        var app = new Stacks(name, new StacksArgs
        {
            Stage = stage,
            Stacks = { ["app"] = new StacksEntryArgs { Stack = $"shop-app/{name}", Source = repo, Directory = "app" } },
        });
        new Job($"smoke-{name}", new JobArgs
        {
            Stage = stage,
            Source = repo,
            Directory = "delivery",
            Command = "sh smoke.sh",
            Environment =
            {
                ["ENDPOINT"] = app.Outputs.Apply(o => o["app"]["endpoint"].ToString()!),
                ["EXPECTED_REGION"] = region,
            },
        });
    }

    var dev = new Stage("dev", new StageArgs { Pipeline = pipeline });
    Deploy(dev, "dev", "eu-central-1");

    var staging = new Stage("staging", new StageArgs { Pipeline = pipeline, From = { dev } });
    Deploy(staging, "staging", "eu-west-1");

    var prod = new Stage("prod", new StageArgs { Pipeline = pipeline, From = { staging }, When = new RuleArgs { Kind = "approval" } });
    Deploy(prod, "prod", "us-west-2");
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

            var pipeline = new Pipeline("shop", PipelineArgs.builder()
                .program(ProgramSourceArgs.builder().source(repo).directory("delivery").build())
                .build());

            var dev = new Stage("dev", StageArgs.builder().pipeline(pipeline).build());
            deploy(repo, dev, "dev", "eu-central-1");

            var staging = new Stage("staging", StageArgs.builder().pipeline(pipeline).from(dev).build());
            deploy(repo, staging, "staging", "eu-west-1");

            var prod = new Stage("prod", StageArgs.builder()
                .pipeline(pipeline)
                .from(staging)
                .when(RuleArgs.builder().kind("approval").build())
                .build());
            deploy(repo, prod, "prod", "us-west-2");
        });
    }

    static void deploy(GitHubSource repo, Stage stage, String name, String region) {
        var app = new Stacks(name, StacksArgs.builder()
            .stage(stage)
            .stacks(Map.of(
                "app", StacksEntryArgs.builder().stack("shop-app/" + name).source(repo).directory("app").build()))
            .build());
        new Job("smoke-" + name, JobArgs.builder()
            .stage(stage)
            .source(repo)
            .directory("delivery")
            .command("sh smoke.sh")
            .environment(app.outputs().applyValue(o -> Map.of(
                "ENDPOINT", String.valueOf(o.get("app").get("endpoint")),
                "EXPECTED_REGION", region)))
            .build());
    }
}
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "delivery_git_hub_source" "repo" {
  repository = "acme/shop"
  branch     = "main"
  trigger = {
    paths = ["app/**", "delivery/**"]
  }
}

resource "delivery_pipeline" "shop" {
  program = {
    source    = delivery_git_hub_source.repo
    directory = "delivery"
  }
}

resource "delivery_stage" "dev" {
  pipeline = delivery_pipeline.shop
}

resource "delivery_stage" "staging" {
  pipeline = delivery_pipeline.shop
  from     = [delivery_stage.dev]
}

resource "delivery_stage" "prod" {
  pipeline = delivery_pipeline.shop
  from     = [delivery_stage.staging]
  when     = { kind = "approval" }
}

locals {
  environments = {
    dev     = { stage = delivery_stage.dev, region = "eu-central-1" }
    staging = { stage = delivery_stage.staging, region = "eu-west-1" }
    prod    = { stage = delivery_stage.prod, region = "us-west-2" }
  }
}

resource "delivery_stacks" "app" {
  for_each = local.environments
  stage    = each.value.stage
  stacks = {
    app = {
      stack     = "shop-app/${each.key}"
      source    = delivery_git_hub_source.repo
      directory = "app"
    }
  }
}

resource "delivery_job" "smoke" {
  for_each  = local.environments
  stage     = each.value.stage
  source    = delivery_git_hub_source.repo
  directory = "delivery"
  command   = "sh smoke.sh"
  environment = {
    ENDPOINT        = delivery_stacks.app[each.key].outputs["app"]["endpoint"]
    EXPECTED_REGION = each.value.region
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Resource names must be unique, so build them from the environment name. The region itself comes from each target stack's config file (for AWS, `aws:region` in `Pulumi.<stack>.yaml`). The `region` argument is passed to the job as `EXPECTED_REGION`, for checks you add to `smoke.sh`.

## Running smoke tests after deployment

Put a `Job` in the same stage as the `Stacks` resource it tests, so the test runs right after the deploy and before the release moves on. A job can read outputs from its own stage or an earlier one, but not from a later stage. This `smoke.sh` retries, because a new deployment can take a few seconds to answer. On success, it publishes a `checked` output through `DELIVERY_OUTPUTS` (see [Job outputs](/docs/delivery/concepts/stacks-and-jobs/#job-outputs)):

```bash
set -eu
for attempt in 1 2 3 4 5; do
    if curl -fsS "$ENDPOINT/health" > /dev/null; then
        echo "{\"checked\": \"$ENDPOINT\"}" > "$DELIVERY_OUTPUTS"
        exit 0
    fi
    sleep 10
done
echo "Smoke test failed for $ENDPOINT" >&2
exit 1
```

`curl -fsS` makes an HTTP error return a non-zero exit code. When the job fails, its stage fails and later stages don't start. Fix the problem, then retry the run from its page in the Pulumi Cloud console.

## Next steps

- Pass values between pipelines in [Connecting pipelines](/docs/delivery/guides/multiple-pipelines/).
- Check the [limits](/docs/delivery/limits/) on pipelines and runs.
