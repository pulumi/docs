---
title: "Resource Names"
meta_desc: A resource in Pulumi has a logical name (in Pulumi) and a physical name (in the cloud provider).
menu:
  intro:
    parent: resources
    weight: 1
---

Each resources in Pulumi has a [logical name]({{< relref "#logicalname" >}}) and a [physical name]({{< relref "#autonaming" >}}).  The logical name is how the resource is known inside Pulumi, and establishes a notion of identity within Pulumi even when the physical resource might need to change (for example, during a replacement).  The physical name is the name used for the resource in the cloud provider that a Pulumi program is deploying to.

Pulumi [auto-names](({{< relref "#autonaming" >}})) most resource by default, using the logical name and a random suffix to construct a unique physical name for a resource.  Users can provide explicit names to override this default.

Each resource also has a [Uniform Resource Name (URN)]({{< relref "#urns" >}}) which is a unique name derived from both the logical name of the resource and the type of the resource and, in the case of components, its parents.

## Logical Names {#logicalname}

Every resource managed by Pulumi has a logical name that you specify as an argument to its constructor. For instance, the logical name of this IAM role is `my-role`:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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

{{< /chooser >}}

The logical name you specify during resource creation is used in two ways:

- As a default prefix for the resource’s physical name, assigned by the cloud provider.
- To construct the [Universal Resource Name (URN)]({{< relref "#urns" >}}) used to track the resource across updates.

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

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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
role = iam.Role('my-role', {
    name='my-role-001'
})
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

{{< /chooser >}}

If the `name` property is not available on a resource, consult the [Registry]({{< relref "/registry" >}}) for the specific resource you are creating. Some resources use a different property to override auto-naming. For instance, the `aws.s3.Bucket` type uses the property `bucket` instead of name. Other resources, such as `aws.kms.Key`, do not have physical names and use other auto-generated IDs to uniquely identify them.

Overriding auto-naming makes your project susceptible to naming collisions. As a result, for resources that may need to be replaced, you should specify `deleteBeforeReplace: true` in the resource’s options. This option ensures that old resources are deleted before new ones are created, which will prevent those collisions.

Because physical and logical names do not need to match, you can construct the physical name by using your project and stack names. Similarly to auto-naming, this approach protects you from naming collisions while still having meaningful names. Note that `deleteBeforeReplace` is still necessary:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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
role = iam.Role('my-role', {
    name='my-role-{}-{}'.format(pulumi.get_project(), pulumi.get_stack())
}, opts=ResourceOptions(delete_before_replace=True))
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

{{< /chooser >}}

## Resource URNs {#urns}

Each resource is assigned a [Uniform Resource Name (URN)](https://en.wikipedia.org/wiki/Uniform_Resource_Name) that uniquely identifies that resource globally. Unless you are writing a tool, you will seldom need to interact with an URN directly, but it is fundamental to how Pulumi works so it’s good to have a general understanding of it.

The URN is automatically constructed from the project name, stack name, resource name, resource type, and the types of all the parent resources (in the case of [component resources]({{< relref "components" >}})).

The following is an example of a URN:

```text
urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket
           ^^^^^^^^^^  ^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^
           <stack-name> <project-name>   <parent-type>             <resource-type>       <resource-name>
```

The URN must be globally unique. This means all of the components that go into a URN must be unique within your program. If you create two resources with the same name, type, and parent path, for instance, you will see an error:

```bash
error: Duplicate resource URN 'urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket'; try giving it a unique name
```

Any change to the URN of a resource causes the old and new resources to be treated as unrelated—the new one will be created (since it was not in the prior state) and the old one will be deleted (since it is not in the new desired state). This behavior happens when you change the `name` used to construct the resource or the structure of a resource’s parent hierarchy.

Both of these operations will lead to a different URN, and thus require the `create` and `delete` operations instead of an `update` or `replace` operation that you would use for an existing resource. In other words, be careful when you change a resource’s name.

{{% notes "info" %}}
If you’d like to rename a resource without destroying the old one, refer to the [aliases]({{< relref "options/aliases" >}}) resource option.
{{% /notes %}}

Resources constructed as children of a component resource should ensure their names are unique across multiple instances of the component resource. In general, the name of the component resource instance itself (the `name` parameter passed into the component resource constructor) should be used as part of the name of the child resources.
