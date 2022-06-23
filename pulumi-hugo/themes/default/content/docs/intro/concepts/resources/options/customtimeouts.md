---
title: "CustomTimeouts"
meta_desc: The customTimeouts resource option specifies the default retry/timeout behavior for resource provisioning.
menu:
  intro:
    identifier: customTimeouts
    parent: options
    weight: 3
---

The `customTimeouts` resource option provides a set of custom timeouts for `create`, `update`, and `delete` operations on a resource. These timeouts are specified using a duration string such as "5m" (5 minutes), "40s" (40 seconds), or "1d" (1 day). Supported duration units are "ns", "us" (or "µs"), "ms", "s", "m", and "h" (nanoseconds, microseconds, milliseconds, seconds, minutes, and hours, respectively).

For the most part, Pulumi automatically waits for operations to complete and times out appropriately. In some circumstances, such as working around bugs in the infrastructure provider, custom timeouts may be necessary.

This example specifies that the create operation should wait up to 30 minutes to complete before timing out:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("db", {/*...*/},
    { customTimeouts: { create: "30m" } });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("db", {/*...*/},
    { customTimeouts: { create: "30m" } });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(custom_timeouts=CustomTimeouts(create='30m')))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Timeouts(&pulumi.CustomTimeouts{Create: "30m"}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions {
        CustomTimeouts = new CustomTimeouts { Create = TimeSpan.FromMinutes(30) }
    });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .customTimeouts(
            CustomTimeouts.builder()
                .create(Duration.ofMinutes(30))
                .build())
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  db:
    type: Database
    options:
      customTimeouts:
        create: "30m"
```

{{% /choosable %}}

{{< /chooser >}}

{{% notes type="warning" %}}
The `customTimeouts` resource option does not apply to component resources, and will not have the intended effect.
{{% /notes %}}
