---
title: "Logging"
meta_desc: An overview of the Pulumi logging functionality used for debugging and diagnostics.
menu:
  intro:
    parent: concepts
    weight: 9
---

The {{< pulumi-log >}} collection of functions allow you to log diagnostics, warnings, or errors with the Pulumi engine. These are displayed, alongside all other Pulumi output, in the CLI and in the Pulumi Service. Events are logged and kept for historical purposes in case you want to audit or diagnose a past event.

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
pulumi.log.info("message")
pulumi.log.info("message", resource)
pulumi.log.debug("hidden by default")
pulumi.log.warn("warning")
pulumi.log.error("fatal error")
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
pulumi.log.info("message")
pulumi.log.info("message", resource)
pulumi.log.debug("hidden by default")
pulumi.log.warn("warning")
pulumi.log.error("fatal error")
```

{{% /choosable %}}
{{% choosable language python %}}

```python
log.info("message")
log.info("message", resource)
log.debug("hidden by default")
log.warn("warning")
log.error("fatal error")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Optional arguments for logging.
args := &pulumi.LogArgs{
    Resource: resource,
    StreamID: 0,
    Ephemeral: false,
}

ctx.Log.Info("message", nil)
ctx.Log.Info("message", args)
ctx.Log.Debug("hidden by default", nil)
ctx.Log.Warn("warning", nil)
ctx.Log.Error("fatal error", nil)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
Pulumi.Log.Info("message");
Pulumi.Log.Info("message", resource);
Pulumi.Log.Debug("hidden by default");
Pulumi.Log.Warn("warning");
Pulumi.Log.Error("fatal error");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
public static void stack(Context ctx) {
    ctx.log.info("message");
    ctx.log.info("message", resource);
    ctx.log.debug("hidden by default");
    ctx.log.warn("warning");
    ctx.log.error("fatal error");
}
```

{{% /choosable %}}

{{< /chooser >}}

For information on how to use diagnostic information for troubleshooting, see [Diagnosing Issues]({{< relref "/docs/support/troubleshooting#diagnosing-issues" >}}).
