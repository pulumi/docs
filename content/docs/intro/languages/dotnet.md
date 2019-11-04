---
title: ".NET"
menu:
  intro:
    parent: languages
    weight: 2

aliases: ["/docs/reference/dotnet/"]
---

{{< langchoose dotnetonly >}}

Pulumi supports programs written in .NET, because programs are just .NET, you may elect to write them in a .NET supported language. That includes C#, F#, or Visual Basic, in addition to your favorite tools such as build systems, linters, or
test frameworks.

## Getting Started

### Prerequisites

1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)
1. [Install .NET Core 3.0+](https://dotnet.microsoft.com/download)

To get started with .NET use a template.  From an empty directory in which you'd like to create a new project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new csharp
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}), a `.csproj` file that holds references used by the project, and an `Program.cs` file, containing your program. The name of the directory is used as the project name in `Pulumi.yaml`.

## C#

You can write Pulumi programs in C# to get additional verification and tooling benefits. As of version 1.5, Pulumi supports .NET natively. The fastest way to get started with Pulumi in C#, is to use a template:

```bash
$ mkdir myproject && cd myproject
$ pulumi new csharp
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}), a `Infra.csproj` file that holds references used by the project, and a `Program.cs` file, containing your program. The `.csproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

### C# Templates

In addition to the `csharp` template, Pulumi provides the following c# templates:

* `aws-csharp`
* `azure-csharp`
* `gcp-csharp`

## F#

You can write Pulumi programs in F# to get additional verification and tooling benefits. As of version 1.5, Pulumi supports .NET natively. The fastest way to get started with Pulumi in f#, is to use a template:

```bash
$ mkdir myproject && cd myproject
$ pulumi new fsharp
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}), a `Infra.fsproj` file that holds references used by the project, and a `Program.fs` file, containing your program. The `.fsproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

### F# Templates

In addition to the `fsharp` template, there is also a `azure-fsharp` template

## Visual Basic

You can write Pulumi programs in C# to get additional verification and tooling benefits. As of version 1.5, Pulumi supports .NET natively. The fastest way to get started with Pulumi in Visual Basic, is to use a template:

```bash
$ mkdir myproject && cd myproject
$ pulumi new visualbasic
```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}), a `Infra.vbproj` file that holds references used by the project, and a `Program.vb` file, containing your program. The `.vbproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

### Visual Basic Templates

In addition to the `visualbasic` template, there is also a `azure-visualbasic` template.