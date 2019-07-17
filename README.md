# Pulumi Documentation Site

| Staging | Production |
|---|---|
| [![Build Status](https://travis-ci.com/pulumi/docs.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https://travis-ci.com/pulumi/docs) | [![Build Status](https://travis-ci.com/pulumi/docs.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=production)](https://travis-ci.com/pulumi/docs) |

## Contributing

**Before adding new content, read [CONTRIBUTING.md](CONTRIBUTING.md).**

## Toolchain

The website is statically built using [Hugo](https://gohugo.io). So we have basic templating
for generating HTML and the ability to write most files in Markdown.

TypeScript documentation is generated directly from source using [TYPEDOC](http://typedoc.org/). We
just check the resulting files directly into the repo under `./content/reference/pkg/nodejs`.

## Development

### Prerequisites

- [Node.js and npm](https://www.npmjs.com/get-npm)
- [Ruby](https://www.ruby-lang.org/en/downloads/)
- [Yarn](https://yarnpkg.com/en/docs/install) for installing dependencies in package.json
- [Hugo](#hugo)
- [Go](https://golang.org/dl/)

#### Hugo

The website is powered by [Hugo](https://gohugo.io).

**IMPORTANT.** Recent versions of Hugo have bugs in the markdown renderer (Blackfriday) that prevents fenced code from rendering correctly in lists when a language is specified. Many of our tutorials are made up of ordered lists of steps, each step containing a code snippet. Until those bugs are fixed, and Hugo has adopted the version of Blackfriday with the fixes, we'll pin to [Hugo v0.55.4](https://github.com/gohugoio/hugo/releases/tag/v0.55.4). Tracking issue: https://github.com/pulumi/docs/issues/1091

#### macOS

The following commands use the package manager, [Homebrew](https://brew.sh/). 

##### Install Hugo 

If you already have Hugo installed, uninstall it:

```bash
brew uninstall hugo
```

Install Hugo v0.55.4:

```bash
brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/cf3219506fd28f7133041b74761e8025418435a3/Formula/hugo.rb
```

To prevent brew from upgrading Hugo:

```bash
brew pin hugo
```

##### Install Go


```bash
brew install go
```

#### Linux (Ubuntu)

##### Install Hugo

The quickest way to install the extended version of Hugo v0.55.4 on your Linux machine is to use `wget` and the `dpkg` utility. For confirming your server architecture and post-installation cleanup, see [Installing Hugo Using the dpkg utility](https://hostadvice.com/how-to/how-to-install-hugo-on-ubuntu-18-04).

```bash
wget https://github.com/gohugoio/hugo/releases/download/v0.55.4/hugo_extended_0.55.4_Linux-64bit.deb
```

```bash
sudo dpkg -i hugo_extended_0.55.4_Linux-64bit.deb
```

If you wish to use `brew` on Linux, see [Homebrew on Linux](https://docs.brew.sh/Homebrew-on-Linux).

##### Install Go

Download the Linux package from https://golang.org/dl/. Follow [installation and setup steps](https://tecadmin.net/install-go-on-ubuntu/) on "Installing Go on Ubuntu".

#### Go-based Tools

There are several other Go-based tools to install as well.

```bash
go get -u github.com/cbroglie/mustache
go get -u github.com/gobuffalo/packr
```

### Makefile

`make ensure` will run `yarn install` which resolves project dependencies.

`make build` will generate the website (published to public).

`make serve` will build the website and serve it to http://localhost:1313.

`make test` runs a broken link checker tool against http://localhost:1313.

`make generate` will regenerate the TypeScript documentation if needed, as well as the CLI documentation in [content/references/cli](content/reference/cli). The generated API documentation is placed in the [/content/reference/pkg/nodejs]/content/reference/pkg/nodejs) folder. This is extremely hacky.

The following repos must be peers of `docs`, should be checked out to an appropriate branch, and should be built before running `make generate`:

- `pulumi`
- `pulumi-aws`
- `pulumi-azure`
- `pulumi-cloud`
- `pulumi-gcp`
- `pulumi-kubernetes`
- etc.

## Updating API docs

to update API docs for all Pulumi packages, run the following commands to fetch latest release of each package and rebuild docs into `.content/reference/pkg` folder:

```bash
./scripts/update_repos.sh
./scripts/run_typedoc.sh
```

To update a single package, make sure you have it checked out at the desired release label, and then run:

```bash
PKGS=yourpackagename ./scripts/run_typedoc.sh
```

Docs for additional packages can be added by updating `./scripts/run_typedoc.sh` to include the package, and then updating `./config.toml` to include the package in the TOC as a `[[menu.reference]]` entry.

## Deploying updates

When changes are merged into `master` our staging website (https://staging.pulumi.io/) is automatically deployed. You can use the [Travis UI](https://travis-ci.com/pulumi/docs) to check on the status of the deployment. Once it has been deployed, browse around the staging website and ensure the changes you expected were made and render correctly. Then, open a Pull Request to merge `master` into `production`.

## Design Reference

Web design is hard. Documentation is hard. Good web design for documentation is harder.

Examples of other sites and their docs as inspiration:

- https://kubernetes.github.io/
- https://devcenter.heroku.com/
- https://stripe.com/docs/api/curl#authentication
- http://developer.mailchimp.com/documentation/mailchimp/
- http://ionicframework.com/docs/
- https://www.twilio.com/docs/
