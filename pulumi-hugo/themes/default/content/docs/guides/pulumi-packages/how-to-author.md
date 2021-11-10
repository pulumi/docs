---
title: Authoring & Publishing
meta_desc: "Learn how to create a Pulumi Package: create a Native Provider, author a Component, or bridge a Terraform provider into the Pulumi ecosystem."
menu:
    userguides:
        parent: pulumi-packages
        identifier: how-to-author
        weight: 2
---

This how-to guide will take you step-by-step through the tasks required to author and publish a Pulumi Package. You can use this guide to create any [type of Pulumi Package]({{<relref "/docs/guides/pulumi-packages#types-of-pulumi-packages">}}): a Native Provider, a provider bridged from an existing Terraform provider, or a Component. This guide assumes you're using GitHub to host your package's source code and GitHub Actions to publish various parts of your package.

## Prerequisites

- You need to [install Pulumi]({{<relref "/docs/get-started/install">}}).
- You should be familiar with the Pulumi [Resource and Component model]({{<relref "/docs/intro/concepts/resources">}}).
- Pulumi Packages are multi-language: you can write your package once in either Go, Python, or TypeScript/JavaScript and then make it available to all Pulumi users, even if they use another language. To develop them, you need to have Git, Go, .NET Core, Python, and TypeScript installed on your system.
- To follow the whole guide, you need a GitHub account. However, using GitHub is not a requirement; you may still find this guide useful even if you use another system to store your source code.

## Create a repository

To get started, create a repository for your Pulumi Package. We recommend hosting your Pulumi Package in a public repository on GitHub. We also recommend following the naming conventions below to help the community find the source code for your packages.

### Select a template

To get started, click the link for the boilerplate repository template that you want to use, then click "Use this template" to make a copy of it.

