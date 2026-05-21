---
title_tag: "Resource Options | Pulumi Concepts"
meta_desc: Resource options can be used to configure how all Pulumi resources are managed. Learn more about the types of resource options and how to use them here.
title: Resource options
h1: Resource options
meta_image: /images/docs/meta-images/docs-meta.png
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

Not all resource options apply to [component resources](/docs/iac/concepts/components/). Component resources are logical groupings that don't have a backing cloud provider, so options that affect provider behavior have no effect on the component itself (though they may affect child resources). The **Applies to** column in the table above shows which options apply to component resources; each option's reference page explains the behavior in detail.

{{% notes type="info" %}}
When you apply a resource option to a component that doesn't support it, the option is silently ignored. To apply options like `protect` or `ignoreChanges` to the child resources within a component, use the `transforms` option to modify child resources as they're created.
{{% /notes %}}
