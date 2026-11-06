---
# This file is auto-generated from github.com/pulumi/pulumi/v3/pkg/cmd/pulumi/markdown
title: "pulumi policy exception new | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_policy_exception_new/
  - /docs/iac/cli/commands/pulumi_policy_exception_create/
  - /docs/reference/cli/pulumi_policy_exception_create/
meta_desc: "Reference for the pulumi policy exception new command: create a policy exception from a run's violations. Usage, flags, and examples for the Pulumi CLI."
---



[EXPERIMENTAL] Create a policy exception from a run's violations

## Synopsis

[EXPERIMENTAL] Create a policy exception from a run's violations.

Reads the policy violations of the stack's latest run, update or preview, so you don't have to
re-run it or copy URNs. In a terminal, you pick the violations to exempt and enter a reason.
--policy, --target and --level narrow the violations to pick from, and --file reads a whole
exception instead. Only mandatory violations are read unless --level says otherwise.

The exception belongs to the Policy Pack named as <policy-pack> or <org>/<policy-pack>; the
organization defaults to the stack's. It gets one entry per resource, listing the resource's
selected policies. Requesting the same exception again returns the existing one.

When the organization requires approval for policy exceptions, or --draft is passed, the
command creates a change request for the exception instead and submits it, with the reason as
its description. The exception is created once the change request is approved and applied.
With --expires-in, the exception is removed once it expires.

The command prints a link to the exception, or to its change request. --output json prints the
result, with the exception's ID, to stdout. --dry-run --output json prints the run's violations,
with their URNs, and the exception the command would create, without creating it.

For scripts and agents, pass --yes (or run without a terminal) to skip the picker: every
violation the run didn't already exempt is included. --reason is then required unless --file
has one, and so is the Policy Pack when the violations are from several. Check first with
--dry-run --output json, edit the JSON if needed, and create it with --file -.

```
pulumi policy exception new [policy-pack] [flags]
```

## Examples

```
  # Pick from the violations of the current stack's latest run
  pulumi policy exception new aws-security

  # Exempt one policy on every resource that violated it, without prompting
  pulumi policy exception new aws-security --policy required-tags --reason "Shared buckets (LOG-31)" --yes

  # Include advisory violations, from update 12 instead of the latest run
  pulumi policy exception new aws-security --update=12 --level mandatory --level advisory --dry-run

  # Preview the exception as JSON, then create it from the edited output
  pulumi policy exception new aws-security -s web/prod --dry-run --output json > exc.json
  pulumi policy exception new aws-security --file exc.json --yes

  # Expire it after 30 days; with an approval gate this opens a change request instead
  pulumi policy exception new aws-security -s web/prod --policy s3-no-public-read \
      --reason "LOG-31" --expires-in 30d --yes --output json

  # Request the exception in a change request, even if no approval is required
  pulumi policy exception new aws-security --policy required-tags --reason "LOG-31" --draft

  # See where violations are recorded, or the findings of a stack
  pulumi stack history events latest --event-type 9 --output json
  pulumi policy issue list
```

## Options

```
      --draft                       Request the exception in a change request, even if the organization doesn't require approval
      --dry-run                     Show the violations and the exception, without creating it
      --expires-in string           Expire the exception this long after it's created, in days (7d) or hours (12h); by default it never expires
      --file string                 Read the exception from this JSON or YAML file, or from stdin with -; its policyPack is the default
  -h, --help                        help for new
      --level stringArray           Only exempt violations of this enforcement level (mandatory, advisory, remediate or all); may be repeated (default [mandatory])
      --output string               Output format. Supported values are: default and json (default "default")
      --policy stringArray          Only exempt violations of this policy; may be repeated
      --preview string[="latest"]   Read the violations of a preview, as --preview=<id> (default: the latest)
      --reason string               Why it's safe to exempt the violations
  -s, --stack stringArray           The stack whose violations to read; may be repeated. Defaults to the current stack
      --target stringArray          Only exempt violations on this resource URN; may be repeated
      --update string[="latest"]    Read the violations of an update, as --update=<version> (default: the latest)
  -y, --yes                         Skip prompts and confirmation
```

## Options inherited from parent commands

```
      --color string                 Colorize output. Choices are: always, never, raw, auto (default "auto")
  -C, --cwd string                   Run pulumi as if it had been started in another directory
      --disable-integrity-checking   Disable integrity checking of checkpoint files
  -e, --emoji                        Enable emojis in the output
  -Q, --fully-qualify-stack-names    Show fully-qualified stack names
      --logflow                      Flow log settings to child processes (like plugins)
      --logtostderr                  Log to stderr instead of to files
      --memprofilerate int           Enable more precise (and expensive) memory allocation profiles by setting runtime.MemProfileRate
      --non-interactive              Disable interactive mode for all commands
      --otel-traces string           Export OpenTelemetry traces to the specified endpoint. Use file:// for local JSON files, grpc:// or https:// for remote collectors
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                  Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## SEE ALSO

* [pulumi policy exception](/docs/iac/cli/commands/pulumi_policy_exception/)	 - [EXPERIMENTAL] Manage policy exceptions

###### Auto generated by spf13/cobra on 6-Nov-2026
