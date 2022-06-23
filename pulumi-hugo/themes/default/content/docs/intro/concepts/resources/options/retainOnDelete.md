---
title: "RetainOnDelete"
meta_desc: The `retainOnDelete` resource option marks a resource to be retained during a delete operation.
menu:
  intro:
    identifier: retainOnDelete
    parent: options
    weight: 13
---

The `retainOnDelete` resource option marks a resource to be retained. If this option is set then Pulumi will not call through to the resource provider's `Delete` method when deleting or replacing the resource during `pulumi up` or `pulumi destroy`. As a result, the resource will not be deleted from the backing cloud provider, but will be removed from the Pulumi state.

If a retained resource is deleted by Pulumi and you later want to actually delete it from the backing cloud provider you will either need to use your provider's manual interface to find and delete the resource, or import the resource back into Pulumi to unset `retainOnDelete` and delete it again fully.

To actually delete a retained resource, this setting must first be set to `false`.

* Set `retainOnDelete: false` and then run `pulumi up`

Once the resource is no longer marked retained, it can be fully deleted as part of a following update.

The default is to inherit this value from the parent resource, and `false` for resources without a parent.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("db", {}, { retainOnDelete: true });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("db", {}, { retainOnDelete: true });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database("db", opts=ResourceOptions(retain_on_delete=True))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, _ := NewDatabase(ctx, "db", &DatabaseArgs{}, pulumi.RetainOnDelete(true));
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

{{< /chooser >}}

{{% notes type="warning" %}}
The `retainOnDelete` resource option does not apply to component resources, and will not have the intended effect.
{{% /notes %}}
