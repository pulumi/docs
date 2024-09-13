---
title_tag: Pulumi Packages
meta_desc: Pulumi Packages enable you to write infrastructure abstractions once in TypeScript, C#, Go, or Python and make them available for use in any Pulumi language.
title: Pulumi packages
h1: Pulumi packages
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Pulumi packages
        parent: iac-packages-automation
        weight: 1
        identifier: iac-packages-automation-packages
    usingpulumi:
        identifier: pulumi-packages
        weight: 7
aliases:
- /docs/guides/pulumi-packages/
- /docs/using-pulumi/pulumi-packages/
---

Pulumi Packages are the core technology that enables cloud infrastructure resource provisioning to be defined once, and made available to users in all Pulumi languages. With Pulumi Packages, [Resources and Components](/docs/concepts/resources/) can be written once, in your preferred language, and made available in all the other languages supported by Pulumi.

![A diagram showing how Pulumi Package code can be authored in one language and made available in all other languages supported by Pulumi](img/pulumi-package-overview.png)

## Find Pulumi Packages on Pulumi Registry

[Pulumi Registry](/registry/) is the central location where you can find all of the Pulumi Packages you can use. Visit [Pulumi Registry](/registry/) to get started!

## Author a Pulumi Package

To create your own Pulumi Package, use the [guide](/docs/using-pulumi/pulumi-packages/how-to-author/).

### Overview of authoring a package

Regardless of the type of Pulumi Package you want to author, there are a few key steps in the process of authoring a Pulumi package.

1. Decide the [type](#types-of-pulumi-packages) of package you want to create and create a repository for it using one of the template repos provided by Pulumi
1. Create the [Resources or Components](/docs/concepts/resources/) you want to include in the package, either by authoring them manually (in the case of a Component Package) or generating them from a cloud provider's API or via a provider bridge
1. Build the resource provider plugin: the binary file that contains all of the components or resources you defined in your source code
1. Generate the SDK code for all languages supported by Pulumi and packs the SDK packages–the npm, NuGet, and Python packages–that the Pulumi Package’s users will reference in their own programs
1. Publish the SDK packages and the resource provider plugin

![A graphic representation of the steps listed above](img/pulumi-package-concepts.png)

All Pulumi Packages must include a [schema](/docs/using-pulumi/pulumi-packages/schema/), which defines the resources and functions exposed by the package, and is used to drive the generation of language-specific SDKs and documentation.

### Types of Pulumi Packages

There are currently 3 different types of Pulumi Packages:

1. **Native Pulumi Provider Package:** Use the full features of the Pulumi resource model to create a provider for a new cloud platform. Examples: the [`kubernetes`](/registry/packages/kubernetes), [`azure-native`](/registry/packages/azure-native), and [`google-native`](/registry/packages/google-native) packages.
2. **Bridged Provider Package:** Take an existing resource provider from another supported ecosystem (like a Terraform provider), and bridge it to be exposed as a Pulumi Package. Examples: the [`aws`](/registry/packages/aws), [`tls`](/registry/packages/tls), and [`cloudflare`](/registry/packages/cloudflare) packages. Bridged provider packages can be static or Parameterized. Static providers (like [`aws`](/registry/packages/aws)) serve a fixed set of resources. Parameterized providers (like [`terraform-provider`](/registry/packages/terraform-provider)) serve a kind of resource, but are not limited to a closed set of resources. For example: [`terraform-provider`](/registry/packages/terraform-provider) can be parameterized to act in place of any Terraform provider, and so serve any resource supported by Terraform.
3. **Component Package:** Write a Pulumi Component in your language of choice and expose it to users in all Pulumi languages. Example: the [`eks`](/registry/packages/eks) package.
