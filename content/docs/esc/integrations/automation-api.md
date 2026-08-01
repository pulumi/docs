---
title: Automation API
title_tag: Manage Pulumi ESC resources in your automation workflows
h1: Manage Pulumi ESC resources in your automation workflows
meta_desc: Pulumi Automation API allows you to interact with ESC resources like environments, permissions and version tags.
menu:
  esc:
    identifier: esc-automation-api
    parent: esc-integrations
    weight: 13
aliases:
  - /docs/esc/development/automation-api/
  - /docs/esc/languages-sdks/automation-api/
---

Pulumi Automation API includes methods for interacting with Pulumi ESC Environments programmatically. This enables you to seamlessly integrate environment management into your automated workflows and build sophisticated custom tooling.

Automation API methods for ESC include:

- `addEnvironments(...)`: Add environments in order to your Pulumi stacks' [import](/docs/esc/concepts/environments/#using-environments-with-pulumi-iac) list.
- `listEnvironments()`: Retrieve a list of environments currently imported into your stack.
- `removeEnvironment(environment)`: Remove a specific environment from your stack's import list.

These methods provide the building blocks for advanced automation scenarios such as dynamically configuring applications based on environments, managing environment dependencies, and integrating ESC into CI/CD pipelines.

If you haven't used Automation API before, get started [here](/docs/iac/guides/building-extending/automation-api/).

Full Pulumi ESC Automation API support — adding, listing, and removing environments — is available for [TypeScript/JavaScript](/docs/reference/pkg/nodejs/pulumi/pulumi/classes/automation.Stack.html#addEnvironments), [Python](/docs/reference/pkg/python/pulumi/#pulumi.automation.LocalWorkspace.add_environments), and [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3@v3.117.0/go/auto#LocalWorkspace.AddEnvironments). The [.NET SDK](/docs/reference/pkg/dotnet/Pulumi.Automation/Pulumi.Automation.WorkspaceStack.html) and the [Java SDK](/docs/reference/pkg/java/com/pulumi/automation/WorkspaceStack.html) both support adding and removing environments but do not provide a method to list them. Here are some examples:

{{< chooser language "typescript,python,go,csharp,java" />}}

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

{{% choosable language csharp %}}

The .NET SDK supports adding and removing environments, but does not provide a method to list them.

```csharp
using System.Threading.Tasks;
using Pulumi.Automation;

class ManageEnvironments
{
    static async Task Main()
    {
        var projectName = "myProject";
        var stackName = "dev";

        // Set up an inline (empty) program, since we're only manipulating
        // environments, not deploying resources.
        var stackArgs = new InlineProgramArgs(projectName, stackName, PulumiFn.Create(() => { }));

        // Create or select an existing stack.
        var stack = await LocalWorkspace.CreateOrSelectStackAsync(stackArgs);

        // Add environments to the stack's import list.
        // This is like adding them to the `imports` section of an ESC environment.
        await stack.AddEnvironmentsAsync(new[] { "env1", "env2" });

        // Remove an environment from the stack's import list.
        await stack.RemoveEnvironmentAsync("env1");
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

The Java SDK supports adding and removing environments, but does not provide a method to list them.

```java
import com.pulumi.automation.LocalWorkspace;
import com.pulumi.automation.WorkspaceStack;

import java.util.List;

public class ManageEnvironments {
    public static void main(String[] args) {
        var projectName = "myProject";
        var stackName = "dev";

        // Create or select an existing stack, using an empty inline program
        // since we're only manipulating environments, not deploying resources.
        try (WorkspaceStack stack = LocalWorkspace.createOrSelectStack(projectName, stackName, ctx -> { })) {
            // Add environments to the stack's import list.
            // This is like adding them to the `imports` section of an ESC environment.
            stack.addEnvironments(List.of("env1", "env2"));

            // Remove an environment from the stack's import list.
            stack.removeEnvironment("env1");
        }
    }
}
```

{{% /choosable %}}
