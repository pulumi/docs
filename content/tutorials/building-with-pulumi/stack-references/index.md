---
title_tag: Understanding Stack References | Learn Pulumi
title: "Understanding Stack References"
layout: topic
date: 2021-09-20T08:33:49-05:00
draft: false
description: Learn how to share outputs across stacks with stack references.
meta_desc: Learn what stack references are, how they differ from stack outputs, and how to share stack outputs from one Pulumi program to another in this tutorial.
index: 3
estimated_time: 10
meta_image: meta.png
aliases:
    - /learn/building-with-pulumi/stack-references/
---

Stack references extend the utility of stack outputs by allowing you to access them programmatically from another Pulumi program at runtime.

In this section, you'll create a new project and stack that'll use the stack outputs from the program we created in the previous topic.

Let's start by making a new program in a new directory, alongside `my-first-app`:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```bash
$ mkdir ../my-second-app
$ cd ../my-second-app
$ pulumi new typescript -y
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ mkdir ../my-second-app
$ cd ../my-second-app
$ pulumi new python -y
```

{{% /choosable %}}

Let's go ahead and create a `staging` stack here as well:

```bash
$ pulumi stack init staging
```

Now comes the fun part! Let's add a little code to pull in the values from the
`my-first-app` stacks, based on the corresponding environment.

Add this code to the {{< langfile >}} file inside of `my-second-app`:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const stack = pulumi.getStack();
const org = config.require("org");

const stackRef = new pulumi.StackReference(`${org}/my-first-app/${stack}`)

export const shopUrl = stackRef.getOutput("url");
```

The `org` configuration variable is new, as is the `stackRef` declaration. That
declaration sets up an instance of the `StackReference` class, which needs the
fully qualified name of the stack as an input. Here, `org` is the
organization associated with your account, `my-first-app` is the name of the
project you've been working in, and `stack` is the stack that you want to
reference. If you have an individual account, the org is your account name. The
export then grabs the `url` output from the other stack.

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

config = pulumi.Config()
stack = pulumi.get_stack()
org = config.require("org")

stack_ref = pulumi.StackReference(f"{org}/my-first-app/{stack}")

pulumi.export("shopUrl", stack_ref.get_output("url"))
```

The `org` configuration variable is new, as is the `stack_ref` declaration. That
declaration sets up an instance of the `StackReference` class, which needs the
fully qualified name of the stack as an input. Here, `org` is the
organization associated with your account, `my-first-app` is the name of the
project you've been working in, and `stack` is the stack that you want to
reference. If you have an individual account, the org is your account name. The
export then grabs the `url` output from the other stack.

{{% /choosable %}}

Set the `org` configuration variable using `pulumi config set`:

```bash
pulumi config set org <YOURNAME>
```

Run `pulumi up`. You'll see the value gets exported from the other project's
stack to reference in this new project's stack:

```bash
$ pulumi up
...

Updating (staging)
...

     Type                 Name                   Status
 +   pulumi:pulumi:Stack  my-second-app-staging  created (1s)

Outputs:
    shopUrl: "http://localhost:3002"

Resources:
    + 1 created

Duration: 3s
```

These exported values are incredibly useful when using Pulumi stacks. For example, let's say you have two systems that depend on one another, perhaps a frontend application with a database and a complex backend API. You might have two separate staging environments that you want to have reference one another. You can use stack references to share automatically generated connection strings from the staging API to the staging frontend application to see how they might work together.

Next up, we're going to change gears and start exploring how Pulumi handles secrets.

{{< tutorials/stepper >}}