- Author a **Native Provider** with [`pulumi/pulumi-provider-boilerplate`](https://github.com/pulumi/pulumi-provider-boilerplate)
- Author a **Bridged Provider** with [`pulumi/pulumi-tf-provider-boilerplate`](https://github.com/pulumi/pulumi-tf-provider-boilerplate)
- Author a **Component** with:
  - **Go:** [`pulumi/pulumi-component-provider-go-boilerplate`](https://github.com/pulumi/pulumi-component-provider-go-boilerplate)
  - **Python:** [`pulumi/pulumi-component-provider-py-boilerplate`](https://github.com/pulumi/pulumi-component-provider-py-boilerplate)
  - **TypeScript:** [`pulumi/pulumi-component-provider-ts-boilerplate`](https://github.com/pulumi/pulumi-component-provider-ts-boilerplate)
  - **C#:** a template repository is coming soon

### Name your repository

You should name your repository (and thus, your Pulumi Package) using the following guidelines:

- The name should start with `pulumi-`, like our [`pulumi-aws-native`]({{<relref "/registry/packages/aws-native">}}) AWS Native Provider and our [`pulumi-eks`]({{<relref "/registry/packages/eks">}}) Component for AWS Elastic Kubernetes Service (EKS)
- If you're naming a **native provider**, use the cloud provider's name and the suffix `-native`, like our [`pulumi-azure-native`]({{<relref "/registry/packages/azure-native">}}) Azure Native Provider
- If you're naming a **bridged provider**, re-use the Terraform provider's name but replace the `terraform-provider-` prefix with `pulumi-`
- If you're naming a **component**, name your package using both the cloud provider whose resources you're building on top of and the resources, like our [`pulumi-aws-api-gateway`]({{<relref "/registry/packages/pulumi-aws-api-gateway">}}) Component for AWS API Gateway

## Author your resources or components

See the instructions in your new repository's `README.md` file for specific instructions on how to author your package.

## Write documentation

To help others in the Pulumi community use your package, we recommend authoring some documentation. In your repository, there is a `docs/` folder with a few template pages you can use that correspond to the various tabs on a package page in Pulumi Registry (like [this page for AWS Native]({{<relref "/registry/packages/aws-native">}})). Use the guidance in the following sections to author content in these pages.

### Overview, installation, & configuration

Specifically, you should author a few pages:

1. `_index.md`, which will be shown on the Overview tab for your package. The Overview is a great place to include a description of what your package does, a simple example, and any other details that you want prospective users of your package to know in order to be successful.
1. `installation-configuration.md`, which will be shown on the Installation & Configuration tab for your package. Use this page to describe any details of how to set up your package, including authenticating to a cloud provider, and to list the configuration options that can be used with your package.

{{% notes type="info" %}}
A future improvement to Pulumi Packages will enable Pulumi Registry to create the contents for the Overview tab of your package directly from a `README.md` in the root of your package's repository. Until then, we recommend keeping the contents of `README.md` and `_index.md` similar or the same, save for the YAML metadata/front-matter that's in `_index.md`.
{{% /notes %}}

### Package metadata

Metadata for your package is generated from the `schema.json` in your repository. To make sure your package looks great in Pulumi Registry, ensure you add metadata like:

- `displayName`: the friendly name for your package that's displayed throughout Registry
- `description`: a short description of your package
- `logoUrl`: a web-accessible URL to a logo for your package (ideally an SVG); we recommend using the githubrawcontent.com URL for a logo stored in your package's repository
- `publisher`: your personal/company name, as you'd like it to be shown on Registry
- `keywords`:
  - `category/CATEGORY`: replace `CATEGORY` with one of `cloud`, `database`, `infrastructure`, `monitoring`, `network`, `utility`, `versioncontrol`
  - `kind/KIND`: replace `KIND` with one of `native`, TODO FOR COMPONENT AND BRIDGED

### API docs

API docs for your package are also generated from the `schema.json` in your repository. Many Pulumi users learn to use a Pulumi Package via the API docs, since they appear automatically in many IDEs' auto-complete and inline documentation features, like Visual Studio Code's IntelliSense feature. Investing in API docs for your package is one of the best ways to improve its usability. Check out the [`pulumi-eks` schema](https://github.com/pulumi/pulumi-eks/blob/master/provider/cmd/pulumi-resource-eks/schema.json) and how it translates to [Pulumi Registry]({{<relref "/registry/packages/eks/api-docs">}}) for an example of great API docs.

### How-to guides

You can also create how-to guides for your packages by contributing them to the [`pulumi/examples`](https://github.com/pulumi/examples) repository on GitHub.

## Publish your package

Once you've authored and tested your package locally, you can publish it to make it available to the Pulumi community. You must publish several artifacts:

- The npm, NuGet, and Python SDK packages to the [npm Registry](https://npmjs.com), the [NuGet Gallery](https://nuget.org), and the [Python Package Index](https://pypi.org)
- The Go module to your Git repository, by adding a tag, which we'll explain in the sections below
- The binary Pulumi resource provider plugin to a binary hosting provider of your choice
- The package documentation–overview, installation & configuration, API docs, and how-to guides–to [Pulumi Registry]({{<relref "/registry">}})

Future iterations of this guide will cover how to publish the first three items; for now, these are left as an exercise for the package author.

### Publish the documentation

For now, all package documentation on Pulumi Registry is published via the [`pulumi/registry` repository on GitHub](https://github.com/pulumi/registry). To publish your package on Pulumi Registry:

1. Fork the [`pulumi/registry` repository](https://github.com/pulumi/registry) and clone it locally.
1. Create a new directory for your package inside the [`themes/default/content/registry/packages` folder](https://github.com/pulumi/registry/tree/master/themes/default/content/registry/packages) that uses your repository's name but remove the `pulumi-` prefix.
1. Copy the contents of the `docs/` folder in your package's repository to the folder you created in the last step.
1. Create a pull request from your fork back to `pulumi/registry`.
    1. In the pull request description, list the URL of your repository and the path to the schema within your repository (usually `provider/cmd/pulumi-resource-[your-package-name]/schema.json`).

From there, a Pulumi employee will work with you to get your Pulumi Package published. To do so, they'll:

1. Review your pull request and trigger the automation that builds the package listing and the API docs from your schema.
1. Merge the resulting pull request as well as your original pull request.
1. Merge the resulting pull request in `pulumi/docs` that pulls the latest Registry content into pulumi.com and publishes it.

## Congratulations

Congratulations on publishing your Pulumi Package!
