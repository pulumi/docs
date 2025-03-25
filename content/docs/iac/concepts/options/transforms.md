---
title_tag: "transforms | Resource Options"
meta_desc: The transforms resource option provides a list of transforms to apply to
  a resource and all of its children.
title: "transforms"
h1: "Resource option: transforms"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: transforms
    parent: options-concepts
    weight: 15
aliases:
  - /docs/intro/concepts/resources/options/transforms/
  - /docs/concepts/options/transforms/
search:
  keywords:
    - transforms
    - children
    - resource
    - option
    - apply
    - args
    - list
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
// Pulumi Java support for transforms is coming soon
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Pulumi YAML does not support transforms
```

{{% /choosable %}}

{{< /chooser >}}

## Stack Transforms

Transforms can also be applied in bulk to many or all resources in a stack by using Stack transforms, which are applied to the root stack resource and as a result inherited by all other resources in the stack.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
pulumi.runtime.registerResourceTransform(args => {
    if (isTaggable(args.type)) {
        args.props["tags"] = Object.assign(args.props["tags"], autoTags);
        return { props: args.props, opts: args.opts };
    }
};
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
pulumi.runtime.registerResourceTransform(args => {
    if (isTaggable(args.type)) {
        args.props["tags"] = Object.assign(args.props["tags"], autoTags);
        return { props: args.props, opts: args.opts };
    }
};
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
            return new ResourcetransformResult(args.Args, options);
        }

        return null;
    }
}
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

## Transforms vs. Transformations

Transforms are a replacement for [Transformations](/docs/concepts/options/transformations/). Transformations will be deprecated in the future in favor of Transforms.

Transforms offer support for the following capabilities that are not supported by Transformations:

- **Support for transforming child resources of packaged components**, such as components in [awsx](/registry/packages/awsx) and [eks](/registry/packages/eks).

- **Support for async transform functions**. In Node.js and Python, transform functions can optionally be `async` and return a `Promise`/`Awaitable` so you can use `await` for async calls in the transform. In .NET, transform functions take a `CancellationToken` as an argument and return a `Task` so you can use `await` for async calls in the transform. In Go, transform functions take a `context.Context` as an argument, allowing access to the async context for tracing/logging/cancellation.

While the Transforms APIs are similar to Transformations, there are some differences in both API signatures and runtime behavior. These are discussed in detail in [Migrating from Transformations to Transforms](/docs/concepts/options/transformations/#migrating-from-transformations-to-transforms).

## Transforms for Packaged Component Resources

Note that a transform will be called twice for packaged component resources (such as those in [awsx](/registry/packages/awsx) and [eks](/registry/packages/eks)). The transform will be called before the component resource is constructed, providing an opportunity to modify inputs and resource options before being passed to the provider that implements the component, and then again when the component resource is actually created in the provider, providing an opportunity to modify any resource options that were configured inside the implementation of the component.
