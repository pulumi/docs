---
title_tag: "Resource Names"
meta_desc: A resource in Pulumi has a logical name (in Pulumi) and a physical name (in the cloud provider). Learn more about resource names and how to use them here.
title: Names
h1: Resource names
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    parent: resources
    weight: 1
aliases:
- /docs/intro/concepts/resources/names/
---

Each resource in Pulumi has a [logical name](#logicalname) and a [physical name](#autonaming).  The logical name is how the resource is known inside Pulumi, and establishes a notion of identity within Pulumi even when the physical resource might need to change (for example, during a replacement).  The physical name is the name used for the resource in the cloud provider that a Pulumi program is deploying to.

Pulumi [auto-names](#autonaming) most resources by default, using the logical name and a random suffix to construct a unique physical name for a resource.  Users can provide explicit names to override this default.

Each resource also has a [Uniform Resource Name (URN)](#urns) which is a unique name derived from both the logical name of the resource and the type of the resource and, in the case of components, its parents.

{{% notes type="warning" %}}

Be careful when you change a resource’s name because changing the name of a resource will create a new resource and delete the old/original resource. If you’d like to rename a resource without destroying the old one, refer to the [aliases](/docs/concepts/options/aliases/) resource option.

{{% /notes %}}

## Logical Names {#logicalname}

Every resource managed by Pulumi has a logical name that you specify as an argument to its constructor. For instance, the logical name of this IAM role is `my-role`:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let role = new aws.iam.Role("my-role");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let role = new aws.iam.Role("my-role");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = iam.Role("my-role")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("my-role");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var role = new com.pulumi.aws.iam.Role("my-role");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  my-role:
    type: aws:iam:Role
```

{{% notes type="info" %}}

In Pulumi YAML, you always use the logical name of a resource (e.g., my-role in the above)
to refer to it. There are no distinct variable names, as there are in other languages.

{{% /notes %}}

{{% /choosable %}}

{{< /chooser >}}

The logical name you specify during resource creation is used in two ways:

- As a default prefix for the resource’s physical name, assigned by the cloud provider.
- To construct the [Universal Resource Name (URN)](#urns) used to track the resource across updates.

Pulumi uses the logical name to track the identity of a resource through multiple deployments of the same program and uses it to choose between creating new resources or updating existing ones.

The variable names assigned to resource objects are not used for either logical or physical resource naming. The variable only refers to that resource in the program. For example, in this code:

```typescript
var foo = new aws.Thing("my-thing");
```

The variable name `foo` has no bearing at all on the resulting infrastructure. You could change it to another name, run `pulumi up`, and the result would be no changes. The only exception is if you export that variable, in which case the name of the export would change to the new name.

## Physical Names and Auto-Naming {#autonaming}

A resource’s logical and physical names may not match. In fact, most physical resource names in Pulumi are, by default, auto-named. As a result, even if your IAM role has a logical name of `my-role`, the physical name will typically look something like `my-role-d7c2fa0`. The suffix appended to the end of the name is random.

This random suffix serves two purposes:

- It ensures that two stacks for the same project can be deployed without their resources colliding. The suffix helps you to create multiple instances of your project more easily, whether because you want, for example, many development or testing stacks, or to scale to new regions.
- It allows Pulumi to do zero-downtime resource updates. Due to the way some cloud providers work, certain updates require replacing resources rather than updating them in place. By default, Pulumi creates replacements first, then updates the existing references to them, and finally deletes the old resources.

For cases that require specific names, you can override auto-naming by specifying a physical name. Most resources have a `name` property that you can use to name the resource yourself. Specify your name in the argument object to the constructor. Here’s an example.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let role = new aws.iam.Role("my-role", {
    name: "my-role-001",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let role = new aws.iam.Role("my-role", {
    name: "my-role-001",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = iam.Role('my-role', name='my-role-001')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
    Name: pulumi.String("my-role-001"),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
{
    Name = "my-role-001",
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var role = new com.pulumi.aws.iam.Role("my-role",
    com.pulumi.aws.iam.RoleArgs.builder()
        .name("my-role-001")
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
    role:
        type: aws:iam:Role
        properties:
            name: my-role-001
```

{{% /choosable %}}

{{< /chooser >}}

If the `name` property is not available on a resource, consult the [Registry](/registry/) for the specific resource you are creating. Some resources use a different property to override auto-naming. For instance, the `aws.s3.Bucket` type uses the property `bucket` instead of name. Other resources, such as `aws.kms.Key`, do not have physical names and use other auto-generated IDs to uniquely identify them.

Overriding auto-naming makes your project susceptible to naming collisions. As a result, for resources that may need to be replaced, you should specify `deleteBeforeReplace: true` in the resource’s options. This option ensures that old resources are deleted before new ones are created, which will prevent those collisions.

Because physical and logical names do not need to match, you can construct the physical name by using your project and stack names. Similarly to auto-naming, this approach protects you from naming collisions while still having meaningful names. Note that `deleteBeforeReplace` is still necessary:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let role = new aws.iam.Role("my-role", {
    name: "my-role-" + pulumi.getProject() + "-" + pulumi.getStack(),
}, { deleteBeforeReplace: true });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let role = new aws.iam.Role("my-role", {
    name: `my-role-${pulumi.getProject()}-${pulumi.getStack()}`,
}, { deleteBeforeReplace: true });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = iam.Role(
    'my-role',
    name=f'my-role-{ pulumi.get_project() }-{ pulumi.get_stack() }',
    opts=ResourceOptions(delete_before_replace=True),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, _ := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
    Name: fmt.Sprintf("my-role-%s-%s", ctx.Project(), ctx.Stack()),
}, pulumi.DeleteBeforeReplace(true))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
    {
        Name = string.Format($"my-role-{Deployment.Instance.ProjectName}-{Deployment.Instance.StackName}"),
    },
    new CustomResourceOptions { DeleteBeforeReplace = true }
);
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var role = new com.pulumi.aws.iam.Role("my-role",
    com.pulumi.aws.iam.RoleArgs.builder()
        .name(String.format("my-role-%s-%s", ctx.projectName(), ctx.stackName()))
        .build(),
    CustomResourceOptions.builder()
        .deleteBeforeReplace(true)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  role:
    type: aws:iam:Role
    properties:
      name: my-role${pulumi.project}-${pulumi.stack}
    options:
      deleteBeforeReplace: true
```

{{% /choosable %}}

{{< /chooser >}}

## Resource Types {#types}

Each resource is an instance of a specific Pulumi resource type.  This type is specified by a type token in the format `<package>:<module>:<typename>`.  Concrete examples of this format are:

- `aws:s3/bucket:Bucket`
- `azure-native:compute:VirtualMachine`
- `kubernetes:apps/v1:Deployment`
- `random:index:RandomPassword`

The `<package>` component of the type (e.g. `aws`, `azure-native`, `kubernetes`, `random`) specifies which [Pulumi Package](/docs/using-pulumi/pulumi-packages/) defines the resource.  This is mapped to the package in the [Pulumi Registry](/registry/) and to the underlying [Resource Provider](/docs/concepts/resources/providers/).

The `<module>` component of the type (e.g. `s3/bucket`, `compute`, `apps/v1`, `index`) is the module path where the resource lives within the package.  It is `/` delimited by component of the path.  Per-language Pulumi SDKs use the module path to emit nested namespaces/modules in a language-specific way to organize all the types defined in a package.  For example, the `Deployment` resource above is available at `kubernetes.apps.v1.Deployment` in TypeScript and in the `github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1` module in Go.  For historical reasons only, some packages include the type name itself as a final component of the module (e.g. `s3/bucket` for the type name `Bucket`) - in this case, this component is not included in the SDK namespace.  The name `index` indicates that the resource is not nested, and is instead available at the top level of the package.  For example, the `RandomPassword` resource above is available at `random.RandomPassword` in TypeScript.

The `<typename>` component of the type (e.g. `Bucket`, `VirtualMachine`, `Deployment`, `RandomPassword`) is the identifier used to refer to the resource itself.  It is mapped to the class or constructor name in the per-language Pulumi SDK.

Note that because of some of the historical details of how `<module>` is defined, a "simplified" resource type name is accepted or presented in certain places, and mapped into the "full" resource type name specified above.  The simplified resource type name applies the following rules:

1. If the type token is two components instead of three, that is `<package>:<typename>`, it is interpreted as if it was `<package>:index:<typename>`.
2. The repetition of the `<typename>` as part of the module definition is not required, and will be inferred if necessary - that is `aws:s3:Bucket` will be interpreted as referring to `aws:s3/bucket:Bucket`.

This "simplified" type name format is currently used in the following places:

- The [Pulumi YAML](/docs/languages-sdks/yaml/) language allows simple type names to be used as the `type` of a resource.

The examples above can be written in simplified form as:

- `aws:s3:Bucket`
- `azure-native:compute:VirtualMachine`
- `kubernetes:apps/v1:Deployment`
- `random:RandomPassword`

## Resource URNs {#urns}

Each resource is assigned a [Uniform Resource Name (URN)](https://en.wikipedia.org/wiki/Uniform_Resource_Name) that uniquely identifies that resource globally. Unless you are writing a tool, you will seldom need to interact with an URN directly, but it is fundamental to how Pulumi works so it’s good to have a general understanding of it.

The URN is automatically constructed from the project name, stack name, resource name, resource type, and the types of all the parent resources (in the case of [component resources](/docs/concepts/resources/components/)).

The following is an example of a URN:

```text
urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket
           ^^^^^^^^^^  ^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^
           <stack-name> <project-name>   <parent-type>             <resource-type>       <resource-name>
```

The type components of the URN are [resource types](#types) as defined above, and the full type in the URN is a `$` delimited path of the parent chain of resource types that the resource is nested within (up to and excluding the root Stack resource).

The URN must be globally unique. This means all of the components that go into a URN must be unique within your program. If you create two resources with the same name, type, and parent path, for instance, you will see an error:

```bash
error: Duplicate resource URN 'urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket'; try giving it a unique name
```

Any change to the URN of a resource causes the old and new resources to be treated as unrelated—the new one will be created (since it was not in the prior state) and the old one will be deleted (since it is not in the new desired state). This behavior happens when you change the `name` used to construct the resource or the structure of a resource’s parent hierarchy.

Both of these operations will lead to a different URN, and thus require the `create` and `delete` operations instead of an `update` or `replace` operation that you would use for an existing resource.

Resources constructed as children of a component resource should ensure their names are unique across multiple instances of the component resource. In general, the name of the component resource instance itself (the `name` parameter passed into the component resource constructor) should be used as part of the name of the child resources.
