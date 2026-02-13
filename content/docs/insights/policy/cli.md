---
title: CLI Reference
title_tag: "CLI Reference | Pulumi Policies"
h1: Policy CLI Reference
meta_desc: Use the pulumi policy CLI commands to create, publish, install, enable, and manage policy packs and policy groups from the command line.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: CLI Reference
    parent: insights-policy
    weight: 55
---

The `pulumi policy` command group provides CLI commands for creating, managing, and enforcing policy packs. You can use these commands to author new policy packs, publish them to Pulumi Cloud, and manage policy groups across your organization.

## Policy pack commands

| Command | Description |
| --- | --- |
| [`pulumi policy new`](/docs/iac/cli/commands/pulumi_policy_new/) | Create a new policy pack from a template |
| [`pulumi policy install`](/docs/iac/cli/commands/pulumi_policy_install/) | Install required policy packs for a stack |
| [`pulumi policy publish`](/docs/iac/cli/commands/pulumi_policy_publish/) | Publish a policy pack to Pulumi Cloud |
| [`pulumi policy enable`](/docs/iac/cli/commands/pulumi_policy_enable/) | Enable a policy pack for a Pulumi organization |
| [`pulumi policy disable`](/docs/iac/cli/commands/pulumi_policy_disable/) | Disable a policy pack for a Pulumi organization |
| [`pulumi policy ls`](/docs/iac/cli/commands/pulumi_policy_ls/) | List all policy packs for a Pulumi organization |
| [`pulumi policy rm`](/docs/iac/cli/commands/pulumi_policy_rm/) | Remove a policy pack from a Pulumi organization |
| [`pulumi policy validate-config`](/docs/iac/cli/commands/pulumi_policy_validate-config/) | Validate a policy pack configuration against its schema |

## Policy group commands

| Command | Description |
| --- | --- |
| [`pulumi policy group`](/docs/iac/cli/commands/pulumi_policy_group/) | Manage policy groups |
| [`pulumi policy group ls`](/docs/iac/cli/commands/pulumi_policy_group_ls/) | List all policy groups for a Pulumi organization |

## Running policies locally

You can run policy packs locally during `pulumi preview` or `pulumi up` by using the `--policy-pack` flag. This does not require Pulumi Cloud and works with any backend, including the self-managed backend.

```bash
pulumi preview --policy-pack /path/to/policy-pack
```

```bash
pulumi up --policy-pack /path/to/policy-pack
```

You can also apply multiple policy packs at the same time:

```bash
pulumi up --policy-pack /path/to/pack-1 --policy-pack /path/to/pack-2
```

{{% notes type="info" %}}
When using `--policy-pack`, the policy pack must be present on disk. Pulumi Cloud users can skip this flag entirely — policy packs enabled through [policy groups](/docs/insights/policy/policy-groups/) are downloaded and applied automatically.
{{% /notes %}}

## Common workflows

### Create and test a policy pack

```bash
# Create a new policy pack from a template
pulumi policy new aws-typescript

# Test policies locally during preview
pulumi preview --policy-pack .
```

### Publish and enable a policy pack

```bash
# Publish the policy pack to Pulumi Cloud
pulumi policy publish

# Enable the latest version for your organization
pulumi policy enable my-org/my-policy-pack latest
```

### Manage policy packs

```bash
# List all policy packs in your organization
pulumi policy ls

# Disable a policy pack
pulumi policy disable my-org/my-policy-pack

# Remove a policy pack (must be disabled first)
pulumi policy rm my-org/my-policy-pack
```

For the full CLI reference, see [`pulumi policy`](/docs/iac/cli/commands/pulumi_policy/).
