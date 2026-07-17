---
title_tag: Understanding Stack References | Pulumi Tutorials
title: Understanding Stack References
layout: topic
description: Learn how to share outputs across stacks with stack references.
meta_desc: Learn what stack references are, how they differ from stack outputs, and how to share stack outputs from one Pulumi program to another in this tutorial.
weight: 3
estimated_time: 10
aliases:
    - /learn/building-with-pulumi/stack-references/
---

Stack references extend the utility of stack outputs by allowing you to access them programmatically from another Pulumi program at runtime.

In this section, you'll create a new project and stack that'll use the stack outputs from the program we created in the previous topic.

Let's start by making a new program in a new directory, alongside `my-first-app`:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" />}}

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

{{% choosable language go %}}

```bash
$ mkdir ../my-second-app
$ cd ../my-second-app
$ pulumi new go -y
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ mkdir ../my-second-app
$ cd ../my-second-app
$ pulumi new csharp -y
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ mkdir ../my-second-app
$ cd ../my-second-app
$ pulumi new java -y
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ mkdir ../my-second-app
$ cd ../my-second-app
$ pulumi new yaml -y
```

{{% /choosable %}}

{{% choosable language hcl %}}

```bash
$ mkdir ../my-second-app
$ cd ../my-second-app
$ pulumi new hcl -y
```

{{% /choosable %}}

Let's go ahead and create a `staging` stack here as well:

```bash
$ pulumi stack init staging
```

Now comes the fun part! Let's add a little code to pull in the values from the
`my-first-app` stacks, based on the corresponding environment.

Add this code to the {{< langfile >}} file inside of `my-second-app`:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const stack = pulumi.getStack();
const org = config.require("org");

const stackRef = new pulumi.StackReference(`${org}/my-first-app/${stack}`)

export const shopUrl = stackRef.getOutput("url");
```

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

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		org := cfg.Require("org")
		stack := ctx.Stack()

		stackRef, err := pulumi.NewStackReference(ctx,
			fmt.Sprintf("%s/my-first-app/%s", org, stack), nil)
		if err != nil {
			return err
		}

		ctx.Export("shopUrl", stackRef.GetOutput(pulumi.String("url")))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;

return await Deployment.RunAsync(() =>
{
    var config = new Config();
    var org = config.Require("org");
    var stack = Deployment.Instance.StackName;

    var stackRef = new StackReference($"{org}/my-first-app/{stack}");

    return new Dictionary<string, object?>
    {
        ["shopUrl"] = stackRef.GetOutput("url"),
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.resources.StackReference;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var org = ctx.config().require("org");
            var stack = ctx.stackName();

            var stackRef = new StackReference(
                String.format("%s/my-first-app/%s", org, stack));

            ctx.export("shopUrl", stackRef.output("url"));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my-second-app
runtime: yaml

config:
  org:
    type: string

resources:
  stackRef:
    type: pulumi:pulumi:StackReference
    properties:
      name: ${org}/my-first-app/${pulumi.stack}

outputs:
  shopUrl: ${stackRef.outputs["url"]}
```

{{% /choosable %}}

{{% choosable language hcl %}}

```hcl
variable "org" {
  type = string
}

resource "pulumi_stack_reference" "stack_ref" {
  name = "${var.org}/my-first-app/${pulumi.stack}"
}

output "shopUrl" {
  value = pulumi_stack_reference.stack_ref.outputs["url"]
}
```

{{% /choosable %}}

The `org` configuration variable is new, as is the stack reference declaration.
That declaration sets up an instance of the `StackReference` type, which needs
the fully qualified name of the stack as an input. Here, `org` is the
organization associated with your account, `my-first-app` is the name of the
project you've been working in, and the current stack name selects the stack
that you want to reference. If you have an individual account, the org is your
account name. The export then grabs the `url` output from the other stack.

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
