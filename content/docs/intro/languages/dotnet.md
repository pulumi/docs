---
title: ".NET Core"
menu:
  intro:
    parent: languages
    weight: 3

aliases: ["/dotnet/"]
---

<img src="/logos/tech/dotnet.png" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports infrastructure as code using any .NET Core language. You can use your favorite .NET tools &mdash; such as editors, package managers, build systems, and test frameworks &mdash; to create, deploy, and manage infrastructure on any cloud, including Azure, AWS, and GCP.

> **Note:** Pulumi for .NET is in preview and is under active development. We would [love your feedback](https://github.com/pulumi/pulumi/issues/new)!

For example, this C# program provisions an Azure resource group and storage account:

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Azure.Core;
using Pulumi.Azure.Storage;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(() => {
            // Create an Azure Resource Group
            var resourceGroup = new ResourceGroup("resourceGroup");

            // Create an Azure Storage Account
            var storageAccount = new Account("storage", new AccountArgs
            {
                ResourceGroupName = resourceGroup.Name,
                AccountReplicationType = "LRS",
                AccountTier = "Standard",
            });

            // Export the connection string for the storage account
            return new Dictionary<string, object>
            {
                { "connectionString", storageAccount.PrimaryConnectionString },
            };
        });
    }
}
```

## Getting Started

The fastest way to get up and running is to choose from one of the following Getting Started guides:

<div class="md:flex flex-row mt-6 mb-6">
    <a class="btn bg-transparent border w-1/2 border-solid border-gray-300 hover:bg-gray-200 justify-center p-4 mr-5" href="{{< relref "../../get-started/aws" >}}">
        <img class="h-5 ml-auto mr-auto" src="/logos/tech/aws.svg" alt="AWS">
    </a>
    <a class="btn bg-transparent border w-1/2 border-solid border-gray-300 hover:bg-gray-200 justify-center items-center p-4 mr-4" href="{{< relref "../../get-started/azure" >}}">
        <img class="h-5 ml-auto mr-auto" src="/logos/tech/azure.svg" alt="Azure">
    </a>
    <a class="btn bg-transparent border w-1/2 border-solid border-gray-300 hover:bg-gray-200 justify-center p-4 mr-4" href="{{< relref "../../get-started/gcp" >}}">
        <img class="h-5 ml-auto mr-auto" src="/logos/tech/gcp.svg" alt="Google Cloud">
    </a>
    <a class="btn bg-transparent border w-1/2 border-solid border-gray-300 hover:bg-gray-200 justify-center p-4" href="{{< relref "../../get-started/kubernetes" >}}">
        <img class="h-5 ml-auto mr-auto" src="/logos/tech/k8s.svg" alt="Kubernetes">
    </a>
</div>

> The Getting Started guides currently only demonstrate C#. For F# and Visual Basic, please refer to the
> documentation below. They will work just fine &mdash; the guides simply aren't ready for them yet.

## Prerequisites

Before using Pulumi for .NET, you will need to install both Pulumi and .NET Core 3.0 or later. If you follow the Getting Started guides above, they will walk you through doing this.

1. [Install Pulumi]({{< relref "/docs/get-started/install" >}})
1. [Install .NET Core SDK 3.0](https://dotnet.microsoft.com/download)


## C\#, F\#, and VB Templates

As of version 1.5, Pulumi supports .NET Core 3.0. You can write Pulumi programs in your favorite .NET language to get additional verification and tooling benefits. The fastest way to get started is to use a template. The template will autogenerate a set of files and initialize a Pulumi project. The getting started guides shown above will help do this on your cloud of choice, but this section describes doing so independently.

{{< langchoose dotnetonly >}}

<div class="language-prologue-csharp"></div>
<span>
{{% md %}}
You can write Pulumi programs in **C#**. From an empty directory, create a new C# project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new csharp
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change), an `Infra.csproj` file that holds references used by the project, and a `Program.cs` file, containing your program. The `.csproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

To deploy your infrastructure run `pulumi up` and the Pulumi engine automatically runs `dotnet build` as part of the deployment. Pulumi will perform the operations needed to deploy the infrastructure you have declared.

