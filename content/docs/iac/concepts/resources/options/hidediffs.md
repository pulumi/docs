---
title_tag: "hideDiffs | Resource Options"
meta_desc: The hideDiffs resource option controls how property diffs are displayed in the CLI.
title: "hideDiffs"
h1: "Resource option: hideDiffs"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: hideDiffs
    parent: options-concepts
    weight: 8
aliases:
  - /docs/iac/concepts/options/hidediffs/
  - /docs/concepts/options/hidediffs/
---

The `hideDiffs` resource option specifies a list of property paths whose diff details Pulumi will compact in CLI output. Setting `hideDiffs` does not affect what resources are updated, only how those updates are displayed.

## How hideDiffs works

When you set `hideDiffs` on a resource property, Pulumi will:

1. Still detect and process all changes to that property during preview and update operations.
1. Compact the diff display in the CLI, hiding the details of what changed within that property.
1. Show that the property changed without expanding the full before/after values.
1. Continue to update the resource normally based on those changes.

This is useful when working with properties that generate large or verbose diffs that clutter CLI output, while still allowing Pulumi to manage those properties normally.

## Example usage

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let res = new MyResource("res",
    { prop: "new-value" }, { hideDiffs: ["prop"] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
res = MyResource("res",
    prop="new-value",
    opts=ResourceOptions(hide_diffs=["prop"]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
res, _ := NewMyResource(ctx, "res",
    &MyResourceArgs{Prop: "new-value"},
    pulumi.HideDiffs([]string{"prop"}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var res = new MyResource("res",
    new MyResourceArgs { Prop = "new-value" },
    new CustomResourceOptions { HideDiffs = { "prop" } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var res = new MyResource("res",
    MyResourceArgs.builder()
        .prop("new-value")
        .build(),
    CustomResourceOptions.builder()
        .hideDiffs("prop")
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  res:
    type: MyResource
    properties:
      prop: new-value
    options:
      hideDiffs:
        - prop
```

{{% /choosable %}}

{{< /chooser >}}

## Property Paths

In addition to passing simple property names, nested properties can also be supplied to hide diffs for a more targeted nested part of the resource's properties. See [property paths](/docs/iac/concepts/inputs-outputs/property-paths/) for examples of legal paths that can be passed to specify nested properties of objects and arrays.

For example, to hide diffs for all weights in an AWS load balancer listener's target groups:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const listener = new aws.lb.Listener("listener", {
    // ... other configuration ...
    defaultActions: [{
        type: "forward",
        forward: {
            targetGroups: [
                { arn: blueGroup.arn, weight: 80 },
                { arn: greenGroup.arn, weight: 20 },
            ],
        },
    }],
}, { hideDiffs: ["defaultActions[*].forward.targetGroups[*].weight"] });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
listener = aws.lb.Listener("listener",
    # ... other configuration ...
    default_actions=[{
        "type": "forward",
        "forward": {
            "target_groups": [
                {"arn": blue_group.arn, "weight": 80},
                {"arn": green_group.arn, "weight": 20},
            ],
        },
    }],
    opts=ResourceOptions(hide_diffs=["defaultActions[*].forward.targetGroups[*].weight"]))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
listener, err := lb.NewListener(ctx, "listener", &lb.ListenerArgs{
    // ... other configuration ...
    DefaultActions: lb.ListenerDefaultActionArray{
        &lb.ListenerDefaultActionArgs{
            Type: pulumi.String("forward"),
            Forward: &lb.ListenerDefaultActionForwardArgs{
                TargetGroups: lb.ListenerDefaultActionForwardTargetGroupArray{
                    &lb.ListenerDefaultActionForwardTargetGroupArgs{
                        Arn:    blueGroup.Arn,
                        Weight: pulumi.Int(80),
                    },
                    &lb.ListenerDefaultActionForwardTargetGroupArgs{
                        Arn:    greenGroup.Arn,
                        Weight: pulumi.Int(20),
                    },
                },
            },
        },
    },
}, pulumi.HideDiffs([]string{"defaultActions[*].forward.targetGroups[*].weight"}))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var listener = new Aws.LB.Listener("listener", new()
{
    // ... other configuration ...
    DefaultActions = new[]
    {
        new Aws.LB.Inputs.ListenerDefaultActionArgs
        {
            Type = "forward",
            Forward = new Aws.LB.Inputs.ListenerDefaultActionForwardArgs
            {
                TargetGroups = new[]
                {
                    new Aws.LB.Inputs.ListenerDefaultActionForwardTargetGroupArgs
                    {
                        Arn = blueGroup.Arn,
                        Weight = 80,
                    },
                    new Aws.LB.Inputs.ListenerDefaultActionForwardTargetGroupArgs
                    {
                        Arn = greenGroup.Arn,
                        Weight = 20,
                    },
                },
            },
        },
    },
}, new CustomResourceOptions { HideDiffs = { "defaultActions[*].forward.targetGroups[*].weight" } });
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var listener = new Listener("listener", ListenerArgs.builder()
    // ... other configuration ...
    .defaultActions(ListenerDefaultActionArgs.builder()
        .type("forward")
        .forward(ListenerDefaultActionForwardArgs.builder()
            .targetGroups(
                ListenerDefaultActionForwardTargetGroupArgs.builder()
                    .arn(blueGroup.arn())
                    .weight(80)
                    .build(),
                ListenerDefaultActionForwardTargetGroupArgs.builder()
                    .arn(greenGroup.arn())
                    .weight(20)
                    .build())
            .build())
        .build())
    .build(),
    CustomResourceOptions.builder()
        .hideDiffs("defaultActions[*].forward.targetGroups[*].weight")
        .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  listener:
    type: aws:lb:Listener
    properties:
      # ... other configuration ...
      defaultActions:
        - type: forward
          forward:
            targetGroups:
              - arn: ${blueGroup.arn}
                weight: 80
              - arn: ${greenGroup.arn}
                weight: 20
    options:
      hideDiffs:
        - defaultActions[*].forward.targetGroups[*].weight
```

{{% /choosable %}}

{{< /chooser >}}

{{% notes type="info" %}}
The `hideDiffs` option only affects CLI display output. It does not change resource update behavior, prevent changes from being detected, or modify what gets stored in state.
{{% /notes %}}

{{% notes type="info" %}}
Unlike `ignoreChanges`, `hideDiffs` does not affect which properties trigger updates. If you want to prevent updates based on property changes, use the [`ignoreChanges`](/docs/concepts/options/ignorechanges/) option instead.
{{% /notes %}}
