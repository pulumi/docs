---
title: All Pulumi CLI flags are now supported as environment variables
date: 2025-11-21
meta_desc: "You can now configure all Pulumi CLI flags via environment variables, and use tools like direnv to define project-wide settings"
meta_image: meta.png
authors:
    - tom-harding
tags:
    - features
    - iac
    - release
    - cli

social:
    twitter: |
        All Pulumi CLI flags now support environment variables! Set any flag with PULUMI_OPTION_*. Combine with direnv to version-control your team's CLI configuration. Available in v3.208.0+
    linkedin: |
        Pulumi v3.208.0 adds environment variable support for all CLI flags.

        Key highlights:
        → Set any CLI flag as an environment variable using PULUMI_OPTION_* prefix
        → Version control your team's CLI defaults with direnv
        → You no longer need to repeat --verbose, --refresh, --target flags across commands
        → Command-line flags override env vars when you need flexibility

        This means your CLI configuration can live alongside your infrastructure code, consistent across your entire team.
---

With the release of [Pulumi v3.208.0](https://github.com/pulumi/pulumi/releases/tag/v3.208.0), all CLI flags can now be configured as environment variables. This addresses a common friction point of having to remember the same flags across multiple commands and of ensuring that your entire team uses consistent CLI options.

<!--more-->

## Use cases

An example use case might be that you want to always refresh state before operations, or re-run programs during refresh and destroy (using [`--run-program`](https://www.pulumi.com/blog/improved-refresh-destroy-experience/)). But remembering to add `--refresh` every time is tedious.

Another example is you're working on a specific subset of your infrastructure and need to pass the same `--target` or `--exclude` flags repeatedly across multiple operations.

You're working in a CI environment where you want to skip interactive prompts and previews. That means adding `--yes` and `--skip-preview` to every single command in your pipeline.

The usual workaround, if there is no env var already, is writing wrapper scripts or shell aliases, but these become another thing to maintain and share across your team.

## How it works

Any CLI flag can now be set as an environment variable. The naming convention is straightforward: prefix the flag name with `PULUMI_OPTION_`, and convert dashes to underscores.

For example:

```shell
export PULUMI_OPTION_REFRESH=true
```

Target specific resources without repeating flags:

```shell
export PULUMI_OPTION_TARGET=foo,bar
# Equivalent to: --target foo --target bar
```

This works for any flag the CLI accepts. The environment variable takes precedence if you don't explicitly pass the flag on the command line.

## Using with direnv for project-level defaults

This becomes particularly useful when combined with tools like [`direnv`](https://direnv.net/). You can define project-specific CLI defaults in a `.envrc` file at the root of your project:

```shell
# Enable very verbose logging for debugging purposes
export PULUMI_OPTION_VERBOSE=3

# Always refresh before any Pulumi operation
export PULUMI_OPTION_REFRESH=true

# Skip previews and any dialogs or user prompts
export PULUMI_OPTION_YES=true
export PULUMI_OPTION_SKIP_PREVIEW=true
```

Now, running `direnv allow .` in this directory means that, whenever we access this directory, these options will be automatically applied to all commands that we run until we leave the directory\!

## Wrapping up

We hope that this change makes Pulumi much easier to configure across a range of different environments, and gives you another tool for managing operation defaults across your team. Thanks for reading, and feel free to share any feedback on [GitHub](https://github.com/pulumi/pulumi), [X](https://twitter.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).
