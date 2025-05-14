---
title_tag: "Component Resources"
meta_desc: A component resource is a logical grouping of resources. Learn how to author a new component resource, create child resources, and more in this guide.
title: Components
h1: Component resources
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Components
        parent: iac-concepts-resources
        weight: 3
    concepts:
        parent: resources
        weight: 3
aliases:
- /docs/intro/concepts/resources/components/
- /docs/concepts/resources/components/
---

Pulumi Components enable you to create, share, and consume reusable infrastructure building blocks across your organization and the broader community. Components instantiate a set of related resources, acting as an abstraction to encapsulate the resources' implementation details.

Here are a few examples of component resources:

- A `Vpc` that automatically comes with built-in best practices.
- An `AcmeCorpVirtualMachine` that adheres to your company’s requirements, such as tagging.
- A `KubernetesCluster` that can create EKS, AKS, and GKE clusters, depending on the target.

The implicit `pulumi:pulumi:Stack` resource is itself a component resource that contains all top-level resources in a program.

## Authoring a New Component Resource

To author a new component, either in a program or for a reusable library, create a subclass of [`ComponentResource`](/docs/reference/pkg/python/pulumi/#pulumi.ComponentResource). Inside of its constructor, chain to the base constructor, passing its type string, name, arguments, and options. Also inside of its constructor, allocate any child resources, passing the [`parent`](/docs/concepts/options/parent) option as appropriate to ensure component resource children are parented correctly.

Here’s a simple component example:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
class MyComponent extends pulumi.ComponentResource {
    constructor(name, myComponentArgs, opts) {
        super("pkg:index:MyComponent", name, {}, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
class MyComponent extends pulumi.ComponentResource {
    constructor(name: string, myComponentArgs: MyComponentArgs, opts: pulumi.ComponentResourceOptions) {
        super("pkg:index:MyComponent", name, {}, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
class MyComponent(pulumi.ComponentResource):
    def __init__(self, name, my_component_args, opts = None):
        super().__init__('pkg:index:MyComponent', name, None, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
type MyComponent struct {
    pulumi.ResourceState
}

func NewMyComponent(ctx *pulumi.Context, name string, myComponentArgs MyComponentArgs, opts ...pulumi.ResourceOption) (*MyComponent, error) {
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
    public MyComponent(string name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts)
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
    public MyComponent(String name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts) {
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

If you wish to have full control over one of the custom resource’s lifecycle in your component resource—including running specific code when a resource has been updated or deleted—you should look into [`dynamic providers`](/docs/concepts/resources/dynamic-providers). These let you create full-blown resource abstractions in your language of choice.

A component resource must register a unique type name with the base constructor. In the example, the registration is `pkg:index:MyComponent`. To reduce the potential of other type name conflicts, this name contains the package and module name, in addition to the type: `<package>:<module>:<type>`. These names are namespaced alongside non-component resources, such as aws:lambda:Function.

For more information about component resources, see the [Pulumi Components tutorial](/registry/packages/aws/how-to-guides/s3-folder-component/). For a detailed look at supporting component consumption in multiple languages, see the [Building a Component](/docs/iac/using-pulumi/extending-pulumi/build-a-component) guide

## Creating Child Resources

Component resources often contain child resources. The names of child resources are often derived from the component resources’s name to ensure uniqueness. For example, you might use the component resource’s name as a prefix. Also, when constructing a resource, children must be registered as such. To do this, pass the component resource itself as the `parent` option.

This example demonstrates both the naming convention and how to designate the component resource as the parent:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
let bucket = new aws.s3.BucketV2(`${name}-bucket`,
    {/*...*/}, { parent: this });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let bucket = new aws.s3.BucketV2(`${name}-bucket`,
    {/*...*/}, { parent: this });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
bucket = s3.BucketV2(f"{name}-bucket",
    opts=pulumi.ResourceOptions(parent=self))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
bucket, err := s3.NewBucketV2(ctx, fmt.Sprintf("%s-bucket", name),
    &s3.BucketV2Args{ /*...*/ }, pulumi.Parent(myComponent))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var bucket = new Aws.S3.BucketV2($"{name}-bucket",
    new Aws.S3.BucketV2Args(/*...*/), new CustomResourceOptions { Parent = this });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var bucket = new BucketV2(String.format("%s-bucket", name),
    BucketV2Args.builder()
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

One option all resources have is the ability to pass an [explicit resource provider](/docs/concepts/resources/providers/) to supply explicit configuration settings. For instance, you may want to ensure that all AWS resources are created in a different region than the globally configured region. In the case of component resources, the challenge is that these providers must flow from parent to children.

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

## Adding Multi-language Support

By default, components are authored and consumed in the same programming language by extending the `ComponentResource` class. The class can then be imported or referenced using the language's applicable pattern. To support consuming components in other languages, Pulumi can introspect your component class and generate the necessary SDKs. To support multi-language consumption, a couple additional steps are required.

### Define a `PulumiPlugin.yaml` file

In your component directory, create a `PulumiPlugin.yaml` file and specify the runtime the component is authored in.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
runtime: nodejs
```

{{% /choosable %}}
{{% choosable language python %}}

```python
runtime: python
```

{{% /choosable %}}
{{% choosable language go %}}

```go
runtime: go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
runtime: dotnet
```

{{% /choosable %}}
{{% choosable language java %}}

```java
runtime: java
```

{{% /choosable %}}

{{< /chooser >}}

### Define an Entry Point

The entrypoint analyzes components to automatically build a schema, and interact with the Pulumi engine to mange the component lifecycle.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

Not required for TypeScript.

{{% /choosable %}}
{{% choosable language python %}}

1. Create a `_main_.py` file in your component directory
2. In the `main` function, add a call to `component_provider_host`, specifying a list of components for the `components` argument

```python
from pulumi.provider.experimental import Metadata, component_provider_host
from staticpage import MyComponent

if __name__ == "__main__":
    component_provider_host(name="python-components", components=[MyComponent])
```

{{% /choosable %}}
{{% choosable language go %}}

1. Define a `main.go` file
2. Declare an instance of `NewProviderBuilder`,  passing in a name, namespace and the components being built

{{% notes type="info" %}}
The code below uses the new pulumi-go-provider v1 APIs. Make sure you are using the latest version of `github.com/pulumi/pulumi-go-provider`.
{{% /notes %}}

```go
package main

import (
    "context"
    "log"

    "github.com/pulumi/pulumi-go-provider/infer"
)

func main() {
    prov, err := infer.NewProviderBuilder().
            WithNamespace("your-org-name").
            WithComponents(
                infer.ComponentF(MyComponent),
            ).
            Build()
    if err != nil {
        log.Fatal(err.Error())
    }

    _ = prov.Run(context.Background(), "go-components", "v0.0.1")
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

1. Create a `Program.cs` file
2. Add an entry point that calls the `ComponentProviderHost`

```csharp
using System.Threading.Tasks;

class Program
{
    public static Task Main(string []args) =>
        Pulumi.Experimental.Provider.ComponentProviderHost.Serve(args);
}
```

{{% /choosable %}}
{{% choosable language java %}}

1. Create an `App.java` file
2. Create a new instance of `ComponentProviderHost` in the entry point

```java
package com.example.components;

import java.io.IOException;
import com.pulumi.provider.internal.Metadata;
import com.pulumi.provider.internal.ComponentProviderHost;

public class App {
    public static void main(String[] args) throws IOException, InterruptedException {
        new ComponentProviderHost("java-components", App.class.getPackage()).start(args);
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

### Publishing the Component

Once a component is authored, it can be published to the [IDP Private Registry](/docs/idp/get-started/private-registry/) or consumed directly from a git repo.

#### Private Registry Publishing

Pulumi Private Registry is the source of truth for an organization's infrastructure building blocks like components and templates -- the same [components](/docs/iac/concepts/resources/components/) and [templates](/docs/pulumi-cloud/developer-portals/templates/) that power golden path workflows in Pulumi. To learn more about publishing packages to the private registry, check out the [Pulumi Private Registry guide](/idp/get-started/private-registry/).

#### Consumption

In the consuming Pulumi application, add the component as a dependency.

```bash
pulumi package add github.com/myorg/my-component
```

If you're using version tags, you can specify those as well.

```bash
pulumi package add github.com/myorg/my-component@v1.0.0
```

Under the hood, Pulumi:

- Fetches your code from GitHub
- Generates a local SDK from the component’s schema
- Makes the generated SDK available to your Pulumi program in your chosen language

#### Referencing Components Locally

For scenarios like monorepos, rapid development iterations, or when you’re working with components that don’t need to be published to a repository, you can reference local source code directly:

```bash
pulumi package add /path/to/local/secure-s3-component
```

Pulumi will identify the folder as a Pulumi component project, generate a local SDK, and make it available for import in your program—even if your consumer program is in a different language.

## The Spectrum of Pulumi Components You Can Build

You can use Pulumi Components with more flexibility and control depending on your use case. This table shows the variety of use cases:

| Feature | Single language | Multi-language with Auto-Generated SDKs | Manual Schema and SDKs |
|---------|--------------------------|-------------------------------------------|--------------------------|
| **Best for** | Quick development within a single language ecosystem | Cross-language teams needing to share components | More flexibility and control needed or strict API requirements |
| **Cross-language consumption** | No - limited to original language | Yes - consume in any Pulumi language | Yes - consume in any Pulumi language but YAML|
| **Setup complexity** | Minimal - standard programming patterns | Minimal - just requires package management | High - requires schema authoring and validation |
| **Development workflow** | Fast iteration with direct code changes | Requires SDK regeneration when component changes | Complex with schema updates and SDK publishing |
| **API control** | N/A | Moderate - auto-generated from source | Full - ship the same interface to all consumers |
| **Version management** | Simple - standard code versioning | Moderate - requires careful API changes | Complex - strict semantic versioning needed |
| **Typical user** | Individual developers or same-language teams | Platform teams sharing with developers | Enterprise teams with strict requirements or package publishers |
| **Ideal use cases** | • Rapid prototyping<br>• Single team projects<br>• Simple components | • Organization-wide libraries<br>• Platform engineering<br>• Multi-language environments | • Published packages<br>• Complex validation needs |
| **Limitations** | • Single language only<br> | • SDK regeneration overhead<br>• Runtime dependencies<br>• Some translation limitations | • Complex setup<br>• Steep learning curve<br>• Slower iteration |
