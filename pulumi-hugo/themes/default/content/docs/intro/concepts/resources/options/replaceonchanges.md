---
title: "ReplaceOnChanges"
meta_desc: The replaceOnChanges resource option indicates that changes to properties on a resource should force a replacement instead of an in-place update.
menu:
  intro:
    parent: options
    weight: 11
---

The `replaceOnChanges` resource option can be used to indicate that changes to certain properties on a resource should force a replacement of the resource instead of an in-place update.  Typically users rely on the resource provider to make this decision based on whether the input property is one that the provider knows how to update in place, or if not, requires a replacement to modify.  However, there are cases where users want to replace a resource on a change to an input property even if the resource provider itself doesn't believe it has to replace the resource.

For example, with Kubernetes `CustomResource` resources, the Kubernetes resource model doesn't know whether or not a specific input property on a specific kind of `CustomResource` requires a replacement, and so assumes that *any* change can be made without replacement.  However, in practice, many specific kinds of `CustomResource` in the Kubernetes ecosystem *do* require replacement when certain input properties are changed.  The Kubernetes provider itself can't know this, but users can use `replaceOnChanges` to ensure that these changes can be made correctly via Pulumi.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let widget = new k8s.apiextensions.CustomResource("widget", {
    apiVersion: 'acmecorp.com/v1alpha1',
    kind: 'Widget',
    spec: {
        input: "something",
    },
}, { replaceOnChanges: ["spec.input"] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let widget = new k8s.apiextensions.CustomResource("widget", {
    apiVersion: 'acmecorp.com/v1alpha1',
    kind: 'Widget',
    spec: {
        input: "something",
    },
}, { replaceOnChanges: ["spec.input"] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
widget = apiextensions.CustomResource("widget",
    api_version="acmecorp.com/v1alpha1",
    kind="Widget",
    spec={
        "input": "something",
    },
    opts=ResourceOptions(replace_on_changes=["spec.input"])
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
widget, err = apiextensions.NewCustomResource(ctx, "widgt", &apiextensions.CustomResourceArgs{
    ApiVersion: pulumi.String("acmecorp.com/v1alpha1"),
    Kind:       pulumi.String("Widget"),
    OtherFields: kubernetes.UntypedArgs{
        "spec": map[string]interface{}{
            "input": "something",
        },
    },
}, pulumi.ReplaceOnChanges([]string{"spec.input"})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var widget = new Pulumi.Kubernetes.ApiExtensions.CustomResource("widget", new WidgetArgs
{
    Spec = new WidgetSpecArgs
    {
        Input = "something",
    }
}, pulumi.ReplaceOnChanges([]string{"spec.input"}));
```

{{% /choosable %}}

{{< /chooser >}}

The property paths provided as input to `replaceOnChanges` can each describe a subset of the properties of the resource which should trigger a replacement on changes.  The `*` wildcard can be used in any part of a path.  A few examples of what changes will trigger replacement for a given property path string are:

- `*`: any property change
- `spec`: any change to the `spec` property or any of its children
- `spec[0]`: any change to the first element of the array in the `spec` property or any of its children
- `spec[*].item`: any change to the `item` property of any element of the array in the `spec` prroperty or any of the `item` property's children

{{% notes "info" %}}
The property paths passed to `replaceOnChanges` should always be the "camelCase" version of the property name, as used in the core Pulumi resource model.
{{% /notes %}}

If there are initialization errors on a resource (because the resource was created but failed to fully initialize correctly on a previous deployment) then the resource will normally be updated on the following Pulumi update, even if there are no other changes to the resource's inputs.  If `*` is specified as a property path for `replaceOnChanges`, then initialization errors will trigger a replacement instead of an update.

The `replaceOnChanges` resource option can be combined with the [`deleteBeforeReplace`]({{< relref "deletebeforereplace" >}}) resource option to trigger a resource to be deleted before it is replaced whenever a given input has changes.
