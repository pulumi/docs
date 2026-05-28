---
title_tag: "C#, VB, F# (.NET) | Languages & SDKs"
meta_desc: An overview of how to use .NET languages like C#, F#, and VB with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
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

Pulumi supports writing your infrastructure as code in any .NET language, including C#, F#, and Visual Basic. Using a general-purpose language for infrastructure as code provides several key advantages:

- **Familiar syntax**: Write infrastructure code using the same language and patterns you already know
- **Rich ecosystem**: Leverage the [NuGet](https://www.nuget.org/) package ecosystem in your infrastructure code
- **Native tooling**: Use your existing IDE, such as Visual Studio, Visual Studio Code, or Rider, along with test frameworks such as xUnit, NUnit, and MSTest, without requiring plugins or extensions
- **Type safety**: Catch errors at compile time with .NET's static type system

## Installation requirements

### .NET runtime

Pulumi supports any [supported version](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core#lifecycle) of .NET. We recommend using a recent release for the best experience. Pulumi currently tests against .NET 8, .NET 9, and .NET 10.

To use the .NET runtime, set `runtime: dotnet` in your `Pulumi.yaml`:

```yaml
runtime: dotnet
```

Install the [.NET SDK](https://dotnet.microsoft.com/download) for your platform.

### Supported .NET languages

Pulumi provides templates and first-class support for the three main .NET languages:

- **C#**: Fully supported
- **F#**: Fully supported
- **Visual Basic**: Fully supported

Because Pulumi runs your compiled .NET assembly, any other language that targets the .NET runtime can also be used, though only C#, F#, and Visual Basic ship with `pulumi new` templates.

### Package management

Pulumi packages are distributed on [NuGet](https://www.nuget.org/packages?q=pulumi) and managed with the standard `dotnet` CLI. Add the Pulumi SDK and provider packages to your project with `dotnet add package`:

```bash
$ dotnet add package Pulumi
```

## Getting started

The fastest way to get started with Pulumi and .NET is to use a template:

```bash
$ pulumi new csharp
```

Templates are also available for `fsharp` and `visualbasic`. You can discover additional templates by running `pulumi new` with no arguments, or you can initialize a Pulumi program by supplying a specific URL to the `pulumi new` command. For example:

```bash
$ pulumi new https://github.com/pulumi/templates/tree/master/aws-csharp
```

See the [`pulumi new` documentation](/docs/iac/cli/commands/pulumi_new/) for full details.

The base templates are cloud agnostic, and you will need to install additional NuGet packages for the cloud provider of your choice. Additional templates are available that do this for you:

- `pulumi new aws-csharp`: creates a starter AWS C# project
- `pulumi new azure-csharp`: creates a starter Azure C# project
- `pulumi new gcp-csharp`: creates a starter Google Cloud C# project

Equivalent cloud-specific templates are available for F# (for example, `aws-fsharp`) and Visual Basic (for example, `aws-visualbasic`).

### Program entrypoint

A Pulumi .NET program is an ordinary .NET console application whose entry point calls `Deployment.RunAsync`. New C# templates use top-level statements:

```csharp
using Pulumi;

return await Deployment.RunAsync(() =>
{
    // Declare your resources here.
});
```

By default, Pulumi builds and runs the .NET project in the project directory using `dotnet run`. You can point at a different project file with the top-level `main` attribute in your `Pulumi.yaml`:

```yaml
name: my-project
runtime: dotnet
main: ./infra/infra.csproj
```

If you prefer to build the program yourself, set the `binary` runtime option to the path of a prebuilt assembly, and Pulumi will run it directly instead of compiling on each invocation:

```yaml
runtime:
  name: dotnet
  options:
    binary: bin/MyInfra.dll
```

## Defining resources

Writing a Pulumi program in .NET involves declaring infrastructure resources using resource constructors. Here are the key concepts:

- **Declare resources**: Create infrastructure resources by instantiating resource classes from provider packages. For example, `new Bucket("my-bucket")` creates an S3 bucket.
- **Inputs and outputs**: The Pulumi programming model uses `Input` and `Output` types to track dependencies between resources. Understanding how to work with inputs and outputs is essential for building infrastructure. See the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation for details.
- **Immutable infrastructure**: Once declared, resource properties are immutable within your program. Changes to resource definitions result in updates during the next deployment.
- **Stack outputs**: Export values from your program by returning a dictionary from `Deployment.RunAsync` (or by decorating fields with the `[Output]` attribute) to make them accessible from the CLI or to other Pulumi programs.

The Pulumi SDK provides constructs for working with key Pulumi concepts. For more information, see:

- [Pulumi Concepts](/docs/iac/concepts/)
- [How Pulumi Works](/docs/iac/guides/basics/how-pulumi-works/)

## Program execution

Pulumi programs are most commonly executed using the Pulumi CLI commands such as `pulumi up`, `pulumi preview`, and `pulumi destroy`. The CLI builds your .NET program and handles authentication, state management, and orchestrating resource operations.

Alternatively, you can use the [Automation API](/docs/iac/concepts/automation-api/) to programmatically control the Pulumi engine from within your .NET code. The Automation API allows you to:

- Embed Pulumi operations in regular .NET applications
- Build custom deployment tools and workflows
- Create self-service infrastructure platforms

With Automation API, your .NET code controls Pulumi, rather than Pulumi controlling your code.

## Documentation and resources

### Pulumi SDK

The [Pulumi SDK (`Pulumi`)](/docs/reference/pkg/dotnet/pulumi/pulumi.html) is distributed on NuGet and contains the core constructs for working with Pulumi, including resources, configuration, stack outputs, and more. You will need to reference it in most Pulumi programs. F# users can also reference the [`Pulumi.FSharp`](/docs/reference/pkg/dotnet/pulumi.fsharp/pulumi.fsharp.html) package for idiomatic F# helpers, and the [`Pulumi.Automation`](/docs/reference/pkg/dotnet/pulumi.automation/pulumi.automation.html) package provides the Automation API.

### Provider SDKs

For managing resources in a Pulumi program, you can find the relevant SDK reference documentation for each provider in [the Pulumi Registry](/registry/), which houses 100+ .NET packages.

### Policy SDK

Pulumi Policy as Code packs cannot be authored in .NET. Policy packs are authored in [TypeScript/JavaScript](/docs/reference/pkg/nodejs/pulumi/policy/) or [Python](/docs/reference/pkg/python/pulumi_policy/). A .NET program can still be validated by policy packs written in those languages. For more information, see [Pulumi Policy as Code](/docs/insights/policy/).

### Dev versions

Pulumi SDKs also publish pre-release versions that include all the latest changes from the main development branch. To install a pre-release version, add the `--prerelease` flag to `dotnet add package`. For example:

```bash
$ dotnet add package Pulumi --prerelease
```

For more information on when and how to use dev builds, see [Using dev builds for unreleased fixes](/docs/iac/operations/debugging/using-dev-builds/).

### Testing

- [Unit testing](/docs/iac/concepts/testing/unit/): Test your infrastructure code in isolation
- [Integration testing](/docs/iac/concepts/testing/integration/): Test your infrastructure deployments end-to-end

## Troubleshooting .NET versions

Pulumi supports multiple side-by-side versions of the .NET runtime at once, so you can maintain programs that target different runtimes on the same machine. If the version your project targets is not installed, you may encounter an error like this:

```
error NETSDK1045: The current .NET SDK does not support targeting .NET 10.0.  Either target .NET 8.0 or lower, or use a version of the .NET SDK that supports .NET 10.0. Download the .NET SDK from https://aka.ms/dotnet/download
```

This error means the program requires a .NET version you do not have installed. The target version is defined by the `<TargetFramework>` property in your `.csproj`, `.fsproj`, or `.vbproj` file:

```xml
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

The `<TargetFramework>` value (`net8.0` above) indicates which .NET version the program requires. Install that version, or update the property to match a version you already have. To see what is installed, run `dotnet --info`. Note that SDKs, the `NETCore.App` runtime, and the `AspNetCore.App` runtime are listed separately; check the error message to determine which one you are missing, since some installers do not include the ASP.NET Core runtime.

If you are still stuck, reach out on the [Community Slack](https://slack.pulumi.com/) and we are happy to help you get unblocked.
