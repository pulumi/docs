---
title: "pulumi stack change-secrets-provider"
aliases:
  - /docs/reference/cli/pulumi_stack_change-secrets-provider/
---



Change the secrets provider for a stack

## Synopsis

Change the secrets provider for a stack. Valid secret providers types are `default`, `passphrase`, `awskms`, `azurekeyvault`, `gcpkms`, `hashivault`.

To change to using the Pulumi Default Secrets Provider, use the following:

pulumi stack change-secrets-provider default

To change the stack to use a cloud secrets backend, use one of the following:

* `pulumi stack change-secrets-provider "awskms://alias/ExampleAlias?region=us-east-1"`
* `pulumi stack change-secrets-provider "awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1"`
* `pulumi stack change-secrets-provider "azurekeyvault://mykeyvaultname.vault.azure.net/keys/mykeyname"`
* `pulumi stack change-secrets-provider "gcpkms://projects/<p>/locations/<l>/keyRings/<r>/cryptoKeys/<k>"`
* `pulumi stack change-secrets-provider "hashivault://mykey"`

```
pulumi stack change-secrets-provider <new-secrets-provider> [flags]
```

## Options

```
  -h, --help           help for change-secrets-provider
  -s, --stack string   The name of the stack to operate on. Defaults to the current stack
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
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                  Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## SEE ALSO

* [pulumi stack](/docs/iac/cli/commands/pulumi_stack/)	 - Manage stacks and view stack state

###### Auto generated by spf13/cobra on 31-Jul-2025
