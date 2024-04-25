---
title_tag: "How to Author & Publish Pulumi Packages"
meta_desc: "Learn how to create a Pulumi Package: create a Native Provider, author a Component, or bridge a Terraform provider into the Pulumi ecosystem."
title: Author packages
h1: Author packages in Pulumi Registry
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    usingpulumi:
        parent: pulumi-packages
        identifier: how-to-author
        weight: 2
aliases:
- /docs/guides/pulumi-packages/how-to-author/
---

This how-to guide will take you step-by-step through the tasks required to author and publish a Pulumi Package. You can use this guide to create any [type of Pulumi Package](/docs/guides/pulumi-packages#types-of-pulumi-packages): a Native Provider, a provider bridged from an existing Terraform provider, or a Component. This guide assumes you're using GitHub to host your package's source code and GitHub Actions to publish various parts of your package.

## Prerequisites

- You need to [install Pulumi](/docs/install/).
- You should be familiar with the Pulumi [Resource and Component model](/docs/concepts/resources/).
- Pulumi Packages are multi-language: you can write your package once in either Go, Python, or TypeScript/JavaScript and then make it available to all Pulumi users, even if they use another language. To develop them, you need to have Git, Go, .NET, Python, and TypeScript installed on your system.
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

- The name should start with `pulumi-`, like our [`pulumi-aws-native`](/registry/packages/aws-native) AWS Native Provider and our [`pulumi-eks`](/registry/packages/eks) Component for AWS Elastic Kubernetes Service (EKS)
- If you're naming a **native provider**, use the cloud provider's name and the suffix `-native`, like our [`pulumi-azure-native`](/registry/packages/azure-native) Azure Native Provider
- If you're naming a **bridged provider**, re-use the Terraform provider's name but replace the `terraform-provider-` prefix with `pulumi-`
- If you're naming a **component**, name your package using both the cloud provider whose resources you're building on top of and the resources, like our [`pulumi-aws-apigateway`](/registry/packages/aws-apigateway) Component for AWS API Gateway

## Author your resources or components

See the instructions in your new repository's `README.md` file for specific instructions on how to author your package.

## Write documentation

We recommend authoring documentation to help others in the Pulumi community use your package. In your repository, there should be a `docs/` folder with a few template pages you can use that correspond to the various tabs on a package page in Pulumi Registry (like the [AWS Native](/registry/packages/aws-native/) package). Use the guidance in the following sections to author content in these pages.

### Overview, installation, & configuration

Specifically, you should author a few pages:

1. `_index.md`, which will be shown on the Overview tab for your package. The title of this page should match the package display name and is the heading shown on the package detail page. The Overview is a great place to include a description of what your package does, a simple example, and any other details that you want prospective users of your package to know to be successful.
1. `installation-configuration.md`, which will be shown on your package's Installation & Configuration tab. Use this page to describe how to set up your package, including authenticating to a cloud provider, and to list the configuration options that can be used with your package. The title of this page should be in the form `<Package display name> Installation & Configuration`.

{{% notes type="info" %}}
We recommend keeping the contents of `README.md` and `_index.md` similar or the same, save for the YAML metadata/front-matter that's in `_index.md`.
{{% /notes %}}

### Package metadata

Metadata for your package is generated from the [`schema.json`](/docs/using-pulumi/pulumi-packages/schema) in your repository. To make sure your package looks great in Pulumi Registry, ensure you add metadata like:

- `displayName`: the friendly name for your package displayed on the Registry's browse page; this name should match the title of the `_index.md` file.
- `description`: a short description of your package; it should include the package name
- `logoUrl`: a web-accessible URL to a logo for your package (ideally an SVG); we recommend using the githubrawcontent.com URL for a logo stored in your package's repository; all surrounding whitespace should be removed from the logo, and wordmarks are preferred
- `publisher`: your personal/company name, as you'd like it to be shown on Registry
- `keywords`:
  - `category/CATEGORY`: replace `CATEGORY` with one of `cloud`, `database`, `infrastructure`, `monitoring`, `network`, `utility`, `versioncontrol`
  - `kind/KIND`: replace `KIND` with one of `native`, `component`
    - Note: don't set a kind if you're bridging a Terraform provider
- `pluginDownloadURL`: a web-accessible URL that contains the compiled binary plugin associated with your package; for more information see [Publish your package](#publish-your-package)

{{% notes %}}
Pulumi will interpolate `${VERSION}`, `${OS}` and `${ARCH}` with their respective values if found in `pluginDownloadURL`.
{{% /notes %}}

### API docs

API docs for your package are automatically generated from the `schema.json` in your repository. Many Pulumi users learn to use a Pulumi Package via the API docs, since they appear automatically in many IDEs' auto-complete and inline documentation features, like Visual Studio Code's IntelliSense feature. Investing in API docs for your package is one of the best ways to improve its usability. Check out the [`pulumi-eks` schema](https://github.com/pulumi/pulumi-eks/blob/master/provider/cmd/pulumi-resource-eks/schema.json) and how it translates to [Pulumi Registry](/registry/packages/eks/api-docs/) for an example of great API docs.

### How-to guides

You can also create how-to guides for your packages by contributing them to the [`pulumi/examples`](https://github.com/pulumi/examples) repository on GitHub.

## Publish your package

Once you've authored and tested your package locally, you can publish it to make it available to the Pulumi community. You must publish several artifacts:

- The npm, NuGet, Java, and Python SDK packages to the [npm Registry](https://npmjs.com), the [NuGet Gallery](https://nuget.org), [Maven Central](https://central.sonatype.com) and the [Python Package Index](https://pypi.org)
  - If your package is hosted on GitHub, you may choose to use our [custom Action for publishing Pulumi packages](https://github.com/pulumi/pulumi-package-publisher)
- The Go module to your Git repository, by adding a tag, which we'll explain in the sections below
- The binary Pulumi resource provider plugin to a binary hosting provider of your choice
- The [package documentation](#publish-the-documentation) - overview, installation & configuration, API docs, and how-to guides to [Pulumi Registry](/registry/)

The URL used to download a plugin is derived from `pluginDownloadURL`, as specified in the schema. Pulumi expects to find a plugin at

```
${pluginDownloadURL}/pulumi-${kind}-${name}-v${version}-${os}-${arch}.tar.gz
```

- `name`: the name field specified in the schema
- `version`: the version field specified in the schema
- `kind`: the kind specified in schema, probably `resource`
- `os`: the target operating system (one of `darwin`, `linux`, `windows`)
- `arch`: the target system architecture (one of `amd64`, `arm64`)

Pulumi packages consist of SDKs, as well as a binary to facilitate the actual task (creating cloud resources, ect.). Package
managers (npm, NuGet, Pip, GitHub) host the SDKs, but we need to know where the plugin is hosted. When a package embeds its
`pluginDownloadURL`, we can automatically fetch the plugin. This means that `pulumi up` just works, and there is no need to run
`pulumi plugin install ${NAME} ${VERSION} --server ${pluginDownloadURL}`. If `pluginDownloadURL` is not supplied, then the Pulumi
CLI assumes the plugin is hosted at `get.pulumi.com`.

### Support for GitHub releases

Since [release 3.35.3](https://github.com/pulumi/pulumi/releases/tag/v3.35.3), Pulumi understands a special form of `pluginDownloadURL` to download plugins via GitHub releases

```
github://${github api host}/{organization}[/{repository}]
```

- `github api host`: the address of a GitHub API, for `github.com` this is `api.github.com`
- `organization`: the GitHub organization to use
- `repository`: the GitHub repository to use, this defaults to `pulumi-${package name}`

For example the [Pulumiverse Astra](https://github.com/pulumiverse/pulumi-astra) package would specify `github://api.github.com/pulumiverse`.

### Support for Gitlab releases

Since [release 3.56.0](https://github.com/pulumi/pulumi/releases/tag/v3.56.0), Pulumi understands a special form of `pluginDownloadURL` to download plugins via Gitlab releases

```
gitlab://${gitlab api host}/{<project_id>}
```

- `gitlab api host`: the address of a Gitlab API, for Gitlab SaaS this is `gitlab.com`
- `project_id`: the Gitlab project ID to use. The project ID can be found right below the project name on the project page.

## Publish the documentation

All package documentation on Pulumi Registry is published via the [`pulumi/registry` repository on GitHub](https://github.com/pulumi/registry). To publish your package on Pulumi Registry:

1. Fork and clone the [`pulumi/registry` repository](https://github.com/pulumi/registry).
1. Add your package to [the community package list](https://github.com/pulumi/registry/blob/master/community-packages/package-list.json)
    1. Add your package's GitHub repo slug, e.g. `"checkly/pulumi-checkly"`
    1. Add the path to your package's `schema.json` file from the root of your provider repository, e.g. `"provider/cmd/pulumi-resource-checkly/schema.json"`
1. Open a pull request with the above changes and await review from a Pulumi team member.

{{% notes %}}
API docs for your package will be automatically generated at the time of building the registry site. You do not need to take any action to generate API docs other than make sure your package repository has the right `schema.json` (or `.yaml`).
{{% /notes %}}

From there, a Pulumi employee will work with you to get your Pulumi Package published. To do so, they'll:

1. Review your pull request and trigger the automation that builds the package listing and the API docs from your schema.
1. Merge upon approval of your PR
1. Merge the resulting pull request in `pulumi/docs` that pulls the latest Registry content into pulumi.com and publishes it.

## Congratulations

Congratulations on publishing your Pulumi Package!
