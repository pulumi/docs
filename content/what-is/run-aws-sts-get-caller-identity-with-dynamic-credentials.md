---
title: Run 'aws sts get-caller-identity' using Dynamic Credentials
meta_desc: Run aws sts get-caller-identity with short-lived, OIDC-issued credentials from Pulumi ESC. No static IAM keys, scoped by role, auditable in CloudTrail.
meta_image: /images/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials-meta.png
type: what-is
page_title: Run 'aws sts get-caller-identity' using Dynamic Credentials
authors: ["diana-esteves"]
---

**This guide shows how to run `aws sts get-caller-identity` using short-lived AWS credentials brokered by [Pulumi ESC](/product/esc/) over OIDC, instead of long-lived `AKIA...` keys in `~/.aws/credentials`.** The credentials are issued by AWS STS at the moment the command runs, scoped to a specific IAM role, expire automatically, and show up in CloudTrail as an assumed-role principal. `aws sts get-caller-identity` returns the account, user ID, and ARN of the calling identity. It requires no IAM permissions, which makes it the ideal first command to verify that your dynamic credential pipeline works end to end.

In this article, we'll cover:

* Why dynamic credentials beat static IAM keys
* Prerequisites for this guide
* Step-by-step ESC setup with the `aws-login` provider
* Running `aws sts get-caller-identity` through `esc run`
* Verifying the assumed-role principal in CloudTrail
* Common errors and how to fix them
* Frequently asked questions

## Why dynamic credentials beat static IAM keys

Static IAM access keys (`AKIA...` plus a secret) sit in `~/.aws/credentials` indefinitely, are easily leaked, and grant every permission attached to the IAM user. Dynamic credentials invert every one of those defaults:

