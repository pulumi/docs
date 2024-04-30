---
title_tag: "Resources | Pulumi Concepts"
meta_desc: Resources represent the fundamental units that make up your cloud infrastructure. Learn how Pulumi resources work and how to use them in this guide.
title: Resources
h1: Resources
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: resources
    weight: 3
aliases:
- /docs/intro/concepts/resources/
---

<script>
    // The following list maps the headings that previously appeared on this page to their new locations.
    // We use this list to determine whether we can redirect visitors from the old content to the new.
    var redirects = {
        "#options": "/docs/concepts/options/",
        "#additionalsecretoutputs": "/docs/concepts/options/additionalsecretoutputs",
        "#aliases": "/docs/concepts/options/aliases",
        "#customtimeouts": "/docs/concepts/options/customtimeouts",
        "#deletebeforereplace": "/docs/concepts/options/deletebeforereplace",
        "#dependson": "/docs/concepts/options/dependson",
        "#ignorechanges": "/docs/concepts/options/ignorechanges",
        "#import": "/docs/concepts/options/import",
        "#parent": "/docs/concepts/options/parent",
        "#protect": "/docs/concepts/options/protect",
        "#provider": "/docs/concepts/options/provider",
        "#replaceonchanges": "/docs/concepts/options/replaceonchanges",
        "#transformations": "/docs/concepts/options/transformations",
        "#version": "/docs/concepts/options/version",
        "#components": "/docs/concepts/resources/components",
        "#authoring-a-new-component-resource": "/docs/concepts/resources/components/#authoring-a-new-component-resource",
        "#creating-child-resources": "/docs/concepts/resources/components/#creating-child-resources",
        "#registering-component-outputs": "/docs/concepts/resources/components/#registering-component-outputs",
        "#inheriting-resource-providers": "/docs/concepts/resources/components/#inheriting-resource-providers",
        "#providers": "/docs/concepts/resources/providers",
        "#default-provider-configuration": "/docs/concepts/resources/providers/#default-provider-configuration",
        "#explicit-provider-configuration": "/docs/concepts/resources/providers/#explicit-provider-configuration",
        "#dynamicproviders": "/docs/concepts/resources/dynamic-providers",
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

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let res = new Resource(name, args, options);
```

{{% /choosable %}}
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

All resources have a required [`name`](/docs/concepts/resources/names) argument, which must be unique across resources of the same kind in a [`stack`](/docs/concepts/stack). This *logical name* influences the *physical name* assigned by your infrastructure’s cloud provider. Pulumi [auto-names](/docs/concepts/resources/names#autonaming) physical resources by default, so the physical name and the logical name may differ. This auto-naming behavior can be overridden, if required.

The `args` argument is an object with a set of named property input values that are used to initialize the resource. These can be normal raw values—such as strings, integers, lists, and maps—or [outputs](/docs/concepts/inputs-outputs/) from other resources. Each resource has a number of named input properties that control the behavior of the resulting infrastructure. To determine what arguments a resource supports, refer to that resource’s API documentation in the [Registry](/registry/).

The [`options`](/docs/concepts/options) argument is optional, but lets you control certain aspects of the resource. For example, you can show explicit dependencies, use a custom provider configuration, or import an existing infrastructure.

## Resource Details

The following topics provide more details on the core concepts for working with resources in Pulumi:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/resources/names/"><i class="fas fa-font pr-2"></i>Resource Names</a></h3>
        <p>Learn more about resource names and how to use them.</p>
    </div>
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/options/"><i class="fas fa-cogs pr-2"></i>Resource Options</a></h3>
        <p>Learn how to use resource options to modify the way that resources are managed by Pulumi.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/resources/components/"><i class="fas fa-project-diagram pr-2"></i>Components</a></h3>
        <p>Learn what a component resource is, how to author a new component resource, how to create child resources, and more.</p>
    </div>
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/resources/providers/"><i class="fas fa-server pr-2"></i>Providers</a></h3>
        <p>Learn how a resource provider handles communications with a cloud service to create, read, update, and delete the resources you define in your Pulumi programs.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/resources/dynamic-providers/"><i class="fas fa-file-alt pr-2"></i>Dynamic Providers</a></h3>
        <p>Learn how to use dynamic providers and use cases for them.</p>
    </div>
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/resources/get/"><i class="fas fa-cloud-download-alt pr-2"></i>Getter Functions</a></h3>
        <p>Learn how a Pulumi resource uses its `get` function to retrieve a reference to an existing instance of the resource.</p>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/resources/functions/"><i class="fas fa-file-alt pr-2"></i>Provider Functions</a></h3>
        <p>Learn how to use the functions included with Pulumi packages.</p>
    </div>
</div>
