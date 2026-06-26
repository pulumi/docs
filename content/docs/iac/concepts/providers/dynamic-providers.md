---
title_tag: "Dynamic Resource Providers"
meta_desc: Dynamic resource providers are providers that can be written inside your Pulumi program. Learn how to use dynamic providers and use cases for them.
title: Dynamic providers
h1: Dynamic resource providers
menu:
    iac:
        name: Dynamic providers
        parent: iac-concepts-providers
        weight: 6
    concepts:
        parent: providers
        weight: 6
aliases:
- /docs/intro/concepts/resources/dynamic-providers/
- /docs/concepts/resources/dynamic-providers/
- /docs/iac/concepts/resources/dynamic-providers/
---

The dynamic resource provider construct can be used to build a local provider for simple APIs and use-cases. Dynamic resource providers are only able to be used in Pulumi programs written in the same language as the dynamic resource provider. But, they are lighter weight than custom providers and for many use-cases are sufficient to leverage the Pulumi state model. For more sophisticated APIs, one can create a [bridged or native provider](/docs/iac/packages-and-automation/pulumi-packages/).

{{% notes type="info" %}}
Dynamic providers are supported only in TypeScript and Python.
{{% /notes %}}

{{% notes type="info" %}}
A dynamic provider is often not the best tool for the job. An existing provider, [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/), or the [Command Provider](https://www.pulumi.com/registry/packages/command/) is frequently a better fit. Before authoring one, work through the [decision diagram](/docs/iac/guides/building-extending/providers/dynamic-providers/#when-to-use-a-dynamic-provider) in the guide to confirm you actually need one.
{{% /notes %}}

There are several reasons why you might want to write a dynamic resource provider. Here are some of them:

- You want to create some new custom resource types.
- You want to use a cloud provider that Pulumi doesn't support.

All dynamic providers must conform to certain interface requirements. You must at least implement the `create` function but, in practice, you will probably also want to implement the `update` and `delete` functions as well. Note that `read` is not currently functional for dynamic providers. For the full interface, see [Author a Dynamic Provider](/docs/iac/guides/building-extending/providers/dynamic-providers/).

For example, if creating a dynamic resource provider for WordPress, you would probably want to create new blogs, update existing blogs, and destroy them. The mechanics of how these operations happen would be essentially the same as if you used one of the standard resource providers. The difference is that the calls that would've been made on the standard resource provider by the Pulumi engine would now be made on your dynamic resource provider and it, in turn, would make the API calls to WordPress.

Dynamic providers are defined by first implementing the `pulumi.dynamic.ResourceProvider` interface. This interface supports all CRUD operations, but only the create function is required. A minimal implementation might look like this:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
const myProvider: pulumi.dynamic.ResourceProvider = {
    async create(inputs) {
        return { id: "foo", outs: {}};
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi.dynamic import ResourceProvider, CreateResult

class MyProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_="foo", outs={})
```

{{% /choosable %}}

{{< /chooser >}}

This dynamic resource provider is then used to create a new kind of custom resource by subclassing the dynamic resource base class:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

Extend `pulumi.dynamic.Resource`, which is a subclass of `pulumi.CustomResource`:

```typescript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name: string, props: {}, opts?: pulumi.CustomResourceOptions) {
        super(myProvider, name, props, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

Subclass `pulumi.dynamic.Resource`, which is a subclass of `pulumi.CustomResource`:

```python
from pulumi import ResourceOptions
from pulumi.dynamic import Resource
from typing import Any, Optional

class MyResource(Resource):
    def __init__(self, name: str, props: Any, opts: Optional[ResourceOptions] = None):
         super().__init__(MyProvider(), name, props, opts)
```

{{% /choosable %}}

{{< /chooser >}}

We can now create instances of the new `MyResource` resource type in our program with `new MyResource("name", args)`, just like we would any custom resource. Pulumi understands how to use the custom provider logic appropriately.

Specifically:

1. If Pulumi determines the resource has not yet been created, it will call the create method on the resource provider interface.
1. If another Pulumi deployment happens and the resource already exists, Pulumi will call the diff method to determine whether a change can be made in place or whether a replacement is needed.
1. If a replacement is needed, Pulumi will call create for the new resource and then call delete for the old resource.
1. If no replacement is needed, Pulumi will call update.
1. In all cases, Pulumi first calls the check method with the resource arguments to give the provider a chance to verify that the arguments are valid.
1. If Pulumi needs to read an existing resource without managing it directly, it will call read. (Note: `read` is not currently implemented for dynamic providers.)

For details on each of these functions, see [Author a Dynamic Provider](/docs/iac/guides/building-extending/providers/dynamic-providers/).

## How Dynamic Providers Work

Dynamic providers are a flexible and low-level mechanism that allow you to include arbitrary code directly into the deployment process. While most code in a Pulumi program runs while the desired state of the resources is constructed (in other words, as the resource graph is built), the code inside a dynamic provider's implementation, such as `create` or `update`, runs during resource provisioning, while the resource graph is being turned into a set of CRUD operations scheduled against the cloud provider.

These two phases of execution run in separate processes. The construction of a `new MyResource` happens inside the language-specific process running in your Pulumi program. In contrast, your implementations of create or update are executed by a special resource provider binary called, e.g., `pulumi-resource-pulumi-nodejs`. This binary is what actually implements the Pulumi resource provider gRPC interface and it speaks directly to the Pulumi engine.

Because your implementation of the resource provider interface must be used by a different process, potentially at a different point in time, dynamic providers are built on top of the same [function serialization](/docs/iac/concepts/functions/function-serialization/) that is used for turning callbacks into AWS Lambdas or Google Cloud Functions. Because of this serialization, there are some limits on what can be done inside the implementation of the resource provider interface. You can read more about these limitations in the function serialization documentation.

## Limitations

Dynamic providers are deliberately lightweight, and that comes with trade-offs. Before choosing one, be aware of the following limitations:

- **Single language.** A dynamic provider can only be used from programs written in the same language as the provider. For multi-language support, build a [bridged or native provider](/docs/iac/packages-and-automation/pulumi-packages/).
- **No `read` support.** The `read` method is not currently functional, so [`pulumi import`](/docs/iac/cli/commands/pulumi_import/) and the static [`get` method](/docs/iac/concepts/resources/get/) are not supported. This is tracked in [pulumi/pulumi#16175](https://github.com/pulumi/pulumi/issues/16175).
- **Function serialization limits.** Provider methods are serialized to run in a separate process, which limits what code they can capture. See [function serialization](/docs/iac/concepts/functions/function-serialization/).
- **No pnpm support (TypeScript).** Dynamic providers in TypeScript are incompatible with projects using pnpm as a package manager. Use npm or yarn instead. See [pulumi/pulumi#9085](https://github.com/pulumi/pulumi/issues/9085).
- **No Bun runtime support (TypeScript).** Dynamic providers are not supported with the Bun runtime (`runtime: bun`), because they depend on function serialization, which requires Node.js v8/inspector APIs that Bun [does not fully implement yet](https://bun.com/docs/runtime/nodejs-compat#nodeinspector). Use `runtime: nodejs` instead.
- **Awkward policy authoring.** All dynamic resources share the same resource type (`pulumi-nodejs:dynamic:Resource` for TypeScript or `pulumi-python:dynamic:Resource` for Python), so [Pulumi Policy Packs](/docs/insights/policy/) must identify specific dynamic providers by checking for unique properties. See [Writing policies for dynamic providers](/docs/insights/policy/policy-packs/authoring/#writing-policies-for-dynamic-providers).

## Authoring a dynamic provider

Ready to build one? The [Author a Dynamic Provider](/docs/iac/guides/building-extending/providers/dynamic-providers/) guide covers the full resource provider interface, strongly typed inputs and outputs, credential handling, and complete TypeScript and Python examples.
