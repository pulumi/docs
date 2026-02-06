---
title: "New in Pulumi IaC: `onError` Resource Hook"
date: 2026-02-06
meta_desc: "You can now use the `onError` resource hook to control the retry behaviour of failing resource registrations"
meta_image: meta.png
authors:
    - tom-harding
tags:
    - features
    - iac
    - releases
social:
    twitter: "New in Pulumi IaC: the new `onError` hook gives you full control over deployment failures"
    linkedin: "Pulumi introduces a new type of resource hook: the `onError` hook, letting you control the retry behaviour of resources that fail to create."
---

Last year, Pulumi IaC introduced the [resource hooks](/blog/resource-hooks/) feature, allowing you to run custom code at different points in the lifecycle of resources. Today, we'd like to talk about the latest addition to these hooks: the `onError` hook.

<!--more-->

## Recovering from errors

A Pulumi program will run for as long as things go according to plan. When an error is encountered, this error is reported back to us with information about what went wrong. However, sometimes, these errors are intermitent or temporary.

For this blog, we'll look at a common example: resource readiness. Often, we want to create resources that depend on things like DNS propagation, or the readiness state of other servers. In these cases, a Pulumi program can fail simply because we executed the program too quickly!

In this case, we often don't want the program to fail - we just want to wait for a period of time and retry the operation. This is where the `onError` hook can help us:

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

        await new Promise((resolve) => setTimeout(resolve, 1000));
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

Each time the operation fails, the new error will be passed along with all the previous attempts' errors (newest first) to the error hook. The hook should then return either true or false to tell Pulumi whether to retry the operation or not. If we decide not to retry the operation, the program will fail as normal, with the most recent error being shown as the reason for failure. What the error hook does is up to you: the number of errors can be used to determine how many times the operation has failed, which means we can implement systems like exponential backoff or maximum retries as error hooks!

## Next steps

This feature is fully supported in our Node, Python, and Go SDKs as of v3.219.0, with .NET support landing in the next release. For more information, see the [hooks documentation](/docs/iac/concepts/resources/options/hooks/). Thanks for reading, and feel free to reach out with any questions via [GitHub](https://github.com/pulumi/pulumi), [X](https://x.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).
