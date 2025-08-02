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

Rather than migrating your entire Terraform infrastructure to Pulumi, you can reference existing Terraform state files to access outputs and resource attributes. This enables coexistence where different teams can use their preferred tools while sharing infrastructure.

Common scenarios include:

* Operations teams manage core infrastructure with Terraform
* Development teams deploy applications with Pulumi
* Gradual adoption of Pulumi happens alongside existing Terraform workflows

## Referencing Existing Infrastructure State

Here's an example of a minimal Terraform config that centrally manages an AWS ECS cluster and ECR repository. Pulumi can reference these outputs programmatically.

```hcl
# An AWS ECS Cluster
resource "aws_ecs_cluster" "cluster" {
  name = "app-cluster"
}

# An AWS ECR Repository
resource "aws_ecr_repository" "repo" {
  name = "image-repo"
}

# Outputs that Pulumi will reference
output "ecs_cluster_name" {
  value = aws_ecs_cluster.cluster.name
}

output "ecr_repository_url" {
  value = aws_ecr_repository.repo.repository_url
}
```

### Reference local state files

For Terraform workspaces using local state files, you can reference them directly, via the [`getLocalReference`](/registry/packages/terraform/api-docs/state/getlocalreference/) function:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

```typescript
import * as terraform from "@pulumi/terraform";

// Reference local Terraform state
const tfState = terraform.state.getLocalReferenceOutput({
    path: "../infrastructure/terraform.tfstate",
});

// Access Terraform outputs
const ecsClusterName = tfState.outputs["ecs_cluster_name"];
const ecrRepository = tfState.outputs["ecr_repository_url"];
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi
import pulumi_terraform as terraform

# Reference local Terraform state
tf_state = terraform.state.get_local_reference(
    path="../infrastructure/terraform.tfstate"
)

# Access Terraform outputs
ecs_cluster_name = tf_state.outputs["ecs_cluster_name"]
ecr_repository = tf_state.outputs["ecr_repository_url"]

pulumi.export("clusterName", ecs_cluster_name)
pulumi.export("repositoryUrl", ecr_repository)
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
package main

import (
	"github.com/pulumi/pulumi-terraform/sdk/v6/go/terraform/state"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		tfState := state.GetLocalReferenceOutput(ctx, state.GetLocalReferenceOutputArgs{
			Path: pulumi.String("../infrastructure/terraform.tfstate"),
		})

		// Access Terraform outputs
		ecsClusterName := tfState.Outputs().MapIndex(pulumi.String("ecs_cluster_name"))
		ecrRepository := tfState.Outputs().MapIndex(pulumi.String("ecr_repository_url"))

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
    var tfState = GetLocalReference.Invoke(new GetLocalReferenceInvokeArgs
    {
        Path = "../infrastructure/terraform.tfstate",
    }).Apply(x => x.Outputs);

    // Access Terraform outputs
    var ecsClusterName = tfState.Apply(x => x["ecs_cluster_name"]);
    var ecrRepository = tfState.Apply(x => x["ecr_repository_url"]);

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
import com.pulumi.core.Output;
import com.pulumi.terraform.state.StateFunctions;
import com.pulumi.terraform.state.inputs.GetLocalReferenceArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Reference local Terraform state
            var tfState = StateFunctions.getLocalReference(
                GetLocalReferenceArgs.builder()
                .path("../infrstructure/terraform.tfstate")
                .build()
            );

            // Access Terraform outputs
            var ecsClusterName = tfState.applyValue(x -> x.outputs().get("ecs_cluster_name"));
            var ecrRepository = tfState.applyValue(x -> x.outputs().get("ecr_repository_url"));

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
variables:
  tfState:
    fn::invoke:
      function: terraform:state:getLocalReference
      arguments:
        path: ../terraform.tfstate
outputs:
  clusterName: ${tfState.outputs["ecs_cluster_name"]}
  repositoryUrl: ${tfState.outputs["ecr_repository_url"]}
```

