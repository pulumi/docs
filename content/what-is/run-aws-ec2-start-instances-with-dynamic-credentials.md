---
title: Run 'aws ec2 start-instances' using Dynamic Credentials
meta_desc: "Start EC2 instances with 'aws ec2 start-instances' using short-lived, OIDC-scoped credentials brokered by Pulumi ESC. No static keys, fully auditable."
meta_image: /images/what-is/run-aws-ec2-start-instances-with-dynamic-credentials-meta.png
type: what-is
page_title: Run 'aws ec2 start-instances' using Dynamic Credentials
authors: ["diana-esteves"]
---

**This guide shows you how to run `aws ec2 start-instances` with dynamic, short-lived AWS credentials brokered by [Pulumi ESC](/product/esc/) over OIDC, instead of long-lived `aws_access_key_id` / `aws_secret_access_key` pairs on disk.** Dynamic credentials are issued by AWS STS at the moment the command runs, scoped to a single IAM role, time-bound to the role's session duration, and visible end-to-end in CloudTrail. You'll need the Pulumi CLI, the [`esc` CLI](/docs/install/esc/), a Pulumi Cloud account, and an AWS IAM role configured to trust Pulumi as an OIDC provider.

In this article, we'll cover:

- Why dynamic credentials beat static AWS keys for state-changing EC2 calls
- Prerequisites for the `esc run` workflow
- How to create an ESC environment with the `aws-login` provider
- The `aws ec2 start-instances` invocation, explained flag-by-flag
- How to verify the call ran with assumed-role credentials
- Common errors and how to fix them
- FAQs about CI use, multi-account, tag-scoped permissions, and `aws-vault` differences

## Why dynamic credentials beat static AWS keys

- **No `aws_access_key_id` on disk.** Nothing to leak from `~/.aws/credentials`, a developer laptop, a CI runner cache, or a screenshot in Slack.
- **Scoped to one IAM role.** The role's policy is the upper bound. For start/stop automation, scope to a tag like `aws:ResourceTag/Automation=true` so the session can only touch instances you've opted in.
- **Time-bound by STS.** Sessions expire on the `duration` you configure (default 1 hour). An exfiltrated session token is useless within the hour.
- **Auditable in CloudTrail.** Every `StartInstances` event carries the assumed-role principal and a session name you control, so you can prove which automation started which instance and when.
- **One source of truth.** The ESC environment defines the role and trust policy once; every teammate, CI job, and script gets the same credentials, never their own copy.

## Prerequisites

