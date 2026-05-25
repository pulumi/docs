---
title: Automating AWS S3 File Expiration with Pulumi
meta_desc: "Automate S3 file expiration with lifecycle rules. Expire, transition to IA or Glacier, abort multipart uploads, and manage versions, all with Pulumi."
meta_image: /images/what-is/guide-to-automating-file-expiration-in-aws-s3-meta.png
type: what-is
page_title: Automate AWS S3 File Expiration with Pulumi
authors: ["james-denyer"]
---

**S3 Lifecycle rules let you automate what happens to objects in a bucket as they age: delete them after a set number of days, move them to a cheaper storage class, expire old versions, or clean up incomplete multipart uploads.** Lifecycle rules attach to the bucket, evaluate once per day, and run without any application code or scheduled jobs. With Pulumi's [`aws.s3.BucketLifecycleConfigurationV2`](/registry/packages/aws/api-docs/s3/bucketlifecycleconfigurationv2/) resource, you can manage those rules as code in TypeScript, Python, Go, C#, Java, or YAML.

In this guide, we'll cover:

* How S3 Lifecycle rules work
* What you can automate
* Storage class transition rules and minimum durations
* A working Pulumi TypeScript example
* Configuration via the console and CLI
* Verifying lifecycle behavior
* Frequently asked questions

## How S3 Lifecycle rules work

A lifecycle configuration is a set of rules attached to a bucket. Each rule has:

* **A filter** — applied by prefix, object tag, object size, or "all objects."
* **One or more actions** — expire, transition, abort multipart, expire delete markers, or transition non-current versions.
* **An age threshold** — number of days after creation, or a specific date.

S3 evaluates rules once per day. The action is asynchronous — an object marked for deletion may take a few hours to disappear after the day count is met, and AWS does not bill for storage past the expiration day. You're not charged for the transition or expiration evaluation itself, but each [`PUT` transition to IA, Glacier, or Deep Archive](https://aws.amazon.com/s3/pricing/) does incur a per-object request fee, which matters for buckets with millions of small objects.

## What you can automate

S3 Lifecycle supports five common actions, often combined in one rule:

1. **Expire current versions.** Delete objects (or insert delete markers in a versioned bucket) after N days.
1. **Transition to a cheaper storage class.** Move objects from Standard to Standard-IA, Intelligent-Tiering, Glacier Instant Retrieval, Glacier Flexible Retrieval, or Glacier Deep Archive based on age.
1. **Abort incomplete multipart uploads.** Clean up the parts of uploads that never finished — a hidden cost in many older buckets.
1. **Expire non-current versions.** In a versioned bucket, delete old versions of objects after N days.
1. **Expire delete markers.** Remove orphaned delete markers left behind when all non-current versions of an object have been expired.

## Storage class transition rules and minimum durations

S3 enforces minimums on how soon you can transition objects, because cheaper tiers have higher retrieval costs and are designed for longer retention.

| Storage class | Minimum age before transition | Use case |
|---|---|---|
| Standard-IA | 30 days | Infrequently accessed data still needing fast retrieval |
| One Zone-IA | 30 days | Same, but only one Availability Zone (lower durability) |
| Intelligent-Tiering | None | AWS auto-tiers based on access patterns |
| Glacier Instant Retrieval | 90 days | Archive with millisecond access |
| Glacier Flexible Retrieval | 90 days | Archive with minutes-to-hours retrieval |
| Glacier Deep Archive | 180 days | Long-term archive, 12-hour retrieval |

Expiration itself has a minimum of 1 day. Smaller objects also have a minimum-size consideration: AWS does not move objects smaller than 128 KB to IA tiers because the per-object overhead would cost more than the savings.

## A working Pulumi example

The following TypeScript program creates an S3 bucket, enables versioning, and attaches a lifecycle configuration that transitions objects to Glacier after 90 days, deletes them after 365, expires non-current versions after 30, and cleans up incomplete multipart uploads after 7.

```typescript
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.BucketV2("documents", {});

new aws.s3.BucketVersioningV2("documents-versioning", {
    bucket: bucket.id,
    versioningConfiguration: {
        status: "Enabled",
    },
});

new aws.s3.BucketLifecycleConfigurationV2("documents-lifecycle", {
    bucket: bucket.id,
    rules: [{
        id: "archive-and-expire",
        status: "Enabled",
        filter: {
            prefix: "documents/",
        },
        transitions: [{
            days: 90,
            storageClass: "GLACIER",
        }],
        expiration: {
            days: 365,
        },
        noncurrentVersionExpiration: {
            noncurrentDays: 30,
        },
        abortIncompleteMultipartUpload: {
            daysAfterInitiation: 7,
        },
    }],
});

export const bucketName = bucket.id;
```

