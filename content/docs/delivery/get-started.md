---
title_tag: Get started with Pulumi Delivery
meta_desc: Register your first Pulumi Delivery pipeline and deploy a release through dev, staging, and prod, with a manual gate before production.
title: Get started
h1: Get started with Pulumi Delivery
menu:
  delivery:
    name: Get started
    parent: delivery-home
    identifier: delivery-get-started
    weight: 5
aliases: []
---

<!-- TODO: Replace the project setup in this guide with a Delivery `pulumi new` template once it's published (for example, `pulumi new delivery-typescript`). The template should create the pipeline program, add the Delivery package, and create the pipeline stack, so the separate SDK install step and the hand-written program go away. Match the template's source and variable names. -->

In this guide, you'll write a pipeline that deploys an app through three environments, `dev`, `staging`, and `prod`, and pauses before `prod` until you tell it to continue. You'll register the pipeline with Pulumi Cloud, push a commit, and watch the release move through each stage. From then on, every push to `main` starts a new run.

{{% notes type="info" %}}
Pulumi Delivery is in public preview. Behavior, the SDK, and the REST API routes under `/api/preview/` can change before general availability.
{{% /notes %}}

## Before you begin

You'll need:

- A Pulumi Cloud organization on any edition
- Pulumi CLI v3.277.0 or later.
- A GitHub repository you can push to, with the [GitHub integration](/docs/integrations/version-control/github-app/) installed for your organization and given access to that repository.
- The toolchain for the language you'll write the pipeline in, such as Node.js for TypeScript

This guide uses a repository named `acme/shop` on the `main` branch. Replace `acme/shop` with your own repository as you go.

## Lay out the repository

The pipeline program and the project it deploys live side by side in the same repository:

```text
app/        the project the pipeline deploys
delivery/   the pipeline program
```

## Create the app stacks

Delivery updates existing stacks but doesn't create them, so you'll create one stack for each environment first. To keep the focus on the pipeline, the `app` project doesn't create any cloud resources. It only returns a URL built from the stack name. Create `app/Pulumi.yaml`:

```yaml
name: shop-app
runtime: yaml
outputs:
  url: https://${pulumi.stack}.shop.example.com
```

Then create a `dev`, `staging`, and `prod` stack for the project:

```bash
cd app
pulumi stack init dev
pulumi stack init staging
pulumi stack init prod
cd ..
```

Because the project creates no resources, Delivery doesn't need any cloud credentials to deploy it. When you're ready to deploy real infrastructure, see [Cloud credentials](/docs/delivery/guides/cloud-credentials/).

## Write the pipeline program

The pipeline program is a Pulumi project of its own, written in any Pulumi language. Create it in the `delivery` directory along with its stack, `main`:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```bash
mkdir delivery && cd delivery
pulumi new typescript --name shop-delivery --stack main --yes
npm install @pulumi/delivery
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
mkdir delivery && cd delivery
pulumi new python --name shop-delivery --stack main --yes
echo "pulumi_delivery" >> requirements.txt
pulumi install
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
mkdir delivery && cd delivery
pulumi new go --name shop-delivery --stack main --yes
go get github.com/pulumi/pulumi-delivery/sdk
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
mkdir delivery && cd delivery
pulumi new csharp --name shop-delivery --stack main --yes
dotnet add package Pulumi.Delivery
```

{{% /choosable %}}
{{% choosable language java %}}

```bash
mkdir delivery && cd delivery
pulumi new java --name shop-delivery --stack main --yes
```

Then add the Delivery SDK to the `dependencies` in `pom.xml`:

```xml
<dependency>
    <groupId>com.pulumi</groupId>
    <artifactId>delivery</artifactId>
    <version>0.1.0</version>
</dependency>
```

{{% /choosable %}}
{{% choosable language yaml %}}

```bash
mkdir delivery && cd delivery
pulumi new yaml --name shop-delivery --stack main --yes
pulumi package add delivery
```

{{% /choosable %}}
{{% choosable language hcl %}}

<!-- TODO(launch): Confirm the setup steps for an HCL pipeline program, including whether it needs `pulumi package add delivery` or only the `required_providers` block. -->

Create `delivery/Pulumi.yaml` with the HCL runtime:

```yaml
name: shop-delivery
runtime: hcl
```

Then create the pipeline stack:

```bash
cd delivery
pulumi stack init main
```

{{% /choosable %}}

{{< /chooser >}}

In a language with an SDK, the install step adds the Delivery SDK to the project's dependency file, such as `package.json` or `requirements.txt`. In YAML, `pulumi package add delivery` writes a `packages` entry to `Pulumi.yaml`. Commit that file, because Pulumi Cloud installs the package from it for each run. An HCL program names the provider in its `required_providers` block.