{{% /choosable %}}

### Reference remote state

For production environments, many prefer to store thier state in Terraform Cloud. To reference remote state, use the [`getRemoteReference`](/registry/packages/terraform/api-docs/state/getremotereference/) function:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

```typescript
import * as terraform from "@pulumi/terraform";

// Reference remote Terraform state
const tfState = terraform.state.getRemoteReferenceOutput({
    token: "<secret-token>",
    organization: "my-org",
    workspaces: {
        prefix: "dev",
    },
});

// Access Terraform outputs
const ecsClusterName = tfState.outputs["ecs_cluster_name"];
const ecrRepository = tfState.outputs["ecr_repository_url"];
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi
import pulumi_terraform as terraform

# Reference remote Terraform state
tf_state = terraform.state.get_remote_reference_output(
    token="<secret-token>",
    organization="my-org",
    workspaces={
        "prefix": "dev",
    }
)

# Access Terraform outputs
ecs_cluster_name = tf_state.outputs["ecs_cluster_name"]
ecr_repository = tf_state.outputs["ecr_repository_url"]

pulumi.export("clusterName", ecs_cluster_name)
pulumi.export("repositoryUrl", ecr_repository)
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
package main

import (
	"github.com/pulumi/pulumi-terraform/sdk/v6/go/terraform/state"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		organization := "my-org"
		workspacesPrefiix := "dev"
		token := "<secret-token>"

        // Reference remote Terraform state
		tfState := state.GetRemoteReferenceOutput(ctx, state.GetRemoteReferenceOutputArgs{
			Organization: pulumi.String(organization),
			Token:        pulumi.String(token),
			Workspaces: state.WorkspacesArgs{
				Prefix: pulumi.StringPtr(workspacesPrefiix),
			},
		})

		// Access Terraform outputs
		ecsClusterName := tfState.Outputs().MapIndex(pulumi.String("ecs_cluster_name"))
		ecrRepository := tfState.Outputs().MapIndex(pulumi.String("ecr_repository_url"))

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
    // Reference remote Terraform state
    var tfState = GetRemoteReference.Invoke(new GetRemoteReferenceInvokeArgs
    {
        Organization = "my-org",
	    Token = "<secret-token>>",
	    Workspaces = new Pulumi.Terraform.State.Inputs.WorkspacesArgs{
		    Prefix="dev"
	    }
    }).Apply(x => x.Outputs);

    // Access Terraform outputs
    var ecsClusterName = tfState.Apply(x => x["ecs_cluster_name"]);
    var ecrRepository = tfState.Apply(x => x["ecr_repository_url"]);

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
import com.pulumi.core.Output;
import com.pulumi.terraform.state.StateFunctions;
import com.pulumi.terraform.state.inputs.GetRemoteReferenceArgs;
import com.pulumi.terraform.state.inputs.WorkspacesArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Reference remote Terraform state
            var tfState = StateFunctions.getRemoteReference(
                GetRemoteReferenceArgs.builder()
                .organization("my-org")
        		.token("<secret-token>")
		        .workspaces(
		            WorkspacesArgs.builder()
		            .prefix("together-guide")
                    .build()
		        )
                .build()
            );

            // Access Terraform outputs
            var ecsClusterName = tfState.applyValue(x -> x.outputs().get("ecs_cluster_name"));
            var ecrRepository = tfState.applyValue(x -> x.outputs().get("ecr_repository_url"));

            ctx.export("clusterName", ecsClusterName);
            ctx.export("repositoryUrl", ecrRepository);
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```yaml
name: terraform-remote-state-with-yaml
runtime: yaml
variables:
  tfState:
    fn::invoke:
      function: terraform:state:getRemoteReference
      arguments:
        organization: my-org
        token:
          fn::secret: ${remote_tf_token} # A secret value containing the Terraform API token
        workspaces:
          prefix: dev
outputs:
  clusterName: ${tfState.outputs["ecs_cluster_name"]}
  repositoryUrl: ${tfState.outputs["ecr_repository_url"]}
