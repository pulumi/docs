---
title: "Retain on Delete"
date: 2022-02-23
meta_desc: Introducing the new resource option RetainOnDelete.
meta_image: meta.png
authors:
    - fraser-waters
tags:
    - features

---

Pulumi is frequently used to manage the entire lifecycle of a resource, from creation, to updates, to replacement, to deletion. However, there are some cases where it is important to ensure that a resource's life can extend beyond the lifetime of the Pulumi program that created it. To support these use cases, Pulumi now supports a new resource option `RetainOnDelete` which allows a resource to be retained in a cloud provider even after it is deleted from the Pulumi stack it is part of.

<!--more-->

We've seen a number of user questions over the years about keeping resources after Pulumi deployments, or sharing resources between deployments. All of these worked down to needing a new [resource option](https://github.com/pulumi/pulumi/issues/7747) to tell the Pulumi engine to not actually delete a resource when replacing or removing it from the stack.

## Retain on delete

We [now support](https://github.com/pulumi/pulumi/releases/tag/v3.25.0) a new resource option [retain on delete]({{< relref "docs/intro/concepts/resources/options/retainOnDelete" >}}) that allows you to specify this case to the engine.

When a resource marked with `RetainOnDelete` is deleted or replaced by a Pulumi update, the resource is removed from the Pulumi state but Pulumi does not delete the actual resource in the cloud. That is, it won't call through to the resource provider's `Delete` function. This is the similar to AWS CloudFormation's [Retain DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

## New workflows enabled

This feature enables a number of new workflows with Pulumi.

### Supporting data storage policies

Using this new feature it is now possible to uncouple resource lifecycles from deployment cycles. This can be especially useful to teams with policy around data and storage. For example your company may require that all S3 storage is backed up and retained for some amount of time. Using `RetainOnDelete` you can ensure that the S3 buckets that Pulumi creates aren't deleted by Pulumi, leaving the data alive for your storage policy team to backup and then delete when no longer required.

### Supporting shared resources

Another workflow this option enables is the ability to manage externally owned resources via Pulumi deployments. You may have an external long lived resource that you want to temporarily manage via a Pulumi program, but then relinquish back to the external owner rather than deleting when you're finished with it.

Using a combination of [import](https://www.pulumi.com/docs/guides/adopting/import/) and `RetainOnDelete` you can bring a resource under management and then relinquish it back to the external owner.

### Working around provider issues

Although it isn't really a workflow, `RetainOnDelete` can also be used to work around some provider issues. Some providers may fail to refresh and detect that a resource is now deleted, leading Pulumi to issue a delete call to a resource that no longer exists. While you could always manually edit your state file to resolve cases like this, `RetainOnDelete` give you the option to fix this via program changes instead. Simply mark the faulty resource with `RetainOnDelete`, run `pulumi up` to apply the mark and then delete the resource from your program and run `pulumi up` again. The engine will cleanly delete the resource from your state file without communicating with the faulty provider.

## Using retain on delete

Setting retain on delete is done via a resource option. The following example builds two AWS S3 bucket objects, with one used for logging which will not be deleted by Pulumi.

```typescript
import * as pulumi from "@pulumi/pulumi";
import { s3 } from "@pulumi/aws";

const logBucket = new aws.s3.Bucket("logBucket", {
    acl: "log-delivery-write"
}, {
    retainOnDelete: true
});
const bucket = new aws.s3.Bucket("bucket", {
    acl: "private",
    loggings: [{
        targetBucket: logBucket.id,
        targetPrefix: "log/",
    }],
});
```

Read more about retain on delete in our [docs]({{< relref "docs/intro/concepts/resources/options/retainOnDelete" >}}). Let us know how you get on with this new feature at our community [Slack](https://slack.pulumi.com/)!
