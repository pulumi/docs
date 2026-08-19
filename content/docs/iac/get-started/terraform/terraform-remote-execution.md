---
title_tag: Remote Execution for Terraform and OpenTofu | Pulumi for Terraform Users
title: Remote Execution
h1: "Remote Execution"
meta_desc: Run Terraform and OpenTofu plans and applies remotely on Pulumi Cloud using managed infrastructure, ESC for credentials, and VCS-triggered automation.
weight: 10
menu:
    iac:
        name: Remote Execution
        parent: terraform-get-started
        weight: 10
        identifier: terraform-remote-execution

aliases:
---

Pulumi Cloud can run your Terraform and OpenTofu operations remotely. Instead of running `plan` and `apply` on your local machine, the Terraform or OpenTofu CLI uploads your configuration to Pulumi Cloud, which executes the operation in a managed container and streams the output back to your terminal in real time. Pulumi Cloud implements the Terraform Cloud remote execution protocol, so the CLI workflow you already know — `terraform plan`, `terraform apply`, saved plans — works unchanged.

Remote execution gives you:

- **Consistent environment** — every plan and apply runs in the same managed infrastructure, not on individual developer machines
- **Centralized credentials** — use [Pulumi ESC](/docs/esc/) for cloud provider credentials instead of configuring them on every developer's laptop
- **VCS automation** — pushes and pull requests trigger runs automatically through [deployment settings](/docs/deployments/concepts/settings/)
- **Run approvals** — VCS-triggered applies pause for confirmation before proceeding, with confirm and discard controls in the Pulumi Cloud console
- **Policy enforcement** — [preventative policies](/docs/insights/policy/) evaluate against the plan and block applies that violate policy
- **Team visibility** — run history, logs, and status are visible in the Pulumi Cloud console

## How it works

