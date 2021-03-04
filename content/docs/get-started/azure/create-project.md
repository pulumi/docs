---
title: Create a New Project | Azure
h1: Create a New Project
linktitle: Create a New Project
meta_desc: This page provides an overview of how to create a new Azure + Pulumi project.
weight: 3
menu:
  getstarted:
    parent: azure
    identifier: azure-create-project

aliases: ["/docs/quickstart/azure/create-project/"]
---

Now that you have set up your environment by installing Pulumi, installing your preferred language runtime, and configuring your AWS credentials, let's get started with creating your first Pulumi program.

In this guide you will:

- Create a new Pulumi project.
- Provision a new Blob storage container.
- Add an `index.html` file to your container.
- Serve the `index.html` as a static website.
- Destroy the resources you've provisioned.

To get started, first create a new directory and project.

{{< chooser language "typescript,python,go,csharp" / >}}

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
# from within your $GOPATH
$ mkdir quickstart && cd quickstart
$ pulumi new azure-go
```

{{% /choosable %}}

The [`pulumi new`]({{< relref "/docs/reference/cli/pulumi_new" >}}) command creates a new Pulumi project with some basic scaffolding based on the cloud and language specified.

{{< cli-note >}}

After logging in, the CLI will proceed with walking you through creating a new project.

First, you will be asked for a project name and description. Hit `ENTER` to accept the default values or specify new values.

Next, you will be asked for the name of a stack. Hit `ENTER` to accept the default value of `dev`.

For Azure projects, the default region is `WestUS`; however, you can change the region for your stack by using the `pulumi config set` command as shown below:

```bash
pulumi config set azure-native:location EastUS
```

> What are [projects]({{< relref "/docs/intro/concepts/project" >}}) and [stacks]({{< relref "/docs/intro/concepts/stack" >}})? Pulumi projects and stacks let you organize Pulumi code. Consider a Pulumi _project_ to be analogous to a GitHub repo---a single place for code---and a _stack_ to be an instance of that code with a separate configuration. For instance, _Project Foo_ may have multiple stacks for different development environments (Dev, Test, or Prod), or perhaps for different cloud configurations (geographic region for example). See [Organizing Projects and Stacks]({{< relref "/docs/guides/organizing-projects-stacks" >}}) for some best practices on organizing your Pulumi projects and stacks.

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

Next, we'll review the generated project files.

{{< get-started-stepper >}}
