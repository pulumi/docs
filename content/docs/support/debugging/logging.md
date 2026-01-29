---
title_tag: "Logging in Pulumi for Debugging"
meta_desc: "Learn about logging in Pulumi including CLI verbose logging for troubleshooting and program logging for diagnostics."
title: Logging
h1: Logging
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    support:
        name: Logging
        parent: support-debugging
        weight: 5
        identifier: support-debugging-logging
aliases:
- /docs/intro/concepts/logging/
- /docs/concepts/logging/
- /docs/iac/concepts/logging/
- /docs/iac/troubleshooting/debugging/logging/
---

Pulumi provides two main types of logging to help with debugging and troubleshooting: CLI logging for diagnosing Pulumi engine operations and program logging for emitting custom diagnostics from your Pulumi programs.

## CLI verbose logging

Verbose logging of the internals of the Pulumi engine and resource providers can be enabled by passing the `-v` flag to any `pulumi` CLI command. Pulumi emits logs at log levels between `1` and `11`, with `11` being the most verbose. At log level 10 or below, Pulumi will avoid intentionally exposing any *known* credentials. At log level 11, Pulumi will intentionally expose some known credentials to aid with debugging, so these log levels should be used only when absolutely needed.

By default, logs are written to the top-level temp directory (usually `/tmp` or the value of `$TMPDIR`). The following flags control logging behavior:

* `--logtostderr`: Write logs to stderr instead of temp files.
* `--logflow`: Pass the same log level to resource providers. Without this flag, only the Pulumi engine logs at the specified verbosity level, while resource providers use their default log level.

The `--logflow` flag is particularly useful when debugging cloud provider API interactions. At high verbosity levels (such as `-v=9`), resource providers will log HTTP requests and responses to their cloud APIs. This helps diagnose issues like incorrect resource references, unexpected 404 errors, or API parameter problems.

{{% notes type="warning" %}}
Enabling verbose logging may reveal sensitive information (tokens, credentials...) that is provided from your execution environment directly to your cloud provider, and which Pulumi may not be aware of. Before sharing the logs, be careful to audit and redact any sensitive information.
{{% /notes %}}

```bash
$ pulumi up --logtostderr --logflow -v=9 2> out.txt
```

Diagnostic logging can also be controlled with flags and environment variables of the resource providers. For example, Pulumi providers that use a bridged Terraform provider can make use of the [`TF_LOG`](https://www.terraform.io/docs/internals/debugging.html) environment variable (set to `TRACE`, `DEBUG`, `INFO`, `WARN` or `ERROR`) in order to provide additional diagnostic information.

```bash
$ TF_LOG=TRACE pulumi up --logtostderr --logflow -v=10 2> out.txt
```

## Program logging

In addition to CLI logging, you can emit custom log messages from within your Pulumi programs using the logging functions provided by the Pulumi SDK. These messages are displayed alongside all other Pulumi output in the CLI and in Pulumi Cloud, and are logged and kept for historical purposes.

{{< chooser language "typescript,python,go,csharp,java" >}}

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
pulumi.info("message")
pulumi.info("message", resource)
pulumi.debug("hidden by default")
pulumi.warn("warning")
pulumi.error("fatal error")
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
    ctx.log().info("message");
    ctx.log().info("message", resource);
    ctx.log().debug("hidden by default");
    ctx.log().warn("warning");
    ctx.log().error("fatal error");
}
```

{{% /choosable %}}

{{< /chooser >}}

{{% notes type="tip" %}}
Debug log messages from your program are hidden by default. To see them use the `-d` or `--debug` flag when running the `pulumi up`, `pulumi preview`, `pulumi destroy`, `pulumi import`, `pulumi refresh`, or `pulumi watch` commands.
{{% /notes %}}

## Combining CLI and program logging

When troubleshooting issues, you may want to use both CLI verbose logging and program logging together:

```bash
# Enable both CLI verbose logging and program debug logging
$ pulumi up --logtostderr --logflow -v=9 -d 2> out.txt
```

This combination provides the most comprehensive view of what's happening during your Pulumi operations, showing both engine internals and your custom program diagnostics.

## Debugging cloud provider API calls

When you encounter errors from cloud providers (such as 404 responses or permission issues), the verbose logs can help you see exactly what API calls are being made. For example:

```bash
$ pulumi up --logtostderr --logflow -v=9 2>&1 | grep -i "http"
```

This is particularly useful for debugging scenarios where:

* A resource property expects a name versus a fully qualified ID
* You're getting generic errors without clear root causes
* You need to verify the exact API endpoints being called
