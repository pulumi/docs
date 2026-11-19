---
title_tag: Pulumi Delivery pipeline patterns
meta_desc: Common patterns for Pulumi Delivery pipelines, including helper functions, smoke tests after each deployment, and building container images once.
title: Pipeline patterns
h1: Pipeline patterns
menu:
  delivery:
    name: Pipeline patterns
    parent: delivery-guides
    weight: 20
aliases: []
---

<!-- TODO(launch): Once a Delivery `pulumi new` template is published, align these examples with the template's source and variable names. -->

This page shows common patterns for building pipelines with Pulumi Delivery. If you haven't registered a pipeline yet, start with [Get started](/docs/delivery/get-started/). The first example runs a `smoke.sh` script from the repository's `delivery` directory, shown in [Running smoke tests after deployment](#running-smoke-tests-after-deployment). The last section builds a container image once and deploys it to every stage.

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

const pipeline = new delivery.Pipeline("shop");

function deploy(stage: delivery.Stage, name: string, region: string) {
    const app = new delivery.Stacks(name, {
        stage,
        stacks: {
            app: { stack: `shop-app/${name}`, source: repo, directory: "app" },
        },
    });
    new delivery.Job(`smoke-${name}`, {
        stage,
        source: repo,
        directory: "delivery",
        command: "sh smoke.sh",
        environment: {
            ENDPOINT: app.outputs.apply((o) => String(o["app"]["endpoint"])),
            EXPECTED_REGION: region,
        },
    });
}

const dev = new delivery.Stage("dev", { pipeline });
deploy(dev, "dev", "eu-central-1");

const staging = new delivery.Stage("staging", { pipeline, from: [dev] });
deploy(staging, "staging", "eu-west-1");

const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.approval(),
});
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

pipeline = delivery.Pipeline("shop")


def deploy(stage: delivery.Stage, name: str, region: str):
    app = delivery.Stacks(
        name,
        stage=stage,
        stacks={
            "app": {
                "stack": f"shop-app/{name}",
                "source": repo,
                "directory": "app",
            },
        },
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

prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(kind="approval"),
)
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
		repo, err := delivery.NewGitHubSource(ctx, "repo",
			&delivery.GitHubSourceArgs{
				Repository: pulumi.String("acme/shop"),
				Branch:     pulumi.String("main"),
				Trigger: delivery.SourceTriggerArgs{
					Paths: pulumi.StringArray{
						pulumi.String("app/**"),
						pulumi.String("delivery/**"),
					},
				},
			})
		if err != nil {
			return err
		}

		pipeline, err := delivery.NewPipeline(ctx, "shop", nil)
		if err != nil {
			return err
		}

		deploy := func(
			stage *delivery.Stage, name string, region string,
		) error {
			app, err := delivery.NewStacks(ctx, name, &delivery.StacksArgs{
				Stage: stage,
				Stacks: delivery.StacksEntryMap{
					"app": delivery.StacksEntryArgs{
						Stack:     pulumi.String("shop-app/" + name),
						Source:    repo,
						Directory: pulumi.String("app"),
					},
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
					"ENDPOINT": app.Outputs.ApplyT(
						func(o map[string]map[string]interface{}) string {
							return fmt.Sprint(o["app"]["endpoint"])
						},
					).(pulumi.StringOutput),
					"EXPECTED_REGION": pulumi.String(region),
				},
			})
			return err
		}

		dev, err := delivery.NewStage(ctx, "dev", &delivery.StageArgs{
			Pipeline: pipeline,
		})
		if err != nil {
			return err
		}
		if err := deploy(dev, "dev", "eu-central-1"); err != nil {
			return err
		}

		staging, err := delivery.NewStage(ctx, "staging", &delivery.StageArgs{
			Pipeline: pipeline,
			From:     delivery.StageArray{dev},
		})
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
using Pulumi.Delivery;
using Pulumi.Delivery.Inputs;

