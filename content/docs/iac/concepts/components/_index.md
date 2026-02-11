---
title_tag: "Component Resources"
meta_desc: A component resource is a logical grouping of resources. Learn how to author a new component resource, create child resources, and more in this guide.
title: Components
h1: Component resources
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Components
        parent: iac-concepts
        weight: 100
        identifier: iac-concepts-components
aliases:
- /docs/intro/concepts/resources/components/
- /docs/concepts/resources/components/
- /docs/iac/concepts/resources/components/
---

Pulumi Components enable you to create, share, and consume reusable infrastructure building blocks across your organization and the broader community. Components instantiate a set of related resources, acting as an abstraction to encapsulate the resources' implementation details.

Here are a few examples of component resources:

- A `Vpc` that automatically comes with built-in best practices.
- An `AcmeCorpVirtualMachine` that adheres to your company's requirements, such as tagging.
- A `KubernetesCluster` that can create EKS, AKS, and GKE clusters, depending on the target.

The implicit `pulumi:pulumi:Stack` resource is itself a component resource that contains all top-level resources in a program.

## Authoring a New Component Resource

To author a new component, either in a program or for a reusable library, create a subclass of [`ComponentResource`](/docs/reference/pkg/python/pulumi/#pulumi.ComponentResource). Inside of its constructor, chain to the base constructor, passing its type string, name, arguments, and options. Also inside of its constructor, allocate any child resources, passing the [`parent`](/docs/concepts/options/parent) option as appropriate to ensure component resource children are parented correctly.

Here's a simple component example:

{{< chooser language "typescript,python,go,csharp,java" >}}

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
using System.Collections.Generic;
using Pulumi;

class MyComponent : ComponentResource
{
    public MyComponent(string name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts)
        : base("pkg:index:MyComponent", name, opts)
    {
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
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Upon creating a new instance of MyComponent, the call to the base constructor (using `super/base`) registers the component resource instance with the Pulumi engine. This records the resource's state and tracks it across program deployments so that you see diffs during updates just like with a regular resource (even though component resources have no provider logic associated with them). Since all resources must have a name, a component resource constructor should accept a name and pass it to super.

If you wish to have full control over one of the custom resource's lifecycle in your component resource—including running specific code when a resource has been updated or deleted—you should look into [`dynamic providers`](/docs/concepts/resources/dynamic-providers). These let you create full-blown resource abstractions in your language of choice.

A component resource must register a unique type name with the base constructor. In the example, the registration is `pkg:index:MyComponent`. To reduce the potential of other type name conflicts, this name contains the package and module name, in addition to the type: `<package>:<module>:<type>`. These names are namespaced alongside non-component resources, such as aws:lambda:Function.

{{< notes type="info" >}}
For a complete end-to-end walkthrough of building a component from scratch, including setup, implementation, and publishing, see the [Build a Component](/docs/iac/using-pulumi/build-a-component/) guide.
{{< /notes >}}

{{< notes type="info" >}}
Not all [resource options](/docs/iac/concepts/resources/options/) apply to component resources. For a complete list of which options work with components and how to apply options to child resources, see [Resource options and component resources](/docs/iac/concepts/resources/options/#resource-options-and-component-resources).
{{< /notes >}}

## Component arguments and type requirements

When authoring components that will be consumed across different languages (multi-language components), the arguments class has specific requirements and limitations due to the need for serialization. These constraints ensure that component arguments can be transmitted to the Pulumi engine and reconstructed across language boundaries.

### Serialization requirements

Component arguments must be serializable, meaning you must convert them to a format that the engine can transmit and reconstruct. This is necessary because:

1. The Pulumi engine needs to understand and validate the inputs
1. Multi-language components need to translate arguments between languages
1. The state needs to be stored and retrieved across deployments

### Supported types

The following types are supported in component arguments:

- **Primitive types**: `string`, `number`/`int`, `boolean`.
- **Arrays/lists**: Arrays of any supported type.
- **Objects/maps**: Objects with properties of supported types.
- **Input wrappers**: Language-specific input types that wrap values:
  - TypeScript/JavaScript: `pulumi.Input<T>`
  - Python: `pulumi.Input[T]`
  - Go: `pulumi.StringInput`, `pulumi.IntInput`, etc.
  - .NET: `Input<T>`
  - Java: `Output<T>`

### Unsupported types

The following types are not supported in component arguments:

- **Union types**: TypeScript and Python union types like `string | number` are not supported due to limitations in schema inference. One exception: unions of `undefined` (TypeScript) or `None` (Python) with exactly one other type are supported to represent optional values (e.g., `string | undefined` or `str | None`).
- **Functions/callbacks**: Functions cannot be used in component arguments as they cannot be represented in the schema.
- **Platform-specific types**: Types that exist only in one language and cannot be translated.

### Design recommendations

For better usability and maintainability:

- **Avoid deeply nested types**: While complex generic types can be serialized, deeply nested structures make components harder to use and understand. Keep argument structures simple and flat when possible.

**Example of unsupported TypeScript types:**

```typescript
// ❌ This will NOT work - union types are not supported
export interface MyComponentArgs {
    value: string | number;  // Union type - unsupported
    callback: () => void;    // Function - unsupported
}

// ✅ This WILL work - use primitives or Input types
export interface MyComponentArgs {
    value: pulumi.Input<string>;
    count: pulumi.Input<number>;
}
```

### Constructor requirements by language

Each language has specific requirements for component constructors to ensure proper schema generation:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

**Requirements:**

- The constructor must have an argument named exactly `args`
- The `args` parameter must have a type declaration (e.g., `args: MyComponentArgs`)

```typescript
class MyComponent extends pulumi.ComponentResource {
    constructor(name: string, args: MyComponentArgs, opts?: pulumi.ComponentResourceOptions) {
        super("pkg:index:MyComponent", name, {}, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

**Requirements:**

- The `__init__` method must have an argument named exactly `args`
- The `args` parameter must have a type annotation (e.g., `args: MyComponentArgs`)

```python
class MyComponent(pulumi.ComponentResource):
    def __init__(self, name: str, args: MyComponentArgs, opts: Optional[pulumi.ResourceOptions] = None):
        super().__init__('pkg:index:MyComponent', name, None, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

**Requirements:**

- The constructor function should accept a context, name, args struct, and variadic resource options
- The args should be a struct type

```go
func NewMyComponent(ctx *pulumi.Context, name string, args *MyComponentArgs, opts ...pulumi.ResourceOption) (*MyComponent, error) {
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

**Requirements:**

- The constructor must have exactly 3 arguments:
  1. A `string` for the name (or any unspecified first argument)
  1. An argument that is assignable from `ResourceArgs` (must extend `ResourceArgs`)
  1. An argument that is assignable from `ComponentResourceOptions`

```csharp
public class MyComponent : ComponentResource
{
    public MyComponent(string name, MyComponentArgs args, ComponentResourceOptions? opts = null)
        : base("pkg:index:MyComponent", name, opts)
    {
    }
}

public sealed class MyComponentArgs : ResourceArgs
{
    [Input("value")]
    public Input<string>? Value { get; set; }
}
```

{{% /choosable %}}
{{% choosable language java %}}

**Requirements:**

- The constructor must have exactly one argument that extends `ResourceArgs`
- Other arguments (name, options) are not restricted but typically follow the standard pattern

```java
public class MyComponent extends ComponentResource {
    public MyComponent(String name, MyComponentArgs args, ComponentResourceOptions opts) {
        super("pkg:index:MyComponent", name, null, opts);
    }
}

class MyComponentArgs extends ResourceArgs {
    @Import(name = "value")
    private Output<String> value;

    public Output<String> getValue() {
        return this.value;
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

### Best practices

When designing component arguments:

1. **Wrap all scalar members in Input types**: Every scalar argument should be wrapped in the language's input type (e.g., `pulumi.Input<string>`). This allows users to pass both plain values and outputs from other resources, avoiding the need to use `apply` for resource composition.
1. **Use basic types**: Stick to primitive types, arrays, and basic objects.
1. **Avoid union types**: Instead of a single value with multiple types, consider multiple, mutually exclusive argument members and validate that only one of them has a value in your component constructor.
1. **Document required vs. optional**: Clearly document which arguments are required and which have defaults.
1. **Follow language conventions**: Use camelCase for schema properties but follow language-specific naming in implementation (snake_case in Python, PascalCase in .NET).

## Creating Child Resources

Component resources often contain child resources. The names of child resources are often derived from the component resources's name to ensure uniqueness. For example, you might use the component resource's name as a prefix. Also, when constructing a resource, children must be registered as such. To do this, pass the component resource itself as the `parent` option.

This example demonstrates both the naming convention and how to designate the component resource as the parent:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
class MyComponent extends pulumi.ComponentResource {
    bucket: aws.s3.Bucket;

    constructor(name: string, myComponentArgs: MyComponentArgs, opts: pulumi.ComponentResourceOptions) {
        super("pkg:index:MyComponent", name, {}, opts);

        // Create Child Resource
        this.bucket = new aws.s3.Bucket(`${name}-bucket`,
            {}, { parent: this });
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
class MyComponent(pulumi.ComponentResource):
    def __init__(self, name, my_component_args, opts = None):
        super().__init__('pkg:index:MyComponent', name, None, opts)

        # Create Child Resource
        self.bucket = s3.Bucket(f"{name}-bucket",
            opts=pulumi.ResourceOptions(parent=self))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
type MyComponent struct {
    pulumi.ResourceState
    Bucket *s3.Bucket
}

func NewMyComponent(ctx *pulumi.Context, name string, myComponentArgs MyComponentArgs, opts ...pulumi.ResourceOption) (*MyComponent, error) {
    myComponent := &MyComponent{}
    err := ctx.RegisterComponentResource("pkg:index:MyComponent", name, myComponent, opts...)
    if err != nil {
        return nil, err
    }

    // Create Child Resource
    bucket, err := s3.NewBucket(ctx, fmt.Sprintf("%s-bucket", name),
        &s3.BucketArgs{}, pulumi.Parent(myComponent))
    if err != nil {
        return nil, err
    }
    myComponent.Bucket = bucket

    return myComponent, nil
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.S3;

class MyComponent : ComponentResource
{
    public Bucket Bucket { get; private set; }

    public MyComponent(string name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts)
        : base("pkg:index:MyComponent", name, opts)
    {
        // Create Child Resource
        this.Bucket = new Bucket($"{name}-bucket",
            new BucketArgs(), new CustomResourceOptions { Parent = this });
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.resources.CustomResourceOptions;

class MyComponent extends ComponentResource {
    private final Bucket bucket;

    public MyComponent(String name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts) {
        super("pkg:index:MyComponent", name, null, opts);

        // Create Child Resource
        this.bucket = new Bucket(String.format("%s-bucket", name),
            BucketArgs.builder().build(),
            CustomResourceOptions.builder()
                .parent(this)
                .build());
    }

    public Bucket bucket() {
        return this.bucket;
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

## Registering Component Outputs

Component resources can define their own output properties. Outputs in a component must be registered with the Pulumi IaC engine by calling `registerOutputs`. The Pulumi engine uses this information to display the logical outputs of the component resource and any changes to those outputs will be shown during an update.

For example, this code registers an S3 bucket's computed domain name, which won't be known until the bucket is created:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
class MyComponent extends pulumi.ComponentResource {
    bucket: aws.s3.Bucket;

    constructor(name: string, myComponentArgs: MyComponentArgs, opts: pulumi.ComponentResourceOptions) {
        super("pkg:index:MyComponent", name, {}, opts);

        this.bucket = new aws.s3.Bucket(`${name}-bucket`,
            {}, { parent: this });

        // Registering Component Outputs
        this.registerOutputs({
            bucketDnsName: this.bucket.bucketDomainName
        });
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
class MyComponent(pulumi.ComponentResource):
    bucket_dns_name: pulumi.Output[str]
    """The DNS name of the bucket"""

    def __init__(self, name, my_component_args, opts = None):
        super().__init__('pkg:index:MyComponent', name, None, opts)

        self.bucket = s3.Bucket(f"{name}-bucket",
            opts=pulumi.ResourceOptions(parent=self))

        # Registering Component Outputs
        self.register_outputs({
            "bucket_dns_name": self.bucket.bucket_domain_name
        })
```

{{% /choosable %}}
{{% choosable language go %}}

```go
type MyComponent struct {
    pulumi.ResourceState
    Bucket *s3.Bucket
}

func NewMyComponent(ctx *pulumi.Context, name string, myComponentArgs MyComponentArgs, opts ...pulumi.ResourceOption) (*MyComponent, error) {
    myComponent := &MyComponent{}
    err := ctx.RegisterComponentResource("pkg:index:MyComponent", name, myComponent, opts...)
    if err != nil {
        return nil, err
    }

    bucket, err := s3.NewBucket(ctx, fmt.Sprintf("%s-bucket", name),
        &s3.BucketArgs{}, pulumi.Parent(myComponent))
    if err != nil {
        return nil, err
    }
    myComponent.Bucket = bucket

    //Registering Component Outputs
    ctx.RegisterResourceOutputs(myComponent, pulumi.Map{
        "bucketDnsName": bucket.BucketDomainName,
    })

    return myComponent, nil
}

```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.S3;

class MyComponent : ComponentResource
{
    public Bucket Bucket { get; private set; }

    public MyComponent(string name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts)
        : base("pkg:index:MyComponent", name, opts)
    {

        this.Bucket = new Bucket($"{name}-bucket",
            new BucketArgs(), new CustomResourceOptions { Parent = this });

        // Registering Component Outputs
        this.RegisterOutputs(new Dictionary<string, object?>
        {
            { "bucketDnsName", Bucket.BucketDomainName }
        });
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.resources.CustomResourceOptions;

class MyComponent extends ComponentResource {
    private final Bucket bucket;

    public MyComponent(String name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts) {
        super("pkg:index:MyComponent", name, null, opts);

        this.bucket = new Bucket(String.format("%s-bucket", name),
            BucketArgs.builder().build(),
            CustomResourceOptions.builder()
                .parent(this)
                .build());

        // Registering Component Outputs
        this.registerOutputs(Map.of(
            "bucketDnsName", bucket.bucketDomainName()
        ));
    }

    public Bucket bucket() {
        return this.bucket;
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

The call to `registerOutputs` typically happens at the very end of the component resource's constructor.

### What RegisterOutputs Does

The `registerOutputs` call serves two critical functions:

1. **Marks the component as fully constructed**: It signals to the Pulumi engine that the component resource has finished registering all its child resources and should be considered complete.
1. **Saves outputs to state**: It registers the component's outputs with the Pulumi engine so they are properly saved to the state file and can be referenced by other resources or exported from the stack.

{{% notes type="warning" %}}
Failing to call `registerOutputs` could cause serious issues with your component resource:

- The component will appear as "creating..." indefinitely in the Pulumi Console
- Outputs will not be saved to the state file, potentially causing data loss
- The component lifecycle will not complete properly, which may affect dependency tracking and updates
{{% /notes %}}

## Inheriting Resource Providers

One option all resources have is the ability to pass an [explicit resource provider](/docs/concepts/resources/providers/) to supply explicit configuration settings. For instance, you may want to ensure that all AWS resources are created in a different region than the globally configured region. In the case of component resources, the challenge is that these providers must flow from parent to children.

To allow this, component resources accept a `providers` option that custom resources don't have. This value contains a map from the provider name to the explicit provider instance to use for the component resource. The map is used by a component resource to fetch the proper `provider` object to use for any child resources. This example overrides the globally configured AWS region and sets it to us-east-1. Note that `myk8s` is the name of the Kubernetes provider.

{{< chooser language "typescript,python,go,csharp,java" >}}

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

The contents of the `PulumiPlugin.yaml` file depends on what you're using to manage your Python dependencies:

{{< chooser pythontoolchain "pip,uv,poetry" >}}

{{% choosable pythontoolchain pip %}}

If you're using `pip`, you only need to specify the runtime language:

```yaml
runtime: python
```

{{% /choosable %}}

{{% choosable pythontoolchain uv %}}

If you're using `uv`, you'll need to specify the toolchain option:

```yaml
runtime:
  name: python
  options:
    toolchain: uv
```

{{% /choosable %}}

{{% choosable pythontoolchain poetry %}}

If you're using `poetry`, you'll need to specify the toolchain option:

```yaml
runtime:
  name: python
  options:
    toolchain: poetry
```

{{% /choosable %}}

{{< /chooser >}}

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

The entrypoint analyzes components to automatically build a schema, and interact with the Pulumi engine to manage the component lifecycle.

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

Pulumi Private Registry is the source of truth for an organization's infrastructure building blocks like components and templates -- the same [components](/docs/iac/concepts/resources/components/) and [templates](/docs/idp/developer-portals/templates/) that power golden path workflows in Pulumi. To learn more about publishing packages to the private registry, check out the [Pulumi Private Registry guide](/docs/idp/get-started/private-registry/).

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
- Generates a local SDK from the component's schema
- Makes the generated SDK available to your Pulumi program in your chosen language

{{< notes type="info" >}}
For detailed information about working with local packages, including SDK generation and dependency management, see the [Local Packages](/docs/iac/guides/building-extending/packages/local-packages/) guide.
{{< /notes >}}

#### Referencing Components Locally

For scenarios like monorepos, rapid development iterations, or when you're working with components that don't need to be published to a repository, you can reference local source code directly:

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
