---
# This file is auto-generated from github.com/pulumi/pulumi/v3/pkg/cmd/pulumi/markdown
title: "pulumi policy group new | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_policy_group_new/
  - /docs/iac/cli/commands/pulumi_policy_group_create/
  - /docs/reference/cli/pulumi_policy_group_create/
  - /docs/iac/cli/commands/pulumi_policy_group_setup/
  - /docs/reference/cli/pulumi_policy_group_setup/
meta_desc: "Reference for the pulumi policy group new command: create a new Policy Group. Usage, flags, and examples for the Pulumi CLI."
---



[EXPERIMENTAL] Create a new Policy Group

## Synopsis

[EXPERIMENTAL] Create a new Policy Group.

Creates a new Policy Group in the given organization. Policy Groups
define which Policy Packs are enforced on which stacks or cloud
accounts, with configurable enforcement levels per pack.

When run interactively, prompts for required values that aren't
provided via flags. Pass --yes to skip prompts; --mode is then required.

Match rules (preview; requires the tag-based policy groups feature):

--stack-rule and --account-rule set a rule over stack tags or Insights
account tags. Stacks or accounts whose tags satisfy the rule are members
of the group alongside those added individually. --account-rule is only
allowed on audit groups. Setting a rule replaces the group's current rule,
and setting it to '' removes it.

A non-empty value is one of:
  - Tag conditions separated by commas, all of which must hold:
      key=value    the tag is set to value
      key!=value   the tag is not set to value (also true when the tag is absent)
      key          the tag exists
      !key         the tag does not exist
    Separate alternatives with " OR " to match entities that satisfy any
    of them, as in 'env=prod,region=us-west-2 OR team'. This is the syntax
    `pulumi policy group get` prints.
  - A JSON PermissionBooleanExpression, as returned in the stackMatchRule
    and accountMatchRule fields of `pulumi policy group get --output json`.

Use JSON when a tag key or value contains ',', '=' or the word "or", or a
key starts or ends with '!' or starts with '{'.

```
pulumi policy group new <name> [flags]
```

## Examples

```
  # Create a Policy Group interactively
  pulumi policy group new prod-policies

  # Create a preventative Policy Group non-interactively
  pulumi policy group new prod-policies --mode preventative --yes

  # Create an audit Policy Group
  pulumi policy group new compliance --mode audit --yes

  # Create a preventative group that holds every stack tagged env=prod
  pulumi policy group new prod-policies --mode preventative \
    --stack-rule env=prod --yes

  # Create an audit group for prod accounts not owned by the sandbox team
  pulumi policy group new prod-accounts --mode audit \
    --account-rule 'env=prod,team!=sandbox' --yes

  # Create a group whose stack rule is read from a JSON file
  pulumi policy group new tagged --mode audit --stack-rule "$(cat rule.json)" --yes

  # Emit JSON
  pulumi policy group new prod-policies --mode preventative \
    --yes --output json
```

## Options

```
      --account-rule string    Insights account match rule, in the same syntax as --stack-rule. Audit groups only
      --agent-pool-id string   Agent pool ID for policy evaluation (optional)
  -h, --help                   help for new
      --mode string            The enforcement mode: audit or preventative
      --org string             The organization to create the Policy Group in
      --output string          Output format. Supported values are: default and json (default "default")
      --stack-rule string      Stack match rule: tag conditions such as 'env=prod,team!=web OR owner', or a JSON expression
  -y, --yes                    Skip prompts; --mode is then required
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

* [pulumi policy group](/docs/iac/cli/commands/pulumi_policy_group/)	 - Manage policy groups

###### Auto generated by spf13/cobra on 12-Nov-2026
