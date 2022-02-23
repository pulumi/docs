---
title: "Transformations"
meta_desc: The transformations resource option provides a list of transformations to apply to a resource and all of its children.
menu:
  intro:
    identifier: transformations
    parent: options
    weight: 14
---

The `transformations` resource option provides a list of transformations to apply to a resource and all of its children. This option is used to override or modify the inputs to the child resources of a component resource. One example is to use the option to add other resource options (such as `ignoreChanges` or `protect`). Another example is to modify an input property (such as adding to tags or changing a property that is not directly configurable).

Each transformation is a callback that gets invoked by the Pulumi runtime. It receives the resource type, name, input properties, resource options, and the resource instance object itself. The callback returns a new set of resource input properties and resource options that will be used to construct the resource instead of the original values.

This example looks for all VPC and Subnet resources inside of a component’s child hierarchy and adds an option to ignore any changes for tags properties (perhaps because we manage all VPC and Subnet tags outside of Pulumi):

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const vpc = new MyVpcComponent("vpc", {}, {
    transformations: [args => {
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
    transformations: [args => {
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
def transformation(args: ResourceTransformationArgs):
    if args.type_ == "aws:ec2/vpc:Vpc" or args.type_ == "aws:ec2/subnet:Subnet":
        return ResourceTransformationResult(
            props=args.props,
            opts=ResourceOptions.merge(args.opts, ResourceOptions(
                ignore_changes=["tags"],
            )))

vpc = MyVpcComponent("vpc", opts=ResourceOptions(transformations=[transformation]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
transformation := func(args *pulumi.ResourceTransformationArgs) *pulumi.ResourceTransformationResult {
    if args.Type == "aws:ec2/vpc:Vpc" || args.Type == "aws:ec2/subnet:Subnet" {
        return &pulumi.ResourceTransformationResult{
            Props: args.Props,
            Opts:  append(args.Opts, pulumi.IgnoreChanges([]string{"tags"}))
        }
    }
    return nil
}

vpc := MyVpcComponent("vpc", pulumi.Transformations([]pulumi.ResourceTransformation{transformation}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var vpc = new MyVpcComponent("vpc", new ComponentResourceOptions
{
    ResourceTransformations =
    {
        args =>
        {
            if (args.Resource.GetResourceType() == "aws:ec2/vpc:Vpc" ||
                args.Resource.GetResourceType() == "aws:ec2/subnet:Subnet")
            {
                var options = CustomResourceOptions.Merge(
                    (CustomResourceOptions) args.Options,
                    new CustomResourceOptions { IgnoreChanges = {"tags"} });
                return new ResourceTransformationResult(args.Args, options);
            }

            return null;
        }
    }
});
```

{{% /choosable %}}

{{< /chooser >}}

## Stack Transformations

Transformations can also be applied in bulk to many or all resources in a stack by using Stack Transformations, which are applied to the root stack resource and as a result inherited by all other resources in the stack.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
pulumi.runtime.registerStackTransformation((args) => {
    if (isTaggable(args.type)) {
        args.props["tags"] = Object.assign(args.props["tags"], autoTags);
        return { props: args.props, opts: args.opts };
    }
};
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
pulumi.runtime.registerStackTransformation(args => {
    // ...
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
def my_transformation(args):
    # ...

pulumi.runtime.register_stack_transformation(my_transformation)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.RegisterStackTransformation(
    func(args *pulumi.ResourceTransformationArgs) *pulumi.ResourceTransformationResult {
        // ...
    },
)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
public class MyStack : Stack
{
    public MyStack() : base(new StackOptions { ResourceTransformations = { MyTransformation } })
    {
        ...
    }

    private static ResourceTransformationResult? MyTransformation(ResourceTransformationArgs args)
    {
        // ...
    }
}
```

{{% /choosable %}}

{{< /chooser >}}
