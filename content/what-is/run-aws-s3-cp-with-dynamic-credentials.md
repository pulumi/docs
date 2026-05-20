---
title: Run 'aws s3 cp' using Dynamic Credentials
meta_desc: Run aws s3 cp with short-lived, OIDC-issued credentials from Pulumi ESC. No static AWS keys, scoped by IAM role, fully auditable in CloudTrail.
meta_image: /images/what-is/run-aws-s3-cp-with-dynamic-credentials-meta.png
type: what-is
page_title: Run 'aws s3 cp' using Dynamic Credentials
authors: ["diana-esteves"]
---

**This guide shows how to run `aws s3 cp` using short-lived AWS credentials brokered by [Pulumi ESC](/product/esc/) over OIDC, instead of long-lived `AKIA...` keys in `~/.aws/credentials`.** Pulumi ESC exchanges a Pulumi-issued OIDC token for an AWS STS session, scoped to a specific IAM role, expiring automatically. `aws s3 cp` copies a single object or local file to or from S3, automatically using multipart upload for files larger than 8 MB. The IAM permissions you grant the role determine which directions of copy are allowed.

In this article, we'll cover:

* Why dynamic credentials beat static IAM keys
* The IAM permissions `aws s3 cp` needs (upload, download, copy between buckets)
* Prerequisites for this guide
* Step-by-step ESC setup with the `aws-login` provider
* Running `aws s3 cp` in both directions and across buckets
* Multipart upload, verification, and common errors
* Frequently asked questions

## Why dynamic credentials beat static IAM keys

Static IAM access keys persist in `~/.aws/credentials`, leak easily into git or shell history, and carry every permission attached to the user. Dynamic credentials reverse all of that:

* **No long-lived secrets on disk.** Pulumi ESC issues fresh `AccessKeyId`, `SecretAccessKey`, and `SessionToken` values on every `esc run`. Nothing persists locally.
* **Scoped by IAM role.** The IAM role's trust and permission policies define exactly which buckets and which actions the session can perform.
* **Time-bound.** Sessions expire after the ESC environment's `duration` (1 hour by default). A leaked token is useless almost immediately.
* **Auditable.** CloudTrail records each S3 operation under the assumed-role ARN with the `sessionName` you configured.
* **Centrally rotated.** Update the IAM role or session duration in one ESC environment and every developer and CI job that consumes it picks up the change.

## What `aws s3 cp` does (and the IAM you need)

`aws s3 cp` is the AWS CLI's S3 copy primitive. It supports three directional patterns:

| Direction | Example | Min IAM permissions |
|---|---|---|
| Local → S3 (upload) | `aws s3 cp ./file.txt s3://bucket/key` | `s3:PutObject` on the destination |
| S3 → Local (download) | `aws s3 cp s3://bucket/key ./file.txt` | `s3:GetObject` on the source |
| S3 → S3 (copy) | `aws s3 cp s3://src/a s3://dst/a` | `s3:GetObject` on source, `s3:PutObject` on destination |
| Recursive (directory) | `aws s3 cp ./dir s3://bucket/prefix/ --recursive` | Above + `s3:ListBucket` |

Grant the role only the actions the script needs. For production, scope by bucket ARN and prefer per-prefix `Resource` ARNs over `arn:aws:s3:::*`.

## Prerequisites

