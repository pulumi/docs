# Pulumi Documentation Site

![Deployment Status](https://github.com/pulumi/docs/actions/workflows/build-and-deploy.yml/badge.svg?branch=master)

## Contributing

First, be sure to read our [contributing guide](CONTRIBUTING.md) and review our [code of conduct](CODE_OF_CONDUCT.md).

## About this repository

This repository hosts the documentation we generate for the Pulumi CLI, SDK, and tutorials sourced from https://github.com/pulumi/examples. It's also responsible for building and deploying the https://www.pulumi.com website.

If you're interested in contributing a blog post or other documentation, you'll probably want [pulumi/pulumi-hugo](https://github.com/pulumi/pulumi-hugo) instead. There, you'll find all of our hand-authored documentation, including, guides, tutorials, blogs, and landing pages, along with all of the assets and templates we use to render the website. You'll also find all of the instructions you need to get going.
## Toolchain

We build the Pulumi website statically with Hugo, manage our dependencies with Node.js and Yarn, and write our documentation in Markdown. Below is a list of the tools you'll need if you'd like to work on the project:

* [Go](https://golang.org/)
* [Hugo](https://gohugo.io)
* [Node.js](https://nodejs.org/en/)
* [Yarn](https://classic.yarnpkg.com/en/)

Out TypeScript documentation is generated directly from source using [TypeDoc](http://typedoc.org/), and we check in the resulting files at `./content/reference/pkg/nodejs`.

#### Go-based tools

In order to run the documentation generators, you'll need to install some additional Go-based tools as well:

```bash
go get -u github.com/cbroglie/mustache
go get -u github.com/gobuffalo/packr
go get -u github.com/pkg/errors
go get -u github.com/russross/blackfriday/v2
```
### Makefile

The `Makefile` exposes a number of helpers:

* `make ensure` resolves and installs dependencies
* `make lint` checks all Markdown files for correctness
* `make build` generates the website and writes it to `./public`
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

The primary script is `./scripts/gen_resource_docs.sh`. The script takes the following arguments (in order):

* The provider package name, ex. `aws`.
* Whether to install the resource plugin (almost always should be `true`): `true` or `false`.
* The version of the provider so that the provider repo will be checked out at that version, as well as the resource plugin for that version will be installed.
  * The version must match a release tag exactly.

We currently have CI in-place to call the above script whenever a new provider version is released. See [`build-package-docs.sh`](https://github.com/pulumi/scripts/blob/master/ci/build-package-docs.sh#L62) in the `pulumi/scripts` repo.

If you are looking to generate resource docs for _all_ providers, then you might find `./scripts/gen_all_resource_docs.sh` useful. The only use-case for this script is if you need to regenerate docs for all supported providers out-of-band from CI on your local machine and then a PR for it.

## Enlisting a new provider for docs

### Generating docs for a new provider
Since Pulumi uses CI to generate docs, there isn't a need to keep scripts up-to-date when docs for a new provider
 need to be generated. Every provider repo uses similar `Makefile`  that contains calls to the
  relevant scripts to generate docs for that provider when a new version is released.

However, there may be times when you need to generate docs for all providers out-of-band and submit a PR for it. To
 do that, ensure that the following files have all of the providers listed:
* For NodeJS API docs: `scripts/run_typedoc.sh`
* For Python API docs: `scripts/generate_python_docs.sh` and `tools/pydocgen/pulumi-docs.json`
* For Resource docs: `scripts/generate_all_resource_docs.sh`

See each script for its usage, and the optional arguments they may accept.

### Creating a new cloud providers intro page

Add a new folder under `content/docs/intro/cloud-providers` with instructions on how to use the provider.

## Deploying updates

When changes are merged into `master`, https://www.pulumi.com/ is automatically deployed.
