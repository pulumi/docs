---
title_tag: "Packages & Dependencies | Language Essentials"
meta_desc: Learn how each language's package manager fits into Pulumi, installing providers, pinning versions, and publishing components.
title: Packages
h1: Packages and Dependencies
menu:
    iac:
        name: Packages & Dependencies
        parent: iac-guides-language-essentials
        weight: 60
aliases:
    - /docs/iac/guides/language-essentials/packages-and-dependencies/
---

A package is a unit of code you install rather than write. You already depend
on this idea: a Terraform provider comes from a registry, and a Pulumi YAML
program declares the providers it needs in its project file. In a
general-purpose language, that dependency is managed by the language's own
package manager, which resolves versions, downloads code, and records exactly
what your program depends on.

## The package manager per language

Every Pulumi language uses that language's standard tooling; there's no
Pulumi-specific package format to learn.

- **TypeScript and JavaScript**: npm or Yarn, with dependencies declared in
  `package.json`.
- **Python**: pip, uv, or Poetry, with dependencies declared in
  `requirements.txt` or `pyproject.toml`.
- **Go**: Go modules, with dependencies declared in `go.mod`.
- **C#**: NuGet, with dependencies declared in the project's `.csproj` file.
- **Java**: Maven, with dependencies declared in `pom.xml`.

Importing a package into your program uses that language's own import syntax:
`import * as aws from "@pulumi/aws"` in TypeScript, `import pulumi_aws as aws`
in Python, and so on. There's nothing to configure beyond what you'd already
do for any other dependency.

## Providers are packages too

A cloud provider, such as AWS, Azure, or Google Cloud, is distributed as an
ordinary package in your language's package registry, paired with a plugin
binary that Pulumi downloads and runs. When you scaffold a new project with
`pulumi new`, the template's package file already lists the providers it
uses, and `pulumi install` resolves and downloads everything, dependencies
and plugins alike. You rarely have to think about the plugin layer directly;
it's there so the same provider works consistently across every supported
language.

## What to watch out for

Pin your versions and commit your lockfile, the same discipline you already
apply to Terraform provider version constraints. It matters more here than in
application code, because an unpinned provider upgrade can change a
resource's default behavior between one `pulumi up` and the next, not just
its API surface. Treat a provider or package upgrade as a deliberate,
reviewed change.

The [Pulumi Registry](/registry/) is where providers and Pulumi packages,
including components other teams have published, are discovered and
documented for every supported language. For components that are specific to
your organization and shouldn't be public, Pulumi Cloud supports private
packages, so you get the same install-and-import experience internally
without publishing anything externally.

## Next steps

Revisit the [series overview](/docs/iac/guides/basics/language-essentials/) or apply
what you've learned by
[organizing your projects and stacks](/docs/iac/guides/basics/organizing-projects-stacks/).

## Learn more

- [Building and publishing packages](/docs/iac/guides/building-extending/packages/)
  for authoring a Pulumi package that other teams and languages can consume.
