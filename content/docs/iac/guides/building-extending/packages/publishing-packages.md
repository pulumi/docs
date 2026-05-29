---
title_tag: "Publishing to the Pulumi Registry"
meta_desc: "Learn how to publish a Pulumi package to the public Pulumi Registry so it's discoverable by the Pulumi community."
title: Publishing to the Pulumi Registry
h1: Publishing to the Pulumi Registry
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Publishing to the Pulumi Registry
        parent: iac-guides-packages
        weight: 30
aliases:
- /docs/guides/pulumi-packages/how-to-author/
- /docs/using-pulumi/pulumi-packages/contribute-to-pulumi-registry/
- /docs/using-pulumi/pulumi-packages/how-to-author
- /docs/using-pulumi/pulumi-packages/authoring/
- /docs/iac/packages-and-automation/pulumi-packages/authoring/
- /docs/iac/using-pulumi/pulumi-packages/authoring/
- /docs/iac/using-pulumi/extending-pulumi/publishing-packages/
- /docs/iac/extending-pulumi/publishing-packages/
- /docs/iac/build-with-pulumi/publishing-packages/
---

This page covers publishing a [Pulumi package](/docs/iac/concepts/packages/) to the public [Pulumi Registry](/registry/) so it's discoverable by the Pulumi community.

{{% notes type="info" %}}
Publishing to your organization's **[Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/)**? Use the [`pulumi package publish`](/docs/iac/cli/commands/pulumi_package_publish/) command — see [Publishing Components from GitHub Actions](/docs/idp/guides/publishing-from-github-actions/) for the full workflow. This page covers the public Pulumi Registry only.
{{% /notes %}}

You can publish the following types of packages to the public Pulumi Registry:

- A [component](/docs/iac/concepts/components) or related group of components
- A custom provider where you define the CRUD operations for each resource type
- A bridged provider, which wraps an existing Terraform provider and leverages its code to perform the CRUD operations for each resource type

{{% notes type="info" %}}
If you are a cloud or SaaS provider interested in publishing a Pulumi provider or component, please [reach out to our partners team](/contact).
{{% /notes %}}

## Prerequisites

{{% notes type="info" %}}
This guide assumes you're using GitHub to host your package's source code and GitHub Actions to publish various parts of your package.
{{% /notes %}}

- You need to [install Pulumi](/docs/install/).
- You should be familiar with the Pulumi [Resource and Component model](/docs/concepts/resources/).
- Pulumi Packages are multi-language: you can write your package once in either Go, Python, or TypeScript/JavaScript and then make it available to all Pulumi users, even if they use another language. To develop them, you need to have Git, Go, .NET, Python, and TypeScript installed on your system.
- To follow the whole guide, you need a GitHub account. However, using GitHub is not a requirement; you may still find this guide useful even if you use another system to store your source code.

## Create a repository and author your package

To get started, create a repository for your Pulumi Package. We recommend hosting your Pulumi Package in a public repository on GitHub. We also recommend following the naming conventions below to help the community find the source code for your packages.

### Select a template

We've created some template repositories for you to use as a starting point for your package. These templates are for **provider-based packages**. If you are building a cross-language component (recommended for most platform teams), see [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) for the recommended approach.

Click the link for the boilerplate repository template that you want to use, then click "Use this template" to make a copy of it.