return await Deployment.RunAsync(() =>
{
    var repo = new GitHubSource("repo", new GitHubSourceArgs
    {
        Repository = "acme/shop",
        Branch = "main",
        Trigger = new SourceTriggerArgs { Paths = { "app/**", "delivery/**" } },
    });

    var pipeline = new Pipeline("shop");

    void Deploy(Stage stage, string name, string region)
    {
        var app = new Stacks(name, new StacksArgs
        {
            Stage = stage,
            Stacks =
            {
                ["app"] = new StacksEntryArgs
                {
                    Stack = $"shop-app/{name}",
                    Source = repo,
                    Directory = "app",
                },
            },
        });
        new Job($"smoke-{name}", new JobArgs
        {
            Stage = stage,
            Source = repo,
            Directory = "delivery",
            Command = "sh smoke.sh",
            Environment =
            {
                ["ENDPOINT"] = app.Outputs.Apply(
                    o => o["app"]["endpoint"].ToString()!),
                ["EXPECTED_REGION"] = region,
            },
        });
    }

    var dev = new Stage("dev", new StageArgs { Pipeline = pipeline });
    Deploy(dev, "dev", "eu-central-1");

    var staging = new Stage("staging", new StageArgs
    {
        Pipeline = pipeline,
        From = { dev },
    });
    Deploy(staging, "staging", "eu-west-1");

    var prod = new Stage("prod", new StageArgs
    {
        Pipeline = pipeline,
        From = { staging },
        When = new RuleArgs { Kind = "approval" },
    });
    Deploy(prod, "prod", "us-west-2");
});
```

{{% /choosable %}}
{{% choosable language java %}}

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
                .trigger(SourceTriggerArgs.builder()
                    .paths("app/**", "delivery/**")
                    .build())
                .build());

            var pipeline = new Pipeline("shop");

            var dev = new Stage("dev", StageArgs.builder()
                .pipeline(pipeline)
                .build());
            deploy(repo, dev, "dev", "eu-central-1");

            var staging = new Stage("staging", StageArgs.builder()
                .pipeline(pipeline)
                .from(dev)
                .build());
            deploy(repo, staging, "staging", "eu-west-1");

            var prod = new Stage("prod", StageArgs.builder()
                .pipeline(pipeline)
                .from(staging)
                .when(RuleArgs.builder().kind("approval").build())
                .build());
            deploy(repo, prod, "prod", "us-west-2");
        });
    }

    static void deploy(GitHubSource repo, Stage stage, String name,
            String region) {
        var app = new Stacks(name, StacksArgs.builder()
            .stage(stage)
            .stacks(Map.of(
                "app", StacksEntryArgs.builder()
                    .stack("shop-app/" + name)
                    .source(repo)
                    .directory("app")
                    .build()))
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

To hold a stage until an endpoint is healthy instead of failing it, use an [HTTP gate](/docs/delivery/concepts/stages-and-gates/#http-gates).

## Building container images

Many pipelines deploy an application as a container image. Build the image once, in a build stage, and pass its digest to the stages that deploy it.

Avoid rebuilding in each stage, because each build can pull a newer base image, newer packages, or a newer build tool, so prod could run a different image from the one you tested in staging. Rebuilding the image also repeats a slow step in every stage. A digest, unlike a tag, always references the same image, so every stage runs exactly the image you tested, with a predictable, reproducible result.

In the build stage, use a stack whose Pulumi program uses the Docker Build provider's `Image` resource. The program pushes the image to a registry and exports a reference that includes the image digest as a stack output. The pipeline passes that output to the stacks that deploy the image through each entry's [`config`](/docs/delivery/concepts/stacks-and-jobs/#stacks).

This program, in the `image` directory, builds the application in `app` and reads the registry and its credentials from stack config:

{{< chooser language "typescript,python,go,csharp,java,hcl" >}}

{{% choosable language typescript %}}

<!-- This program is tested verbatim in https://github.com/pulumi/dac-docker-build-playground/tree/main/doc-pipeline-patterns-typescript. Update both together. -->

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as dockerBuild from "@pulumi/docker-build";

const config = new pulumi.Config();
// Registry host, for example "ghcr.io".
const registry = config.require("registry");
// Repository in that registry, for example "acme/shop".
const repository = config.require("repository");
// Source commit, passed by the pipeline.
const commit = config.require("commit");

const image = new dockerBuild.Image("shop", {
    context: { location: "../app" },
    // For example "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a".
    tags: [`${registry}/${repository}:${commit}`],
    push: true,
    // Credentials for pushing to the registry.
    registries: [{
        address: registry,
        username: config.require("registryUsername"),
        password: config.requireSecret("registryPassword"),
    }],
});

// The tag plus the digest, for example
// "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a@sha256:4e8d2f0c5b9a…".
export const imageRef = image.ref;
```

