---
title: "pulumi refresh"
---



Refresh the resources in a stack

### Synopsis

Refresh the resources in a stack.

This command compares the current stack's resource state with the state known to exist in
the actual cloud provider. Any such changes are adopted into the current stack. Note that if
the program text isn't updated accordingly, subsequent updates may still appear to be out of
synch with respect to the cloud provider's source of truth.

The program to run is loaded from the project in the current directory. Use the `-C` or
`--cwd` flag to use a different directory.

```
pulumi refresh [flags]
```

### Options

```
      --config-file string                    Use the configuration values in the specified file rather than detecting the file name
  -d, --debug                                 Print detailed debugging output during resource operations
      --diff                                  Display operation as a rich diff showing the overall change
      --expect-no-changes                     Return an error if any changes occur during this update
  -h, --help                                  help for refresh
  -j, --json                                  Serialize the refresh diffs, operations, and overall output as JSON
  -m, --message string                        Optional message to associate with the update operation
  -p, --parallel int                          Allow P resource operations to run in parallel at once (1 for no parallelism). Defaults to unbounded. (default 2147483647)
      --show-replacement-steps                Show detailed resource replacement creates and deletes instead of a single step
      --show-sames                            Show resources that needn't be updated because they haven't changed, alongside those that do
  -f, --skip-preview                          Do not perform a preview before performing the refresh
  -s, --stack string                          The name of the stack to operate on. Defaults to the current stack
      --suppress-outputs                      Suppress display of stack outputs (in case they contain sensitive values)
      --suppress-permalink string[="false"]   Suppress display of the state permalink
  -t, --target stringArray                    Specify a single resource URN to refresh. Multiple resource can be specified using: --target urn1 --target urn2
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
