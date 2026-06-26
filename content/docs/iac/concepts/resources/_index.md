---
title_tag: "Resources | Pulumi Concepts"
meta_desc: Resources represent the fundamental units that make up your cloud infrastructure. Learn how Pulumi resources work and how to use them in this guide.
title: Resources
h1: Resources
menu:
    iac:
        name: Resources
        parent: iac-concepts
        weight: 50
        identifier: iac-concepts-resources
    concepts:
        identifier: resources
        weight: 3
aliases:
- /docs/intro/concepts/resources/
- /docs/concepts/resources/
---

<script>
    // The following list maps the headings that previously appeared on this page to their new locations.
    // We use this list to determine whether we can redirect visitors from the old content to the new.
    var redirects = {
        "#options": "/docs/iac/concepts/resources/options/",
        "#additionalsecretoutputs": "/docs/iac/concepts/resources/options/additionalsecretoutputs",
        "#aliases": "/docs/iac/concepts/resources/options/aliases",
        "#customtimeouts": "/docs/iac/concepts/resources/options/customtimeouts",
        "#deletebeforereplace": "/docs/iac/concepts/resources/options/deletebeforereplace",
        "#dependson": "/docs/iac/concepts/resources/options/dependson",
        "#ignorechanges": "/docs/iac/concepts/resources/options/ignorechanges",
        "#import": "/docs/iac/concepts/resources/options/import",
        "#parent": "/docs/iac/concepts/resources/options/parent",
        "#protect": "/docs/iac/concepts/resources/options/protect",
        "#provider": "/docs/iac/concepts/resources/options/provider",
        "#replaceonchanges": "/docs/iac/concepts/resources/options/replaceonchanges",
        "#transformations": "/docs/iac/concepts/resources/options/transformations",
        "#transforms": "/docs/iac/concepts/resources/options/transforms",
        "#version": "/docs/iac/concepts/resources/options/version",
        "#components": "/docs/concepts/resources/components",
        "#authoring-a-new-component-resource": "/docs/iac/guides/building-extending/components/build-a-component/",
        "#creating-child-resources": "/docs/iac/guides/building-extending/components/build-a-component/#creating-child-resources",
        "#registering-component-outputs": "/docs/iac/guides/building-extending/components/build-a-component/#registering-component-outputs",
        "#inheriting-resource-providers": "/docs/iac/guides/building-extending/components/build-a-component/#inheriting-resource-providers",
        "#providers": "/docs/iac/concepts/providers",
        "#default-provider-configuration": "/docs/iac/concepts/providers/#default-provider-configuration",
        "#explicit-provider-configuration": "/docs/iac/concepts/providers/#explicit-provider-configuration",
        "#dynamicproviders": "/docs/iac/concepts/providers/dynamic-providers",
        "#names": "/docs/concepts/resources/names",
        "#autonaming": "/docs/concepts/resources/names/#autonaming",
        "#urns": "/docs/concepts/resources/names/#urns",
        "#resource-get": "/docs/concepts/resources/get",
    };

    var redirect = redirects[location.hash];
    if (redirect) {
        location.href = redirect;
    }
</script>

Resources represent the fundamental units that make up your cloud infrastructure, such as a compute instance, a storage bucket, or a Kubernetes cluster.

All infrastructure resources are described by one of two subclasses of the `Resource` class. These two subclasses are:

- `CustomResource`: A custom resource is a cloud resource managed by a [resource provider](/docs/concepts/resources/providers/) such as AWS, Microsoft Azure, Google Cloud or Kubernetes.
- `ComponentResource`: A [component resource](/docs/concepts/resources/components/) is a logical grouping of other resources that creates a larger, higher-level abstraction that encapsulates its implementation details.

A resource’s desired state is declared by constructing an instance of the resource:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let res = new Resource(name, args, options);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
res = Resource(name, args, options)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
res, err := NewResource(ctx, name, args, opt1, opt2)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var res = new Resource(name, args, options);
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var res = new Resource(name, args, options);
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  res:
    type: the:resource:Type
    properties: ...args
    options: ...options
```

{{% /choosable %}}

{{< /chooser >}}

All resources have a required [`name`](/docs/concepts/resources/names) argument, which must be unique across resources of the same kind in a [`stack`](/docs/concepts/stack). This *logical name* influences the *physical name* assigned by your infrastructure’s cloud provider. Pulumi [auto-names](/docs/concepts/resources/names/#autonaming) physical resources by default, so the physical name and the logical name may differ. This auto-naming behavior can be overridden, if required.

The `args` argument is an object with a set of named property input values that are used to initialize the resource. These can be normal raw values—such as strings, integers, lists, and maps—or [outputs](/docs/concepts/inputs-outputs/) from other resources. Each resource has a number of named input properties that control the behavior of the resulting infrastructure. To determine what arguments a resource supports, refer to that resource’s API documentation in the [Registry](/registry/).

The [`options`](/docs/concepts/options) argument is optional, but lets you control certain aspects of the resource. For example, you can show explicit dependencies, use a custom provider configuration, or import existing infrastructure.

## Related topics

- [Resource Names](/docs/concepts/resources/names/) - Learn more about resource names and how to use them.
- [Resource Options](/docs/concepts/options/) - Learn how to use resource options to modify the way that resources are managed by Pulumi.
- [Components](/docs/concepts/resources/components/) - Learn what a component resource is, how to author a new component resource, how to create child resources, and more.
- [Providers](/docs/iac/concepts/providers/) - Learn how a resource provider handles communications with a cloud service to create, read, update, and delete the resources you define in your Pulumi programs.
- [Dynamic Providers](/docs/iac/concepts/providers/dynamic-providers/) - Learn how to use dynamic providers and use cases for them.
- [Getter Functions](/docs/concepts/resources/get/) - Learn how a Pulumi resource uses its `get` function to retrieve a reference to an existing instance of the resource.
- [Provider Functions](/docs/concepts/resources/functions/) - Learn how to use the functions included with Pulumi packages.
