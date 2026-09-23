---
# This file is auto-generated from github.com/pulumi/pulumi/v3/pkg/cmd/pulumi/markdown
title: "pulumi deployment settings edit | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_deployment_settings_edit/
  - /docs/iac/cli/commands/pulumi_deployment_settings_update/
  - /docs/reference/cli/pulumi_deployment_settings_update/
  - /docs/iac/cli/commands/pulumi_deployment_settings_modify/
  - /docs/reference/cli/pulumi_deployment_settings_modify/
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
    --vcs-provider github --repo acme/infra --branch main --folder stacks/prod \
    --preview-prs --push-to-deploy

  # Configure a GitLab source.
  pulumi deployment settings edit \
    --vcs-provider gitlab --repo acme/infra --branch main --push-to-deploy

  # Authenticate against a private git repository with an access token.
  pulumi deployment settings edit \
    --git-url https://git.acme.example/infra.git --git-auth-access-token "$GIT_TOKEN"

  # Authenticate against a private git repository with an SSH key.
  pulumi deployment settings edit \
    --git-url git@git.acme.example:acme/infra.git \
    --git-auth-ssh-private-key-path ~/.ssh/id_ed25519

  # Set environment variables (plaintext and encrypted).
  pulumi deployment settings edit --env LOG_LEVEL=info --secret-env API_KEY=s3cret

  # Remove an environment variable.
  pulumi deployment settings edit --remove-env STALE_VAR

  # Configure AWS OIDC.
  pulumi deployment settings edit \
    --oidc-aws-role-arn arn:aws:iam::123:role/pulumi-deploy \
    --oidc-aws-session-name pulumi-deploy --oidc-aws-duration 30m

  # Remove the AWS OIDC configuration entirely.
  pulumi deployment settings edit --remove-oidc-aws

  # Clear the agent pool back to the Pulumi-hosted default.
  pulumi deployment settings edit --runner-pool ""

  # Clear the pre-run command list.
  pulumi deployment settings edit --pre-run-command ""
```

## Options

```
      --branch string                              Source branch
      --cache                                      Cache dependencies between deployments
      --commit string                              Source commit hash
      --delete-after-destroy                       Delete the stack after a successful destroy
      --deploy-tags                                Run updates for pushed tags (cannot be enabled together with --push-to-deploy)
      --env stringArray                            Set a plaintext environment variable (repeatable, KEY=VALUE)
      --executor-image string                      Custom executor image; empty string clears it to the default image
      --executor-root-path string                  Executor root path; empty string clears it to the default (/)
      --folder string                              Path to the Pulumi.yaml folder within the source repo
      --git-auth-access-token string               Git source: personal access token (pass --remove-git-auth to remove stored credentials)
      --git-auth-password string                   Git source: basic auth password
      --git-auth-ssh-private-key string            Git source: PEM-encoded SSH private key, key material and not a path
      --git-auth-ssh-private-key-password string   Git source: password for the SSH private key
      --git-auth-ssh-private-key-path string       Git source: path to a PEM-encoded SSH private key file (mutually exclusive with --git-auth-ssh-private-key)
      --git-auth-username string                   Git source: basic auth username
      --git-url string                             Git source: full repository URL (mutually exclusive with --repo)
  -h, --help                                       help for edit
      --installation-id string                     Version control integration ID; only needed to choose between several integrations for the same provider. List them with: pulumi api ListAllVCSIntegrations -F orgName=<org>
      --oidc-aws-duration string                   AWS OIDC: assume-role session duration (e.g. 30m, 1h)
      --oidc-aws-policy-arn strings                AWS OIDC: replace the session policy ARN list (repeatable or comma-separated)
      --oidc-aws-role-arn string                   AWS OIDC: IAM role ARN to assume
      --oidc-aws-session-name string               AWS OIDC: assume-role session name
      --oidc-azure-client-id string                Azure OIDC: federated workload identity client ID
      --oidc-azure-subscription-id string          Azure OIDC: federated workload identity subscription ID
      --oidc-azure-tenant-id string                Azure OIDC: federated workload identity tenant ID
      --oidc-gcp-project-number string             GCP OIDC: numerical project number (e.g. 987654321)
      --oidc-gcp-provider-id string                GCP OIDC: identity provider ID within the workload pool
      --oidc-gcp-region string                     GCP OIDC: region
      --oidc-gcp-service-account string            GCP OIDC: service account email
      --oidc-gcp-token-lifetime string             GCP OIDC: lifetime of the temporary credentials (e.g. 30m, 1h)
      --oidc-gcp-workload-pool-id string           GCP OIDC: workload identity pool ID
      --output string                              Output format. Supported values are: default and json (default "default")
      --path-filter stringArray                    Replace the path filter list (repeatable; pass once per filter); empty string clears it
      --pr-template                                Use this stack as a template for PR review stacks
      --pre-run-command stringArray                Replace the pre-run command list (repeatable; pass once per command); empty string clears it
      --preview-prs                                Run previews for pull requests
      --push-to-deploy                             Run updates for pushed commits (cannot be enabled together with --deploy-tags)
      --remediate-if-drift-detected                Remediate the stack when a drift detection run finds drift
      --remove-all-env                             Remove every environment variable
      --remove-env strings                         Delete an environment variable by key (repeatable or comma-separated)
      --remove-git-auth                            Remove the stored git credentials, whichever authentication mode they use
      --remove-oidc-aws                            AWS OIDC: remove the entire configuration
      --remove-oidc-azure                          Azure OIDC: remove the entire configuration
      --remove-oidc-gcp                            GCP OIDC: remove the entire configuration
      --repo string                                Version control source: repository reference, e.g. organization/repository (mutually exclusive with --git-url)
      --review-stack-label stringArray             GitHub only: replace the labels that trigger a PR review stack (repeatable); empty string clears them
      --runner-pool string                         Deployment runner pool ID; empty string clears it to the Pulumi-hosted pool
      --secret-env stringArray                     Set an encrypted environment variable (repeatable, KEY=VALUE)
      --shell string                               Shell to use for pre-run commands
      --skip-install-deps                          Skip automatic dependency installation
      --skip-intermediate-deployments              Skip intermediate deployments
  -s, --stack string                               The name of the stack to operate on. Defaults to the current stack
      --tag-filter stringArray                     Replace the tag filter list (repeatable; pass once per filter); empty string clears it
      --template-source-url string                 Template source URL, e.g. registry://templates/source/acme/vpc; empty string clears it
      --vcs-provider string                        Version control provider: github, gitlab, azure_devops, bitbucket or custom
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

* [pulumi deployment settings](/docs/iac/cli/commands/pulumi_deployment_settings/)	 - Manage stack deployment settings

###### Auto generated by spf13/cobra on 23-Sep-2026
