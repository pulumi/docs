---
title_tag: "Automation API Guides"
meta_desc: The Pulumi Automation API is a programmatic interface for running Pulumi programs without the Pulumi CLI. View our Automation API guides here.
title: Automation API
h1: Automation API
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    usingpulumi:
        identifier: automation-api
        weight: 3
aliases:
- /docs/guides/automation-api/
---

The Pulumi Automation API is a programmatic interface for running Pulumi programs without the Pulumi CLI. Conceptually, this can be thought of as encapsulating the functionality of the CLI (`pulumi up`, `pulumi preview`, `pulumi destroy`, `pulumi stack init`, etc.) but with more flexibility. It is a strongly typed and safe way to use Pulumi in embedded contexts such as web servers, without requiring invoking the CLI from a shell process.

![automation-api](automation-api.png)

Automation API allows you to embed Pulumi within your application code, making it easy to create custom experiences on top of Pulumi that are tailored to your use-case, domain, and team.

{{% notes type="info" %}}
Automation API requires the Pulumi CLI to be installed and available in your `PATH` environment variable.
{{% /notes %}}

## Getting started

To learn how to use Automation API, see [Getting Started with Automation API](/docs/using-pulumi/automation-api/getting-started-automation-api/).

## Examples

The following examples demonstrate how to use Automation API in various use cases.

{{< chooser language "typescript,javascript,python,go,csharp" >}}

{{% choosable language typescript %}}

* [Inline Program - ts-node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/inlineProgram-tsnode)
* [Inline Program - tsc + node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/inlineProgram-ts)
* [Local Program - ts-node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/localProgram-tsnode)
* [Cross-Language Program - ts-node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/crossLanguage-tsnode)
* [Pulumi Over HTTP - tsc + node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/pulumiOverHttp-ts)
* [Database Migration - tsc + node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/databaseMigration-ts)
* [Remote Deployment - ts-node](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/remoteDeployment-tsnode)

{{% /choosable %}}
{{% choosable language javascript %}}

* [Inline Program](https://github.com/pulumi/automation-api-examples/blob/main/nodejs/inlineProgram-js)

{{% /choosable %}}
{{% choosable language python %}}

* [Inline Program](https://github.com/pulumi/automation-api-examples/blob/main/python/inline_program)
* [Local Program](https://github.com/pulumi/automation-api-examples/blob/main/python/local_program)
* [Cross-Language Program](https://github.com/pulumi/automation-api-examples/blob/main/python/cross_language)
* [Database Migration](https://github.com/pulumi/automation-api-examples/blob/main/python/database_migration)
* [Pulumi Over HTTP](https://github.com/pulumi/automation-api-examples/blob/main/python/pulumi_over_http)
* [Pulumi via Jupyter Notebook](https://github.com/pulumi/automation-api-examples/blob/main/python/pulumi_via_jupyter)
* [Remote Deployment](https://github.com/pulumi/automation-api-examples/blob/main/python/remote_deployment)

{{% /choosable %}}
{{% choosable language go %}}

* [Inline Program](https://github.com/pulumi/automation-api-examples/blob/main/go/inline_program)
* [Local Program](https://github.com/pulumi/automation-api-examples/blob/main/go/local_program)
* [Inline/Local Hybrid Program](https://github.com/pulumi/automation-api-examples/blob/main/go/inline_local_hybrid)
* [Multi-Stack Orchestration](https://github.com/pulumi/automation-api-examples/blob/main/go/multi_stack_orchestration)
* [Pulumi Over HTTP](https://github.com/pulumi/automation-api-examples/blob/main/go/pulumi_over_http)
* [Database Migration](https://github.com/pulumi/automation-api-examples/blob/main/go/database_migration)
* [Git Repo](https://github.com/pulumi/automation-api-examples/blob/main/go/git_repo_program)
* [Remote Deployment](https://github.com/pulumi/automation-api-examples/blob/main/go/remote_deployment)

{{% /choosable %}}
{{% choosable language csharp %}}

* [Inline Program](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/InlineProgram)
* [Local Program](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/LocalProgram)
* [Cross-Language Program](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/CrossLanguage)
* [Database Migration](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/DatabaseMigration)
* [Remote Deployment](https://github.com/pulumi/automation-api-examples/blob/main/dotnet/RemoteDeployment)

{{% /choosable %}}

{{% /chooser %}}

Visit the [examples repo](https://github.com/pulumi/automation-api-examples) for more code examples and links to projects using Automation API.

## Languages

Like all of Pulumi, Automation API is available in multiple languages, so you can create applications that use it in TypeScript/JavaScript, Python, Go, and C#.

Automation API supports cross-language implementations where it runs in a program of a different language than the Pulumi programs it manages.

|                                                        | Language                                                                | Status                                                            |
| ------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------- |
| <img src="/logos/tech/logo-ts.png" class="h-10" />     | [TypeScript](/docs/reference/pkg/nodejs/pulumi/pulumi/automation/) | Stable                                                            |
| <img src="/logos/tech/logo-js.png" class="h-10" />     | [JavaScript](/docs/reference/pkg/nodejs/pulumi/pulumi/automation/) | Stable                                                            |
| <img src="/logos/tech/logo-python.png" class="h-10" /> | [Python](/docs/reference/pkg/python/pulumi/#module-pulumi.automation) | Stable                                                           |
| <img src="/logos/tech/dotnet.png" class="h-10" />      | [.NET](/docs/reference/pkg/dotnet/Pulumi.Automation/Pulumi.Automation.html) | Stable |
| <img src="/logos/tech/logo-golang.png" class="h-10" /> | [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/auto?tab=doc) | Stable |

## Blog Posts

For more ideas of what's possible with Automation API, [check out](/blog/tag/automation-api/) some of the ways we and community members use it in different use cases.

## Known issues

The GA release of Automation API is stable; however, we know bugs can pop up. We are tracking a list of [known issues](https://github.com/pulumi/pulumi/issues?q=is%3Aissue+is%3Aopen+label%3Aarea%2Fautomation-api) and encourage you to [file additional issues](https://github.com/pulumi/pulumi/issues/new?assignees=&labels=needs-triage&template=bug_report.md&title=) as you find them.
