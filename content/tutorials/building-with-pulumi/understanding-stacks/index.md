---
title_tag: Understanding Stacks | Pulumi Tutorials
title: Understanding Stacks
layout: topic
description: Learn a bit more about stacks as part of using Pulumi.
meta_desc: Learn what a stack is, how stacks work within Pulumi, and how to create, list, and select stacks in this tutorial.
meta_image: meta.png
weight: 1
estimated_time: 10
aliases:
    - /learn/building-with-pulumi/understanding-stacks/
---

Every Pulumi program is deployed to a stack. A stack is an isolated, independently [configurable](/docs/concepts/config/) instance of a Pulumi program. Stacks are commonly used to denote different phases of development (such as `development`, `staging`, and `production`) or feature branches (such as `feature-x-dev`).

A project can have as many stacks as you need. By default, as you've seen in previous tutorials, Pulumi creates one for you when you create a new project with `pulumi new`.

## Create a stack

To create a new stack, we use the command `pulumi stack init <stack-name>`. This command creates an empty stack and sets it as the _active_ stack. The project that the stack is associated with is determined by the nearest `Pulumi.yaml` file.

The stack name must be unique within a project. Stack names may only contain alphanumeric characters, hyphens, underscores, or periods.

Let's create a new stack in the `my-first-app` project and call it `staging`:

```bash
$ pulumi stack init staging
```

## Listing stacks

We have a couple of stacks in our project now --- but how do we know which
ones we have? If we run the command `pulumi stack ls`, it will tell us!

```bash
$ pulumi stack ls
NAME      LAST UPDATE    RESOURCE COUNT  URL
dev       2 minutes ago  0               https://app.pulumi.com/***/my-first-app/dev
staging*  n/a            n/a             https://app.pulumi.com/***/my-first-app/staging
```

Notice that the `staging` stack has an `*` after its name; this asterisk marks
this stack as the active stack (i.e., the stack that all our commands will run
on).

## Selecting stacks

When we run a Pulumi command (such as `config`, `up`, or `destroy`), the command
operates on the *active* stack. But what if we want to change which stack is
active? For this task, we use the `pulumi stack select` command:

```bash
$ pulumi stack select dev
$ pulumi stack ls

NAME     LAST UPDATE    RESOURCE COUNT  URL
dev*     3 minutes ago  0               https://app.pulumi.com/***/my-first-app/dev
staging  n/a            n/a             https://app.pulumi.com/***/my-first-app/staging

```

Notice that `dev` is now the active stack.

Also note that the stack has a resource count of zero, courtesy of the `pulumi destroy` we ran at the end of the Fundamentals tutorial. If your resource count is something other than zero, be sure to run `pulumi destroy` before moving on.

Next up, we're going to explore how to get information out of a stack to use in
other places, like elsewhere in our program or in general spots like your
browser.

{{< tutorials/stepper >}}
