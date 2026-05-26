---
title: Run 'aws s3 ls' using Dynamic Credentials
meta_desc: Run aws s3 ls with short-lived, OIDC-issued credentials from Pulumi ESC. No static AWS keys, scoped by IAM role, fully auditable in CloudTrail.
meta_image: /images/what-is/run-aws-s3-ls-with-dynamic-credentials-meta.png
type: what-is
page_title: Run 'aws s3 ls' using Dynamic Credentials
authors: ["diana-esteves"]
---

**This guide shows how to run `aws s3 ls` using short-lived AWS credentials brokered by [Pulumi ESC](/product/esc/) over OIDC, instead of long-lived `AKIA...` keys in `~/.aws/credentials`.** ESC exchanges a Pulumi-issued OIDC token for an AWS STS session, scoped to a specific IAM role, expiring automatically. `aws s3 ls` has two modes: with no argument it lists every bucket the caller's identity owns (`s3:ListAllMyBuckets`), and with a bucket name it lists objects inside that bucket (`s3:ListBucket`). The IAM permissions you grant the role determine which mode works.

In this article, we'll cover:

* Why dynamic credentials beat static IAM keys
* The two modes of `aws s3 ls` and the IAM permissions each one needs
* Prerequisites for this guide
* Step-by-step ESC setup with the `aws-login` provider
* Running `aws s3 ls` for buckets and for objects
* Verification and common errors
* Frequently asked questions

## Why dynamic credentials beat static IAM keys

Static IAM access keys sit in `~/.aws/credentials` until you delete them, are easily leaked into shell history or git, and carry every permission attached to the user. Dynamic credentials reverse all of that:

* **No long-lived secrets on disk.** Pulumi ESC issues a fresh `AccessKeyId`, `SecretAccessKey`, and `SessionToken` on every `esc run`. Nothing persists locally.
* **Scoped by IAM role.** The role's trust policy and attached policies define exactly what the session can do — read one bucket prefix, nothing else.
* **Time-bound.** Sessions expire after the ESC environment's `duration` (1 hour by default). A leaked token is useless almost immediately.
* **Auditable.** CloudTrail records the call under the assumed-role ARN with the `sessionName` you configured, so each S3 read is traceable to a specific Pulumi session.
* **Centrally rotated.** Update the IAM role or session duration in one ESC environment and every developer and CI job that consumes it picks up the change.

## What `aws s3 ls` does (and the IAM you need)

`aws s3 ls` has two modes, with different IAM requirements:

| Mode | Command | Min IAM permission |
|---|---|---|
| List all buckets in the account | `aws s3 ls` | `s3:ListAllMyBuckets` |
| List objects in a single bucket | `aws s3 ls s3://my-bucket/` | `s3:ListBucket` on the bucket |
| List objects under a prefix | `aws s3 ls s3://my-bucket/logs/` | `s3:ListBucket` with a `Condition` on `s3:prefix` |
| Recursive object listing | `aws s3 ls s3://my-bucket/ --recursive` | `s3:ListBucket` on the bucket |

Grant only the mode you need. `s3:ListAllMyBuckets` is account-wide and discloses every bucket name; `s3:ListBucket` on a single bucket is the least-privilege option for most scripts.

## Prerequisites

