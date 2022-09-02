---
title: "pulumi watch"
---



Continuously update the resources in a stack

### Synopsis

[EXPERIMENTAL] Continuously update the resources in a stack.

This command watches the working directory or specified paths for the current project and updates
the active stack whenever the project changes.  In parallel, logs are collected for all resources
in the stack and displayed along with update progress.

The program to watch is loaded from the project in the current directory by default. Use the `-C` or
`--cwd` flag to use a different directory.

```
pulumi watch [flags]
```

### Options

```
  -c, --config stringArray           Config to use during the update
      --config-file string           Use the configuration values in the specified file rather than detecting the file name
      --config-path                  Config keys contain a path to a property in a map or list to set
  -d, --debug                        Print detailed debugging output during resource operations
  -h, --help                         help for watch
  -m, --message string               Optional message to associate with each update operation
  -p, --parallel int                 Allow P resource operations to run in parallel at once (1 for no parallelism). Defaults to unbounded. (default 2147483647)
      --path stringArray             Specify one or more relative or absolute paths that need to be watched. A path can point to a folder or a file. Defaults to working directory
      --policy-pack strings          Run one or more policy packs as part of each update
      --policy-pack-config strings   Path to JSON file containing the config for the policy pack of the corresponding "--policy-pack" flag
  -r, --refresh                      Refresh the state of the stack's resources before each update
      --secrets-provider string      The type of the provider that should be used to encrypt and decrypt secrets (possible choices: default, passphrase, awskms, azurekeyvault, gcpkms, hashivault). Only used when creating a new stack from an existing template (default "default")
      --show-config                  Show configuration keys and variables
      --show-replacement-steps       Show detailed resource replacement creates and deletes instead of a single step
      --show-sames                   Show resources that don't need be updated because they haven't changed, alongside those that do
  -s, --stack string                 The name of the stack to operate on. Defaults to the current stack
```

### Options inherited from parent commands

```
      --alsologtostderr                             log to standard error as well as files
      --color string                                Colorize output. Choices are: always, never, raw, auto (default "auto")
  -C, --cwd string                                  Run pulumi as if it had been started in another directory
      --dirs regexFlag                              optional list of regexes to use to select integration tests to run
      --disable-integrity-checking                  Disable integrity checking of checkpoint files
  -e, --emoji                                       Enable emojis in the output
      --list-dirs                                   list available integration tests without running them
      --log_backtrace_at traceLocation              when logging hits line file:N, emit a stack trace (default :0)
      --log_dir string                              If non-empty, write log files in this directory
      --logflow                                     Flow log settings to child processes (like plugins)
      --logtostderr                                 Log to stderr instead of to files
      --non-interactive                             Disable interactive mode for all commands
      --profiling string                            Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --sdk.no-checks                               when set, skips all post-SDK-generation checks
      --stderrthreshold severity                    logs at or above this threshold go to stderr (default 2)
      --test.bench regexp                           run only benchmarks matching regexp
      --test.benchmem                               print memory allocations for benchmarks
      --test.benchtime d                            run each benchmark for duration d (default 1s)
      --test.blockprofile file                      write a goroutine blocking profile to file
      --test.blockprofilerate rate                  set blocking profile rate (see runtime.SetBlockProfileRate) (default 1)
      --test.count n                                run tests and benchmarks n times (default 1)
      --test.coverprofile file                      write a coverage profile to file
      --test.cpu list                               comma-separated list of cpu counts to run each test with
      --test.cpuprofile file                        write a cpu profile to file
      --test.failfast                               do not start new tests after the first test failure
      --test.fuzz regexp                            run the fuzz test matching regexp
      --test.fuzzcachedir string                    directory where interesting fuzzing inputs are stored (for use only by cmd/go)
      --test.fuzzminimizetime durationOrCountFlag   time to spend minimizing a value after finding a failing input (default 1m0s)
      --test.fuzztime durationOrCountFlag           time to spend fuzzing; default is to run indefinitely (default 0s)
      --test.fuzzworker                             coordinate with the parent process to fuzz random values (for use only by cmd/go)
      --test.list regexp                            list tests, examples, and benchmarks matching regexp then exit
      --test.memprofile file                        write an allocation profile to file
      --test.memprofilerate rate                    set memory allocation profiling rate (see runtime.MemProfileRate)
      --test.mutexprofile string                    write a mutex contention profile to the named file after execution
      --test.mutexprofilefraction int               if >= 0, calls runtime.SetMutexProfileFraction() (default 1)
      --test.outputdir dir                          write profiles to dir
      --test.paniconexit0                           panic on call to os.Exit(0)
      --test.parallel n                             run at most n tests in parallel (default 2)
      --test.run regexp                             run only tests and examples matching regexp
      --test.short                                  run smaller test suite to save time
      --test.shuffle string                         randomize the execution order of tests and benchmarks (default "off")
      --test.testlogfile file                       write test action log to file (for use only by cmd/go)
      --test.timeout d                              panic test binary after duration d (default 0, timeout disabled) (default 0s)
      --test.trace file                             write an execution trace to file
      --test.v                                      verbose: print additional output
      --tracing file:                               Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                                 Enable verbose logging (e.g., v=3); anything >3 is very verbose
      --vmodule moduleSpec                          comma-separated list of pattern=N settings for file-filtered logging
```

### SEE ALSO

* [pulumi](/docs/reference/cli/pulumi/)	 - Pulumi command line

###### Auto generated by spf13/cobra on 2-Sep-2022
