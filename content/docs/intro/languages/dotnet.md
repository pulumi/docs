---
title: ".NET"
menu:
  intro:
    parent: languages
    weight: 2

aliases: ["/docs/reference/dotnet/"]
---

Pulumi supports .NET programs running on .NET Core 3 and later. You can also use your favorite .NET tools such as editors, package managers, build systems, and test frameworks.

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

You can write Pulumi programs in C# to get additional verification and tooling benefits. As of version 1.5, Pulumi supports .NET natively. The fastest way to get started with Pulumi in C#, is to use a template. The template will autogenerate a set of files that make up a Pulumi project.

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change), a `Infra.csproj` file that holds references used by the project, and a `Program.cs` file, containing your program. The `.csproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.



## F\#

You can write Pulumi programs in F# to get additional verification and tooling benefits. The fastest way to get started with Pulumi in F# is to use a template:

  ```bash
  $ mkdir myproject && cd myproject
  $ pulumi new fsharp
  ```

## Visual Basic

You can write Pulumi programs in Visual Basic to get additional verification and tooling benefits. The easiest way to get started with Pulumi in Visual Basic is to use a template:

  ```bash
  $ mkdir myproject && cd myproject
  $ pulumi new visualbasic
  ```

## Templates

In addition to the C#, F#, and Visual Basic templates, there are additional .NET templates for cloud providers. To list the templates:

  ```bash
  $ pulumi new
  ```
