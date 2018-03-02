# Pulumi Documentation Site

"Because knowing is half the battle."

| Staging | Production |
|---|---|
| [![Build Status](https://travis-ci.com/pulumi/docs.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https://travis-ci.com/pulumi/docs) | [![Build Status](https://travis-ci.com/pulumi/docs.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=production)](https://travis-ci.com/pulumi/docs) |


## Toolchain

The website is statically built using [Jekyll](https://jekyllrb.com). So we have basic templating
for generating HTML and the ability to write most files in Markdown.

TypeScript documentation is generated directly from source using [TYPEDOC](http://typedoc.org/). We
just check the resulting files directly into the repo under `./libraries/`.

## Development

Run `make configure` to get the required Gem dependencies. (Assuming you have a recent Ruby
installation on your system.

`make build` will generate the website (published to _site).

`make generate` will regenerate the TypeScript documentation if needed. Requires you have the
other Pulumi repos (pulumi, pulumi-cloud, pulumi-aws) as peers of the docs repo and in a good
working state.

`make serve` will build the website and serve it to http://localhost:4000.

## Site structure

- There is a folder for each heading in the top navigation, such as `Install`, `Quickstart`, etc.

- The mapping from documentation page to section and table-of-contents (TOC) is stored in yaml files in `_data`. 

- To rename a section, rename both the value of `nav_section` in the toc yaml file (e.g., `_data\install.yaml`) and update the layout in `_includes\header.html`.

- To add a new article and add it to the table-of-contents for that section, create a new file in the right section and add an entry in the corresponding file in `_data\top-level-section.yaml`.

## Design Reference

Web design is hard. Documentation is hard. Good web design for documentation is harder.

Examples of other sites and their docs as inspiration:

- https://kubernetes.github.io/
- https://devcenter.heroku.com/
- https://stripe.com/docs/api/curl#authentication
- http://developer.mailchimp.com/documentation/mailchimp/
- http://ionicframework.com/docs/
- https://www.twilio.com/docs/
