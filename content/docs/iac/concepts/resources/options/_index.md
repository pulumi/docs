---
title_tag: "Resource Options | Pulumi Concepts"
meta_desc: Resource options can be used to configure how all Pulumi resources are managed. Learn more about the types of resource options and how to use them here.
title: Resource options
h1: Resource options
menu:
  iac:
    parent: iac-concepts-resources
    identifier: options-concepts
    weight: 50
aliases:
  - /docs/iac/concepts/options/
  - /docs/intro/concepts/resources/options/
  - /docs/concepts/options/
---

All Pulumi IaC resources support a common set of options that allow you to customize how your resources are managed. Resource options allow you to do things like protect resources from being deleted, express more fine-grained control to the order in which resources are changed, or apply custom code that will allow you to change the properties of your resources.

Resource constructors accept the following resource options. Each option's reference page describes its behavior in depth and how the Pulumi SDKs enforce which resource types it applies to.

{{< resource-options-table >}}

## Resource options and component resources

Not all resource options apply to [component resources](/docs/iac/concepts/components/). Component resources are logical groupings that don't have a backing cloud provider, so options that affect provider behavior have no effect on the component itself (though, as described below, several of them are inherited by the component's children). The **Applies to** column in the table above shows which options have a direct effect on the component itself; each option's reference page explains the behavior in detail.

{{% notes type="info" %}}
When you apply a resource option to a component that doesn't support it, the option has no direct effect on the component. To apply options like `ignoreChanges` to the child resources within a component, use the `transforms` option to modify child resources as they're created.
{{% /notes %}}

### Options inherited from a component to its children

When a resource option is set on a component, several options propagate from the component to each of its child resources automatically. The child resource doesn't need to set the option itself; the engine carries the value down the parent/child chain at resource registration time. Each option's reference page describes how the option behaves on a component in detail.

{{< resource-options-inheritance-table >}}

Options marked **N/A** can't be set on a component to begin with: `additionalSecretOutputs`, `deleteBeforeReplace`, and `import` are custom-resource-only (and a compile-time error on components in TypeScript, C#, and Java); `envVarMappings` only applies to explicitly configured provider resources; and `parent` defines the parent/child relationship itself rather than being a value that's inherited.

For options that aren't inherited, set them on each child resource that needs the behavior, or use `transforms` on the component to inject the option into matching child registrations as they're created.
