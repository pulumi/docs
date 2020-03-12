# Resource Docs generator driver

This tool generates the provider schema using `tfgen`, then calls the docs generator tool in `pulumi/pulumi` to use the schema to generate docs.

## Generating docs

Run `make resource_docs`.

### Using the latest templates in `pulumi/pulumi`

This tool indirectly depends on the `pulumi/pulumi` repo, namely the `pkg/codegen/docs` generator and the templates it uses, which is the underlying tool responsible for generating docs from the Pulumi schema.

To make changes to the templates or to use the latest ones from `master`, you will need to override the module path for `pulumi/pulumi` in your local copy of `pulumi-terraform-bridge` using:

```
go mod edit -replace github.com/pulumi/pulumi=path/to/local/repo
```

where `/path/to/local/repo` is the path to the `pulumi/pulumi` repo on your machine. This will ensure that the docs are generated using the templates in your local machine rather than the released version.
