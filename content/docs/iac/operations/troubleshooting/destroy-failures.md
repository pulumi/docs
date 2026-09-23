---
title_tag: "Resolving Pulumi Destroy Failures"
meta_desc: "Learn how to handle scenarios when pulumi destroy fails to delete resources as expected."
title: Destroy failures
h1: Pulumi destroy fails
menu:
    iac:
        name: Destroy Failures
        parent: iac-operations-troubleshooting
        weight: 50
aliases:
    - /docs/troubleshooting/#pulumi-destroy-fails
    - /docs/support/troubleshooting/common-issues/destroy-failures/
    - /docs/iac/troubleshooting/common-issues/destroy-failures/
---

There are scenarios when `pulumi destroy` will fail to delete resources as expected. This is anticipated due to the nature of cloud provider dependencies, permissions, resources being in a state that prevents their deletion, or when a timeout is not long enough for the cloud provider to complete its operation. Review the output to identify which resources were not deleted and consider the following steps depending on the nature of the failure.

## Stale or expired credentials

If your Pulumi program fetches provider credentials at runtime — from an OIDC exchange, a secrets manager, or a platform-team library — `pulumi destroy` does not re-run the program by default. It reuses the provider configuration recorded during the last update, so any short-lived credential it captured has likely expired. The destroy then fails with what looks like an auth error from the cloud provider.

Re-run the program before destroying by passing `--run-program`:

```bash
pulumi destroy --run-program
```

See [Running your program on refresh and destroy](/docs/iac/operations/stack-management/run-program/) for the full explanation.

## Deletion protection on the resource itself

A `pulumi destroy` failure is often not an engine problem at all: the resource itself is guarded against deletion, and something has to remove that guard before Pulumi can delete it. Three distinct layers can hold this kind of protection, and the error message usually tells you which one you hit.

- **Pulumi's own `protect` resource option.** This is an engine-level guard that never reaches the cloud provider. If you see an error naming a URN and mentioning `protect`, see [Protect](/docs/iac/concepts/resources/options/protect/) for how to remove it.
- **A provider-enforced flag.** Some Pulumi providers refuse to issue the delete call at all when a resource carries a deletion-protection attribute, for example `deletionProtection` on `gcp.sql.DatabaseInstance` or `gcp.container.Cluster`. The failure surfaces from the provider before any request reaches the cloud API.
- **A cloud-API-enforced protection.** Some clouds reject the delete call themselves, independent of Pulumi, for example AWS RDS `deletionProtection`, EC2 `disableApiTermination`, or an Azure Resource Manager management lock. The error text in this case comes back from the cloud provider's API, often with a distinct error code such as `ScopeLocked`.

The remediation for the second and third cases is the same, and it isn't what most people try first. Because `pulumi destroy` deletes what is already recorded in your stack's state, not what your program currently says, setting the attribute to `false` in your program is not enough on its own:

1. Set the deletion-protection attribute to `false` in your Pulumi program.
1. Run `pulumi up` so the change reaches both the live resource and Pulumi's state.
1. Run `pulumi destroy`.

If the protection was already disabled outside of Pulumi, for example directly in the cloud console, `pulumi refresh` synchronizes your stack's state with reality, and `pulumi destroy` then succeeds without needing an intervening `pulumi up`.

The following resources are common sources of this kind of failure:

| Provider | Resource | Attribute | Notes |
| --- | --- | --- | --- |
| GCP | `gcp.sql.DatabaseInstance` | `deletionProtection` | Provider-enforced; a nested `settings.deletionProtectionEnabled` also guards the instance at the GCP API level. |
| GCP | `gcp.container.Cluster` | `deletionProtection` | Provider-enforced. |
| GCP | `gcp.bigquery.Table` | `deletionProtection` | Provider-enforced. |
| GCP | `gcp.bigquery.Dataset` | `deleteContentsOnDestroy` | Destroying a dataset that still contains tables fails unless this is `true`. |
| AWS | `aws.rds.Instance` / `aws.rds.Cluster` | `deletionProtection` | Enforced by the AWS API; defaults to `false`. |
| AWS | `aws.s3.BucketV2` | `forceDestroy` | Defaults to `false`; a non-empty bucket otherwise fails to delete. |
| AWS | `aws.ec2.Instance` | `disableApiTermination` | Enforced by the AWS API (EC2 termination protection). |
| AWS | `aws.dynamodb.Table` | `deletionProtectionEnabled` | Enforced by the AWS API; defaults to `false`. |
| Azure | Any resource under a management lock | N/A (`azure-native.authorization.ManagementLock`) | Enforced by Azure Resource Manager; a `CanNotDelete` lock must be removed before the resource can be deleted, independent of anything in your Pulumi program. |
| Azure | `azure-native.keyvault.Vault` | Soft delete and purge protection | Destroying the vault only soft-deletes it. Recreating a vault with the same name fails with `VaultAlreadyExists` until the soft-deleted vault is purged or recovered, and purge protection prevents purging until its retention period elapses. |

## Check to see if a resource was deleted after all

Some resources take time to be removed. Common examples include CloudFront Lambda@Edge functions, which will fail to `destroy` but will eventually disappear without requiring further action. In these cases, you can wait and run `pulumi refresh` to see if the cloud provider was able to remove the resource.

## Check dependencies

If the issue is due to dependencies, identify and delete the dependent external resources manually. This may involve navigating the cloud provider's console or using its CLI to pinpoint and resolve these dependencies.

## Empty or adjust resources

Occasionally a resource cannot be deleted because it contains data or uses network interfaces or other dependencies managed outside the stack. Common examples include deleting VPCs with EINs attached elsewhere or deleting a security group when it is in use. You will need to evaluate the dependencies given the failure and take the necessary actions to resolve this on each provider resource.

## Delete resources manually

For each resource that couldn't be deleted, use the cloud provider's console or CLI to manually delete it. This may be necessary for resources in a locked state or those with specific permissions preventing automated deletion.

Once you have resolved the source of the deletion failure, you can run `pulumi refresh` to validate that all of your resources are destroyed. This command will update your Pulumi state to reflect the current state in the cloud, effectively recognizing any manual deletions or changes that occurred outside of Pulumi's management.
