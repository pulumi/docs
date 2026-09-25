---
title_tag: "retainOnDelete | Resource Options"
meta_desc: The `retainOnDelete` resource option marks a resource to be retained during a delete operation.
title: "retainOnDelete"
h1: "Resource option: retainOnDelete"
menu:
  iac:
    identifier: retainOnDelete
    parent: options-concepts
    weight: 190
aliases:
  - /docs/intro/concepts/resources/options/retainondelete/
  - /docs/concepts/options/retainondelete/
  - /docs/iac/concepts/options/retainondelete/
  - /docs/iac/concepts/options/retainOnDelete/
---

The `retainOnDelete` resource option marks a resource to be retained. If this option is set, Pulumi does not call through to the resource provider's `Delete` method when deleting or replacing the resource during `pulumi up` or `pulumi destroy`. As a result, the resource is not deleted from the backing cloud provider, but is removed from the Pulumi state.

{{< resource-option-scope "retainOnDelete" >}}

For a complete walkthrough of using this option to remove a resource from a stack without deleting the underlying infrastructure, including how it compares to `pulumi state delete`, see [Removing resources without deleting them](/docs/iac/operations/stack-management/removing-resources-without-deleting-them/).

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const db = new Database("db", {}, { retainOnDelete: true });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database("db", opts=ResourceOptions(retain_on_delete=True))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, _ := NewDatabase(ctx, "db", &DatabaseArgs{}, pulumi.RetainOnDelete(true))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { RetainOnDelete = true });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .retainOnDelete(true)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  db:
    type: Database
    options:
      retainOnDelete: true
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "database" "db" {
  # ...

  pulumi {
    retain_on_delete = true
  }
}
```

{{% /choosable %}}

{{< /chooser >}}

## Deleting a retained resource

To delete a retained resource from the backing cloud provider, first set `retainOnDelete: false` and run `pulumi up`. Once the resource is no longer marked retained, a later update that removes it, or `pulumi destroy`, deletes it fully.

If Pulumi has already removed a retained resource from the stack, the resource still exists in the cloud provider. To delete it, either use the provider's console or CLI, or [import](/docs/iac/concepts/resources/options/import/) it back into Pulumi, unset `retainOnDelete`, and delete it again.

## Inheritance from parent

`retainOnDelete` is inherited from a resource's [`parent`](/docs/iac/concepts/resources/options/parent/), and defaults to `false` for resources without a parent. Setting `retainOnDelete` on a parent retains every descendant in the resource tree, which makes it the way to retain all of the resources in a [component resource](/docs/iac/concepts/components/).

Because a component has no infrastructure of its own in the cloud provider, setting `retainOnDelete` on a component has no direct effect on the component. Its effect comes entirely from propagating the value to the component's children.

A child can override an inherited value by setting `retainOnDelete` explicitly. For example, set `retainOnDelete: false` on a child to delete it normally even though its parent is retained. For the full list of options children inherit, see [Inherited resource options](/docs/iac/concepts/resources/options/parent/#inherited-resource-options).
