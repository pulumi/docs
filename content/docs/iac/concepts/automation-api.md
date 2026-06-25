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

`RemoteWorkspace` represents a workspace for running Pulumi operations remotely with [Pulumi Deployments](/docs/pulumi-cloud/deployments/), where the program is located in a remote Git repository.

## Stacks

A `Stack` is an isolated, independently configurable instance of a Pulumi program. It exposes methods for the full Pulumi lifecycle (`up`, `preview`, `refresh`, and `destroy`) as well as methods for managing configuration. Multiple stacks are commonly used to represent different phases of development---such as development, staging, and production---or feature branches. For background on stacks, see [Stacks](/docs/iac/concepts/stacks/).

A `RemoteStack` is the equivalent of a `Stack` for a `RemoteWorkspace`. It exposes the same lifecycle methods, run remotely from a remote workspace.

## Programs

Automation API can drive two kinds of Pulumi programs.

### Local programs

A local program is a traditional, CLI-driven Pulumi program with its own directory, a `Pulumi.yaml` file, and a file that defines the program. Automation API can drive these programs the same way the CLI does.

### Inline programs

Unlike traditional Pulumi programs, an inline program doesn't require a separate package on disk with its own file and `Pulumi.yaml`. Inline programs are functions that can be authored in the same file as your Automation API program or imported from another package.

The program's lifecycle must be fully contained within the function, callback, or closure passed as the inline program. Performing actions outside the scope of the inline program function is unsafe and can lead to unpredictable behavior.

## Supported languages

Like the rest of Pulumi, Automation API is available in multiple languages, so you can build applications that use it in TypeScript/JavaScript, Python, Go, C#, and Java. Automation API also supports cross-language use, where it runs in a program written in a different language than the Pulumi programs it manages.

|                                                        | Language                                                                | Status |
| ------------------------------------------------------ | ----------------------------------------------------------------------- | ------ |
| <img src="/logos/tech/logo-ts.png" class="h-10" />     | [TypeScript](/docs/reference/pkg/nodejs/pulumi/pulumi/automation/) | Stable |
| <img src="/logos/tech/logo-js.png" class="h-10" />     | [JavaScript](/docs/reference/pkg/nodejs/pulumi/pulumi/automation/) | Stable |
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
