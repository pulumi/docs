---
title: "Pulumi SDK Helper Functions"
meta_desc: A quick look at runtime helper functions for Pulumi.
menu:
  reference:
    name: Pulumi SDK Helper Functions
    weight: 4

---

The Pulumi SDK library includes a number of helper functions for the following actions:

- Getting information about the current deployment
- Using logging information for diagnostics, warnings, or errors pertaining to the deployment
- Serializing Lambdas to turn JavaScript callbacks into data, which can be used as application code

## Getting the Current Project or Stack

The {{< pulumi-getproject >}} and {{< pulumi-getstack >}} functions give you the currently deploying project and stack, respectively. This can be useful for naming or tagging resources.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let project = pulumi.getProject();
let stack = pulumi.getStack();
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let project = pulumi.getProject();
let stack = pulumi.getStack();
```

{{% /choosable %}}
{{% choosable language python %}}

```python
project = pulumi.get_project()
stack = pulumi.get_stack()
```

{{% /choosable %}}
{{% choosable language go %}}

```go
project := ctx.Project()
stack := ctx.Stack()
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var project = Deployment.Instance.ProjectName;
var stack = Deployment.Instance.StackName;
```

{{% /choosable %}}

{{< /chooser >}}

## Logging

The {{< pulumi-log >}} collection of functions allow you to log diagnostics, warnings, or errors with the Pulumi engine. These are displayed, alongside all other Pulumi output, in the CLI and in the Pulumi Console. They are also logged and stored in case you want to audit or diagnose a past event. They will also be logged and kept for historical purposes if you ever want to use them to audit or diagnose what has transpired.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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

{{< /chooser >}}

## Serializing Lambdas <span class="badge">NODE.JS ONLY</span>

You can create libraries and components that allow the caller to pass in JavaScript callbacks that are invoked at runtime. For example, you can create an AWS Lambda function or an Azure function by providing a JavaScript callback that serves as its implementation.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let bucket = new aws.s3.Bucket("mybucket");
bucket.onObjectCreated("onObject", async (ev) => {
    // This is the code that will be run when the Lambda is invoked (any time an object is added to the bucket).
    console.log(JSON.stringify(ev));
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let bucket = new aws.s3.Bucket("mybucket");
bucket.onObjectCreated("onObject", async (ev: aws.s3.BucketEvent) => {
    // This is the code that will be run when the Lambda is invoked (any time an object is added to the bucket).
    console.log(JSON.stringify(ev));
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# Runtime code provided via callbacks are currently not supported in Python.
#
# See https://github.com/pulumi/pulumi/issues/1535.
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Runtime code provided via callbacks are currently not supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Runtime code provided via callbacks are currently not supported in .NET.
//
// See https://github.com/pulumi/pulumi/issues/3406.
```

{{% /choosable %}}

{{< /chooser >}}

Libraries that use JavaScript callbacks as inputs that are provided as source text to resource construction—such as the Lambda that is created by the `onObjectCreated` function in the previous example—are built on top of the [`pulumi.runtime.serializeFunction`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi/runtime#serializeFunction" >}}) API, which takes a JavaScript `Function` object as input, and returns a `Promise` that contains the serialized form of that function.

Here is what occurs when a function is serialized to text:

1. Any captured variables referenced by the function are evaluated when the function is serialized.
1. The values of those variables are serialized.
1. When the values are objects, all properties and prototype chains are serialized. When the values are functions, those functions are serialized by following these same steps.

See [`Serializing Functions`]({{< relref "/docs/tutorials/aws/serializing-functions" >}}) for more details.
