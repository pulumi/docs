---
title_tag: "transforms | Resource Options"
meta_desc: The transforms resource option provides a list of transforms to apply to a resource and all its children.
title: "transforms"
h1: "Resource option: transforms"
menu:
  iac:
    identifier: transforms
    parent: options-concepts
    weight: 210
aliases:
  - /docs/intro/concepts/resources/options/transforms/
  - /docs/concepts/options/transforms/
  - /docs/iac/concepts/options/transforms/
---

The `transforms` resource option provides a list of transforms to apply to a resource and all its children. Use this option to override or modify the inputs to the child resources of a component resource. One example is to use the option to add other resource options (such as `ignoreChanges` or `protect`). Another example is to modify an input property (such as adding to tags or changing a property that is not directly configurable).

Each transform is a callback that the Pulumi engine invokes. It receives the resource type, name, input properties, and resource options. The callback returns a new set of resource input properties and resource options that will be used to construct the resource instead of the original values.

{{< resource-option-scope "transforms" >}}

## VPC example

This example looks for all VPC and Subnet resources in a component's child hierarchy and adds an option to ignore any changes to their `tags` property (for example, because you manage all VPC and Subnet tags outside of Pulumi):

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const vpc = new MyVpcComponent("vpc", {}, {
    transforms: [args => {
        if (args.type === "aws:ec2/vpc:Vpc" || args.type === "aws:ec2/subnet:Subnet") {
            return {
                props: args.props,
                opts: pulumi.mergeOptions(args.opts, { ignoreChanges: ["tags"] })
            }
        }
        return undefined;
    }],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def transform(args: ResourceTransformArgs):
    if args.type_ == "aws:ec2/vpc:Vpc" or args.type_ == "aws:ec2/subnet:Subnet":
        return ResourceTransformResult(
            props=args.props,
            opts=ResourceOptions.merge(args.opts, ResourceOptions(
                ignore_changes=["tags"],
            )))

vpc = MyVpcComponent("vpc", opts=ResourceOptions(transforms=[transform]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
transform := func(_ context.Context, args *pulumi.ResourceTransformArgs) *pulumi.ResourceTransformResult {
    if args.Type == "aws:ec2/vpc:Vpc" || args.Type == "aws:ec2/subnet:Subnet" {
        args.Opts.IgnoreChanges = append(args.Opts.IgnoreChanges, "tags")
        return &pulumi.ResourceTransformResult{
            Props: args.Props,
            Opts:  args.Opts,
        }
    }
    return nil
}

vpc := MyVpcComponent("vpc", pulumi.Transforms([]pulumi.ResourceTransform{transform}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var vpc = new MyVpcComponent("vpc", new ComponentResourceOptions
{
    ResourceTransforms =
    {
        async (args, _) =>
        {
            if (args.Type == "aws:ec2/vpc:Vpc" ||
                args.Type == "aws:ec2/subnet:Subnet")
            {
                var options = CustomResourceOptions.Merge(
                    (CustomResourceOptions) args.Options,
                    new CustomResourceOptions { IgnoreChanges = {"tags"} });
                return new ResourceTransformResult(args.Args, options);
            }

            return null;
        }
    }
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Pulumi Java support for transforms is coming soon
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Pulumi YAML does not support transforms
```

{{% /choosable %}}

{{< /chooser >}}

## Stack transforms

To apply a transform in bulk to many or all resources in a stack, use a stack transform. A stack transform applies to all future resources constructed in the stack.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
pulumi.runtime.registerResourceTransform(args => {
    if (args.type === "aws:ec2/vpc:Vpc" || args.type === "aws:ec2/subnet:Subnet") {
        return {
            props: args.props,
            opts: pulumi.mergeOptions(args.opts, { ignoreChanges: ["tags"] })
        }
    }
    return undefined;
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
def transform(args: ResourceTransformArgs):
    if args.type_ == "aws:ec2/vpc:Vpc" or args.type_ == "aws:ec2/subnet:Subnet":
        return ResourceTransformResult(
            props=args.props,
            opts=ResourceOptions.merge(args.opts, ResourceOptions(
                ignore_changes=["tags"],
            )))

pulumi.runtime.register_resource_transform(transform)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.RegisterResourceTransform(
    func(_ context.Context, args *pulumi.ResourceTransformArgs) *pulumi.ResourceTransformResult {
        if args.Type == "aws:ec2/vpc:Vpc" || args.Type == "aws:ec2/subnet:Subnet" {
            args.Opts.IgnoreChanges = append(args.Opts.IgnoreChanges, "tags")
            return &pulumi.ResourceTransformResult{
                Props: args.Props,
                Opts:  args.Opts,
            }
        }
        return nil
    },
)
```

{{% /choosable %}}

{{% choosable language csharp %}}

You can define stack transforms in C# in two ways, depending on which style your Pulumi program uses.

The original way, inheriting from the `Stack` class:

```csharp
public class MyStack : Stack
{
    public MyStack() : base(new StackOptions { ResourceTransforms = { MyTransform } })
    {
        ...
    }

    private static async Task<ResourceTransformResult?> MyTransform(ResourceTransformArgs args, CancellationToken ct)
    {
        if (args.Type == "aws:ec2/vpc:Vpc" ||
            args.Type == "aws:ec2/subnet:Subnet")
        {
            var options = CustomResourceOptions.Merge(
                (CustomResourceOptions) args.Options,
                new CustomResourceOptions { IgnoreChanges = {"tags"} });
            return new ResourceTransformResult(args.Args, options);
        }

        return null;
    }
}
```

or the newer, asynchronous way:

```csharp
using System.Collections.Generic;
using Pulumi;

return await Deployment.RunAsync(async () =>
{
    // register resources here

    return new Dictionary<string, object?>
    {
        ["outputKey"] = "outputValue"
    };
}, new StackOptions
{
    ResourceTransforms =
    {
        async (args, _) =>
        {
            if (args.Type == "aws:ec2/vpc:Vpc" ||
                args.Type == "aws:ec2/subnet:Subnet")
            {
                var options = CustomResourceOptions.Merge(
                    (CustomResourceOptions) args.Options,
                    new CustomResourceOptions { IgnoreChanges = {"tags"} });
                return new ResourceTransformResult(args.Args, options);
            }

            return null;
        }
    }
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Pulumi Java support for transforms is coming soon
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Pulumi YAML does not support transforms
```

{{% /choosable %}}

{{< /chooser >}}

## Transforms vs. transformations

Transforms are a replacement for [transformations](/docs/iac/concepts/resources/options/transformations/). Transformations will be deprecated in the future in favor of transforms.

Transforms offer support for the following capabilities that are not supported by Transformations:

- **Support for transforming child resources of packaged components**, such as components in [awsx](/registry/packages/awsx/) and [eks](/registry/packages/eks/).

- **Support for async transform functions**. In Node.js and Python, transform functions can optionally be `async` and return a `Promise`/`Awaitable` so you can use `await` for async calls in the transform. In .NET, transform functions take a `CancellationToken` as an argument and return a `Task` so you can use `await` for async calls in the transform. In Go, transform functions take a `context.Context` as an argument, allowing access to the async context for tracing/logging/cancellation.

While the Transforms APIs are similar to Transformations, there are some differences in both API signatures and runtime behavior. These are discussed in detail in [Migrating from Transformations to Transforms](/docs/iac/concepts/resources/options/transformations/#migrating-from-transformations-to-transforms).

## Transforms for packaged component resources

Note that a transform will be called twice for packaged component resources (such as those in [awsx](/registry/packages/awsx/) and [eks](/registry/packages/eks/)). The transform will be called before the component resource is constructed, providing an opportunity to modify inputs and resource options before being passed to the provider that implements the component, and then again when the component resource is actually created in the provider, providing an opportunity to modify any resource options that were configured inside the implementation of the component.
