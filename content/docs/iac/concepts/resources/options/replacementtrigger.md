---
title_tag: "replacementtrigger | Resource Options"
meta_desc: The replacementTrigger resource option allows finer control over when resources are replaced.
title: "replacementTrigger"
h1: "Resource option: replacementTrigger"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: replacementTrigger
    parent: options-concepts
    weight: 5
aliases:
  - /docs/intro/concepts/resources/options/replacementtrigger/
  - /docs/concepts/options/replacementtrigger/
  - /docs/iac/concepts/options/replacementtrigger/
---

The `replacementTrigger` resource option allows you to force a replace operation on the current resource every time a given value is updated. This value could be a `YYYY-MM` string to make sure the given resource is replaced each month, or a version number to make sure a resource updates when a new version is available.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
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

During each deploy, the value is checked against the previous value of the trigger, and if they don't match, the resource will be marked for replacement. Note that, if either the previous value or the current value is `null`, a replacement operation will not be forced. This means that adding or removing a replacement trigger from a resource will _not_ trigger a replacement - only changing a pre-existing trigger value.