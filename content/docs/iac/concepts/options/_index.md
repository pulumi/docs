---
title_tag: "Resource Options | Pulumi Concepts"
meta_desc: Resource options can be used to configure how all Pulumi resources are managed. Learn more about the types of resource options and how to use them here.
title: Resource options
h1: Resource options
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: options
    weight: 4
aliases:
- /docs/intro/concepts/resources/options/
---

All resource constructors accept an options argument that provide the following resource options:

- [additionalSecretOutputs](/docs/concepts/options/additionalsecretoutputs/): specify properties that must be encrypted as secrets.
- [aliases](/docs/concepts/options/aliases/): specify aliases for this resource, so that renaming or refactoring doesn’t replace it.
- [customTimeouts](/docs/concepts/options/customtimeouts/): override the default retry/timeout behavior for resource provisioning. The default value varies by resource.
- [deleteBeforeReplace](/docs/concepts/options/deletebeforereplace/): override the default create-before-delete behavior when replacing a resource.
- [deletedWith](/docs/concepts/options/deletedwith/): If set, the provider's Delete method will not be called for this resource if the specified resource is being deleted as well.
- [dependsOn](/docs/concepts/options/dependson/): specify additional explicit dependencies in addition to the ones in the dependency graph.
- [ignoreChanges](/docs/concepts/options/ignorechanges/): declare that changes to certain properties should be ignored during a diff.
- [import](/docs/concepts/options/import/): bring an existing cloud resource into Pulumi.
- [parent](/docs/concepts/options/parent/): establish a parent/child relationship between resources.
- [protect](/docs/concepts/options/protect/): prevent accidental deletion of a resource by marking it as protected.
- [provider](/docs/concepts/options/provider/): pass an [explicitly configured provider](/docs/concepts/resources/providers/#explicit-provider-configuration), instead of using the default global provider.
- [providers](/docs/concepts/options/providers/): pass a set of [explicitly configured providers](/docs/concepts/resources/providers/#explicit-provider-configuration). These are used if provider is not given, and are passed to child resources.
- [replaceOnChanges](/docs/concepts/options/replaceonchanges/): declare that changes to certain properties should be treated as forcing a replacement.
- [retainOnDelete](/docs/concepts/options/retainondelete/): if true the resource will be retained in the backing cloud provider during a Pulumi delete operation.
- [transformations](/docs/concepts/options/transformations/): dynamically transform a resource’s properties on the fly. Prefer `transforms` if possible. `transformations` will be deprecated in the future in favor of `transforms`.
- [transforms](/docs/concepts/options/transforms/): dynamically transform a resource’s properties on the fly.
- [version](/docs/concepts/options/version/): pass a provider plugin version that should be used when operating on a resource.
