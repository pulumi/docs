---
title: Create a New Project | AWS
h1: Create a New Project
linktitle: Create a New Project
meta_desc: This page provides an overview of how to create a new AWS + Pulumi project.
weight: 5
menu:
  getstarted:
    parent: aws
    identifier: aws-create-project

aliases: ["/docs/quickstart/aws/create-project/"]
---

Let's get started with a new project in a new directory.

{{< langchoose csharp >}}

<div class="language-prologue-javascript"></div>

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-javascript
```

<div class="language-prologue-typescript"></div>

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-typescript
```

<div class="language-prologue-python"></div>

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-python
```

<div class="language-prologue-go"></div>

```bash
# from within your $GOPATH
$ mkdir quickstart && cd quickstart
$ pulumi new aws-go
```

<div class="language-prologue-csharp"></div>

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-csharp
```

{{< cli-note >}}

After logging in, the CLI will proceed with walking you through creating a new project.

```
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart)
project description: (A minimal AWS Pulumi program)
Created project 'quickstart'

stack name: (dev)
Created stack 'dev'

aws:region: The AWS region to deploy into: (us-east-1)
Saved config
```

First, you will be asked for a project name and description. Hit `ENTER` to accept the default values or specify new values.

Next, you will be asked for the name of a stack. You can hit `ENTER` to accept the default value of `dev`.

> What are [projects]({{< relref "/docs/intro/concepts/project" >}}) and [stacks]({{< relref "/docs/intro/concepts/stack" >}})? Pulumi projects and stacks let you organize Pulumi code. Consider a Pulumi _project_ to be analogous to a GitHub repo---a single place for code---and a _stack_ to be an instance of that code with a separate configuration. For instance, _Project Foo_ may have multiple stacks for different development environments (Dev, Test, or Prod), or perhaps for different cloud configurations (geographic region for example). See [Organizing Projects and Stacks]({{< relref "/docs/intro/concepts/organizing-stacks-projects" >}}) for some best practices on organizing your Pulumi projects and stacks.

Next, you will be prompted for some configuration values for the stack.

For AWS projects, you will be prompted for the AWS region. You can accept the default value or choose another value like `us-west-2`.

{{% lang nodejs %}}
After some dependency installations from `npm`, the project and stack will be ready.
{{% /lang %}}

{{% lang python %}}
After the command completes, the project and stack will be ready.
{{% /lang %}}

{{% lang go %}}
After the command completes, the project and stack will be ready.
{{% /lang %}}

{{% lang dotnet %}}
After the command completes, the project and stack will be ready.
{{% /lang %}}

Next, we'll review the generated project files.

{{< get-started-stepper >}}
