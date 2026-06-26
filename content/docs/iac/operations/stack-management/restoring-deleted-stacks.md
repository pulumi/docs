---
title_tag: "Restoring deleted stacks | Pulumi Operations"
meta_desc: Restore a deleted stack in Pulumi Cloud to recover its state file and history after an accidental removal with the Pulumi CLI.
title: Restoring deleted stacks
h1: Restoring deleted stacks
menu:
    iac:
        name: Restoring deleted stacks
        parent: iac-operations-stack-management
        weight: 35
---

Pulumi Cloud retains the state file versions of recently deleted stacks so that organization administrators can recover them through the Pulumi Cloud console. This is useful when a stack is deleted accidentally — most often by `pulumi stack rm --force`, which removes the state file even when the stack still has resources associated with it — or when a stack was intentionally deleted but its activity history is later needed.

{{% notes type="info" %}}
Restoring deleted stacks is a [Pulumi Cloud](/docs/pulumi-cloud/) feature. Stacks stored in a [DIY backend](/docs/iac/operations/stack-management/using-a-diy-backend/) cannot be restored this way; if you operate a DIY backend, you are responsible for your own backup and recovery process for the underlying storage.
{{% /notes %}}

## What gets restored

When you restore a deleted stack, Pulumi Cloud restores the stack's state file and update history. Restoring a stack does not re-create any cloud resources that were destroyed by a prior `pulumi destroy`; it only brings back the stack record and its state so you can resume managing it from Pulumi.

If the stack was deleted with `pulumi stack rm --force` while resources still existed, the cloud resources themselves were not deleted — they were orphaned. Once you restore the stack, those resources are again represented in state and you can manage them with Pulumi as before.

## Limits

- Only the **last 25 deleted stacks** in an organization are available for self-service restore.
- Only **organization administrators** can restore stacks.
- If you need to restore an older stack that is no longer in the list, [contact Pulumi support](/support/).

## Restore a stack

1. Sign in to the [Pulumi Cloud console](https://app.pulumi.com/) as an organization administrator and select the organization the stack belonged to.
1. Navigate to the **Stacks** page for the organization.
1. Next to the **Create project** button, open the three-dot menu and choose **Restore stacks**.
1. Locate the stack you want to restore in the list of recently deleted stacks and select **Restore**.

After the stack is restored, it appears in the organization's stack list with its prior state and history.

## Avoiding accidental deletion

The restore window is finite, so the best protection against accidental loss is preventing the deletion in the first place:

- Prefer `pulumi stack rm` (without `--force`) so the CLI refuses to remove a stack that still has resources tracked in state. Use `pulumi destroy` first, confirm the stack is empty, and then remove it.
- Reserve `pulumi stack rm --force` for cases where you have intentionally decided to orphan the underlying cloud resources or where you are certain the state file does not need to be preserved.
- For stacks that should never be removable through routine operations, restrict who has organization-admin or stack-write permissions. See [Teams and RBAC](/docs/administration/organizations-teams/teams/).

## Related

- [Stacks](/docs/iac/concepts/stacks/) — concept reference, including how to delete a stack.
- [Editing state files](/docs/iac/operations/stack-management/editing-state-files/) — safe techniques for modifying state when normal operations cannot recover.
- [Troubleshooting](/docs/iac/operations/troubleshooting/) — diagnosing and resolving common Pulumi failures.
