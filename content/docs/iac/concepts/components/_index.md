---
title_tag: "Component Resources"
meta_desc: Learn what Pulumi component resources are, how to consume them, and how to author your own reusable infrastructure building blocks.
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

A component is a logical grouping of Pulumi resources that is exposed as a single Pulumi resource. Components encapsulate related resources and their configuration, letting consumers create complex infrastructure through a simple, well-defined interface—without needing to know the implementation details.

Components are part of [packages](/docs/iac/concepts/packages/), which are the distributable unit. A single package can contain multiple components alongside other resources and utilities.

For example, the [AWSx](/registry/packages/awsx/) package contains many components, including:

- `awsx.ec2.Vpc` — creates a complete VPC with subnets, route tables, and gateways preconfigured to AWS best practices.
- `awsx.ecs.FargateService` — creates an ECS service with a load balancer and all required networking.
- `awsx.ecr.Repository` — creates an ECR repository with image scanning and lifecycle policies.

Your organization might publish a package that contains components like:

- An `AcmeCorpVirtualMachine` component that enforces your company's tagging requirements on every VM it creates.
- A `SecureS3Bucket` component that bakes in encryption, versioning, and access logging so consumers get a compliant bucket by default.

Platform teams can use components to codify infrastructure best practices, security policies, and compliance requirements as reusable building blocks. When published to the [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/), packages containing components become discoverable across the organization and can be consumed by any team without needing to understand the underlying implementation.

{{< notes type="info" >}}
Components are analogous to [Terraform modules](https://developer.hashicorp.com/terraform/language/modules) and [AWS CDK Constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html). Pulumi also lets you consume Terraform modules and CDK constructs directly in your Pulumi programs. See [Use a Terraform Module](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) and [Pulumi CDK Adapter](/docs/iac/clouds/aws/guides/cdk/).
{{< /notes >}}

## Consuming components

How you consume a component depends on how it has been distributed.

### Local components

Components that live in the same repository as your Pulumi program are consumed by importing or referencing the class using your language's standard import mechanism—no additional installation steps are needed.

### Single-language packages

Some components are distributed as standard language packages without cross-language support. Add them to your project via your native package manager:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```bash
npm install @my-org/my-component
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
pip install my-org-my-component
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
go get github.com/my-org/my-component
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
dotnet add package MyOrg.MyComponent
```

{{% /choosable %}}
{{% choosable language java %}}

```xml
<dependency>
    <groupId>com.my-org</groupId>
    <artifactId>my-component</artifactId>
    <version>1.0.0</version>
</dependency>
```

{{% /choosable %}}

{{< /chooser >}}

### Cross-language packages without pre-published SDKs

Components distributed as Pulumi packages can be consumed in any language using the `pulumi package add` command. Pulumi generates an SDK for your language on-the-fly and wires it into your project:

```bash
pulumi package add github.com/my-org/my-component@v1.0.0
```

This pattern is common for components your organization publishes for internal consumption via a Git repository or the [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/).

### Cross-language packages with pre-published SDKs

Some packages with components have pre-generated SDKs published for each language, allowing consumers to install them directly via their native package manager without running `pulumi package add`. Pulumi-published packages such as [AWSx](/registry/packages/awsx/) are distributed this way. Your organization may also opt to publish SDKs for each language.

Add the package to your project using your native package manager:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```bash
npm install @pulumi/awsx
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
pip install pulumi-awsx
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
go get github.com/pulumi/pulumi-awsx/sdk/v3/go/awsx
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
dotnet add package Pulumi.Awsx
```

{{% /choosable %}}
{{% choosable language java %}}

```xml
<dependency>
    <groupId>com.pulumi</groupId>
    <artifactId>awsx</artifactId>
    <version>3.0.0</version>
</dependency>
```

{{% /choosable %}}

{{< /chooser >}}

{{< notes type="info" >}}
The [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/) provides a browsable gallery of all packages in use across your Pulumi Cloud organization, including packages containing components.
{{< /notes >}}

## Example: consuming a component

The `awsx.ec2.Vpc` component from the [AWSx](/registry/packages/awsx/) package is a good example of a component resource. It creates a complete VPC—including subnets, route tables, and internet gateways—behind a simple interface.

After adding the AWSx package (see above), instantiate the component like any other Pulumi resource, passing arguments and resource options:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";

const vpc = new awsx.ec2.Vpc("vpc", {
    subnetSpecs: [
        { type: awsx.ec2.SubnetType.Public, cidrMask: 22 },
        { type: awsx.ec2.SubnetType.Private, cidrMask: 20 },
    ],
}, { protect: true });

export const vpcId = vpc.vpcId;
export const privateSubnetIds = vpc.privateSubnetIds;
export const publicSubnetIds = vpc.publicSubnetIds;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("vpc",
    awsx.ec2.VpcArgs(
        subnet_specs=[
            awsx.ec2.SubnetSpecArgs(type=awsx.ec2.SubnetType.PUBLIC, cidr_mask=22),
            awsx.ec2.SubnetSpecArgs(type=awsx.ec2.SubnetType.PRIVATE, cidr_mask=20),
        ],
    ),
    opts=pulumi.ResourceOptions(protect=True),
)

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-awsx/sdk/v3/go/awsx/ec2"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        vpc, err := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{
            SubnetSpecs: []ec2.SubnetSpecArgs{
                {Type: ec2.SubnetTypePublic, CidrMask: pulumi.IntRef(22)},
                {Type: ec2.SubnetTypePrivate, CidrMask: pulumi.IntRef(20)},
            },
        }, pulumi.Protect(true))
        if err != nil {
            return err
        }

        ctx.Export("vpcId", vpc.VpcId)
        ctx.Export("privateSubnetIds", vpc.PrivateSubnetIds)
        ctx.Export("publicSubnetIds", vpc.PublicSubnetIds)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using System.Collections.Generic;