When you run `terraform plan` or `terraform apply` against a Pulumi Cloud stack with [remote execution enabled](#enable-remote-execution):

1. The CLI packages your local configuration files into a tarball and uploads them to Pulumi Cloud.
1. Pulumi Cloud creates a run and executes the operation using [OpenTofu](https://opentofu.org/) in a managed container.
1. Logs stream back to your terminal as the operation progresses.
1. State is stored directly in Pulumi Cloud.

For VCS-triggered runs, Pulumi Cloud fetches your configuration from the repository directly instead of receiving an upload from the CLI.

{{% notes "info" %}}
Pulumi Cloud uses OpenTofu as the execution engine for remote runs. You can use either the Terraform CLI or the OpenTofu CLI on your local machine — both communicate with Pulumi Cloud using the same protocol.
{{% /notes %}}

Terraform workspaces map to Pulumi Cloud [stacks](/docs/iac/concepts/stacks/). This page uses both terms depending on context — "workspace" when describing Terraform CLI behavior and "stack" when describing Pulumi Cloud concepts.

## Enable remote execution

Remote execution uses the same backend configuration as [Terraform state storage](/docs/iac/get-started/terraform/terraform-state-backend/) — both the `cloud` block and `backend "remote"` block work. If you have not set up a Pulumi Cloud backend yet, follow the [state storage setup steps](/docs/iac/get-started/terraform/terraform-state-backend/#2-update-your-backend-configuration) first.

New stacks created through the Terraform or OpenTofu CLI default to remote execution. For existing stacks, set the `terraform:execution-mode` [stack tag](/docs/iac/concepts/stacks/#stack-tags) to `remote` to enable it. See [Control execution mode](#control-execution-mode) for details.

## Run plans and applies

### Remote plan

{{< chooser tf-tool "terraform,opentofu" >}}

{{% choosable tf-tool terraform %}}

```bash
terraform plan
```

{{% /choosable %}}

{{% choosable tf-tool opentofu %}}

```bash
tofu plan
```

{{% /choosable %}}

{{< /chooser >}}

Your configuration is uploaded and the plan runs remotely. Output streams to your terminal as if it were running locally. Because the plan is speculative (no apply will follow), it does not block other operations on the same workspace.

### Remote apply

{{< chooser tf-tool "terraform,opentofu" >}}

{{% choosable tf-tool terraform %}}

```bash
terraform apply
```

{{% /choosable %}}

{{% choosable tf-tool opentofu %}}

```bash
tofu apply
```

{{% /choosable %}}

{{< /chooser >}}

The CLI uploads your configuration, runs a plan remotely, displays the proposed changes, and prompts for confirmation. After you confirm, the apply runs remotely and the updated state is stored in Pulumi Cloud.

To skip the confirmation prompt:

{{< chooser tf-tool "terraform,opentofu" >}}

{{% choosable tf-tool terraform %}}

```bash
terraform apply -auto-approve
```

{{% /choosable %}}

{{% choosable tf-tool opentofu %}}

```bash
tofu apply -auto-approve
```

{{% /choosable %}}

{{< /chooser >}}

### Saved plans

You can save a plan and apply it later — useful for review workflows where the plan and apply happen in separate steps:

{{< chooser tf-tool "terraform,opentofu" >}}

{{% choosable tf-tool terraform %}}

```bash
# Save a plan
terraform plan -out=tfplan

# Apply the saved plan (can be hours or days later)
terraform apply tfplan
```

{{% /choosable %}}

{{% choosable tf-tool opentofu %}}

```bash
# Save a plan
tofu plan -out=tfplan

# Apply the saved plan (can be hours or days later)
tofu apply tfplan
```

{{% /choosable %}}

{{< /chooser >}}

The saved plan file is a bookmark containing a run ID — the actual plan artifact is stored securely in Pulumi Cloud. You can save multiple plans to different files and they are independent of each other. When you apply a bookmark, Pulumi Cloud uses the original saved plan, guaranteeing that the apply matches exactly what you reviewed even if infrastructure drifted in the meantime. Saved plans expire after approximately one week.

### Destroy, refresh, and targeted operations

Remote execution supports the standard Terraform operation flags:

{{< chooser tf-tool "terraform,opentofu" >}}

{{% choosable tf-tool terraform %}}

```bash
# Destroy all resources
terraform apply -destroy

# Refresh-only (reconcile state with real infrastructure)
terraform apply -refresh-only

# Target specific resources
terraform plan -target=aws_instance.web

# Force replacement
terraform plan -replace=aws_instance.web
```

{{% /choosable %}}

{{% choosable tf-tool opentofu %}}

```bash
# Destroy all resources
tofu apply -destroy

# Refresh-only (reconcile state with real infrastructure)
tofu apply -refresh-only

# Target specific resources
tofu plan -target=aws_instance.web

# Force replacement
tofu plan -replace=aws_instance.web
```

{{% /choosable %}}

{{< /chooser >}}

### Run serialization

Non-speculative operations (applies, destroys) are serialized per workspace — only one can run at a time. If you start a new run while another is in progress, it is queued and starts automatically when the previous run completes. Speculative plans run concurrently and never block other operations.

## Provide credentials with ESC

Pulumi Cloud uses [Pulumi ESC](/docs/esc/) for environment configuration and credentials. When you create a Terraform stack through the CLI, Pulumi Cloud automatically provisions a linked ESC environment with the same name as the stack. You can see and edit this environment in the Pulumi Cloud console.

ESC environments can provide:

- **Static secrets** — API keys, database passwords, and other sensitive values
- **Dynamic cloud credentials** — AWS OIDC, Azure federated credentials, and GCP workload identity tokens that are resolved fresh for each run
- **Composition** — environments can import values from other environments

To configure credentials for remote execution, add them to the stack's linked ESC environment. For example, to provide AWS credentials via OIDC and pass Terraform input variables, use the `environmentVariables` block with the [`TF_VAR_<name>` convention](https://opentofu.org/docs/language/values/variables/#environment-variables):

```yaml
# ESC environment example
values:
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
    TF_VAR_region: us-west-2
    TF_VAR_instance_type: t3.micro
```

When a remote run executes, the linked ESC environment is resolved dynamically and its values are injected as environment variables into the OpenTofu process. For the saved-plan workflow, credentials are resolved fresh at apply time — not baked in from the plan — so dynamic credentials remain valid even if the apply happens hours later.

{{% notes "info" %}}
The `-var` flag is not supported for remote runs. Use `TF_VAR_*` environment variables through ESC, or include a `.auto.tfvars` file in your configuration directory.
{{% /notes %}}

## Automate with VCS triggers

You can configure your workspace to trigger runs automatically when you push to a repository or open a pull request, using the same [deployment settings](/docs/deployments/concepts/settings/) as Pulumi Deployments:

- **Push events** trigger a plan and apply (or plan with manual confirmation)
- **Pull request events** trigger a speculative plan
- **Git tag pushes** can trigger runs via [tag filtering](/docs/deployments/concepts/settings/tag-filtering/)

To set up VCS-triggered runs:

1. Connect a [version control integration](/docs/integrations/version-control/) (GitHub, GitLab, Bitbucket, or Azure DevOps) to your Pulumi organization.
1. Configure [deployment settings](/docs/deployments/concepts/settings/) on your stack, specifying the source repository and branch.
1. Optionally, configure a [working directory](/docs/deployments/concepts/settings/source/) if your Terraform files are in a subdirectory.

### Manual approval for VCS-triggered applies

By default, VCS-triggered applies pause after the plan completes and wait for manual approval before proceeding. The Pulumi Cloud console shows the plan output and provides **Confirm** and **Discard** buttons. If a preventative policy fails, the failure is shown in the plan logs.

To enable auto-apply (skip the approval step), set the `terraform:auto-apply` [stack tag](/docs/iac/concepts/stacks/#stack-tags) to `true`.

## Enforce policy

{{< pulumi-cloud "preventative-policies" />}}

[Preventative policies](/docs/insights/policy/) automatically evaluate against the plan before an apply proceeds. If any mandatory policy violations are found, the apply is blocked.

Policy enforcement for remote execution works the same way as [audit policies for Terraform stacks](/docs/iac/get-started/terraform/terraform-state-backend/#audit-policies) — add your stack to a [policy group](/docs/insights/policy/policy-groups/) and the configured policy packs are evaluated on every run. Policy packs that target [bridged providers](/docs/iac/concepts/providers/) work automatically, since Terraform resources map to their bridged equivalents. Policy packs that target native Pulumi providers (like the Kubernetes provider) do not apply to Terraform stacks, since Terraform does not use those providers.

## Control execution mode

Execution mode is controlled by the `terraform:execution-mode` [stack tag](/docs/iac/concepts/stacks/#stack-tags) on the Pulumi Cloud stack:

| Tag value | Behavior |
| --- | --- |
| `remote` (default for new stacks) | Plans and applies run on Pulumi Cloud |
| `local` | Plans and applies run on your local machine; Pulumi Cloud stores state only |

Stacks created through the Terraform or OpenTofu CLI default to remote execution. You can change the execution mode at any time from the stack's **Settings** tab in the Pulumi Cloud console, or using the Pulumi CLI:

```bash
# Switch to local execution
pulumi stack tag set terraform:execution-mode local -s <org>/<project>/<stack>

# Switch back to remote execution
pulumi stack tag set terraform:execution-mode remote -s <org>/<project>/<stack>
```

{{% notes "info" %}}
Stacks created before remote execution was available default to local execution mode. Set the tag to `remote` to enable remote execution on an existing stack.
{{% /notes %}}

## Execution environment

Remote runs execute in a managed container environment with the following characteristics:

- **Engine**: [OpenTofu](https://opentofu.org/) — the version is managed by Pulumi Cloud and is not currently configurable
- **Isolation**: each run gets its own container; there is no shared filesystem between runs
- **Provider downloads**: providers are downloaded fresh on each run during `tofu init`

## Migrate from HCP Terraform

If you are migrating from HCP Terraform (Terraform Cloud), the remote execution experience is similar. The main differences are:

| HCP Terraform | Pulumi Cloud |
| --- | --- |
| Workspace variables for credentials | [Pulumi ESC](/docs/esc/) environments |
| `hostname = "app.terraform.io"` | `hostname = "tf.pulumi.com"` |
| Sentinel / OPA for policy | [Pulumi policy packs](/docs/insights/policy/) |
| Runs page in HCP UI | Runs view in Pulumi Cloud console (plan logs, apply logs, confirm/discard) |

To migrate:

1. Follow the [HCP Terraform state migration steps](/docs/iac/get-started/terraform/terraform-state-backend/#migrate-from-hcp-terraform-terraform-cloud) to move your state.
1. Update your `cloud` block to point at Pulumi Cloud (change `hostname` and `organization`).
1. Add your cloud credentials to the stack's [automatically provisioned ESC environment](#provide-credentials-with-esc) to replace workspace variables. If you were using HashiCorp Vault for secrets, ESC can integrate directly via the [Vault secrets provider](/docs/esc/providers/secrets/vault-secrets/) and [Vault login provider](/docs/esc/providers/login/vault-login/).
1. Run `terraform plan` to verify the migration — you should see **No changes**.

## FAQ

### Can I use the Terraform CLI with remote execution?

Yes. Both the Terraform CLI and the OpenTofu CLI communicate with Pulumi Cloud using the same protocol. You can use whichever CLI your team prefers. The remote execution engine always uses OpenTofu regardless of which CLI you use locally.

### How does this compare to HCP Terraform (Terraform Cloud)?

Pulumi Cloud implements a compatible subset of the Terraform Cloud API. The CLI workflow is the same — `terraform plan`, `terraform apply`, saved plans, and interactive confirmation all work as expected. The main differences are that Pulumi Cloud uses ESC for credentials and secrets (instead of workspace variables) and Pulumi policy packs for policy enforcement (instead of Sentinel or OPA).

### Can I use `-var` flags?

Not currently. Use environment variables through an [ESC environment](#provide-credentials-with-esc), or include a `.auto.tfvars` file in your configuration directory. OpenTofu automatically loads `.auto.tfvars` files during plan and apply.

### Is drift detection available?

Not currently for Terraform-managed stacks. You can run `terraform plan` on a schedule via CI/CD to detect drift manually, or [convert your Terraform code to Pulumi](/docs/iac/get-started/terraform/convert-hcl/) (including [Pulumi HCL](/docs/iac/languages-sdks/hcl/)) and use Pulumi's built-in [drift detection](/docs/deployments/concepts/drift/).

### How are resources priced?

Each Terraform resource stored in Pulumi Cloud counts as a resource under management (RUM), the same as a Pulumi-managed resource. Remote execution time is billed as workflow minutes. See the [pricing page](/pricing/) for details.

### Can I use a custom OpenTofu version or executor image?

Not currently. The OpenTofu version is managed by Pulumi Cloud. Custom executor images are planned for a future release.
