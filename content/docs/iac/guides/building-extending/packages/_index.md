---
title_tag: "Pulumi Packages Guides"
meta_desc: Pulumi packages let you author infrastructure abstractions and consume them in any Pulumi language via source-based or executable-based plugins.
title: Pulumi Packages Guides
h1: Pulumi Packages Guides
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Packages
    identifier: iac-guides-packages
    parent: iac-guides-building-extending
    weight: 2
---

A [Pulumi package](/docs/iac/concepts/packages/) bundles components or a provider with a plugin so Pulumi can generate an SDK for any supported language. Package authors choose between two distribution models — source-based and executable-based — which differ in consumer runtime requirements, registry support, and publishing overhead.

{{% notes type="info" %}}
Native language packages (npm, PyPI, Go modules, etc.) are another option for sharing components within a single language — see [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) for details.
{{% /notes %}}

## Package types

### Source-based plugin package

A Pulumi package distributed as source code. SDKs are usually generated locally by the Pulumi CLI when consumers run `pulumi package add` against a Git URL, a local path, or a `PulumiPlugin.yaml` in an existing repo — though you can also pre-publish per-language SDKs to native package registries if you prefer. The runtime requirements for consumers are the same as for any Pulumi program written in the authoring language: Node.js for TypeScript, Python for Python, a JVM for Java, and so on. Compiled Go and .NET components have no additional consumer runtime requirement.

Choose this when:

- You want multi-language consumption with the least authoring overhead.
- Your consumers can reasonably install the authoring language's runtime.
- You're publishing to the Pulumi IDP Private Registry, or to no registry at all (source-based packages work fine consumed directly from Git).

See [Authoring a Source-Based Plugin Package](./source-based-plugin/) for the full workflow.

### Executable-based plugin package

A Pulumi package whose plugin is a pre-built executable, typically a Pulumi [provider](/docs/iac/concepts/providers/). The Pulumi CLI downloads the binary at `pulumi install` time from a `pluginDownloadURL` and runs it as a subprocess, so no authoring-language runtime is required on the consumer's machine. SDKs are usually pre-published to npm, PyPI, NuGet, Maven Central, and as a tagged Go module — consumers can still generate SDKs locally from the schema, but since you're already running a CI/CD pipeline to publish binaries, publishing the SDKs alongside is a natural extension.

Pulumi only provides supported tooling for authoring executable plugins in Go (via [`pulumi-go-provider`](./pulumi-go-provider-sdk/)), and for practical purposes new executable plugins should be written in Go. Other languages are documented but require hand-authoring the schema and managing serialization details yourself.

Choose this when:

- You are publishing to the public [Pulumi Registry](/registry/).
- You need to expose custom resources or provider functions from any authoring language.
- You want zero consumer runtime dependencies and are willing to invest in cross-compilation and (usually) per-language SDK publishing.

See [Authoring an Executable Plugin Package](./executable-plugin/) for the full workflow.

## Comparison

| | Source-based plugin package | Executable-based plugin package |
|---|---|---|
| Consumer runtime required | Authoring language | None |
| Custom resources and functions | Go only via [`pulumi-go-provider`](./source-based-plugin/#package-contents-by-authoring-language) | Yes (all languages) |
| Pulumi IDP Private Registry | Supported | Supported |
| Public Pulumi Registry | Not supported today | Supported |
| Pre-publishing SDKs | Optional (usually generated locally) | Typical (consumers can still generate locally) |
| Publishing overhead | Low | High |
| Iteration speed | Fast | Slower |

## Guides in this section

- [Authoring a Source-Based Plugin Package](./source-based-plugin/) — author a Pulumi package distributed as source and consumed via `pulumi package add`. Pulumi generates the SDK in the consumer's language on demand.
- [Authoring an Executable Plugin Package](./executable-plugin/) — cross-compile a plugin binary, configure `pluginDownloadURL`, and publish per-language SDKs so the package runs on any consumer with no runtime dependency.
- [Publishing a Package to the Pulumi Registry](./publishing-packages/) — publish to the public Pulumi Registry.
- [Publishing Components from GitHub Actions](/docs/idp/guides/publishing-from-github-actions/) — publish to the Pulumi IDP Private Registry.
- [Repository Strategy for Pulumi Packages](./repository-strategy/) — group components and providers across repositories and versions; applies to both source-based and executable-based packages.
- [Local Packages](./local-packages/) — consume a package from a local path for iteration and monorepos.
- [Pulumi Go Provider SDK](./pulumi-go-provider-sdk/) — build components, custom resources, and functions in Go.
- [Schema Reference](./schema/) — Pulumi package schema for providers.
