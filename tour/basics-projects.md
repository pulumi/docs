---
title: Creating a project
redirect_from: "/tour/basics-templates.html"
---

To get started with Pulumi, you'll need a project.

A project is defined by a directory that contains a `Pulumi.yaml` [project file](../reference/project.html).  This file
simply defines minimal metadata about your program so that Pulumi knows what to do with it.

Use [`pulumi new <template-name>`](/reference/cli/pulumi_new.html) to quickly scaffold a new project from scratch:

{% include langchoose.html %}

<div class="language-prologue-javascript"></div>
```bash
$ pulumi new aws-javascript --dir ahoy-pulumi
This command will walk you through creating a new Pulumi project.
Enter a value or leave blank to accept the default, and press <ENTER>.
Press ^C at any time to quit.

project name: (ahoy-pulumi)
project description: Ahoy, Pulumi!
stack name: (ahoy-pulumi-dev)
aws:region: (us-east-1)

New project is configured and ready to deploy with 'pulumi update'.
```

<div class="language-prologue-typescript"></div>
```bash
$ pulumi new aws-typescript --dir ahoy-pulumi
This command will walk you through creating a new Pulumi project.
Enter a value or leave blank to accept the default, and press <ENTER>.
Press ^C at any time to quit.

project name: (ahoy-pulumi)
project description: Ahoy, Pulumi!
stack name: (ahoy-pulumi-dev)
aws:region: (us-east-1)

New project is configured and ready to deploy with 'pulumi update'.
```

<div class="language-prologue-python"></div>
```bash
$ pulumi new aws-python --dir ahoy-pulumi
This command will walk you through creating a new Pulumi project.
Enter a value or leave blank to accept the default, and press <ENTER>.
Press ^C at any time to quit.

project name: (ahoy-pulumi)
project description: Ahoy, Pulumi!
stack name: (ahoy-pulumi-dev)
aws:region: (us-east-1)

New project is configured and ready to deploy with 'pulumi update'.
```

<div class="language-prologue-go"></div>
```bash
$ pulumi new aws-go --dir ahoy-pulumi
This command will walk you through creating a new Pulumi project.
Enter a value or leave blank to accept the default, and press <ENTER>.
Press ^C at any time to quit.

project name: (ahoy-pulumi)
project description: Ahoy, Pulumi!
stack name: (ahoy-pulumi-dev)
aws:region: (us-east-1)

New project is configured and ready to deploy with 'pulumi update'.
```

This single command created a project, program, stack, and even configured it.

Many interesting templates are available.  Run `pulumi new` without any arguments to see a list.  Templates are defined
in [our pulumi/templates GitHub repo](https://github.com/pulumi/templates), and PRs are welcome if you find anything
missing!

***

Next up, let's learn how to deploy our program to the cloud.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-programs.html" title="Programs">◀</a>
    <span class="tour-index"><strong>3</strong>/8</span>
    <a class="tour-button enabled" href="basics-deploying.html" title="Deploying code">▶</a>
</div>
