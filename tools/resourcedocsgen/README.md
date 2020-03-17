# Resource Docs generator driver

This tool generates the provider schema using `tfgen`, then calls the docs generator tool in `pulumi/pulumi` to use the schema to generate docs.

## Generating docs

Run `make resource_docs`.

### Using the latest templates in `pulumi/pulumi`

This tool indirectly depends on the `pulumi/pulumi` repo, namely the `pkg/codegen/docs` generator and the templates it uses, which is the underlying tool responsible for generating docs from the Pulumi schema.

To make changes to the templates or to use the latest ones from `master`, make sure you have `pulumi/pulumi` cloned at the right commit hash, or have made changes to the templates in that repo locally.

> Any updates to the templates must also be submitted as a PR to the `pulumi/pulumi` repo as well for the time being.
