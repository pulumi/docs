---
title: Run 'aws lambda list-functions' with Dynamic Credentials
meta_desc: Run aws lambda list-functions with short-lived, OIDC-issued credentials from Pulumi ESC. No static AWS keys, scoped by IAM role, auditable in CloudTrail.
meta_image: /images/what-is/run-aws-lambda-list-functions-with-dynamic-credentials-meta.png
type: what-is
page_title: Run 'aws lambda list-functions' with Dynamic Credentials
authors: ["diana-esteves"]
---

**This guide shows how to run `aws lambda list-functions` using short-lived AWS credentials brokered by [Pulumi ESC](/product/esc/) over OIDC, instead of long-lived `AKIA...` keys in `~/.aws/credentials`.** Pulumi ESC exchanges a Pulumi-issued OIDC token for an AWS STS session, scoped to a specific IAM role, expiring automatically. `aws lambda list-functions` enumerates Lambda functions in a single region and returns their ARNs, runtimes, memory sizes, and configuration metadata. The result is per-region, paginated, and gated by a single IAM permission: `lambda:ListFunctions`.

In this article, we'll cover:

* Why dynamic credentials beat static IAM keys
* What `aws lambda list-functions` returns and the IAM it needs
* Prerequisites for this guide
* Step-by-step ESC setup with the `aws-login` provider
* Running `aws lambda list-functions` and paginating across regions
* Verification, common errors, and FAQ

## Why dynamic credentials beat static IAM keys

Static IAM access keys persist in `~/.aws/credentials`, leak easily, and carry every permission attached to the user. Dynamic credentials reverse all of that:

* **No long-lived secrets on disk.** Pulumi ESC issues a fresh `AccessKeyId`, `SecretAccessKey`, and `SessionToken` on every `esc run`. Nothing persists locally.
* **Scoped by IAM role.** The IAM role's trust policy and attached permissions define exactly what the session can do — read Lambda metadata, nothing else.
* **Time-bound.** Sessions expire after the ESC environment's `duration` (1 hour by default). A leaked token is useless almost immediately.
* **Auditable.** CloudTrail records the call under the assumed-role ARN with the `sessionName` you configured.
* **Centrally rotated.** Update the IAM role or session duration in one ESC environment and every developer and CI job that consumes it picks up the change.

## What `aws lambda list-functions` does (and the IAM you need)

`aws lambda list-functions` returns a JSON array of function metadata for a single region. Each entry includes `FunctionName`, `FunctionArn`, `Runtime`, `Role`, `Handler`, `CodeSize`, `MemorySize`, `Timeout`, and `LastModified`. The output does **not** include the function code or environment variables — those require `lambda:GetFunction`.

| Aspect | Detail |
|---|---|
| Min IAM permission | `lambda:ListFunctions` |
| Scope | **Per-region**; run once per region you care about |
| Pagination | Server-side; AWS CLI handles automatically (default 50 per page, `--max-items` to limit) |
| Read-only | Yes; no Lambda invocations triggered |
| Cross-account | Requires the destination account to allow the role's ARN in its IAM policy |

For least privilege, attach a policy with just `lambda:ListFunctions` and (optionally) `lambda:ListLayerVersions` if you also want layer metadata.

## Prerequisites