* An AWS account where you can create or update IAM roles
* The [Pulumi CLI](/docs/install/) and [Pulumi ESC CLI](/docs/install/esc/) installed
* A [Pulumi Cloud account](https://app.pulumi.com/signup) and access to an organization
* The [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed locally
* An IAM role with OIDC trust configured for Pulumi (see [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/)), with `s3:ListAllMyBuckets` and/or `s3:ListBucket` attached

## Step-by-step setup

### 1. Log in to Pulumi ESC

```bash
esc login
```

Follow the browser prompt or paste an access token from <https://app.pulumi.com/account/tokens>.

### 2. Configure OIDC between Pulumi and AWS

Follow the [Pulumi OIDC + AWS guide](/docs/esc/environments/configuring-oidc/aws/) to create an IAM role whose trust policy accepts a JWT from `api.pulumi.com/oidc`. Attach a policy granting at minimum the S3 listing permissions you need (see the table above). Note the role ARN.

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

## Run `aws s3 ls`

### List every bucket in the account

```bash
esc run <your-org>/<your-project>/<your-env> -- aws s3 ls
```

Expected output:

```bash
2025-04-12 09:14:02 my-app-logs
2025-05-01 17:33:48 my-app-backups
2025-05-09 11:02:11 pulumi-esc-demo
```

Each row is `creation-date creation-time bucket-name`. The list is account-wide; bucket-level policies do not filter it.

### List objects inside a single bucket

```bash
esc run <your-org>/<your-project>/<your-env> -- aws s3 ls s3://pulumi-esc-demo/
```

```bash
                           PRE logs/
2025-05-10 14:08:55       1024 helloWorld.txt
```

`PRE` indicates a prefix (a "folder" in S3's flat namespace). Append the prefix to drill deeper, or add `--recursive` to traverse the whole bucket.

## Verify in CloudTrail

S3 list operations show up in CloudTrail as `ListBuckets` (account-level) or `ListObjects` / `ListObjectsV2` (bucket-level). The `userIdentity.type` should be `AssumedRole` and the `arn` should include `assumed-role/<your-role>/pulumi-environments-session` — confirmation that the session came from ESC and not from a long-lived access key.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `AccessDenied` on `ListBuckets` | IAM role missing `s3:ListAllMyBuckets` | Add the permission to the role's policy, or list objects in a specific bucket instead |
| `AccessDenied` on `ListObjectsV2` | IAM role missing `s3:ListBucket` on the named bucket | Attach a statement allowing `s3:ListBucket` on `arn:aws:s3:::my-bucket` |
| `InvalidClientTokenId` | Stale local `AWS_*` env vars overriding ESC | Run `unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN` and retry |
| `ExpiredToken` | Session exceeded `duration` | Re-run; `esc run` fetches fresh credentials each invocation |
| `NoSuchBucket` | Bucket name typo or region mismatch | Confirm bucket exists in the account; add `--region` if non-default |
| `Unable to locate credentials` | `esc run` env vars not exported to the subprocess | Verify the `environmentVariables` block in the ESC YAML is at the top level |

## Frequently asked questions

### Why does `aws s3 ls` (with no bucket) fail when the bucket-level call works?

The two calls map to different IAM actions. `aws s3 ls` with no arguments calls `ListBuckets`, which requires `s3:ListAllMyBuckets` — an account-level permission. `aws s3 ls s3://bucket/` calls `ListObjectsV2`, which requires `s3:ListBucket` scoped to that bucket's ARN.

### Can I scope the role to a single bucket or prefix?

Yes. Attach a policy with `s3:ListBucket` on `arn:aws:s3:::my-bucket` and add a `Condition` on `s3:prefix` to restrict to specific paths. Pulumi ESC's role assumption respects any IAM restrictions you place on the role.

### How long are the credentials valid?

By default 1 hour, set by the `duration` field in the ESC environment. The maximum is bounded by the IAM role's `MaxSessionDuration` (1 hour for OIDC by default; raise it on the IAM role if needed).

### Can `aws s3 ls` page through millions of objects?

Yes. The AWS CLI handles pagination automatically. For very large buckets prefer `aws s3api list-objects-v2 --max-items` with manual pagination for finer control, or filter by `--prefix` to limit scope.

### Does this work in CI?

Yes — it's the recommended pattern. Replace `AWS_*` secrets in your CI configuration with a single `esc run <org>/<project>/<env> -- <command>` invocation. Pulumi's GitHub Action, GitLab integration, and the `esc open` command for shell exports all work the same way.

### How do I confirm the credentials really came from ESC?

Run `aws sts get-caller-identity` inside the same `esc run`. The returned `Arn` should be `assumed-role/<your-role>/pulumi-environments-session`, not a long-lived IAM user ARN. See [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/).

### What about S3 Block Public Access — does this affect `ls`?

No. Block Public Access controls public anonymous access, not authenticated calls from your IAM role. `aws s3 ls` operates as the assumed role and is unaffected by BPA.

## Learn more

* [Pulumi ESC product page](/product/esc/)
* [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/)
* [Run `aws s3 cp` with dynamic credentials](/what-is/run-aws-s3-cp-with-dynamic-credentials/)
* [Run `aws s3 sync` with dynamic credentials](/what-is/run-aws-s3-sync-with-dynamic-credentials/)
* [Resolve `Unable to locate credentials`](/what-is/resolve-unable-to-locate-credentials/)
* [Resolve `InvalidClientTokenId`](/what-is/resolve-list-buckets-invalid-client-token-id/)

[Join our community on Slack](https://slack.pulumi.com/) to discuss further, and let us know what you build.
