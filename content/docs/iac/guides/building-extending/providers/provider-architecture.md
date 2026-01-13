---
title_tag: "Provider architecture"
meta_desc: "Understand the layered architecture of Pulumi providers and choose the right level of abstraction for your needs."
title: Provider architecture
h1: Provider architecture
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Provider architecture
        parent: iac-guides-providers
        weight: 20
---

A Pulumi provider allows you to define new resource types, enabling integration with virtually any service or tool. Providers are how Pulumi communicates with cloud platforms, SaaS APIs, and other external systems to create, read, update, and delete resources.

{{% notes type="info" %}}
Pulumi also supports [dynamic providers](/docs/iac/concepts/providers/dynamic-providers/), which are lightweight providers defined inline within a Pulumi program. This page focuses on standalone providers that are built and distributed as separate packages.
{{% /notes %}}

Pulumi providers are built on a layered architecture. Understanding these layers helps you choose the right approach for your needs—from high-level SDKs that handle complexity for you, to low-level protocol access for maximum control.

## The three layers

```
┌─────────────────────────────────────────┐
│      Higher-level SDKs (Layer 3)        │  Convenience + opinions
│         e.g., pulumi-go-provider        │  Schema inference, middleware
├─────────────────────────────────────────┤
│   Generated language bindings (Layer 2) │  Direct implementation
│      Go, Python, TypeScript, etc.       │  Full control, any language
├─────────────────────────────────────────┤
│     gRPC/Protobuf protocol (Layer 1)    │  The wire format
│           provider.proto                │  Language-agnostic contract
└─────────────────────────────────────────┘
```

### Layer 1: The provider protocol

At the foundation is the [provider protocol](https://github.com/pulumi/pulumi/blob/master/proto/pulumi/provider.proto), defined using [gRPC](https://grpc.io/) and [Protocol Buffers](https://protobuf.dev/). This specifies exactly how the Pulumi engine communicates with providers.

The protocol defines approximately 20 RPC methods. The most important are `Configure` for initializing the provider with credentials and settings, `GetSchema` for returning the provider's resource and type definitions, `Check` for validating and transforming resource inputs, `Diff` for computing changes between current and desired state, and the CRUD operations `Create`, `Read`, `Update`, and `Delete` for managing resource lifecycle.

This layer is language-agnostic. Any language that can implement a gRPC server can implement a Pulumi provider.

For protocol details, see [Provider protocol reference](/docs/iac/guides/building-extending/providers/implementers/protocol-reference/).

### Layer 2: Generated language bindings

The Protocol Buffers definition generates native classes and interfaces for each language—Go, Python, TypeScript, Java, C#, and any other language with gRPC support. These generated bindings give you direct access to the provider protocol in idiomatic code for your language.

At this layer, you implement the provider interface directly. You write your [schema JSON](/docs/iac/guides/building-extending/packages/schema/) by hand, giving you complete control over resource definitions, property types, and how data structures map between Pulumi and your provider. This explicit control over the schema is particularly valuable when you need precise type mappings or want to define resources that don't fit standard patterns.

Choose this layer when you need a provider in a language without a higher-level SDK, when you want full control over your schema and data structure mappings, when you're building something unusual that doesn't fit SDK patterns, or when you prefer explicit protocol handling over framework abstractions.

For implementation guides, see [Direct implementation in Python](/docs/iac/guides/building-extending/providers/implementers/python/), [Direct implementation in Go](/docs/iac/guides/building-extending/providers/implementers/go/), or [Direct implementation in TypeScript](/docs/iac/guides/building-extending/providers/implementers/typescript/).

### Layer 3: Higher-level SDKs

SDKs build on the language bindings to provide a more ergonomic development experience. Currently, the [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/) is available for Go.

The Go SDK provides schema inference from Go structs and tags, default implementations for most methods, middleware support for cross-cutting concerns, a testing framework for provider validation, and automatic multi-language SDK generation.

Choose this layer when you're writing a provider in Go and want the fastest path to a working provider. It's ideal when you prefer convention over configuration and want automatic schema generation.

## Choosing your layer

| Consideration | Layer 2 (Direct) | Layer 3 (SDK) |
|---------------|------------------|---------------|
| **Language** | Any with gRPC support | Go only (currently) |
| **Schema** | Hand-written JSON | Inferred from code |
| **Boilerplate** | More | Less |
| **Control** | Full | Framework-guided |
| **Learning curve** | Protocol knowledge required | Go SDK patterns |

### Choosing a language

Many teams prefer to write providers in their standard language, giving them access to familiar tools and libraries. However, Go has a significant advantage: providers written in Go compile to standalone binaries with no runtime dependencies. Users of your provider can consume it from any Pulumi language without installing Go.

Providers written in Python or TypeScript require their respective runtimes to be installed, which adds friction for users. You can bundle Python providers with [PyInstaller](https://pyinstaller.org/) or TypeScript providers with [pkg](https://github.com/vercel/pkg) to create standalone executables, though this adds build complexity. That said, if your team is more productive in Python or TypeScript, the familiar ecosystem and libraries may outweigh the runtime dependency—especially for internal providers where you control the deployment environment.

### When to use Layer 2 (direct implementation)

Direct implementation is the right choice when you want complete control over your provider's schema and how data structures are mapped. It's also the path for languages without a higher-level SDK, such as Python or TypeScript. Choose this layer when you need precise control over Check/Diff/Update behavior, when your provider doesn't fit standard CRUD semantics, or when you want to understand exactly how providers work at the protocol level.

### When to use Layer 3 (SDK)

The SDK approach is ideal for Go providers where the SDK handles most complexity for you. It works well when your resources follow typical CRUD patterns, when you want automatic SDK generation for multiple languages, and when you want built-in testing infrastructure.

## What all providers need

Regardless of which layer you choose, every provider needs a schema defining resources, their inputs, outputs, and configuration. It also needs CRUD implementations for each resource type, configuration handling for credentials and settings, and proper diffing to detect what changed.

The schema can be hand-written JSON when using Layer 2, or inferred from code when using the Layer 3 SDK. See [Schema reference](/docs/iac/guides/building-extending/packages/schema/) for the complete schema specification.

## Next steps

To get started quickly with the Go SDK, see [Build a provider](/docs/iac/guides/building-extending/providers/build-a-provider/). For direct implementation, start with the [Protocol reference](/docs/iac/guides/building-extending/providers/implementers/protocol-reference/). For Python providers specifically, see [Direct implementation in Python](/docs/iac/guides/building-extending/providers/implementers/python/). For schema details, see [Schema reference](/docs/iac/guides/building-extending/packages/schema/).
