---
title: "pulumi stack"
---



Manage stacks

### Synopsis

Manage stacks

A stack is a named update target, and a single project may have many of them.
Each stack has a configuration and update history associated with it, stored in
the workspace, in addition to a full checkpoint of the last known good update.


```
pulumi stack [flags]
```

### Options

```
  -h, --help           help for stack
  -i, --show-ids       Display each resource's provider-assigned unique ID
      --show-name      Display only the stack name
      --show-secrets   Display stack outputs which are marked as secret in plaintext
  -u, --show-urns      Display each resource's Pulumi-assigned globally unique URN
  -s, --stack string   The name of the stack to operate on. Defaults to the current stack
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
* [pulumi stack change-secrets-provider](/docs/reference/cli/pulumi_stack_change-secrets-provider/)	 - Change the secrets provider for the current stack
* [pulumi stack export](/docs/reference/cli/pulumi_stack_export/)	 - Export a stack's deployment to standard out
* [pulumi stack graph](/docs/reference/cli/pulumi_stack_graph/)	 - Export a stack's dependency graph to a file
* [pulumi stack history](/docs/reference/cli/pulumi_stack_history/)	 - [PREVIEW] Display history for a stack
* [pulumi stack import](/docs/reference/cli/pulumi_stack_import/)	 - Import a deployment from standard in into an existing stack
* [pulumi stack init](/docs/reference/cli/pulumi_stack_init/)	 - Create an empty stack with the given name, ready for updates
* [pulumi stack ls](/docs/reference/cli/pulumi_stack_ls/)	 - List stacks
* [pulumi stack output](/docs/reference/cli/pulumi_stack_output/)	 - Show a stack's output properties
* [pulumi stack rename](/docs/reference/cli/pulumi_stack_rename/)	 - Rename an existing stack
* [pulumi stack rm](/docs/reference/cli/pulumi_stack_rm/)	 - Remove a stack and its configuration
* [pulumi stack select](/docs/reference/cli/pulumi_stack_select/)	 - Switch the current workspace to the given stack
* [pulumi stack tag](/docs/reference/cli/pulumi_stack_tag/)	 - Manage stack tags

###### Auto generated by spf13/cobra on 24-Feb-2022
