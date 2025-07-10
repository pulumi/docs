---
title_tag: Use Terraform Providers | Pulumi for Terraform Users
title: Use Terraform Providers
h1: "Use Terraform Providers"
meta_desc: Learn how to use any Terraform provider in Pulumi programs for accessing the full ecosystem of 3000+ providers.
weight: 4
menu:
    iac:
        name: Use Terraform Providers
        parent: terraform-get-started
        weight: 4

aliases:
- /docs/iac/get-started/terraform/terraform-providers/
---

## Access the provider ecosystem

Pulumi provides access to over 3000 Terraform providers through the Terraform bridge.
This means you can use any Terraform provider in your Pulumi programs, including community providers and custom providers that aren't available as native Pulumi providers.

## Add a Terraform provider

Use the `pulumi package add` command to add Terraform providers to your project:

```bash
pulumi package add terraform-provider-random
```

This command automatically:
* Downloads the Terraform provider binary
* Generates Pulumi bindings for the provider
* Adds the provider to your project dependencies

## Example: random naming for containers

Let's enhance our containerized application example by adding random suffixes to container images using the `random` Terraform provider:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

First, add the random provider:

```bash
pulumi package add terraform-provider-random
```

Then use it in your Pulumi program:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as random from "@pulumi/random";
import * as terraform from "@pulumi/terraform";

// Reference Terraform state for infrastructure
const tfState = new terraform.state.S3Reference("infrastructure", {
    bucket: "my-terraform-state-bucket",
    key: "infrastructure/terraform.tfstate",
    region: "us-west-2",
});

const clusterName = tfState.getOutput("ecs_cluster_name");
const repositoryUrl = tfState.getOutput("ecr_repository_url");

// Create random suffix for image tagging
const imageSuffix = new random.RandomId("image-suffix", {
    byteLength: 4,
});

// Build and tag container image
const image = new aws.ecr.LifecyclePolicy("app-image", {
    repository: repositoryUrl,
    policy: JSON.stringify({
        rules: [{
            rulePriority: 1,
            description: "Keep last 10 images",
            selection: {
                tagStatus: "tagged",
                tagPrefixList: ["v"],
                countType: "imageCountMoreThan",
                countNumber: 10,
            },
            action: {
                type: "expire"
            }
        }]
    }),
});

// Create task definition with random-tagged image
const taskDefinition = new aws.ecs.TaskDefinition("app-task", {
    family: "my-app",
    networkMode: "awsvpc",
    requiresCompatibilities: ["FARGATE"],
    cpu: "256",
    memory: "512",
    executionRoleArn: taskRole.arn,
    containerDefinitions: pulumi.interpolate`[
        {
            "name": "my-app",
            "image": "${repositoryUrl}:v${imageSuffix.hex}",
            "essential": true,
            "portMappings": [
                {
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ],
            "environment": [
                {
                    "name": "APP_VERSION",
                    "value": "${imageSuffix.hex}"
                }
            ]
        }
    ]`,
});

export const imageTag = imageSuffix.hex;
export const fullImageUrl = pulumi.interpolate`${repositoryUrl}:v${imageSuffix.hex}`;
```

{{% /choosable %}}

{{% choosable language "python" %}}

First, add the random provider:

```bash
pulumi package add terraform-provider-random
```

Then use it in your Pulumi program:

```python
import pulumi
import pulumi_aws as aws
import pulumi_random as random
import pulumi_terraform as terraform

# Reference Terraform state for infrastructure
tf_state = terraform.state.S3Reference("infrastructure",
    bucket="my-terraform-state-bucket",
    key="infrastructure/terraform.tfstate",
    region="us-west-2"
)

cluster_name = tf_state.get_output("ecs_cluster_name")
repository_url = tf_state.get_output("ecr_repository_url")

# Create random suffix for image tagging
image_suffix = random.RandomId("image-suffix", byte_length=4)

