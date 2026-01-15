---
title: "New in Pulumi IaC: `replacementTrigger` Resource Option"
date: 2026-01-19
meta_desc: "You can now use the `replacementTrigger` resource option to control when resources are recreated"
meta_image: meta.png
authors:
    - tom-harding
tags:
    - features
    - iac
    - releases
social:
    twitter: "New in Pulumi IAC: Use the `replacementTrigger` resource option to control redeployments of your infrastructure resources."
    linkedin: "Pulumi introduces a powerful new feature for fine-grained control over infrastructure deployment: the `replacementTrigger` resource option. Now you can override the replacement mechanism in the Pulumi engine to enable finer control over features like key cycling and versioning.
---

# New in Pulumi IaC: `replacementTrigger` Resource Option

Pulumi IaC gives us a declarative interface to deployments. When we perform a deploy, Pulumi calculates the difference between your currently deployed infrastructure and what is being proposed, then deploys only what is required to migrate from the old state to the new state. Normally, this is exactly what we want: we minimise the amount of work required to perform the deploy, and don’t recreate anything unnecessarily. However, every now and then, we want to override this behaviour.

Recently, we talked about the new [`replaceWith`](https://www.pulumi.com/blog/dependent-resource-replacements/) option, which allows us to tell Pulumi that any replacement of one resource should always trigger a replacement of another (for example, if the database is replaced, we should re-deploy our application server). Today, we’re going to take this idea one step further and talk about another new feature that gives us even more control over this process: replacement triggers.

<!--more-->

## Forcing redeployments

Let’s imagine we have a resource that, upon deployment, generates some private keys. If that’s all the resource does, it probably isn’t ever going to change as far as Pulumi’s concerned: we wanted the resource before, and we want it after, so there is no change and no need to replace the resource that is already live. Now, let’s imagine that we want to cycle these private keys every month. How do we tell Pulumi that, if this deployment happens more than two weeks after the last time this resource was deployed, we want to recreate it?

As another example, perhaps we want to replace a resource every time some external version number is bumped. Let’s imagine a documentation server may need to be redeployed every time a new version of an API is made available. We could use the `--replace` flag each time, but this process is error prone to do manually, and would incur a maintenance burden to automate.

## Defining replacement triggers

In essence, a replacement trigger is just a value attached to the resource as metadata. However, whenever this value changes between deployments, it will trigger a replace operation on the given resource, regardless of whether anything else has changed.

Let’s take our previous example: we want something to be replaced every month. With replacement triggers, we can solve this by representing the current year and month as as a string:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```javascript
...

const today = new Date()

const keyManager = new KeyManagerResource("key-manager", {}, {
  replacementTrigger: today.getMonth() + '-' + today.getFullYear()
});

...
```

{{% /choosable %}}
{{% choosable language python %}}

```py
...

today = datetime.now()
trigger = f"{today.month}-{today.year}"

key_manager = KeyManagerResource("key-manager", {},
    opts=pulumi.ResourceOptions(replacement_trigger=trigger))

...
```

{{% /choosable %}}
{{% choosable language go %}}

```go
...

today := time.Now()
trigger := fmt.Sprintf("%d-%d", int(today.Month()), today.Year())

keyManager, err := NewKeyManagerResource(ctx, "key-manager", &KeyManagerResourceArgs{},
    pulumi.ReplacementTrigger(pulumi.Any(trigger)))

...
```

{{% /choosable %}}
{{% choosable language java %}}

```java
...

var today = LocalDate.now();
var trigger = String.format("%d-%d", today.getMonthValue(), today.getYear())

var keyManager = new KeyManagerResource("key-manager",
    KeyManagerResourceArgs.Empty,
    CustomResourceOptions.builder()
        .replacementTrigger(Output.of(trigger))
        .build());

...
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
...

var today = DateTime.Now;
var trigger = $"{today.Month}-{today.Year}";

var keyManager = new KeyManagerResource("key-manager", new KeyManagerResourceArgs(),
    new CustomResourceOptions
    {
        ReplacementTrigger = Output.Create(trigger)
    });

...
```

{{% /choosable %}}
{{< /chooser >}}

When we run this deploy for the first time, the replacement trigger will be persisted to the Pulumi state. Each time we run a deploy, we’ll re-calculate the date string, and compare it against the current string. Finally, when we run the deploy again next month, and the date string no longer matches, our `key-manager` will be replaced and our new keys will be generated\!

## Next steps

This feature is fully supported across all our SDKs as of v3.215.0. Thanks for reading, and feel free to reach out with any questions via [GitHub](https://github.com/pulumi/pulumi), [X](https://x.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).