---
title: "pulumi new"
---



Create a new Pulumi project

### Synopsis

Create a new Pulumi project and stack from a template.

To create a project from a specific template, pass the template name (such as `aws-typescript`
or `azure-python`).  If no template name is provided, a list of suggested templates will be presented
which can be selected interactively.

By default, a stack created using the pulumi.com backend will use the pulumi.com secrets
provider and a stack created using the local or cloud object storage backend will use the
`passphrase` secrets provider.  A different secrets provider can be selected by passing the
`--secrets-provider` flag.

To use the `passphrase` secrets provider with the pulumi.com backend, use:
* `pulumi new --secrets-provider=passphrase`

To use a cloud secrets provider with any backend, use one of the following:
* `pulumi new --secrets-provider="awskms://alias/ExampleAlias?region=us-east-1"`
* `pulumi new --secrets-provider="awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1"`
* `pulumi new --secrets-provider="azurekeyvault://mykeyvaultname.vault.azure.net/keys/mykeyname"`
* `pulumi new --secrets-provider="gcpkms://projects/p/locations/l/keyRings/r/cryptoKeys/k"`
* `pulumi new --secrets-provider="hashivault://mykey"`

To create a project from a specific source control location, pass the url as follows e.g.
* `pulumi new https://gitlab.com/<user>/<repo>`
* `pulumi new https://bitbucket.org/<user>/<repo>`
* `pulumi new https://github.com/<user>/<repo>`

To create the project from a branch of a specific source control location, pass the url to the branch, e.g.
* `pulumi new https://gitlab.com/<user>/<repo>/tree/<branch>`
* `pulumi new https://bitbucket.org/<user>/<repo>/tree/<branch>`
* `pulumi new https://github.com/<user>/<repo>/tree/<branch>`


```
pulumi new [template|url] [flags]
```

### Options

```
  -c, --config stringArray        Config to save
      --config-path               Config keys contain a path to a property in a map or list to set
  -d, --description string        The project description; if not specified, a prompt will request it
      --dir string                The location to place the generated project; if not specified, the current directory is used
  -f, --force                     Forces content to be generated even if it would change existing files
  -g, --generate-only             Generate the project only; do not create a stack, save config, or install dependencies
  -h, --help                      help for new
  -n, --name string               The project name; if not specified, a prompt will request it
  -o, --offline                   Use locally cached templates without making any network requests
      --secrets-provider string   The type of the provider that should be used to encrypt and decrypt secrets (possible choices: default, passphrase, awskms, azurekeyvault, gcpkms, hashivault) (default "default")
  -s, --stack string              The stack name; either an existing stack or stack to create; if not specified, a prompt will request it
  -y, --yes                       Skip prompts and proceed with default values
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