This `csharp` template is cloud agnostic, and you will need to install NuGet packages for the cloud provider of your choice. Additional templates are available:

* `aws-csharp`: a starter AWS project in C#
* `azure-csharp`: a starter Azure project in C#
* `gcp-csharp`: a starter GCP project in C#
{{% /md %}}
</span>

<div class="language-prologue-fsharp"></div>
<span>
{{% md %}}
You can write Pulumi programs in **F#**. From an empty directory, create a new F# project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new fsharp
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change), an `Infra.fsproj` file that holds references used by the project, and a `Program.fs` file, containing your program. The `.fsproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

To deploy your infrastructure run `pulumi up` and the Pulumi engine automatically runs `dotnet build` as part of the deployment. Pulumi will perform the operations needed to deploy the infrastructure you have declared.

This `fsharp` template is cloud agnostic, and you will need to install NuGet packages for the cloud provider of your choice. Additional templates are available:

* `aws-fsharp`: a starter AWS project in F#
* `azure-fsharp`: a starter Azure project in F#
* `gcp-fsharp`: a starter GCP project in F#
{{% /md %}}
</span>

<div class="language-prologue-visualbasic"></div>
<span>
{{% md %}}
You can write Pulumi programs in **Visual Basic**. From an empty directory, create a new Visual Basic project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new visualbasic
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change), an `Infra.vbproj` file that holds references used by the project, and a `Program.vb` file, containing your program. The `.vbproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

To deploy your infrastructure run `pulumi up` and the Pulumi engine automatically runs `dotnet build` as part of the deployment. Pulumi will perform the operations needed to deploy the infrastructure you have declared.

This `visualbasic` template is cloud agnostic, and you will need to install NuGet packages for the cloud provider of your choice. Additional templates are available:

* `aws-visualbasic`: a starter AWS project in F#
* `azure-visualbasic`: a starter Azure project in F#
* `gcp-visualbasic`: a starter GCP project in F#
{{% /md %}}
</span>

## .NET Core Tools

Pulumi packages are distributed on [NuGet for download](https://www.nuget.org/packages?q=pulumi).

Although you can use any editor, [Visual Studio Code](https://code.visualstudio.com/download) or [Visual Studio](https://visualstudio.microsoft.com/downloads/) will deliver full tooling support for .NET Core out-of-the-box, including auto-completion, red error markers and build errors.

![VSCode](/images/docs/quickstart/vscode-dotnet.png)

## Continuous Delivery

In addition to the CLI-driven workflows shown above, you can continuously deploy your infrastructure using .NET by integrating with your CI/CD provider of choice. This ensures automated deployments triggered by events such as commits to your Git repo.

### Azure DevOps Pipelines

<img src="/logos/tech/azuredevops.png" align="right" width="100" style="padding:0 0 16px 32px">

Pulumi can deploy infrastructure changes from your Azure DevOps Pipelines. This enables easy integration with your existing automation while using .NET Core for your infrastructure as code, leveraging the Pulumi task in the Visual Studio Marketplace.

To learn more, [see the Pulumi Azure DevOps user guide]({{< relref "/docs/guides/continuous-delivery/azure-devops" >}}).

### GitHub Actions

<img src="/logos/tech/githubactions.png" align="right" width="120" style="padding:0 0 16px 32px">

Pulumi can deploy infrastructure using GitHub Actions, making Git-driven deployments of your infrastructure as code straightforward. To learn more, [see the Pulumi GitHub Actions user guide]({{< relref "/docs/guides/continuous-delivery/github-actions" >}}).

There is also a Pulumi GitHub App that integrates with Pull Requests so that you get previews of deployments before they are merged inline in your PRs where it's easy to comment and collaborate. [Read more here about how to install this app into your organization]({{< relref "/docs/guides/continuous-delivery/github-app" >}}).

### Other CI/CD Integrations

If you don't use Azure DevOps or GitHub Actions, Pulumi also supports a number of other CI/CD integrations. For a complete list, [go here]({{< relref "/docs/guides/continuous-delivery" >}}).