# Create task definition with random-tagged image
task_definition = aws.ecs.TaskDefinition("app-task",
    family="my-app",
    network_mode="awsvpc",
    requires_compatibilities=["FARGATE"],
    cpu="256",
    memory="512",
    execution_role_arn=task_role.arn,
    container_definitions=pulumi.Output.format("""[
        {{
            "name": "my-app",
            "image": "{0}:v{1}",
            "essential": true,
            "portMappings": [
                {{
                    "containerPort": 80,
                    "protocol": "tcp"
                }}
            ],
            "environment": [
                {{
                    "name": "APP_VERSION",
                    "value": "{1}"
                }}
            ]
        }}
    ]""", repository_url, image_suffix.hex)
)

pulumi.export("imageTag", image_suffix.hex)
pulumi.export("fullImageUrl", pulumi.Output.format("{0}:v{1}", repository_url, image_suffix.hex))
```

{{% /choosable %}}

{{% choosable language "go" %}}

First, add the random provider:

```bash
pulumi package add terraform-provider-random
```

Then use it in your Pulumi program:

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ecs"
	"github.com/pulumi/pulumi-random/sdk/v4/go/random"
	"github.com/pulumi/pulumi-terraform/sdk/v5/go/terraform/state"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Reference Terraform state for infrastructure
		tfState, err := state.NewS3Reference(ctx, "infrastructure", &state.S3ReferenceArgs{
			Bucket: pulumi.String("my-terraform-state-bucket"),
			Key:    pulumi.String("infrastructure/terraform.tfstate"),
			Region: pulumi.String("us-west-2"),
		})
		if err != nil {
			return err
		}

		clusterName := tfState.GetOutput(pulumi.String("ecs_cluster_name"))
		repositoryUrl := tfState.GetOutput(pulumi.String("ecr_repository_url"))

		// Create random suffix for image tagging
		imageSuffix, err := random.NewRandomId(ctx, "image-suffix", &random.RandomIdArgs{
			ByteLength: pulumi.Int(4),
		})
		if err != nil {
			return err
		}

		// Create task definition with random-tagged image
		containerDefinitions := pulumi.Sprintf(`[
			{
				"name": "my-app",
				"image": "%s:v%s",
				"essential": true,
				"portMappings": [
					{
						"containerPort": 80,
						"protocol": "tcp"
					}
				],
				"environment": [
					{
						"name": "APP_VERSION",
						"value": "%s"
					}
				]
			}
		]`, repositoryUrl, imageSuffix.Hex, imageSuffix.Hex)

		taskDefinition, err := ecs.NewTaskDefinition(ctx, "app-task", &ecs.TaskDefinitionArgs{
			Family:                  pulumi.String("my-app"),
			NetworkMode:             pulumi.String("awsvpc"),
			RequiresCompatibilities: pulumi.StringArray{pulumi.String("FARGATE")},
			Cpu:                     pulumi.String("256"),
			Memory:                  pulumi.String("512"),
			ExecutionRoleArn:        taskRole.Arn,
			ContainerDefinitions:    containerDefinitions,
		})
		if err != nil {
			return err
		}

		ctx.Export("imageTag", imageSuffix.Hex)
		ctx.Export("fullImageUrl", pulumi.Sprintf("%s:v%s", repositoryUrl, imageSuffix.Hex))
		ctx.Export("taskDefinitionArn", taskDefinition.Arn)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

First, add the random provider:

```bash
pulumi package add terraform-provider-random
```

Then use it in your Pulumi program:

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.Ecs;
using Pulumi.Random;
using Pulumi.Terraform.State;

return await Deployment.RunAsync(() =>
{
    // Reference Terraform state for infrastructure
    var tfState = new S3Reference("infrastructure", new S3ReferenceArgs
    {
        Bucket = "my-terraform-state-bucket",
        Key = "infrastructure/terraform.tfstate",
        Region = "us-west-2",
    });

    var clusterName = tfState.GetOutput("ecs_cluster_name");
    var repositoryUrl = tfState.GetOutput("ecr_repository_url");

    // Create random suffix for image tagging
    var imageSuffix = new RandomId("image-suffix", new RandomIdArgs
    {
        ByteLength = 4,
    });

    // Create task definition with random-tagged image
    var taskDefinition = new TaskDefinition("app-task", new TaskDefinitionArgs
    {
        Family = "my-app",
        NetworkMode = "awsvpc",
        RequiresCompatibilities = new[] { "FARGATE" },
        Cpu = "256",
        Memory = "512",
        ExecutionRoleArn = taskRole.Arn,
        ContainerDefinitions = Output.Format($@"[
            {{
                ""name"": ""my-app"",
                ""image"": ""{repositoryUrl}:v{imageSuffix.Hex}"",
                ""essential"": true,
                ""portMappings"": [
                    {{
                        ""containerPort"": 80,
                        ""protocol"": ""tcp""
                    }}
                ],
                ""environment"": [
                    {{
                        ""name"": ""APP_VERSION"",
                        ""value"": ""{imageSuffix.Hex}""
                    }}
                ]
            }}
        ]"),
    });

    return new Dictionary<string, object?>
    {
        ["imageTag"] = imageSuffix.Hex,
        ["fullImageUrl"] = Output.Format($"{repositoryUrl}:v{imageSuffix.Hex}"),
        ["taskDefinitionArn"] = taskDefinition.Arn,
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

First, add the random provider:

```bash
pulumi package add terraform-provider-random
```

Then use it in your Pulumi program:

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.ecs.TaskDefinition;
import com.pulumi.aws.ecs.TaskDefinitionArgs;
import com.pulumi.core.Output;
import com.pulumi.random.RandomId;
import com.pulumi.random.RandomIdArgs;
import com.pulumi.terraform.state.S3Reference;
import com.pulumi.terraform.state.S3ReferenceArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Reference Terraform state for infrastructure
            var tfState = new S3Reference("infrastructure", S3ReferenceArgs.builder()
                .bucket("my-terraform-state-bucket")
                .key("infrastructure/terraform.tfstate")
                .region("us-west-2")
                .build());

            var clusterName = tfState.getOutput("ecs_cluster_name");
            var repositoryUrl = tfState.getOutput("ecr_repository_url");

            // Create random suffix for image tagging
            var imageSuffix = new RandomId("image-suffix", RandomIdArgs.builder()
                .byteLength(4)
                .build());

            // Create task definition with random-tagged image
            var containerDefinitions = Output.format("""
                [
                    {
                        "name": "my-app",
                        "image": "%s:v%s",
                        "essential": true,
                        "portMappings": [
                            {
                                "containerPort": 80,
                                "protocol": "tcp"
                            }
                        ],
                        "environment": [
                            {
                                "name": "APP_VERSION",
                                "value": "%s"
                            }
                        ]
                    }
                ]
                """, repositoryUrl, imageSuffix.hex(), imageSuffix.hex());

            var taskDefinition = new TaskDefinition("app-task", TaskDefinitionArgs.builder()
                .family("my-app")
                .networkMode("awsvpc")
                .requiresCompatibilities("FARGATE")
                .cpu("256")
                .memory("512")
                .executionRoleArn(taskRole.arn())
                .containerDefinitions(containerDefinitions)
                .build());

            ctx.export("imageTag", imageSuffix.hex());
            ctx.export("fullImageUrl", Output.format("%s:v%s", repositoryUrl, imageSuffix.hex()));
            ctx.export("taskDefinitionArn", taskDefinition.arn());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

First, add the random provider:

```bash
pulumi package add terraform-provider-random
```

Then use it in your Pulumi program:

```yaml
name: terraform-provider-example
runtime: yaml
description: Use Terraform providers in Pulumi

