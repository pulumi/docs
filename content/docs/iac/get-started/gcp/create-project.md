---
title_tag: Create a New Project | Google Cloud
title: Create project
h1: "Get started with Pulumi and Google Cloud"
meta_desc: This page provides an overview of how to create a new Google Cloud + Pulumi project.
weight: 3
menu:
    iac:
        name: Create project
        identifier: gcp-get-started.create-project
        parent: gcp-get-started
        weight: 3

aliases:
    - /docs/quickstart/gcp/create-project/
    - /docs/clouds/gcp/get-started/create-project/
---

## Create a new project

A [**project**](/docs/iac/concepts/projects) is a program in your chosen language that defines a collection of related
cloud resources. In this step, you will create a new project.

### Initializing your project

Each project lives in its own directory. Create a new one:

{{% choosable os "linux,macos" %}}

```bash
$ mkdir pulumi-start-gcp
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> mkdir pulumi-start-gcp
```

{{% /choosable %}}

Change into the new directory:

{{% choosable os "linux,macos" %}}

```bash
$ cd pulumi-start-gcp
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> cd pulumi-start-gcp
```

{{% /choosable %}}

Now initialize a new Pulumi project for Google Cloud using the `pulumi new` command:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-typescript
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-typescript
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language python %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-python
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-python
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language go %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-go
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-go
```

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language csharp %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-csharp
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-csharp
```

{{% /choosable %}}

{{% /choosable %}}

{{% choosable language java %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-java
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-java
```

{{% /choosable %}}

{{% /choosable %}}

{{% choosable language yaml %}}

{{% choosable os "linux,macos" %}}

```bash
$ pulumi new gcp-yaml
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi new gcp-yaml
```

{{% /choosable %}}

{{% /choosable %}}

The [`pulumi new`](/docs/cli/commands/pulumi_new) command interactively walks through initializing a new project, as well as creating a
[**stack**](/docs/iac/concepts/stacks) and [**configuring**](/docs/iac/concepts/config) it. A stack is an instance of your
project and you may have many of them -- like `dev`, `staging`, and `prod` -- each with different configuration settings.

You will be prompted for configuration values such as the Google Cloud project. Enter the project ID for the project you
set with the gcloud CLI or hit ENTER to accept any defaults:

```
gcp:project: The Google Cloud project to deploy into: my-project
Saved config
```

{{< cli-note >}}

{{< cli-note >}}

After logging in, the CLI will proceed with walking you through creating a new project.

First, you will be asked for a **project name** and **project description**. Hit `ENTER` to accept the default values or specify new values.

```
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart)
project description: (A minimal Google Cloud Pulumi program)
Created project 'quickstart'
```

Next, you will be asked for a **stack name**. Hit `ENTER` to accept the default value of `dev`.

```
Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'
```

Finally, you will be prompted for some configuration values for the stack. For Google Cloud projects, you will be prompted for the Google Cloud project. Enter your Google Cloud project ID at this prompt.

```
gcp:project: The Google Cloud project to deploy into: my-project
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

{{< get-started-stepper >}}
