---
title_tag: "transforms | Resource Options"
meta_desc: The transforms resource option provides a list of transforms to apply to a resource and all of its children.
title: "transforms"
h1: "Resource option: transforms"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: transforms
    parent: options
    weight: 15
aliases:
- /docs/intro/concepts/resources/options/transforms/
---

The `transforms` resource option provides a list of transforms to apply to a resource and all of its children. This option is used to override or modify the inputs to the child resources of a component resource. One example is to use the option to add other resource options (such as `ignoreChanges` or `protect`). Another example is to modify an input property (such as adding to tags or changing a property that is not directly configurable).

Each transform is a callback that gets invoked by the Pulumi engine. It receives the resource type, name, input properties, and resource options. The callback returns a new set of resource input properties and resource options that will be used to construct the resource instead of the original values.

## VPC example

This example looks for all VPC and Subnet resources inside of a component’s child hierarchy and adds an option to ignore any changes for tags properties (perhaps because we manage all VPC and Subnet tags outside of Pulumi):

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
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
def transform(args: ResourcetransformArgs):
    if args.type_ == "aws:ec2/vpc:Vpc" or args.type_ == "aws:ec2/subnet:Subnet":
        return ResourcetransformResult(
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
        return &pulumi.ResourceTransformResult{
            Props: args.Props,
            Opts:  append(args.Opts, pulumi.IgnoreChanges([]string{"tags"}))
        }
    }
    return nil
}

vpc := MyVpcComponent("vpc", pulumi.transforms([]pulumi.ResourceTransform{transform}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var vpc = new MyVpcComponent("vpc", new ComponentResourceOptions
{
    ResourceTransforms =
    {
        (args, _) =>
        {
            if (args.Type == "aws:ec2/vpc:Vpc" ||
                args.Type == "aws:ec2/subnet:Subnet")
            {
                var options = CustomResourceOptions.Merge(
                    (CustomResourceOptions) args.Options,
                    new CustomResourceOptions { IgnoreChanges = {"tags"} });
                return new ResourcetransformResult(args.Args, options);
            }

            return null;
        }
    }
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
# Pulumi Java does not support transforms
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Pulumi YAML does not support transforms
```

{{% /choosable %}}

{{< /chooser >}}

## Stack transforms

Transforms can also be applied in bulk to many or all resources in a stack by using Stack transforms, which are applied to the root stack resource and as a result inherited by all other resources in the stack.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
pulumi.runtime.registerStackTransform((args) => {
    if (isTaggable(args.type)) {
        args.props["tags"] = Object.assign(args.props["tags"], autoTags);
        return { props: args.props, opts: args.opts };
    }
};
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
pulumi.runtime.registerStackTransform(args => {
    // ...
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
def my_transform(args):
    # ...

pulumi.runtime.register_stack_transform(my_transform)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.RegisterStackTransform(
    func(_ context.Context, args *pulumi.ResourceTransformArgs) *pulumi.ResourceTransformResult {
        // ...
    },
)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
public class MyStack : Stack
{
    public MyStack() : base(new StackOptions { ResourceTransforms = { MyTransform } })
    {
        ...
    }

    private static ResourceTransformResult? MyTransform(ResourceTransformArgs args, CancellationToken ct)
    {
        // ...
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
# Pulumi Java does not support transforms
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Pulumi YAML does not support transforms
```

{{% /choosable %}}

{{< /chooser >}}

## Transforms vs Transformations

The `transforms` option is the replacement system to [transformations](/docs/concepts/options/transformations/). Calling transform functions is managed by the engine, rather than by each SDK and so transforms apply to resources created inside remote component resources (such as those in [AWSX](https://www.pulumi.com/registry/packages/awsx/)).

That last point does not apply to the old `transformations` system, which couldn't operate on resources created inside remote components.

However because `transforms` are invoked by the engine the properties are the values after being serialised and deserialised across the wire protocol to the engine and back to the SDK runtime. As such unlike with `transformations` there is no `Resource` object, and the properties will be raw property maps not typed resource arg classes.

The new transform system is also natively async. As such, depending on the language you are using you may have to lift your transform function to be `async` and/or to handle an extra parameter for the async context (e.g. a `context.Context` in Go, or `System.Threading.CancellationToken` in C#).

As such when moving from `transformations` to `transforms` you will need to update your transform code to handle these differences.

### No resource type

There is no `Resource` object passed to transform functions. Most of the information you could have retrieved from that object is presented on the transform arguments directly.

For example given the following C# transform:

```csharp
args =>
{
    if (args.Resource.GetResourceType() == "random:index/randomString:RandomString")
    {
        var resultOpts = CustomResourceOptions.Merge((CustomResourceOptions)args.Options,
            new CustomResourceOptions {AdditionalSecretOutputs = {"length"}});
        return new ResourceTransformationResult(resultArgs, resultOpts);
    }
    return null;
}
```

We can rewrite this to:

```csharp
async (args, _) =>
{
    if (args.Type == "random:index/randomString:RandomString")
    {
        var resultOpts = CustomResourceOptions.Merge((CustomResourceOptions)args.Options,
            new CustomResourceOptions {AdditionalSecretOutputs = {"length"}});
        return new ResourceTransformResult(resultArgs, resultOpts);
    }
    return null;
}
```

### No typed resource args class

In the old transform system the transform function was called with the same object that was passed to the resource constructor. This meant that
in typed languages like Go and C# you could typecast to the typed arguments struct.

```go
func(_ context.Context, rta *pulumi.ResourceTransformationArgs) *pulumi.ResourceTransformationResult {
    if rta.Type == "testprovider:index:Random" {
        var props *RandomArgs
        if rta.Props == nil {
            props = &RandomArgs{}
        } else {
            props = rta.Props.(*RandomArgs)
        }
        props.Length = props.Length.ToOutput().ApplyT(func(v int) int { return v * 2 })

        return &pulumi.ResourceTransformationResult{
            Props: props,
            Opts:  rta.Opts,
        }
    }
    return nil
}
```

The new transform system works over the wire protocol, allowing it to run for resources created in other
processes, but it means the properties object you get is closer to the raw protocol than the typed arguments
you might expect.

In this Go example the old system would have given us a typed `RandomArgs` structure with the length field
being a `pulumi.IntInput`. The new system is just a map where we have to know the key is `"length"` and the
value is a `Float64Output`.

You might ask why `Float64Output` instead of at least `IntOutput`. This is because the wire protocol doesn't
actually have support for integers (being JSON based), so on receiving the untyped properties the transform
callback can only go on their JSON values and all numbers are 64-bit floats.

```go
func(_ context.Context, rta *pulumi.XResourceTransformArgs) *pulumi.XResourceTransformResult {
    if rta.Type == "testprovider:index:Random" {
        length := rta.Props["length"].(pulumi.Float64Output)
        rta.Props["length"] = length.ApplyT(func(v float64) float64 { return v * 2 })

        return &pulumi.XResourceTransformResult{
            Props: rta.Props,
            Opts:  rta.Opts,
        }
    }
    return nil
},
```

### Natively async

The new transform API has been designed from the start with async support in mind.

In all applicable languages the transform functions support returning a Promise/Task so you can use standard `await` operators for async calls in the transform.

For Go we pass a `context.Context` in as the first argument for the transform function. This is to indicate its async nature, but also allows you access to the async context for tracing/logging/cancellation.

For DotNet we pass a `System.Threading.CancellationToken` as the last argument of the transform function. This allows you to handle cancellation if needed.