* An AWS account with one or more Lambda functions to enumerate
* The [Pulumi CLI](/docs/install/) and [Pulumi ESC CLI](/docs/install/esc/) installed
* A [Pulumi Cloud account](https://app.pulumi.com/signup) and access to an organization
* The [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed locally
* An IAM role with OIDC trust configured for Pulumi (see [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/)), with `lambda:ListFunctions` attached

## Step-by-step setup

### 1. Log in to Pulumi ESC

```bash
esc login
```

Follow the browser prompt or paste an access token from <https://app.pulumi.com/account/tokens>.

### 2. Configure OIDC between Pulumi and AWS

Follow the [Pulumi OIDC + AWS guide](/docs/esc/environments/configuring-oidc/aws/) to create an IAM role whose trust policy accepts a JWT from `api.pulumi.com/oidc`. Attach a policy with `lambda:ListFunctions`. Note the role ARN.

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

## Run `aws lambda list-functions`

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws lambda list-functions --region <aws-region>
```

Expected output:

```json
{
    "Functions": [
        {
            "FunctionName": "my-api-handler",
            "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-api-handler",
            "Runtime": "nodejs20.x",
            "Role": "arn:aws:iam::123456789012:role/my-api-handler-role",
            "Handler": "index.handler",
            "CodeSize": 1024,
            "MemorySize": 256,
            "Timeout": 30,
            "LastModified": "2025-05-09T11:02:11.000+0000"
        }
    ]
}
```

### Filter the output with `--query`

Use JMESPath to extract only what you need:

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws lambda list-functions --region us-west-2 \
    --query 'Functions[].[FunctionName,Runtime,MemorySize]' --output table
```

### Paginate across many functions

The AWS CLI paginates automatically. For accounts with hundreds of functions use `--max-items` and `--starting-token` for manual control:

```bash
esc run <your-org>/<your-project>/<your-env> -- \
    aws lambda list-functions --region us-west-2 --max-items 50
```

### List functions across all regions

`list-functions` is per-region. To enumerate every region, loop:

```bash
for region in $(aws ec2 describe-regions --query 'Regions[].RegionName' --output text); do
    echo "== $region =="
    esc run <your-org>/<your-project>/<your-env> -- \
        aws lambda list-functions --region "$region" \
        --query 'Functions[].FunctionName' --output text
done
```

## Verify in CloudTrail

In CloudTrail the event appears as `ListFunctions20150331` with `userIdentity.type=AssumedRole` and an `arn` containing `assumed-role/<your-role>/pulumi-environments-session` — confirmation the session came from ESC.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `AccessDeniedException` | IAM role missing `lambda:ListFunctions` | Add the permission to the role's policy |
| `InvalidClientTokenId` | Stale local `AWS_*` env vars overriding ESC | Run `unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN` and retry |
| `ExpiredToken` | Session exceeded `duration` | Re-run; `esc run` fetches fresh credentials each invocation |
| Empty `Functions: []` | Wrong region — Lambda is regional | Confirm with `--region` or loop across regions |
| `EndpointConnectionError` | Region disabled in account | Enable the region or pick another |
| `Unable to locate credentials` | `esc run` env vars not exported to the subprocess | Verify the `environmentVariables` block in the ESC YAML is at the top level |

## Frequently asked questions

### Is `aws lambda list-functions` global or regional?

Regional. Each Lambda function lives in a single AWS region, and `ListFunctions` only returns functions from the region in the API call. To inventory every region, iterate over `aws ec2 describe-regions` (see the example above).

### What's the minimum IAM permission?

`lambda:ListFunctions`. That single action is enough to enumerate all functions and their basic metadata in the region. Function code and environment variables require `lambda:GetFunction` and `lambda:GetFunctionConfiguration` respectively — keep those off the role if you only need an inventory.

### How does pagination work?

The AWS CLI transparently follows the `NextMarker` pointer in each response, so `aws lambda list-functions` returns the complete set by default. Override with `--max-items` to cap the number of items returned, and `--starting-token` to resume from a previous run.

### Can I see functions in other AWS accounts?

Only if those accounts grant your role explicit `lambda:ListFunctions` via a resource-based policy or AssumeRole chain. Cross-account Lambda inventory typically uses a delegated read-only role per account; Pulumi ESC handles the role assumption regardless.

### How long are ESC-issued credentials valid?

By default 1 hour, set by the `duration` field in the ESC environment YAML. The maximum is bounded by the IAM role's `MaxSessionDuration` attribute (1 hour for OIDC by default; raise it on the IAM role if needed).

### Does this work in CI/CD?

Yes — this is the recommended pattern. Replace `AWS_*` secrets in your CI configuration with a single `esc run` invocation. The Pulumi GitHub Action, GitLab integration, and `esc open` for shell exports all work the same way.

### How do I confirm the credentials really came from ESC?

Run `aws sts get-caller-identity` inside the same `esc run`. The returned `Arn` should be `assumed-role/<your-role>/pulumi-environments-session`. See [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/).

## Learn more

* [Pulumi ESC product page](/product/esc/)
* [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/)
* [Run `aws ec2 describe-instances` with dynamic credentials](/what-is/run-aws-ec2-describe-instances-with-dynamic-credentials/)
* [Run `aws iam list-users` with dynamic credentials](/what-is/run-aws-iam-list-users-with-dynamic-credentials/)
* [Resolve `Unable to locate credentials`](/what-is/resolve-unable-to-locate-credentials/)
* [Resolve `InvalidClientTokenId`](/what-is/resolve-list-buckets-invalid-client-token-id/)

[Join our community on Slack](https://slack.pulumi.com/) to discuss further, and let us know what you build.
