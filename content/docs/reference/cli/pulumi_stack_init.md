---
title: "pulumi stack init"
---



Create an empty stack with the given name, ready for updates

### Synopsis

Create an empty stack with the given name, ready for updates

This command creates an empty stack with the given name.  It has no resources,
but afterwards it can become the target of a deployment using the `update` command.

To create a stack in an organization when logged in to the Pulumi service,
prefix the stack name with the organization name and a slash (e.g. 'acmecorp/dev')

By default, a stack created using the pulumi.com backend will use the pulumi.com secrets
provider and a stack created using the local or cloud object storage backend will use the
`passphrase` secrets provider.  A different secrets provider can be selected by passing the
`--secrets-provider` flag.

To use the `passphrase` secrets provider with the pulumi.com backend, use:

* `pulumi stack init --secrets-provider=passphrase`

To use a cloud secrets provider with any backend, use one of the following:

* `pulumi stack init --secrets-provider="awskms://alias/ExampleAlias?region=us-east-1"`
* `pulumi stack init --secrets-provider="awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1"`
* `pulumi stack init --secrets-provider="azurekeyvault://mykeyvaultname.vault.azure.net/keys/mykeyname"`
* `pulumi stack init --secrets-provider="gcpkms://projects/<p>/locations/<l>/keyRings/<r>/cryptoKeys/<k>"`
* `pulumi stack init --secrets-provider="hashivault://mykey"
`
A stack can be created based on the configuration of an existing stack by passing the
`--copy-config-from` flag.
* `pulumi stack init --copy-config-from dev`

```
pulumi stack init [<org-name>/]<stack-name> [flags]
```

### Options

```
      --copy-config-from string   The name of the stack to copy existing config from
  -h, --help                      help for init
      --secrets-provider string   The type of the provider that should be used to encrypt and decrypt secrets
                                  (possible choices: default, passphrase, awskms, azurekeyvault, gcpkms, hashivault) (default "default")
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
  -s, --stack string                     The name of the stack to operate on. Defaults to the current stack
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

* [pulumi stack](/docs/reference/cli/pulumi_stack/)	 - Manage stacks

###### Auto generated by spf13/cobra on 24-Feb-2022
