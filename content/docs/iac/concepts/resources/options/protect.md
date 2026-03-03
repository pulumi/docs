---
title_tag: "protect | Resource Options"
meta_desc: The protect resource option prevents accidental deletion of a resource by marking it as protected.
title: "protect"
h1: "Resource option: protect"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: protect
    parent: options-concepts
    weight: 130
aliases:
  - /docs/iac/concepts/options/protect/
  - /docs/intro/concepts/resources/options/protect/
  - /docs/concepts/options/protect/
---

The `protect` resource option marks a resource as protected. A protected resource cannot be deleted directly, and it will be an error to do a Pulumi deployment which tries to delete a protected resource for any reason.

To delete a protected resource, it must first be *unprotected*. There are two ways to unprotect a resource:

* Set `protect: false` and then run `pulumi up`
* Use the [`pulumi state unprotect`](/docs/cli/commands/pulumi_state_unprotect) command

Once the resource is unprotected, it can be deleted as part of a following update.

The default is to inherit this value from the parent resource, and `false` for resources without a parent.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let db = new Database("db", {}, { protect: true });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database("db", opts=ResourceOptions(protect=True))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, _ := NewDatabase(ctx, "db", &DatabaseArgs{}, pulumi.Protect(true))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { Protect = true });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .protect(true)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  db:
    type: Database
    options:
      protect: true
```

{{% /choosable %}}

{{< /chooser >}}

## Overriding inherited protection

Child resources inherit the `protect` option from their [parent resource](/docs/iac/concepts/options/parent). When a parent resource has `protect: true`, all of its children are also protected by default. To allow a specific child resource to be deleted independently of its protected parent, explicitly set `protect: false` on that child.

The following example creates a protected parent resource alongside a child resource with protection explicitly disabled:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const parent = new MyResource("parent", {}, { protect: true });
const child = new MyResource("child", {}, { parent: parent, protect: false });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
parent = MyResource("parent", opts=ResourceOptions(protect=True))
child = MyResource("child", opts=ResourceOptions(parent=parent, protect=False))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
parent, _ := NewMyResource(ctx, "parent", &MyResourceArgs{}, pulumi.Protect(true))
child, _ := NewMyResource(ctx, "child", &MyResourceArgs{}, pulumi.Parent(parent), pulumi.Protect(false))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var parent = new MyResource("parent", new MyResourceArgs(),
    new CustomResourceOptions { Protect = true });
var child = new MyResource("child", new MyResourceArgs(),
    new CustomResourceOptions { Parent = parent, Protect = false });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var parent = new MyResource("parent",
    MyResourceArgs.Empty,
    CustomResourceOptions.builder()
        .protect(true)
        .build());
var child = new MyResource("child",
    MyResourceArgs.Empty,
    CustomResourceOptions.builder()
        .parent(parent)
        .protect(false)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  parent:
    type: MyResource
    options:
      protect: true
  child:
    type: MyResource
    options:
      parent: ${parent}
      protect: false
```

{{% /choosable %}}

{{< /chooser >}}

## Applying protection to all resources

There is no built-in configuration flag to mark every resource in a stack as protected. To apply `protect: true` to all resources in a stack, use [stack transforms](/docs/iac/concepts/options/transforms#stack-transforms). A stack transform is a callback that the Pulumi engine invokes for every resource during deployment; it can inspect and modify resource options, including `protect`, before the resource is created or updated.
