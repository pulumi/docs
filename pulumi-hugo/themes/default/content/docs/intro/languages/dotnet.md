---
title: ".NET"
menu:
  intro:
    parent: languages
    weight: 2

aliases: ["/dotnet/"]
---

Pulumi supports .NET programs running on .NET Core 3 and later. You can also use your favorite .NET tools such as editors, package managers, build systems, and test frameworks to deploy infrastructure on Azure, AWS and GCP. 

Pulumi packages are available on [Nuget for download](https://www.nuget.org/packages?q=pulumi). Use [Visual Studio Code](https://code.visualstudio.com/download) or [Visual Studio](https://visualstudio.microsoft.com/downloads/) to get full tooling support for .NET, including auto-completion, red error markers and build errors.

![VSCode](/images/docs/quickstart/vscode-dotnet.png)

___
**NOTE**

> Pulumi .NET support is in preview and is under active development.
___

## Prerequisites

1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)
1. [Install .NET Core SDK 3.0](https://dotnet.microsoft.com/download)

## Example .NET Project

As of version 1.5, Pulumi supports .NET natively. You can write Pulumi programs in C# to get additional verification and tooling benefits. The fastest way to get started with Pulumi in C# is to use a template. The template will autogenerate a set of files and initialize a Pulumi project.

You can get started with .NET using a Pulumi template. From an empty directory, create a new C# project:

   ```bash
  $ mkdir myproject && cd myproject
  $ pulumi new csharp
  ```

This will create a `Pulumi.yaml` [project file]({{< relref "project.md" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change), a `Infra.csproj` file that holds references used by the project, and a `Program.cs` file, containing your program. The `.csproj` file can be named more appropriately depending upon the project. The name of the directory is used as the project name in `Pulumi.yaml`.

To deploy your infrastructure run `pulumi up` and the Pulumi engine automatically runs `dotnet build` as part of the deployment. Pulumi will perform the CRUD operations needed to deploy the infrastructure you have declared.

## F\#

You can write Pulumi programs in F#. To start a Pulumi project in F# use a template:

  ```bash
  $ mkdir myproject && cd myproject
  $ pulumi new fsharp
  ```

## Visual Basic

You can write Pulumi programs in Visual Basic. To start a Pulumi project in Visual Basic is to use a template:

  ```bash
  $ mkdir myproject && cd myproject
  $ pulumi new visualbasic
  ```

## Templates

In addition to the C#, F#, and Visual Basic templates, there are additional .NET templates for cloud providers. To list the templates:

  ```bash
  $ pulumi new
  ```
