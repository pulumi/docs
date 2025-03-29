---
title: "Introducing Pulumi ESC Support in Automation API and the Pulumi Service Provider"
allow_long_title: true
date: 2024-06-05T00:00:00-05:00
draft: false
meta_desc: "Supercharge how you manage your infrastructure and application secrets
  and configurations using the Pulumi Service Provider and Automation API."
meta_image: "meta.png"
authors:
  - arun-loganathan
  - iaroslav-titov
tags:
  - esc
  - secrets
  - config management
  - features
search:
  keywords:
    - Automation
    - Environments
    - Automation API
    - Service Provider
---

We're excited to announce two powerful new capabilities for [Pulumi Environments Secrets and Configurations](/product/esc) (ESC) that supercharge how you manage and control your infrastructure and application secrets and configurations:

- **Pulumi Service Provider Support for ESC Environments**: Manage your environments as code right alongside your infrastructure including fine-grained access control using [Pulumi Service Provider](/registry/packages/pulumiservice/).
- **Automation API Enhancements for ESC**: Seamlessly integrate ESC Environments into your [Automation API](/automation/)-based Pulumi projects.
  
<!--more-->

These updates build upon Pulumi ESC's commitment to simplify and streamline secrets and configuration management providing you with greater control, security, and automation capabilities.

## Manage ESC Environments as Code with the Pulumi Service Provider

