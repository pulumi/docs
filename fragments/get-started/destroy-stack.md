## Cleanup & destroy the stack

Our final step is to clean up all of the resources we've allocated in this tutorial.

Run the `pulumi destroy` command to delete all cloud resources in this project/stack:

{{< os-command "pulumi destroy" >}}

Just like `pulumi up`, you'll be shown a preview to ensure that you want to proceed:

{{< gs-include "destroy-stack/preview" >}}

As with an update, we can choose `no` or `details`; select `yes` to proceed:

{{< gs-include "destroy-stack/destroy" >}}

At this stage, your stack still exists, but all cloud resources have been deleted from it.

## Remove the stack

The final step is to remove the stack itself. Destroy keeps the stack around so that you still have the full
history of what happened to the stack. Running [`pulumi stack rm`](/docs/iac/cli/commands/pulumi_stack_rm) will
delete it entirely, including all history and state snapshots. Be careful, this step cannot be undone!

{{< os-command "pulumi stack rm" >}}

You'll be prompted to confirm the removal. Confirm it to successfully complete this tutorial.
