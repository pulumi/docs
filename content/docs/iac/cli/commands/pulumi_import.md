---
title: "pulumi import | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_import/
meta_desc: "Learn about the pulumi import command."
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

When importing multiple resources at once the `--file` option can be used to pass a JSON file
containing multiple resources: 
     pulumi import --file import.json

Where import.json is a file that matches the following JSON format:

    {
        "resources": [
            {
                "type": "aws:ec2/vpc:Vpc",
                "name": "application-vpc",
                "id": "vpc-0ad77710973388316"
            },
            ...
            {
                ...
            }
        ],
    }

The full import file schema references can be found in the [import documentation](https://www.pulumi.com/docs/iac/adopting-pulumi/import/#bulk-import-operations).

The import JSON file can be generated from a Pulumi program by running

    pulumi preview --import-file import.json

This will create entries for all resources that need creating from the preview, filling
in the name, type, parent and provider information and just requiring you to fill in the
resource IDs.


```
pulumi import [arg]... [flags]
```

## Options

```
      --config-file string                    Use the configuration values in the specified file rather than detecting the file name
  -d, --debug                                 Print detailed debugging output during resource operations
      --diff                                  Display operation as a rich diff showing the overall change
  -f, --file string                           The path to a JSON-encoded file containing a list of resources to import
      --from string                           Invoke a converter to import the resources
      --generate-code                         Generate resource declaration code for the imported resources (default true)
      --generate-resources string             When used with --from, always write a JSON-encoded file containing a list of importable resources discovered by conversion to the specified path
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

###### Auto generated by spf13/cobra on 10-Feb-2026
