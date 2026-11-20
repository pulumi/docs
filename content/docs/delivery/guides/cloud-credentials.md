---
title_tag: Cloud credentials for Pulumi Delivery
meta_desc: Give each stage of a Pulumi Delivery pipeline its own cloud credentials, as environment variables on a stack update or with Pulumi ESC and OIDC.
title: Cloud credentials
h1: Cloud credentials for each stage
menu:
  delivery:
    name: Cloud credentials
    parent: delivery-guides
    weight: 10
aliases: []
---

Delivery pipelines manage multiple stacks, and each stack needs credentials to deploy into its cloud environment.

You can provide them in two ways: by passing them through the pipeline in each `Stacks` entry's `environment`, or by using Pulumi ESC (Environments, Secrets, and Configuration) to grant each stack short-lived cloud credentials through OpenID Connect (OIDC).

## Passing credentials through the pipeline

One way to provide credentials is to store them in the pipeline stack's config and pass them to each stack update as environment variables:

```bash
pulumi config set awsAccessKeyId <your-access-key-id>
pulumi config set --secret awsSecretAccessKey <your-secret-access-key>
```

Then read them in the pipeline program and pass them in the `Stacks` entry's `environment`, a map of environment variables for that stack update. Values you read with `requireSecret` stay secret:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as delivery from "@pulumi/delivery";

const cfg = new pulumi.Config();

new delivery.Stacks("prod", {
    stage: prod,
    stacks: {
        app: {
            stack: "shop-infra/prod",
            source: repo,
            directory: "infra",
            environment: {
                AWS_ACCESS_KEY_ID: cfg.require("awsAccessKeyId"),
                AWS_SECRET_ACCESS_KEY: cfg.requireSecret("awsSecretAccessKey"),
            },
        },
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_delivery as delivery

cfg = pulumi.Config()

delivery.Stacks(
    "prod",
    stage=prod,
    stacks={
        "app": {
            "stack": "shop-infra/prod",
            "source": repo,
            "directory": "infra",
            "environment": {
                "AWS_ACCESS_KEY_ID": cfg.require("awsAccessKeyId"),
                "AWS_SECRET_ACCESS_KEY": cfg.require_secret("awsSecretAccessKey"),
            },
        },
    },
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
cfg := config.New(ctx, "")

_, err = delivery.NewStacks(ctx, "prod", &delivery.StacksArgs{
	Stage: prod,
	Stacks: delivery.StacksEntryMap{
		"app": delivery.StacksEntryArgs{
			Stack:     pulumi.String("shop-infra/prod"),
			Source:    repo,
			Directory: pulumi.String("infra"),
			Environment: pulumi.StringMap{
				"AWS_ACCESS_KEY_ID":     pulumi.String(cfg.Require("awsAccessKeyId")),
				"AWS_SECRET_ACCESS_KEY": cfg.RequireSecret("awsSecretAccessKey"),
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
var cfg = new Config();

new Stacks("prod", new StacksArgs
{
    Stage = prod,
    Stacks =
    {
        ["app"] = new StacksEntryArgs
        {
            Stack = "shop-infra/prod",
            Source = repo,
            Directory = "infra",
            Environment =
            {
                ["AWS_ACCESS_KEY_ID"] = cfg.Require("awsAccessKeyId"),
                ["AWS_SECRET_ACCESS_KEY"] = cfg.RequireSecret("awsSecretAccessKey"),
            },
        },
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var cfg = ctx.config();
var awsAccessKeyId = cfg.require("awsAccessKeyId");

new Stacks("prod", StacksArgs.builder()
    .stage(prod)
    .stacks(Map.of(
        "app", StacksEntryArgs.builder()
            .stack("shop-infra/prod")
            .source(repo)
            .directory("infra")
            .environment(cfg.requireSecret("awsSecretAccessKey").applyValue(awsSecretAccessKey -> Map.of(
                "AWS_ACCESS_KEY_ID", awsAccessKeyId,
                "AWS_SECRET_ACCESS_KEY", awsSecretAccessKey)))
            .build()))
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
config:
  awsAccessKeyId:
    type: string
  awsSecretAccessKey:
    type: string
    secret: true

resources:
  prodApp:
    type: delivery:Stacks
    properties:
      stage: ${prod}
      stacks:
        app:
          stack: shop-infra/prod
          source: ${repo}
          directory: infra
          environment:
            AWS_ACCESS_KEY_ID: ${awsAccessKeyId}
            AWS_SECRET_ACCESS_KEY: ${awsSecretAccessKey}
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

variable "awsAccessKeyId" {
  type = string
}

variable "awsSecretAccessKey" {
  type      = string
  sensitive = true
}

resource "delivery_stacks" "prod" {
  stage = delivery_stage.prod
  stacks = {
    app = {
      stack     = "shop-infra/prod"
      source    = delivery_git_hub_source.repo
      directory = "infra"
      environment = {
        AWS_ACCESS_KEY_ID     = var.awsAccessKeyId
        AWS_SECRET_ACCESS_KEY = var.awsSecretAccessKey
      }
    }
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

The drawback of this approach is that it keeps long-lived credentials in the pipeline stack's config file. To use short-lived credentials instead, use Pulumi ESC.

## Using short-lived credentials with Pulumi ESC

With ESC, you can give each stack an [ESC environment](/docs/esc/concepts/environments/) that issues short-lived credentials through OIDC, such as one built with the [`aws-login`](/docs/esc/providers/login/aws-login/) provider. To do so, import the environment in the stack's config file, for example `infra/Pulumi.dev.yaml`:

```yaml
environment:
  - aws-login/dev-sandbox
```

Because credentials come from each stack's config file, each stack can get its own: `Pulumi.dev.yaml` can import the sandbox environment, `Pulumi.prod.yaml` the production one, and so on.

A `Stacks` update runs as the [pipeline's identity](/docs/delivery/concepts/identity/), which must be allowed to open the environment. If it isn't, the update fails.

Delivery does not implicitly grant access to environments. Whether the pipeline runs as the service principal Delivery generates for it, a service principal you manage, or a team, give that identity Environment Open on each environment that the pipeline stack and the target stacks import, from the environment's [access settings](/docs/administration/concepts/rbac/entities/#entity-access). Your own access isn't enough.

## Next steps

- Set up [OIDC for Pulumi ESC](/docs/esc/guides/configuring-oidc/).

<!-- TODO(launch): Consider a full AWS end-to-end example. -->
