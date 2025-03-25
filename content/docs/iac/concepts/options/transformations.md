---
title_tag: "transformations | Resource Options"
meta_desc: The transformations resource option provides a list of transformations
  to apply to a resource and all of its children.
title: "transformations"
h1: "Resource option: transformations"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: transformations
    parent: options-concepts
    weight: 15
aliases:
  - /docs/intro/concepts/resources/options/transformations/
  - /docs/concepts/options/transformations/
search:
  keywords:
    - transformations
    - children
    - resource
    - option
    - apply
    - props
    - list
---

The `transformations` resource option provides a list of transformations to apply to a resource and all of its children. This option is used to override or modify the inputs to the child resources of a component resource. One example is to use the option to add other resource options (such as `ignoreChanges` or `protect`). Another example is to modify an input property (such as adding to tags or changing a property that is not directly configurable).

Each transformation is a callback that gets invoked by the Pulumi runtime. It receives the resource type, name, input properties, resource options, and the resource instance object itself. The callback returns a new set of resource input properties and resource options that will be used to construct the resource instead of the original values.

{{% notes type="warning" %}}
Note that Transformations will be deprecated in the future in favor of [Transforms](/docs/concepts/options/transforms).

Transforms support modifying child resources of packaged components (such as those in [awsx](/registry/packages/awsx) and [eks](/registry/packages/eks)) whereas Transformations do not.

