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
- Ensure `jq` is installed, e.g. on macOS:
  ```brew install jq```

Run `make configure` to get the required Gem dependencies. (Assuming you have a recent Ruby
installation on your system.

`make build` will generate the website (published to _site).

`make serve` will build the website and serve it to http://localhost:4000.

`make test` runs a broken link checker tool against http://localhost:4000.

`make generate` will regenerate the TypeScript documentation if needed, as well as the CLI documentation in [references/cli](reference/cli). The generated API documentation is placed in the [packages](packages/) folder. This is extremely hacky.

The following repos must be peers of `docs`, should be checked out to an appropriate branch, and should be built before running `make generate`:
- `pulumi`
- `pulumi-aws`
- `pulumi-azure`
- `pulumi-cloud`
- `pulumi-gcp`
- `pulumi-kubernetes`

## Generating a change log

To generate a change log from closed pull requests, run the script `/scripts/generate_changelog.sh`. It generates a file using the rules documented here: [Planning, Work Items, and Changelog](https://github.com/pulumi/home/wiki/Planning,-Work-Items,-and-Changelog#tldr-minimal-label-requirements).

1. Run `./scripts/update_repos.sh` to pull down the latest tags for the repos `pulumi`, `pulumi-cloud`, `pulumi-aws`, `pulumi-terraform`, and `pulumi-azure`

1. Set the environment variable `GITHUB_TOKEN` to a token that has "repo" scope.

1. [Will be improved] Clone the repo at https://github.com/pulumi/github-pr-changelog and run `npm i -g` to globally install the command `gh-changelog`.

1. Generate a change log with the following command:

    ```
    ./scripts/generate_changelog.sh <from-git-tag> <to-git-tag> > output.file
    ```

    You can also use the optional flags `--all-prs` to print out all PRs (not just ones with the relevant labels) and `--tab-output` to print in a format that can be pasted to a Google Sheet.

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
