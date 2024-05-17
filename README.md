# Pulumi Documentation Site

![Deployment Status](https://github.com/pulumi/docs/actions/workflows/build-and-deploy.yml/badge.svg?branch=master&event=push)
![Examples Tests](https://github.com/pulumi/docs/actions/workflows/scheduled-test.yml/badge.svg?branch=master)

## About this repository

This repository hosts all of the hand-crafted documentation, guides, tutorials, blogs, and landing pages that you see on https://pulumi.com, as well as all of the assets and templates we use to render the Pulumi website. It also houses the documentation that we generate for the Pulumi CLI and language SDKs, and it's responsible for building and deploying the website (with Pulumi, of course!).

### What's not in this repository

* Pulumi AI: You'll find the open-source components of the Pulumi AI project at https://github.com/pulumi/pulumi-ai.
* Pulumi Registry: You'll find everything related to the Registry at https://github.com/pulumi/registry.

## Contributing

We welcome all contributions to this repository. Be sure to read our [contributing guide](CONTRIBUTING.md) and [code of conduct](CODE-OF-CONDUCT.md) first, then [submit a pull request](https://github.com/pulumi/docs/pulls) here on GitHub. If you see something that needs fixing but don't have time to contribute, you can also [file an issue](https://github.com/pulumi/docs/issues).

See also:

* [Publishing a Pulumi blog post](./BLOGGING.md)
* [Documentation and coding style guide](./STYLE-GUIDE.md)

## Toolchain

We build the Pulumi website with Hugo, manage our dependencies with Node.js and Yarn, and write our documentation in Markdown. Below is a list of the tools you'll need if you'd like to work on the website (e.g., to contribute docs content, a blog post, etc.):

* [Hugo](https://gohugo.io) (>= 0.111.0)
  * Hugo 0.111.0 is highly recommended. This is the version we use in our deployment pipelines.
* [Node.js](https://nodejs.org/en/) (>= 18)
* [Yarn](https://classic.yarnpkg.com/en/) (1.x)

Additionally, to build the SDK and CLI documentation, you'll also need:

* [Go](https://golang.org/) (>= 1.21)
* [Python](https://www.python.org) (>= 3.7)
* [.NET](https://dotnet.microsoft.com/en-us/download) (>= 6)
* [Pulumi](https://www.pulumi.com/docs/install)
* [Pulumi ESC](https://www.pulumi.com/docs/install/esc)

## Repository layout

* Documentation and page content: We generally follow Hugo's [directory-structure conventions](https://gohugo.io/getting-started/directory-structure/), with Markdown files in `./content`, layout files (including partials and shortcodes) in `./layout`, and data files in `./data`. There are also several [Hugo templates](https://gohugo.io/content-management/archetypes/) available in `./archetypes` for bootstrapping common content types like blog posts and Learn modules.

* CSS and JavaScript: We build our CSS and JavaScript bundles separately from Hugo and check in the built artifacts at `./assets`. We use [Tailwind](https://tailwindcss.com/) for CSS, [Stencil](https://stenciljs.com/) for web components, and [jQuery](https://jquery.com/) for wiring things together in general.

* Examples: Many of the examples we include in our documentation are maintained as full Pulumi programs and tested daily. You'll find them all at `./static/programs`.

* Infrastructure: We deploy the website as a statically built artifact to a unique Amazon S3 bucket on every commit to the base branch of this repo. The Pulumi program that handles this is located in `./infrastructure`. This is also where you'll find the CloudFront configuration that handles proxying [Pulumi AI](https://pulumi.com/ai) and the [Pulumi Registry](https://pulumi.com/registry).

## Makefile

The `Makefile` exposes a number of useful helpers:

* `make ensure` resolves and installs all dependencies
* `make lint` checks all Markdown files for correctness
* `make format` formats all applicable files to ensure they conform to style guidelines
* `make serve` runs the Hugo server locally at http://localhost:1313 and watches content and layout folders for changes
* `make serve-all` does the same as `make serve`, but also watches changes to CSS and JS source files and rebuilds those as well
* `make build` generates the website and writes it to `./public`
* `make serve-static` runs a local HTTP server that serves the contents of `./public`
* `make test` tests all of the programs in `./static/programs` (pass `ONLY_TEST="your-prefix-*"` to test only a subset of them)
* `make generate` builds the TypeScript, Python, and CLI documentation
* `make new-blog-post` scaffolds a new, bare-bones blog post with placeholder content
* `make new-example-program` generates a new, named set of new Pulumi programs at `./static/programs` for use site-wide

## Generating SDK and CLI documentation

We generate two kinds of reference documentation with this repository: language-specific SDK docs (for a subset of Pulumi packages) and CLI docs (for command-line tools like `pulumi` and `esc`). Instructions for generating both types of docs are listed below.

### SDK docs

We build and host language-specific SDK documentation for the following Pulumi packages:

* [pulumi](https://github.com/pulumi/pulumi)
* [pulumi-awsx](https://github.com/pulumi/pulumi-awsx)
* [pulumi-cloud](https://github.com/pulumi/pulumi-cloud)
* [pulumi-kubernetesx](https://github.com/pulumi/pulumi-kubernetesx)
* [pulumi-policy](https://github.com/pulumi/pulumi-policy)
* [pulumi-terraform](https://github.com/pulumi/pulumi-terraform)

The Node.js, Python, and .NET versions of these docs are built using language-specific tooling and checked into the repository as stand-alone mini-sites. (Go versions are sourced directly from GitHub source and hosted at [https://pkg.go.dev](/github.com/pulumi/pulumi/sdk/v3/go/pulumi).)

To build the docs for these packages yourself, you'll first need to clone each package into a sibling directory. The easiest way to do this is to use the `make update-repos` helper:


```bash
# Clone and update all of the repositories above into sibling directories of this repo.
make update-repos
```

Once you've done this, you can generate the docs for each package.

#### Generating the Node.js and Python SDK docs

The Node and Python SDK docs are built with [TypeDoc](http://typedoc.org/) and [Pydocgen](https://pypi.org/project/pydocgen/). The easiest way to generate these docs is to use the `make generate` helper:

```bash
make ensure          # Install dependencies.
make update-repos    # Clone and update all package repositories.
make generate        # Generate the Node.js and Python docs for all packages.
```

Generated docs are rendered into the `./static-prebuilt/nodejs` and `./static-prebuilt/python` folders. At deploy-time, we copy the contents of these folders into `./docs/reference/pkg` to make them available on pulumi.com --- for example, [here](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/pulumi) and [here](https://www.pulumi.com/docs/reference/pkg/python/pulumi).

See below to learn how to view these rendered docs locally.

#### Generating the .NET SDK docs

The .NET SDK docs are built with [Docfx](https://github.com/dotnet/docfx). To generate these docs, you'll need both `dotnet` and `docfx` installed and on your PATH. For example, assuming you've already [installed the `dotnet` executable](https://dotnet.microsoft.com/en-us/download) for your platform, you can:

```bash
make ensure                     # Install dependencies.
make update-repos               # Clone and update all package repositories.
dotnet tool install -g docfx    # Install docfx globally, following the instructions to ensure it's on your PATH.
docfx build docfx/docfx.json    # Generate the .NET docs.
```

### CLI docs

The `make generate` helper also generates the Pulumi CLI documentation. If you'd prefer not to use that helper (for example, to avoid having to clone package repos and generate any SDK docs), you can build them directly using the `pulumi` and `esc` CLIs:

```bash
pulumi gen-markdown ./content/docs/cli/commands         # Generate Pulumi CLI documentation.
pulumi esc gen-docs ./content/docs/esc-cli/commands     # Generate Pulumi ESC CLI documentation.
```

### Viewing rendered SDK and CLI docs locally

After building the SDK and/or CLI docs, you can view them locally by running `make build` followed by `make serve-static`.

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

All generated docs, including Node.js, Python, and .NET SDK docs and all CLI docs, get checked into the repository.

## Migrating from pulumi-hugo

The pulumi-hugo repository was archived on May 16, 2024. This repository previously housed most of our website content. This content has now moved to this repository. There is a slight directory structure change in this repo compared to pulumi-hugo. For the most part, everything that was located under the `themes/default` directory in pulumi-hugo now lives under the root directory of this repository, i.e. `themes/default/content/blog` is now under `/content/blog`. Everything still functions the same way it did previously when it comes to local devleopment, e.g. `make ensure`, `make serve`, `make build-assets`, etc.

### How to migrate PRs from the pulumi-hugo repo

If you have open pull requests in the pulumi-hugo repo, here are the steps to follow in order to move them over to the docs repository. You will need to copy over your files to the docs repo and place them in the new directory location.

#### Steps:
1. Clone the docs repo if you haven't done so already.
2. Create a new branch in the docs repository.
3. Copy the files you changed/added to the docs repo. The directory structure is similar to how this repo was configured, except everything under themes/default has been moved to the root. For example, if you have a blog under `themes/default/content/blog/my-cool-blog`, you will need to relocate it under `content/blog/my-cool-blog` in the docs repo.
4. Run make ensure in the docs repo and then a make serve to verify the files have been moved correctly.
5. Push changes to the docs repo.
6. Open a PR in the docs repo to add the changes there.
