---
title_tag: "Recovering from Interrupted Pulumi Updates"
meta_desc: "Learn how to recover when the Pulumi CLI is interrupted during a deployment."
title: Interrupted updates
h1: Recovering from an interrupted update
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    support:
        name: Interrupted Updates
        parent: support-troubleshooting-common-issues
        weight: 60
aliases:
    - /docs/troubleshooting/#interrupted-update-recovery
    - /docs/iac/troubleshooting/common-issues/interrupted-updates/
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

## Resolving pending creates

When you have pending create operations, `pulumi refresh` will prompt you interactively to resolve them. You'll need to determine whether the resource was actually created in your cloud provider:

1. **If the resource was NOT created:** Select "clear" to remove the pending operation
1. **If the resource WAS created:** You'll need to provide the resource's physical ID so Pulumi can import it into state

### Non-interactive mode

In CI/CD environments or scripts where interactive prompts aren't available, use these flags:

**To clear all pending creates (resource was not created):**

```bash
pulumi refresh --clear-pending-creates --yes
```

**To import pending creates (resource was created):**

Use `--import-pending-creates` with pairs of URN and physical ID:

```bash
pulumi refresh --import-pending-creates "urn:pulumi:dev::myproject::aws:s3/bucket:Bucket::mybucket" "my-bucket-abc123" --yes
```

For multiple pending creates, provide additional URN/ID pairs:

```bash
pulumi refresh \
  --import-pending-creates "urn:pulumi:dev::myproject::aws:s3/bucket:Bucket::bucket1" "bucket1-id" \
  --import-pending-creates "urn:pulumi:dev::myproject::aws:s3/bucket:Bucket::bucket2" "bucket2-id" \
  --yes
```

{{% notes type="warning" %}}
The `--import-pending-creates` flag requires **pairs** of values: the resource URN followed by its physical ID from the cloud provider. If you provide an odd number of values, you'll see the error: `each URN must be followed by an ID: found an odd number of entries`.
{{% /notes %}}

### Finding the physical ID

To find the physical ID of a resource that was created:

- **AWS:** Check the AWS Console or use the AWS CLI to find the resource
- **Azure:** Check the Azure Portal or use `az` CLI
- **GCP:** Check the Cloud Console or use `gcloud` CLI

The physical ID format varies by provider and resource type. For example:

- AWS S3 bucket: the bucket name (e.g., `my-bucket-abc123`)
- AWS EC2 instance: the instance ID (e.g., `i-0123456789abcdef0`)
- Azure resource: the full resource ID path

At this point your stack should be valid, up-to-date, and ready to accept future updates.
