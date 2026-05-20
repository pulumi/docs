---
title: Run 'aws iam list-users' using Dynamic Credentials
meta_desc: "Run 'aws iam list-users' with short-lived, OIDC-scoped credentials brokered by Pulumi ESC. No static IAM keys, least-privilege role, fully auditable."
meta_image: /images/what-is/run-aws-iam-list-users-with-dynamic-credentials-meta.png
type: what-is
page_title: Run 'aws iam list-users' using Dynamic Credentials
authors: ["diana-esteves"]
---

**This guide shows you how to run `aws iam list-users` with dynamic, short-lived AWS credentials brokered by [Pulumi ESC](/product/esc/) over OIDC, instead of long-lived `aws_access_key_id` / `aws_secret_access_key` pairs on disk.** Because IAM enumerates principals and trust relationships across the entire account, the role you use should be tightly scoped — read-only IAM, with no other actions attached. Dynamic credentials are issued by AWS STS at the moment the command runs, scoped to that single role, time-bound to the role's session duration, and visible end-to-end in CloudTrail. You'll need the Pulumi CLI, the [`esc` CLI](/docs/install/esc/), a Pulumi Cloud account, and an AWS IAM role configured to trust Pulumi as an OIDC provider.

In this article, we'll cover:

- Why dynamic credentials beat static AWS keys for sensitive IAM reads
- Prerequisites for the `esc run` workflow
- How to create an ESC environment with the `aws-login` provider
- The `aws iam list-users` invocation, explained flag-by-flag
- How to verify the call ran with assumed-role credentials
- Common errors and how to fix them
- FAQs on least privilege, CI use, multi-account, and `aws-vault` differences

## Why dynamic credentials beat static AWS keys

- **No `aws_access_key_id` on disk.** Nothing to leak from `~/.aws/credentials`, a developer laptop, a CI runner cache, or a screenshot in Slack. Especially important for IAM, which exposes the account's identity surface.
- **Scoped to one IAM role.** Keep this role's policy at `iam:ListUsers`, `iam:GetUser`, and the other read-only actions you actually need. No `iam:*` and no write actions.
- **Time-bound by STS.** Sessions expire on the `duration` you configure (default 1 hour). An exfiltrated session token is useless within the hour.
- **Auditable in CloudTrail.** Every `ListUsers` event carries the assumed-role principal and a session name you control. Pair with CloudTrail alerts on the role for high-signal detection of misuse.
- **One source of truth.** The ESC environment defines the role and trust policy once; every teammate, CI job, and script gets the same credentials, never their own copy.

## Least privilege matters more for IAM

IAM reads enumerate the security perimeter of the account. Use a dedicated read-only role for this workflow:

- Do not attach `AdministratorAccess` or any `iam:*` write actions to the role.
- Use a separate ESC environment from any role that can write. Reviewers can then audit the YAML to confirm scope.
- Consider an MFA condition on the trust policy if the OIDC flow is initiated by humans rather than CI.
- Forward CloudTrail to a centralized log account and alert on unexpected `AssumeRoleWithWebIdentity` events naming this role.

## Prerequisites