using Pulumi.Awsx.Ec2.Inputs;
using Ec2 = Pulumi.Awsx.Ec2;

return await Deployment.RunAsync(() =>
{
    var vpc = new Ec2.Vpc("vpc", new()
    {
        SubnetSpecs =
        {
            new SubnetSpecArgs { Type = Ec2.SubnetType.Public, CidrMask = 22 },
            new SubnetSpecArgs { Type = Ec2.SubnetType.Private, CidrMask = 20 },
        },
    }, new ComponentResourceOptions { Protect = true });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
        ["privateSubnetIds"] = vpc.PrivateSubnetIds,
        ["publicSubnetIds"] = vpc.PublicSubnetIds,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import java.util.Arrays;
import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.enums.SubnetType;
import com.pulumi.awsx.ec2.inputs.SubnetSpecArgs;
import com.pulumi.resources.ComponentResourceOptions;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var vpc = new Vpc("vpc",
                VpcArgs.builder()
                    .subnetSpecs(Arrays.asList(
                        SubnetSpecArgs.builder().type(SubnetType.Public).cidrMask(22).build(),
                        SubnetSpecArgs.builder().type(SubnetType.Private).cidrMask(20).build()
                    ))
                    .build(),
                ComponentResourceOptions.builder().protect(true).build());

            ctx.export("vpcId", vpc.vpcId());
            ctx.export("privateSubnetIds", vpc.privateSubnetIds());
            ctx.export("publicSubnetIds", vpc.publicSubnetIds());
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Notice that components are instantiated exactly like any other Pulumi resource: with a name, arguments defined by the component author, and resource options like `protect`.

### Components in `pulumi up` output

When you run `pulumi up`, components appear as a resource tree in the CLI output. Child resources are displayed nested under their parent component, giving you visibility into everything the component created on your behalf:

```output
Updating (dev):
     Type                            Name              Status
 +   pulumi:pulumi:Stack             my-stack          created
 +   └─ awsx:ec2:Vpc                 vpc               created
 +      └─ aws:ec2:Vpc               vpc               created
 +         ├─ aws:ec2:Subnet         vpc-private-1     created
 +         │  └─ aws:ec2:RouteTable  vpc-private-1     created
 +         │     ├─ aws:ec2:Route    vpc-private-1     created
 +         │     └─ aws:ec2:RouteTableAssociation  vpc-private-1  created
 +         └─ aws:ec2:Subnet         vpc-public-1      created
 +            └─ aws:ec2:RouteTable  vpc-public-1      created
 +               ├─ aws:ec2:Route    vpc-public-1      created
 +               └─ aws:ec2:RouteTableAssociation  vpc-public-1   created
```

This tree makes it clear that a single `awsx:ec2:Vpc` component encapsulates multiple AWS resources—subnets, route tables, routes, and associations—that would otherwise need to be defined and managed individually.

### Resource options and component resources

Resource options passed to a component resource do not always behave the same as they do for custom resources. For example, the `provider` option has no effect on a component—use `providers` instead to pass explicit provider configuration to a component's child resources. For a complete list of which options apply to component resources, see [Resource options and component resources](/docs/iac/concepts/resources/options/#resource-options-and-component-resources).

## Authoring a new component resource

To author a new component, either in a program or for a reusable library, create a subclass of [`ComponentResource`](/docs/reference/pkg/python/pulumi/#pulumi.ComponentResource). Inside of its constructor, chain to the base constructor, passing its type string, name, arguments, and options. Also inside of its constructor, allocate any child resources, passing the component resource itself as the [`parent`](/docs/concepts/options/parent) option. Setting `parent` correctly ensures that child resources appear under the component in the resource graph, inherit provider configuration, and are tracked as dependencies of the component.

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
For a complete end-to-end walkthrough of building a component from scratch, including setup, implementation, and publishing, see the [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/) guide.
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
- **Enums**: Enum types are supported in TypeScript and Python:

  **TypeScript:** Both the `enum` keyword and the "as const object pattern" are supported:

  ```typescript
  // Using the enum keyword
  enum MyEnum { Value1 = "Value1", Value2 = "Value2" }

  // or alternatively using a const object
  const MyEnum = { Value1: "Value1", Value2: "Value2" } as const;
  type MyEnum = typeof MyEnum[keyof typeof MyEnum];
  ```

  **Python:** The standard library `enum` module is supported:

  ```python
  from enum import Enum

  class MyEnum(Enum):
      VALUE1 = "Value1"
      VALUE2 = "Value2"
  ```

- **Utility types** (TypeScript): The `Required<T>` and `Partial<T>` utility types are supported.

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

## Creating child resources

Component resources often contain child resources. The names of child resources are often derived from the component resource's name to ensure uniqueness. For example, you might use the component resource's name as a prefix. Also, when constructing a resource, children must be registered as such. To do this, pass the component resource itself as the `parent` option.

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

{{% notes type="warning" %}}
Always set `parent` when creating resources inside a component. Omitting it causes the following problems:

- **Resource graph**: Child resources won't appear under the component in `pulumi preview` and the Pulumi Console, making the resource hierarchy unclear.
- **Provider inheritance**: Child resources won't automatically inherit provider configuration (such as region or credentials) passed to the component via the `providers` option.
- **Dependency tracking**: Other resources that depend on the component won't automatically wait for un-parented resources to finish creating, which can cause race conditions or incomplete deployments.
{{% /notes %}}

## Registering component outputs

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

### What registerOutputs does

The `registerOutputs` call serves two purposes:

1. **Marks the component as fully constructed**: It signals to the Pulumi engine that the component resource has finished registering all its child resources and should be considered complete.
1. **Saves outputs to state**: It saves the component's output properties to the state file so they appear in the Pulumi Console and CLI.

{{% notes type="info" %}}
Calling `registerOutputs` is strongly recommended, even when you have no outputs to register (pass an empty object). Without this call:

- The component will appear as "creating..." in the CLI and Pulumi Console until the entire deployment completes, rather than when the component itself finishes.
- The component's output properties will not be saved to the state file. (Child resource state is unaffected.)
- Resource [hooks](/docs/iac/concepts/resources/options/hooks/) such as `afterCreate` will not fire on the component.
{{% /notes %}}

{{% notes type="info" %}}
**.NET**: Since `pulumi-dotnet` 3.59.0, calling `RegisterOutputs()` without arguments automatically registers all properties decorated with `[Output]`.
{{% /notes %}}

## Inheriting resource providers

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

## Cross-language components

By default, components are authored and consumed in the same programming language by extending the `ComponentResource` class. However, components can also be made available to programs written in other languages. When configured for cross-language support, Pulumi can introspect your component class and automatically generate SDKs for consumption in any Pulumi language.

For detailed information on setting up and using cross-language components, including how to configure `PulumiPlugin.yaml`, define entry points, publish, and consume components, see [Cross-language Components](/docs/iac/concepts/components/cross-language-components/).

For a comparison of all component packaging approaches (single-language, cross-language, and provider-based), see [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/).

## Additional resources

- [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/) — Step-by-step guide to authoring a component from scratch, including setup, implementation, and publishing.
- [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) — How to package and distribute components for use by others.
- [Testing Components](/docs/iac/guides/building-extending/components/testing-components/) — How to write tests for your component resources.
- [Cross-language Components](/docs/iac/concepts/components/cross-language-components/) — How to make your component consumable in any Pulumi language.
- [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/) — How to publish and discover components within your organization.
