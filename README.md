# Pulumi Documentation Site

![Deployment Status](https://github.com/pulumi/docs/actions/workflows/build-and-deploy.yml/badge.svg?branch=master)

## Contributing

First, be sure to read our [contributing guide](CONTRIBUTING.md) and review our [code of conduct](CODE-OF-CONDUCT.md).

## About this repository

This repository hosts the documentation that we **generate** for the Pulumi CLI, SDK, and tutorials sourced from https://github.com/pulumi/examples. It's also responsible for building and deploying the https://www.pulumi.com website.

If you're interested in contributing a blog post or other documentation, **you'll likely want to consult [pulumi/pulumi-hugo](https://github.com/pulumi/pulumi-hugo) instead**. There, you'll find all of our hand-crafted documentation, including, guides, tutorials, blogs, and landing pages, along with all of the assets and templates we use to render the Pulumi website. You'll also find all of the instructions you need to get going.
## Toolchain

We build the Pulumi website statically with Hugo, manage our dependencies with Node.js and Yarn, and write our documentation in Markdown. Below is a list of the tools you'll need if you'd like to work on the project:

* [Go](https://golang.org/) (>= 1.15)
* [Hugo](https://gohugo.io) (>= 0.92)
* [Node.js](https://nodejs.org/en/) (>= 18)
* [Yarn](https://classic.yarnpkg.com/en/) (1.x)

Our TypeScript documentation is generated directly from source using [TypeDoc](http://typedoc.org/), and we check in the resulting files at `./content/reference/pkg/nodejs`.

#### Go-based tools

In order to run the documentation generators, you'll need to install some additional Go-based tools as well:

```bash
go install github.com/cbroglie/mustache@latest
go install github.com/gobuffalo/packr@latest
go install github.com/pkg/errors@latest
go install github.com/russross/blackfriday/v2@latest
```
### Makefile

The `Makefile` exposes a number of helpers:

* `make ensure` resolves and installs dependencies, including the Hugo module containing website layouts and content
* `make lint` checks all Markdown files for correctness
* `make build` generates the website and writes it to `./public`
* `make serve-static` runs a local HTTP server that serves the contents of `./public`
* `make test` runs a script that checks for broken links
* `make generate` builds the TypeScript, Python, and CLI documentation, and renders tutorials sourced from https://github.com/pulumi/examples.

## Generating API docs

To update API docs for all Pulumi packages, run the following commands to fetch latest the release of each package (packages must be sibling directories alongside this repository) and rebuild docs into `./content/reference/pkg`:

```bash
./scripts/update_repos.sh
./scripts/run_typedoc.sh
```

To update a single package, make sure you have it checked out at the desired release label, and then run:

```bash
PKGS=yourpackagename ./scripts/run_typedoc.sh
```

Docs for additional packages can be added by updating `./scripts/run_typedoc.sh` to include the package, and then updating `./config.yml` to include the package in the website table of contents as a menu entry.

## Generating resource docs

> Resource docs are only available for providers for which we can generate a Pulumi schema.

For more information see https://github.com/pulumi/docs/blob/master/tools/resourcedocsgen/README.md

## Deploying updates

When changes are merged into `master`, https://www.pulumi.com/ is automatically deployed.
