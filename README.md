# Pulumi Documentation Site

"Because knowing is half the battle."

| Staging | Production |
|---|---|
| [![Build Status](https://travis-ci.com/pulumi/docs.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https://travis-ci.com/pulumi/docs) | [![Build Status](https://travis-ci.com/pulumi/docs.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=production)](https://travis-ci.com/pulumi/docs) |


## Toolchain

The website is statically built using [Jekyll](https://jekyllrb.com). So we have basic templating
for generating HTML and the ability to write most files in Markdown.

TypeScript documentation is generated directly from source using [TYPEDOC](http://typedoc.org/). We
just check the resulting files directly into the repo under `./packages/`.

## Development

Run `make configure` to get the required Gem dependencies. (Assuming you have a recent Ruby
installation on your system.

`make build` will generate the website (published to _site).

`make generate` will regenerate the TypeScript documentation if needed. The generated documentation is placed in the [packages](packages/) folder. This is extremely hacky.

   Prerequisites:
  - Ensure that repos `pulumi`, `pulumi-aws`, and `pulumi-cloud` are peers to `docs`, and have been checked out to the right release branch.
  - Run `make only_build` in each of these repos
  - Install typedoc globally:
    ```npm install -g typedoc@0.8```
  - Patch typedoc so it doesn't bring its own version of TypeScript. For more information, see [this issue comment in typedoc](https://github.com/TypeStrong/typedoc/issues/624#issuecomment-352897218). On a Mac:
    ```rm -rf /usr/local/lib/node_modules/typedoc/node_modules/typescript/```
  - Install TypeScript globally:
    ```npm install -g typescript@2.6.2```

`make serve` will build the website and serve it to http://localhost:4000.

## Site structure

- There is a folder for each heading in the top navigation, such as `Install`, `Quickstart`, etc.

- The mapping from documentation page to section and table-of-contents (TOC) is stored in yaml files in `_data`. 

- To rename a section, rename both the value of `nav_section` in the toc yaml file (e.g., [`_data/install.yaml`](_data/install.yaml)) and update the layout in [`_includes/header.html`](_includes/header.html).

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
