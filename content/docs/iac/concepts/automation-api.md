---
title_tag: "Automation API"
meta_desc: The Pulumi Automation API is a programmatic interface for running Pulumi programs without the Pulumi CLI. Learn its core concepts and terminology.
title: Automation API
h1: Automation API
menu:
    iac:
        name: Automation API
        parent: iac-concepts
        weight: 108
aliases:
- /docs/guides/automation-api/
- /docs/using-pulumi/automation-api/
- /docs/iac/packages-and-automation/automation-api/
- /docs/iac/using-pulumi/automation-api/
- /docs/iac/automation-api/
- /docs/guides/automation-api/concepts-terminology/
- /docs/using-pulumi/automation-api/concepts-terminology/
- /docs/iac/packages-and-automation/automation-api/concepts-terminology/
- /docs/iac/using-pulumi/automation-api/concepts-terminology/
- /docs/iac/automation-api/concepts-terminology/
---

The Pulumi Automation API is a programmatic interface for running Pulumi programs without the Pulumi CLI. It encapsulates the functionality of the CLI---`pulumi up`, `pulumi preview`, `pulumi destroy`, `pulumi stack init`, and so on---as a strongly typed SDK, so you can drive the Pulumi engine from within your own application instead of invoking the `pulumi` command from a shell.

With Automation API you define a Pulumi program, its resources, stacks, and stack configuration entirely in code, then run that code as an ordinary executable in your language of choice (for example, `python3 main.py` instead of `pulumi up`). Automation API is distributed as a namespace within the Pulumi SDK and is part of Pulumi IaC's open source offering.

For a step-by-step walkthrough of building an Automation API program, see [Using Automation API](/docs/iac/guides/building-extending/automation-api/).

{{% notes type="info" %}}
Automation API drives the Pulumi CLI under the hood, so the CLI must be available to your program at runtime. You can install it ahead of time and add it to your `PATH`, or install it programmatically from your Automation API program. See [Using Automation API](/docs/iac/guides/building-extending/automation-api/#prerequisites) for details.
{{% /notes %}}

{{% notes type="tip" %}}
Automation API drives the Pulumi engine itself, running updates, previews, refreshes, and destroys from a program. If you instead need to read or modify Pulumi Cloud resources (for example, stack metadata, access tokens, or [Insights](/docs/insights/) data) without running a Pulumi program, use [`pulumi api`](/docs/iac/cli/api/), the CLI command for calling the [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/) directly.
{{% /notes %}}

## Use cases

Automation API is well suited to scenarios where infrastructure provisioning is part of a larger application or workflow, including:

- Driving infrastructure deployments within CI/CD workflows
- Integration testing
- Multi-stage deployments such as blue-green deployment patterns
- Deployments involving application code, such as database migrations
- Building higher-level tools, such as custom CLIs over Pulumi
- Exposing Pulumi behind a REST or gRPC API
- Debugging Pulumi programs by using a single entrypoint with inline programs

## Workspaces

To enable a broad range of runtime customization, Automation API defines a `Workspace` interface. A `Workspace` is the execution context that contains a single Pulumi project, a program, and one or more stacks. Workspaces manage the execution environment, providing utilities such as plugin installation, environment configuration (`$PULUMI_HOME`), and the creation, deletion, and listing of stacks.

### LocalWorkspace

`LocalWorkspace` is the default implementation of `Workspace`. It relies on `Pulumi.yaml` and `Pulumi.<stack>.yaml` as the on-disk format for project and stack settings. Modifying `ProjectSettings` alters the workspace's `Pulumi.yaml` file, and setting configuration on a stack modifies the corresponding `Pulumi.<stack>.yaml` file. This is identical to the behavior of CLI-driven workspaces.

### RemoteWorkspace

`RemoteWorkspace` represents a workspace for running Pulumi operations remotely with [Pulumi Deployments](/docs/deployments/concepts/), where the program is located in a remote Git repository.

## Stacks

A `Stack` is an isolated, independently configurable instance of a Pulumi program. It exposes methods for the full Pulumi lifecycle (`up`, `preview`, `refresh`, and `destroy`) as well as methods for managing configuration. Multiple stacks are commonly used to represent different phases of development---such as development, staging, and production---or feature branches. For background on stacks, see [Stacks](/docs/iac/concepts/stacks/).

A `RemoteStack` is the equivalent of a `Stack` for a `RemoteWorkspace`. It exposes the same lifecycle methods, run remotely from a remote workspace.

Beyond running a stack's lifecycle, Automation API can also manage which [ESC environments](/docs/esc/concepts/environments/) a stack imports, adding, listing, and removing them programmatically instead of editing a stack's configuration file by hand. See [Automation API for ESC](/docs/esc/integrations/automation-api/) for the supported methods and examples in each language.

## Programs

Automation API can drive two kinds of Pulumi programs.

### Local programs

A local program is a traditional, CLI-driven Pulumi program with its own directory, a `Pulumi.yaml` file, and a file that defines the program. Automation API can drive these programs the same way the CLI does.

### Inline programs

Unlike traditional Pulumi programs, an inline program doesn't require a separate package on disk with its own file and `Pulumi.yaml`. Inline programs are functions that can be authored in the same file as your Automation API program or imported from another package.

The program's lifecycle must be fully contained within the function, callback, or closure passed as the inline program. Performing actions outside the scope of the inline program function is unsafe and can lead to unpredictable behavior.

## Plugins

Pulumi providers are distributed as plugins that the engine loads at runtime, separately from the language SDK you import in your program. When you run the CLI, the engine automatically downloads any missing provider plugin before an operation. Automation API drives the same engine, so this behavior is identical: for providers published to the [Pulumi Registry](/registry/), you don't need to install plugins yourself---running `up`, `preview`, or `refresh` downloads them on demand, matching the SDK version your program references.

A `Workspace` still exposes an explicit `installPlugin` method (`install_plugin`, `InstallPlugin`, `InstallPluginAsync`). You need it only in specific cases:

- **Local or parameterized packages** that aren't published to the Registry---such as [`terraform-provider`](/registry/packages/terraform-provider/) or a custom provider---where the engine can't resolve the plugin automatically. See [Using local packages with Automation API](/docs/iac/guides/building-extending/automation-api/#using-local-packages-with-automation-api).
- **Pinning a specific plugin version** independently of the SDK, or **pre-fetching** plugins ahead of an operation---for example in air-gapped environments or to avoid a download during a timed deployment.

For background on plugins and the [`pulumi plugin`](/docs/iac/cli/commands/pulumi_plugin/) CLI commands that manage them, see [Pulumi packages](/docs/iac/concepts/packages/).

## Importing resources

A `Stack` also exposes an import operation, the programmatic equivalent of the [`pulumi import`](/docs/iac/cli/commands/pulumi_import/) CLI command. It brings existing cloud resources under Pulumi management without creating or modifying anything in the target cloud, generates program code for the imported resources, and records them in the stack's state so later updates manage them going forward. This makes it the building block for programmatic brownfield adoption---platforms that migrate teams onto Pulumi Cloud in bulk, rather than one resource at a time from the CLI, drive that migration through this method.

The method takes a list of resources to import, each identified by its Pulumi type token, a logical name, and the cloud provider's own resource ID. If any imported resource specifies a parent or provider, you also need a name table mapping the language names used in the generated program to their corresponding parent and provider URNs. By default, imported resources are protected from deletion and the operation generates program code alongside the import; both behaviors can be turned off.

The method name differs slightly across languages, since `import` is a reserved word in some of them:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language "typescript" %}}