* **No long-lived secrets on disk.** Pulumi ESC issues a fresh `AccessKeyId`, `SecretAccessKey`, and `SessionToken` on every `esc run`. Nothing lingers in `~/.aws/credentials`.
* **Scoped by IAM role.** The IAM role's trust policy and attached policies define exactly what the session can do. STS get-caller-identity itself needs no permissions, but the same plumbing enforces least privilege for every other command.
* **Time-bound.** Sessions expire after the duration in the ESC environment (1 hour by default, configurable up to the IAM role's `MaxSessionDuration`). A leaked token is useless once it expires.
* **Auditable.** CloudTrail records the call under the assumed-role ARN, with `sessionName` from the ESC environment, so it's clear which Pulumi org and user triggered the command.
* **Centrally rotated.** Updating the IAM role trust policy or session duration in one ESC environment immediately affects every developer and CI job that consumes it.

## Prerequisites

* An AWS account where you can create or update IAM roles
* The [Pulumi CLI](/docs/install/) and [Pulumi ESC CLI](/docs/install/esc/) installed
* A [Pulumi Cloud account](https://app.pulumi.com/signup) and access to an organization
* The [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed locally
* An IAM role with OIDC trust configured for Pulumi (see [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/))

For `aws sts get-caller-identity` specifically, the IAM role needs **no managed policies** — STS get-caller-identity is allowed for any authenticated principal. Use that to your advantage: this command is the cleanest way to confirm OIDC works before layering on real permissions.

## Step-by-step setup

### 1. Log in to Pulumi ESC

```bash
esc login
```

Follow the browser prompt or paste an access token from <https://app.pulumi.com/account/tokens>.

### 2. Configure OIDC between Pulumi and AWS

Follow the [Pulumi OIDC + AWS guide](/docs/esc/environments/configuring-oidc/aws/) to create an IAM role whose trust policy accepts a JWT from `api.pulumi.com/oidc`. Note the role ARN — you'll paste it into your ESC environment below.

### 3. Create a new Pulumi ESC environment

In [Pulumi Cloud](https://app.pulumi.com/), open your organization, click **Environments**, then **Create environment**. Name it something like `aws-prod-env`.

### 4. Add the `aws-login` provider to the environment

Replace the placeholder YAML in the editor with the following, substituting `<your-oidc-iam-role-arn>`:

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

The `fn::open::aws-login` function exchanges the Pulumi-issued OIDC token for AWS STS credentials. The `environmentVariables` block exposes them to any subprocess started by `esc run`.

### 5. Confirm there are no static credentials on disk

```bash
aws configure list
```

You should see `<not set>` for `access_key` and `secret_key`. This guarantees that the next step is using ESC-issued credentials and not something stale on the machine.

## Run `aws sts get-caller-identity`

```bash
esc run <your-org>/<your-project>/<your-env> -- aws sts get-caller-identity
```

Expected output:

```json
{
    "UserId": "AROAEXAMPLE12345:pulumi-environments-session",
    "Account": "123456789012",
    "Arn": "arn:aws:sts::123456789012:assumed-role/pulumi-esc-role/pulumi-environments-session"
}
```

Three things to notice in that response:

* **`Arn` starts with `assumed-role/`** — confirming you're not using static IAM user credentials.
* **The role name** matches the IAM role you set in the ESC environment.
* **The session name** (`pulumi-environments-session`) matches the `sessionName` field in your YAML — useful for filtering CloudTrail.

## Verify in CloudTrail

Within ~5 minutes the call appears in CloudTrail with `eventName=GetCallerIdentity` and a `userIdentity` block like:

```json
{
  "type": "AssumedRole",
  "principalId": "AROAEXAMPLE12345:pulumi-environments-session",
  "arn": "arn:aws:sts::123456789012:assumed-role/pulumi-esc-role/pulumi-environments-session",
  "sessionContext": {
    "sessionIssuer": {
      "type": "Role",
      "arn": "arn:aws:iam::123456789012:role/pulumi-esc-role"
    }
  }
}
```

That `AssumedRole` type is the signal an auditor wants to see: every call is tied to a specific IAM role and a specific session, not an anonymous long-lived access key.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `InvalidClientTokenId` | The ESC environment didn't issue credentials, or they were overridden by stale env vars | Run `unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN` and retry under `esc run` |
| `ExpiredToken` | Session exceeded `duration` (default 1h) | Re-run the command; `esc run` requests fresh credentials each invocation |
| `AccessDenied` on AssumeRoleWithWebIdentity | OIDC trust policy mismatch | Check `roleArn`, the trust policy's `sub` claim, and that the audience matches `api.pulumi.com` |
| `Unable to locate credentials` | `esc run` env vars not exported to the subprocess | Confirm the YAML's `environmentVariables` block uses `${aws.login.*}` references and is at the top level |
| `RegionDisabledException` | The account hasn't enabled the region for STS | Use the global STS endpoint or enable the region in the AWS console |

## Frequently asked questions

### What permissions does `aws sts get-caller-identity` require?

None. AWS explicitly allows any authenticated principal to call `GetCallerIdentity`, regardless of attached IAM policies. This is what makes it the canonical "am I authenticated, and as whom?" diagnostic.

### Why does the `Arn` look different from a normal IAM user ARN?

Because you're not signed in as an IAM user. The `assumed-role/<role-name>/<session-name>` format is how STS reports any principal that arrived via `AssumeRole`, `AssumeRoleWithWebIdentity`, or `AssumeRoleWithSAML` — including OIDC sessions issued by Pulumi ESC.

### How long do ESC-issued AWS credentials last?

By default, 1 hour, controlled by the `duration` field in the ESC environment. The maximum is bounded by the IAM role's `MaxSessionDuration` attribute (up to 12 hours for role chaining and 1 hour for OIDC by default).

### Can I use this in CI/CD instead of static `AWS_*` secrets?

Yes — that is the primary production use case. The Pulumi GitHub Action, GitLab integration, and `esc open` / `esc run` in any CI runner all work the same way. See the [esc-env-run-aws blog post](/blog/esc-env-run-aws/) and [Pulumi ESC docs](/docs/pulumi-cloud/esc/) for examples.

### How do I know the credentials came from ESC and not from `~/.aws/credentials`?

Run `aws configure list` outside of `esc run` and confirm `access_key` is `<not set>`. Inside `esc run`, the value will be reported with `Type=env`, indicating it came from environment variables injected by ESC.

### Why doesn't `aws sts get-caller-identity` need a region?

STS has a global endpoint (`sts.amazonaws.com`) plus regional endpoints. For OIDC `AssumeRoleWithWebIdentity` Pulumi ESC uses the regional endpoint matching `AWS_REGION` if set, otherwise the global endpoint. The call itself does not require an active region.

### What's the difference between `aws sts get-caller-identity` and `aws iam get-user`?

`get-caller-identity` works for any principal type (user, role, assumed-role session) and needs no permissions. `iam get-user` only works for IAM users, requires `iam:GetUser`, and fails when the caller is a role session — making it useless for verifying OIDC.

## Learn more

* [Pulumi ESC product page](/product/esc/)
* [Configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [Resolve `Unable to locate credentials`](/what-is/resolve-unable-to-locate-credentials/)
* [Resolve `InvalidClientTokenId`](/what-is/resolve-list-buckets-invalid-client-token-id/)
* [Resolve `ExpiredToken`](/what-is/resolve-list-buckets-expired-token/)
* [Run `aws s3 ls` with dynamic credentials](/what-is/run-aws-s3-ls-with-dynamic-credentials/)
* [Run `aws iam list-users` with dynamic credentials](/what-is/run-aws-iam-list-users-with-dynamic-credentials/)

[Join our community on Slack](https://slack.pulumi.com/) to discuss further, and let us know what you build.
