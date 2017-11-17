# Pulumi Documentation Site

"Because knowing is half the battle."

## Toolchain

The website is statically built using [Jekyll](https://jekyllrb.com). So we have basic templating
for generating HTML and the ability to write most files in Markdown.

TypeScript documentation is generated directly from source using [TYPEDOC](http://typedoc.org/). We
just check the resulting files directly into the repo under `./libraries/`.

## Git LFS

We use Git LFS to manage release binaries that are checked in.  Please ensure that you've [installed Git LFS](
https://help.github.com/articles/installing-git-large-file-storage/) before cloning the repo.  See [this tutorial](
https://help.github.com/articles/configuring-git-large-file-storage/) for more information on using Git LFS with GitHub.

## Development

Run `make configure` to get the required Gem dependencies. (Assuming you have a recent Ruby
installation on your system.

`make build` will generate the website (published to _site).

`make generate` will regenerate the TypeScript documentation if needed. Requires you have the
other Pulumi repos (pulumi, pulumi-cloud, pulumi-aws) as peers of the docs repo and in a good
working state.

`make serve` will build the website and serve it to http://localhost:4000.

## Design Reference

Web design is hard. Documentation is hard. Good web design for documentation is harder.

Examples of other sites and their docs as inspiration:

- https://kubernetes.github.io/
- https://devcenter.heroku.com/
- https://stripe.com/docs/api/curl#authentication
- http://developer.mailchimp.com/documentation/mailchimp/
- http://ionicframework.com/docs/
- https://www.twilio.com/docs/
