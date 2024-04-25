---
title_tag: "ignoreChanges | Resource Options"
meta_desc: The ignoreChanges resource option declares that changes to certain properties should be ignored during a diff.
title: "ignoreChanges"
h1: "Resource option: ignoreChanges"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: ignoreChanges
    parent: options
    weight: 7
aliases:
- /docs/intro/concepts/resources/options/ignorechanges/
---

The `ignoreChanges` resource option specifies a list of properties that Pulumi will ignore when it updates existing resources. Pulumi ignores a property by using the old value from the state instead of the value provided by the Pulumi program when determining whether an update or replace is needed. Ignored properties will still be used from the program when there is no previous value in the state, most importantly when creating the resource.

For instance, in this example, the resource’s prop property "new-value" will be set when Pulumi initially creates the resource, but from then on, any updates will ignore it:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let res = new MyResource("res",
    { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let res = new MyResource("res",
    { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
res = MyResource("res",
    prop="new-value",
    opts=ResourceOptions(ignore_changes=["prop"]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
res, _ := NewMyResource(ctx, "res",
    &MyResourceArgs{Prop: "new-value"},
    pulumi.IgnoreChanges([]string{"prop"}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var res = new MyResource("res",
    new MyResourceArgs { Prop = "new-value" },
    new CustomResourceOptions { IgnoreChanges = { "prop" } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var res = new MyResource("res",
    MyResourceArgs.builder()
        .prop("new-value")
        .build(),
    CustomResourceOptions.builder()
        .ignoreChanges("prop")
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
      ignoreChanges:
        - prop
```

{{% /choosable %}}

{{< /chooser >}}

One reason you would use the `ignoreChanges` option is to ignore changes in properties that lead to diffs. Another reason is to change the defaults for a property without forcing all existing deployed stacks to update or replace the affected resource. This is common after you’ve imported existing infrastructure provisioned by another method into Pulumi. In these cases, there may be historical drift that you’d prefer to retain, rather than replacing and reconstructing critical parts of your infrastructure.

{{% notes "info" %}}
The `ignoreChanges` option only applies to resource inputs, not outputs.
{{% /notes %}}

{{% notes "info" %}}
The `ignoreChanges` resource option does not apply to inputs to component resources.  If `ignoreChanges` is passed to a component resource, it is up to that component's implementation to decide what if anything it will do.
{{% /notes %}}

In addition to passing simple property names, nested properties can also be supplied to ignore changes to a more targeted nested part of the resource's inputs. Here are examples of legal paths that can be passed to specify nested properties of objects and arrays, as well as to escape object keys that contain special characters:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language python %}}

{{% notes "info" %}}
The property names passed to `ignoreChanges` should always be the "camelCase" version of the property name, as used in the core Pulumi resource model.
For example, a property named `nested_resource` would turn into `nestedResource`.
{{% /notes %}}

{{% /choosable %}}

{{% choosable language go %}}

{{% notes "info" %}}
The property names passed to `ignoreChanges` should always be the "camelCase" version of the property name, as used in the core Pulumi resource model.
For example, a property named `NestedResource` would turn into `nestedResource`.
{{% /notes %}}

{{% /choosable %}}

{{% choosable language csharp %}}

{{% notes "info" %}}
The property names passed to `ignoreChanges` should always be the "camelCase" version of the property name, as used in the core Pulumi resource model.
For example, a property named `NestedResource` would turn into `nestedResource`.
{{% /notes %}}

{{% /choosable %}}

{{< /chooser >}}

- `root`
- `root.nested`
- `root["nested"]`
- `root.double.nest`
- `root["double"].nest`
- `root["double"]["nest"]`
- `root.array[0]`
- `root.array[100]`
- `root.array[0].nested`
- `root.array[0][1].nested`
- `root.nested.array[0].double[1]`
- `root["key with \"escaped\" quotes"]`
- `root["key with a ."]`
- `["root key with \"escaped\" quotes"].nested`
- `["root key with a ."][100]`
- `root.array[*].field`
- `root.array["*"].field`
