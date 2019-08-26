---
title: Create a New Project
weight: 5
menu:
  getstarted:
    parent: aws
    identifier: aws-create-project

aliases: ["/docs/quickstart/aws/create-project/"]
---

Let's get started with a new project in a new directory.

{{< langchoose nogo >}}

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

> If this is your first time running `pulumi new` or most other `pulumi` commands, you will be prompted to log in to the [Pulumi service](https://app.pulumi.com). The [Pulumi CLI]({{< relref "/docs/reference/cli" >}}) works in tandem with the Pulumi service in order to deliver a reliable experience. It is free for individual use, with [additional features available for teams](https://www.pulumi.com/pricing/). Hitting `ENTER` at the prompt opens up a web browser allowing you to either sign in or sign up.

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

Next, we'll review the generated project files.

{{< get-started-stepper >}}
