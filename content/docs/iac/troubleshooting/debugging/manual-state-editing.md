---
title_tag: "Editing Pulumi State Files"
meta_desc: "Learn how to safely edit Pulumi state files when necessary"
title: Editing state files
h1: Editing state files
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Editing State Files
        parent: iac-troubleshooting
        weight: 30
---

The Pulumi engine uses both your program's code and your stack's existing state to make decisions about what resources to create, read, update, or delete, and in what order. In some cases, you may need to perform edits to your state file, either programmatically (preferred) or by editing the state file in a text editor (as a last resort).

This page is a guide on how to edit your state file as safely as possible.

## When you might need to edit your state file

You might need to edit your state file in the following situations:

- You want to move resources between stacks in the course of refactoring of your Pulumi codebase(s)
- You need to unprotect resources from deletion
- A Pulumi command fails with an error indicating a corrupt state, for example if you see [an I/O error with the text `after mutation of snapshot`](/docs/iac/troubleshooting/common-problems/post-step-errors), which can occur in rare scenarios like a network partition during a state file update.

## What to try before editing your state file

Before manually editing your state file, consider these troubleshooting steps:

1. Run the `pulumi refresh` command.
1. Update to the latest version of the Pulumi CLI ([installation instructions](/docs/iac/cli/install/)) and attempt your operation again.
1. If a `pulumi update` failed and a resource was created and shows in your cloud console, but Pulumi is attempting to create the resource again, use the `pulumi import` command instead of editing your state file.
1. If you have recently updated the Pulumi CLI, consider downgrading back to the previous known-good version and attempt your operation again.
1. Update the Pulumi SDK to the version that matches the Pulumi CLI.
1. If the problem seems to be related to a particular resource type or provider, consider updating your provider dependencies (do this work on a separate git branch so you can easily undo any changes to your Pulumi code).

{{% notes type="info" %}}
If your Pulumi issue is causing a serious outage for your workload(s), and Pulumi CLI operations are taking too long, consider the `--target` option, which allows you to limit the refresh operation only to the resources you specify. (The flag can be specified more than once.)

The following commands support the `--target` option:

- `pulumi refresh`
- `pulumi preview`
- `pulumi up`
- `pulumi destroy`
{{% /notes %}}

## How to edit your state file safely

If you have determined that it is appropriate and necessary to edit your state file, follow these steps to do so safely:

{{% notes type="info" %}}
If possible, ensure that your team members do not attempt to make updates to your stack while you are editing your state file, e.g., by communicating your intent over a shared chat channel. Additional Pulumi operations (e.g., performed by other team members unaware that you are editing the state file) that write to the state file can invalidate the changes you are making.
{{% /notes %}}

### 1. Save a backup of your state file

First, you should take a backup of your state file to ensure that any changes you make can be easily reversed. To take a backup of your state file:

```bash
pulumi stack export --file pulumi-state-backup.json
```

If you want to undo the changes you make in subsequent steps, you can restore your state file from backup:

```bash
pulumi stack import --file pulumi-state-backup.json
```

### 2. Try targeted fixes with the `pulumi state` command

The [`pulumi state`](/docs/iac/cli/commands/pulumi_state) command allows you to make targeted, surgical changes to your state file without the risk of exposing your entire state file in an editor for hand-editing, which can cause additional errors.

The `pulumi state` command can help with the following scenarios:

- Automatically repairing your state file with [`pulumi state repair`](/docs/iac/cli/commands/pulumi_state_repair)
- Deleting resources from your state file with [`pulumi state delete`](/docs/iac/cli/commands/pulumi_state_delete)
- Moving resources between stacks with [`pulumi state move`](/docs/iac/cli/commands/pulumi_state_move)
- Unprotecting resources from deletion with [`pulumi state unprotect`](/docs/iac/cli/commands/pulumi_state_unprotect)
- Targeting resources for recreation with [`pulumi state taint`](/docs/iac/cli/commands/pulumi_state_taint)

Refer to [the `pulumi state` reference docs](/docs/iac/cli/commands/pulumi_state) for a complete list of capabilities.

### 3. If necessary, export your state file and edit

If the `pulumi state` command does not resolve the issue for you, you will need to edit your Pulumi state file in an editor to resolve the issue. First, export the state file again:

```bash
pulumi stack export --file state.json
```

{{% notes type="warning" %}}
The recommendation to export your state file a second time with a different filename from the backup you created earlier is intentional!

Do not forget to export an additional copy of your Pulumi state file. Failing to do so may make it difficult or impossible to undo your changes once you save your state file to your Pulumi state backend.
{{% /notes %}}

Then, perform any manual edits using the [State File reference](#state-file-reference) as a guide. When your edits are complete, import the edited state file with the following command:

```bash
pulumi stack import --file state.json
```

## State file reference

Your state file is represented as a JSON object. At the top level, this JSON object has two fields:

| Field | Description |
| - | - |
| `version` | The version of the file format. This should not be changed. |
| `deployment` | The last deployment state of the stack. |

The `deployment` object has the following fields:

| Field | Description |
| - | - |
| `manifest` | Metadata about the previous deployment. This should not be changed. |
| `pending_operations` | List of the operations that the Pulumi engine started but has not finished. |
| `resources` | List of resources that Pulumi knows about. |

The `resources` field is a list, not a set: The order of resources in the list is important and is enforced by the Pulumi engine. Resources in a deployment must be in *dependency order* - if resource A depends on resource B, resource A *must* appear after resource B in the list.

The possible fields of an entry in `resources` are:

| Field |  Description |
| - | - |
| `urn` | The resource URN, which is a Pulumi-specific universal resource identifier. |
| `custom` | A boolean indicating whether or not this resource is a `custom` resource, which means that it uses a resource provider to operate. Component resources are not `custom`. |
| `delete` | A boolean indicating whether or not this resource is pending deletion. |
| `id` | This resource's ID, which is a provider-specific resource identifier. This often corresponds to a cloud provider's identifier for a resource. |
| `type` | The Pulumi type of this resource. |
| `inputs` | A map of inputs for this resource. Inputs are the set of key-value pairs used as an input to a resource provider. |
| `outputs` | A map of outputs for this resource. Outputs are the set of key-value pairs that were given to Pulumi by a resource provider after a resource has been provisioned. |
| `parent` | A URN for this resource's parent resource. |
| `protect` |  A boolean indicating whether or not this resource is protected. Protected resources can not be deleted. |
| `external` | A boolean indicating whether or not this resource is external to Pulumi. If a resource is external, Pulumi does not own its life cycle and it will not ever delete or update the resource. Resources that are read using the `get` function are external. |
| `dependencies` | A list of URNs indicating the resources that this resource depends on. Pulumi tracks dependencies between resources. It is important that this list be the full list of resources upon which this resource depends. |
| `initErrors` | A list of errors that occurred that prevented the resource from initializing. Some resource providers (most notably Kubernetes) populate this field to indicate that a resource was created but failed to initialize. |
| `provider` | Reference to the provider responsible for the resource. |