Now replace the program that `pulumi new` created with the pipeline. The program declares the repository as a source, three stages in order, and the `app` stack each stage updates:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

In `index.ts`:

```typescript
import * as delivery from "@pulumi/delivery";

const repo = new delivery.GitHubSource("repo", {
    repository: "acme/shop",
    branch: "main",
    trigger: true,
});

const pipeline = new delivery.Pipeline("shop");

const dev = new delivery.Stage("dev", { pipeline });
const staging = new delivery.Stage("staging", { pipeline, from: [dev] });
const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.manual({ description: "Check staging before you ship to prod." }),
});

for (const [env, stage] of Object.entries({ dev, staging, prod })) {
    new delivery.Stacks(env, {
        stage,
        stacks: {
            app: { stack: `shop-app/${env}`, source: repo, directory: "app" },
        },
    });
}
```

{{% /choosable %}}
{{% choosable language python %}}

In `__main__.py`:

```python
import pulumi_delivery as delivery

repo = delivery.GitHubSource(
    "repo", repository="acme/shop", branch="main", trigger=True
)

pipeline = delivery.Pipeline("shop")

dev = delivery.Stage("dev", pipeline=pipeline)
staging = delivery.Stage("staging", pipeline=pipeline, from_=[dev])
prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(kind="manual", description="Check staging before you ship to prod."),
)

for env, stage in {"dev": dev, "staging": staging, "prod": prod}.items():
    delivery.Stacks(
        env,
        stage=stage,
        stacks={
            "app": {"stack": f"shop-app/{env}", "source": repo, "directory": "app"},
        },
    )
```

{{% /choosable %}}
{{% choosable language go %}}

In `main.go`:

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
			Trigger:    pulumi.Bool(true),
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
		staging, err := delivery.NewStage(ctx, "staging", &delivery.StageArgs{
			Pipeline: pipeline,
			From:     delivery.StageArray{dev},
		})
		if err != nil {
			return err
		}
		prod, err := delivery.NewStage(ctx, "prod", &delivery.StageArgs{
			Pipeline: pipeline,
			From:     delivery.StageArray{staging},
			When: delivery.RuleArgs{
				Kind:        pulumi.String("manual"),
				Description: pulumi.String("Check staging before you ship to prod."),
			},
		})
		if err != nil {
			return err
		}

		for env, stage := range map[string]*delivery.Stage{"dev": dev, "staging": staging, "prod": prod} {
			_, err := delivery.NewStacks(ctx, env, &delivery.StacksArgs{
				Stage: stage,
				Stacks: delivery.StacksEntryMap{
					"app": delivery.StacksEntryArgs{Stack: pulumi.String("shop-app/" + env), Source: repo, Directory: pulumi.String("app")},
				},
			})
			if err != nil {
				return err
			}
		}
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

In `Program.cs`:

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Delivery;
using Pulumi.Delivery.Inputs;

return await Deployment.RunAsync(() =>
{
    var repo = new GitHubSource("repo", new GitHubSourceArgs
    {
        Repository = "acme/shop",
        Branch = "main",
        Trigger = true,
    });

    var pipeline = new Pipeline("shop");

    var dev = new Stage("dev", new StageArgs { Pipeline = pipeline });
    var staging = new Stage("staging", new StageArgs { Pipeline = pipeline, From = { dev } });
    var prod = new Stage("prod", new StageArgs
    {
        Pipeline = pipeline,
        From = { staging },
        When = new RuleArgs { Kind = "manual", Description = "Check staging before you ship to prod." },
    });

    var stages = new Dictionary<string, Stage> { ["dev"] = dev, ["staging"] = staging, ["prod"] = prod };
    foreach (var (env, stage) in stages)
    {
        new Stacks(env, new StacksArgs
        {
            Stage = stage,
            Stacks =
            {
                ["app"] = new StacksEntryArgs { Stack = $"shop-app/{env}", Source = repo, Directory = "app" },
            },
        });
    }
});
```

{{% /choosable %}}
{{% choosable language java %}}

In `src/main/java/myproject/App.java`:

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.delivery.*;
import com.pulumi.delivery.inputs.*;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var repo = new GitHubSource("repo", GitHubSourceArgs.builder()
                .repository("acme/shop")
                .branch("main")
                .trigger(true)
                .build());

            var pipeline = new Pipeline("shop");

            var dev = new Stage("dev", StageArgs.builder().pipeline(pipeline).build());
            var staging = new Stage("staging", StageArgs.builder().pipeline(pipeline).from(dev).build());
            var prod = new Stage("prod", StageArgs.builder()
                .pipeline(pipeline)
                .from(staging)
                .when(RuleArgs.builder()
                    .kind("manual")
                    .description("Check staging before you ship to prod.")
                    .build())
                .build());

            Map.of("dev", dev, "staging", staging, "prod", prod).forEach((env, stage) ->
                new Stacks(env, StacksArgs.builder()
                    .stage(stage)
                    .stacks(Map.of(
                        "app", StacksEntryArgs.builder().stack("shop-app/" + env).source(repo).directory("app").build()))
                    .build()));
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

In `Pulumi.yaml`, keep the `packages` entry and replace the rest with:

```yaml
name: shop-delivery
runtime: yaml

