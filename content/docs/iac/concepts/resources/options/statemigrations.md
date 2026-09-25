---
title: stateMigrations
title_tag: stateMigrations | Resource options
h1: "Resource option: stateMigrations"
meta_desc: Use ordered state migration callbacks to upgrade a component's internal resources before Pulumi calculates changes during previews and updates.
menu:
  iac:
    identifier: stateMigrations
    parent: options-concepts
    weight: 195
---

The `stateMigrations` resource option lets a component author supply an ordered list of callbacks that translate the component's prior state and the state of its children before diffing. Use it when a new component version changes its internal resource structure while preserving existing cloud resources.

{{< resource-option-scope "stateMigrations" >}}

{{% notes type="info" %}}
This API is **experimental** and may change.

<!-- TODO: Add the feedback discussion URL -->
<!-- Share feedback by commenting on the GitHub discussion (link coming soon). -->

{{% /notes %}}

## Callback API

Each migration callback is a pure function that transforms the saved state of a component and its children into the state expected by a new component version.

Each callback receives the registering component's URN and the prior state of the component and its descendants. It returns a complete replacement state and, when removing or renaming resource URNs, a mapping from each old URN to its successor. Returning no result leaves the state unchanged and allows later callbacks to run.

The prior subtree contains the component itself first and then its descendants in checkpoint resource format. The registering URN can differ from the root's prior URN when Pulumi matches it through an alias. Each callback receives the preceding callback's result.

A changed result must contain the entire replacement subtree, including unchanged resources. Every input URN must either remain in the result or have a successor mapping to a resource in the result, but not both. Multiple removed URNs can map to the same successor.

## Example

Define a migration callback and pass it to a component through the `stateMigrations` option.

{{< chooser language "typescript,python,go" >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="component-state-migrations-option" language="typescript" >}}
```

API reference: [StateMigrationArgs](/docs/reference/pkg/nodejs/pulumi/pulumi/interfaces/StateMigrationArgs.html) · [StateMigrationResult](/docs/reference/pkg/nodejs/pulumi/pulumi/interfaces/StateMigrationResult.html).

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="component-state-migrations-option" language="python" >}}
```

API reference: [StateMigrationArgs](/docs/reference/pkg/python/pulumi/#pulumi.StateMigrationArgs) · [StateMigrationResult](/docs/reference/pkg/python/pulumi/#pulumi.StateMigrationResult).

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="component-state-migrations-option" language="go" >}}
```

API reference: [StateMigrationArgs](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi#StateMigrationArgs) · [StateMigrationResult](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi#StateMigrationResult).

{{% /choosable %}}

{{< /chooser >}}

See the [state migrations guide](/docs/iac/guides/building-extending/components/state-migrations/) for a complete example.

## Behavior

Callbacks run during previews and updates when prior state exists. They must be idempotent and return no result when the state no longer needs migration. They rewrite state without performing provider operations.

Callbacks must preserve managed resource identity, lifecycle safety flags, and secret envelopes. They must not perform Pulumi runtime operations or wait for unresolved outputs.

See [State migrations](/docs/iac/guides/building-extending/components/state-migrations/) for the full contract, restrictions, and complete examples.
