---
title: "pulumi import"
aliases:
  - /docs/reference/cli/pulumi_import/
---



Import resources into an existing stack

## Synopsis

Import resources into an existing stack.

Resources that are not managed by Pulumi can be imported into a Pulumi stack
using this command. A definition for each resource will be printed to stdout
in the language used by the project associated with the stack; these definitions
should be added to the Pulumi program. The resources are protected from deletion
by default.

Should you want to import your resource(s) without protection, you can pass
`--protect=false` as an argument to the command. This will leave all resources unprotected.

A single resource may be specified in the command line arguments or a set of
resources may be specified by a JSON file.

If using the command line args directly, the type token, name, id and optional flags
must be provided.  For example:

    pulumi import 'aws:iam/user:User' name id

The type token and property used for resource lookup are available in the Import section of
the resource's API documentation in the Pulumi Registry (https://www.pulumi.com/registry/).
To fully specify parent and/or provider, subsitute the <urn> for each into the following:

     pulumi import 'aws:iam/user:User' name id --parent 'parent=<urn>' --provider 'admin=<urn>'

If using the JSON file format to define the imported resource(s), use this instead:

     pulumi import -f import.json

Where import.json is a file that matches the following JSON format:

    {
        "nameTable": {
            "provider-or-parent-name-0": "provider-or-parent-urn-0",
            ...
            "provider-or-parent-name-n": "provider-or-parent-urn-n",
        },
        "resources": [
            {
                "type": "type-token",
                "name": "name",
                "id": "resource-id",
                "parent": "optional-parent-name",
                "provider": "optional-provider-name",
                "version": "optional-provider-version",
                "pluginDownloadUrl": "optional-provider-plugin-url",
                "logicalName": "optionalLogicalName",
                "properties": ["optional-property-names"],
                "component": false,
                "remote": false,
            },
            ...
            {
                ...
            }
        ],
    }

The name table maps language names to parent and provider URNs. These names are
used in the generated definitions, and should match the corresponding declarations
in the source program. This table is required if any parents or providers are
specified by the resources to import.

The resources list contains the set of resources to import. Each resource is
specified as a triple of its type, name, and ID. The format of the ID is specific
to the resource type. Each resource may specify the name of a parent or provider;
these names must correspond to entries in the name table. If a resource does not
specify a provider, it will be imported using the default provider for its type. A
resource that does specify a provider may specify the version of the provider
that will be used for its import.

A resource can define a logical name as well as its name for the name table.
If a logical name is given, it will be used to name the resource in the Pulumi state.

A resource can also be declared as a "component" (and optionally as "remote"). These resources
don't have an id set and instead just create an empty placeholder component resource in the Pulumi state.

Each resource may specify which input properties to import with;

If a resource does not specify any properties the default behaviour is to
import using all required properties.

You can use `pulumi preview` with the `--import-file` option to emit an import file
for all resources that need creating from the preview. This will fill in all the name,
type, parent and provider information for you and just require you to fill in resource
IDs and any properties.


```
pulumi import [type] [name] [id] [flags]
```

## Options

```
      --config-file string                    Use the configuration values in the specified file rather than detecting the file name
  -d, --debug                                 Print detailed debugging output during resource operations
      --diff                                  Display operation as a rich diff showing the overall change
  -f, --file string                           The path to a JSON-encoded file containing a list of resources to import
      --from string                           Invoke a converter to import the resources
      --generate-code                         Generate resource declaration code for the imported resources (default true)
  -h, --help                                  help for import
  -j, --json                                  Serialize the import diffs, operations, and overall output as JSON
  -m, --message string                        Optional message to associate with the update operation
  -o, --out string                            The path to the file that will contain the generated resource declarations
  -p, --parallel int32                        Allow P resource operations to run in parallel at once (1 for no parallelism). (default 16)
      --parent string                         The name and URN of the parent resource in the format name=urn, where name is the variable name of the parent resource
      --preview-only                          Only show a preview of the import, but don't perform the import itself
      --properties strings                    The property names to use for the import in the format name1,name2
      --protect                               Allow resources to be imported with protection from deletion enabled (default true)
      --provider string                       The name and URN of the provider to use for the import in the format name=urn, where name is the variable name for the provider resource
      --skip-preview                          Do not calculate a preview before performing the import
  -s, --stack string                          The name of the stack to operate on. Defaults to the current stack
      --suppress-outputs                      Suppress display of stack outputs (in case they contain sensitive values)
      --suppress-permalink string[="false"]   Suppress display of the state permalink
      --suppress-progress                     Suppress display of periodic progress dots
  -y, --yes                                   Automatically approve and perform the import after previewing it
```

## Options inherited from parent commands

```
      --color string                 Colorize output. Choices are: always, never, raw, auto (default "auto")
  -C, --cwd string                   Run pulumi as if it had been started in another directory
      --disable-integrity-checking   Disable integrity checking of checkpoint files
  -e, --emoji                        Enable emojis in the output
  -Q, --fully-qualify-stack-names    Show fully-qualified stack names
      --logflow                      Flow log settings to child processes (like plugins)
      --logtostderr                  Log to stderr instead of to files
      --memprofilerate int           Enable more precise (and expensive) memory allocation profiles by setting runtime.MemProfileRate
      --non-interactive              Disable interactive mode for all commands
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                  Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## SEE ALSO

* [pulumi](/docs/iac/cli/commands/pulumi/)	 - Pulumi command line

###### Auto generated by spf13/cobra on 24-Mar-2025