resources:
  # Reference Terraform state for infrastructure
  infrastructure:
    type: terraform:state:S3Reference
    properties:
      bucket: my-terraform-state-bucket
      key: infrastructure/terraform.tfstate
      region: us-west-2

  # Create random suffix for image tagging
  image-suffix:
    type: random:RandomId
    properties:
      byteLength: 4

  # Create task definition with random-tagged image
  app-task:
    type: aws:ecs:TaskDefinition
    properties:
      family: my-app
      networkMode: awsvpc
      requiresCompatibilities: [FARGATE]
      cpu: "256"
      memory: "512"
      executionRoleArn: ${taskRole.arn}
      containerDefinitions: |
        [
          {
            "name": "my-app",
            "image": "${infrastructure.outputs.ecr_repository_url}:v${image-suffix.hex}",
            "essential": true,
            "portMappings": [
              {
                "containerPort": 80,
                "protocol": "tcp"
              }
            ],
            "environment": [
              {
                "name": "APP_VERSION",
                "value": "${image-suffix.hex}"
              }
            ]
          }
        ]

outputs:
  imageTag: ${image-suffix.hex}
  fullImageUrl: ${infrastructure.outputs.ecr_repository_url}:v${image-suffix.hex}
  taskDefinitionArn: ${app-task.arn}
