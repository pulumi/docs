---
title: "pulumi import"
---



Import resources into an existing stack

### Synopsis

Import resources into an existing stack.

Resources that are not managed by Pulumi can be imported into a Pulumi stack
using this command. A definition for each resource will be printed to stdout
in the language used by the project associated with the stack; these definitions
should be added to the Pulumi program. The resources are protected from deletion
by default.

Should you want to import your resource(s) without protection, you can pass
`--protect=false` as an argument to the command. This will leave all resources unprotected.

A single resource may be specified in the command line arguments or a set of
resources may be specified by a JSON file. This file must contain an object
of the following form:

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
                "properties": ["optional-property-names"],
            },
            ...
            {
                ...
            }
        ]
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
Each resource may specify which input properties to import with;
If a resource does not specify any properties the default behaviour is to
import using all required properties.


```
pulumi import [type] [name] [id] [flags]
```

### Options

```
      --config-file string                    Use the configuration values in the specified file rather than detecting the file name
  -d, --debug                                 Print detailed debugging output during resource operations
      --diff                                  Display operation as a rich diff showing the overall change
  -f, --file string                           The path to a JSON-encoded file containing a list of resources to import
  -h, --help                                  help for import
  -m, --message string                        Optional message to associate with the update operation
  -o, --out string                            The path to the file that will contain the generated resource declarations
  -p, --parallel int                          Allow P resource operations to run in parallel at once (1 for no parallelism). Defaults to unbounded. (default 2147483647)
      --parent string                         The name and URN of the parent resource in the format name=urn, where name is the variable name of the parent resource
      --properties strings                    The property names to use for the import in the format name1,name2
      --protect                               Allow resources to be imported with protection from deletion enabled (default true)
      --provider string                       The name and URN of the provider to use for the import in the format name=urn, where name is the variable name for the provider resource
      --skip-preview                          Do not perform a preview before performing the refresh
  -s, --stack string                          The name of the stack to operate on. Defaults to the current stack
      --suppress-outputs                      Suppress display of stack outputs (in case they contain sensitive values)
      --suppress-permalink string[="false"]   Suppress display of the state permalink
  -y, --yes                                   Automatically approve and perform the refresh after previewing it
```

### Options inherited from parent commands

```
      --alsologtostderr                  log to standard error as well as files
      --color string                     Colorize output. Choices are: always, never, raw, auto (default "auto")
  -C, --cwd string                       Run pulumi as if it had been started in another directory
      --disable-integrity-checking       Disable integrity checking of checkpoint files
  -e, --emoji                            Enable emojis in the output
      --log_backtrace_at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log_dir string                   If non-empty, write log files in this directory
      --logflow                          Flow log settings to child processes (like plugins)
      --logtostderr                      Log to stderr instead of to files
      --non-interactive                  Disable interactive mode for all commands
      --profiling string                 Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
      --test.bench regexp                run only benchmarks matching regexp
      --test.benchmem                    print memory allocations for benchmarks
      --test.benchtime d                 run each benchmark for duration d (default 1s)
      --test.blockprofile file           write a goroutine blocking profile to file
      --test.blockprofilerate rate       set blocking profile rate (see runtime.SetBlockProfileRate) (default 1)
      --test.count n                     run tests and benchmarks n times (default 1)
      --test.coverprofile file           write a coverage profile to file
      --test.cpu list                    comma-separated list of cpu counts to run each test with
      --test.cpuprofile file             write a cpu profile to file
      --test.failfast                    do not start new tests after the first test failure
      --test.list regexp                 list tests, examples, and benchmarks matching regexp then exit
      --test.memprofile file             write an allocation profile to file
      --test.memprofilerate rate         set memory allocation profiling rate (see runtime.MemProfileRate)
      --test.mutexprofile string         write a mutex contention profile to the named file after execution
      --test.mutexprofilefraction int    if >= 0, calls runtime.SetMutexProfileFraction() (default 1)
      --test.outputdir dir               write profiles to dir
      --test.paniconexit0                panic on call to os.Exit(0)
      --test.parallel n                  run at most n tests in parallel (default 2)
      --test.run regexp                  run only tests and examples matching regexp
      --test.short                       run smaller test suite to save time
      --test.shuffle string              randomize the execution order of tests and benchmarks (default "off")
      --test.testlogfile file            write test action log to file (for use only by cmd/go)
      --test.timeout d                   panic test binary after duration d (default 0, timeout disabled) (default 0s)
      --test.trace file                  write an execution trace to file
      --test.v                           verbose: print additional output
      --tracing file:                    Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                      Enable verbose logging (e.g., v=3); anything >3 is very verbose
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging
```

### SEE ALSO

* [pulumi](/docs/reference/cli/pulumi/)	 - Pulumi command line

###### Auto generated by spf13/cobra on 24-Feb-2022
