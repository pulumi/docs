---
title: "Introducing Resource Transforms: Enhancing Flexibility for Packaged Component
  Resources"
allow_long_title: true
date: 2024-07-19
meta_desc: Announcing a new Transform system with support for transforming child resources
  of packaged components.
meta_image: meta.png
authors:
  - fraser-waters
  - justin-vanpatten
tags:
  - features
search:
  keywords:
    - Transforms
    - Resources
    - Resource Transforms
    - Packaged Components
    - Component Resources
---

Pulumi has supported a [Transformations](/docs/concepts/options/transformations) system for a number of years now. This has proved to be a powerful and flexible escape hatch for modifying resource properties and options across your entire program. For example, you could use Transformations to [automatically apply tags](/blog/automatically-enforcing-aws-resource-tagging-policies/#automatically-applying-tags) to all taggable resources in your program, including the children of component resources.

However, there is one major limitation with the existing Transformations system: it isn't able to transform the children of _packaged_ component resources, such as those in [awsx](/registry/packages/awsx) and [eks](/registry/packages/eks). This limitation is due to the fact that _packaged_ component resources are created in a separate provider process and Transformations only work with resources created in your program's process.

To address this limitation we're introducing a new system called [Transforms](/docs/concepts/options/transforms), which works with all resources, including packaged component resources and their children. The new Transforms system is intended to fully replace the old Transformations system (we plan to deprecate the old system in the future).

<!--more-->

Here's an example that demonstrates adding tags to all `Subnet` child resources created by the `Vpc` packaged component:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";

const myTags = { test: "TEST" };

pulumi.runtime.registerResourceTransform(args => {
    if (args.type === "aws:ec2/subnet:Subnet") {
        const tags = pulumi.output(args.props.tags || {});
        args.props.tags = tags.apply(t => ({ ...t, ...myTags }));
        return { props: args.props, opts: args.opts };
    }
    return undefined;
});

const vpc = new awsx.ec2.Vpc("test");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_awsx import ec2

my_tags = { "test": "TEST" }

def tag_transform(args):
    if args.type_ == "aws:ec2/subnet:Subnet":
        tags = pulumi.Output.from_input(args.props.get("tags", {}))
        args.props["tags"] = tags.apply(lambda v: {**v, **my_tags})
        return pulumi.ResourceTransformResult(args.props, args.opts)

pulumi.runtime.register_resource_transform(tag_transform)

my_vpc = ec2.Vpc("my-vpc")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "context"

    "github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        myTags := map[string]string{"test": "TEST"}

        err := ctx.RegisterResourceTransform(func(_ context.Context, args *pulumi.ResourceTransformArgs) *pulumi.ResourceTransformResult {
            if args.Type == "aws:ec2/subnet:Subnet" {
                tags, ok := args.Props["tags"].(pulumi.StringMapInput)
                if !ok {
                    tags = pulumi.StringMap{}
                }
                args.Props["tags"] = tags.ToStringMapOutput().ApplyT(func(m map[string]string) map[string]string {
                    result := make(map[string]string)
                    for k, v := range m {
                        result[k] = v
                    }
                    for k, v := range myTags {
                        result[k] = v
                    }
                    return result
                })
                return &pulumi.ResourceTransformResult{
                    Props: args.Props,
                    Opts:  args.Opts,
                }
            }
            return nil
        })
        if err != nil {
            return err
        }

        _, err = ec2.NewVpc(ctx, "test", nil)
        if err != nil {
            return err
        }

        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System;
using System.Collections.Immutable;
using Pulumi;
using Pulumi.Awsx.Ec2;

await Deployment.RunAsync<MyStack>();

class MyStack : Stack
{
    public MyStack() : base(new StackOptions
    {
        ResourceTransforms =
        {
            async (args, _) => {
                var myTags = ImmutableDictionary.Create<string, object>()
                    .Add("test", "Test");

                if (args.Type == "aws:ec2/subnet:Subnet")
                {
                    InputMap<object> tags =
                        args.Args.TryGetValue("tags", out var tagsValue) && tagsValue is not null ?
                            tagsValue is Output<ImmutableDictionary<string, object>> tagsOutput ? tagsOutput :
                            tagsValue is ImmutableDictionary<string, object> tagsDictionary ? tagsDictionary :
                            throw new InvalidOperationException($"Unexpected tags type: {tagsValue.GetType()}") :
                        ImmutableDictionary<string, object>.Empty;

                    tags = tags.Apply(t => t.SetItems(myTags));
                    return new(args.Args.SetItem("tags", tags), args.Options);
                }
                return null;
            },
        }
    })
    {
        var vpc = new Vpc("test");
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Using the new Transforms system is similar to the old system, but there are some differences between the two systems. A guide on [Migrating from Transformations to Transforms](/docs/concepts/options/transformations/#migrating-from-transformations-to-transforms) is available to help transition to the new system.

We're excited to make it possible to transform all resources in your program, including those from packaged components. If you have any questions or feedback, please don't hesitate to reach out to us on [Slack](https://slack.pulumi.com/).
