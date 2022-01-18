---
title: "Resources"
meta_desc: An in depth look at Pulumi resources and their usage.
menu:
  intro:
    identifier: resources
    parent: concepts
    weight: 4
---

<script>
    // The following list maps the headings that previously appeared on this page to their new locations.
    // We use this list to determine whether we can redirect visitors from the old content to the new.
    var redirects = {
        "#options": "/docs/intro/concepts/resources/options",
        "#additionalsecretoutputs": "/docs/intro/concepts/resources/options/additionalsecretoutputs",
        "#aliases": "/docs/intro/concepts/resources/options/aliases",
        "#customtimeouts": "/docs/intro/concepts/resources/options/customtimeouts",
        "#deletebeforereplace": "/docs/intro/concepts/resources/options/deletebeforereplace",
        "#dependson": "/docs/intro/concepts/resources/options/dependson",
        "#ignorechanges": "/docs/intro/concepts/resources/options/ignorechanges",
        "#import": "/docs/intro/concepts/resources/options/import",
        "#parent": "/docs/intro/concepts/resources/options/parent",
        "#protect": "/docs/intro/concepts/resources/options/protect",
        "#provider": "/docs/intro/concepts/resources/options/provider",
        "#replaceonchanges": "/docs/intro/concepts/resources/options/replaceonchanges",
        "#transformations": "/docs/intro/concepts/resources/options/transformations",
        "#version": "/docs/intro/concepts/resources/options/version",
        "#components": "/docs/intro/concepts/resources/components",
        "#authoring-a-new-component-resource": "/docs/intro/concepts/resources/components/#authoring-a-new-component-resource",
        "#creating-a-child-resource": "/docs/intro/concepts/resources/components/#creating-a-child-resource",
        "#registering-component-outputs": "/docs/intro/concepts/resources/components/#registering-component-outputs",
        "#inheriting-resource-providers": "/docs/intro/concepts/resources/components/#inheriting-resource-providers",
        "#providers": "/docs/intro/concepts/resources/providers",
        "#default-provider-configuration": "/docs/intro/concepts/resources/providers/#default-provider-configuration",
        "#explicit-provider-configuration": "/docs/intro/concepts/resources/providers/#explicit-provider-configuration",
        "#dynamicproviders": "/docs/intro/concepts/resources/dynamicproviders",
        "#names": "/docs/intro/concepts/resources/names",
        "#autonaming": "/docs/intro/concepts/resources/names/#autonaming",
        "#urns": "/docs/intro/concepts/resources/names/#urns",
        "#resource-get": "/docs/intro/concepts/resources/get",
    };

    var redirect = redirects[location.hash];
    if (redirect) {
        location.href = redirect;
    }
</script>

Resources represent the fundamental units that make up your cloud infrastructure, such as a compute instance, a storage bucket, or a Kubernetes cluster.

All infrastructure resources are described by one of two subclasses of the `Resource` class. These two subclasses are:

- `CustomResource`: A custom resource is a cloud resource managed by a [resource provider]({{< relref "providers" >}}) such as AWS, Microsoft Azure, Google Cloud or Kubernetes.
- `ComponentResource`: A [component resource]({{< relref "components" >}}) is a logical grouping of other resources that creates a larger, higher-level abstraction that encapsulates its implementation details.

A resource’s desired state is declared by constructing an instance of the resource:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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

{{< /chooser >}}

All resources have a required [`name`]({{< relref "names" >}}) argument, which must be unique across resources of the same kind in a [`stack`]({{< relref "/docs/intro/concepts/stack" >}}). This *logical name* influences the *physical name* assigned by your infrastructure’s cloud provider. Pulumi [auto-names]({{< relref "#autonaming" >}}) physical resources by default, so the physical name and the logical name may differ. This auto-naming behavior can be overridden, if required.

The `args` argument is an object with a set of named property input values that are used to initialize the resource. These can be normal raw values—such as strings, integers, lists, and maps—or [outputs]({{< relref "docs/intro/concepts/inputs-outputs" >}}) from other resources. Each resource has a number of named input properties that control the behavior of the resulting infrastructure. To determine what arguments a resource supports, refer to that resource’s API documentation in the [Registry]({{< relref "/registry" >}}).

The [`options`]({{< relref "options" >}}) argument is optional, but lets you control certain aspects of the resource. For example, you can show explicit dependencies, use a custom provider configuration, or import an existing infrastructure.

## Resource Details

The following topics provide more details on the core concepts for working with resources in Pulumi:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "names" >}}"><i class="fas fa-font pr-2"></i>Resource Names</a></h3>
        <p>Learn how Pulumi projects are organized and configured.</p>
    </div>
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "options" >}}"><i class="fas fa-cogs pr-2"></i>Resource Options</a></h3>
        <p>Learn how to use resource options to modify the way that resources are managed by Pulumi.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "components" >}}"><i class="fas fa-project-diagram pr-2"></i>Components</a></h3>
        <p>Learn how to create and deploy stacks.</p>
    </div>
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "providers" >}}"><i class="fas fa-server pr-2"></i>Providers</a></h3>
        <p>Learn more about how to use and manage resources in your program.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "dynamic-providers" >}}"><i class="fas fa-file-alt pr-2"></i>Dynamic Providers</a></h3>
        <p>Learn how Pulumi stores state and manages concurrency.</p>
    </div>
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "get" >}}"><i class="fas fa-cloud-download-alt pr-2"></i>Getter Functions</a></h3>
        <p>Learn how to configure stacks for different deployment scenarios.</p>
    </div>
</div>
