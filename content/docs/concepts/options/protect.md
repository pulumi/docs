---
title_tag: "protect | Resource Options"
meta_desc: The protect resource option prevents accidental deletion of a resource by marking it as protected.
title: "protect"
h1: "Resource option: protect"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: protect
    parent: options
    weight: 10
aliases:
- /docs/intro/concepts/resources/options/protect/
---

The `protect` resource option marks a resource as protected. A protected resource cannot be deleted directly, and it will be an error to do a Pulumi deployment which tries to delete a protected resource for any reason.

To delete a protected resource, it must first be *unprotected*.  There are two ways to unprotect a resource:

* Set `protect: false` and then run `pulumi up`
* Use the [`pulumi state unprotect`](/docs/cli/commands/pulumi_state_unprotect) command

Once the resource is unprotected, it can be deleted as part of a following update.

The default is to inherit this value from the parent resource, and `false` for resources without a parent.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("db", {}, { protect: true});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("db", {}, { protect: true});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database("db", opts=ResourceOptions(protect=True))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, _ := NewDatabase(ctx, "db", &DatabaseArgs{}, pulumi.Protect(true));
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
  type: Database
  options:
    protect: true
```

{{% /choosable %}}

{{< /chooser >}}
