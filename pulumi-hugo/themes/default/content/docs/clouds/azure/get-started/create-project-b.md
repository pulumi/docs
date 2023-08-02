---
title_tag: Create a New Project | Azure
meta_desc: This page provides an overview of how to create a new Azure + Pulumi project.
title: Create project
h1: "Pulumi & Azure: Create project"
block_external_search_index: true
---

Now that you have set up your environment by installing Pulumi and installed your preferred language runtime, let's create your first Pulumi program.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new azure-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new azure-python
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new azure-csharp
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new azure-go
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new azure-java
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new azure-yaml
```

{{% /choosable %}}

The [`pulumi new`](/docs/cli/commands/pulumi_new) command creates a new Pulumi project with some basic scaffolding based on the cloud and language specified.

First, you will be asked for a **project name** and **project description**. Hit `ENTER` to accept the default values or specify new values.

```
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart)
project description: (A minimal Azure Native Pulumi program)
Created project 'quickstart'
```

Next, you will be asked for a **stack name**. Hit `ENTER` to accept the default value of `dev`.

```
Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'
```

For Azure projects, you will be prompted for the Azure location. You can accept the default value of `WestUS` or choose another location.

```
azure-native:location: The Azure location to use: (WestUS2)
Saved config
```

> What are [projects](/docs/concepts/projects/) and [stacks](/docs/concepts/stack/)? Pulumi projects and stacks let you organize Pulumi code. Consider a Pulumi _project_ to be analogous to a GitHub repo---a single place for code---and a _stack_ to be an instance of that code with a separate configuration. For instance, _Project Foo_ may have multiple stacks for different development environments (Dev, Test, or Prod), or perhaps for different cloud configurations (geographic region for example). See [Organizing Projects and Stacks](/docs/using-pulumi/organizing-projects-stacks/) for some best practices on organizing your Pulumi projects and stacks.

{{% choosable language "typescript" %}}

After some dependency installations from `npm`, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language python %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language go %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language java %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language yaml %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

Next, we'll review the generated project files.

<div class="mt-6">
    <a data-track="previous-step" class="btn btn-secondary" href="/docs/get-started/b/">&larr; Previous Step</a>
    <a data-track="next-step" class="btn" href="/docs/clouds/azure/get-started/review-project-b/">Review Project &rarr;</a>
</div>
