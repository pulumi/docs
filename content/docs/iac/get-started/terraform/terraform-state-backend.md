---
title_tag: Store Terraform State in Pulumi Cloud | Pulumi for Terraform Users
title: Store Terraform State in Pulumi Cloud
h1: "Store Terraform State in Pulumi Cloud"
meta_desc: Use Pulumi Cloud as your Terraform state backend for update history, state locking, RBAC, audit policies, and unified resource visibility.
weight: 9
menu:
    iac:
        name: Store Terraform State
        parent: terraform-get-started
        weight: 9
        identifier: terraform-state-backend

aliases:
---

Pulumi Cloud can serve as a [Terraform state backend](https://developer.hashicorp.com/terraform/language/backend), letting you store and manage Terraform state alongside your Pulumi stacks. Your team can continue using the Terraform or OpenTofu CLI for day-to-day operations while gaining the benefits of Pulumi Cloud: encrypted state storage, update history, state locking, role-based access control, audit policies, and unified resource visibility through [Insights](/docs/pulumi-cloud/insights/).

{{% notes "info" %}}
This feature is currently in **public beta**.
{{% /notes %}}

## Why store Terraform state in Pulumi Cloud

If you are managing Terraform state in S3, Azure Blob Storage, or another DIY backend, migrating to Pulumi Cloud gives you:

- **Encrypted state** — state is encrypted in transit and at rest, a common concern with S3 backends
- **Update history and versioning** — every state change is tracked as a versioned checkpoint, visible in the [stack Activity tab](/docs/deployments/projects-and-stacks/#stack-activity)
- **Automatic state locking** — prevents concurrent operations from corrupting state
- **Role-based access control** — control who can read or modify each stack with [teams and RBAC](/docs/administration/access-identity/rbac/)
- **Unified resource visibility** — view Terraform-managed resources alongside Pulumi-managed resources in [Resource Search](/docs/pulumi-cloud/insights/search/)

## How it works

Pulumi Cloud implements the [Terraform remote backend API](https://developer.hashicorp.com/terraform/language/backend/remote). This means you can point the Terraform CLI at Pulumi Cloud using the standard `backend "remote"` configuration block — no changes to your Terraform code or workflow are required.

### Concept mapping

| Terraform concept | Pulumi Cloud concept |
| --- | --- |
| Workspace | [Stack](/docs/iac/concepts/stacks/) |
| Workspace prefix | [Project](/docs/iac/concepts/projects/) |
| State file | Checkpoint (versioned) |
| Workspace lock | Stack update lock |

When you migrate state, each Terraform workspace maps to a Pulumi stack. The workspace name follows the convention `<project>_<stack>` (for example, `networking_prod` creates a stack named `prod` in the `networking` project).

If you use Terraform [workspace prefixes](https://developer.hashicorp.com/terraform/language/backend/remote#workspace-prefix) instead of a single named workspace, Pulumi Cloud supports the `workspaces.prefix` configuration as well. Each workspace matching the prefix maps to a separate stack under the same project.

### Resource mapping

When Terraform state is stored in Pulumi Cloud, each Terraform resource is converted to a synthetic Pulumi resource for visibility in the console and Resource Search. Resources are stored using a `pulumi:terraform:<tf-type>` type convention — for example, an `aws_instance` resource in Terraform appears as `pulumi:terraform:aws_instance` in Pulumi Cloud.

This "mechanical" mapping preserves the Terraform resource structure (attribute names, IDs, dependencies) without transforming it to Pulumi provider schemas. Resource properties use Terraform naming conventions, so practitioners can search for resources in Resource Search using the attribute names they are already familiar with. Sensitive values marked in your Terraform state are encrypted.

Terraform root module outputs are mapped to Pulumi [stack outputs](/docs/iac/concepts/stacks/#outputs), making them available for [stack references](/docs/iac/concepts/stacks/#stackreferences). This means your Pulumi stacks can directly reference Terraform outputs — useful for sharing foundational infrastructure like VPC IDs or DNS zones across teams.

### Audit policies

You can run [audit (detective) policy packs](/docs/insights/policy/policy-groups/) against Terraform-managed stacks. During policy evaluation, Pulumi performs a best-effort schema mapping from Terraform resource shapes to their Pulumi bridged provider equivalents using the latest provider version. This allows existing policy packs written against Pulumi schemas — including Pulumi's [pre-built compliance packs](/docs/insights/policy/policy-packs/pre-built-packs/) — to evaluate Terraform resources.

To configure audit policies for a Terraform stack, add the stack to an [audit policy group](/docs/insights/policy/policy-groups/) in Insights. Policy packs are then evaluated continuously against the stack's resources.

{{% notes "info" %}}
Only audit (detective) policies are supported for Terraform-managed stacks. Preventative policies require a Pulumi program and are not applicable to stacks updated via the Terraform CLI. The schema mapping works automatically for [bridged providers](/docs/iac/concepts/resources/providers/) but does not currently cover native Pulumi providers like Kubernetes.
{{% /notes %}}

## Migrate from a standard backend (S3, Azure Blob, GCS, local)

If your Terraform state is currently stored in S3, Azure Blob Storage, GCS, a local file, or any other standard backend, migration is a single command.

### 1. Back up your state

Before making any changes, create a backup of your current state file:

```bash
terraform state pull > terraform_state_backup.tfstate
```

### 2. Update your backend configuration

Replace your existing backend block with the Pulumi Cloud remote backend:

```hcl
terraform {
  backend "remote" {
    hostname     = "api.pulumi.com"
    organization = "<your-pulumi-org>"

    workspaces {
      name = "<project>_<stack>"
    }
  }
}
```

Replace the placeholders:

| Placeholder | Description | Example |
| --- | --- | --- |
| `<your-pulumi-org>` | Your Pulumi Cloud organization name | `acme-corp` |
| `<project>` | The Pulumi project name for this stack | `networking` |
| `<stack>` | The Pulumi stack name | `prod` |

{{% notes "info" %}}
If you are using a [self-hosted Pulumi Cloud](/docs/pulumi-cloud/self-hosted/) instance, replace `api.pulumi.com` with your instance's API URL.
{{% /notes %}}

### 3. Set your access token

For security, use an environment variable instead of hardcoding the token in your configuration:

```bash
export TF_TOKEN_api_pulumi_com="pul-xxxxxxxxxxxx"
```

The environment variable follows the Terraform convention `TF_TOKEN_<hostname>` where dots in the hostname are replaced with underscores.

### 4. Run the migration

```bash
terraform init -migrate-state
```

Terraform detects the backend change and prompts you to confirm the migration. Type `yes` to proceed.

### 5. Verify the migration

```bash
terraform plan
```

You should see **No changes**. This confirms that the state was migrated correctly and matches your infrastructure.

You can also verify in the Pulumi Cloud console — navigate to your organization and look for the new stack. Terraform-managed stacks appear with a Terraform icon in the default group-by-project view!

![Terraform-managed stack in the Pulumi Cloud console](/images/docs/iac/get-started/terraform/terraform-stack-console.png)

## Migrate from HCP Terraform (Terraform Cloud)

HCP Terraform does not support automatic state migration using `terraform init -migrate-state`. You need to export the state manually and push it to Pulumi Cloud.

### 1. Back up your state from HCP Terraform

Make sure your local Terraform version matches the version configured in your HCP workspace, then pull the state:

```bash
terraform state pull > hcp_state_backup.tfstate
```

Verify the backup contains your resources:

```bash
terraform state list -state=hcp_state_backup.tfstate
```

### 2. Remove the HCP Terraform configuration

Back up your configuration file, then remove the `cloud` block:

```hcl
terraform {
  # Remove or comment out the cloud block:
  # cloud {
  #   organization = "your-org"
  #   workspaces {
  #     name = "your-workspace"
  #   }
  # }

  required_providers {
    # ... your providers remain unchanged
  }
}
```

Clear the local Terraform cache:

```bash
rm -rf .terraform
```

### 3. Add the Pulumi Cloud backend configuration

Add the remote backend block as described in the [standard migration section above](#2-update-your-backend-configuration).

### 4. Initialize the new backend

```bash
terraform init
```

Since this is a fresh backend with no existing state, Terraform initializes without prompting for migration.

### 5. Push the state

```bash
terraform state push hcp_state_backup.tfstate
```

If you encounter lineage or serial number errors, you can force the push:

```bash
terraform state push -force hcp_state_backup.tfstate
```

{{% notes "warning" %}}
Only use `-force` if you are certain the state file is correct and no concurrent operations are running.
{{% /notes %}}

### 6. Verify the migration

```bash
terraform plan
```

You should see **No changes**.

## Update CI/CD pipelines

After migrating, update your CI/CD pipelines to authenticate with Pulumi Cloud instead of your previous backend.

### GitHub Actions example

```yaml
env:
  TF_TOKEN_api_pulumi_com: ${{ secrets.PULUMI_ACCESS_TOKEN }}

steps:
  - name: Terraform Init
    run: terraform init

  - name: Terraform Plan
    run: terraform plan
```

## Post-migration: using Pulumi Cloud

Once your Terraform state is in Pulumi Cloud, you can:

- **View resources** in [Resource Search](/docs/pulumi-cloud/insights/search/) alongside your Pulumi-managed resources
- **Run audit policies** by adding the stack to an [audit policy group](/docs/insights/policy/policy-groups/) in Insights
- **Continue using Terraform or OpenTofu** for all `plan`, `apply`, and `destroy` operations

### Restoring a previous state version

Pulumi Cloud stores every state update as a versioned checkpoint. If you need to restore a previous version, export it and import it back:

```bash
pulumi stack export --version <version-number> > previous_checkpoint.json
pulumi stack import --file previous_checkpoint.json
```

You can find version numbers in the stack's **Activity** tab in the Pulumi Cloud console. For more details on working with state files, see [Editing state files](/docs/support/troubleshooting/editing-state-files/).

## FAQ

### Can I use drift detection or Pulumi Deployments with Terraform-managed stacks?

Not currently. Drift detection and [Pulumi Deployments](/docs/pulumi-cloud/deployments/) require a Pulumi program to execute. If you want these features, you can [convert your Terraform code to Pulumi](/docs/iac/get-started/terraform/convert-hcl/) and then run updates with the Pulumi CLI.

### Can I use preventative policies?

Preventative policies run during `pulumi preview` and `pulumi up`, which are Pulumi CLI operations. Since Terraform-managed stacks are updated via the Terraform CLI, only audit (detective) policies are supported. See [audit policies](#audit-policies) above.

### How do update diffs work for Terraform stacks?

Pulumi Cloud generates update diffs by comparing the previous and current Terraform state snapshots. These diffs are best-effort — they show which resources were created, updated, replaced, or deleted, along with property-level changes, but they may not match `terraform plan` output exactly since they are derived from state rather than from the Terraform execution plan.

Terraform [check blocks](https://developer.hashicorp.com/terraform/language/checks) are surfaced as diagnostic events in the update timeline, giving you visibility into check failures directly in the Pulumi Cloud console.

### How are Terraform resources priced?

Each Terraform resource stored in Pulumi Cloud counts as a resource under management (RUM), the same as a Pulumi-managed resource. See the [pricing page](/pricing/) for details.

## Troubleshooting

### "Backend configuration changed" error

If you see this error after modifying the backend, re-initialize with:

```bash
terraform init -reconfigure
```

### "State serial is less than current" error

The state in Pulumi Cloud has a higher serial number than your local copy. Either pull the current state and merge manually, or use `terraform state push -force` if you are certain your local state is correct.

### "Failed to get existing workspaces" error

Verify your Pulumi access token is correct:

```bash
pulumi whoami
```

Check that the `TF_TOKEN_api_pulumi_com` environment variable is set and that your token has permissions for the target organization.

### "Migrating state from HCP Terraform to another backend is not yet implemented" error

This is expected when migrating from HCP Terraform. Follow the [HCP Terraform migration steps](#migrate-from-hcp-terraform-terraform-cloud) instead of using `terraform init -migrate-state`.
