---
# This file is auto-generated from github.com/pulumi/pulumi/v3/pkg/cmd/pulumi/markdown
title: "pulumi deployment settings edit | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_deployment_settings_edit/
meta_desc: "Learn about the pulumi deployment settings edit command."
---



[EXPERIMENTAL] Create or update deployment settings for a stack

## Synopsis

[EXPERIMENTAL] Create or update deployment settings for a stack.

```
pulumi deployment settings edit [flags]
```

## Examples

```
  # Switch the deployment source branch.
  pulumi deployment settings edit --branch feature-x

  # Configure a GitHub source.
  pulumi deployment settings edit \
    --github-repo acme/infra --branch main --folder stacks/prod \
    --preview-prs --push-to-deploy

  # Set environment variables (plaintext and encrypted).
  pulumi deployment settings edit --env LOG_LEVEL=info --secret-env API_KEY=s3cret

  # Remove an environment variable.
  pulumi deployment settings edit --remove-env STALE_VAR

  # Configure AWS OIDC.
  pulumi deployment settings edit \
    --oidc-aws-role-arn arn:aws:iam::123:role/pulumi-deploy \
    --oidc-aws-session-name pulumi-deploy --oidc-aws-duration 30m

  # Remove the AWS OIDC configuration entirely.
  pulumi deployment settings edit --oidc-aws-clear

  # Clear the agent pool back to the Pulumi-hosted default.
  pulumi deployment settings edit --runner-pool ""
```

## Options

```
      --branch string                       Source branch
      --commit string                       Source commit hash
      --delete-after-destroy                Delete the stack after a successful destroy
      --env stringArray                     Set a plaintext environment variable (repeatable, KEY=VALUE)
      --executor-image string               Custom executor image; empty string clears it to the default image
      --executor-root-path string           Executor root path; empty string clears it to the default (/)
      --folder string                       Path to the Pulumi.yaml folder within the source repo
      --git-url string                      Git source: full repository URL (mutually exclusive with --github-repo)
      --github-repo string                  GitHub source: organization/repository (mutually exclusive with --git-url)
  -h, --help                                help for edit
      --oidc-aws-clear                      Remove the entire AWS OIDC configuration
      --oidc-aws-duration string            AWS OIDC: assume-role session duration (e.g. 30m, 1h)
      --oidc-aws-policy-arn strings         AWS OIDC: replace the session policy ARN list (repeatable, comma-separated)
      --oidc-aws-role-arn string            AWS OIDC: IAM role ARN to assume
      --oidc-aws-session-name string        AWS OIDC: assume-role session name
      --oidc-azure-clear                    Remove the entire Azure OIDC configuration
      --oidc-azure-client-id string         Azure OIDC: federated workload identity client ID
      --oidc-azure-subscription-id string   Azure OIDC: federated workload identity subscription ID
      --oidc-azure-tenant-id string         Azure OIDC: federated workload identity tenant ID
      --oidc-gcp-clear                      Remove the entire GCP OIDC configuration
      --oidc-gcp-project-number string      GCP OIDC: numerical project number (e.g. 987654321)
      --oidc-gcp-provider-id string         GCP OIDC: identity provider ID within the workload pool
      --oidc-gcp-region string              GCP OIDC: region
      --oidc-gcp-service-account string     GCP OIDC: service account email
      --oidc-gcp-token-lifetime string      GCP OIDC: lifetime of the temporary credentials (e.g. 30m, 1h)
      --oidc-gcp-workload-pool-id string    GCP OIDC: workload identity pool ID
      --output string                       Output format. Supported values are: default and json (default "default")
      --path-filter strings                 GitHub: replace the path filter list (repeatable, comma-separated)
      --pr-template                         GitHub: use this stack as a template for PR review stacks
      --pre-run-command stringArray         Replace the pre-run command list (repeatable; pass once per command
      --preview-prs                         GitHub: run previews for pull requests
      --push-to-deploy                      GitHub: run updates for pushed commits
      --remove-env strings                  Delete an environment variable by key (repeatable, comma-separated)
      --runner-pool string                  Deployment runner pool ID; empty string clears it to the Pulumi-hosted pool
      --secret-env stringArray              Set an encrypted environment variable (repeatable, KEY=VALUE)
      --shell string                        Shell to use for pre-run commands
      --skip-install-deps                   Skip automatic dependency installation
      --skip-intermediate-deployments       Skip intermediate deployments
  -s, --stack string                        The name of the stack to operate on. Defaults to the current stack
```

## Options inherited from parent commands

```
      --color string                 Colorize output. Choices are: always, never, raw, auto (default "auto")
      --config-file string           Override the file name where the deployment settings are specified. Default is Pulumi.[stack].deploy.yaml
  -C, --cwd string                   Run pulumi as if it had been started in another directory
      --disable-integrity-checking   Disable integrity checking of checkpoint files
  -e, --emoji                        Enable emojis in the output
  -Q, --fully-qualify-stack-names    Show fully-qualified stack names
      --logflow                      Flow log settings to child processes (like plugins)
      --logtostderr                  Log to stderr instead of to files
      --memprofilerate int           Enable more precise (and expensive) memory allocation profiles by setting runtime.MemProfileRate
      --non-interactive              Disable interactive mode for all commands
      --otel-traces string           Export OpenTelemetry traces to the specified endpoint. Use file:// for local JSON files, grpc:// for remote collectors
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                  Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## SEE ALSO

* [pulumi deployment settings](/docs/iac/cli/commands/pulumi_deployment_settings/)	 - Manage stack deployment settings

###### Auto generated by spf13/cobra on 1-Jul-2026
