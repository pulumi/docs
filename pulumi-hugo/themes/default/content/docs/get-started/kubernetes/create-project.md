---
title: Create a New Project | Kubernetes
h1: Create a New Project
linktitle: Create a New Project
meta_desc: This page provides an overview of how to create a new Kubernetes + Pulumi project.
weight: 3
menu:
  getstarted:
    parent: kubernetes
    identifier: kubernetes-create-project

aliases: ["/docs/quickstart/kubernetes/create-project/"]
---
Now that you have set up your environment let's create your first Pulumi program.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-javascript
```

{{% /choosable %}}
{{% choosable language typescript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-csharp
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-java
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-yaml
```

{{% /choosable %}}

{{< cli-note >}}

After logging in, the CLI will proceed with walking you through creating a new project.

First, you will be asked for a **project name** and **project description**. Hit `ENTER` to accept the default values or specify new values.

```
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart)
project description: (A minimal Kubernetes Pulumi program)
Created project 'quickstart'
```

Next, you will be asked for a **stack name**. You can hit `ENTER` to accept the default value of `dev`.

```
Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'
```

> What are [projects](/docs/intro/concepts/project/) and [stacks](/docs/intro/concepts/stack/)? Pulumi projects and stacks let you organize Pulumi code. Consider a Pulumi _project_ to be analogous to a GitHub repo---a single place for code---and a _stack_ to be an instance of that code with a separate configuration. For instance, _Project Foo_ may have multiple stacks for different development environments (Dev, Test, or Prod), or perhaps for different cloud configurations (geographic region for example). See [Organizing Projects and Stacks](/docs/guides/organizing-projects-stacks/) for some best practices on organizing your Pulumi projects and stacks.

{{% choosable language "javascript,typescript" %}}

After some dependency installations from `npm`, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language python %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language go %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{% choosable language csharp %}}

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
