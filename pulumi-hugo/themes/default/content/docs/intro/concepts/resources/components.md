---
title: "Components"
meta_desc: A component resource is a logical grouping of resources.
menu:
  intro:
    parent: resources
    weight: 3
---

A component resource is a logical grouping of resources. Components usually instantiate a set of related resources in their constructor, aggregate them as children, and create a larger, useful abstraction that encapsulates their implementation details.

Here are a few examples of component resources:

- A `Vpc` that automatically comes with built-in best practices.
- An `AcmeCorpVirtualMachine` that adheres to your company’s requirements, such as tagging.
- A `KubernetesCluster` that can create EKS, AKS, and GKE clusters, depending on the target.

The implicit `pulumi:pulumi:Stack` resource is itself a component resource that contains all top-level resources in a program.

## Authoring a New Component Resource

To author a new component, either in a program or for a reusable library, create a subclass of [`ComponentResource`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.ComponentResource" >}}). Inside of its constructor, chain to the base constructor, passing its type string, name, arguments, and options. Also inside of its constructor, allocate any child resources, passing the [`parent`]({{< relref "options/parent" >}}) option as appropriate to ensure component resource children are parented correctly.

Here’s a simple component example:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
class MyComponent extends pulumi.ComponentResource {
    constructor(name, opts) {
        super("pkg:index:MyComponent", name, {}, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
class MyComponent extends pulumi.ComponentResource {
    constructor(name, opts) {
        super("pkg:index:MyComponent", name, {}, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
class MyComponent(pulumi.ComponentResource):
    def __init__(self, name, opts = None):
        super().__init__('pkg:index:MyComponent', name, None, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
type MyComponent struct {
    pulumi.ResourceState
}

func NewMyComponent(ctx *pulumi.Context, name string, opts ...pulumi.ResourceOption) (*MyComponent, error) {
    myComponent := &MyComponent{}
    err := ctx.RegisterComponentResource("pkg:index:MyComponent", name, myComponent, opts...)
    if err != nil {
        return nil, err
    }

    return myComponent, nil
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
class MyComponent : Pulumi.ComponentResource
{
    public MyComponent(string name, ComponentResourceOptions opts)
        : base("pkg:index:MyComponent", name, opts)
    {
        // initialization logic.

        // Signal to the UI that this resource has completed construction.
        this.RegisterOutputs();
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;

class MyComponent extends ComponentResource {
    public MyComponent(String name, ComponentResourceOptions opts) {
        super("pkg:index:MyComponent", name, null, opts);
        // initialization logic.

        // Signal to the UI that this resource has completed construction.
        this.registerOutputs();
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Upon creating a new instance of MyComponent, the call to the base constructor (using `super/base`) registers the component resource instance with the Pulumi engine. This records the resource’s state and tracks it across program deployments so that you see diffs during updates just like with a regular resource (even though component resources have no provider logic associated with them). Since all resources must have a name, a component resource constructor should accept a name and pass it to super.

If you wish to have full control over one of the custom resource’s lifecycle in your component resource—including running specific code when a resource has been updated or deleted—you should look into [`dynamic providers`]({{< relref "dynamic-providers" >}}). These let you create full-blown resource abstractions in your language of choice.

A component resource must register a unique type name with the base constructor. In the example, the registration is `pkg:index:MyComponent`. To reduce the potential of other type name conflicts, this name contains the package and module name, in addition to the type: `<package>:<module>:<type>`. These names are namespaced alongside non-component resources, such as aws:lambda:Function.

For more information about component resources, see the [Pulumi Components tutorial]({{< relref "/registry/packages/aws/how-to-guides/s3-folder-component" >}}).

## Creating Child Resources

Component resources often contain child resources. The names of child resources are often derived from the component resources’s name to ensure uniqueness. For example, you might use the component resource’s name as a prefix. Also, when constructing a resource, children must be registered as such. To do this, pass the component resource itself as the `parent` option.

This example demonstrates both the naming convention and how to designate the component resource as the parent:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
let bucket = new aws.s3.Bucket(`${name}-bucket`,
    {/*...*/}, { parent: this });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let bucket = new aws.s3.Bucket(`${name}-bucket`,
    {/*...*/}, { parent: this });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
bucket = s3.Bucket(f"{name}-bucket",
    opts=pulumi.ResourceOptions(parent=self))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
bucket, err := s3.NewBucket(ctx, fmt.Sprintf("%s-bucket", name),
    &s3.BucketArgs{ /*...*/ }, pulumi.Parent(myComponent))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var bucket = new Aws.S3.Bucket($"{name}-bucket",
    new Aws.S3.BucketArgs(/*...*/), new CustomResourceOptions { Parent = this });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var bucket = new Bucket(String.format("%s-bucket", name),
    BucketArgs.builder()
    ...
    .build(),
    CustomResourceOptions.builder()
    .parent(this)
    .build());
```

{{% /choosable %}}

{{< /chooser >}}

## Registering Component Outputs

Component resources can define their own output properties by using register_outputs . The Pulumi engine uses this information to display the logical outputs of the component resource and any changes to those outputs will be shown during an update.

For example, this code registers an S3 bucket’s computed domain name, which won’t be known until the bucket is created:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
this.registerOutputs({
    bucketDnsName: bucket.bucketDomainName,
})
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
this.registerOutputs({
    bucketDnsName: bucket.bucketDomainName,
})
```

{{% /choosable %}}
{{% choosable language python %}}

```python
self.register_outputs({
    "bucketDnsName": bucket.bucketDomainName
})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
ctx.RegisterResourceOutputs(myComponent, pulumi.Map{
    "bucketDnsName": bucket.BucketDomainName,
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
this.RegisterOutputs(new Dictionary<string, object>
{
    { "bucketDnsName", bucket.BucketDomainName }
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
this.registerOutputs(Map.of(
    "bucketDnsName", bucket.bucketDomainName()
));
```

{{% /choosable %}}

{{< /chooser >}}

The call to `registerOutputs` typically happens at the very end of the component resource’s constructor.

The call to `registerOutputs` also tells Pulumi that the resource is done registering children and should be considered fully constructed, so—although it’s not enforced—the best practice is to call it in all components even if no outputs need to be registered.

## Inheriting Resource Providers

One option all resources have is the ability to pass an [explicit resource provider]({{< relref "providers">}}) to supply explicit configuration settings. For instance, you may want to ensure that all AWS resources are created in a different region than the globally configured region. In the case of component resources, the challenge is that these providers must flow from parent to children.

To allow this, component resources accept a `providers` option that custom resources don’t have. This value contains a map from the provider name to the explicit provider instance to use for the component resource. The map is used by a component resource to fetch the proper `provider` object to use for any child resources. This example overrides the globally configured AWS region and sets it to us-east-1. Note that `myk8s` is the name of the Kubernetes provider.

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
let component = new MyComponent("...", {
    providers: {
        aws: useast1,
        kubernetes: myk8s,
    },
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let component = new MyComponent("...", {
    providers: {
        aws: useast1,
        kubernetes: myk8s,
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
component = MyComponent('...', ResourceOptions(providers={
    'aws': useast1,
    'kubernetes': myk8s,
}))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
component, err := NewMyResource(ctx, "...", nil, pulumi.ProviderMap(
    map[string]pulumi.ProviderResource{
        "aws":        awsUsEast1,
        "kubernetes": myk8s,
    },
))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var component = new MyResource("...", new ComponentResourceOptions {
    Providers = {
        { "aws", awsUsEast1 },
        { "kubernetes", myk8s }
    }
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var component = new MyResource("...",
    ComponentResourceOptions.builder()
        .providers(awsUsEast1, myk8s)
        .build());
```

{{% /choosable %}}

{{< /chooser >}}

If a component resource is itself a child of another component resource, its set of providers is inherited from its parent by default.
