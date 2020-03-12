---
title: Create a New Project | GCP
h1: Create a New Project
linktitle: Create a New Project
meta_desc: This page provides an overview of how to create a new Google Cloud (GCP) + Pulumi project.
weight: 5
menu:
  getstarted:
    parent: gcp
    identifier: gcp-create-project

aliases: ["/docs/quickstart/gcp/create-project/"]
---

Let's get started with a new project in a new directory.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new gcp-javascript
```

{{% /choosable %}}
{{% choosable language typescript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new gcp-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new gcp-python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
# install the pulumi gcp plugin
# check for the release version here https://github.com/pulumi/pulumi-gcp/releases
$ pulumi plugin install resource gcp 2.6.0
# from within your $GOPATH
$ mkdir quickstart && cd quickstart
$ pulumi new gcp-go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new gcp-csharp
```

{{% /choosable %}}

{{< cli-note >}}

After logging in, the CLI will proceed with walking you through creating a new project.

```
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart)
project description: (A minimal Google Cloud Pulumi program)
Created project 'quickstart'

stack name: (dev)
Created stack 'dev'

gcp:project: The Google Cloud project to deploy into:
Saved config
```

First, you will be asked for a project name and description. Hit `ENTER` to accept the default values or specify new values.

Next, you will be asked for the name of a stack. You can hit `ENTER` to accept the default value of `dev`.

> What are [projects]({{< relref "/docs/intro/concepts/project" >}}) and [stacks]({{< relref "/docs/intro/concepts/stack" >}})? Pulumi projects and stacks let you organize Pulumi code. Consider a Pulumi _project_ to be analogous to a GitHub repo---a single place for code---and a _stack_ to be an instance of that code with a separate configuration. For instance, _Project Foo_ may have multiple stacks for different development environments (Dev, Test, or Prod), or perhaps for different cloud configurations (geographic region for example). See [Organizing Projects and Stacks]({{< relref "/docs/intro/concepts/organizing-stacks-projects" >}}) for some best practices on organizing your Pulumi projects and stacks.

After logging in, the CLI will proceed with walking you through creating a new project.

Next, you will be prompted for some configuration values for the stack.

For GCP projects you will be prompted for the Google Cloud project to deploy into.

{{% choosable language "javascript,typescript" %}}
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
