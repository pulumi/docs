---
title: "Resource Options"
meta_desc: Resource options can be used to configure how all Pulumi resources are managed.
menu:
  intro:
    identifier: options
    parent: resources
    weight: 2
---

All resource constructors accept an options argument that provide the following resource options:

- [additionalSecretOutputs]({{< relref "additionalsecretoutputs" >}}): specify properties that must be encrypted as secrets.
- [aliases]({{< relref "aliases" >}}): specify aliases for this resource, so that renaming or refactoring doesn’t replace it.
- [customTimeouts]({{< relref "customtimeouts" >}}): override the default retry/timeout behavior for resource provisioning. The default value varies by resource.
- [deleteBeforeReplace]({{< relref "deletebeforereplace" >}}): override the default create-before-delete behavior when replacing a resource.
- [dependsOn]({{< relref "dependson" >}}): specify additional explicit dependencies in addition to the ones in the dependency graph.
- [ignoreChanges]({{< relref "ignorechanges" >}}): declare that changes to certain properties should be ignored during a diff.
- [import]({{< relref "import" >}}): bring an existing cloud resource into Pulumi.
- [parent]({{< relref "parent" >}}): establish a parent/child relationship between resources.
- [protect]({{< relref "protect" >}}): prevent accidental deletion of a resource by marking it as protected.
- [provider]({{< relref "provider" >}}): pass an [explicitly configured provider]({{< relref "../providers/#explicit-provider-configuration" >}}), instead of using the default global provider.
- [replaceOnChanges]({{< relref "replaceonchanges" >}}): declare that changes to certain properties should be treated as forcing a replacement.
- [transformations]({{< relref "transformations" >}}): dynamically transform a resource’s properties on the fly.
- [version]({{< relref "version" >}}): pass a provider plugin version that should be used when operating on a resource.