You can now manage your Pulumi ESC [Environments](/docs/esc/environments/) directly within the Pulumi Service using the powerful Pulumi Service Provider. This means you can define environments, add [version tags](/docs/esc/environments/#tagging-versions), and even control access using familiar Infrastructure as Code (IaC) practices ensuring consistency and repeatability across your deployments.

Here's a glimpse of what you can achieve:

- **Programmatically create and manage ESC Environments**: Define environments alongside your infrastructure code for a unified workflow.
- **Add version tags to environments**: Add tags when you are creating the environment.
- **Enforce granular team permissions**: Control who can [read, open, or modify](/docs/esc/environments/#organization-wide-permissions) your environments ensuring secure collaboration and preventing unauthorized access.

Bringing Pulumi ESC Environments support into the Pulumi Service Provider empowers you to manage your entire infrastructure and application landscape through a unified approach.

Pulumi Service Provider ESC capabilities are available for TypeScript/JavaScript, Go, Python, C#, Java, and YAML. See our [Environment](/registry/packages/pulumiservice/api-docs/environment/), [Environment Version Tag](/registry/packages/pulumiservice/api-docs/environmentversiontag/), and [Environment Permissions](/registry/packages/pulumiservice/api-docs/teamenvironmentpermission/) Pulumi Service Provider docs. Here are examples of creating environments in TypeScript/JavaScript, Go, and Python:

{{< chooser language "typescript,python,go" />}}

{{% choosable language typescript %}}

```typescript
import * as service from "@pulumi/pulumiservice";
import * as pulumi from "@pulumi/pulumi";

var environment = new service.Environment("testing-environment", {
  organization: "service-provider-test-org",
  name: "testing-environment-ts",
  yaml: new pulumi.asset.StringAsset(
    `values:
    myKey1: "myValue1"
    myNestedKey:
    myKey2: "myValue2"
    myNumber: 1`
  )
})
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_pulumiservice import Environment

environment = Environment(
    "testing-environment",
    organization="service-provider-test-org",
    name="testing-environment-py",
    yaml=pulumi.StringAsset("""
        values:
          myKey1: "myValue1"
          myNestedKey:
            myKey2: "myValue2"
            myNumber: 1
    """)
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-pulumiservice/sdk/go/pulumiservice"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := pulumiservice.NewEnvironment(ctx, "testing-environment", &pulumiservice.EnvironmentArgs{
			Name:         pulumi.String("testing-environment-go"),
			Organization: pulumi.String("service-provider-test-org"),
			Yaml: pulumi.NewStringAsset(`
            values:
              myKey1: "myValue1"
              myNestedKey:
                myKey2: "myValue2"
                myNumber: 1`),
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}

## Streamline Automated Workflows with Automation API Enhancements

We're expanding the powerful Pulumi Automation API to include new methods for interacting with Pulumi ESC Environments programmatically. This enables you to seamlessly integrate environment management into your automated workflows and build sophisticated custom tooling.

The new Automation API methods for ESC include:

- `addEnvironments(...)`: Append environments in order to your Pulumi stack's [import](/docs/esc/environments/#using-environments-with-pulumi-iac) list.
- `listEnvironments()`: Retrieve a list of environments currently imported into your stack.
- `removeEnvironment(environment)`: Remove a specific environment from your stack's import list.

These additions provide the building blocks for advanced automation scenarios such as dynamically configuring applications based on environments, managing environment dependencies, and integrating ESC into CI/CD pipelines.

Pulumi ESC Automation API capabilities are available for [TypeScript/JavaScript](/docs/reference/pkg/nodejs/pulumi/pulumi/classes/automation.Stack.html#addEnvironments), [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3@v3.117.0/go/auto#LocalWorkspace.AddEnvironments), and [Python](/docs/reference/pkg/python/pulumi/#pulumi.automation.LocalWorkspace.add_environments). Here are some examples:

{{< chooser language "typescript,python,go" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as automation from "@pulumi/pulumi/automation";

async function manageEnvironments() {
    const projectName = "myProject";
    const stackName = "dev";
    
    // Set up your stack options. Here we're using an empty program
    // since we're only manipulating environments, not deploying resources.
    const stackArgs: automation.InlineProgramArgs = {
        stackName,
        projectName,
        program: async () => { },
    };

    // Create or select an existing stack.
    const stack = await automation.LocalWorkspace.createOrSelectStack(stackArgs);

    // Add environments to your stack's configuration.
    // This is like adding them to the `imports` section of an ESC environment.
    await stack.addEnvironments("env1", "env2");
    // The stack's configuration now includes `env1` and `env2`.

    // List the environments currently configured for the stack.
    const environments = await stack.listEnvironments();
    console.log("Current environments:", environments); // Output: ["env1", "env2"]

    // Remove an environment from the stack's configuration.
    await stack.removeEnvironment("env1");
    // The stack's configuration now only includes `env2`.

    // List environments again to confirm the removal.
    const updatedEnvironments = await stack.listEnvironments();
    console.log("Updated environments:", updatedEnvironments); // Output: ["env2"]
}

// Call the async function to execute.
manageEnvironments().catch(console.error);

```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi.automation import LocalWorkspace, ProjectSettings, Stack

def manage_environments():
    stack_name = "dev"
    project_name = "myProject"
    
    # Define the project settings.
    project_settings = ProjectSettings(
        name=project_name,
        runtime="python",
    )

    # Create a LocalWorkspace with the project settings.
    workspace = LocalWorkspace(
        work_dir=".",  # Use the current directory as the working directory
        project_settings=project_settings,
    )

    # Create or select an existing stack.
    stack = Stack.create(stack_name=stack_name, workspace=workspace)

    # Add environments to the stack's configuration.
    stack.add_environments("env1", "env2")

    # List the environments associated with the stack.
    environments = stack.list_environments()
    print("Current environments:", environments)  # Output: ['env1', 'env2']

    # Remove an environment from the stack's configuration.
    stack.remove_environment("env1")

    # List the environments again to verify the removal.
    updated_environments = stack.list_environments()
    print("Updated environments:", updated_environments)  # Output: ['env2']

# Run the function to manage environments.
manage_environments()

```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"context"
	"fmt"
	"log"
	"github.com/pulumi/pulumi/sdk/v3/go/auto"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/pulumi/pulumi/sdk/v3/go/common/workspace"
)

func main() {
	ctx := context.Background()
	projectName := "myProject"
	stackName := "dev"

	// Define the project configuration.
	project := workspace.Project{
		Name:    tokens.PackageName(projectName),
		Runtime: workspace.NewProjectRuntimeInfo("go", nil),
	}

	// Create a workspace with the project configuration.
	// Here we're using an empty program since we're only manipulating environments, not deploying resources.
	ws, err := auto.NewLocalWorkspace(ctx, auto.Project(project), auto.Program(nil))
	if err != nil {
		log.Fatalf("Failed to create workspace: %v", err)
	}

	// Create or select an existing stack.
	stack, err := auto.UpsertStack(ctx, stackName, ws)
	if err != nil {
		log.Fatalf("Failed to create or select stack: %v", err)
	}

	// Add environments to the stack's configuration.
	// This is like adding them to the `imports` section of an ESC environment.
	err = stack.AddEnvironments(ctx, "env1", "env2")
	if err != nil {
		log.Fatalf("Failed to add environments: %v", err)
	}
	// The stack's configuration now includes `env1` and `env2`.

	// List the environments associated with the stack.
	envs, err := stack.ListEnvironments(ctx)
	if err != nil {
		log.Fatalf("Failed to list environments: %v", err)
	}
	fmt.Println("Current environments:", envs) // Output: map[env1:{env1} env2:{env2}]

	// Remove an environment from the stack's configuration.
	err = stack.RemoveEnvironment(ctx, "env1")
	if err != nil {
		log.Fatalf("Failed to remove environment: %v", err)
	}
	// The stack's configuration now only includes `env2`.

	// List the environments again to confirm the removal.
	envs, err = stack.ListEnvironments(ctx)
	if err != nil {
		log.Fatalf("Failed to list environments: %v", err)
	}
	fmt.Println("Updated environments:", envs) // Output: map[env2:{env2}]
}
```

{{% /choosable %}}

## What’s Coming in the Future

We have exciting plans to further enhance these capabilities. Here's a sneak peek at what's on the horizon:

- **Pulumi service Provider**: Capabilities to Open, Read, and List any environment versions and version tags
- **Automation API**: Capabilities to author new environments, and assign version tags

Need more features or want to share feedback? We encourage you to open new issues on our [GitHub repository](https://github.com/pulumi/esc/issues/new/choose) or upvote existing [ones](https://github.com/pulumi/esc/issues).

## Get Started Today!

These powerful new features are available now! We're excited to see how you leverage these updates to simplify your secrets and configuration management, enhance your security posture, and unlock new levels of automation.

To learn more and start leveraging the enhanced capabilities of Pulumi ESC check out the following resources:

- Pulumi Service Provider for ESC [Environment](/registry/packages/pulumiservice/api-docs/environment/), [Environment Version Tag](/registry/packages/pulumiservice/api-docs/environmentversiontag/), and [Environment Permissions](/registry/packages/pulumiservice/api-docs/teamenvironmentpermission/)
- Pulumi ESC Automation API in [TypeScript/JavaScript](/docs/reference/pkg/nodejs/pulumi/pulumi/classes/automation.Stack.html#addEnvironments), [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3@v3.117.0/go/auto#LocalWorkspace.AddEnvironments), and [Python](/docs/reference/pkg/python/pulumi/#pulumi.automation.LocalWorkspace.add_environments)