resources:
  repo:
    type: delivery:GitHubSource
    properties:
      repository: acme/shop
      branch: main
      trigger: true
  shop:
    type: delivery:Pipeline

  dev:
    type: delivery:Stage
    properties:
      pipeline: ${shop}
  staging:
    type: delivery:Stage
    properties:
      pipeline: ${shop}
      from:
        - ${dev}
  prod:
    type: delivery:Stage
    properties:
      pipeline: ${shop}
      from:
        - ${staging}
      when:
        kind: manual
        description: Check staging before you ship to prod.

  devStacks:
    type: delivery:Stacks
    properties:
      stage: ${dev}
      stacks:
        app: { stack: shop-app/dev, source: "${repo}", directory: app }
  stagingStacks:
    type: delivery:Stacks
    properties:
      stage: ${staging}
      stacks:
        app: { stack: shop-app/staging, source: "${repo}", directory: app }
  prodStacks:
    type: delivery:Stacks
    properties:
      stage: ${prod}
      stacks:
        app: { stack: shop-app/prod, source: "${repo}", directory: app }
```

{{% /choosable %}}
{{% choosable language hcl %}}

In `main.tf`:

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
  trigger    = true
}

resource "delivery_pipeline" "shop" {}

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
  when = {
    kind        = "manual"
    description = "Check staging before you ship to prod."
  }
}

locals {
  environments = {
    dev     = delivery_stage.dev
    staging = delivery_stage.staging
    prod    = delivery_stage.prod
  }
}

resource "delivery_stacks" "env" {
  for_each = local.environments
  stage    = each.value
  stacks = {
    app = { stack = "shop-app/${each.key}", source = delivery_git_hub_source.repo, directory = "app" }
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

Here's what each part does:

- The `GitHubSource` points at `main` in your repository. Setting `trigger` to `true` starts a run on every push to `main`.
- The `Pipeline` resource declares the pipeline. A pipeline program declares exactly one.
- The three `Stage` resources run in order, because each one lists the stage before it in `from`. The `prod` stage also has a manual gate in `when`, so a release waits there until someone continues it.
- The loop adds a `Stacks` resource to each stage, which runs `pulumi up` on that environment's `shop-app` stack.

<!-- TODO(launch): Only TypeScript was run end to end (2026-11-17, delivery 0.0.1-alpha.6). The other languages are adapted from the launch blog post, and C# and Java haven't been compiled. Run each one against the GA build. -->

## Register the pipeline

Register the pipeline from the `delivery` directory:

```bash
pulumi delivery register
```

Registering tells Pulumi Cloud about the pipeline and writes the program's location in your repository to the `delivery:source` setting in `Pulumi.main.yaml`. It doesn't start a run, so the output lists each stage as waiting for one. Commit everything, including that config file, and push:

```bash
cd ..
git add app delivery
git commit -m "Add the shop delivery pipeline"
git push origin main
```

The push matches the source's trigger, so it starts your first run.

## Watch the release

In the [Pulumi Cloud console](https://app.pulumi.com), navigate to **Delivery** > **Pipelines** and select `shop-delivery/main`. Your run is listed under **In progress**. Select it to open the run page.

The `dev` stage updates `shop-app/dev`, and once it succeeds, `staging` updates `shop-app/staging`. The run then pauses at the manual gate in front of `prod`, and its status reads "Waiting for someone to continue at prod".

In the run graph, select the **Manual** gate before `prod`. It shows the description you gave it. Select **Continue**, and Delivery updates `shop-app/prod`. Once the run finishes, open any of the three `shop-app` stacks to see the update the pipeline ran and the `url` output for that environment.

That's your first release. Every push to `main` from now on starts a new run, pinned to that commit, so the code that passed `staging` is the code that reaches `prod`.

## Next steps

- Learn how [pipelines, runs, and releases](/docs/delivery/concepts/) fit together, and how to [test the pipeline locally](/docs/delivery/concepts/#testing-locally) while you iterate on it.
- Require named approvers before `prod` with an [approval gate](/docs/delivery/concepts/stages-and-gates/#approval-gates).
- Give each stage [cloud credentials](/docs/delivery/guides/cloud-credentials/) so it can deploy real infrastructure.
- Add tests and smoke checks with the [pipeline patterns](/docs/delivery/guides/pipeline-patterns/) guide.
