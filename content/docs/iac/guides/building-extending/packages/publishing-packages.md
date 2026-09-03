---
title_tag: "Publishing to the Pulumi Registry"
meta_desc: "Learn how to publish a Pulumi package to the public Pulumi Registry so it's discoverable by the Pulumi community."
title: Publishing to the Pulumi Registry
h1: Publishing to the Pulumi Registry
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
- You should be familiar with the Pulumi [Resource and Component model](/docs/iac/concepts/resources/).
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
Just want to use an existing Terraform provider, not author and maintain a full package? See [Alternative: use an existing Terraform provider](#alternative-use-an-existing-terraform-provider) below.
{{% /notes %}}

### Name your provider and repository

When you publish to the [Pulumi Package Registry](https://www.pulumi.com/registry/), you will need to pick a unique name. This is normally named after the cloud provider or service the provider configures.

Your repository name should start with `pulumi-` followed by the name of your provider e.g. [`pulumi-aws`](https://github.com/pulumi/pulumi-aws) for AWS, or [`pulumi-kubernetes`](https://github.com/pulumi/pulumi-kubernetes) for the Kubernetes provider.

- If you're bridging a Terraform provider, re-use the Terraform provider's name - replacing `terraform-provider-` with `pulumi-` e.g. use `pulumi-auth0` for bridging `terraform-provider-auth0`.
- If you're building a component on top of an existing provider, consider using the provider name followed by the component name. For example, if building an API Gateway component using the AWS provider, name your project `pulumi-aws-apigateway`.

### Alternative: use an existing Terraform provider

If you don't need the full customization of a published package — you just want to make an existing Terraform provider usable from Pulumi — you don't have to author or maintain a package at all. With the [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/) feature, you run `pulumi package add terraform-provider <author>/<name>` and Pulumi generates a fully-typed local SDK from the provider's schema on the fly.

Popular Terraform providers also surface in the public Pulumi Registry as **dynamically-bridged** listings (for example, [Honeycomb](/registry/packages/honeycombio/) and [Supabase](/registry/packages/supabase/)); consumers still generate the SDK locally with `pulumi package add`. The rest of this guide covers authoring and publishing a full package; if the Any Terraform Provider path fits your needs, follow that guide instead.

{{% notes type="info" %}}
Registry listings for dynamically-bridged Terraform providers are generated automatically and don't include a logo by default. To have a logo added to your provider's Registry page, reach out to [Pulumi support](/support/new/) with a link to a web-accessible SVG (wordmarks preferred, with all surrounding whitespace removed).
{{% /notes %}}

## Author your resources or components

See the instructions in your new repository's `README.md` file for specific instructions on how to author your package. We also have guides you can follow for building [components](/docs/iac/concepts/components/) and [providers](/docs/iac/concepts/providers/) without the template repos.

## Write documentation

We recommend writing documentation to help others in the Pulumi community use your package. In your repository, there should be a `docs/` folder containing markdown files (the templates include a few suggested pages). The files should correspond to the various tabs on a package page in Pulumi Registry (like the [Azure Native](/registry/packages/azure-native/) package). Use the guidance in the following sections to author content in these pages.

### Overview, installation, & configuration

`docs/_index.md` is the only documentation page the Pulumi Registry requires. It renders as your package's Overview tab, and it's where a reader decides whether your package does what they need and how to start using it. Give it a description of what your package does, a simple example, and whatever else a prospective user needs to succeed. Follow the [Overview page guidelines](https://github.com/pulumi/registry/blob/master/docs/overview-page.md) for the required front matter (`title`, `meta_desc`, `layout: package`) and expected section order.

{{% notes type="info" %}}
We recommend keeping the contents of `README.md` and `docs/_index.md` similar or the same, save for the YAML front matter that's in `_index.md`.
{{% /notes %}}

If your installation and configuration material outgrows the Overview page &mdash; several authentication methods, a long configuration table &mdash; move it into a second page, `docs/installation-configuration.md`, which renders as a separate Installation & Configuration tab. This is about volume, not an extra requirement: most packages don't need it, and a single Overview page is a complete submission. The large cloud providers use it; see the [AWS installation & configuration page](/registry/packages/aws/installation-configuration/) for an example.

For reference, the [ImprovMX](https://github.com/pulumi/registry/tree/master/themes/default/content/registry/packages/improvmx) community provider is a well-authored example: see its [`_index.md`](https://github.com/pulumi/registry/blob/master/themes/default/content/registry/packages/improvmx/_index.md). The [Logfire provider](https://github.com/pulumi/registry/tree/master/themes/default/content/registry/packages/logfire) is another recent example.

You author these files in your package repository's `docs/` folder, and never commit them to the [`pulumi/registry` GitHub repository](https://github.com/pulumi/registry) yourself &mdash; the [Submit your package to the Registry](#submit-your-package-to-the-registry) section below explains how the Registry picks them up.

### Package metadata

Metadata for your package is generated from the [`schema.json`](/docs/iac/guides/building-extending/packages/schema/) in your repository. To make sure your package looks great in the Pulumi Registry, don't forget to add metadata like:

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

- **A per-language SDK for every language you want consumers to use.** Pulumi generates SDKs from your `schema.json` with [`pulumi package gen-sdk`](/docs/iac/cli/commands/pulumi_package_gen-sdk/), then you publish each one to its language's package registry:

  | Language | Published to |
  |----------|--------------|
  | TypeScript/JavaScript | [npm Registry](https://npmjs.com) |
  | Python | [Python Package Index (PyPI)](https://pypi.org) |
  | .NET (C#/F#/VB) | [NuGet Gallery](https://nuget.org) |
  | Java | [Maven Central](https://central.sonatype.com) |
  | Go | your Git repository, by pushing a module tag (no external registry) |

  Publish an SDK for **all** of these languages so your package is usable by the whole Pulumi community; a complete Registry listing expects each of them. Publish a subset only if you intentionally support fewer languages. Pulumi YAML is the exception — YAML programs reference the package directly through its schema and need no per-language SDK.

  If your package is hosted on GitHub, the [`pulumi/pulumi-package-publisher`](https://github.com/pulumi/pulumi-package-publisher) GitHub Action publishes the npm, PyPI, NuGet, and Maven Central SDKs in a single step (select languages with its `sdk:` input); you push the Go module tag separately. See the [Publishing SDKs](/docs/iac/guides/building-extending/packages/executable-plugin/#publishing-sdks) section of the executable-plugin guide for the full workflow.
- The plugin binary to a host of your choice (GitHub Releases, GitLab Releases, or a custom HTTP endpoint).
- The [package documentation](#write-documentation) — overview, installation & configuration, API docs, and how-to guides to [Pulumi Registry](/registry/).

For how to cross-compile the plugin binary, the archive naming convention the CLI expects, and the supported `pluginDownloadURL` forms, see [Authoring an Executable Plugin Package](/docs/iac/guides/building-extending/packages/executable-plugin/). That guide also covers the canonical release pipeline used by Pulumi's own providers, including the [`pulumi/pulumi-package-publisher`](https://github.com/pulumi/pulumi-package-publisher) GitHub Action for publishing SDKs.

## Submit your package to the Registry

Registering your package with the Pulumi Registry is a pull request against the [`pulumi/registry` repository on GitHub](https://github.com/pulumi/registry) that adds exactly one entry to [`community-packages/package-list.json`](https://github.com/pulumi/registry/blob/master/community-packages/package-list.json), and changes nothing else:

```json
{
  "repoSlug": "<owner>/<repo>",
  "schemaFile": "provider/cmd/pulumi-resource-<name>/schema.json"
}
```

That one entry is the whole registration. Your `docs/_index.md`, API docs, and package metadata are all generated from your repository and published after merge, so don't commit generated files &mdash; a PR that touches anything besides `package-list.json` (and, for a brand-new publisher, [`publisher-names.json`](https://github.com/pulumi/registry/blob/master/tools/resourcedocsgen/pkg/publishers/publisher-names.json)) is automatically rejected. For a recent example of a complete submission, see [pulumi/registry#12279](https://github.com/pulumi/registry/pull/12279).

Before you open the PR, confirm:

- Your provider has a `v`-prefixed [Semver 2.0](https://semver.org) release, e.g. `v1.2.3`.
- The `schemaFile` path resolves in your repository at that release.
- Your repository has `docs/_index.md`, following the [Overview page guidelines](https://github.com/pulumi/registry/blob/master/docs/overview-page.md).
- The SDKs you advertise are actually published.

Not sure about one of these? Open the PR anyway; the automated check will tell you exactly what's missing.

{{% notes %}}
A **dynamically bridged** Terraform provider &mdash; one you consume with `pulumi package add terraform-provider <name>`, with no provider repository or committed `schema.json` &mdash; can't be added by pull request. Open a [New Package issue](https://github.com/pulumi/registry/issues/new?template=new-package.yml) to request one instead.
{{% /notes %}}

### What happens after you open the PR

Automated checks run on your PR and post a fact-sheet comment: they pin your latest release, install the SDKs you advertise, and validate your docs. They hold no secrets, so they run on a fork just as well as a branch in the repository.

- If something is red, fix it in your provider repository &mdash; cut a release, publish an SDK, correct the schema path &mdash; then comment `/check` on the PR to re-run the check. It reads your live upstream repository, not this diff, so you never need to push a new commit here to re-validate.
- A Pulumi maintainer reads the fact-sheet, may comment `/preview` to build a live preview of your package's pages, and approves. Nothing merges automatically.
- After merge, your package listing and API docs are generated from your schema and published to pulumi.com/registry for you. You never commit generated files to `pulumi/registry`.
