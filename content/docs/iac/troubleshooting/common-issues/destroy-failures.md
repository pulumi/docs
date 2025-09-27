---
title_tag: "Resolving Pulumi Destroy Failures"
meta_desc: "Learn how to handle scenarios when pulumi destroy fails to delete resources as expected."
title: Destroy failures
h1: Pulumi destroy fails
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Destroy Failures
        parent: iac-troubleshooting-common-issues
        weight: 50
aliases:
    - /docs/troubleshooting/#pulumi-destroy-fails
---

There are scenarios when `pulumi destroy` will fail to delete resources as expected. This is anticipated due to the nature of cloud provider dependencies, permissions, resources being in a state that prevents their deletion, or when a timeout is not long enough for the cloud provider to complete its operation. Review the output to identify which resources were not deleted and consider the following steps depending on the nature of the failure.

## Check to see if a resource was deleted after all

Some resources take time to be removed. Common examples include CloudFront Lambda@Edge functions, which will fail to `destroy` but will eventually disappear without requiring further action. In these cases, you can wait and run `pulumi refresh` to see if the cloud provider was able to remove the resource.

## Check dependencies

If the issue is due to dependencies, identify and delete the dependent external resources manually. This may involve navigating the cloud provider's console or using its CLI to pinpoint and resolve these dependencies.

## Empty or adjust resources

Occasionally a resource cannot be deleted because it contains data or uses network interfaces or other dependencies managed outside the stack. Common examples include deleting VPCs with EINs attached elsewhere or deleting a security group when it is in use. You will need to evaluate the dependencies given the failure and take the necessary actions to resolve this on each provider resource.

## Delete resources manually

For each resource that couldn't be deleted, use the cloud provider's console or CLI to manually delete it. This may be necessary for resources in a locked state or those with specific permissions preventing automated deletion.

Once you have resolved the source of the deletion failure, you can run `pulumi refresh` to validate that all of your resources are destroyed. This command will update your Pulumi state to reflect the current state in the cloud, effectively recognizing any manual deletions or changes that occurred outside of Pulumi's management.