```typescript
import { LocalWorkspace } from "@pulumi/pulumi/automation";

const stack = await LocalWorkspace.createOrSelectStack(args);

const result = await stack.import({
    resources: [
        {
            type: "aws:s3/bucketV2:BucketV2",
            name: "my-bucket",
            id: "my-existing-bucket-name",
        },
    ],
    protect: false,
});

console.log(result.generatedCode);
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
from pulumi import automation as auto
from pulumi.automation import ImportResource

stack = auto.create_or_select_stack(stack_name=stack_name, work_dir=work_dir)

result = stack.import_resources(
    resources=[
        ImportResource(
            type="aws:s3/bucketV2:BucketV2",
            name="my-bucket",
            id="my-existing-bucket-name",
        ),
    ],
    protect=False,
)

print(result.generated_code)
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
import (
    "fmt"

    "github.com/pulumi/pulumi/sdk/v3/go/auto"
    "github.com/pulumi/pulumi/sdk/v3/go/auto/optimport"
)

stack, err := auto.UpsertStackLocalSource(ctx, stackName, workDir)
if err != nil {
    return err
}

result, err := stack.ImportResources(ctx,
    optimport.Resources([]*optimport.ImportResource{
        {
            Type: "aws:s3/bucketV2:BucketV2",
            Name: "my-bucket",
            ID:   "my-existing-bucket-name",
        },
    }),
    optimport.Protect(false),
)
if err != nil {
    return err
}

fmt.Println(result.GeneratedCode)
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
using Pulumi.Automation;

var stack = await LocalWorkspace.CreateOrSelectStackAsync(args);

var result = await stack.ImportAsync(new ImportOptions
{
    Resources = new List<ImportResource>
    {
        new ImportResource
        {
            Type = "aws:s3/bucketV2:BucketV2",
            Name = "my-bucket",
            Id = "my-existing-bucket-name",
        },
    },
    Protect = false,
});

Console.WriteLine(result.GeneratedCode);
```

{{% /choosable %}}

{{% choosable language "java" %}}

The Java Automation API doesn't yet expose a resource-import method; `WorkspaceStack` has no equivalent to the other languages' `import`/`import_resources`/`ImportResources`/`ImportAsync`. Drive `pulumi import` directly through the CLI in the meantime.

{{% /choosable %}}

{{% /chooser %}}

