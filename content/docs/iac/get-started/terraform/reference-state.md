---
title_tag: Reference Terraform State | Pulumi for Terraform Users
title: Reference Terraform State
h1: "Reference Terraform State"
meta_desc: Learn how to read from existing Terraform state files in Pulumi for seamless coexistence.
weight: 3
menu:
    iac:
        name: Reference Terraform State
        parent: terraform-get-started
        weight: 3

aliases:
- /docs/iac/get-started/terraform/reference-state/
---

## Why reference state?

Rather than migrating your entire Terraform infrastructure to Pulumi, you can reference existing Terraform state files to access outputs and resource attributes.
This enables coexistence where different teams can use their preferred tools while sharing infrastructure.

Common scenarios include:
* Operations teams manage core infrastructure with Terraform
* Development teams deploy applications with Pulumi
* Gradual adoption of Pulumi alongside existing Terraform workflows

## Reference local state files

For Terraform workspaces using local state files, you can reference them directly:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

```typescript
import * as terraform from "@pulumi/terraform";

// Reference local Terraform state
const tfState = new terraform.state.LocalReference("infrastructure", {
    path: "../infrastructure/terraform.tfstate",
});

// Access Terraform outputs
const ecsClusterName = tfState.getOutput("ecs_cluster_name");
const ecrRepository = tfState.getOutput("ecr_repository_url");

export const clusterName = ecsClusterName;
export const repositoryUrl = ecrRepository;
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi
import pulumi_terraform as terraform

# Reference local Terraform state
tf_state = terraform.state.LocalReference("infrastructure",
    path="../infrastructure/terraform.tfstate"
)

# Access Terraform outputs
ecs_cluster_name = tf_state.get_output("ecs_cluster_name")
ecr_repository = tf_state.get_output("ecr_repository_url")

pulumi.export("clusterName", ecs_cluster_name)
pulumi.export("repositoryUrl", ecr_repository)
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
package main

import (
	"github.com/pulumi/pulumi-terraform/sdk/v5/go/terraform/state"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Reference local Terraform state
		tfState, err := state.NewLocalReference(ctx, "infrastructure", &state.LocalReferenceArgs{
			Path: pulumi.String("../infrastructure/terraform.tfstate"),
		})
		if err != nil {
			return err
		}

		// Access Terraform outputs
		ecsClusterName := tfState.GetOutput(pulumi.String("ecs_cluster_name"))
		ecrRepository := tfState.GetOutput(pulumi.String("ecr_repository_url"))

		ctx.Export("clusterName", ecsClusterName)
		ctx.Export("repositoryUrl", ecrRepository)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Terraform.State;

return await Deployment.RunAsync(() =>
{
    // Reference local Terraform state
    var tfState = new LocalReference("infrastructure", new LocalReferenceArgs
    {
        Path = "../infrastructure/terraform.tfstate",
    });

    // Access Terraform outputs
    var ecsClusterName = tfState.GetOutput("ecs_cluster_name");
    var ecrRepository = tfState.GetOutput("ecr_repository_url");

    return new Dictionary<string, object?>
    {
        ["clusterName"] = ecsClusterName,
        ["repositoryUrl"] = ecrRepository,
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.terraform.state.LocalReference;
import com.pulumi.terraform.state.LocalReferenceArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Reference local Terraform state
            var tfState = new LocalReference("infrastructure", LocalReferenceArgs.builder()
                .path("../infrastructure/terraform.tfstate")
                .build());

            // Access Terraform outputs
            var ecsClusterName = tfState.getOutput("ecs_cluster_name");
            var ecrRepository = tfState.getOutput("ecr_repository_url");

            ctx.export("clusterName", ecsClusterName);
            ctx.export("repositoryUrl", ecrRepository);
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```yaml
name: reference-terraform-state
runtime: yaml
description: Reference Terraform state from Pulumi

resources:
  infrastructure:
    type: terraform:state:LocalReference
    properties:
      path: ../infrastructure/terraform.tfstate

outputs:
  clusterName: ${infrastructure.outputs.ecs_cluster_name}
  repositoryUrl: ${infrastructure.outputs.ecr_repository_url}
```

{{% /choosable %}}

## Reference remote state

For production environments, you'll likely reference remote state stored in S3, Terraform Cloud, or other backends:

### S3 remote state

{{% choosable language "typescript" %}}

```typescript
import * as terraform from "@pulumi/terraform";

// Reference S3 remote state
const tfState = new terraform.state.S3Reference("infrastructure", {
    bucket: "my-terraform-state-bucket",
    key: "infrastructure/terraform.tfstate",
    region: "us-west-2",
});

