---
title_tag: "Intro to Pulumi: Resource Options"
title: "Resource Options"
meta_desc: Resource options can be used to configure how all Pulumi resources are managed. Learn more about the types of resource options and how to use them here.
menu:
  intro:
    identifier: options
    parent: resources
    weight: 2
---

All resource constructors accept an options argument that provide the following resource options:

- [additionalSecretOutputs](/docs/intro/concepts/resources/options/additionalsecretoutputs/): specify properties that must be encrypted as secrets.
- [aliases](/docs/intro/concepts/resources/options/aliases/): specify aliases for this resource, so that renaming or refactoring doesn’t replace it.
- [customTimeouts](/docs/intro/concepts/resources/options/customtimeouts/): override the default retry/timeout behavior for resource provisioning. The default value varies by resource.
- [deleteBeforeReplace](/docs/intro/concepts/resources/options/deletebeforereplace/): override the default create-before-delete behavior when replacing a resource.
- [dependsOn](/docs/intro/concepts/resources/options/dependson/): specify additional explicit dependencies in addition to the ones in the dependency graph.
- [ignoreChanges](/docs/intro/concepts/resources/options/ignorechanges/): declare that changes to certain properties should be ignored during a diff.
- [import](/docs/intro/concepts/resources/options/import/): bring an existing cloud resource into Pulumi.
- [parent](/docs/intro/concepts/resources/options/parent/): establish a parent/child relationship between resources.
- [protect](/docs/intro/concepts/resources/options/protect/): prevent accidental deletion of a resource by marking it as protected.
- [provider](/docs/intro/concepts/resources/options/provider/): pass an [explicitly configured provider](../providers/#explicit-provider-configuration), instead of using the default global provider.
- [providers](/docs/intro/concepts/resources/options/providers/): pass a set of [explicitly configured providers](../providers/#explicit-provider-configuration). These are used if provider is not given, and are passed to child resources.
- [replaceOnChanges](/docs/intro/concepts/resources/options/replaceonchanges/): declare that changes to certain properties should be treated as forcing a replacement.
- [retainOnDelete](/docs/intro/concepts/resources/options/retainondelete/): if true the resource will be retained in the backing cloud provider during a Pulumi delete operation.
- [transformations](/docs/intro/concepts/resources/options/transformations/): dynamically transform a resource’s properties on the fly.
- [version](/docs/intro/concepts/resources/options/version/): pass a provider plugin version that should be used when operating on a resource.