This capability has shipped since Pulumi CLI v3.127.0. If your program [installs the CLI programmatically](/docs/iac/guides/building-extending/automation-api/#install-the-cli-programmatically) rather than relying on a preinstalled copy, make sure it resolves to that version or later.

## Supported languages

Like the rest of Pulumi, Automation API is available in multiple languages, so you can build applications that use it in TypeScript/JavaScript, Python, Go, .NET, and Java. Automation API also supports cross-language use, where it runs in a program written in a different language than the Pulumi programs it manages.

Each language has its own Automation API reference documentation. Follow the link in the **API reference** column below to view the reference for your language.

|                                                        | API reference                                                           | Status |
| ------------------------------------------------------ | ----------------------------------------------------------------------- | ------ |
| <img src="/logos/tech/logo-ts.png" class="h-10" />     | [TypeScript](/docs/reference/pkg/nodejs/pulumi/pulumi/modules/automation.html) | Stable |
| <img src="/logos/tech/logo-js.png" class="h-10" />     | [JavaScript](/docs/reference/pkg/nodejs/pulumi/pulumi/modules/automation.html) | Stable |
| <img src="/logos/tech/logo-python.png" class="h-10" /> | [Python](/docs/reference/pkg/python/pulumi/#module-pulumi.automation) | Stable |
| <img src="/logos/tech/dotnet.png" class="h-10" />      | [.NET](/docs/reference/pkg/dotnet/pulumi.automation/pulumi.automation.html) | Stable |
| <img src="/logos/tech/logo-golang.png" class="h-10" /> | [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/auto?tab=doc) | Stable |
| <img src="/logos/tech/java.svg" class="h-10" /> | [Java](/docs/reference/pkg/java/com/pulumi/automation/package-summary.html) | Stable |

## Examples

The [`automation-api-examples` repository](https://github.com/pulumi/automation-api-examples) contains runnable examples for every supported language, covering common patterns such as inline and local programs, cross-language programs, database migrations, and exposing Pulumi over HTTP:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

- [Inline Program - ts-node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/inlineProgram-tsnode)
- [Inline Program - tsc + node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/inlineProgram-ts)
- [Local Program - ts-node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/localProgram-tsnode)
- [Cross-Language Program - ts-node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/crossLanguage-tsnode)
- [Pulumi Over HTTP - tsc + node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/pulumiOverHttp-ts)
- [Database Migration - tsc + node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/databaseMigration-ts)
- [Remote Deployment - ts-node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/remoteDeployment-tsnode)

{{% /choosable %}}

{{% choosable language python %}}

- [Inline Program](https://github.com/pulumi/automation-api-examples/blob/main/python/inline_program)
- [Local Program](https://github.com/pulumi/automation-api-examples/blob/main/python/local_program)
- [Cross-Language Program](https://github.com/pulumi/automation-api-examples/blob/main/python/cross_language)
- [Database Migration](https://github.com/pulumi/automation-api-examples/blob/main/python/database_migration)
- [Pulumi Over HTTP](https://github.com/pulumi/automation-api-examples/blob/main/python/pulumi_over_http)
- [Pulumi via Jupyter Notebook](https://github.com/pulumi/automation-api-examples/blob/main/python/pulumi_via_jupyter)
- [Remote Deployment](https://github.com/pulumi/automation-api-examples/blob/main/python/remote_deployment)

{{% /choosable %}}
{{% choosable language go %}}

- [Inline Program](https://github.com/pulumi/automation-api-examples/blob/main/go/inline_program)
- [Local Program](https://github.com/pulumi/automation-api-examples/blob/main/go/local_program)
- [Inline/Local Hybrid Program](https://github.com/pulumi/automation-api-examples/blob/main/go/inline_local_hybrid)
- [Multi-Stack Orchestration](https://github.com/pulumi/automation-api-examples/blob/main/go/multi_stack_orchestration)
- [Pulumi Over HTTP](https://github.com/pulumi/automation-api-examples/blob/main/go/pulumi_over_http)
- [Database Migration](https://github.com/pulumi/automation-api-examples/blob/main/go/database_migration)
- [Git Repo](https://github.com/pulumi/automation-api-examples/blob/main/go/git_repo_program)
- [Remote Deployment](https://github.com/pulumi/automation-api-examples/blob/main/go/remote_deployment)

{{% /choosable %}}
{{% choosable language csharp %}}

- [Inline Program](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/InlineProgram)
- [Local Program](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/LocalProgram)
- [Cross-Language Program](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/CrossLanguage)
- [Database Migration](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/DatabaseMigration)
- [Remote Deployment](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/RemoteDeployment)

{{% /choosable %}}

{{% choosable language java %}}

- [Inline Program](https://github.com/pulumi/automation-api-examples/blob/main/java/inlineProgram)
- [Local Program](https://github.com/pulumi/automation-api-examples/blob/main/java/localProgram)
- [Database Migration](https://github.com/pulumi/automation-api-examples/blob/main/java/databaseMigration)

{{% /choosable %}}

{{% /chooser %}}

## Giving feedback

We encourage you to [file an issue](https://github.com/pulumi/pulumi/issues/new?assignees=&labels=needs-triage&template=bug_report.md&title=) if you have feedback on using Automation API.
