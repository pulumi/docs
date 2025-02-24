<p align="center">
  <a href="https://www.pulumi.com?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=top-logo" title="Pulumi Documentation - Build and Deploy Infrastructure as Code Solutions on Any Cloud">
    <img src="https://www.pulumi.com/images/logo/logo-on-white-box.svg?" width="350">
   </a>

  [![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=slack-badge)
  [![GitHub Discussions](https://img.shields.io/github/discussions/pulumi/pulumi)](https://github.com/pulumi/pulumi/discussions)
  [![License](https://img.shields.io/github/license/pulumi/pulumi)](LICENSE)
  ![Deployment Status](https://github.com/pulumi/docs/actions/workflows/build-and-deploy.yml/badge.svg?branch=master&event=push)
  ![Examples Tests](https://github.com/pulumi/docs/actions/workflows/scheduled-test.yml/badge.svg?branch=master)

# Pulumi Documentation Site

## Table of contents

- :blue_book: [View Pulumi Docs](https://pulumi.com/docs/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-toc)
- :clap: [Contributing](#Contributing)
- :toolbox:	[Setup and Development](#setup-and-development)
  - [Generating SDK and CLI documentation](#generating-sdk-and-cli-documentation)
- :busts_in_silhouette: [Pulumi Community](#community)
- :blue_book: [Pulumi Developer Resources](#pulumi-resources)
- :compass:	[Pulumi Roadmap](#pulumi-roadmap)

## About this repository

This repository hosts all of the hand-crafted documentation, guides, tutorials, blogs, and landing pages that you see on [https://pulumi.com](https://pulumi.com?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=about-docs), as well as all of the assets and templates we use to render the Pulumi website. It also houses the documentation that we generate for the Pulumi CLI and language SDKs, and it's responsible for building and deploying the website (with Pulumi, of course!).

### What's not in this repository

* Pulumi AI: You'll find the open-source components of the Pulumi AI project at https://github.com/pulumi/pulumi-ai.
* Pulumi Registry: You'll find everything related to the Registry at https://github.com/pulumi/registry.

## Contributing

We welcome all contributions to this repository. Be sure to read our [contributing guide](CONTRIBUTING.md) and [code of conduct](CODE-OF-CONDUCT.md) first, then [submit a pull request](https://github.com/pulumi/docs/pulls) here on GitHub. If you see something that needs fixing but don't have time to contribute, you can also [file an issue](https://github.com/pulumi/docs/issues).

See also:

* [Publishing a Pulumi blog post](./BLOGGING.md)
* [Documentation and coding style guide](./STYLE-GUIDE.md)

# Setup and Development

### Toolchain

We build the Pulumi website with Hugo, manage our dependencies with Node.js and Yarn, and write our documentation in Markdown. Below is a list of the tools you'll need if you'd like to work on the website (e.g., to contribute docs content, a blog post, etc.):

* [Hugo](https://gohugo.io/installation/) (>= 0.126.0)
  * Hugo 0.126.0 is highly recommended. This is the version we use in our deployment pipelines.
* [Node.js](https://nodejs.org/en/download/package-manager) (>= 18)
* [Yarn](https://classic.yarnpkg.com/lang/en/docs/install) (1.x)

Additionally, to build the SDK and CLI documentation, you'll also need:

* [Go](https://golang.org/) (>= 1.21)
* [Python](https://www.python.org) (>= 3.7)
* [.NET](https://dotnet.microsoft.com/en-us/download) (>= 6)
* [Pulumi](https://www.pulumi.com/docs/install)
* [Pulumi ESC](https://www.pulumi.com/docs/install/esc)

### Repository layout

* **Documentation and page content**: We generally follow Hugo's [directory-structure conventions](https://gohugo.io/getting-started/directory-structure/), with Markdown files in `./content`, layout files (including partials and shortcodes) in `./layout`, and data files in `./data`. There are also several [Hugo templates](https://gohugo.io/content-management/archetypes/) available in `./archetypes` for bootstrapping common content types like blog posts and Learn modules.

* **CSS and JavaScript**: We build our CSS and JavaScript bundles separately from Hugo and check in the built artifacts at `./assets`. We use [Tailwind](https://tailwindcss.com/) for CSS, [Stencil](https://stenciljs.com/) for web components, and [jQuery](https://jquery.com/) for wiring things together in general. Source files for these are in `./theme`.

* **Examples**: Many of the examples we include in our documentation are maintained as full Pulumi programs and tested daily. You'll find them all at `./static/programs`.

* **Infrastructure**: We deploy the website as a statically built artifact to a unique Amazon S3 bucket on every commit to the base branch of this repo. The Pulumi program that handles this is located in `./infrastructure`. This is also where you'll find the CloudFront configuration that handles proxying [Pulumi AI](https://pulumi.com/ai) and the [Pulumi Registry](https://pulumi.com/registry).

### Using the Makefile

The `Makefile` exposes a number of useful helpers for authoring:

* `make ensure` resolves and installs all dependencies
* `make lint` checks all Markdown files for correctness
* `make format` formats all applicable files to ensure they conform to style guidelines
* `make serve` runs the Hugo server locally at http://localhost:1313 and watches for changes. You can set `BUILD_FUTURE=false` to simulate production behavior by excluding future-dated content (e.g., `BUILD_FUTURE=false make serve`)
* `make serve-all` does the same as `make serve`, but also watches for changes to CSS and JS source files
* `make build` generates the website and writes it to `./public`
* `make build-assets` builds only the CSS and JavaScript asset bundles
* `make serve-static` runs a local HTTP server that serves the contents of `./public`
* `make test` tests all of the programs in `./static/programs` (see `./scripts/programs/test.sh` for options)
* `make generate` builds the TypeScript, Python, and Pulumi CLI documentation
* `make new-blog-post` scaffolds a new, bare-bones blog post with placeholder content
* `make new-tutorial` scaffolds a new single-page tutorial
* `make new-tutorial-module` scaffolds a new multi-page tutorial
* `make new-tutorial-topic` scaffolds a new tutorial topic and adds it to an existing multi-page tutorial
* `make new-example-program` generates a new multi-language set of examples at `./static/programs`
* `make new-dev-stack` creates a new dev stack (in the `pulumi` organization, which you must belong to)
* `make deploy-dev-stack` runs a build, deploys to S3, runs the tests, and deploys to the selected dev stack

As a content contributor, the commands you'll use most often are these:

```bash
make ensure    # Install or update dependencies.
make serve     # Run the development server locally on http://localhost:1313.
make lint      # Identify any Markdown or code-formatting issues so you can fix them.
```

## Generating SDK and CLI documentation

We generate two kinds of reference documentation with this repository: language-specific SDK docs (for a subset of Pulumi packages) and CLI docs (for command-line tools like `pulumi` and `esc`). Instructions for generating both types of docs are listed below.

### SDK docs

We build and host language-specific SDK documentation for the following Pulumi packages:

* [pulumi](https://github.com/pulumi/pulumi)
* [pulumi-awsx](https://github.com/pulumi/pulumi-awsx)
* [pulumi-kubernetesx](https://github.com/pulumi/pulumi-kubernetesx)
* [pulumi-policy](https://github.com/pulumi/pulumi-policy)
* [pulumi-terraform](https://github.com/pulumi/pulumi-terraform)

The Node.js, Python, and .NET versions of these docs are built using language-specific tooling and checked into the repository as stand-alone docsets. (Go versions are sourced directly from GitHub and hosted at [pkg.go.dev](/github.com/pulumi/pulumi/sdk/v3/go/pulumi).)

To build the docs for these packages yourself, you'll first need to clone each package into a sibling directory. The easiest way to do this is to use the `make update-repos` helper:

```bash
# Clone and update all of the repositories above into sibling directories of this repo.
make update-repos
```

Once you've done this, you can generate the docs for each package.

### Generating the Node.js and Python SDK docs

The Node and Python SDK docs are built with [TypeDoc](http://typedoc.org/) and [Pydocgen](https://pypi.org/project/pydocgen/). The easiest way to generate these docs is to use the `make generate` helper:

```bash
make ensure          # Install dependencies.
make update-repos    # Clone and update all package repositories.
make generate        # Generate the Node.js and Python docs for all packages.
```

Generated docs are rendered into the `./static-prebuilt/nodejs` and `./static-prebuilt/python` folders. At deploy-time, we copy the contents of these folders into `./docs/reference/pkg` to make them available on pulumi.com -- for example, [here](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/pulumi) and [here](https://www.pulumi.com/docs/reference/pkg/python/pulumi).

See below to learn how to view these rendered docs locally.

### Generating the .NET SDK docs

The .NET SDK docs are built with [Docfx](https://github.com/dotnet/docfx). To generate these, you'll need both `dotnet` and `docfx` installed and on your PATH. For example, assuming you've already [installed the `dotnet` executable](https://dotnet.microsoft.com/en-us/download) for your platform, you can:

```bash
make ensure                     # Install dependencies.
make update-repos               # Clone and update all package repositories.
dotnet tool install -g docfx    # Install docfx globally, following the instructions to ensure it's on your PATH.
docfx build docfx/docfx.json    # Generate the .NET docs.
```

### CLI docs

The `make generate` helper also generates the Pulumi CLI documentation. If you'd prefer not to use that helper (e.g., to avoid having to clone all the repos and generate SDK docs), you can build them directly using the `pulumi` and `esc` CLIs:

```bash
pulumi gen-markdown ./content/docs/cli/commands    # Generate Pulumi CLI documentation.
esc gen-docs ./content/docs/esc-cli/commands       # Generate Pulumi ESC CLI documentation.
```

Generated docs reflect the functionality of the currently installed CLI, so make sure you've installed the latest public version of each one ([`pulumi`](https://github.com/pulumi/pulumi/releases), [`esc`](https://github.com/pulumi/esc/releases)) before running these commands and submitting your PR.

### Viewing rendered SDK and CLI docs locally

After building the SDK and/or CLI docs, you can view them locally with `make build` and `make serve-static`.

For example, from a fresh clone of this repository, you can install all dependencies and generate and browse the Node.js, Python, and Pulumi CLI docs using the following sequence:

```bash
make ensure          # Install dependencies.
make update-repos    # Clone and update all package repositories.
make generate        # Generate the Node.js, Python, and Pulumi CLI docs.
make build           # Build the website, copying all generated docs into place.
make serve-static    # Serve the built website statically to make sure everything looks right.
```

With `make serve-static` running, you can browse to the docs by navigating to http://localhost:8080/docs. Then, from the left-hand menu:

* Choose Languages &amp; SDKs followed by your language of choice, then scroll to the bottom of the page to find the package you're interested in
* Choose Pulumi CLI or Pulumi ESC CLI, then Commands

### Checking in generated docs

All generated docs, including all Node.js, Python, and .NET SDK docs and all Pulumi and Pulumi ESC CLI docs, get checked into this repository.

## Search

We use [Algolia](https://www.algolia.com/) for search, and we update the Algolia search index [on every deployment](https://github.com/pulumi/docs/blob/master/scripts/ci-push.sh#L13) of the website. Whether you're adding a new page or updating an existing one, your changes will be reflected in search results within a few seconds of release.

### Creating findable content

We currently index every page of the website, including the blog and the Registry. However, we do not index all of the content of every page &mdash; we only index certain properties of the page. These include:

* Page titles (specifically the `title` and `h1` frontmatter params)
* Page descriptions (specifically the `meta_desc` param)
* Second-level headings (e.g., those prefixed with `##` in Markdown files)
* Keywords, if any (via the `search.keywords` param)
* Authors, if any (via the `authors` param)
* Tags, if any (via the `tags` param)

Because of this, it's important to be thoughtful about the terms you use for these fields, especially titles, keywords, descriptions, and H2 headings. If you want your content to be findable by specific terms, you must make sure those terms exist in one or more of the fields listed above.

For example, if you were writing a guide to building an ETL pipeline with Redshift, and you wanted to make sure the page would be surfaced for queries like `redshift data warehouse etl`, you might construct the page's frontmatter in the following way:

```yaml
title: Build an ETL pipeline with Redshift and AWS Glue
meta_desc: Learn how to combine AWS Glue and Amazon Redshift to build a fully-automated ETL pipeline with Pulumi.
search:
    keywords:
        - data warehouse
```

In this case, the optional `search.keywords` field is included to cover the terms `data warehouse`, as those terms don't exist in the page's title or description. If it weren't, queries for `data warehouse` would fail to match this particular page.

Certain fields also rank higher than others in terms of their overall relevance. (Titles and keywords, for example, are considered more relevant than descriptions.) For a full list of these rankings, along with all of the rules we apply to the search index, see the [search app in pulumi/docs](https://github.com/pulumi/docs/blob/master/scripts/search/settings.js).

### Keeping pages out of search results

To keep a page from showing up in search results (including on Google, etc.), use the `block_external_search_index` frontmatter parameter:

```yaml
title: My page
...
block_external_search_index: true
```
## Community

Engage with our community to elevate your developer experience:

- **Join our online [Pulumi Community on Slack](https://slack.pulumi.com/?utm_campaign=pulumi-docs-repo&utm_source=github.com&utm_medium=welcome-slack)** - Interact with thousands of Pulumi developers for collaborative problem-solving and knowledge-sharing!
- **Join a [Local Pulumi User Groups (PUGs)](https://www.meetup.com/pro/pugs/)**-  Attend tech-packed meetups and hands-on virtual or in-person workshops.
- **Follow [@PulumiCorp](https://twitter.com/PulumiCorp) on X (Twitter)** - Get real-time updates, technical insights, and sneak peeks into the latest features.
- **Subscribe to our YouTube Channel, [PulumiTV](https://www.youtube.com/@PulumiTV)** - Learn about AI / ML essentials, launches, workshops, demos and more.
- **Follow our [LinkedIn](https://www.linkedin.com/company/pulumi/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-community)** - Uncover company news, achievements, and behind-the-scenes glimpses.

## Pulumi developer resources

Delve deeper into Pulumi with additional resources:

- [Get Started with Pulumi](https://www.pulumi.com/docs/get-started/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-resources): Deploy a simple application in AWS, Azure, Google Cloud, or Kubernetes using Pulumi.
- [Registry](https://www.pulumi.com/registry/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-resources): Search for packages and learn about the supported resources you need. Install the package directly into your project, browse the API documentation, and start building.
- [Pulumi Blog](https://www.pulumi.com/blog/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-resources) - Stay in the loop with our latest tech announcements, insightful articles, and updates.
- [Try Pulumi AI](https://www.pulumi.com/ai/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-resources) - Use natural-language prompts to generate Pulumi infrastructure-as-code programs in any language.

## Pulumi roadmap

Review the planned work for the upcoming quarter and a selected backlog of issues that are on our mind but not yet scheduled on the [Pulumi Roadmap.](https://github.com/orgs/pulumi/projects/44)
