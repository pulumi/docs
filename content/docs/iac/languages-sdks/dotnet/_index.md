---
title_tag: "C#, VB, F# (.NET) | Languages & SDKs"
meta_desc: An overview of how to use .NET languages like C# and F# with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: C#, VB, F# (.NET)
h1: Pulumi & C#, VB, F# (.NET)
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: C#, F#, VB (.NET)
        parent: iac-languages
        weight: 3
        identifier: iac-languages-dotnet
    languages:
        identifier: dotnet
        weight: 3
aliases:
    - /dotnet/
    - /docs/intro/languages/dotnet/
    - /docs/languages-sdks/dotnet/
---

<img src="/logos/tech/dotnet.png" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code in any .NET language using any [supported version](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core#lifecycle).

You can use your favorite .NET tools &mdash; such as editors, package managers, build systems, and test frameworks &mdash; to create, deploy, and manage infrastructure on any cloud, including Azure, AWS, and Google Cloud.

<a class="btn btn-secondary" href="https://dotnet.microsoft.com/download" target="_blank" title="Install .NET">Install .NET</a>

## Prerequisites

Before using Pulumi for .NET, you will need to install both Pulumi and a [supported .NET version](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core#lifecycle).

1. [Install Pulumi](/docs/install/)
1. [Install .NET SDK](https://dotnet.microsoft.com/download)

## Example

{{% chooser language "csharp,fsharp,visualbasic" %}}

{{% choosable language csharp %}}
For example, this C# program provisions an Azure resource group and storage account:

```csharp
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Azure.Core;
using Pulumi.Azure.Storage;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

public class MyStack : Stack
{
    public MyStack()
    {
        // Create an Azure Resource Group
        var resourceGroup = new ResourceGroup("resourceGroup", new ResourceGroupArgs
        {
            Location = "West Europe",
        });

        // Create an Azure Storage Account
        var storageAccount = new Account("storage", new AccountArgs
        {
            ResourceGroupName = resourceGroup.Name,
            AccountReplicationType = "LRS",
            AccountTier = "Standard",
        });

        // Export the connection string for the storage account
        this.ConnectionString = storageAccount.PrimaryConnectionString;
    }

    [Output] public Output<string> ConnectionString { get; set; }
}
```

{{% /choosable %}}

{{% choosable language fsharp %}}
For example, this F# program provisions an Azure resource group and storage account:

```fsharp
module Program

open Pulumi.FSharp
open Pulumi.Azure.Core
open Pulumi.Azure.Storage

let infra () =
    // Create an Azure Resource Group
    let resourceGroup = new ResourceGroup "resourceGroup"

    // Create an Azure Storage Account
    let storageAccount =
        new Account("storage",
            new AccountArgs
               (ResourceGroupName = io resourceGroup.Name,
                AccountReplicationType = input "LRS",
                AccountTier = input "Standard"))

    // Export the connection string for the storage account
    dict [("connectionString", storageAccount.PrimaryConnectionString :> obj)]

[<EntryPoint>]
let main _ =
  Deployment.run infra
```

{{% /choosable %}}

{{% choosable language visualbasic %}}
For example, this Visual Basic program provisions an Azure resource group and storage account:

```vb
Imports System.Threading.Tasks
Imports Pulumi
Imports Pulumi.Azure.Core
Imports Pulumi.Azure.Storage

Module Program
    Public Function Run() As IDictionary(Of String, Object)
        ' Create an Azure Resource Group
        Dim resourceGroup = New ResourceGroup("resourceGroup")

        ' Create an Azure Storage Account
        Dim storageAccount = New Account("storageAccount", New AccountArgs With {
            .ResourceGroupName = resourceGroup.Name,
            .AccountReplicationType = "LRS",
            .AccountTier = "Standard"
        })

        ' Export the connection string for the storage account
        Return New Dictionary(Of String, Object) From {
            {"connectionString", storageAccount.PrimaryConnectionString}
        }
    End Function

    Sub Main()
        Deployment.RunAsync(AddressOf Run).Wait()
    End Sub

End Module
```

{{% /choosable %}}

{{% /chooser %}}

## C#, F#, and VB Templates

The fastest way to get started is to use a template. The template will autogenerate a set of files and initialize a Pulumi project.

{{< chooser language "csharp,fsharp,visualbasic" >}}

{{% choosable language csharp %}}
From an empty directory, create a new C# project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new csharp
```

This creates a `Pulumi.yaml` [project file](/docs/concepts/projects/), an `myproject.csproj` file, and a `Program.cs` file containing the program entry point and resource definitions. The directory name becomes the project name in `Pulumi.yaml` and the `csproj` file name.

Additional cloud-specific templates are available:

* `pulumi new aws-csharp`
* `pulumi new azure-csharp`
* `pulumi new gcp-csharp`
{{% /choosable %}}

{{% choosable language fsharp %}}
From an empty directory, create a new F# project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new fsharp
```

This creates a `Pulumi.yaml` [project file](/docs/concepts/projects/), an `myproject.fsproj` file, and a `Program.fs` file containing your program. The directory name becomes the project name in `Pulumi.yaml` and the `fsproj` file name.

Additional cloud-specific templates are available:

* `pulumi new aws-fsharp`
* `pulumi new azure-fsharp`
* `pulumi new gcp-fsharp`
{{% /choosable %}}

{{% choosable language visualbasic %}}
From an empty directory, create a new Visual Basic project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new visualbasic
```

This creates a `Pulumi.yaml` [project file](/docs/concepts/projects/), an `myproject.vbproj` file, and a `Program.vb` file containing the program entry point and resource definitions. The directory name becomes the project name in `Pulumi.yaml` and the `vbproj` file name.

Additional cloud-specific templates are available:

* `pulumi new aws-visualbasic`
* `pulumi new azure-classic-visualbasic`
* `pulumi new gcp-visualbasic`
{{% /choosable %}}

{{< /chooser >}}

To deploy your infrastructure, run `pulumi up`. The Pulumi engine automatically runs `dotnet build` as part of the deployment.

The base templates are cloud agnostic. To use cloud-specific resources, install the appropriate NuGet packages for your cloud provider or use one of the cloud-specific templates listed above.

## .NET Tools

Pulumi packages are distributed on [NuGet for download](https://www.nuget.org/packages?q=pulumi).

Although you can use any editor, [Visual Studio Code](https://code.visualstudio.com/download), [Visual Studio](https://visualstudio.microsoft.com/downloads/), or [Rider](https://www.jetbrains.com/rider/) will deliver full tooling support for .NET out-of-the-box, including auto-completion, red error markers and build errors.

![VSCode](/images/docs/quickstart/vscode-dotnet.png)

## Pulumi Programming Model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using
Pulumi. [Concepts](/docs/intro/concepts) describes these concepts
with examples available in Python. These concepts are made available to you in the Pulumi SDK.

The Pulumi SDK is available to .NET developers as a Nuget package. To learn more,
[refer to the Pulumi SDK Reference Guide](/docs/reference/pkg/dotnet/pulumi/pulumi.html).

The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with .NET and Pulumi, and the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

## Continuous Delivery

In addition to the CLI-driven workflows shown above, you can continuously deploy your infrastructure using .NET by integrating with your CI/CD provider of choice. This ensures automated deployments triggered by events such as commits to your Git repo.

### Azure DevOps Pipelines

<img src="/logos/tech/azuredevops.png" align="right" width="100" style="padding:0 0 16px 32px">

Pulumi can deploy infrastructure changes from your Azure DevOps Pipelines. This enables easy integration with your existing automation while using .NET for your infrastructure as code, leveraging the Pulumi task in the Visual Studio Marketplace.

To learn more, [see the Pulumi Azure DevOps user guide](/docs/using-pulumi/continuous-delivery/azure-devops/).

### GitHub Actions

<img src="/logos/tech/githubactions.png" align="right" width="120" style="padding:0 0 16px 32px">

Pulumi can deploy infrastructure using GitHub Actions, making Git-driven deployments of your infrastructure as code straightforward. To learn more, [see the Pulumi GitHub Actions user guide](/docs/using-pulumi/continuous-delivery/github-actions/).

There is also a [Pulumi GitHub App](/docs/using-pulumi/continuous-delivery/github-app/) that integrates with Pull Requests so that you get previews of deployments before they are merged inline in your PRs where it's easy to comment and collaborate.

### Other CI/CD Integrations

If you don't use Azure DevOps or GitHub Actions, Pulumi also supports a number of other [CI/CD integrations](/docs/using-pulumi/continuous-delivery/).

## Package Documentation

### Standard Packages

In addition to the standard packages the [Pulumi Registry](/registry/) houses 100+ .NET packages.

<dl class="tabular">
    <dt>Pulumi SDK</dt>
    <dd><a href="/docs/reference/pkg/dotnet/pulumi/pulumi.html">Pulumi</a></dd>
    <dt>Pulumi FSharp SDK</dt>
    <dd><a href="/docs/reference/pkg/dotnet/pulumi.fsharp/pulumi.fsharp.html">Pulumi.FSharp</a></dd>
    <dt>Pulumi Automation API</dt>
    <dd><a href="/docs/reference/pkg/dotnet/pulumi.automation/pulumi.automation.html">Pulumi.Automation</a></dd>
</dl>

### Dev Versions

Pulumi SDKs also publish pre-release versions that include all the latest changes from the main development branch. To use them, add the `--prerelease` flag. For example: `dotnet add package Pulumi --prerelease`.

## Troubleshooting

### What .NET version do I need to have installed?

While we will always officially support the [current set of .NET versions that are supported by Microsoft](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core#lifecycle), that isn't what is always in use at the moment. Pulumi supports multiple side-by-side versions of the .NET runtime at once. You might be supporting multiple programs that depend on different runtimes. Luckily, Pulumi actually is able to use a wide range of .NET runtime versions side-by-side.

This can get confusing. You may encounter an error like this:

```
Determining projects to restore...
    /usr/local/share/dotnet/sdk/8.0.420/Sdks/Microsoft.NET.Sdk/targets/Microsoft.NET.TargetFrameworkInference.targets(166,5): error NETSDK1045: The current .NET SDK does not support targeting .NET 10.0.  Either target .NET 8.0 or lower, or use a version of the .NET SDK that supports .NET 10.0. Download the .NET SDK from https://aka.ms/dotnet/download [/code/csharp-test/csharp-test.csproj]
    Build FAILED.
    /usr/local/share/dotnet/sdk/8.0.420/Sdks/Microsoft.NET.Sdk/targets/Microsoft.NET.TargetFrameworkInference.targets(166,5): error NETSDK1045: The current .NET SDK does not support targeting .NET 10.0.  Either target .NET 8.0 or lower, or use a version of the .NET SDK that supports .NET 10.0. Download the .NET SDK from https://aka.ms/dotnet/download [/code/csharp-test/csharp-test.csproj]
        0 Warning(s)
        1 Error(s)
    Time Elapsed 00:00:00.22

    [Pulumi Neo] Would you like help with these diagnostics?
    https://app.pulumi.com/pulumi/csharp-test/dev/previews/f0ba97bf-762b-465a-9c25-2d59cfe82976?explainFailure

error: failed to discover package requirements: 'dotnet build -nologo /code/csharp-test' exited with non-zero exit code: 1
```

This error means the Pulumi program requires .NET 10, but you have .NET 8 installed. You can either install .NET 10 or update the program to use your installed version. The target version is defined in your `.csproj`/`.fsproj`/`.vbproj` file:

```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Pulumi" Version="3.*" />
  </ItemGroup>

</Project>
```

The `<TargetFramework>` value `net8.0` indicates this code requires .NET 8. Depending on your project, this could be .NET 8, .NET 9, or .NET 10. Install the version that matches your project file.

To see the versions you have installed, run `dotnet --info`:

```
$ dotnet --info

.NET SDK:
 Version:   8.0.101
 Commit:    2ef4b6e3a4

Runtime Environment:
 OS Name:     Mac OS X
 OS Version:  14.0
 OS Platform: Darwin
 RID:         osx.14-x64
 Base Path:   /usr/local/share/dotnet/sdk/8.0.101/

Host:
  Version:      8.0.1
  Architecture: x64
  Commit:       2ef4b6e3a4

.NET SDKs installed:
  8.0.101 [/usr/local/share/dotnet/sdk]

.NET runtimes installed:
  Microsoft.AspNetCore.App 8.0.1 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.NETCore.App 8.0.1 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
```

Notice that SDKs, `NETCore.App`, and `AspNetCore.App` runtimes are listed separately. Check the error message to determine which you're missing, then install it. Some installers don't include the ASP.NET Core runtime, which can be confusing if your project needs it but you have the SDK installed.

At the time of this writing, .NET 8 is the current long-term support version, and all of our built-in .NET templates require .NET 8 or later. If you have an older version installed, upgrade your runtime before using a template. Always check the project file's `<TargetFramework>` property to confirm which version your project requires. We currently test on .NET 8, .NET 9, and .NET 10.

When in doubt, reach out! We have an active [Community Slack channel](https://slack.pulumi.com/) and are happy to help you get unblocked if you're running into an issue like this.
