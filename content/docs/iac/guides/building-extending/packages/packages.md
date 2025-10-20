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
---

Pulumi Packages are the core technology that enables Pulumi [resources](/docs/iac/concepts/resources/), [components](/docs/iac/concepts/components/), and [functions](/docs/iac/concepts/functions/) to be defined once and made available to users in all Pulumi languages.

## How packages work

Pulumi packages consist of two parts that allow them to be consumed in any Pulumi language:

1. **The provider plugin** which contains Pulumi code and can be written in any language Pulumi supports. The Pulumi code in the provider plugin is comprised of some combination of custom resources (the most basic Pulumi resource type where you define the CRUD operations), functions (which allow you to query cloud providers for resources) or components (which encapsulate custom resources or even other components).
1. **An SDK** in the language of the consuming program, which is generated from the provider's schema file. SDKs may be published and hosted on package feeds (npm, PyPI, etc.) or they may be generated locally by the Pulumi CLI (in combination with the package schema) when the package is added to your Pulumi program.

## Consuming packages

The method of consuming a Pulumi package depends on whether the package has published SDKs or not:

- For packages with published SDKs, you can consume the package by adding a reference to the published SDK from the package feed, e.g. `npm install`, `dotnet package add`, etc. The published SDKs contain commands to automatically download the provider code/binary.
- For packages without published SDKs, called [local packages](/docs/iac/guides/building-extending/packages/local-packages/#updating-local-packages), you can consume a package via the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command, which will download the package, either read (or dynamically generate) its schema, and generate a local SDK based on the schema file. The local SDKs may be committed to version control, or they can be regenerated at any time with the [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) command.

Some common use cases for local packages include:

1. Using the [Any Terraform provider](/registry/packages/terraform-provider/) to generate a local SDK for a Terraform provider. (This feature allows you to consume any Terraform provider in a Pulumi program.)
1. Using the [Azure Native provider](/registry/packages/azure-native/) to [generate a local SDK for a specific version of the Azure API](/registry/packages/azure-native/version-guide/#accessing-any-api-version-via-local-packages).
1. Consuming a Pulumi component published in [Pulumi IDP](/docs/idp/), or directly via a Git reference.

In order to consume a Pulumi package, you must have the runtime installed for the language in which the provider is written. For example, if a package is written in TypeScript, any consumers of the package will require the NodeJS runtime to be installed in order to use the package.

Go compiles to a native binary and does not require a runtime, and thus has the lowest overhead for package consumers. Most Pulumi packages in the Pulumi Registry (including all of the packages for the major cloud providers) are written in Go.

## The Pulumi Registry

The Pulumi Registry contains a listing of popular Pulumi packages, and each package's Installation & Configuration page contains instructions on how to install the SDK for the provider ([example](/registry/packages/aws/installation-configuration/)). Most packages in the Pulumi Registry have published SDKs, including all of the packages for the major cloud providers. For packages that do not have published SDKs, the package's main page will show how to generate an SDK ([example](/registry/packages/terraform-provider/installation-configuration/#usage)).

## Authoring packages

There are two common cases for authoring packages:

1. You are authoring a Pulumi component to be shared within your team, organization, or by anyone in the Pulumi community.
1. You are authoring a Pulumi provider that allows your package's consumers to manage resources for a cloud or SaaS provider. (You might optionally publish this provider in the Pulumi Registry if you intend it for public consumption.)

### Authoring a component for distribution

If you are authoring a Pulumi component to be shared within your team or organization, you will need to decide whether to use local packages or publish SDKs. **Most component authors will want consumers to use local packages** for the following reasons:

- The overhead of publishing SDKs can be significant: your CI/CD process will need to generate SDKs for all Pulumi languages (or at least all the languages your package consumers will use) and you will need package feeds to host those published SDKs.
- Pulumi only offers tooling for writing packages with published SDKs in Go, the [Pulumi Provider SDK](/docs/iac/guides/building-extending/providers/pulumi-provider-sdk/).

For an example of building and publishing a component with local packages, see [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/).

{{% notes type="info" %}}
It is technically possible to author a Pulumi provider in any language, create a hand-authored schema, then generate and publish SDKs from the hand-authored schema. Most organizations will find this approach difficult to manage at scale.
{{% /notes %}}

However, there are some circumstances when using Pulumi Provider SDK and publishing SDKs may be a better option:

- The requirement for consumers to install the package language's runtime is onerous. This may be because you have a large number of development teams that all want to write Pulumi in different languages, or you are writing a component for public consumption. The [Pulumi EKS package](/registry/packages/eks/) is an example of the latter use case.
- Your team is comfortable writing and maintaining code in Go.
- Your organization already has the package feeds necessary to host SDKs in all languages in which the component may be consumed.

### Authoring a Pulumi provider

If you are authoring a Pulumi provider that allows consumers to manage resources for a new cloud or SaaS provider, you should author your provider in Go using [Pulumi Provider SDK](/docs/iac/guides/building-extending/providers/pulumi-provider-sdk/).

For a guide to authoring your provider, see [Build a Provider](/docs/iac/guides/building-extending/providers/build-a-provider/). For a guide to publishing your provider in the Pulumi Registry, see [Publishing Pulumi Packages](/docs/iac/guides/building-extending/packages/publishing-packages/).