- A [Pulumi Cloud](https://app.pulumi.com/signin) account and an organization you can create environments in.
- The Pulumi CLI and the [ESC CLI](/docs/install/esc/) installed and authenticated (`esc login`).
- An AWS account with permission to create and update IAM roles.
- An IAM role with `iam:ListUsers` (the minimum), and a trust policy that allows Pulumi's OIDC issuer to assume it. Use the [Pulumi + AWS OIDC guide](/docs/esc/guides/configuring-oidc/aws/) to set it up.
- The AWS CLI v2 installed.

## Step-by-step: set up dynamic credentials for IAM read

### 1. Configure the OIDC trust between Pulumi and AWS

Follow the [configuring OIDC between Pulumi and AWS guide](/docs/esc/guides/configuring-oidc/aws/) to create an IAM role whose trust policy accepts Pulumi's OIDC issuer. Note the role's ARN.

### 2. Create a Pulumi ESC environment

```bash
$ esc env init <your-pulumi-org>/<your-project>/aws-iam-read
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

## Run `aws iam list-users` with dynamic credentials

```bash
$ esc run <your-pulumi-org>/<your-project>/aws-iam-read -- aws iam list-users
```

What each flag does:

- `esc run <env> --` opens the named ESC environment, assumes the IAM role, and injects the short-lived credentials as environment variables for the command that follows.
- No `--region` is required: IAM is a global service in the standard partition (`aws`), and the CLI targets `us-east-1` by default. In the `aws-us-gov` or `aws-cn` partitions, set `AWS_REGION` accordingly.

A successful response looks like:

```json
{
  "Users": [
    {
      "UserName": "alice",
      "UserId": "AIDAEXAMPLEUSERID1",
      "Arn": "arn:aws:iam::123456789012:user/alice",
      "CreateDate": "2025-08-14T17:42:11+00:00"
    }
  ]
}
```

For large accounts, paginate with `--max-items 50` and feed `--starting-token` from the previous response.

## Verify you used dynamic credentials

Run a `sts get-caller-identity` through the same environment and inspect the principal:

```bash
$ esc run <your-pulumi-org>/<your-project>/aws-iam-read -- aws sts get-caller-identity
{
  "UserId": "AROAEXAMPLE:pulumi-environments-session",
  "Account": "123456789012",
  "Arn": "arn:aws:sts::123456789012:assumed-role/pulumi-esc-oidc-iam-read/pulumi-environments-session"
}
```

The `assumed-role` ARN and the `pulumi-environments-session` suffix confirm you're using a role session, not an IAM user. The matching CloudTrail `ListUsers` event will show `userIdentity.type = AssumedRole` and the same session name.

## Common errors

| Error | Likely cause | Fix |
|---|---|---|
| `AccessDenied: not authorized to perform: sts:AssumeRoleWithWebIdentity` | IAM role trust policy does not allow Pulumi's OIDC issuer or your org's audience | Re-check the trust policy against the [Pulumi + AWS OIDC guide](/docs/esc/guides/configuring-oidc/aws/) |
| `AccessDenied: ... iam:ListUsers` | Role's identity policy lacks the action | Add `iam:ListUsers` (Resource: `*`) to the role |
| `InvalidClientTokenId` | The ESC env didn't inject credentials; you're hitting AWS with stale or empty keys | Confirm the `environmentVariables` block and that you invoked via `esc run --` ([more](/what-is/resolve-list-buckets-invalid-client-token-id/)) |
| `ExpiredToken` | Session lived past the configured `duration` | Re-run the command; `esc run` mints a fresh session each invocation ([more](/what-is/resolve-list-buckets-expired-token/)) |
| `Unable to locate credentials` | `esc run` was not used and no other AWS credential source is configured | Wrap the command in `esc run <env> --` ([more](/what-is/resolve-unable-to-locate-credentials/)) |

## Frequently asked questions

### Can I use `esc run` in CI to audit IAM users?

Yes — periodic least-privilege reviews are a strong fit. Set `PULUMI_ACCESS_TOKEN` on the runner and invoke `esc run <env> -- aws iam list-users` from a scheduled workflow. Pulumi's GitHub Actions, GitLab CI, and CircleCI integrations all support this pattern. Keep the role read-only.

### What is the minimum IAM permission the role needs?

`iam:ListUsers` and nothing else for plain enumeration. The action does not support resource-level constraints (it returns *all* users), so the policy resource must be `"*"`. If you want richer reports (`GetUser`, `ListAccessKeys`, `ListMFADevices`), add only the specific read actions you need — do not grant `iam:*`.

### Does this work with multiple AWS accounts?

Yes, and it's the recommended pattern for centralized IAM auditing. Create one ESC environment per account, each pointing at a read-only IAM role in that account. Use [environment imports](/docs/esc/environments/imports/) to compose a base "iam-read" environment with per-account overrides.

### Can I require MFA for this role?

Yes. Add a `Condition` block to the trust policy that requires `aws:MultiFactorAuthPresent` (for IAM-user-based assumption) or use OIDC subject conditions to restrict which Pulumi org or environment can assume the role. The OIDC `sub` claim is `pulumi:deploy:org:<org>:env:<env>` and can be matched with `StringEquals`.

### Do I still need static AWS keys for anything?

For local dev, CI, and one-off CLI work against AWS, no. Static keys are only needed by legacy tooling that can't be wrapped in `esc run` or that doesn't accept environment-variable credentials.

### How is this different from `aws-vault`?

`aws-vault` stores long-lived keys in your OS keychain and brokers temporary sessions locally. Pulumi ESC removes the long-lived key entirely: the trust is OIDC-based and lives in IAM, so no key is ever issued to a developer or runner. ESC also gives you centralized environments, secret aggregation from other providers, and audit logs across the team.

### How long can a session last?

Up to the role's `MaxSessionDuration` (default 1 hour, configurable up to 12 hours for non-chained roles). For sensitive IAM reads, prefer the default 1-hour window and have callers re-assume rather than extending the duration.

## Learn more

- [Pulumi ESC product page](/product/esc/)
- [Configuring OIDC between Pulumi and AWS](/docs/esc/guides/configuring-oidc/aws/)
- [`esc run` command reference](/docs/esc/cli/commands/esc_run/)
- Related dynamic-credentials guides:
  - [Run `aws sts get-caller-identity` with dynamic credentials](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/)
  - [Run `aws s3 ls` with dynamic credentials](/what-is/run-aws-s3-ls-with-dynamic-credentials/)
  - [Run `aws ec2 describe-instances` with dynamic credentials](/what-is/run-aws-ec2-describe-instances-with-dynamic-credentials/)
- Related error resolution: [`InvalidClientTokenId`](/what-is/resolve-list-buckets-invalid-client-token-id/), [`ExpiredToken`](/what-is/resolve-list-buckets-expired-token/), [`Unable to locate credentials`](/what-is/resolve-unable-to-locate-credentials/)
