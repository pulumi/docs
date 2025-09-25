---
title_tag: "Recovering from Interrupted Pulumi Updates"
meta_desc: "Learn how to recover when the Pulumi CLI is interrupted during a deployment."
title: Interrupted updates
h1: Recovering from an interrupted update
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Interrupted Updates
        parent: iac-troubleshooting-common-issues
        weight: 60
aliases:
    - /docs/troubleshooting/#interrupted-update-recovery
---

If the Pulumi CLI is interrupted when performing a deployment, you may see a warning message that looks something like this on your next update:

```bash
$ pulumi up
...
Diagnostics:
  pulumi:pulumi:Stack (proj):
    warning: Attempting to deploy or update resources with 1 pending operations from previous deployment.
      * urn:pulumi:dev::proj::aws:s3/bucket:Bucket::bucket, interrupted while creating
    These resources are in an unknown state because the Pulumi CLI was interrupted while waiting for changes to these resources
    to complete. You should confirm whether or not the operations listed completed successfully by checking the state of the
    appropriate provider. For example, if you are using AWS, you can confirm using the AWS Console.

    Once you have confirmed the status of the interrupted operations, you can repair your stack using `pulumi refresh` which will refresh the state from the provider you are using and clear the pending operations if there are any.

    Note that `pulumi refresh` will need to be run interactively to clear pending CREATE operations.
...
```

This occurs when the Pulumi CLI fails to complete cleanly. There are a number of ways this can happen:

- The CLI experiences a network partition when attempting to save your stack's state.
- The CLI process is killed by your operating system while performing an update.
- The CLI crashes when performing an update.

This error means that the Pulumi engine initiated an operation but was not able to determine if the operation completed successfully. As a result, resources may have been created that Pulumi does not know about.

To fix this condition, you should first cancel the update:

```bash
$ pulumi cancel
...
The currently running update for 'interruptedstack' has been canceled!
```

If `pulumi cancel` fails with `error: [400] Bad Request: the update has already completed`, you can safely ignore that error and continue with the next step.

Then run `pulumi refresh` to remove any pending operations cleanly, allowing you to resolve any pending operations that Pulumi could not fix unaided.

At this point your stack should be valid, up-to-date, and ready to accept future updates.
