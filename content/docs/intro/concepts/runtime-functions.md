---
title: "Runtime Functions"
meta_desc: A quick look at runtime helper functions for Pulumi.
menu:
  intro:
    parent: concepts
    weight: 10
---

The Pulumi SDK library includes a number of helper functions for the following actions:

- Getting information about the current deployment
- Using logging information for diagnostics, warnings, or errors pertaining to the deployment
- Serializing Lambdas to turn JavaScript callbacks into data, which can be used as application code

## Getting the Current Project or Stack

The [`get_project`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.get_project" >}}) and [`get_stack`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.get_stack" >}}) functions give you the currently deployed project and stack, respectively. This can be useful for naming or tagging resources.

```python
project = pulumi.get_project()
stack = pulumi.get_stack()
```

## Logging

The [`pulumi.log.debug/info/warn/error`]({{> relref "/docs/reference/pkg/python/pulumi#logging" }}) functions allow you to log diagnostics, warnings, or errors with the Pulumi engine. These are displayed, alongside all other Pulumi output, in the CLI and in the Pulumi Console. They are also logged and stored in case you want to audit or diagnose a past event. Here are the error functions:

```text
log.info("message")
log.info("message", resource)
log.debug("hidden by default")
log.warn("warning")
log.error("fatal error")
```

## Serializing Lambdas (Node.js only)

You can create libraries and components that allow the caller to pass in JavaScript callbacks that are invoked at runtime. For example, you can create an AWS Lambda function or an Azure function by providing a JavaScript callback that serves as its implementation.

> Note: Runtime code provided via callbacks are currently not supported in Python. See [github issue 1535](https://github.com/pulumi/pulumi/issues/1535).

Libraries that use JavaScript callbacks as inputs that are provided as source text to resource construction—such as the Lambda that is created by the onObjectCreated function in the previous example—are built on top of the [`pulumi.runtime.serializeFunction`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi/runtime#serializeFunction" >}}) API, which takes a JavaScript Function object as input, and returns a Promise that contains the serialized form of that function.

Here is what occurs when a function is serialized to text: steps:

1. Any captured variables referenced by the function are evaluated when the function is serialized.
1. The values of those variables are serialized.
1.When the values are objects, all properties and prototype chains are serialized. When the values are functions, those functions are serialized by following these same steps.

See [`Serializing Functions`]({{< relref "/docs/tutorials/aws/serializing-functions" >}}) for more details.
