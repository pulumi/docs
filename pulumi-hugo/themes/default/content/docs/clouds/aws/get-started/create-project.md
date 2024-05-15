---
title_tag: Create a New Project | AWS
title: Create project
h1: "Pulumi & AWS: Create new project"
meta_desc: This page provides an overview of how to create a new AWS + Pulumi project.
weight: 3
menu:
  clouds:
    parent: aws-get-started
    identifier: aws-get-started-create-project

aliases:
- /docs/quickstart/aws/create-project/
- /docs/get-started/aws/create-project/
---

Now that you have set up your environment by installing Pulumi, installing your preferred language runtime,
and configuring your AWS credentials, let's create your first Pulumi program.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-javascript
```

{{% /choosable %}}
{{% choosable language typescript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-csharp
```

{{% /choosable %}}
{{% choosable language java %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-java
```

{{% /choosable %}}
{{% choosable language yaml %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-yaml
```

{{% /choosable %}}

The [`pulumi new`](/docs/cli/commands/pulumi_new) command creates a new Pulumi project with some basic scaffolding based on the cloud and language specified.

{{< cli-note >}}

After logging in, the CLI will proceed with walking you through creating a new project.

First, you will be asked for a **project name** and **project description**. Hit `ENTER` to accept the default values or specify new values.

```
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart)
project description: (A minimal AWS Pulumi program)
Created project 'quickstart'
```

Next, you will be asked for a **stack name**. Hit `ENTER` to accept the default value of `dev`.

```
Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'
```

Finally, you will be prompted for some configuration values for the stack. For AWS projects, you will be prompted for the AWS region. You can accept the default value or choose another value like `us-west-2`.

```
aws:region: The AWS region to deploy into: (us-west-2)
Saved config
```

> What are [projects](/docs/concepts/projects/) and [stacks](/docs/concepts/stack/)? Pulumi projects and stacks let you organize Pulumi code. Consider a Pulumi _project_ to be analogous to a GitHub repo---a single place for code---and a _stack_ to be an instance of that code with a separate configuration. For instance, project `foo` may have multiple stacks for different deployment environments (`dev`, `test`, or `prod`), or perhaps for different cloud configurations (geographic region for example). See [Organizing Projects and Stacks](/docs/using-pulumi/organizing-projects-stacks/) for some best practices on organizing your Pulumi projects and stacks.

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
