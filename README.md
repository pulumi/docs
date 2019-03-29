# Pulumi Documentation Site

"Because knowing is half the battle."

| Staging | Production |
|---|---|
| [![Build Status](https://travis-ci.com/pulumi/docs.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https://travis-ci.com/pulumi/docs) | [![Build Status](https://travis-ci.com/pulumi/docs.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=production)](https://travis-ci.com/pulumi/docs) |

## Contributing

**Before adding new content, read [CONTRIBUTING.md](CONTRIBUTING.md).**

## Toolchain

The website is statically built using [Jekyll](https://jekyllrb.com). So we have basic templating
for generating HTML and the ability to write most files in Markdown.

TypeScript documentation is generated directly from source using [TYPEDOC](http://typedoc.org/). We
just check the resulting files directly into the repo under `./packages/`.

## Development

### Prerequisites
- Install a recent version of Ruby
- Install the necessary Ruby Gems:
  ```gem install jekyll bundler```
- Install a recent version of Go
- Install mustache:
  ```go get -u github.com/cbroglie/mustache```
- Install packr:
  ```go get -u github.com/gobuffalo/packr```

Run `make configure` to get the required Gem dependencies. (Assuming you have a recent Ruby
installation on your system.

`make build` will generate the website (published to _site).

`make serve` will build the website and serve it to http://localhost:4000.

`make docker` will run `build` and `serve` in a docker container with all prerequisites installed.

`make test` runs a broken link checker tool against http://localhost:4000.

`make generate` will regenerate the TypeScript documentation if needed, as well as the CLI documentation in [references/cli](reference/cli). The generated API documentation is placed in the [packages](packages/) folder. This is extremely hacky.

The following repos must be peers of `docs`, should be checked out to an appropriate branch, and should be built before running `make generate`:
- `pulumi`
- `pulumi-aws`
- `pulumi-azure`
- `pulumi-cloud`
- `pulumi-gcp`
- `pulumi-kubernetes`

## Updating API docs

to update API docs for all Pulumi packages, run the following commands to fetch latest release of each pacakge and rebuild docs into `./reference/pkg` folder:

```
$ ./scripts/update_repos.sh
$ ./scripts/run_typedoc.sh
```

To update a single package, make sure you have it checked out at the desired release label, and then run:

```
$ PKGS=yourpackagename ./scripts/run_typedoc.sh
```

Docs for additional pacakges can be added by updating `./scripts/run_typedoc.sh` to include the package, and then updating `./_data/reference.yaml` to include the package in the TOC.

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

## Creating shortlinks

Shortlinks can be created as a permanent reference to documentation that may move around in the repo.
This is particularly useful for troubleshooting links that are produced by CLI tools.

To create a shortlink, create a file under `/shortlinks` in the following format:

```md
---
redirect_to: <link-to-current-docs-page>
permalink: <unique-6-character-shortlink>/
---
```


You can use the scripts/create_short_url.sh script to generate a new random shortlink:

```sh
./scripts/create_short_url.sh /reference/troubleshooting#ingress-status-loadbalancer ingress-status-loadbalancer

Created shortlink definition at <filepath>/ingress-status-loadbalancer.md
https://pulumi.io/xdv72s --> https://pulumi.io/reference/troubleshooting#ingress-status-loadbalancer
```

or you can choose a shortlink:

```sh
./scripts/create_short_url.sh /reference/troubleshooting#ingress-status-loadbalancer ingress-status-loadbalancer help/ingress-lbstaus


Created shortlink definition at <filepath>/ingress-status-loadbalancer.md
https://pulumi.io/help/ingress-lbstatus --> https://pulumi.io/reference/troubleshooting#ingress-status-loadbalancer
```


Here is a concrete example:

```md
---
redirect_to: /reference/troubleshooting.html#ingress-status-loadbalancer
permalink: xdv72s/
---
```

With the above file in place, a redirect will be created from `https://pulumi.io/xdv72s`
to `https://pulumi.io/reference/troubleshooting.html#ingress-status-loadbalancer`

**Note that the trailing `/` on the permalink is required!**

