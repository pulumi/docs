---
title_tag: "Building & Extending Pulumi | Guides"
meta_desc: Learn how to build custom components, providers, and packages to extend Pulumi's capabilities.
title: Building & Extending
h1: Building & Extending Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Building & Extending
        parent: iac-using-pulumi
        weight: 20
        identifier: iac-guides-building-extending
aliases:
  - /docs/iac/build-with-pulumi/
  - /docs/iac/using-pulumi/extending-pulumi/
  - /docs/iac/extending-pulumi/
---

Pulumi's extensibility model allows you to build reusable abstractions, integrate new platforms, and share infrastructure patterns across your organization.

These guides show you how to create custom components that encapsulate best practices, build providers for platforms not yet supported, package your work for distribution, and integrate existing infrastructure tools into your Pulumi programs.

## Components

Build reusable infrastructure components to encapsulate and share infrastructure patterns.

**[Build a Component](/docs/iac/guides/building-extending/components/build-a-component/)** - Learn the process for creating custom Pulumi components that bundle multiple resources into reusable abstractions with built-in best practices.

**[Testing Components](/docs/iac/guides/building-extending/components/testing-components/)** - Write automated tests for your components to ensure they work correctly and maintain quality as they evolve.

**[Package a Component](/docs/iac/guides/building-extending/components/packaging-a-component/)** - Choose the right packaging approach for your components: single-language, cross-language, or provider-based distribution.

## Providers

Create custom providers to integrate new cloud platforms and services with Pulumi.

**[Build a Provider](/docs/iac/guides/building-extending/providers/build-a-provider/)** - Step-by-step guide to building a Pulumi provider that enables infrastructure management for any API or service.

**[Pulumi Provider SDK](/docs/iac/guides/building-extending/providers/pulumi-provider-sdk/)** - Reference documentation for the SDK used to build native Pulumi providers with full access to the resource model.

**[Debugging Providers](/docs/iac/guides/building-extending/providers/debugging-providers/)** - Techniques and tools for troubleshooting provider development and diagnosing issues.

## Packages

Package and distribute your components and providers for use across teams and projects.

**[Pulumi Packages](/docs/iac/concepts/packages/)** - Overview of Pulumi packages and how they enable sharing infrastructure code across all Pulumi languages.

**[Local Packages](/docs/iac/guides/building-extending/packages/local-packages/)** - Develop and test packages locally before publishing them to registries.

**[Publishing Packages](/docs/iac/guides/building-extending/packages/publishing-packages/)** - Distribute your packages to npm, NuGet, PyPI, and other registries for team and community use.

**[Schema](/docs/iac/guides/building-extending/packages/schema/)** - Define package schemas that drive SDK generation and documentation for all supported languages.

## Templates

Create project templates for bootstrapping new Pulumi projects.

**[Creating Templates](/docs/iac/guides/building-extending/creating-templates/)** - Build custom templates that can be used with `pulumi new` to quickly bootstrap new projects with your preferred configurations and patterns.

## Using Existing Tools

Leverage existing infrastructure tools and modules within Pulumi programs.

**[Use Terraform Module](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/)** - Integrate Terraform modules into Pulumi programs to reuse existing infrastructure code without rewriting it.
