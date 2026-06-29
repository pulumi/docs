---
title_tag: "Packaging Components"
meta_desc: "Learn how to package and distribute Pulumi components via native language packages, source-based plugin packages, or executable-based plugin packages."
title: Packaging Components
h1: Packaging Components
menu:
    iac:
        name: Packaging Components
        parent: iac-guides-components
        weight: 30
aliases:
- /docs/iac/guides/building-extending/components/packaging-a-component/
---

Once you've authored a Pulumi component, you will probably want to package and distribute it so others can use it. This guide covers three ways of packaging a component, each with different trade-offs for distribution, versioning, and discoverability.

## Choosing a packaging approach

The three options differ in whether the component ships as a [Pulumi package](/docs/iac/concepts/packages/) and, if so, which kind of [plugin](/docs/iac/concepts/plugins/) carries it:

1. **Native language package** — a plain language-ecosystem package (npm, PyPI, Go module, etc.) containing a component class. Not a Pulumi package; no Pulumi plugin involved. A good fit for smaller organizations where all Pulumi code is written in the same language.
1. **Source-based plugin package** — a Pulumi package distributed as source. Pulumi generates per-language SDKs on-the-fly when a consumer adds the package, so the components can be consumed from any Pulumi language. A good fit for platform teams providing reusable abstractions and self-service. For more information, see [Authoring a source-based plugin package](/docs/iac/guides/building-extending/packages/source-based-plugin/).
1. **Executable-based plugin package** — a Pulumi package whose plugin is a pre-built executable (typically a Pulumi [provider](/docs/iac/concepts/providers/)). No consumer runtime dependencies, and the package can mix in custom resources and functions alongside components. A good fit for large organizations distributing to many teams and languages, or components destined for public release in the Pulumi Registry. For more information, see [Authoring an executable plugin package](/docs/iac/guides/building-extending/packages/executable-plugin/).

{{% notes type="info" %}}
Most platform teams should choose a source-based plugin package by default: it enables multi-language consumption with minimal authoring overhead and integrates with Pulumi Cloud IDP.
{{% /notes %}}

## Native language packages

A component shipped as a native language package is just a shareable class — you distribute it through the same package manager you'd use for any other library in your language (npm for TypeScript, PyPI for Python, Go modules, NuGet, Maven, etc.). There is no Pulumi plugin, no SDK generation, and no `pulumi package add`.

### Distribution and consumption

Publish to the language's package registry and consume via the native package manager, or import directly from a local path on disk. See [Native language packages](/docs/iac/concepts/components/#native-language-packages) on the components concept page for the per-language install commands.

### Advantages and limitations

- **Lowest overhead**: Components behave like any other class in your language; no SDK generation, no `PulumiPlugin.yaml`.
- **No argument type limitations**: Arguments can use any type (including union types) — they don't need to be serializable.
- **Single language only**: Cannot be consumed from other Pulumi languages.
- **No Pulumi IDP support**: Cannot be published to the Pulumi IDP Private Registry.

## Source-based plugin packages

A source-based plugin package is a [Pulumi package](/docs/iac/concepts/packages/) distributed as source code. Pulumi introspects the package and generates an SDK in the consumer's language when they run `pulumi package add`, so the components are consumable from every Pulumi language — including YAML. For the full authoring workflow, see [Authoring a source-based plugin package](/docs/iac/guides/building-extending/packages/source-based-plugin/).

