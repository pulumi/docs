---
title: "pulumi"
---



Pulumi command line

### Synopsis

Pulumi - Modern Infrastructure as Code

To begin working with Pulumi, run the `pulumi new` command:

    $ pulumi new

This will prompt you to create a new project for your cloud and language of choice.

The most common commands from there are:

    - pulumi up       : Deploy code and/or resource changes
    - pulumi stack    : Manage instances of your project
    - pulumi config   : Alter your stack's configuration or secrets
    - pulumi destroy  : Tear down your stack's resources entirely

For more information, please visit the project page: https://www.pulumi.com/docs/

### Options

```
      --alsologtostderr                  log to standard error as well as files
      --color string                     Colorize output. Choices are: always, never, raw, auto (default "auto")
  -C, --cwd string                       Run pulumi as if it had been started in another directory
      --disable-integrity-checking       Disable integrity checking of checkpoint files
  -e, --emoji                            Enable emojis in the output
  -h, --help                             help for pulumi
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

* [pulumi about](/docs/reference/cli/pulumi_about/)	 - Print information about the Pulumi environment.
* [pulumi cancel](/docs/reference/cli/pulumi_cancel/)	 - Cancel a stack's currently running update, if any
* [pulumi config](/docs/reference/cli/pulumi_config/)	 - Manage configuration
* [pulumi console](/docs/reference/cli/pulumi_console/)	 - Opens the current stack in the Pulumi Console
* [pulumi destroy](/docs/reference/cli/pulumi_destroy/)	 - Destroy an existing stack and its resources
* [pulumi import](/docs/reference/cli/pulumi_import/)	 - Import resources into an existing stack
* [pulumi login](/docs/reference/cli/pulumi_login/)	 - Log in to the Pulumi service
* [pulumi logout](/docs/reference/cli/pulumi_logout/)	 - Log out of the Pulumi service
* [pulumi logs](/docs/reference/cli/pulumi_logs/)	 - [PREVIEW] Show aggregated resource logs for a stack
* [pulumi new](/docs/reference/cli/pulumi_new/)	 - Create a new Pulumi project
* [pulumi org](/docs/reference/cli/pulumi_org/)	 - Manage Organization configuration
* [pulumi plugin](/docs/reference/cli/pulumi_plugin/)	 - Manage language and resource provider plugins
* [pulumi policy](/docs/reference/cli/pulumi_policy/)	 - Manage resource policies
* [pulumi preview](/docs/reference/cli/pulumi_preview/)	 - Show a preview of updates to a stack's resources
* [pulumi refresh](/docs/reference/cli/pulumi_refresh/)	 - Refresh the resources in a stack
* [pulumi schema](/docs/reference/cli/pulumi_schema/)	 - Analyze package schemas
* [pulumi stack](/docs/reference/cli/pulumi_stack/)	 - Manage stacks
* [pulumi state](/docs/reference/cli/pulumi_state/)	 - Edit the current stack's state
* [pulumi up](/docs/reference/cli/pulumi_up/)	 - Create or update the resources in a stack
* [pulumi version](/docs/reference/cli/pulumi_version/)	 - Print Pulumi's version number
* [pulumi watch](/docs/reference/cli/pulumi_watch/)	 - [PREVIEW] Continuously update the resources in a stack
* [pulumi whoami](/docs/reference/cli/pulumi_whoami/)	 - Display the current logged-in user

###### Auto generated by spf13/cobra on 24-Feb-2022
