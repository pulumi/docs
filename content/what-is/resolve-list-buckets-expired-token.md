---
title: An error occurred (ExpiredToken) when calling the ListBuckets operation
allow_long_title: true
meta_desc: "The ExpiredToken error from aws s3 ls means your temporary AWS credentials expired. Refresh them with aws sso login or by re-assuming the role."
meta_image: /images/what-is/resolve-list-buckets-expired-token-meta.png
type: what-is
page_title: An error occurred (ExpiredToken) when calling the ListBuckets operation
authors: ["torian-crane"]
---

**The `ExpiredToken` error from `aws s3 ls` means your temporary AWS credentials have expired and need to be refreshed.** STS session tokens are short-lived (default 1 hour, max 12 hours for `assume-role`, up to 12 hours by default and 90 days when extended for IAM Identity Center sessions). When they expire, every AWS API call returns this error until you obtain fresh credentials by re-authenticating with `aws sso login`, calling `aws sts assume-role` again, or letting your credential helper rotate them.

In this article, we'll cover:

* What the `ExpiredToken` error means
* What causes it
* How to fix it in three steps
* How to prevent it from happening again
* Common variations and related errors
* How Pulumi ESC eliminates manual credential refresh
* Frequently asked questions

## What does this error mean?

`ExpiredToken` is an AWS Security Token Service (STS) response code. It is returned by any AWS service (S3, EC2, IAM, and so on) when a request is signed with temporary credentials whose lifetime has passed. The credentials themselves are still well-formed, but AWS has marked them as no longer valid. Until you replace them with fresh ones, every signed request fails the same way.

The error is specific to *temporary* credentials. It does not appear for long-lived IAM user access keys, because those have no expiration. If you see `ExpiredToken`, you are using credentials issued through SSO, `assume-role`, an EKS pod identity, EC2 instance metadata, or some other STS-backed source.

## What causes it?

| Cause | Symptom | Fix |
|---|---|---|
| SSO session lapsed | `aws sso login` was hours ago; `~/.aws/sso/cache/*.json` is stale | `aws sso login --profile <name>` |
| `assume-role` token aged out | Helper script set `AWS_SESSION_TOKEN` more than an hour ago | Re-run `aws sts assume-role` and re-export |
| EC2 or EKS role-cache lag | Process cached creds beyond their TTL | Restart the process or clear the SDK's credential cache |
| Identity broker (Okta, Vault) token expired | Browser flow times out | Re-authenticate through the broker |
| Laptop slept, clock drifted | Token isn't actually expired but appears so to AWS | Sync time (`sntp -sS time.apple.com` or `w32tm /resync`) and retry |

## How to fix it

Follow these steps in order. Each one is copy-pasteable.

1. **Identify how you got the credentials.** Check the SDK chain by running `aws configure list`. The `Source` column tells you whether they came from environment variables, an SSO profile, an EC2 instance role, or a config file.

   ```bash
   aws configure list
   ```

1. **Re-authenticate at the source.** If the profile uses SSO, refresh the SSO session:

   ```bash
   aws sso login --profile my-profile
   ```

   If the profile uses `assume-role` directly, re-assume:

   ```bash
   aws sts assume-role \
     --role-arn arn:aws:iam::123456789012:role/MyRole \
     --role-session-name my-session
   ```

   Export the returned `AccessKeyId`, `SecretAccessKey`, and `SessionToken` as the three `AWS_*` environment variables.

1. **Verify the refresh worked.**

   ```bash
   aws sts get-caller-identity
   aws s3 ls
   ```

   `get-caller-identity` is a cheap call that does not require permissions beyond authentication, which makes it the right smoke test before running real workloads.

## How to prevent it

* **Use credential helpers, not raw exports.** `aws sso login`, `aws-vault`, and `granted` all refresh tokens transparently. Manually exporting `AWS_*` variables in a shell is the fastest way to end up holding stale credentials.
* **Increase the session duration where appropriate.** For `assume-role`, set `--duration-seconds` up to the role's `MaxSessionDuration` (max 43200 seconds, or 12 hours). For SSO, raise the permission set's session duration in IAM Identity Center.
* **Stop using long-lived access keys to work around the error.** It "fixes" the symptom by trading expiration for a much larger blast radius if the keys leak.
* **Move CI/CD off static credentials.** GitHub Actions, GitLab, and other modern runners support OIDC into AWS, which mints short-lived credentials per job and refreshes them automatically.