* An AWS account where you can create or update IAM roles
* The [Pulumi CLI](/docs/install/) and [Pulumi ESC CLI](/docs/install/esc/) installed
* A [Pulumi Cloud account](https://app.pulumi.com/signup) and access to an organization
* The [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed locally
* An IAM role with OIDC trust configured for Pulumi (see [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/)), with the S3 permissions from the table above attached
* An existing S3 bucket you can read from or write to

## Step-by-step setup

### 1. Log in to Pulumi ESC

```bash
esc login
```

Follow the browser prompt or paste an access token from <https://app.pulumi.com/account/tokens>.

### 2. Configure OIDC between Pulumi and AWS

Follow the [Pulumi OIDC + AWS guide](/docs/esc/environments/configuring-oidc/aws/) to create an IAM role whose trust policy accepts a JWT from `api.pulumi.com/oidc`. Attach a policy granting the S3 permissions you need. Note the role ARN.

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

## Run `aws s3 cp`

### Upload a local file to S3

```bash
echo "hello pulumi" > test.txt
esc run <your-org>/<your-project>/<your-env> -- \
    aws s3 cp test.txt s3://<your-bucket>/test.txt
```

Expected output:

```bash
upload: ./test.txt to s3://your-bucket/test.txt
```

### Download an object from S3

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws s3 cp s3://<your-bucket>/test.txt downloaded.txt
```

### Copy between two S3 buckets

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws s3 cp s3://source-bucket/key s3://dest-bucket/key
```

S3-to-S3 copies happen server-side in the same region; the bytes do not transit your laptop.

### Recursive copy of a directory

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws s3 cp ./build s3://<your-bucket>/site/ --recursive
```

Use `--exclude` and `--include` filters for fine-grained control.

## Multipart upload for large files

For files larger than 8 MB (configurable via `aws configure set s3.multipart_threshold`), the AWS CLI automatically uploads in parts. Two things to know:

* **Session duration must outlast the upload.** A 1 GB upload over a slow network can outrun a 1-hour ESC `duration`. Either raise `duration` in the ESC environment (up to the IAM role's `MaxSessionDuration`) or pre-stage uploads with the [`s3:AbortMultipartUpload`](https://docs.aws.amazon.com/AmazonS3/latest/userguide/abort-mpu.html) permission so failed uploads can be retried.
* **Partial uploads accumulate cost.** Multipart uploads that never complete leave orphaned parts charged at the storage rate. Set a lifecycle rule on the bucket to clean up incomplete multipart uploads after N days.

## Verify the upload

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws s3 ls s3://<your-bucket>/
```

In CloudTrail the event appears as `PutObject` or `CopyObject` with `userIdentity.type=AssumedRole` and an `arn` containing `assumed-role/<your-role>/pulumi-environments-session` — confirmation the session came from ESC.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `AccessDenied` on `PutObject` | IAM role missing `s3:PutObject` on the bucket/prefix | Add the action to the role's policy, scoped to the destination ARN |
| `AccessDenied` on `GetObject` | IAM role missing `s3:GetObject` for the source object | Add the action, or use `s3:GetObject*` if dealing with versioned objects |
| `KMS.AccessDenied` | Bucket uses SSE-KMS and role can't decrypt | Grant `kms:Decrypt` (download) or `kms:GenerateDataKey` (upload) on the bucket's KMS key |
| `InvalidClientTokenId` | Stale local `AWS_*` env vars overriding ESC | Run `unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN` and retry |
| `ExpiredToken` (mid-upload) | Multipart upload outlived ESC `duration` | Raise `duration` in the ESC environment, or split the upload |
| `RequestTimeout` on large files | Slow network plus default multipart threshold | Tune `s3.multipart_chunksize`, or use `aws s3 cp` with `--storage-class STANDARD_IA` and retry |
| `NoSuchBucket` | Wrong bucket name or region | Confirm with `aws s3 ls`; add `--region` if the bucket is non-default |

## Frequently asked questions

### Does `aws s3 cp` work for S3-to-S3 copies across accounts?

Yes, but the source bucket policy must allow `s3:GetObject` to the role's ARN, and the destination policy must allow `s3:PutObject` plus `s3:PutObjectAcl` if you want the destination account to own the object. Cross-account copies always require explicit policy on both sides.

### How long are ESC-issued credentials valid?

By default 1 hour, set by the `duration` field in the ESC environment YAML. The maximum is bounded by the IAM role's `MaxSessionDuration` attribute. For long uploads, raise both.

### Can I use server-side encryption (SSE-KMS) with this setup?

Yes. Add the relevant `kms:Decrypt` (for downloads) and `kms:GenerateDataKey` (for uploads) actions to the IAM role and ensure the role's principal is allowed in the KMS key policy.

### Why is my upload slower than the AWS console suggests?

The default multipart chunk size is 8 MB and parallelism is 10. For high-bandwidth links tune `aws configure set default.s3.multipart_chunksize 64MB` and `default.s3.max_concurrent_requests 20`. These settings apply to the AWS CLI invoked under `esc run`.

### Does this work in CI?

Yes — this is the recommended pattern. Replace `AWS_*` secrets in your CI configuration with a single `esc run` invocation. The Pulumi GitHub Action and GitLab integration both support OIDC-issued credentials.

### How do I confirm the credentials really came from ESC?

Run `aws sts get-caller-identity` inside the same `esc run`. The returned `Arn` should start with `assumed-role/<your-role>/pulumi-environments-session`. See [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/).

### Should I use `aws s3 cp` or `aws s3 sync` for many files?

Use `cp --recursive` for one-time copies and `aws s3 sync` for repeated synchronization where only changed files need to move. `sync` uses size and modification time to decide what to transfer; `cp --recursive` re-uploads everything. See [Run `aws s3 sync` with dynamic credentials](/what-is/run-aws-s3-sync-with-dynamic-credentials/).

## Learn more

* [Pulumi ESC product page](/product/esc/)
* [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [Run `aws s3 ls` with dynamic credentials](/what-is/run-aws-s3-ls-with-dynamic-credentials/)
* [Run `aws s3 sync` with dynamic credentials](/what-is/run-aws-s3-sync-with-dynamic-credentials/)
* [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/)
* [Resolve `Unable to locate credentials`](/what-is/resolve-unable-to-locate-credentials/)
* [Resolve `ExpiredToken`](/what-is/resolve-list-buckets-expired-token/)

[Join our community on Slack](https://slack.pulumi.com/) to discuss further, and let us know what you build.