{{% notes type="info" %}}
A source-based plugin package authored in Go can also expose custom resources and functions (invokes) alongside components, since Go uses [`pulumi-go-provider`](https://github.com/pulumi/pulumi-go-provider) for both. Other languages currently support components only. See [Package contents by authoring language](/docs/iac/guides/building-extending/packages/source-based-plugin/#package-contents-by-authoring-language).
{{% /notes %}}

{{% notes type="info" %}}
A common usage pattern is for a platform team to author components in a general-purpose language (like TypeScript), publish them to Pulumi Cloud IDP for discoverability and auto-generated documentation, and let application teams consume them in the language of their choosing (including YAML). This gives application teams self-service access to infrastructure patterns without needing to know how every individual resource is wired up. Application teams can still add resources directly in their Pulumi code when no suitable component is published.
{{% /notes %}}

### Distribution and consumption

Because the package is distributed as source, you don't have to publish anything to use it — consumers run [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) against a Git URL and revision (or a local path for monorepos and local testing), and Pulumi generates the appropriate language SDK as a [local package](/docs/iac/guides/building-extending/packages/local-packages/).

Source-based plugin packages also support [pre-published SDKs](/docs/iac/guides/building-extending/packages/source-based-plugin/#pre-publishing-language-sdks): authors can generate and publish per-language SDKs to native package registries (npm, PyPI, etc.) as part of CI/CD, letting consumers install via their language's package manager without regenerating the SDK. This is uncommon in practice — for internal packages it typically requires maintaining a **private package feed for every consumer language** (private npm registry, private PyPI index, etc.), which is a large amount of infrastructure to stand up just to avoid local SDK generation. Most teams stick with on-the-fly generation via `pulumi package add`.

Pulumi Cloud customers can publish versions of the package to the Pulumi IDP Private Registry using [`pulumi package publish`](/docs/iac/cli/commands/pulumi_package_publish/). Publishing to Pulumi Cloud gives platform teams a browsable gallery complete with READMEs and auto-generated SDK documentation in every Pulumi language. For guidance on how to group components into packages and repositories so versioning stays meaningful, see [Repository strategy for Pulumi packages](/docs/iac/guides/building-extending/packages/repository-strategy/).

### Advantages and limitations

- **Write and consume in any language**: Components can be authored in any supported Pulumi language and consumed from any other.
- **Flexible distribution**: Ship via a Git reference (consumed with `pulumi package add`) or as pre-built SDKs published to native package registries.
- **Pulumi IDP support**: Can be published to Pulumi Cloud for discoverability and automatic API documentation.
- **SDK regeneration overhead**: Without pre-published SDKs, consumers regenerate the SDK each time the package updates.
- **Runtime dependencies**: Consumers need the runtime for the language the package was authored in (Node.js, Python, a JVM, a Go toolchain, etc.).
- **Argument type limitations**: Calls across the plugin boundary are serialized, so some types are not representable. See [Component arguments and type requirements](/docs/iac/guides/building-extending/components/build-a-component/#component-arguments-and-type-requirements).

## Executable-based plugin packages

An executable-based plugin package is a [Pulumi package](/docs/iac/concepts/packages/) whose plugin is a pre-built executable — typically a Pulumi [provider](/docs/iac/concepts/providers/). The executable has no consumer-side runtime dependencies, and the package can expose [components, custom resources, and functions](/docs/iac/concepts/resources/#resources) together. Because the authoring and CI/CD overhead is higher (and most such packages are written in Go), this approach fits very large organizations distributing to many teams and languages, environments where the source-based runtime dependencies aren't acceptable, or components intended for public release in the Pulumi Registry. For more information, see [Authoring an executable plugin package](/docs/iac/guides/building-extending/packages/executable-plugin/).

{{% notes type="info" %}}
To publish a component for public consumption in the [Pulumi Registry](/registry), author it as an executable-based plugin package in Go and publish per-language SDKs to the public feeds (npmjs.org, PyPI, etc.). See [Publishing Pulumi packages](/docs/iac/guides/building-extending/packages/publishing-packages/).
{{% /notes %}}

### Distribution and consumption

Executable-based plugin packages are usually distributed as pre-built per-language SDKs published to multiple package managers (one per consumer language), with the plugin executable published to an accessible location. Pre-publishing SDKs isn't strictly required — consumers can run [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) to generate an SDK locally from the package schema — but most executable packages pre-publish because, once you're already shipping a binary per release, publishing per-language SDKs is a natural extension. Pulumi Cloud customers can also publish to the Pulumi IDP Private Registry using [`pulumi package publish`](/docs/iac/cli/commands/pulumi_package_publish/).

Consumers install the published SDK like any other Pulumi provider package. Pulumi automatically downloads and caches the plugin executable the first time the consuming program runs.

For guidance on how to group components into packages and repositories so versioning stays meaningful, see [Repository strategy for Pulumi packages](/docs/iac/guides/building-extending/packages/repository-strategy/) — the same strategy applies to source-based and executable-based plugin packages.

### Advantages and limitations

- **No consumer runtime dependencies**: The plugin ships as a native executable, so consumers don't need Node.js, Python, a JVM, or a Go toolchain.
- **Full package capabilities**: Can expose custom resources and functions alongside components. (A source-based plugin package in Go can also do this.)
- **Go strongly recommended**: Providers are usually written in Go because [`pulumi-go-provider`](https://github.com/pulumi/pulumi-go-provider) infers the [schema](/docs/iac/guides/building-extending/packages/schema/) automatically; other languages require hand-authored schemas.
- **CI/CD overhead**: Cross-compiling the plugin executable and (usually) pre-publishing SDKs requires a more involved release pipeline.
- **Argument type limitations**: Same serialization limits as source-based plugin packages — see [Component arguments and type requirements](/docs/iac/guides/building-extending/components/build-a-component/#component-arguments-and-type-requirements).

{{% notes type="info" %}}
Executable-based plugin packages can technically be written in any language if the author is willing to hand-author the schema, but this is labor-intensive and the learning curve can be prohibitive. Pulumi ships schema inference tooling only for Go (via [`pulumi-go-provider`](https://github.com/pulumi/pulumi-go-provider)).

Consuming an executable-based plugin package whose plugin is written in a non-Go language requires consumers to have that language's runtime installed — the same situation as a source-based plugin package.
{{% /notes %}}

## Packaging summary

| Feature | Native language package | Source-based plugin package | Executable-based plugin package |
|---------|--------------------------|-------------------------------------------|--------------------------|
| **Best for** | Smaller organizations using a single language | Platform teams providing reusable abstractions and self-service | Distribution to many teams/languages, specific runtime constraints, or public Registry release |
| **Cross-language consumption** | No — limited to the authoring language | Yes — consume in any Pulumi language | Yes — consume in any Pulumi language |
| **Pulumi Cloud IDP Private Registry support** | No | Yes | Yes |
| **Packaging complexity** | Minimal — publish a native package | Low — `PulumiPlugin.yaml` plus an entry file | High — schema authoring, SDK generation, and executable publishing |
| **Distribution** | Native package managers (npm, PyPI, etc.) | Git reference (via `pulumi package add`) or pre-built SDKs on native package managers | Published plugin executable plus per-language SDKs (usually pre-published to npm, PyPI, etc.; can also be generated locally) |
| **Consumer runtime dependencies** | n/a | Authoring language's runtime | None — plugin is a native executable |