```

{{% /choosable %}}

## Compare with Terraform

The same functionality in Terraform would look like:

```hcl
# Terraform equivalent
terraform {
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1"
    }
  }
}

# Reference remote state
data "terraform_remote_state" "infrastructure" {
  backend = "s3"
  config = {
    bucket = "my-terraform-state-bucket"
    key    = "infrastructure/terraform.tfstate"
    region = "us-west-2"
  }
}

# Create random suffix for image tagging
resource "random_id" "image_suffix" {
  byte_length = 4
}

# Create task definition with random-tagged image
resource "aws_ecs_task_definition" "app_task" {
  family                   = "my-app"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.task_role.arn

  container_definitions = jsonencode([
    {
      name      = "my-app"
      image     = "${data.terraform_remote_state.infrastructure.outputs.ecr_repository_url}:v${random_id.image_suffix.hex}"
      essential = true
      portMappings = [
        {
          containerPort = 80
          protocol      = "tcp"
        }
      ]
      environment = [
        {
          name  = "APP_VERSION"
          value = random_id.image_suffix.hex
        }
      ]
    }
  ])
}

output "image_tag" {
  value = random_id.image_suffix.hex
}

output "full_image_url" {
  value = "${data.terraform_remote_state.infrastructure.outputs.ecr_repository_url}:v${random_id.image_suffix.hex}"
}
```

## Advanced provider usage

### Using multiple providers

You can add multiple Terraform providers to leverage specialized functionality:

```bash
# Add providers for different services
pulumi package add terraform-provider-datadog
pulumi package add terraform-provider-pagerduty
pulumi package add terraform-provider-github
```

### Custom provider configuration

Configure Terraform providers with custom settings:

{{% choosable language "typescript" %}}

```typescript
import * as random from "@pulumi/random";

// Configure the random provider
const provider = new random.Provider("custom-random", {
    // Provider-specific configuration
});

// Use the configured provider
const customRandom = new random.RandomId("custom-suffix", {
    byteLength: 8,
}, { provider });
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi_random as random

# Configure the random provider
provider = random.Provider("custom-random")

# Use the configured provider
custom_random = random.RandomId("custom-suffix",
    byte_length=8,
    opts=pulumi.ResourceOptions(provider=provider)
)
```

{{% /choosable %}}

### Version constraints

Specify provider versions for consistency:

```bash
# Add a specific version
pulumi package add terraform-provider-random@3.4.3

# Add with version constraint
pulumi package add terraform-provider-datadog@">=3.0.0,<4.0.0"
```

## Best practices

1. **Pin provider versions**: Use specific versions in production environments
2. **Test provider compatibility**: Verify that Terraform providers work correctly with Pulumi
3. **Monitor provider updates**: Keep track of provider updates and breaking changes
4. **Use native providers when available**: Prefer native Pulumi providers over Terraform providers for better performance and type safety
5. **Document provider usage**: Document which Terraform providers your team uses and why

{{< get-started-stepper >}}