```

{{% /choosable %}}

## Example: Containerized application on ECS

Let's create a practical example where an internal platform engineering team uses Terraform to manage an ECS cluster and ECR repository, while the developer teams use Pulumi to manage containerized application deployments via Fargate.

### Terraform infrastructure (reference)

The Terraform configuration for your company-wide ECS/ECR platform might look like this:

```hcl
# infrastructure/main.tf
resource "aws_ecs_cluster" "cluster" {
  name = "app-cluster"
}

resource "aws_ecr_repository" "repo" {
  name = "app-container-repo"
}

# Outputs that Pulumi will reference
output "ecs_cluster_arn" {
  value = aws_ecs_cluster.cluster.arn
}

output "ecr_repository_url" {
  value = aws_ecr_repository.repo.repository_url
}
```

### Pulumi application deployment

As a developer using this platform, we want to make a small containerized web app and deploy it.

First, we need to make the app. It will consist of a directory called `app/` holding a small `index.html` file, and a `Dockerfile` that defines an Nginx web server to host it.

***Example:** `app/index.html` - The HTML page*

```html
<html>
  <head><meta charset="UTF-8">
    <title>Hello Fargate</title>
  </head>
  <body>
      <p>I LOVE PULUMI!</p>
      <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
  </body>
</html>
```

***Example:** `app/Dockerfile` - The Nginx proxy*

```
FROM nginx
COPY index.html /usr/share/nginx/html
```

Next, we'll make a TypeScript Pulumi program that packages this up into a Docker image and runs the app on the company's shared infrastructure.

***Example:** `index.ts` - A Pulumi program that references the shared infrastructure*

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as pulumi from "@pulumi/pulumi";
import * as terraform from "@pulumi/terraform";

// Reference local Terraform state
const tfState = terraform.state.getLocalReferenceOutput({
    path: "../infrastructure/terraform.tfstate",
});

// Access Terraform outputs
const clusterArn = tfState.outputs["ecs_cluster_arn"];
const repoUrl = tfState.outputs["ecr_repository_url"];

// Build and publish our application's container image from ./app to the ECR repository.
const image = new awsx.ecr.Image("image", {
    repositoryUrl: repoUrl,
    context: "./app",
    platform: "linux/amd64",
});

// Create a load balancer to listen for requests and route them to the container.
const loadbalancer = new awsx.lb.ApplicationLoadBalancer("loadbalancer", {});

// Define the service and configure it to use our image and load balancer.
const service = new awsx.ecs.FargateService("service", {
    cluster: clusterArn,
    assignPublicIp: true,
    taskDefinitionArgs: {
        container: {
            name: "awsx-ecs",
            image: image.imageUri,
            cpu: 128,
            memory: 512,
            essential: true,
            portMappings: [{
                containerPort: 80,
                targetGroup: loadbalancer.defaultTargetGroup,
            }],
        },
    },
});

// Export the URL so we can easily access it.
export const frontendURL = pulumi.interpolate `http://${loadbalancer.loadBalancer.dnsName}`;
```

Our Pulumi program references a local Terraform state file to get the important details (the ECS ARN, the ECR URL), packages up the application into a Docker image, pushes that image to the ECR repo, creates a load balancer, and then defines a Fargate service that uses all of the above to run the containerized app. Finally, we see the deployed URL as a Pulumi output, and can immediately see that the app is running and serving up the HTML file.

This example demonstrates how Pulumi can seamlessly consume Terraform outputs to deploy applications on existing shared infrastructure.

## Best practices

1. **Use consistent naming**: Ensure Terraform output names are descriptive and stable
2. **Secure state access**: Use Terraform Cloud to control access to state files
3. **Document dependencies**: Clearly document which Pulumi stacks depend on which Terraform states
4. **Monitor state changes**: Be aware that changes to Terraform outputs will affect dependent Pulumi stacks

{{< get-started-stepper >}}
