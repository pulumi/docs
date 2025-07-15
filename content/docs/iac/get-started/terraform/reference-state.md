---
title_tag: Reference Terraform State | Pulumi for Terraform Users
title: Reference Terraform State
h1: "Reference Terraform State"
meta_desc: Learn how to read from existing Terraform state files in Pulumi for seamless coexistence.
weight: 4
menu:
    iac:
        name: Reference Terraform State
        parent: terraform-get-started
        weight: 4

aliases:
- /docs/iac/get-started/terraform/reference-state/
---

## Why reference state?

Rather than migrating your entire Terraform infrastructure to Pulumi, you can reference existing Terraform state files to access outputs and resource attributes.
This enables coexistence where different teams can use their preferred tools while sharing infrastructure.

Common scenarios include:

* Operations teams manage core infrastructure with Terraform
* Development teams deploy applications with Pulumi
* Gradual adoption of Pulumi happens alongside existing Terraform workflows

## Reference local state files

For Terraform workspaces using local state files, you can reference them directly:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

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

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

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

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

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

## Example: Containerized application on ECS

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

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

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

{{% choosable language "python" %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_terraform as terraform

# Reference Terraform state
tf_state = terraform.state.S3Reference("infrastructure",
    bucket="my-terraform-state-bucket",
    key="infrastructure/terraform.tfstate",
    region="us-west-2"
)

# Get infrastructure details from Terraform
cluster_name = tf_state.get_output("ecs_cluster_name")
repository_url = tf_state.get_output("ecr_repository_url")
vpc_id = tf_state.get_output("vpc_id")
subnet_ids = tf_state.get_output("private_subnet_ids")

# Create ECS task definition
task_definition = aws.ecs.TaskDefinition("app-task",
    family="my-app",
    network_mode="awsvpc",
    requires_compatibilities=["FARGATE"],
    cpu="256",
    memory="512",
    execution_role_arn=task_role.arn,
    container_definitions=pulumi.Output.all(repository_url, log_group.name).apply(
        lambda args: f"""[
            {{
                "name": "my-app",
                "image": "{args[0]}:latest",
                "essential": true,
                "portMappings": [
                    {{
                        "containerPort": 80,
                        "protocol": "tcp"
                    }}
                ],
                "logConfiguration": {{
                    "logDriver": "awslogs",
                    "options": {{
                        "awslogs-group": "{args[1]}",
                        "awslogs-region": "us-west-2",
                        "awslogs-stream-prefix": "ecs"
                    }}
                }}
            }}
        ]"""
    )
)

# Create ECS service
service = aws.ecs.Service("app-service",
    cluster=cluster_name,
    task_definition=task_definition.arn,
    desired_count=2,
    launch_type="FARGATE",
    network_configuration=aws.ecs.ServiceNetworkConfigurationArgs(
        subnets=subnet_ids,
        security_groups=[security_group.id],
    )
)

pulumi.export("serviceName", service.name)
pulumi.export("taskDefinitionArn", task_definition.arn)
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
package main

import (
	"encoding/json"
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ecs"
	"github.com/pulumi/pulumi-terraform/sdk/v5/go/terraform/state"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Reference Terraform state
		tfState, err := state.NewS3Reference(ctx, "infrastructure", &state.S3ReferenceArgs{
			Bucket: pulumi.String("my-terraform-state-bucket"),
			Key:    pulumi.String("infrastructure/terraform.tfstate"),
			Region: pulumi.String("us-west-2"),
		})
		if err != nil {
			return err
		}

		// Get infrastructure details from Terraform
		clusterName := tfState.GetOutput(pulumi.String("ecs_cluster_name"))
		repositoryUrl := tfState.GetOutput(pulumi.String("ecr_repository_url"))
		vpcId := tfState.GetOutput(pulumi.String("vpc_id"))
		subnetIds := tfState.GetOutput(pulumi.String("private_subnet_ids"))

		// Create container definitions
		containerDefs := pulumi.All(repositoryUrl, logGroup.Name).ApplyT(func(args []interface{}) (string, error) {
			repoUrl := args[0].(string)
			logGroupName := args[1].(string)

			containerDef := []map[string]interface{}{
				{
					"name":      "my-app",
					"image":     fmt.Sprintf("%s:latest", repoUrl),
					"essential": true,
					"portMappings": []map[string]interface{}{
						{
							"containerPort": 80,
							"protocol":      "tcp",
						},
					},
					"logConfiguration": map[string]interface{}{
						"logDriver": "awslogs",
						"options": map[string]interface{}{
							"awslogs-group":         logGroupName,
							"awslogs-region":        "us-west-2",
							"awslogs-stream-prefix": "ecs",
						},
					},
				},
			}

			jsonBytes, err := json.Marshal(containerDef)
			if err != nil {
				return "", err
			}
			return string(jsonBytes), nil
		}).(pulumi.StringOutput)

		// Create ECS task definition
		taskDefinition, err := ecs.NewTaskDefinition(ctx, "app-task", &ecs.TaskDefinitionArgs{
			Family:                  pulumi.String("my-app"),
			NetworkMode:             pulumi.String("awsvpc"),
			RequiresCompatibilities: pulumi.StringArray{pulumi.String("FARGATE")},
			Cpu:                     pulumi.String("256"),
			Memory:                  pulumi.String("512"),
			ExecutionRoleArn:        taskRole.Arn,
			ContainerDefinitions:    containerDefs,
		})
		if err != nil {
			return err
		}

		// Create ECS service
		service, err := ecs.NewService(ctx, "app-service", &ecs.ServiceArgs{
			Cluster:        clusterName,
			TaskDefinition: taskDefinition.Arn,
			DesiredCount:   pulumi.Int(2),
			LaunchType:     pulumi.String("FARGATE"),
			NetworkConfiguration: &ecs.ServiceNetworkConfigurationArgs{
				Subnets:        subnetIds,
				SecurityGroups: pulumi.StringArray{securityGroup.ID()},
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("serviceName", service.Name)
		ctx.Export("taskDefinitionArn", taskDefinition.Arn)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Pulumi.Aws.Ecs;
using Pulumi.Terraform.State;

return await Deployment.RunAsync(() =>
{
    // Reference Terraform state
    var tfState = new S3Reference("infrastructure", new S3ReferenceArgs
    {
        Bucket = "my-terraform-state-bucket",
        Key = "infrastructure/terraform.tfstate",
        Region = "us-west-2",
    });

    // Get infrastructure details from Terraform
    var clusterName = tfState.GetOutput("ecs_cluster_name");
    var repositoryUrl = tfState.GetOutput("ecr_repository_url");
    var vpcId = tfState.GetOutput("vpc_id");
    var subnetIds = tfState.GetOutput("private_subnet_ids");

    // Create container definitions
    var containerDefinitions = Output.Tuple(repositoryUrl, logGroup.Name).Apply(t =>
    {
        var (repoUrl, logGroupName) = t;
        var containerDef = new[]
        {
            new Dictionary<string, object>
            {
                ["name"] = "my-app",
                ["image"] = $"{repoUrl}:latest",
                ["essential"] = true,
                ["portMappings"] = new[]
                {
                    new Dictionary<string, object>
                    {
                        ["containerPort"] = 80,
                        ["protocol"] = "tcp"
                    }
                },
                ["logConfiguration"] = new Dictionary<string, object>
                {
                    ["logDriver"] = "awslogs",
                    ["options"] = new Dictionary<string, object>
                    {
                        ["awslogs-group"] = logGroupName,
                        ["awslogs-region"] = "us-west-2",
                        ["awslogs-stream-prefix"] = "ecs"
                    }
                }
            }
        };
        return JsonSerializer.Serialize(containerDef);
    });

    // Create ECS task definition
    var taskDefinition = new TaskDefinition("app-task", new TaskDefinitionArgs
    {
        Family = "my-app",
        NetworkMode = "awsvpc",
        RequiresCompatibilities = new[] { "FARGATE" },
        Cpu = "256",
        Memory = "512",
        ExecutionRoleArn = taskRole.Arn,
        ContainerDefinitions = containerDefinitions,
    });

    // Create ECS service
    var service = new Service("app-service", new ServiceArgs
    {
        Cluster = clusterName,
        TaskDefinition = taskDefinition.Arn,
        DesiredCount = 2,
        LaunchType = "FARGATE",
        NetworkConfiguration = new ServiceNetworkConfigurationArgs
        {
            Subnets = subnetIds,
            SecurityGroups = new[] { securityGroup.Id },
        },
    });

    return new Dictionary<string, object?>
    {
        ["serviceName"] = service.Name,
        ["taskDefinitionArn"] = taskDefinition.Arn,
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.ecs.Service;
import com.pulumi.aws.ecs.ServiceArgs;
import com.pulumi.aws.ecs.ServiceNetworkConfigurationArgs;
import com.pulumi.aws.ecs.TaskDefinition;
import com.pulumi.aws.ecs.TaskDefinitionArgs;
import com.pulumi.core.Output;
import com.pulumi.terraform.state.S3Reference;
import com.pulumi.terraform.state.S3ReferenceArgs;
import com.google.gson.Gson;

import java.util.List;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Reference Terraform state
            var tfState = new S3Reference("infrastructure", S3ReferenceArgs.builder()
                .bucket("my-terraform-state-bucket")
                .key("infrastructure/terraform.tfstate")
                .region("us-west-2")
                .build());

            // Get infrastructure details from Terraform
            var clusterName = tfState.getOutput("ecs_cluster_name");
            var repositoryUrl = tfState.getOutput("ecr_repository_url");
            var vpcId = tfState.getOutput("vpc_id");
            var subnetIds = tfState.getOutput("private_subnet_ids");

            // Create container definitions
            var containerDefinitions = Output.tuple(repositoryUrl, logGroup.name()).apply(t -> {
                var repoUrl = t.t1;
                var logGroupName = t.t2;
                
                var containerDef = List.of(Map.of(
                    "name", "my-app",
                    "image", repoUrl + ":latest",
                    "essential", true,
                    "portMappings", List.of(Map.of(
                        "containerPort", 80,
                        "protocol", "tcp"
                    )),
                    "logConfiguration", Map.of(
                        "logDriver", "awslogs",
                        "options", Map.of(
                            "awslogs-group", logGroupName,
                            "awslogs-region", "us-west-2",
                            "awslogs-stream-prefix", "ecs"
                        )
                    )
                ));
                
                return new Gson().toJson(containerDef);
            });

            // Create ECS task definition
            var taskDefinition = new TaskDefinition("app-task", TaskDefinitionArgs.builder()
                .family("my-app")
                .networkMode("awsvpc")
                .requiresCompatibilities("FARGATE")
                .cpu("256")
                .memory("512")
                .executionRoleArn(taskRole.arn())
                .containerDefinitions(containerDefinitions)
                .build());

            // Create ECS service
            var service = new Service("app-service", ServiceArgs.builder()
                .cluster(clusterName)
                .taskDefinition(taskDefinition.arn())
                .desiredCount(2)
                .launchType("FARGATE")
                .networkConfiguration(ServiceNetworkConfigurationArgs.builder()
                    .subnets(subnetIds)
                    .securityGroups(securityGroup.id())
                    .build())
                .build());

            ctx.export("serviceName", service.name());
            ctx.export("taskDefinitionArn", taskDefinition.arn());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```yaml
name: ecs-app-deployment
runtime: yaml
description: Deploy containerized app to ECS using Terraform state

resources:
  # Reference Terraform state
  infrastructure:
    type: terraform:state:S3Reference
    properties:
      bucket: my-terraform-state-bucket
      key: infrastructure/terraform.tfstate
      region: us-west-2

  # Create ECS task definition
  app-task:
    type: aws:ecs:TaskDefinition
    properties:
      family: my-app
      networkMode: awsvpc
      requiresCompatibilities:
        - FARGATE
      cpu: "256"
      memory: "512"
      executionRoleArn: ${task-role.arn}
      containerDefinitions: |
        [
          {
            "name": "my-app",
            "image": "${infrastructure.outputs.ecr_repository_url}:latest",
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
                "awslogs-group": "${log-group.name}",
                "awslogs-region": "us-west-2",
                "awslogs-stream-prefix": "ecs"
              }
            }
          }
        ]

  # Create ECS service
  app-service:
    type: aws:ecs:Service
    properties:
      cluster: ${infrastructure.outputs.ecs_cluster_name}
      taskDefinition: ${app-task.arn}
      desiredCount: 2
      launchType: FARGATE
      networkConfiguration:
        subnets: ${infrastructure.outputs.private_subnet_ids}
        securityGroups:
          - ${security-group.id}

outputs:
  serviceName: ${app-service.name}
  taskDefinitionArn: ${app-task.arn}
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
