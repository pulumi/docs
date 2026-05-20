---
title: Run 'aws s3 sync' with Dynamic Credentials
meta_desc: Run aws s3 sync with short-lived, OIDC-issued credentials from Pulumi ESC. No static AWS keys, scoped by IAM role, fully auditable in CloudTrail.
meta_image: /images/what-is/run-aws-s3-sync-with-dynamic-credentials-meta.png
type: what-is
page_title: Run 'aws s3 sync' with Dynamic Credentials
authors: ["diana-esteves"]
---

**This guide shows how to run `aws s3 sync` using short-lived AWS credentials brokered by [Pulumi ESC](/product/esc/) over OIDC, instead of long-lived `AKIA...` keys in `~/.aws/credentials`.** Pulumi ESC exchanges a Pulumi-issued OIDC token for an AWS STS session, scoped to a specific IAM role, expiring automatically. `aws s3 sync` performs incremental, one-way synchronization between a local directory and an S3 prefix (or between two S3 prefixes), using file size and modification time to decide what to transfer. The IAM permissions you grant the role determine which directions of sync are allowed.

In this article, we'll cover:

* Why dynamic credentials beat static IAM keys
* How `aws s3 sync` decides what to transfer
* The IAM permissions sync needs (upload, download, bucket-to-bucket)
* Prerequisites for this guide
* Step-by-step ESC setup with the `aws-login` provider
* Running `aws s3 sync` in both directions
* Common errors and FAQ

## Why dynamic credentials beat static IAM keys

Static IAM access keys persist in `~/.aws/credentials` until you delete them, leak easily into git or shell history, and carry every permission attached to the user. Dynamic credentials reverse all of that:

* **No long-lived secrets on disk.** Pulumi ESC issues a fresh `AccessKeyId`, `SecretAccessKey`, and `SessionToken` on every `esc run`. Nothing persists locally.
* **Scoped by IAM role.** The role's trust and permission policies define exactly which buckets the session can read or write.
* **Time-bound.** Sessions expire after the ESC environment's `duration` (1 hour by default). A leaked token is useless almost immediately.
* **Auditable.** CloudTrail records each S3 operation under the assumed-role ARN with the `sessionName` you configured.
* **Centrally rotated.** Update the IAM role or session duration in one ESC environment and every developer and CI job that consumes it picks up the change.

## How `aws s3 sync` decides what to transfer

`aws s3 sync` compares source and destination by **file size** and **last-modified time** — not by content hash. An object is copied when:

* It exists in the source but not the destination, **or**
* The source object's size differs from the destination's, **or**
* The source object's last-modified time is **newer** than the destination's.