{{% /choosable %}}
{{% choosable language python %}}

<!-- This program is tested verbatim in https://github.com/pulumi/dac-docker-build-playground/tree/main/doc-pipeline-patterns-python. Update both together. -->

```python
import pulumi
import pulumi_docker_build as docker_build

config = pulumi.Config()
# Registry host, for example "ghcr.io".
registry = config.require("registry")
# Repository in that registry, for example "acme/shop".
repository = config.require("repository")
# Source commit, passed by the pipeline.
commit = config.require("commit")

image = docker_build.Image(
    "shop",
    context={"location": "../app"},
    # For example "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a".
    tags=[f"{registry}/{repository}:{commit}"],
    push=True,
    # Credentials for pushing to the registry.
    registries=[
        {
            "address": registry,
            "username": config.require("registryUsername"),
            "password": config.require_secret("registryPassword"),
        }
    ],
)

# The tag plus the digest, for example
# "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a@sha256:4e8d2f0c5b9a…".
pulumi.export("imageRef", image.ref)
```

{{% /choosable %}}
{{% choosable language go %}}

<!-- This program is tested verbatim in https://github.com/pulumi/dac-docker-build-playground/tree/main/doc-pipeline-patterns-go. Update both together. -->

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-docker-build/sdk/go/dockerbuild"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		// Registry host, for example "ghcr.io".
		registry := cfg.Require("registry")
		// Repository in that registry, for example "acme/shop".
		repository := cfg.Require("repository")
		// Source commit, passed by the pipeline.
		commit := cfg.Require("commit")

		image, err := dockerbuild.NewImage(ctx, "shop", &dockerbuild.ImageArgs{
			Context: &dockerbuild.BuildContextArgs{
				Location: pulumi.String("../app"),
			},
			// For example
			// "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a".
			Tags: pulumi.StringArray{
				pulumi.String(fmt.Sprintf("%s/%s:%s",
					registry, repository, commit)),
			},
			Push: pulumi.Bool(true),
			// Credentials for pushing to the registry.
			Registries: dockerbuild.RegistryArray{
				dockerbuild.RegistryArgs{
					Address:  pulumi.String(registry),
					Username: pulumi.String(cfg.Require("registryUsername")),
					Password: cfg.RequireSecret("registryPassword"),
				},
			},
		})
		if err != nil {
			return err
		}

		// The tag plus the digest, for example
		// "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a@sha256:4e8d2f0c5b9a…".
		ctx.Export("imageRef", image.Ref)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

<!-- This program is tested verbatim in https://github.com/pulumi/dac-docker-build-playground/tree/main/doc-pipeline-patterns-csharp. Update both together. -->

