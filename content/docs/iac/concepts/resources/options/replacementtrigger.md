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

The `replacementTrigger` resource option forces a replacement operation on a resource whenever a specified trigger value changes. This is useful when you need to replace resources on a schedule or in response to external events that aren't captured by the resource's properties.

For example, you might want to rotate cryptographic keys monthly by using a `YYYY-MM` string as the trigger, or synchronize infrastructure updates with application releases by using a version number. Unlike `replaceOnChanges`, which triggers replacements based on resource property changes, `replacementTrigger` allows you to control replacement timing based on arbitrary values.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const today = new Date()

const keyManager = new KeyManagerResource("key-manager", {}, {
  replacementTrigger: today.getMonth() + '-' + today.getFullYear()
});
```

{{% /choosable %}}
{{% choosable language python %}}

```py
import datetime

today = datetime.now()
trigger = f"{today.month}-{today.year}"

key_manager = KeyManagerResource("key-manager", {},
    opts=pulumi.ResourceOptions(replacement_trigger=trigger))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
today := time.Now()
trigger := fmt.Sprintf("%d-%d", int(today.Month()), today.Year())

keyManager, err := NewKeyManagerResource(ctx, "key-manager", &KeyManagerResourceArgs{},
    pulumi.ReplacementTrigger(pulumi.Any(trigger)))
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var today = LocalDate.now();
var trigger = String.format("%d-%d", today.getMonthValue(), today.getYear());

var keyManager = new KeyManagerResource("key-manager",
    KeyManagerResourceArgs.Empty,
    CustomResourceOptions.builder()
        .replacementTrigger(Output.of(trigger))
        .build());
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var today = DateTime.Now;
var trigger = $"{today.Month}-{today.Year}";

var keyManager = new KeyManagerResource("key-manager", new KeyManagerResourceArgs(),
    new CustomResourceOptions
    {
        ReplacementTrigger = Output.Create(trigger)
    });
```

{{% /choosable %}}

{{% choosable language yaml }}
configuration:
  rotationPeriod:
    type: string
    default: "11-2024"

resources:
  keyManager:
    type: example:components:KeyManager
    options:
      replacementTrigger: ${rotationPeriod}
{{% /choosable }}

{{< /chooser >}}

{{% notes type="info" %}}
During each deploy, the value is checked against the previous value of the trigger, and if they don't match, the resource will be marked for replacement. Note that, if either the previous value or the current value is `null`, a replacement operation will not be forced. This means that adding or removing a replacement trigger from a resource will _not_ trigger a replacement - only changing a pre-existing trigger value.
{{% /notes %}}