## Common variations

The same root cause produces several closely related messages:

* `An error occurred (ExpiredToken) when calling the ListBuckets operation: The provided token has expired.`
* `An error occurred (ExpiredTokenException) when calling the AssumeRole operation` — your STS *caller* credentials expired, not the target role.
* `Token has expired and refresh failed` — boto3 or another SDK could not auto-refresh because the source credentials are also expired.

The fix is the same in every case: refresh at the original source of the temporary credentials.

## Related errors

* [InvalidClientTokenId](/what-is/resolve-list-buckets-invalid-client-token-id/) — usually a mismatched session token, not an expired one.
* [InvalidAccessKeyId](/what-is/resolve-list-buckets-invalid-access-key-id/) — the access key does not exist, often a stale rotation.
* [SignatureDoesNotMatch](/what-is/resolve-list-buckets-signature-does-not-match/) — typically a wrong secret key or clock skew.
* [Unable to locate credentials](/what-is/resolve-unable-to-locate-credentials/) — the SDK found no credentials at all.

## How Pulumi ESC eliminates manual credential refresh

[Pulumi ESC](/product/esc/) (Environments, Secrets, and Configurations) brokers short-lived AWS credentials via OIDC. Instead of running `aws sso login` and hoping the cached token is still valid, you wrap your command in `esc run`. ESC mints a fresh STS session every time, so `ExpiredToken` cannot occur.

Define the environment once:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::123456789012:role/PulumiESCRole
          sessionName: pulumi-environments-session
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

Then run any AWS command with always-fresh credentials:

```bash
esc run my-org/aws/dev -- aws s3 ls
```

For Pulumi programs themselves, the equivalent provider configuration uses the AWS provider's [`assumeRole` block](/registry/packages/aws/api-docs/provider/), which the provider refreshes automatically during long-running deployments.

## Frequently asked questions

### How long do AWS temporary credentials last?

By default, `assume-role` credentials last 1 hour with a maximum of 12 hours (`MaxSessionDuration` on the role). IAM Identity Center (SSO) sessions can run up to 12 hours by default and can be extended further by an administrator. EC2 instance role credentials refresh automatically.

### Does this error affect IAM users with long-lived access keys?

No. IAM user access keys do not expire on their own. If you see `ExpiredToken` with what you believe is a long-lived key, it almost always means a session token (`AWS_SESSION_TOKEN`) was also exported and is now stale. Unset `AWS_SESSION_TOKEN` and retry.

### Can I extend a single STS session beyond 12 hours?

Not for `assume-role`. The hard maximum is 12 hours, even with `MaxSessionDuration` raised. For longer-running workloads, refresh the credentials on a timer rather than trying to hold one session open.

### Why does my SDK still see the old token after I refreshed?

Most SDKs cache credentials in memory. If a long-running process started with expired credentials, it will keep using them until restarted or until the credential provider chain is reset. Restart the process, or have it call the credential refresh API explicitly.

### Does this only happen with S3?

No. `ExpiredToken` is returned by any AWS service that authenticates a request — EC2, IAM, Lambda, DynamoDB, and so on. `aws s3 ls` happens to be the most common command people run to test credentials, which is why the error is most visible there.

### Will `aws configure` fix this?

No. `aws configure` writes static profile values to `~/.aws/credentials`. It does not refresh STS sessions. Use `aws sso login` (for SSO), re-export credentials from `assume-role`, or use a helper such as `aws-vault` or Pulumi ESC.

## Learn more

* [Pulumi ESC documentation](/docs/pulumi-cloud/esc/)
* [Configuring OIDC between Pulumi ESC and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [AWS provider reference](/registry/packages/aws/api-docs/provider/)
* [AWS STS `AssumeRole` API reference](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