```csharp
using System.Collections.Generic;
using Pulumi;
using DockerBuild = Pulumi.DockerBuild;

return await Deployment.RunAsync(() =>
{
    var config = new Config();
    // Registry host, for example "ghcr.io".
    var registry = config.Require("registry");
    // Repository in that registry, for example "acme/shop".
    var repository = config.Require("repository");
    // Source commit, passed by the pipeline.
    var commit = config.Require("commit");

    var image = new DockerBuild.Image("shop", new DockerBuild.ImageArgs
    {
        Context = new DockerBuild.Inputs.BuildContextArgs
        {
            Location = "../app",
        },
        // For example
        // "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a".
        Tags = { $"{registry}/{repository}:{commit}" },
        Push = true,
        // Credentials for pushing to the registry.
        Registries =
        {
            new DockerBuild.Inputs.RegistryArgs
            {
                Address = registry,
                Username = config.Require("registryUsername"),
                Password = config.RequireSecret("registryPassword"),
            },
        },
    });

    // The tag plus the digest, for example
    // "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a@sha256:4e8d2f0c5b9a…".
    return new Dictionary<string, object?>
    {
        ["imageRef"] = image.Ref,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

<!-- This program is tested verbatim in https://github.com/pulumi/dac-docker-build-playground/tree/main/doc-pipeline-patterns-java. Update both together. -->

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.dockerbuild.Image;
import com.pulumi.dockerbuild.ImageArgs;
import com.pulumi.dockerbuild.inputs.BuildContextArgs;
import com.pulumi.dockerbuild.inputs.RegistryArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var config = ctx.config();
            // Registry host, for example "ghcr.io".
            var registry = config.require("registry");
            // Repository in that registry, for example "acme/shop".
            var repository = config.require("repository");
            // Source commit, passed by the pipeline.
            var commit = config.require("commit");

            var image = new Image("shop", ImageArgs.builder()
                .context(BuildContextArgs.builder().location("../app").build())
                // For example
                // "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a".
                .tags(registry + "/" + repository + ":" + commit)
                .push(true)
                // Credentials for pushing to the registry.
                .registries(RegistryArgs.builder()
                    .address(registry)
                    .username(config.require("registryUsername"))
                    .password(config.requireSecret("registryPassword"))
                    .build())
                .build());

            // The tag plus the digest, for example
            // "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a@sha256:4e8d2f0c5b9a…".
            ctx.export("imageRef", image.ref());
        });
    }
}
```

{{% /choosable %}}
{{% choosable language hcl %}}

<!-- This program is tested verbatim in https://github.com/pulumi/dac-docker-build-playground/tree/main/doc-pipeline-patterns-hcl. Update both together. -->

```hcl
terraform {
  required_providers {
    docker-build = {
      source  = "pulumi/docker-build"
      version = "0.0.23"
    }
  }
}

# Registry host, for example "ghcr.io".
variable "registry" {
  type = string
}

# Repository in that registry, for example "acme/shop".
variable "repository" {
  type = string
}

# Source commit, passed by the pipeline.
variable "commit" {
  type = string
}

variable "registryUsername" {
  type = string
}

variable "registryPassword" {
  type      = string
  sensitive = true
}

resource "docker-build_image" "shop" {
  context = {
    location = "../app"
  }
  # For example "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a".
  tags = ["${var.registry}/${var.repository}:${var.commit}"]
  push = true
  # Credentials for pushing to the registry.
  registries {
    address  = var.registry
    username = var.registryUsername
    password = var.registryPassword
  }
}

# The tag plus the digest, for example
# "ghcr.io/acme/shop:3f2c1a9e4b7d6c5f8a0b2d4e6f8a1c3e5b7d9f0a@sha256:4e8d2f0c5b9a…".
output "imageRef" {
  value = docker-build_image.shop.ref
}
```

{{% /choosable %}}

{{< /chooser >}}

This example pushes to GitHub Container Registry. To use another registry, such as Amazon ECR or Google Artifact Registry, change `registry`, `repository`, and the credentials. To pass credentials to the stack, see [Cloud credentials](/docs/delivery/guides/cloud-credentials/). The [`Image` resource reference](/registry/packages/docker-build/api-docs/image/) includes an example that pushes to Amazon ECR.

