---
title: "New in Pulumi IaC: `onError` Resource Hook"
date: 2026-02-06
meta_desc: "You can now use the `onError` resource hook to control the retry behavior of failing resource registrations"
meta_image: meta.png
authors:
    - tom-harding
tags:
    - features
    - iac
    - releases
social:
    twitter: "New in Pulumi IaC: the `onError` hook gives you full control over deployment failures"
    linkedin: "Pulumi introduces a new type of resource hook: the `onError` hook, letting you control the retry behavior of resources that fail to create."
---

You can now control what happens when a resource fails during create, update, or delete—retry with backoff, fail fast, or handle errors in custom code. Last year, Pulumi IaC introduced the [resource hooks](/blog/resource-hooks/) feature, allowing you to run custom code at different points in the lifecycle of resources. Today we're adding the `onError` hook so you can react when operations fail.

<!--more-->

## Recovering from errors

When a Pulumi program encounters an error while creating, updating, or deleting a resource, the operation halts and the error is reported back. Sometimes that's not what we want—errors can be intermittent or temporary. If you've hit transient failures or resource-not-ready errors, the `onError` hook can help.

A common case is resource readiness: creating resources that depend on DNS propagation or the readiness of other servers. The program can fail simply because it ran too soon. Instead of failing, we can wait and retry. The example below shows how:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const notStartedRetryHook = new pulumi.ErrorHook(
    "retry-when-not-started",
    async (args) => {
        const latestError = args.errors[0] ?? "";

        if (!latestError.includes("resource has not yet started")) {
          return false; // do not retry, this is another type of error
        }

        await new Promise((resolve) => setTimeout(resolve, 5000));
        return true; // retry
    },
);

const res = new MyResource("res", {}, {
    hooks: {
        onError: [notStartedRetryHook],
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import time

import pulumi


def retry_when_not_started(args: pulumi.ErrorHookArgs) -> bool:
    latest_error = args.errors[0] if args.errors else ""

    if "resource has not yet started" not in latest_error:
        return False # do not retry, this is another type of error

    time.sleep(5)
    return True # retry


not_started_retry_hook = pulumi.ErrorHook(
    "retry-when-not-started",
    retry_when_not_started,
)

res = MyResource(
    "res",
    opts=pulumi.ResourceOptions(
        hooks=pulumi.ResourceHookBinding(
            on_error=[not_started_retry_hook],
        ),
    ),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "strings"
    "time"

    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        hook, err := ctx.RegisterErrorHook(
            "retry-when-not-started",
            func(args *pulumi.ErrorHookArgs) (bool, error) {
                latest := ""
                if len(args.Errors) > 0 {
                    latest = args.Errors[0]
                }

                if !strings.Contains(latest, "resource has not yet started") {
                    return false, nil // do not retry, this is another type of error
                }

                time.Sleep(5 * time.Second)
                return true, nil // retry
            },
        )
        if err != nil {
            return err
        }

        _, err = NewMyResource(ctx, "res", &MyResourceArgs{}, pulumi.ResourceHooks(&pulumi.ResourceHookBinding{
            OnError: []*pulumi.ErrorHook{hook},
        }))
        if err != nil {
            return err
        }

        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System;
using System.Threading;
using System.Threading.Tasks;
using Pulumi;

class ErrorHookStack : Stack
{
    public ErrorHookStack()
    {
        var retryHook = new ErrorHook(
            "retry-when-not-started",
            async (args, cancellationToken) =>
            {
                var latestError = args.Errors.Count > 0 ? args.Errors[0] : "";

                if (!latestError.Contains("resource has not yet started"))
                {
                    return false; // do not retry, this is another type of error
                }

                await Task.Delay(TimeSpan.FromSeconds(5), cancellationToken);
                return true; // retry
            });

        var res = new MyResource("res", new MyResourceArgs(), new CustomResourceOptions
        {
            Hooks = new ResourceHookBinding
            {
                OnError = { retryHook },
            },
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Each time the operation fails, the hook receives the new error plus all previous attempts' errors (newest first). The hook returns true or false to tell Pulumi whether to retry. If you return false, the program fails as normal with the most recent error. With that information, you can implement many failure models:

1. Use the number of errors to implement backoff—for example, wait one second on the first failure, two seconds on the second, and so on.
1. For known-intermittent resources, always retry once before failing.
1. Inspect error text to retry only for specific conditions (as in the example) and fail fast for others.

The callback runs in your language of choice, so you have full control over how failures are handled.

## Next steps

This feature is fully supported in our Node, Python, Go, and .NET SDKs as of v3.219.0. For more information, see the [hooks documentation](/docs/iac/concepts/resources/options/hooks/). Thanks for reading, and feel free to reach out with any questions via [GitHub](https://github.com/pulumi/pulumi), [X](https://x.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).
