# Resource Docs generator driver

This tool calls the docs generator tool in `pulumi/pulumi` which uses the Pulumi schema for a package to generate API (resource) docs.

## Installation

You can install the `resorucedocsgen` tool just like any other Go-based CLI tool:

```
go install github.com/pulumi/docs/tools/resourcedocsgen@master
```

To build and install from source:

```
cd tools/resourcedocsgen
go build -o "${GOPATH}/bin/resourcedocsgen" .
```

## Usage

Then you can run any of the available commands using `resourcedocsgen <command> <flags>`. Run `resourcedocsgen --help` to see the available commands.

As of this writing, the tool supports two main purposes:

* Generate the registry metadata
* Generate API docs and the package nav tree

### Generating package metadata

Package metadata is used by the [Pulumi Registry](https://github.com/pulumi/registry) to generate the listing shown at https://pulumi.com/registry.
The metadata file contains information sourced from the package's own Pulumi schema. The `metadata` command can be invoked via the
`generate_package_metadata.sh` script that accepts overrides for most of the properties in the metadata file.

The script provides a wrapper around determining the default location for a package's schema file and also marks a fixed set of
well-known packages as "featured" for the appropriate listing in the Pulumi Registry.

> You can invoke the `metadata` command directly as well. You can use the `generate_package_metadata.sh` as a reference.

### Generating API docs and the package nav tree

* The `docs` command. This command expects the package repo to be cloned alongside the `docs` repo. To help with invoking this command
with the right values, the `gen_resource_docs.sh` script can be used. Run `. ./scripts/gen_resource_docs.sh` from the root of this repo
with the arguments that the script accepts.
* The `registry` command. This command is a child of the above `docs` command. It uses the information in the registry repo at the commit
hash that the `docs` Hugo module depends on. Specifically, it uses the metadata files from the `data` folder of the registry repo's default
Hugo module. The metadata files serve as a snapshot of what packages exist in the registry and therefore, the packages for which API docs
need to be built. If you are running this command from anywhere but the `tools/resourcedocsgen` folder, you should override the values
for `baseDocsOutDir` and `basePackageTreeJSONOutDir`. For example, you might want to run this command to generate API docs and nav tree files
for a certain package (or all packages) within the registry repo for development purposes.

For both of the above commands, the default location for generating the API docs is `content/registry/packages/<package name>/api-docs`
and for the nav tree it is `static/registry/packages/navs/<package name>.json`.

### Updating the API docs templates

This tool depends on the `pulumi/pulumi` repo, namely the `pkg/codegen/docs` generator.
The docs generator uses Go-based [templates](https://github.com/pulumi/pulumi/tree/master/pkg/codegen/docs/templates) to render the markdown files in-memory which this tool then writes to the filesystem.

To make changes to the templates, make sure you have `pulumi/pulumi` cloned locally and override the `github.com/pulumi/pulumi/pkg/v3` dependency to point to
your local repo for testing out the changes to the templates. Once done, you must submit a PR to the `pulumi/pulumi` repo.

Once your `pulumi/pulumi` PR is merged, you should update the pseudo-version that this tool uses by running:

```
go get -u github.com/pulumi/pulumi/pkg/v3@<commit hash>
go get -u github.com/pulumi/pulumi/sdk/v3@<commit hash>
```
