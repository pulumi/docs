---
title_tag: "Providers | Guides"
meta_desc: "Learn what a Pulumi provider is, when to build one, and what tools to use depending on your language and starting point."
title: Introduction
h1: Providers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        parent: iac-guides-providers
        weight: 10
---

A [Pulumi provider](/docs/iac/concepts/providers/) is a [Pulumi package](/docs/iac/concepts/packages/) that lets the Pulumi engine manage [resources](/docs/iac/concepts/resources/) — typically scoped to a given cloud platform, SaaS product, or other API.

{{% notes type="info" %}}
The guides in this section are for authors building a provider. For the consumer-side view of what providers are and how programs use them, see [Providers](/docs/iac/concepts/providers/) in the concepts documentation.
{{% /notes %}}

## What's in a provider

A provider package is made up of a schema plus the code that implements it. In practice, that typically means:

- **Custom resources.** The primary contents of a provider are [custom resources](/docs/iac/concepts/resources/) with CRUD operations (create, read, update, delete) for a specific cloud, SaaS, or API. This is what most providers exist to offer.
- **Functions.** A provider may also expose functions — data-source-style reads that return values without managing a resource lifecycle.

{{% notes type="info" %}}
Providers do not typically contain [components](/docs/iac/concepts/resources/components/); components typically live in a separate package (and may incorporate resources managed by several different providers). There is no technical limitation on shipping components in a provider.
{{% /notes %}}

A provider may also be **bridged** from an upstream Terraform or OpenTofu provider, which lets Pulumi reuse the upstream provider's schema and CRUD code rather than reimplementing them. When a provider is not bridged, the schema and CRUD implementations can be generated from an API specification — for some or all resources — or written by hand.

By convention, providers are distributed as an executable plugin with pre-generated SDKs for each Pulumi-supported language. This is not a technical requirement: source-based plugins are also supported (in Go). Providers intended for public consumption can be published in the [Pulumi Registry](/registry/).

## When to build a provider

Providers require a deeper level of Pulumi expertise and maintenance overhead compared to packaging components. Before building a new provider, check whether you can avoid the work:

- **Is there already a Pulumi provider?** Search the [Pulumi Registry](/registry/). If a well-maintained provider exists, use it.
- **Is there a well-maintained Terraform or OpenTofu provider?** If so, reach for [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/), which lets a Pulumi program consume any provider from the OpenTofu registry without writing a Pulumi provider at all.
- **Do you actually need a provider?** If your goal is to group resources into a reusable abstraction, a [component](/docs/iac/guides/building-extending/components/build-a-component/) is usually the right answer. For one-off programmatic resources, a [dynamic provider](/docs/iac/guides/building-extending/providers/dynamic-providers/) may be simpler than a full provider package.

Build a standalone provider when none of the above apply.

## Picking your approach

Two high-level factors shape how you'll build the provider:

- **Writing in Go?** Use the [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/packages/pulumi-go-provider-sdk/) (`pulumi-go-provider`). It infers your schema from Go structs and tags, supplies default implementations for most provider protocol methods, and generates SDKs for every Pulumi-supported language. Go providers also compile to a standalone binary with no runtime dependencies for your users.
- **Writing in another language?** You'll need to implement the provider protocol directly and hand-maintain the schema JSON, which is more work. See [Direct Provider Implementation](/docs/iac/guides/building-extending/providers/implementers/) for Python and TypeScript guides.

For guidance on choosing between the available options, see [Provider Architecture](/docs/iac/guides/building-extending/providers/provider-architecture/).

## Guides in this section

- [Provider Architecture](/docs/iac/guides/building-extending/providers/provider-architecture/) — the three-layer model of the provider stack and how to choose your layer.
- [Build a Provider](/docs/iac/guides/building-extending/providers/build-a-provider/) — step-by-step guide to using the Pulumi Go Provider SDK.
- [Author a Dynamic Provider](/docs/iac/guides/building-extending/providers/dynamic-providers/) — implementing a lightweight provider inline in a TypeScript or Python program.
- [Provider Configuration](/docs/iac/guides/building-extending/providers/provider-configuration/) — declaring configuration keys, secrets, and environment variable defaults in your provider schema.
- [Direct Provider Implementation](/docs/iac/guides/building-extending/providers/implementers/) — implementing providers in Python or TypeScript against the gRPC protocol directly.
- [Debugging Providers](/docs/iac/guides/building-extending/providers/debugging-providers/) — attaching a debugger to a provider locally and debugging bridged providers and tfgen.