- Author a custom Pulumi provider: [`pulumi/pulumi-provider-boilerplate`](https://github.com/pulumi/pulumi-provider-boilerplate)
- Bridge an existing Terraform Provider to use with Pulumi: [`pulumi/pulumi-tf-provider-boilerplate`](https://github.com/pulumi/pulumi-tf-provider-boilerplate)

{{% notes type="info" %}}
If you need access to a Terraform provider, but don't need the full customization of a published provider, the ["Any Terraform Provider" Pulumi Provider](/registry/packages/terraform-provider) can provide instant access via locally generating SDKs.
{{% /notes %}}

### Name your provider and repository

When you publish to the [Pulumi Package Registry](https://www.pulumi.com/registry/), you will need to pick a unique name. This is normally named after the cloud provider or service the provider configures.

Your repository name should start with `pulumi-` followed by the name of your provider e.g. [`pulumi-aws`](https://github.com/pulumi/pulumi-aws) for AWS, or [`pulumi-kubernetes`](https://github.com/pulumi/pulumi-kubernetes) for the Kubernetes provider.

- If you're bridging a Terraform provider, re-use the Terraform provider's name - replacing `terraform-provider-` with `pulumi-` e.g. use `pulumi-auth0` for bridging `terraform-provider-auth0`.
- If you're building a component on top of an existing provider, consider using the provider name followed by the component name. For example, if building an API Gateway component using the AWS provider, name your project `pulumi-aws-apigateway`.

## Author your resources or components

See the instructions in your new repository's `README.md` file for specific instructions on how to author your package. We also have guides you can follow for building [components](/docs/iac/concepts/resources/components/) and [providers](/docs/iac/concepts/providers/) without the template repos.

## Write documentation

We recommend writing documentation to help others in the Pulumi community use your package. In your repository, there should be a `docs/` folder containing markdown files (the templates include a few suggested pages). The files should correspond to the various tabs on a package page in Pulumi Registry (like the [Azure Native](/registry/packages/azure-native/) package). Use the guidance in the following sections to author content in these pages.

### Overview, installation, & configuration

Specifically, you should author a few pages:

1. `_index.md`, which will be shown on the Overview tab for your package. The title of this page should match the package display name and is the heading shown on the package detail page. The Overview is a great place to include a description of what your package does, a simple example, and any other details that you want prospective users of your package to know to be successful.
1. `installation-configuration.md`, which will be shown on your package's Installation & Configuration tab. Use this page to describe how to set up your package, including authenticating to a cloud provider, and to list the configuration options that can be used with your package. The title of this page should be in the form `<Package display name> Installation & Configuration`.

{{% notes type="info" %}}
We recommend keeping the contents of `README.md` and `_index.md` similar or the same, save for the YAML metadata/front-matter that's in `_index.md`.
{{% /notes %}}

For reference, the [ImprovMX](https://github.com/pulumi/registry/blob/master/themes/default/content/registry/packages/improvmx/) community provider is a well-authored example: see its [`_index.md`](https://github.com/pulumi/registry/blob/master/themes/default/content/registry/packages/improvmx/_index.md) and [`installation-configuration.md`](https://github.com/pulumi/registry/blob/master/themes/default/content/registry/packages/improvmx/installation-configuration.md). The [Logfire provider](https://github.com/pulumi/registry/blob/master/themes/default/content/registry/packages/logfire/) is another recent example.

Although you author these files in your package repository's `docs/` folder, they are published through the [`pulumi/registry` GitHub repository](https://github.com/pulumi/registry), under `themes/default/content/registry/packages/<your-package>/`. The [Publish the documentation](#publish-the-documentation) section below explains how to submit them.

### Package metadata

Metadata for your package is generated from the [`schema.json`](/docs/iac/using-pulumi/extending-pulumi/schema) in your repository. To make sure your package looks great in the Pulumi Registry, don't forget to add metadata like:

- `displayName`: the friendly name for your package displayed on the Registry's browse page; this name should match the title of the `_index.md` file.
- `description`: a short description of your package; it should include the package name
- `logoUrl`: a web-accessible URL to a logo for your package (ideally an SVG); we recommend using the githubrawcontent.com URL for a logo stored in your package's repository; all surrounding whitespace should be removed from the logo, and wordmarks are preferred
- `publisher`: your personal/company name, as you'd like it to be shown on Registry
- `keywords`:
  - `category/CATEGORY`: replace `CATEGORY` with one of `cloud`, `database`, `infrastructure`, `monitoring`, `network`, `utility`, `versioncontrol`
  - `kind/KIND`: replace `KIND` with one of `native`, `component`
    - Note: don't set a kind if you're bridging a Terraform provider
- `pluginDownloadURL`: a web-accessible URL that contains the compiled plugin binary associated with your package. See [Authoring an Executable Plugin Package](/docs/iac/guides/building-extending/packages/executable-plugin/#plugindownloadurl) for the URL format, hosting options (GitHub Releases, GitLab Releases, custom HTTP), and interpolation variables.

### API docs

API docs for your package are automatically generated from the `schema.json` in your repository. Many Pulumi users learn to use a Pulumi Package via the API docs, since they appear automatically in many IDEs' auto-complete and inline documentation features, like Visual Studio Code's IntelliSense feature. Investing in API docs for your package is one of the best ways to improve its usability. Check out the [`pulumi-eks` schema](https://github.com/pulumi/pulumi-eks/blob/master/provider/cmd/pulumi-resource-eks/schema.json) to see how it translates to the [Pulumi Registry](/registry/packages/eks/api-docs/) for an example of great API docs.

### How-to guides

You can also create how-to guides for your packages by contributing them to the [`pulumi/examples`](https://github.com/pulumi/examples) repository on GitHub.

## Publish your package

Once you've authored and tested your package locally, you can publish it to make it available to the Pulumi community. You must publish several artifacts:

- The npm, NuGet, Java, and Python SDK packages to the [npm Registry](https://npmjs.com), the [NuGet Gallery](https://nuget.org), [Maven Central](https://central.sonatype.com) and the [Python Package Index](https://pypi.org).
  - If your package is hosted on GitHub, you may choose to use our [custom Action for publishing Pulumi packages](https://github.com/pulumi/pulumi-package-publisher).
- The Go module to your Git repository, by adding a tag.
- The plugin binary to a host of your choice (GitHub Releases, GitLab Releases, or a custom HTTP endpoint).
- The [package documentation](#publish-the-documentation) — overview, installation & configuration, API docs, and how-to guides to [Pulumi Registry](/registry/).

For how to cross-compile the plugin binary, the archive naming convention the CLI expects, and the supported `pluginDownloadURL` forms, see [Authoring an Executable Plugin Package](/docs/iac/guides/building-extending/packages/executable-plugin/). That guide also covers the canonical release pipeline used by Pulumi's own providers, including the [`pulumi/pulumi-package-publisher`](https://github.com/pulumi/pulumi-package-publisher) GitHub Action for publishing SDKs.

## Publish the documentation

All package documentation in the Pulumi Registry is published via the [`pulumi/registry` repository on GitHub](https://github.com/pulumi/registry). To publish your package to the Pulumi Registry:

1. Fork and clone the [`pulumi/registry` repository](https://github.com/pulumi/registry).
1. Add your package to [the community package list](https://github.com/pulumi/registry/blob/master/community-packages/package-list.json)
    1. Add your package's GitHub repo slug, e.g. `"checkly/pulumi-checkly"`
    1. Add the path to your package's `schema.json` file from the root of your provider repository, e.g. `"provider/cmd/pulumi-resource-checkly/schema.json"`
1. Add your documentation files to `themes/default/content/registry/packages/<your-package>/`, including the `_index.md` and `installation-configuration.md` files you authored in your provider repository's `docs/` folder.
1. Open a pull request with the above changes and await review from a Pulumi team member. For a complete example of a community package submission, see [pulumi/registry#10358](https://github.com/pulumi/registry/pull/10358).

{{% notes %}}
API docs for your package will be automatically generated at the time of building the registry site. You do not need to take any action to generate API docs other than making sure your package repository has the right `schema.json` (or `.yaml`).
{{% /notes %}}

From there, a Pulumi employee will work with you to get your Pulumi Package published. To do so, they'll:

1. Review your pull request and trigger the automation that builds the package listing and the API docs from your schema.
1. Merge upon approval of your PR
1. On merging, CI will automatically publish your package listing and API docs to pulumi.com/registry.
