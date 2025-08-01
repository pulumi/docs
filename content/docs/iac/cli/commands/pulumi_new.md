---
title: "pulumi new"
aliases:
  - /docs/reference/cli/pulumi_new/
---



Create a new Pulumi project

## Synopsis

Create a new Pulumi project and stack from a template.

To create a project from a specific template, pass the template name (such as `aws-typescript`
or `azure-python`). If no template name is provided, a list of suggested templates will be presented
which can be selected interactively.
For testing, a path to a local template may be passed instead (such as `~/templates/aws-typescript`)

By default, a stack created using the pulumi.com backend will use the pulumi.com secrets
provider and a stack created using the local or cloud object storage backend will use the
`passphrase` secrets provider.  A different secrets provider can be selected by passing the
`--secrets-provider` flag.

To use the `passphrase` secrets provider with the pulumi.com backend, use:
* `pulumi new --secrets-provider=passphrase`

To use a cloud secrets provider with any backend, use one of the following:
* `pulumi new --secrets-provider="awskms://alias/ExampleAlias?region=us-east-1"`
* `pulumi new --secrets-provider="awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1"`
* `pulumi new --secrets-provider="azurekeyvault://mykeyvaultname.vault.azure.net/keys/mykeyname"`
* `pulumi new --secrets-provider="gcpkms://projects/p/locations/l/keyRings/r/cryptoKeys/k"`
* `pulumi new --secrets-provider="hashivault://mykey"`

To create a project from a specific source control location, pass the url as follows e.g.
* `pulumi new https://gitlab.com/<user>/<repo>`
* `pulumi new https://bitbucket.org/<user>/<repo>`
* `pulumi new https://github.com/<user>/<repo>`

  Note: If the URL doesn't follow the usual scheme of the given host (e.g. for GitLab subprojects)
        you can append `.git` to the repository to disambiguate and point to the correct repository.
        For example `https://gitlab.com/<project>/<subproject>/<repository>.git`.

To create the project from a branch of a specific source control location, pass the url to the branch, e.g.
* `pulumi new https://gitlab.com/<user>/<repo>/tree/<branch>`
* `pulumi new https://bitbucket.org/<user>/<repo>/tree/<branch>`
* `pulumi new https://github.com/<user>/<repo>/tree/<branch>`

To use a private repository as a template source, provide an HTTPS or SSH URL with relevant credentials.
Ensure your SSH agent has the correct identity (ssh-add) or you may be prompted for your key's passphrase.
* `pulumi new git@github.com:<user>/<private-repo>`
* `pulumi new https://<user>:<password>@<hostname>/<project>/<repo>`
* `pulumi new <user>@<hostname>:<project>/<repo>`
* `PULUMI_GITSSH_PASSPHRASE=<passphrase> pulumi new ssh://<user>@<hostname>/<project>/<repo>`
To create a project using Pulumi AI, either select `ai` from the first selection, or provide any of the following:
* `pulumi new --ai "<prompt>"`
* `pulumi new --language <language>`
* `pulumi new --ai "<prompt>" --language <language>`
Any missing but required information will be prompted for.


```
pulumi new [template|url] [flags]
```

## Options

```
      --ai string                   Prompt to use for Pulumi AI
  -c, --config stringArray          Config to save
      --config-path                 Config keys contain a path to a property in a map or list to set
  -d, --description string          The project description; if not specified, a prompt will request it
      --dir string                  The location to place the generated project; if not specified, the current directory is used
  -f, --force                       Forces content to be generated even if it would change existing files
  -g, --generate-only               Generate the project only; do not create a stack, save config, or install dependencies
  -h, --help                        help for new
      --language pulumiAILanguage   Language to use for Pulumi AI (must be one of TypeScript, JavaScript, Python, Go, C#, Java, or YAML)
  -l, --list-templates              List locally installed templates and exit
  -n, --name string                 The project name; if not specified, a prompt will request it
  -o, --offline                     Use locally cached templates without making any network requests
      --runtime-options strings     Additional options for the language runtime (format: key1=value1,key2=value2)
      --secrets-provider string     The type of the provider that should be used to encrypt and decrypt secrets (possible choices: default, passphrase, awskms, azurekeyvault, gcpkms, hashivault) (default "default")
  -s, --stack string                The stack name; either an existing stack or stack to create; if not specified, a prompt will request it
  -t, --template-mode               Run in template mode, which will skip prompting for AI or Template functionality
  -y, --yes                         Skip prompts and proceed with default values
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

* [pulumi](/docs/iac/cli/commands/pulumi/)	 - Pulumi command line

###### Auto generated by spf13/cobra on 31-Jul-2025
