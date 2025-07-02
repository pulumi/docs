---
title_tag: "hooks | Resource Options"
meta_desc: The hooks resource option provides a set of resource hooks linked to a resource.
title: "hooks"
h1: "Resource option: hooks"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: hooks
    parent: options-concepts
    weight: 7
aliases:
- /docs/intro/concepts/resources/options/hooks/
- /docs/concepts/options/hooks/
---

The `hooks` resource option provides a set of resource hooks linked to a resource. Hooks are used to execute custom logic at specific points in the resource lifecycle, such as before or after creation, update, or deletion.

Each hook is a callback that gets invoked by the Pulumi engine. Hooks that execute before an action are called **before hooks** and have names beginning with `before` or `Before` depending on the language. Hooks that execute after an action are called **after hooks** and have names beginning with `after` or `After` depending on the language. Pulumi currently supports the following hook types:

* *Create hooks* are called before or after a resource is created. This may occur during the initial creation of a resource or when a resource requires replacement due to e.g. a change in an immutable property.

* *Update hooks* are called before or after a resource is updated in-place.

* *Delete hooks* are called before or after a resource is deleted. This may occur during the deletion of a resource due to a `destroy` or that resource's removal from the program, or as part of a resource replacement due to e.g. a change in an immutable property.

When a hook is executed as part of a resource operation, it receives the resource's [URN](/docs/iac/concepts/resources/names/#urns) and ID, as well as any relevant input and output properties. Hooks may return errors. If a before hook returns an error, the action it precedes will *not* be executed and the Pulumi operation will fail with that error. If an after hook returns an error, Pulumi will log a warning diagnostic and the Pulumi operation will continue. The table below illustrates the combinations of inputs, outputs, and error behaviors for each hook type:

| Hook type     | Old inputs | New inputs | Old outputs | New outputs | Error behavior                    |
|---------------|------------|------------|-------------|-------------|-----------------------------------|
| Before create |            | ✓          |             |             | Prevent creation, fail deployment |
| After create  |            | ✓          |             | ✓           | Log warning, continue deployment  |
| Before update | ✓          | ✓          | ✓           |             | Prevent update, fail deployment   |
| After update  | ✓          | ✓          | ✓           | ✓           | Log warning, continue deployment  |
| Before delete | ✓          |            | ✓           |             | Prevent deletion, fail deployment |
| After delete  | ✓          |            | ✓           |             | Log warning, continue deployment  |

## Health checking example

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```python
```

{{% /choosable %}}
{{% choosable language go %}}

```go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Pulumi Java support for hooks is coming soon
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Pulumi YAML does not support resource hooks
```

{{% /choosable %}}

{{< /chooser >}}

## Deletions and delete hooks

In order for delete hooks to run successfully, Pulumi must have access to any necessary hooks at the time of the deletion. You should take the following actions to ensure that delete hooks run as expected:

* When removing resources from your program, first remove *only* the resources you wish to delete, *leaving any delete hooks in place*. Upon running e.g. `pulumi up`, Pulumi will delete the resources and run any relevant delete hooks. Once this operation is complete, you can then remove the delete hooks from your program.

* When running `pulumi destroy`, you must pass the `--run-program` flag to instruct Pulumi to run your program and register any hooks that are to be executed. If Pulumi detects that you are trying to `destroy` a stack that contains hooks _without_ the `--run-program` flag, it will fail with an error.
