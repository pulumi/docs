---
title: "pulumi login"
---



Log in to the Pulumi service

### Synopsis

Log in to the Pulumi service.

The service manages your stack's state reliably. Simply run

    $ pulumi login

and this command will prompt you for an access token, including a way to launch your web browser to
easily obtain one. You can script by using `PULUMI_ACCESS_TOKEN` environment variable.

By default, this will log in to the managed Pulumi service backend.
If you prefer to log in to a self-hosted Pulumi service backend, specify a URL. For example, run

    $ pulumi login https://api.pulumi.acmecorp.com

to log in to a self-hosted Pulumi service running at the api.pulumi.acmecorp.com domain.

For `https://` URLs, the CLI will speak REST to a service that manages state and concurrency control.
You can specify a default org to use when logging into the Pulumi service backend or a self-hosted Pulumi service.

[PREVIEW] If you prefer to operate Pulumi independently of a service, and entirely local to your computer,
pass `file://<path>`, where `<path>` will be where state checkpoints will be stored. For instance,

    $ pulumi login file://~

will store your state information on your computer underneath `~/.pulumi`. It is then up to you to
manage this state, including backing it up, using it in a team environment, and so on.

As a shortcut, you may pass --local to use your home directory (this is an alias for `file://~`):

    $ pulumi login --local

[PREVIEW] Additionally, you may leverage supported object storage backends from one of the cloud providers to manage the state independent of the service. For instance,

AWS S3:

    $ pulumi login s3://my-pulumi-state-bucket

GCP GCS:

    $ pulumi login gs://my-pulumi-state-bucket

Azure Blob:

    $ pulumi login azblob://my-pulumi-state-bucket


```
pulumi login [<url>] [flags]
```

### Options

```
  -c, --cloud-url string     A cloud URL to log in to
      --default-org string   A default org to associate with the login. Please note, currently, only the managed and self-hosted backends support organizations
  -h, --help                 help for login
  -l, --local                Use Pulumi in local-only mode
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
