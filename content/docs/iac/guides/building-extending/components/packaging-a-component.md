---
title_tag: "Packaging a Component"
meta_desc: "Learn how to package and distribute Pulumi components using single-language, cross-language, and provider-based approaches."
title: Packaging a Component
h1: Packaging a Component
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Package a Component
        parent: iac-guides-components
        weight: 30
aliases:
- /docs/iac/guides/building-extending/components/packaging-a-component/
---

Once you've authored a Pulumi component, you will probably want to package and distribute it so others can use it. This guide covers three different approaches to packaging components, each with different trade-offs for distribution, versioning, and discoverability.

## Choosing a packaging approach

Pulumi offers three ways to package components:

1. **[Single-language components](#single-language-components)**: Share components as source code with native package managers. Single-language components are a good fit for smaller organizations where all Pulumi code is written in a single language.
1. **[Cross-language components](#cross-language-components)**: Support multiple languages with auto-generated SDKs from a single implementation. Cross-language components are a good fit for platform teams who want to create reusable abstractions to consume internally or to provide self-service for application teams.
1. **[Provider-based components](#provider-based-components)**: Build components as Pulumi providers with zero runtime dependencies for consumers. Provider-based components are a good fit for organizations with a high degree of Pulumi expertise who expect to distribute components to a large number of teams across many languages or organizations with specific runtime requirements.

{{% notes type="info" %}}
Most platform teams should consider cross-language components as their default option because they provide multi-language consumption with minimal overhead and also have enhanced support within Pulumi Cloud.
{{% /notes %}}

## Single-language components

Single-language components are written and consumed in the same language and behave just like any other shareable class in your language of choice. You distribute single-language components by publishing packages in the language's package manager (npm, PyPI, etc.). Because single-language components are limited to the language of authorship, they are a good fit for smaller teams or organizations that expect to only ever use Pulumi in a single language.

### Distribution and consumption

Single-language components are distributed via the native package management tool for the language in which the component is authored: npm for TypeScript, PyPI for Python, Go modules, etc. They are consumed by adding a reference to the package (or importing from a local path on disk), just like any other module or package.

### Advantages and limitations

When considering single-language components, bear the following tradeoffs in mind:

- **Lowest overhead**: Components work like any other class in your language and do not require SDKs
- **No argument type limitations**: Arguments to single-language components can use any type, including union types, as they do not need to be serializable
- **Single language only**: Cannot be consumed from other Pulumi languages
- **No Pulumi IDP support**: Cannot be published to Pulumi IDP Private Registry at this time

## Cross-language components

Cross-language components support consumption in any Pulumi language. You implement the component once in your preferred language, and Pulumi automatically generates SDKs via [local packages](/docs/iac/guides/building-extending/packages/local-packages/) for other languages when the component is added to a downstream Pulumi program.

For detailed information on packaging and using cross-language components, see [Cross-language Components](/docs/iac/concepts/components/cross-language-components/).

{{% notes type="info" %}}
A common usage pattern for cross-language components is for a platform team to author components in a general purpose language (like TypeScript), publish those components in Pulumi Cloud IDP for discoverability and auto-generated documentation, and then allow application teams to consume those components so they can compose the infrastructure for their applications in the language of their choosing (including YAML).

This pattern gives a high degree of self-service to application teams so that they are able to consume infrastructure patterns without needing to know the details about how to create and connect every individual resource. Applications teams are still free to add additional resources to their Pulumi code in cases where the platform team does not have a suitable component published.
{{% /notes %}}

### Distribution and consumption

Because cross-language components are distributed as source, they do not need to be explicitly published. Consumers use the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command to install the component, specifying a git URL and revision (or a local path for monorepos or local testing), and Pulumi automatically generates the appropriate language SDK as a [local package](/docs/iac/guides/building-extending/packages/local-packages/).

Pulumi Cloud customers can explicitly publish versions of components to Pulumi IDP Private Registry using the [`pulumi package publish`](/docs/iac/cli/commands/pulumi_package_publish/) command. Publishing a package to Pulumi Cloud gives platform teams the ability to provide self-service to application teams by sharing components in a browsable gallery complete with READMEs and auto-generated SDK documentation in all Pulumi languages.

### Advantages and limitations

When considering cross-language components, bear the following tradeoffs in mind:

- **Write and consume in any language**: Cross-language components can be written in and consumed by any supported Pulumi language
- **Lowest overhead for distribution**: Cross-language components are distributed as source via git references (SHA, branch, or tag) and do not require a build artifact (binary or published SDKs) in order to be consumed
- **Pulumi IDP support**: Can be published to Pulumi Cloud for discoverability and automatic API documentation
- **SDK regeneration overhead**: Consumers must regenerate SDKs when the component is updated
- **Runtime dependencies**: Consumers must have the runtime installed for the language in which the component is written (Node.js, Python, etc.)
- **Argument type limitations**: Because calls to cross-language components are serialized, there are some limitations on the types that can be included in the component's resources. For more information see [Component arguments and type requirements](/docs/iac/concepts/components/#component-arguments-and-type-requirements)

## Provider-based components

Provider-based components are built as full Pulumi [providers](/docs/iac/concepts/providers/). They compile to native binaries with no runtime dependencies and can include both [component resources and custom resources](/docs/iac/concepts/resources/#resources). Because provider-based components have a higher overhead for CI/CD and publishing, and in most cases are written in Go, they are a fit for very large organizations that have many teams using many different languages, or organizations where the runtime requirements for cross-language components are not suitable.

{{% notes type="info" %}}
If you want to create a component for public consumption and publish it in the [Pulumi Registry](/registry), you should create a provider-based component, author it in Go, and publish SDKs in the public feeds for each language (npmjs.org, etc.).

For more information on submitting packages to the Pulumi Registry, see [Publishing Pulumi packages](/docs/iac/guides/building-extending/packages/publishing-packages/).
{{% /notes %}}

### Distribution and consumption

Provider-based components are typically distributed as pre-built SDKs published to multiple package managers (one for each language a consumer would use). The provider binary must also be published in an accessible location.

Consumers install the published SDKs (like any other Pulumi provider package). Pulumi will automatically download (and cache) the provider binary when the consuming Pulumi program is first run (just like providers).

For more information on authoring providers see [Build a provider](/docs/iac/guides/building-extending/providers/build-a-provider/)

### Advantages and Limitations

When considering provider-based components, bear the following tradeoffs in mind:

- **No runtime dependencies for consumers**: Consumers don't need Node.js, Python, or any other runtime installed because the provider plugin is distributed as a native binary
- **Full provider capabilities**: In addition to any components you want to include in the package, provider packages written in Go can also include custom resources that make direct API calls
- **Go strongly recommended**: Providers are usually written in Go because the Pulumi supported tooling makes maintaining the provider [schema](/docs/iac/guides/building-extending/packages/schema/) significantly easier compared to other languages (see note for details)
- **CI/CD Overhead**: Provider-based components typically have pre-published SDKs, which requires a more involved CI/CD process (including publishing to a package feed after a release)
- **Argument type limitations**: Because calls to provider-based components are serialized, there are some limitations on the types that can be included in the component's resources. For more information see [Component arguments and type requirements](/docs/iac/concepts/components/#component-arguments-and-type-requirements)
- **No Pulumi IDP support**: Cannot be published to Pulumi IDP Private Registry

{{% notes type="info" %}}
Providers (and provider-based components) may technically be written in any language if the author is willing to hand-author the schema. Maintaining schemas by hand is labor-intensive and the learning curve maintaining schemas may be prohibitive for many teams. Pulumi provides tooling in the [`pulumi-go-provider`](https://github.com/pulumi/pulumi-go-provider) framework to automatically infer the schema and reduce the need for manually maintained schema files. Pulumi does not provide tooling for inferring schemas in languages other than Go.

Consuming providers written in languages other than Go requires consumers to have the runtime of the provider's language installed, similar to Cross-language components.
{{% /notes %}}

## Component packaging summary

The table below summarizes the trade-offs between the three packaging approaches:

| Feature | Single-language components | Cross-language components | Provider-based components |
|---------|--------------------------|-------------------------------------------|--------------------------|
| **Best for** | Smaller organizations using a single language | Platform teams providing reusable abstractions and self-service | Organizations distributing to many teams/languages or with specific runtime requirements, or components designed for public consumption |
| **Cross-language consumption** | No - limited to original language | Yes - consume in any Pulumi language | Yes - consume in any Pulumi language|
| **Pulumi Cloud IDP Private Registry support** | No | Yes | No |
| **Packaging complexity** | Minimal - publish a native package | Low - requires PulumiPlugin.yaml and entry points | High - requires schema authoring, SDK generation, and binary publishing |
| **Distribution** | Source published to package managers (npm, PyPI, etc.) | Pulumi IDP Private Registry and/or git references | Pre-built SDKs published to native package managers |
| **Runtime dependencies** | n/a | Language runtime for authoring language required | None - distributed as native binary |