Deploy with `pulumi up`. From this point forward, every object uploaded under the `documents/` prefix moves to Glacier at 90 days, deletes at 365, leaves behind a delete marker that's cleaned up automatically, and never sits as an unfinished multipart upload for more than a week.

### Cross-account or multi-region patterns

If you operate buckets across multiple AWS accounts, configure the AWS provider with [`assumeRole`](/registry/packages/aws/api-docs/provider/) so the same Pulumi program can manage lifecycle rules in each one:

```typescript
import * as aws from "@pulumi/aws";

const archiveAccount = new aws.Provider("archive-account", {
    region: "us-east-1",
    assumeRole: {
        roleArn: "arn:aws:iam::123456789012:role/PulumiDeploymentRole",
        sessionName: "pulumi-lifecycle",
    },
});

const archiveBucket = new aws.s3.BucketV2("archive", {}, {
    provider: archiveAccount,
});
```

Pair this with [Pulumi ESC](/product/esc/) to keep the role's session credentials out of source control and CI logs.

## Configuration via the console and CLI

Lifecycle rules can also be created in the console or with the AWS CLI. Code-as-source is recommended for production, but the console and CLI are useful for one-off testing.

**Console.** Open the bucket → **Management** → **Lifecycle rules** → **Create lifecycle rule**. Choose the filter and actions, then **Create rule**.

**CLI.** Save the configuration as `lifecycle.json` and apply it:

```bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-bucket \
  --lifecycle-configuration file://lifecycle.json
```

Pulumi reconciles the same API call declaratively, which means you get review, audit, and rollback for free.

## Verifying lifecycle behavior

After deploying, confirm the rule is attached:

```bash
aws s3api get-bucket-lifecycle-configuration --bucket my-bucket
```

In the console, the **Management** tab of the bucket lists every rule with its status, filter, and actions. Note that lifecycle evaluations run once per day; an object created today will not transition or expire instantly even if the rule says "1 day." Allow up to 48 hours for the first transition.

For tagged-object rules, confirm the tag is applied to the objects you expect; an object with no tag will not match a tag-filtered rule and will be skipped entirely.

## Frequently asked questions

### How fast does an expiration rule take effect?

S3 evaluates lifecycle rules once per day, asynchronously. After the age threshold is met, the object is typically removed within 48 hours. You stop being billed for storage on the expiration day, regardless of when the actual deletion completes.

### Can I use lifecycle rules with object tags?

Yes. Filter on a single tag (`key=value`) or up to 1000 tags combined with prefixes. Tag-based rules are useful for mixed-content buckets where retention varies by classification, such as `retention=short` vs `retention=archive`.

### Do lifecycle rules cost money?

The rule evaluation is free. Storage-class transitions cost a per-request fee (see [S3 pricing](https://aws.amazon.com/s3/pricing/)). For very large objects this is negligible; for buckets with millions of small objects, transition costs can exceed the storage savings. Run the math before transitioning small objects to Glacier.

### What happens to versioned objects?

In a versioned bucket, `expiration` only marks current versions for deletion (it inserts a delete marker). Old versions persist until `noncurrentVersionExpiration` removes them, and the delete marker itself persists until `expiredObjectDeleteMarker` cleans it up. Without all three, versioned buckets can grow indefinitely.

### How is `BucketLifecycleConfigurationV2` different from `BucketLifecycleConfiguration`?

`V2` is the current API. It accepts the full lifecycle schema (filters, transitions, expirations, abort-multipart, non-current versions) in one resource. The original `BucketLifecycleConfiguration` is deprecated and missing newer fields — use `V2` for any new code.

### Can I have more than one lifecycle rule per bucket?

Yes. Up to 1000 rules per bucket. AWS evaluates them in order; if multiple rules target the same object, the most restrictive action wins. Keep rules narrowly scoped by prefix or tag to avoid surprises.

### Does versioning need to be enabled to use lifecycle rules?

No. Lifecycle works on both versioned and unversioned buckets. Versioning unlocks more actions (non-current expiration, delete-marker cleanup), but a simple expiration rule works fine on an unversioned bucket.

## Learn more

* [Pulumi AWS `BucketLifecycleConfigurationV2`](/registry/packages/aws/api-docs/s3/bucketlifecycleconfigurationv2/)
* [Pulumi AWS `BucketV2`](/registry/packages/aws/api-docs/s3/bucketv2/)
* [Pulumi ESC for AWS credentials](/docs/esc/environments/configuring-oidc/aws/)
* [AWS S3 Lifecycle documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
* [Pulumi Get Started guide](/docs/get-started/)
