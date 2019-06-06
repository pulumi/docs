---
title: Creating a project
aliases:
    - basics-projects.html
    - /tour/basics-templates.html
menu:
  tour:
    parent: tour
    weight: 2
---

To get started with Pulumi, you'll need a project.

A project is defined by a directory that contains a `Pulumi.yaml` [project file]({{< relref "/reference/project.md" >}}).  This file
simply defines minimal metadata about your program so that Pulumi knows what to do with it.

Use [`pulumi new <template-name>`]({{< relref "/reference/cli/pulumi_new.md" >}}) to quickly scaffold a new project from scratch:

{{< langchoose >}}

<div class="language-prologue-javascript"></div>

```bash
$ mkdir ahoy-pulumi && cd ahoy-pulumi
$ pulumi new aws-javascript
This command will walk you through creating a new Pulumi project.
Enter a value or leave blank to accept the default, and press <ENTER>.
Press ^C at any time to quit.

project name: (ahoy-pulumi)
project description: Ahoy, Pulumi!
stack name: (ahoy-pulumi-dev)
aws:region: (us-east-1)

New project is configured and ready to deploy with 'pulumi up'.
```

<div class="language-prologue-typescript"></div>

```bash
$ mkdir ahoy-pulumi && cd ahoy-pulumi
$ pulumi new aws-typescript
This command will walk you through creating a new Pulumi project.
Enter a value or leave blank to accept the default, and press <ENTER>.
Press ^C at any time to quit.

project name: (ahoy-pulumi)
project description: Ahoy, Pulumi!
stack name: (ahoy-pulumi-dev)
aws:region: (us-east-1)

New project is configured and ready to deploy with 'pulumi up'.
```

<div class="language-prologue-python"></div>

```bash
$ mkdir ahoy-pulumi && cd ahoy-pulumi
$ pulumi new aws-python
This command will walk you through creating a new Pulumi project.
Enter a value or leave blank to accept the default, and press <ENTER>.
Press ^C at any time to quit.

project name: (ahoy-pulumi)
project description: Ahoy, Pulumi!
stack name: (ahoy-pulumi-dev)
aws:region: (us-east-1)

New project is configured and ready to deploy with 'pulumi up'.
```

<div class="language-prologue-go"></div>

```bash
$ mkdir ahoy-pulumi && cd ahoy-pulumi
$ pulumi new aws-go
This command will walk you through creating a new Pulumi project.
Enter a value or leave blank to accept the default, and press <ENTER>.
Press ^C at any time to quit.

project name: (ahoy-pulumi)
project description: Ahoy, Pulumi!
stack name: (ahoy-pulumi-dev)
aws:region: (us-east-1)

New project is configured and ready to deploy with 'pulumi up'.
```

This single command created a project, program, stack, and even configured it.

Many interesting templates are available.  Run `pulumi new` without any arguments to see a list.  Templates are defined
in [our pulumi/templates GitHub repo](https://github.com/pulumi/templates), and PRs are welcome if you find anything
missing!

***

Next up, let's learn how to deploy our program to the cloud.

<div class="tour-nav">
    <a class="tour-button enabled" href="{{< relref "basics-programs.md" >}}" title="Programs">◀</a>
    <span class="tour-index"><strong>3</strong>/8</span>
    <a class="tour-button enabled" href="{{< relref "basics-deploying.md" >}}" title="Deploying code">▶</a>
</div>
