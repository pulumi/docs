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

Resource constructors accept the following resource options:

- [additionalSecretOutputs](/docs/concepts/options/additionalsecretoutputs/): specify properties that must be encrypted as secrets.
- [aliases](/docs/concepts/options/aliases/): specify aliases for this resource, so that renaming or refactoring doesn’t replace it.
- [customTimeouts](/docs/concepts/options/customtimeouts/): override the default retry/timeout behavior for resource provisioning. The default value varies by resource.
- [deleteBeforeReplace](/docs/concepts/options/deletebeforereplace/): override the default create-before-delete behavior when replacing a resource.
- [deletedWith](/docs/concepts/options/deletedwith/): If set, the provider's Delete method will not be called for this resource if the specified resource is being deleted as well.
- [replaceWith](/docs/concepts/options/replacewith/): If set, the resource will be replaced if one of the specified resources is replaced.
- [dependsOn](/docs/concepts/options/dependson/): specify additional explicit dependencies in addition to the ones in the dependency graph.
- [envVarMappings](/docs/concepts/options/envvarmappings/): remap environment variables to custom keys for provider authentication.
- [hideDiffs](/docs/concepts/options/hidediffs/): compact the display of diffs for specified properties in CLI output without affecting update behavior.
- [hooks](/docs/concepts/options/hooks/): specify a set of resource hooks that will be executed at specific points in the resource lifecycle.
- [ignoreChanges](/docs/concepts/options/ignorechanges/): declare that changes to certain properties should be ignored during a diff.
- [import](/docs/concepts/options/import/): bring an existing cloud resource into Pulumi.
- [parent](/docs/concepts/options/parent/): establish a parent/child relationship between resources.
- [protect](/docs/concepts/options/protect/): prevent accidental deletion of a resource by marking it as protected.
- [provider](/docs/concepts/options/provider/): pass an [explicitly configured provider](/docs/concepts/resources/providers/#explicit-provider-configuration), instead of using the default global provider.
- [providers](/docs/concepts/options/providers/): pass a set of [explicitly configured providers](/docs/concepts/resources/providers/#explicit-provider-configuration). These are used if provider is not given, and are passed to child resources.
- [replaceOnChanges](/docs/concepts/options/replaceonchanges/): declare that changes to certain properties should be treated as forcing a replacement.
- [retainOnDelete](/docs/concepts/options/retainondelete/): if true the resource will be retained in the backing cloud provider during a Pulumi delete operation.
- [transformations](/docs/concepts/options/transformations/): dynamically transform a resource's properties on the fly. Prefer `transforms` if possible. `transformations` will be deprecated in the future in favor of `transforms`.
- [transforms](/docs/concepts/options/transforms/): dynamically transform a resource's properties on the fly.
- [version](/docs/concepts/options/version/): pass a provider plugin version that should be used when operating on a resource.

## Resource options and component resources

Not all resource options apply to [component resources](/docs/iac/concepts/components/). Component resources are logical groupings that don't have a backing cloud provider, so options that affect provider behavior have no effect on the component itself (though they may affect child resources).

| Resource option | Applies to components? | Notes |
|----------------|------------------------|-------|
| [additionalSecretOutputs](/docs/concepts/options/additionalsecretoutputs/) | No | Components don't have provider-managed outputs |
| [aliases](/docs/concepts/options/aliases/) | Yes | Works for renaming or refactoring components |
| [customTimeouts](/docs/concepts/options/customtimeouts/) | No | Components don't have provider operations to time out |
| [deleteBeforeReplace](/docs/concepts/options/deletebeforereplace/) | No | Components are not replaced by providers |
| [deletedWith](/docs/concepts/options/deletedwith/) | Yes | Controls deletion behavior |
| [dependsOn](/docs/concepts/options/dependson/) | Yes | Creates explicit dependencies on the component |
| [envVarMappings](/docs/concepts/options/envvarmappings/) | No | Only applies to provider resources |
| [hideDiffs](/docs/concepts/options/hidediffs/) | No | Components don't have provider-generated diffs |
| [hooks](/docs/concepts/options/hooks/) | No | Components don't have provider lifecycle events |
| [ignoreChanges](/docs/concepts/options/ignorechanges/) | No | Components don't have provider-managed inputs. The component implementation may choose to propagate this to children. |
| [import](/docs/concepts/options/import/) | No | Components cannot be imported from cloud providers |
| [parent](/docs/concepts/options/parent/) | Yes | Establishes parent-child relationships |
| [protect](/docs/concepts/options/protect/) | Yes | Protects the component from deletion |
| [provider](/docs/concepts/options/provider/) | No | Use `providers` instead for component resources |
| [providers](/docs/concepts/options/providers/) | Yes | Pass providers to use for child resources |
| [replaceOnChanges](/docs/concepts/options/replaceonchanges/) | No | Components are not replaced by providers |
| [replaceWith](/docs/concepts/options/replacewith/) | No | Components are not replaced by providers |
| [retainOnDelete](/docs/concepts/options/retainondelete/) | No | Components don't have cloud resources to retain |
| [transformations](/docs/concepts/options/transformations/) | Yes | Transform child resources within the component |
| [transforms](/docs/concepts/options/transforms/) | Yes | Transform child resources within the component |
| [version](/docs/concepts/options/version/) | No | Components don't use provider plugins |

{{% notes type="info" %}}
When you apply a resource option to a component that doesn't support it, the option is silently ignored. To apply options like `protect` or `ignoreChanges` to the child resources within a component, use the `transforms` option to modify child resources as they're created.
{{% /notes %}}