This pipeline builds on the [helper example](#reducing-duplication-with-helper-functions), without the smoke-test job to keep it short. It runs the image stack in a `build` stage and passes `imageRef` to the stacks in every later stage:

{{< chooser language "typescript,python,go,csharp,java,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as delivery from "@pulumi/delivery";

const repo = new delivery.GitHubSource("repo", {
    repository: "acme/shop",
    branch: "main",
    trigger: {
        paths: [
            "app/**",      // Application source and its Dockerfile.
            "image/**",    // Program that builds and pushes the image.
            "infra/**",    // Program that deploys the image.
            "delivery/**", // This pipeline program.
        ],
    },
});

const pipeline = new delivery.Pipeline("shop");

const build = new delivery.Stage("build", { pipeline });
const image = new delivery.Stacks("image", {
    stage: build,
    stacks: {
        image: {
            stack: "shop-image/build",
            source: repo,
            directory: "image",
            config: { commit: repo.commit },
        },
    },
});
// The outputs are empty until the image stack has run.
const imageRef = image.outputs.apply(o => String(o?.["image"]?.["imageRef"]));

function deploy(stage: delivery.Stage, name: string) {
    new delivery.Stacks(name, {
        stage,
        stacks: {
            app: {
                stack: `shop-app/${name}`,
                source: repo,
                directory: "infra",
                config: { imageRef },
            },
        },
    });
}

const dev = new delivery.Stage("dev", { pipeline, from: [build] });
deploy(dev, "dev");

const staging = new delivery.Stage("staging", { pipeline, from: [dev] });
deploy(staging, "staging");

const prod = new delivery.Stage("prod", {
    pipeline,
    from: [staging],
    when: delivery.approval(),
});
deploy(prod, "prod");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_delivery as delivery

repo = delivery.GitHubSource(
    "repo",
    repository="acme/shop",
    branch="main",
    trigger={
        "paths": [
            "app/**",       # Application source and its Dockerfile.
            "image/**",     # Program that builds and pushes the image.
            "infra/**",     # Program that deploys the image.
            "delivery/**",  # This pipeline program.
        ],
    },
)

pipeline = delivery.Pipeline("shop")

build = delivery.Stage("build", pipeline=pipeline)
image = delivery.Stacks(
    "image",
    stage=build,
    stacks={
        "image": {
            "stack": "shop-image/build",
            "source": repo,
            "directory": "image",
            "config": {"commit": repo.commit},
        },
    },
)
# The outputs are empty until the image stack has run.
image_ref = image.outputs.apply(
    lambda o: str((o or {}).get("image", {}).get("imageRef"))
)


def deploy(stage: delivery.Stage, name: str):
    delivery.Stacks(
        name,
        stage=stage,
        stacks={
            "app": {
                "stack": f"shop-app/{name}",
                "source": repo,
                "directory": "infra",
                "config": {"imageRef": image_ref},
            },
        },
    )


dev = delivery.Stage("dev", pipeline=pipeline, from_=[build])
deploy(dev, "dev")

staging = delivery.Stage("staging", pipeline=pipeline, from_=[dev])
deploy(staging, "staging")

prod = delivery.Stage(
    "prod",
    pipeline=pipeline,
    from_=[staging],
    when=delivery.RuleArgs(kind="approval"),
)
deploy(prod, "prod")
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
		repo, err := delivery.NewGitHubSource(ctx, "repo",
			&delivery.GitHubSourceArgs{
				Repository: pulumi.String("acme/shop"),
				Branch:     pulumi.String("main"),
				Trigger: delivery.SourceTriggerArgs{
					Paths: pulumi.StringArray{
						// Application source and its Dockerfile.
						pulumi.String("app/**"),
						// Program that builds and pushes the image.
						pulumi.String("image/**"),
						// Program that deploys the image.
						pulumi.String("infra/**"),
						// This pipeline program.
						pulumi.String("delivery/**"),
					},
				},
			})
		if err != nil {
			return err
		}

		pipeline, err := delivery.NewPipeline(ctx, "shop", nil)
		if err != nil {
			return err
		}

		build, err := delivery.NewStage(ctx, "build", &delivery.StageArgs{
			Pipeline: pipeline,
		})
		if err != nil {
			return err
		}
		image, err := delivery.NewStacks(ctx, "image", &delivery.StacksArgs{
			Stage: build,
			Stacks: delivery.StacksEntryMap{
				"image": delivery.StacksEntryArgs{
					Stack:     pulumi.String("shop-image/build"),
					Source:    repo,
					Directory: pulumi.String("image"),
					Config:    pulumi.StringMap{"commit": repo.Commit},
				},
			},
		})
		if err != nil {
			return err
		}
		imageRef := image.Outputs.ApplyT(
			func(o map[string]map[string]interface{}) string {
				return fmt.Sprint(o["image"]["imageRef"])
			},
		).(pulumi.StringOutput)

		deploy := func(stage *delivery.Stage, name string) error {
			_, err := delivery.NewStacks(ctx, name, &delivery.StacksArgs{
				Stage: stage,
				Stacks: delivery.StacksEntryMap{
					"app": delivery.StacksEntryArgs{
						Stack:     pulumi.String("shop-app/" + name),
						Source:    repo,
						Directory: pulumi.String("infra"),
						Config:    pulumi.StringMap{"imageRef": imageRef},
					},
				},
			})
			return err
		}

		dev, err := delivery.NewStage(ctx, "dev", &delivery.StageArgs{
			Pipeline: pipeline,
			From:     delivery.StageArray{build},
		})
		if err != nil {
			return err
		}
		if err := deploy(dev, "dev"); err != nil {
			return err
		}

		staging, err := delivery.NewStage(ctx, "staging", &delivery.StageArgs{
			Pipeline: pipeline,
			From:     delivery.StageArray{dev},
		})
		if err != nil {
			return err
		}
		if err := deploy(staging, "staging"); err != nil {
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
		return deploy(prod, "prod")
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

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
        Trigger = new SourceTriggerArgs
        {
            Paths =
            {
                "app/**",      // Application source and its Dockerfile.
                "image/**",    // Program that builds and pushes the image.
                "infra/**",    // Program that deploys the image.
                "delivery/**", // This pipeline program.
            },
        },
    });

    var pipeline = new Pipeline("shop");

    var build = new Stage("build", new StageArgs { Pipeline = pipeline });
    var image = new Stacks("image", new StacksArgs
    {
        Stage = build,
        Stacks =
        {
            ["image"] = new StacksEntryArgs
            {
                Stack = "shop-image/build",
                Source = repo,
                Directory = "image",
                Config = { ["commit"] = repo.Commit },
            },
        },
    });
    // The outputs are empty until the image stack has run.
    var imageRef = image.Outputs.Apply(o =>
        o?.GetValueOrDefault("image")
            ?.GetValueOrDefault("imageRef")
            ?.ToString() ?? "");

    void Deploy(Stage stage, string name)
    {
        new Stacks(name, new StacksArgs
        {
            Stage = stage,
            Stacks =
            {
                ["app"] = new StacksEntryArgs
                {
                    Stack = $"shop-app/{name}",
                    Source = repo,
                    Directory = "infra",
                    Config = { ["imageRef"] = imageRef },
                },
            },
        });
    }

    var dev = new Stage("dev", new StageArgs
    {
        Pipeline = pipeline,
        From = { build },
    });
    Deploy(dev, "dev");

    var staging = new Stage("staging", new StageArgs
    {
        Pipeline = pipeline,
        From = { dev },
    });
    Deploy(staging, "staging");

    var prod = new Stage("prod", new StageArgs
    {
        Pipeline = pipeline,
        From = { staging },
        When = new RuleArgs { Kind = "approval" },
    });
    Deploy(prod, "prod");
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.delivery.*;
import com.pulumi.delivery.inputs.*;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var repo = new GitHubSource("repo", GitHubSourceArgs.builder()
                .repository("acme/shop")
                .branch("main")
                .trigger(SourceTriggerArgs.builder().paths(
                    "app/**",      // Application source and its Dockerfile.
                    "image/**",    // Program that builds and pushes the image.
                    "infra/**",    // Program that deploys the image.
                    "delivery/**"  // This pipeline program.
                ).build())
                .build());

            var pipeline = new Pipeline("shop");

            var build = new Stage("build", StageArgs.builder()
                .pipeline(pipeline)
                .build());
            var image = new Stacks("image", StacksArgs.builder()
                .stage(build)
                .stacks(Map.of(
                    "image", StacksEntryArgs.builder()
                        .stack("shop-image/build")
                        .source(repo)
                        .directory("image")
                        .config(repo.commit().applyValue(
                            commit -> Map.of("commit", commit)))
                        .build()))
                .build());
            // The outputs are empty until the image stack has run.
            var imageRef = image.outputs().applyValue(o -> String.valueOf(
                o == null
                    ? null
                    : o.getOrDefault("image", Map.of()).get("imageRef")));

            var dev = new Stage("dev", StageArgs.builder()
                .pipeline(pipeline)
                .from(build)
                .build());
            deploy(repo, imageRef, dev, "dev");

            var staging = new Stage("staging", StageArgs.builder()
                .pipeline(pipeline)
                .from(dev)
                .build());
            deploy(repo, imageRef, staging, "staging");

            var prod = new Stage("prod", StageArgs.builder()
                .pipeline(pipeline)
                .from(staging)
                .when(RuleArgs.builder().kind("approval").build())
                .build());
            deploy(repo, imageRef, prod, "prod");
        });
    }

    static void deploy(GitHubSource repo, Output<String> imageRef, Stage stage,
            String name) {
        new Stacks(name, StacksArgs.builder()
            .stage(stage)
            .stacks(Map.of(
                "app", StacksEntryArgs.builder()
                    .stack("shop-app/" + name)
                    .source(repo)
                    .directory("infra")
                    .config(imageRef.applyValue(
                        ref -> Map.of("imageRef", ref)))
                    .build()))
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
    paths = [
      "app/**",      # Application source and its Dockerfile.
      "image/**",    # Program that builds and pushes the image.
      "infra/**",    # Program that deploys the image.
      "delivery/**", # This pipeline program.
    ]
  }
}