Use `--exact-timestamps` to also re-upload files whose timestamps differ even by a second (useful when downloading; the AWS CLI's default treats older-source-than-destination as no-op). `--delete` removes objects from the destination that no longer exist in the source — be careful with this flag in production.

## What `aws s3 sync` does (and the IAM you need)

| Direction | Example | Min IAM permissions |
|---|---|---|
| Local → S3 | `aws s3 sync ./dir s3://bucket/prefix/` | `s3:PutObject`, `s3:ListBucket` |
| S3 → Local | `aws s3 sync s3://bucket/prefix/ ./dir` | `s3:GetObject`, `s3:ListBucket` |
| S3 → S3 | `aws s3 sync s3://src/ s3://dst/` | `s3:GetObject` on source, `s3:PutObject` on destination, `s3:ListBucket` on both |
| With `--delete` | `... --delete` | Above + `s3:DeleteObject` on the destination |

`s3:ListBucket` is required for sync to enumerate objects on both sides. Scope it by bucket ARN, and add a `Condition` on `s3:prefix` for least privilege.

## Prerequisites

* An AWS account where you can create or update IAM roles
* The [Pulumi CLI](/docs/install/) and [Pulumi ESC CLI](/docs/install/esc/) installed
* A [Pulumi Cloud account](https://app.pulumi.com/signup) and access to an organization
* The [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed locally
* An IAM role with OIDC trust configured for Pulumi (see [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/)), with the S3 permissions from the table above attached
* An existing S3 bucket

## Step-by-step setup

### 1. Log in to Pulumi ESC

```bash
esc login
```

Follow the browser prompt or paste an access token from <https://app.pulumi.com/account/tokens>.

### 2. Configure OIDC between Pulumi and AWS

Follow the [Pulumi OIDC + AWS guide](/docs/esc/environments/configuring-oidc/aws/) to create an IAM role whose trust policy accepts a JWT from `api.pulumi.com/oidc`. Attach a policy granting the S3 sync permissions you need. Note the role ARN.

### 3. Create a new Pulumi ESC environment

In [Pulumi Cloud](https://app.pulumi.com/), open your organization, click **Environments**, then **Create environment**. Name it something like `aws-prod-env`.

### 4. Add the `aws-login` provider to the environment

Paste the following YAML, replacing `<your-oidc-iam-role-arn>`:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: <your-oidc-iam-role-arn>
          sessionName: pulumi-environments-session
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

The `fn::open::aws-login` function exchanges the Pulumi-issued OIDC token for AWS STS credentials. The `environmentVariables` block exposes them to any subprocess `esc run` starts.

### 5. Confirm there are no static credentials on disk

```bash
aws configure list
```

You should see `<not set>` for `access_key` and `secret_key`. This guarantees the next step uses ESC-issued credentials.

## Run `aws s3 sync`

### Upload a local directory to S3

```bash
mkdir my-local-dir
echo "hello pulumi" > my-local-dir/helloWorld.txt

esc run <your-org>/<your-project>/<your-env> -- \
    aws s3 sync ./my-local-dir/ s3://<your-bucket>/ --region <aws-region>
```

Expected output:

```bash
upload: my-local-dir/helloWorld.txt to s3://your-bucket/helloWorld.txt
```

Re-run the same command and you'll see no output — sync skipped the file because size and mtime match.

### Download an S3 prefix to local

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws s3 sync s3://<your-bucket>/ ./my-local-dir/
```

### Sync between two S3 buckets

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws s3 sync s3://source-bucket/prefix/ s3://dest-bucket/prefix/
```

S3-to-S3 sync executes server-side `CopyObject` calls; bytes do not transit your laptop.

### Mirror with `--delete`

To make the destination an exact mirror of the source (deleting anything in the destination that doesn't exist in the source):

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws s3 sync ./dist s3://<your-bucket>/ --delete
```

The IAM role needs `s3:DeleteObject` on the destination for this to succeed.

## Verify in CloudTrail

In CloudTrail the events appear as `PutObject` (uploads), `GetObject` (downloads), `CopyObject` (S3-to-S3), or `DeleteObject` (`--delete`), each with `userIdentity.type=AssumedRole` and an `arn` containing `assumed-role/<your-role>/pulumi-environments-session`.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `AccessDenied` on `ListObjects` | IAM role missing `s3:ListBucket` | Add the action, scoped to the bucket ARN |
| `AccessDenied` on `PutObject` / `GetObject` | Role missing the matching object action | Add `s3:PutObject` or `s3:GetObject` on the prefix or bucket |
| `AccessDenied` on `DeleteObject` (`--delete`) | Role lacks `s3:DeleteObject` | Add the action — and double-check the intent of `--delete` |
| `KMS.AccessDenied` | Bucket uses SSE-KMS and role can't decrypt or wrap | Grant `kms:Decrypt` (download) or `kms:GenerateDataKey` (upload) on the bucket's KMS key |
| `InvalidClientTokenId` | Stale local `AWS_*` env vars overriding ESC | Run `unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN` and retry |
| `ExpiredToken` mid-sync | Session expired during a long sync | Raise `duration` in the ESC environment, or chunk the work |
| Files re-uploading unnecessarily | mtime drift between local fs and S3 | Use `--size-only`, or `--exact-timestamps` for downloads |

## Frequently asked questions

### Does `aws s3 sync` check file content?

No. It compares **size** and **last-modified time** only. Two different files with the same size and mtime will not be detected as different. For content-aware sync use `--size-only` plus an ETag check, or a tool like `rclone` that supports hashes.

### Why does `aws s3 sync` keep re-uploading the same files?

The local filesystem's mtime is newer than the S3 object's. This happens after `git clone` (which sets mtimes to checkout time), after build steps, or on file systems with lower mtime resolution than S3. Use `--size-only` to skip the timestamp check.

### Is `--delete` dangerous?

Yes — treat it like `rm -rf`. It deletes any object in the destination that is not in the source. Always run a dry run first with `--dryrun`, and never combine `--delete` with a typo'd source path.

### How does sync handle large files?

Files above the multipart threshold (8 MB by default) upload in parallel parts. If an upload fails partway, the next sync run will re-upload. Set a lifecycle rule on the bucket to abort incomplete multipart uploads after a few days to avoid charges for orphaned parts.

### How long are ESC-issued credentials valid?

By default 1 hour, set by the `duration` field in the ESC environment YAML. The maximum is bounded by the IAM role's `MaxSessionDuration` attribute (1 hour for OIDC by default). For multi-hour syncs raise both.

### Can I sync to a bucket in a different region or account?

Yes for both. Use `--source-region` and `--region` to disambiguate. For cross-account, the source bucket policy must allow `s3:GetObject` and `s3:ListBucket` to the role's ARN, and the destination policy must allow `s3:PutObject` (and optionally `s3:PutObjectAcl` for destination-account ownership).

### How do I confirm the credentials really came from ESC?

Run `aws sts get-caller-identity` inside the same `esc run`. The returned `Arn` should be `assumed-role/<your-role>/pulumi-environments-session`. See [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/).

## Learn more

* [Pulumi ESC product page](/product/esc/)
* [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [Run `aws s3 cp` with dynamic credentials](/what-is/run-aws-s3-cp-with-dynamic-credentials/)
* [Run `aws s3 ls` with dynamic credentials](/what-is/run-aws-s3-ls-with-dynamic-credentials/)
* [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/)
* [Resolve `Unable to locate credentials`](/what-is/resolve-unable-to-locate-credentials/)
* [Resolve `ExpiredToken`](/what-is/resolve-list-buckets-expired-token/)

[Join our community on Slack](https://slack.pulumi.com/) to discuss further, and let us know what you build.
