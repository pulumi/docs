---
title: "Known issues"
---

You should be aware of the following known issues and product limitations.  The team is actively working on fixing these issues.

If you encounter an problem that's not on this list, please file a [GitHub issue](https://github.com/pulumi/pulumi/issues/new). <!-- validate the link once public -->

## Update Lease Cannot Be Renewed {#pulumi-pulumi-1077}

If an update is interrupted when logged into the Pulumi service, for example by hitting ^C, losing Internet connectivity, or closing your laptop in the middle of an update, the update lease token will be orphaned and the service will refuse to let you proceed with subsequent updates.  This will yield the following error message:

    error: another update is currently in progress or was interrupted; try again later

The lease will expire automatically in 5 minutes, so you should wait and try again.  Depending on the manner in which the update was interrupted, your stack may be left in an invalid state.  Please refer to [the other known issue](#pulumi-pulumi-1094) below for more details.

> **Note:** This error is indistinguishable from the case where two parties attempt to update the same stack concurrently.  If you wait 5 minutes and this error recurs, that is the most likely explanation.  Making this situation clearer -- for instance, by showing you who is actively updating the stack and when they started -- is an area for improvement in the future.

Overall improvements to this area are tracked by [Improved UX for cancellation, hibernate, and timeout with managed stacks](https://github.com/pulumi/pulumi/issues/1077).

## Interrupted Updates Can Lead to Unknown State {#pulumi-pulumi-1094}

If an update is interrupted partway through, it is possible that the service's understanding of your stack's state will have drifted from reality.  The Pulumi CLI and service have no way of reconciling this drift today, and react conservatively by marking the state as "unknown."  The result is the following error message:

    error: stack's resources are in an unknown state due to an interrupted update;
        please export the stack, repair any inconsistencies, and import the result

To recover from this situation, you will need to do three things:

1. Export your stack's current state checkpoint by running the `pulumi export` command.  It is JSON and you probably want to redirect it to a file for easy viewing and editing: `pulumi export > stack.json`.  We recommend making a backup of this file for safe-keeping, since what follows requires a bit of manual and error prone editing.
2. Manually verify that the state represents the current state in your cloud and make any necessary edits to the state file (if any -- it is possible none will be needed).  *Be very careful making edits; any incorrect information may worsen the situation, and any deletions are not easy to recover in the current system.*
3. Import your stack's updated state checkpoint, with the newly patched resource information, using the `pulumi import` command.  For example, if stored in the `stack.json` file, just run `pulumi import < stack.json`.  This will upload your file and automatically clear the unknown status on your stack so that it is usable once again.

This issue is being tracked primarily by [Improved recovery for invalid stacks](https://github.com/pulumi/pulumi/issues/1094), although [CLI command to refresh a resource's state](https://github.com/pulumi/pulumi/issues/1081) will also be a critical element to improving the experience here.

## CloudFront ETag Out Of Synch {#pulumi-terraform-57}

When using AWS CloudFront resources with Pulumi, you can run into errors if you update the CloudFront resource directly through AWS, such as the AWS CLI or console. This known issue is anticipated to be solved in the v0.12.0 SDK, as part of implementing the fix [Perform a `Refresh` operation before each `Apply` #57](https://github.com/pulumi/pulumi-terraform/issues/57).

The CLI will show an error such as the following:

```
rpc error: code
  = Unknown desc = deleting urn:pulumi:stack::project::aws:cloudfront/distribution:Distribution::cdn-name:
  PreconditionFailed: The request failed because it didn't meet the preconditions
  in one or more request-header fields.
```

This is because any CloudFront update operation (such as registering a new domain via Route53) rolls forward the [ETag](https://en.wikipedia.org/wiki/HTTP_ETag). Any future management operations must supply the latest ETag, or they will fail. Because Pulumi stores the last ETag in your stack checkpoint file, you must manually update the ETag value if you have managed CloudFront resources outside of Pulumi.

You can update the ETag using the stack `import` and `export` operations:

1.  Export the current stack checkpoint and copy to a new file:

    ```bash
    pulumi stack export > before.json # save current stack contents
    cp before.json after.json         # copy contents to a new file
    ```

1.  Find the CloudFront distribution ID in `before.json`.

1.  Get the latest ETag for your CloudFront resource, using the distribution ID from the previous step:

    ```bash
    aws cloudfront get-distribution --id <ID> | grep -i etag
    ```

1.  Edit `after.json` and replace the `"etag": "<OLD_VALUE>"` with the ETag you retrieved from the previous step.

1.  To ensure the edit was performed correctly, perform a diff: `diff -c before.json after.json`.

1.  Import the new stack value via `pulumi stack import < after.json`. Now, future updates will be based on the correct ETag.

## Cannot Change Pulumi.yaml Project Name {#pulumi-pulumi-541}

The project name in `Pulumi.yaml` is assumed to be part of a stable identifier in identifying a stack (either a local or managed stack). Currently, renaming the project will result in all stack resources being orphaned. To work around this, run `pulumi destroy` before renaming the project. (If you have already changed the project name, simply change back to the old name and run `pulumi destroy`.) See [Changing `name` in Pulumi.yaml leads to assert #541](https://github.com/pulumi/pulumi/issues/541).