- A [Pulumi Cloud](https://app.pulumi.com/signin) account and an organization you can create environments in.
- The Pulumi CLI and the [ESC CLI](/docs/install/esc/) installed and authenticated (`esc login`).
- An AWS account with permission to create and update IAM roles.
- An IAM role with `ec2:StartInstances` and `ec2:DescribeInstances`, and a trust policy that allows Pulumi's OIDC issuer to assume it. Use the [Pulumi + AWS OIDC guide](/docs/esc/guides/configuring-oidc/aws/) to set it up.
- The AWS CLI v2 installed.
- One or more stopped EC2 instances whose IDs you know.

## Step-by-step: set up dynamic credentials for EC2 start

### 1. Configure the OIDC trust between Pulumi and AWS

Follow the [configuring OIDC between Pulumi and AWS guide](/docs/esc/guides/configuring-oidc/aws/) to create an IAM role whose trust policy accepts Pulumi's OIDC issuer. Note the role's ARN.

### 2. Create a Pulumi ESC environment

```bash
$ esc env init <your-pulumi-org>/<your-project>/aws-ec2-control
```

### 3. Add the `aws-login` provider to the environment

Open the environment in `esc env edit` (or in the Pulumi Cloud console) and paste the following, replacing `<your-oidc-iam-role-arn>` with the ARN from step 1:

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

The `fn::open::aws-login` provider performs the `AssumeRoleWithWebIdentity` call against AWS STS at runtime. The `environmentVariables` block exposes the resulting short-lived credentials to any process `esc run` invokes.

### 4. Confirm no static credentials are leaking in

```bash
$ aws configure list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key                <not set>             None    None
secret_key                <not set>             None    None
    region                <not set>             None    None
```

If `access_key` shows a value, unset `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_PROFILE`, or use a fresh shell. The point is to prove the next call cannot fall back to a long-lived key.

## Run `aws ec2 start-instances` with dynamic credentials

```bash
$ esc run <your-pulumi-org>/<your-project>/aws-ec2-control -- \
    aws ec2 start-instances \
      --instance-ids i-0123456789abcdef0 i-0fedcba9876543210 \
      --region <aws-region>
```

What each flag does:

- `esc run <env> --` opens the named ESC environment, assumes the IAM role, and injects the short-lived credentials as environment variables for the command that follows.
- `--instance-ids` is the space-separated list of instance IDs to start.
- `--region` picks the AWS region — EC2 is region-scoped, so the IDs must live in the region you query.

A successful response looks like:

```json
{
  "StartingInstances": [
    {
      "InstanceId": "i-0123456789abcdef0",
      "CurrentState": { "Code": 0, "Name": "pending" },
      "PreviousState": { "Code": 80, "Name": "stopped" }
    }
  ]
}
```

To wait until the instances are fully running before continuing a script:

```bash
$ esc run <your-pulumi-org>/<your-project>/aws-ec2-control -- \
    aws ec2 wait instance-running \
      --instance-ids i-0123456789abcdef0 \
      --region <aws-region>
```

## Verify you used dynamic credentials

Run a `sts get-caller-identity` through the same environment and inspect the principal:

```bash
$ esc run <your-pulumi-org>/<your-project>/aws-ec2-control -- aws sts get-caller-identity
{
  "UserId": "AROAEXAMPLE:pulumi-environments-session",
  "Account": "123456789012",
  "Arn": "arn:aws:sts::123456789012:assumed-role/pulumi-esc-oidc/pulumi-environments-session"
}
```

The `assumed-role` ARN and the `pulumi-environments-session` suffix confirm you're using a role session, not an IAM user. The matching CloudTrail `StartInstances` event will show `userIdentity.type = AssumedRole` and the same session name.

## Common errors

| Error | Likely cause | Fix |
|---|---|---|
| `AccessDenied: not authorized to perform: sts:AssumeRoleWithWebIdentity` | IAM role trust policy does not allow Pulumi's OIDC issuer or your org's audience | Re-check the trust policy against the [Pulumi + AWS OIDC guide](/docs/esc/guides/configuring-oidc/aws/) |
| `UnauthorizedOperation: ... ec2:StartInstances` | Role's identity policy lacks the action or the tag-scoped condition isn't met | Add `ec2:StartInstances` and confirm the instance carries the tags your policy expects |
| `InvalidInstanceID.NotFound` | The instance ID doesn't exist in this region or account | Double-check the region; the role session is bound to one account |
| `InvalidClientTokenId` | The ESC env didn't inject credentials; you're hitting AWS with stale or empty keys | Confirm the `environmentVariables` block and that you invoked via `esc run --` ([more](/what-is/resolve-list-buckets-invalid-client-token-id/)) |
| `ExpiredToken` | Session lived past the configured `duration` | Re-run the command; `esc run` mints a fresh session each invocation ([more](/what-is/resolve-list-buckets-expired-token/)) |
| `Unable to locate credentials` | `esc run` was not used and no other AWS credential source is configured | Wrap the command in `esc run <env> --` ([more](/what-is/resolve-unable-to-locate-credentials/)) |

## Frequently asked questions

### Can I use `esc run` in CI to start instances on a schedule?

Yes. Set `PULUMI_ACCESS_TOKEN` on the runner and invoke `esc run <env> -- aws ec2 start-instances ...` from a cron job or scheduled workflow. The runner needs no long-lived AWS credentials. Pulumi's GitHub Actions, GitLab CI, and CircleCI integrations all support this pattern.

### What is the minimum IAM permission the role needs?

`ec2:StartInstances` for the start action and `ec2:DescribeInstances` so the CLI can resolve and validate the IDs you pass. For least privilege, scope `StartInstances` with the `ec2:ResourceTag/<key>` condition so the session can only act on opted-in instances:

```json
{
  "Effect": "Allow",
  "Action": "ec2:StartInstances",
  "Resource": "arn:aws:ec2:*:*:instance/*",
  "Condition": { "StringEquals": { "aws:ResourceTag/Automation": "true" } }
}
```

### Does this work with multiple AWS accounts?

Yes. Create one ESC environment per account or use [environment imports](/docs/esc/environments/imports/) to compose a base environment with account-specific overrides. Each environment maps to one `roleArn`, so the credentials are always scoped to one account.

### Can I start instances in multiple regions in one command?

No — `start-instances` is a single-region call. Run one `esc run` per region, or loop through your regions in a script and pass `--region` each time. The role is assumed once per `esc run`.

### Do I still need static AWS keys for anything?

For local dev, CI, and one-off CLI work against AWS, no. Static keys are only needed by legacy tooling that can't be wrapped in `esc run` or that doesn't accept environment-variable credentials.

### How is this different from `aws-vault`?

`aws-vault` stores long-lived keys in your OS keychain and brokers temporary sessions locally. Pulumi ESC removes the long-lived key entirely: the trust is OIDC-based and lives in IAM, so no key is ever issued to a developer or runner. ESC also gives you centralized environments, secret aggregation from other providers, and audit logs across the team.

### How long can a session last?

Up to the role's `MaxSessionDuration` (default 1 hour, configurable up to 12 hours for non-chained roles). The `duration` field in the `aws-login` block requests the value; AWS enforces the cap.

## Learn more

- [Pulumi ESC product page](/product/esc/)
- [Configuring OIDC between Pulumi and AWS](/docs/esc/guides/configuring-oidc/aws/)
- [`esc run` command reference](/docs/esc/cli/commands/esc_run/)
- Related dynamic-credentials guides:
  - [Run `aws ec2 stop-instances` with dynamic credentials](/what-is/run-aws-ec2-stop-instances-with-dynamic-credentials/)
  - [Run `aws ec2 describe-instances` with dynamic credentials](/what-is/run-aws-ec2-describe-instances-with-dynamic-credentials/)
  - [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/)
- Related error resolution: [`InvalidClientTokenId`](/what-is/resolve-list-buckets-invalid-client-token-id/), [`ExpiredToken`](/what-is/resolve-list-buckets-expired-token/), [`Unable to locate credentials`](/what-is/resolve-unable-to-locate-credentials/)
