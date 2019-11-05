---
title: ".NET"
menu:
  intro:
    parent: languages
    weight: 2

aliases: ["/docs/reference/dotnet/"]
---

{{< langchoose dotnetonly >}}

Pulumi supports programs written in any supported .NET language, including C#, F#, and Visual Basic. You can also use your favorite .NET tools such as editors, package managers, build systems, and test frameworks.

## Getting Started

### Prerequisites

1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)
1. [Install .NET Core 3.0+](https://dotnet.microsoft.com/download)

### Example .NET Project

You can get started with .NET using a Pulumi template. From an empty directory, create a new .NET project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new csharp
```

The template will autogenerate a set of files that make up a Pulumi project.

{{% lang csharp %}}

## C\#

You can write Pulumi programs in C# to get additional verification and tooling benefits. As of version 1.5, Pulumi supports .NET natively. The fastest way to get started with Pulumi in C#, is to use a template:

```bash
$ mkdir myproject && cd myproject
$ pulumi new csharp
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change), a `Infra.csproj` file that holds references used by the project, and a `Program.cs` file, containing your program. The `.csproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

In addition to the C# template, there are additional .NET templates for cloud providers. To list the templates:

```bash
$ pulumi new
```
{{% /lang %}}


{{% lang fsharp %}}

## F\#

You can write Pulumi programs in F# to get additional verification and tooling benefits. The fastest way to get started with Pulumi in F# is to use a template:

```bash
$ mkdir myproject && cd myproject
$ pulumi new fsharp
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change), a `Infra.fsproj` file that holds references used by the project, and a `Program.fs` file, containing your program. The `.fsproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

In addition to the F# template, there are additional .NET templates for cloud providers. To list the templates:

```bash
$ pulumi new
```

{{% /lang %}}

{{% lang visualbasic %}}

## Visual Basic

You can write Pulumi programs in Visual Basic to get additional verification and tooling benefits. The easiest way to get started with Pulumi in Visual Basic is to use a template:

```bash
$ mkdir myproject && cd myproject
$ pulumi new visualbasic
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change), a `Infra.vbproj` file that holds references used by the project, and a `Program.vb` file, containing your program. The `.vbproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

In addition to the Visual Basic template, there are additional .NET templates for cloud providers. To list the templates:

```bash
$ pulumi new
```

{{% /lang %}}