See [Migrating from Transformations to Transforms](#migrating-from-transformations-to-transforms) below for guidance on how to migrate from Transformations to Transforms.
{{% /notes %}}

This example looks for all VPC and Subnet resources inside of a component’s child hierarchy and adds an option to ignore any changes for tags properties (perhaps because we manage all VPC and Subnet tags outside of Pulumi):

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
{{% choosable language java %}}

```java
var vpc = new MyVpcComponent("vpc",
    ComponentResourceOptions.builder()
        .resourceTransformations(resourceTransformation -> {
            var resource = resourceTransformation.getResource();
            var args = resourceTransformation.getArgs();
            var options = resourceTransformation.getOptions();
            if (resource.getResourceType() == "aws:ec2/vpc:Vpc" ||
                resource.getResourceType() == "aws:ec2/subnet:Subnet") {

                var mergedOptions = CustomResourceOptions.merge(
                    (CustomResourceOptions) options,
                    CustomResourceOptions.builder()
                        .ignoreChanges("tags")
                        .build());
                return Optional.of(new ResourceTransformation.Result(args, mergedOptions));
            }
            return Optional.of(new ResourceTransformation.Result(args, options));
        }).build());

```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Pulumi YAML does not support transformations
```

{{% /choosable %}}

{{< /chooser >}}

## Stack Transformations

Transformations can also be applied in bulk to many or all resources in a stack by using Stack Transformations, which are applied to the root stack resource and as a result inherited by all other resources in the stack.  Note that this applies only to resources that are registered after the stack transformation is registered.  Resources in the stack that have already been registered will not get the Stack Transformation applied to them.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
        var tagProperty = args.Args.GetType().GetProperty("Tags");
        if (tagProperty != null) {
            var currentResourceTags = (InputMap<string>)tagProperty.GetValue(args.Args, null) ?? new InputMap<string>();
            currentResourceTags["env"] = "production";
            tagProperty.SetValue(args.Args, currentResourceTags, null);
            return new ResourceTransformationResult(args.Args, (CustomResourceOptions)args.Options);
        }
        return null;
    }
}
```

{{% notes type="warning" %}}
It is not currently possible to use stack level transformations in .NET when using a top-level async program. We have an [open issue](https://github.com/pulumi/pulumi-dotnet/issues/202) regarding this feature that you can follow to find out more information.
{{% /notes %}}

{{% /choosable %}}
{{% choosable language java %}}

```java
var stackOptions = StackOptions.builder()
    .resourceTransformations(args -> {
        // ...
    })
    .build();

Pulumi.withOptions(stackOptions).run(ctx -> {
    // ...
});
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Pulumi YAML does not support transformations
```

{{% /choosable %}}

{{< /chooser >}}

## Migrating from Transformations to Transforms

Transformations will be deprecated in the future in favor of the more capable [Transforms](/docs/concepts/options/transforms) APIs. While the Transforms APIs are similar to Transformations, there are some differences in both API signatures and runtime behavior to be aware of. When moving from Transformations to Transforms you will need to update your transform code to handle the differences.

Summary of key differences:

- [**No resource object**](#no-resource-object): There is no `Resource` object passed to transform functions. Most of the information you could have retrieved from that object is presented on the transform arguments directly, such as the type of the resource.

- [**No typed args classes**](#no-typed-args-classes): In the old transformation system the transform function is called with the same values that are passed to the resource constructor. This means that in languages like Go, C#, and Python, you could typecast the arguments to the typed args struct/class. The new transform system works over the wire protocol, allowing it to run for resources created in other processes, but it means the properties object you get is closer to the raw protocol than the typed arguments you might expect. Objects are represented as dictionaries/maps with camelCase keys (e.g. in Python, access properties with camelCase keys like `environmentVariables` instead of snake_case keys like `environment_variables`). Property names in resource options are also camelCase.

- [**Natively Async**](#natively-async): The new transform API has been designed from the start with async support in mind. In all applicable languages the transform functions support returning a Promise/Task so you can use standard `await` operators for async calls in the transform. In Node.js and Python, returning a Promise/Awaitable is optional.

### No Resource Object

There is no `Resource` object passed to transform functions. Most of the information you could have retrieved from that object is presented on the transform arguments directly.

This mostly impacts C# transforms. With transformations, you would have to call `args.Resource.GetResourceType()` to get the type of the resource:

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

With transforms, this is now available as `args.Type`:

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

### No Typed Args Classes

In the old transform system the transform function was called with the same values passed to the resource constructor. This meant that in languages like Go, C#, and Python you could typecast to the typed arguments struct/class.

The new transform system works over the wire protocol, allowing it to run for resources created in other
processes, but it means the properties object you get is closer to the raw protocol than the typed arguments
you might expect. Objects are represented as dictionaries/maps with camelCase keys (e.g. in Python, access properties with camelCase keys like `environmentVariables` instead of snake_case keys like `environment_variables`). Property names in resource options are also camelCase.

{{< chooser language "python,go,csharp" >}}

{{% choosable language python %}}

Here's a Python example of the old system:

```python
def transformation(args: pulumi.ResourceTransformationArgs) -> pulumi.ResourceTransformationResult | None:
    if args.type_ == "random:index/randomString:RandomString":
        props = { **args.props }
        length = pulumi.Output.from_input(props["length"])
        props["length"] = length.apply(lambda v: v * 2)
        props["special"] = True
        props["override_special"] = "/@£$"
        return pulumi.ResourceTransformationResult(props=props, opts=args.opts)
```

Here's the example with the new system:

```python
def transform(args: pulumi.ResourceTransformArgs) -> pulumi.ResourceTransformResult | None:
    if args.type_ == "random:index/randomString:RandomString":
        props = { **args.props }
        length = pulumi.Output.from_input(props["length"])
        props["length"] = length.apply(lambda v: v * 2)
        props["special"] = True
        props["overrideSpecial"] = "/@£$"
        return pulumi.ResourceTransformResult(props=props, opts=args.opts)
```

Note in the new system, we specify the property name as `overrideSpecial` instead of `override_special`.

{{% /choosable %}}
{{% choosable language go %}}

In this Go example the old system would have given us a typed `RandomStringArgs` structure with the `Length` field
being a `pulumi.IntInput`:

```go
func(_ context.Context, args *pulumi.ResourceTransformationArgs) *pulumi.ResourceTransformationResult {
    if args.Type == "random:index/randomString:RandomString" {
        var props *random.RandomStringArgs
        if args.Props == nil {
            props = &random.RandomStringArgs{}
        } else {
            props = args.Props.(*random.RandomStringArgs)
        }
        props.Length = props.Length.ToIntOutput().ApplyT(func(v int) int { return v * 2 }).(pulumi.IntOutput)
        props.Special = pulumi.Bool(true)
        props.OverrideSpecial = pulumi.String("/@£$")

        return &pulumi.ResourceTransformationResult{
            Props: props,
            Opts:  args.Opts,
        }
    }
    return nil
}
```

The new system is just a map where we have to know the key is `"length"` and the value is a `Float64Input`:

```go
func(_ context.Context, args *pulumi.ResourceTransformArgs) *pulumi.ResourceTransformResult {
    if args.Type == "random:index/randomString:RandomString" {
        props := args.Props
        if props == nil {
            props = pulumi.Map{}
        }
        length := args.Props["length"].(pulumi.Float64Input).ToFloat64Output()
        props["length"] = length.ApplyT(func(v float64) float64 { return v * 2 })
        props["special"] = pulumi.Bool(true)
        props["overrideSpecial"] = pulumi.String("/@£$")

        return &pulumi.ResourceTransformResult{
            Props: props,
            Opts:  args.Opts,
        }
    }
    return nil
},
```

You might ask why `Float64Input` instead of at least `IntInput`. This is because the wire protocol doesn't
actually have support for integers (being JSON based), so on receiving the untyped properties the transform
callback can only go on their JSON values and all numbers are 64-bit floats.

{{% /choosable %}}
{{% choosable language csharp %}}

In this C# example, the old system would have given us a typed `RandomStringArgs` class with the `Length` field being an `Input<int>`:

```csharp
args =>
{
    if (args.Resource.GetResourceType() == "random:index/randomString:RandomString")
    {
        var props = (RandomStringArgs)args.Args;
        props.Length = props.Length.Apply(v => v * 2);
        props.Special = true;
        props.OverrideSpecial = "/@£$";
        return new ResourceTransformationResult(props, args.Options);
    }
    return null;
}
```

The new system is just a dictionary where we have to know the key is `"length"` and the value is a `Input<double>`:

```csharp
(args, _) =>
{
    if (args.Type == "random:index/randomString:RandomString")
    {
        var props = args.Args;
        var length = (double)props["length"]! * 2;
        props = props.SetItem("length", length);
        props = props.SetItem("special", true);
        props = props.SetItem("overrideSpecial", "/@£$");
        return new ResourceTransformResult(props, args.Options);
    }
    return null;
}
```

{{% /choosable %}}

{{< /chooser >}}

### Natively Async

The new transform API has been designed from the start with async support in mind.

In all applicable languages the transform functions support returning a Promise/Task so you can use standard `await` operators for async calls in the transform.

For Go, we pass a `context.Context` in as the first argument for the transform function. This is to indicate its async nature, but also allows you access to the async context for tracing/logging/cancellation.

For .NET, we pass a `System.Threading.CancellationToken` as the last argument of the transform function. This allows you to handle cancellation if needed.

For Node.js and Python, the transform function can optionally be `async` and return a `Promise`/`Awaitable`.
