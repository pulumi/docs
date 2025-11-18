---
title: Controlling the CLI through environment variables
meta_desc: "You can now configure all Pulumi CLI flags via environment variables, and use tools like direnv to define project-wide settings"
authors:
    - tom-harding
tags:
    - features
    - iac
    - release
    - cli
---

With the release of Pulumi v3.208.0, we have released a small but surprisingly powerful change to the CLI: all CLI flags can now be configured as environment variables\!

## The problem

There are a few situations in which this could be helpful:

* Perhaps we have a particular [policy pack](https://www.pulumi.com/docs/insights/policy/) that we want to run in the given environment \- maybe this is for CI, or a specific deployment configuration. We currently have to remember to add `--policy-pack pulumi-best-practices-aws` for all the commands we want to run.  
    
* For performance reasons, Pulumi does not refresh its understanding of the state of your application before performing operations, and does not re-compute resource registrations during `refresh` and `destroy`. If we want to override this, we have to add `--refresh` [`--run-program`](https://www.pulumi.com/blog/improved-refresh-destroy-experience/) to all operations to ensure that we are definitely in sync.

* We might want to perform a set of operations on a specific subset of our infrastructure. Right now, we need to pass the same `--target` or `--exclude` sets to every command we run.

## The environment variable interface

With this new update, all flags can now be provided as environment variables. These variables’ names follow a pattern: we prefix the flag name with `PULUMI_OPTION_` and dashes become underscores. To return to our above examples:

* Exporting `PULUMI_OPTION_POLICY_PACK=pulumi-best-practices-aws` before running your commands will ensure that the policy pack is always included.  
     
* We can enable refreshing before all operations simply by exporting `PULUMI_OPTION_REFRESH=true` in our environment.

* If we only want to focus on a particular subset, we can recreate a repeated list of arguments like `--target foo --target bar` with `PULUMI_OPTION_TARGET=foo,bar` to limit our operations to only those targets that we have specified.

## Configuring project defaults

Having this interface means that we can use other tools like [`direnv`](https://direnv.net/) to write files to configure project-level defaults. For example, we can add the following `.envrc` to the root of our project:

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
