---
title_tag: Pulumi Packages
meta_desc: Pulumi Packages enable you to write infrastructure abstractions once in TypeScript, C#, Go, or Python and make them available for use in any Pulumi language.
title: Pulumi packages
h1: Pulumi packages
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Packages
        parent: iac-concepts
        weight: 105
aliases:
- /docs/iac/guides/packages/
- /docs/guides/pulumi-packages/
- /docs/using-pulumi/pulumi-packages/
- /docs/iac/packages-and-automation/pulumi-packages/
- /docs/iac/using-pulumi/pulumi-packages/
- /docs/iac/concepts/packages/
- /docs/iac/guides/building-extending/packages/
- /docs/iac/guides/building-extending/packages/packages/
---

Pulumi Packages are the core technology that enables Pulumi [resources](/docs/iac/concepts/resources/), [components](/docs/iac/concepts/components/), and [functions](/docs/iac/concepts/functions/) to be defined once and used in all Pulumi languages.

## How packages work

Pulumi packages consist of two parts that allow them to be consumed in any Pulumi language:

1. **The [provider plugin](/docs/iac/concepts/plugins/#resource-plugins)** which contains Pulumi code and can be written in any language Pulumi supports. The provider plugin contains custom resources, functions, and components. Custom resources define CRUD operations for infrastructure resources. Functions query cloud providers for resource data. Components encapsulate custom resources or other components into reusable abstractions.
1. **An SDK** in the language of the consuming program, which is generated from the provider's schema file. SDKs may be published and hosted on package feeds (npm, PyPI, etc.) or they may be generated locally by the Pulumi CLI (in combination with the package schema) when the package is added to your Pulumi program.

## Consuming packages

There are two ways to add Pulumi packages to your program:

- **Packages with published SDKs**: Use your language's standard package manager. Most packages in the [Pulumi Registry](/registry/) have published SDKs. Each package's Installation & Configuration page shows the specific command for your language ([example](/registry/packages/aws/installation-configuration/)).
- **Local packages**: Use [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/), which generates an SDK locally and adds a reference to `Pulumi.yaml`. This is used for components, Terraform providers, and other packages without published SDKs.

### Installing packages

To install all dependencies, use [`pulumi install`](/docs/iac/cli/commands/pulumi_install/). This is the recommended approach because it handles both standard package manager dependencies (from `package.json`, `requirements.txt`, etc.) and any local packages defined in `Pulumi.yaml` in a single command.

Run `pulumi install` when:

- Setting up a project after cloning from source control
- Adding or updating packages
- Ensuring all team members have the same dependencies

### Adding local packages

For packages without published SDKs, called [local packages](/docs/iac/guides/building-extending/packages/local-packages/), use the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command. This downloads the provider plugin, generates a local SDK in your language, and adds the package to your `Pulumi.yaml`:

```bash
# Example: Add a Terraform provider
pulumi package add terraform-provider hashicorp/random

# Example: Add a component from a git repository
pulumi package add example.com/org/repo.git/path@version
```

After adding a local package, run `pulumi install` to complete the installation.

Some common use cases for local packages include:

1. Using the [Any Terraform provider](/registry/packages/terraform-provider/) to generate a local SDK for a Terraform provider. (This feature allows you to consume any Terraform provider in a Pulumi program.)
1. Using the [Azure Native provider](/registry/packages/azure-native/) to [generate a local SDK for a specific version of the Azure API](/registry/packages/azure-native/version-guide/#accessing-any-api-version-via-local-packages).
1. Consuming a Pulumi component published in [Pulumi IDP](/docs/idp/), or directly via a Git reference.

In order to consume a Pulumi package, there may be additional runtime requirements. Runtime requirements differ by the language in which the package is written:

- TypeScript packages require the NodeJS runtime.
- Python packages require a Python interpreter.
- Go packages do not require a runtime if they are compiled. If they are referenced via source (e.g. a Pulumi component published via Pulumi IDP), they require a compatible version of the Go language to be installed.
- .NET packages do not require a runtime if they are compiled as runtime-included binaries, which is Pulumi's recommended approach. .NET packages compiled as runtime-dependent binaries require a runtime.
- Java packages require a JVM runtime.
- YAML packages do not have any specific runtime requirements.

{{% notes type="info" %}}
Packages in the Pulumi Registry are typically written in Go and are compiled, and therefore do not require a runtime. This includes all packages for popular cloud and SaaS providers.
{{% /notes %}}

## The Pulumi Registry

The Pulumi Registry contains a listing of popular Pulumi packages, and each package's Installation & Configuration page contains instructions on how to install the SDK for the provider ([example](/registry/packages/aws/installation-configuration/)). Most packages in the Pulumi Registry have published SDKs, including all of the packages for the major cloud providers. For packages that do not have published SDKs, the package's main page will show how to generate an SDK ([example](/registry/packages/honeycombio/#generate-provider)).

## Authoring packages

There are two common cases for authoring packages:

1. You are authoring a Pulumi component to be shared within your team, organization, or by anyone in the Pulumi community.
1. You are authoring a Pulumi provider that allows your package's consumers to manage resources for a cloud or SaaS provider. (You might optionally publish this provider in the Pulumi Registry if you intend it for public consumption.)

### Authoring a component for distribution

If you are authoring a Pulumi component to be shared within your team or organization, you will need to decide whether to use local packages or publish SDKs. **Most component authors will want consumers to use local packages** for the following reasons:

- Most component authors will want to use local packages because publishing SDKs requires significant overhead: your CI/CD process will need to generate SDKs for all Pulumi languages (or at least all the languages your package consumers will use) and you will need package feeds to host those published SDKs.
- If you are authoring **components only** (not custom resources), you can write them in any Pulumi language. However, if you want to publish SDKs for your components, you'll need to use the [Pulumi Provider SDK](/docs/iac/guides/building-extending/providers/pulumi-provider-sdk/) (written in Go) to generate the schema that enables multi-language SDK generation. For components, this added complexity is usually not worth the effort compared to using local packages.

For an example of building and publishing a component with local packages, see [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/).

{{% notes type="info" %}}
You can author a Pulumi package in any language, create a hand-authored schema, then generate and publish SDKs from that schema. However, this approach requires significant effort to manage at scale, as you'll need to maintain the schema manually and ensure it stays synchronized with your provider code.
{{% /notes %}}

However, using Pulumi Provider SDK and publishing SDKs might work better when:

- If the component is intended for internal use and your organization has security policies that restrict the ability of developers to install software on their devices (specifically, a required runtime for your package), writing your component in Go and publishing it as a binary with published SDKs hosted in an internal package feed will make it easier for consumers to use your package.
- If you are intending to publish your component(s) in the Pulumi Registry for general public consumption, you should write your component in Go, and publish it as a binary with published SDKs hosted in the standard public package feeds (i.e., npm, PyPI, etc.). Note that the Pulumi Registry requires package contributors to generate SDKs in all languages Pulumi supports.
- Your team is comfortable writing and maintaining code in Go.
- Your organization already has the package feeds necessary to host SDKs in all languages that might consume the component.

### Authoring a Pulumi provider

If you are authoring a Pulumi provider that allows consumers to manage resources for a new cloud or SaaS provider, you should author your provider in Go using [Pulumi Provider SDK](/docs/iac/guides/building-extending/providers/pulumi-provider-sdk/).

For a guide to authoring your provider, see [Build a Provider](/docs/iac/guides/building-extending/providers/build-a-provider/). For a guide to publishing your provider in the Pulumi Registry, see [Publishing Pulumi Packages](/docs/iac/guides/building-extending/packages/publishing-packages/).