// Access Terraform outputs
const ecsClusterName = tfState.getOutput("ecs_cluster_name");
const ecrRepository = tfState.getOutput("ecr_repository_url");
const vpcId = tfState.getOutput("vpc_id");
const privateSubnets = tfState.getOutput("private_subnet_ids");

export const clusterName = ecsClusterName;
export const repositoryUrl = ecrRepository;
export const vpcId = vpcId;
export const subnetIds = privateSubnets;
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi
import pulumi_terraform as terraform

# Reference S3 remote state
tf_state = terraform.state.S3Reference("infrastructure",
    bucket="my-terraform-state-bucket",
    key="infrastructure/terraform.tfstate",
    region="us-west-2"
)

# Access Terraform outputs
ecs_cluster_name = tf_state.get_output("ecs_cluster_name")
ecr_repository = tf_state.get_output("ecr_repository_url")
vpc_id = tf_state.get_output("vpc_id")
private_subnets = tf_state.get_output("private_subnet_ids")

pulumi.export("clusterName", ecs_cluster_name)
pulumi.export("repositoryUrl", ecr_repository)
pulumi.export("vpcId", vpc_id)
pulumi.export("subnetIds", private_subnets)
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
package main

import (
	"github.com/pulumi/pulumi-terraform/sdk/v5/go/terraform/state"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Reference S3 remote state
		tfState, err := state.NewS3Reference(ctx, "infrastructure", &state.S3ReferenceArgs{
			Bucket: pulumi.String("my-terraform-state-bucket"),
			Key:    pulumi.String("infrastructure/terraform.tfstate"),
			Region: pulumi.String("us-west-2"),
		})
		if err != nil {
			return err
		}

		// Access Terraform outputs
		ecsClusterName := tfState.GetOutput(pulumi.String("ecs_cluster_name"))
		ecrRepository := tfState.GetOutput(pulumi.String("ecr_repository_url"))
		vpcId := tfState.GetOutput(pulumi.String("vpc_id"))
		privateSubnets := tfState.GetOutput(pulumi.String("private_subnet_ids"))

		ctx.Export("clusterName", ecsClusterName)
		ctx.Export("repositoryUrl", ecrRepository)
		ctx.Export("vpcId", vpcId)
		ctx.Export("subnetIds", privateSubnets)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Terraform.State;

return await Deployment.RunAsync(() =>
{
    // Reference S3 remote state
    var tfState = new S3Reference("infrastructure", new S3ReferenceArgs
    {
        Bucket = "my-terraform-state-bucket",
        Key = "infrastructure/terraform.tfstate",
        Region = "us-west-2",
    });

    // Access Terraform outputs
    var ecsClusterName = tfState.GetOutput("ecs_cluster_name");
    var ecrRepository = tfState.GetOutput("ecr_repository_url");
    var vpcId = tfState.GetOutput("vpc_id");
    var privateSubnets = tfState.GetOutput("private_subnet_ids");

    return new Dictionary<string, object?>
    {
        ["clusterName"] = ecsClusterName,
        ["repositoryUrl"] = ecrRepository,
        ["vpcId"] = vpcId,
        ["subnetIds"] = privateSubnets,
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.terraform.state.S3Reference;
import com.pulumi.terraform.state.S3ReferenceArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Reference S3 remote state
            var tfState = new S3Reference("infrastructure", S3ReferenceArgs.builder()
                .bucket("my-terraform-state-bucket")
                .key("infrastructure/terraform.tfstate")
                .region("us-west-2")
                .build());

            // Access Terraform outputs
            var ecsClusterName = tfState.getOutput("ecs_cluster_name");
            var ecrRepository = tfState.getOutput("ecr_repository_url");
            var vpcId = tfState.getOutput("vpc_id");
            var privateSubnets = tfState.getOutput("private_subnet_ids");

            ctx.export("clusterName", ecsClusterName);
            ctx.export("repositoryUrl", ecrRepository);
            ctx.export("vpcId", vpcId);
            ctx.export("subnetIds", privateSubnets);
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```yaml
name: reference-terraform-state
runtime: yaml
description: Reference Terraform remote state from Pulumi

resources:
  infrastructure:
    type: terraform:state:S3Reference
    properties:
      bucket: my-terraform-state-bucket
      key: infrastructure/terraform.tfstate
      region: us-west-2

outputs:
  clusterName: ${infrastructure.outputs.ecs_cluster_name}
  repositoryUrl: ${infrastructure.outputs.ecr_repository_url}
  vpcId: ${infrastructure.outputs.vpc_id}
  subnetIds: ${infrastructure.outputs.private_subnet_ids}
```

{{% /choosable %}}

### Terraform Cloud remote state

{{% choosable language "typescript" %}}

```typescript
import * as terraform from "@pulumi/terraform";

// Reference Terraform Cloud remote state
const tfState = new terraform.state.RemoteStateReference("infrastructure", {
    backendType: "remote",
    organization: "my-org",
    workspaces: {
        name: "infrastructure-prod",
    },
});

const ecsClusterName = tfState.getOutput("ecs_cluster_name");
const ecrRepository = tfState.getOutput("ecr_repository_url");
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi_terraform as terraform

# Reference Terraform Cloud remote state
tf_state = terraform.state.RemoteStateReference("infrastructure",
    backend_type="remote",
    organization="my-org",
    workspaces={
        "name": "infrastructure-prod",
    }
)

ecs_cluster_name = tf_state.get_output("ecs_cluster_name")
ecr_repository = tf_state.get_output("ecr_repository_url")
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
// Reference Terraform Cloud remote state
tfState, err := state.NewRemoteStateReference(ctx, "infrastructure", &state.RemoteStateReferenceArgs{
    BackendType:  pulumi.String("remote"),
    Organization: pulumi.String("my-org"),
    Workspaces: map[string]interface{}{
        "name": "infrastructure-prod",
    },
})
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
// Reference Terraform Cloud remote state
var tfState = new RemoteStateReference("infrastructure", new RemoteStateReferenceArgs
{
    BackendType = "remote",
    Organization = "my-org",
    Workspaces = new Dictionary<string, object>
    {
        ["name"] = "infrastructure-prod",
    },
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

```java
// Reference Terraform Cloud remote state
var tfState = new RemoteStateReference("infrastructure", RemoteStateReferenceArgs.builder()
    .backendType("remote")
    .organization("my-org")
    .workspaces(Map.of("name", "infrastructure-prod"))
    .build());
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```yaml
resources:
  infrastructure:
    type: terraform:state:RemoteStateReference
    properties:
      backendType: remote
      organization: my-org
      workspaces:
        name: infrastructure-prod
```

{{% /choosable %}}

## Example: containerized application on ECS

Let's create a practical example where Terraform manages the ECS cluster and ECR repository, while Pulumi manages the containerized application deployment:

### Terraform infrastructure (reference only)

Your existing Terraform configuration might look like this:

```hcl
# infrastructure/main.tf
resource "aws_ecs_cluster" "main" {
  name = "app-cluster"
}

resource "aws_ecr_repository" "app" {
  name = "my-app"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index + 1}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
}

# Outputs that Pulumi will reference
output "ecs_cluster_name" {
  value = aws_ecs_cluster.main.name
}

output "ecr_repository_url" {
  value = aws_ecr_repository.app.repository_url
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}
```

### Pulumi application deployment

{{% choosable language "typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as terraform from "@pulumi/terraform";

// Reference Terraform state
const tfState = new terraform.state.S3Reference("infrastructure", {
    bucket: "my-terraform-state-bucket",
    key: "infrastructure/terraform.tfstate",
    region: "us-west-2",
});

// Get infrastructure details from Terraform
const clusterName = tfState.getOutput("ecs_cluster_name");
const repositoryUrl = tfState.getOutput("ecr_repository_url");
const vpcId = tfState.getOutput("vpc_id");
const subnetIds = tfState.getOutput("private_subnet_ids");

// Create ECS task definition
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
            "image": "${repositoryUrl}:latest",
            "essential": true,
            "portMappings": [
                {
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": "${logGroup.name}",
                    "awslogs-region": "us-west-2",
                    "awslogs-stream-prefix": "ecs"
                }
            }
        }
    ]`,
});

// Create ECS service
const service = new aws.ecs.Service("app-service", {
    cluster: clusterName,
    taskDefinition: taskDefinition.arn,
    desiredCount: 2,
    launchType: "FARGATE",
    networkConfiguration: {
        subnets: subnetIds,
        securityGroups: [securityGroup.id],
    },
});

export const serviceName = service.name;
export const taskDefinitionArn = taskDefinition.arn;
```

{{% /choosable %}}

This example demonstrates how Pulumi can seamlessly consume Terraform outputs to deploy applications on existing infrastructure.

## Best practices

1. **Use consistent naming**: Ensure Terraform output names are descriptive and stable
2. **Version your state**: Use versioned S3 buckets or Terraform Cloud for state management
3. **Secure access**: Use IAM roles and policies to control access to state files
4. **Document dependencies**: Clearly document which Pulumi stacks depend on which Terraform states
5. **Monitor state changes**: Be aware that changes to Terraform outputs will affect dependent Pulumi stacks

{{< get-started-stepper >}}