resource "delivery_pipeline" "shop" {}

resource "delivery_stage" "build" {
  pipeline = delivery_pipeline.shop
}

resource "delivery_stacks" "image" {
  stage = delivery_stage.build
  stacks = {
    image = {
      stack     = "shop-image/build"
      source    = delivery_git_hub_source.repo
      directory = "image"
      config    = { commit = delivery_git_hub_source.repo.commit }
    }
  }
}

resource "delivery_stage" "dev" {
  pipeline = delivery_pipeline.shop
  from     = [delivery_stage.build]
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
  # The outputs are empty until the image stack has run.
  image_ref = try(delivery_stacks.image.outputs["image"]["imageRef"], null)
  environments = {
    dev     = delivery_stage.dev
    staging = delivery_stage.staging
    prod    = delivery_stage.prod
  }
}

resource "delivery_stacks" "app" {
  for_each = local.environments
  stage    = each.value
  stacks = {
    app = {
      stack     = "shop-app/${each.key}"
      source    = delivery_git_hub_source.repo
      directory = "infra"
      config    = { imageRef = local.image_ref }
    }
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

The pipeline passes the commit to the image stack, which uses it as the image tag, so you can trace each image to its source. The stacks deploy the image by its digest, so the tag is only a label.

## Next steps

- Pass values between pipelines in [Connecting pipelines](/docs/delivery/guides/multiple-pipelines/).
- Check the [limits](/docs/delivery/limits/) on pipelines and runs.
