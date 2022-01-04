---
title: "Understanding Stack References"
layout: topic
date: 2021-09-20T08:33:49-05:00
draft: false
description: Learn how to share outputs across stacks with stack references.
meta_desc: Learn how to share outputs across stacks with stack references.
index: 3
estimated_time: 10
meta_image: meta.png
authors:
    - matt-stratton
tags:
    - stacks
    - outputs
block_external_search_index: false
---

We've created some resources. Now, let's see how we can use outputs outside of
Pulumi. In this part, we're going to explore more about stacks, _stack outputs_,
and _stack references_. Stack outputs are, as you might guess, the values
exported from any given stack. These values can also be obtained from the
[Pulumi Console](https://app.pulumi.com), and they're extremely useful when you
want to run commands with the CLI that reference those values. Note, though,
that stack outputs are for the current stack only. If you want to get values
from another stack, you want to use stack references, which bridge different
stacks through inter-stack dependencies.

Stack references allow you to access the outputs of one stack from another
stack. Inter-stack dependencies allow one stack to reference the outputs of
another stack.

For this section, we are going to create a new Pulumi program that will bring in
the stack outputs from the program we just created.

Let's start by making our new Pulumi program in a new directory:

{{< chooser language "python" / >}}

<!--{{% choosable language typescript %}}

```bash
mkdir my-second-app
cd my-second-app
$ pulumi new typescript -y
```

{{% /choosable %}}-->

{{% choosable language python %}}

```bash
mkdir my-second-app
cd my-second-app
$ pulumi new python -y
```

{{% /choosable %}}

<!--{{% choosable language go %}}

```bash
mkdir my-second-app
cd my-second-app
$ pulumi new go -y
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
mkdir my-second-app
cd my-second-app
$ pulumi new csharp -y
```

{{% /choosable %}}-->

Let's go ahead and create a `staging` stack here as well:

```bash
$ pulumi stack init staging
```

Now comes the fun part! Let's add a little code to pull in the values from the
`my-first-app` stacks, based on the corresponding environment.

Add this code to the {{< langfile >}} file inside of `my-second-app`.

{{< chooser language "python" / >}}

<!-- {{% choosable language typescript %}}

```typescript
const env = pulumi.getStack();
const myFirstApp = new pulumi.StackReference(`YOURNAME/my-first-app/${env}`);
export let shopUrl =  myFirstApp.getOutput("url");
```

{{% /choosable %}} -->

{{% choosable language python %}}

```python
import pulumi

config = pulumi.Config()
stack = pulumi.get_stack()
org = config.require("org")

stack_ref = pulumi.StackReference(f"{org}/my-first-app/{stack}")

pulumi.export("shopUrl", stack_ref.get_output("url"))
```

{{% /choosable %}}

<!-- {{% choosable language go %}}

```go
import (
  "fmt"

  "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
  pulumi.Run(func(ctx *pulumi.Context) error {
    slug := fmt.Sprintf("YOURNAME/my-first-app/%v", ctx.Stack())
    stackRef, err := pulumi.NewStackReference(ctx, slug, nil)

    ctx.Export("shopUrl", stackRef.GetOutput(pulumi.String("url")))

    return nil
  }
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
class AppStack : Stack
{
    public AppStack()
    {
        var MyFirstApp = new StackReference($"YOURNAME/my-first-app/{Deployment.Instance.StackName}");
        var name = MyFirstApp.RequireOutput("url").Apply(v => v.ToString());
        this.name = Output.Create(shopUrl);
    }
}
```

{{% /choosable %}} -->

The `org` environment variable is new, as is the `stack_ref` declaration. That
declaration sets up an instance of the `StackReference` class, which needs the
fully qualified name of the stack as an input. Here, the `org` is the
organization associated with your account, the `my-first-app` is the name of the
project you've been working in, and the stack is the stack that you want to
reference. If you have an individual account, the org is your account name. The
export then grabs the `url` output from the other stack.

Set the `org` environment variable, which is the organization associated with
your account, and change the `<YOURNAME>` to your username/account name for
Pulumi:

```bash
pulumi config set org <YOURNAME>
```

Run `pulumi up`. You'll see the value gets exported from the other project's
stack to reference in this new project's stack:

```bash

     Type                 Name               Status
     pulumi:pulumi:Stack  my-second-app-staging

Outputs:
  + shopUrl: "http://localhost:3002"
```

These exported values are incredibly useful when using Pulumi stacks. For
example, let's say you have two systems that depend on one another, perhaps a
frontend application with a database and a complex backend API. You might have
two separate staging environments that you want to have reference one another.
You can use stack references to share automatically generated connection strings
from the staged API to the staged frontend application to see how they might
work together.

Next up, we're going to change gears and start exploring how Pulumi handles
secrets.

<!-- [^1]: [stack output]({{< relref "docs/reference/glossary#stack-output" >}}) -->
<!-- [^2]: [stack reference]({{< relref "docs/reference/glossary#stack-reference" >}}) -->
