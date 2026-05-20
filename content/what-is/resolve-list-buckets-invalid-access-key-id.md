---
title: An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation
allow_long_title: true
meta_desc: "The InvalidAccessKeyId error from aws s3 ls means the access key isn't recognized by AWS. The key has been deleted, deactivated, or mistyped."
meta_image: /images/what-is/resolve-list-buckets-invalid-access-key-id-meta.png
type: what-is
page_title: An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation
authors: ["torian-crane"]
---

**The `InvalidAccessKeyId` error from `aws s3 ls` means the AWS access key ID in the request does not exist in AWS's records.** The key has been deleted, deactivated, never created, or — most commonly — there's a typo or whitespace in the `AWS_ACCESS_KEY_ID` value the SDK picked up. Confirm the key with `aws iam list-access-keys`, re-export a valid one, or switch to a profile or role that produces fresh credentials.

In this article, we'll cover:

* What the `InvalidAccessKeyId` error means
* What causes it
* How to fix it in four steps
* How to prevent it from happening again
* Common variations and related errors
* How Pulumi ESC eliminates manual access key management
* Frequently asked questions

## What does this error mean?

`InvalidAccessKeyId` is an AWS authentication error returned when the access key ID in a request does not match any access key registered in AWS. AWS access keys are 20-character identifiers, typically starting with `AKIA` (for IAM users) or `ASIA` (for temporary STS sessions). When AWS receives a signed request, it looks the access key ID up in its account database; if the lookup fails, the API call is rejected with this error before any S3-specific authorization is checked.

The error means AWS couldn't find the key at all. That's different from `SignatureDoesNotMatch` (the key exists but the secret is wrong) or `ExpiredToken` (the temporary credential is past its lifetime).

## What causes it?

| Cause | Symptom | Fix |
|---|---|---|
| Key was deleted | Worked yesterday; nothing changed locally | Create a new key or switch profile |
| Key was deactivated | `aws iam list-access-keys` shows `Status: Inactive` | Reactivate or rotate the key |
| Typo or whitespace in env var | Key looks right but `echo $AWS_ACCESS_KEY_ID \| wc -c` is not 21 | Re-export the key cleanly |
| Wrong account | Key exists, but in a different AWS account than the resource | Switch to a profile in the correct account |
| Stale `~/.aws/credentials` | A `default` profile still holds a key from months ago | Update or remove the profile |
| `ASIA…` key used without its session token | Temporary key works only with the matching `AWS_SESSION_TOKEN` | Export all three values together |

## How to fix it

Follow these steps in order. Each one is copy-pasteable.

1. **See what the SDK is actually using.** The credential chain is the first thing to check, because the value you think is set may not be the one the SDK picked up.

   ```bash
   aws configure list
   echo "AWS_ACCESS_KEY_ID length: ${#AWS_ACCESS_KEY_ID}"
   ```

   A valid access key ID is 20 characters. Anything else points at a copy/paste issue.

1. **Confirm the key exists in AWS.** If you have working credentials for the same user (for example via the console or another profile):

   ```bash
   aws iam list-access-keys --user-name <your-user>
   ```

   Compare the `AccessKeyId` values and `Status` (`Active` or `Inactive`) with what you have locally.

1. **Rotate or re-export.** If the key is missing or inactive, create a new one and rotate. If you're using SSO or `assume-role`, log in again to refresh:

   ```bash
   aws sso login --profile my-profile
   ```

   For temporary credentials, make sure all three values are exported together:

   ```bash
   export AWS_ACCESS_KEY_ID=ASIA...
   export AWS_SECRET_ACCESS_KEY=...
   export AWS_SESSION_TOKEN=...
   ```

1. **Verify.**

   ```bash
   aws sts get-caller-identity
   aws s3 ls
   ```

   `get-caller-identity` succeeds as soon as authentication works, so it's the cleanest signal that the key is recognized.

## How to prevent it

* **Stop using long-lived access keys for humans.** Use [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/) (SSO) so humans get short-lived `ASIA…` credentials that are never typed or pasted.
* **Use named profiles, not the `default`.** Mistakes happen when a stale `default` profile silently shadows your intent. Explicit `--profile` flags or `AWS_PROFILE` make the active identity obvious.
* **Avoid keys in CI.** GitHub Actions, GitLab, and CircleCI all support OIDC into AWS; that removes long-lived keys from the runner entirely.
* **Rotate on a schedule, not on incident.** AWS recommends rotating IAM user access keys every 90 days. Combined with key-age alerts, this prevents most "the key was deleted and nobody told me" cases.

## Common variations

The same root cause produces a few closely related messages:

* `The AWS Access Key Id you provided does not exist in our records.`
* `An error occurred (InvalidAccessKeyId) when calling the GetCallerIdentity operation` — same problem, surfaced earlier in the chain.
* `InvalidAccessKeyId: The AWS Access Key Id needs a subscription for the service` — almost always the wrong AWS partition (commercial vs GovCloud vs China).

The fix is always the same: prove the access key actually exists in the account you're talking to.

## Related errors

* [SignatureDoesNotMatch](/what-is/resolve-list-buckets-signature-does-not-match/) — the key exists, but the secret is wrong.
* [InvalidClientTokenId](/what-is/resolve-list-buckets-invalid-client-token-id/) — the *session token* doesn't match the access key.
* [ExpiredToken](/what-is/resolve-list-buckets-expired-token/) — the credential is valid but past its lifetime.
* [Unable to locate credentials](/what-is/resolve-unable-to-locate-credentials/) — the SDK found no credentials at all.

## How Pulumi ESC eliminates manual access key management

[Pulumi ESC](/product/esc/) (Environments, Secrets, and Configurations) replaces hand-managed access keys with short-lived, OIDC-issued credentials. There's nothing to rotate, nothing to paste into `~/.aws/credentials`, and no `AKIA…` key to leak.

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

Then run any AWS command with credentials that are always recognized by AWS:

```bash
esc run my-org/aws/dev -- aws s3 ls
```

For Pulumi programs that need to operate across accounts, the AWS provider's [`assumeRole` configuration](/registry/packages/aws/api-docs/provider/) does the same thing inside a deployment — no static keys live in code or CI.

## Frequently asked questions

### How do I check whether my access key still exists?

Use `aws iam list-access-keys --user-name <your-user>`. It returns every key associated with that IAM user along with its status. If your key isn't in the list, it has been deleted.

### What's the difference between `AKIA` and `ASIA` keys?

`AKIA…` keys belong to IAM users and are long-lived; `ASIA…` keys are temporary, issued by STS for an `assume-role`, SSO, or federated session. `ASIA…` keys must always be paired with the matching `AWS_SESSION_TOKEN`. Using one without the other produces this error or `InvalidClientTokenId`.

### Could this be a region problem?

Generally no. `InvalidAccessKeyId` is about identity, not region. The most common region-adjacent variant is the GovCloud/commercial mix-up: a commercial-region key cannot authenticate against `aws-us-gov` endpoints, and the API returns this error.

### Does this happen with EC2 instance roles?

Rarely, and usually as a side effect of a stale local profile. If `AWS_PROFILE` or `AWS_ACCESS_KEY_ID` is set in the shell, the SDK uses those instead of the instance metadata role. Unset them and the instance role takes over.

### Why do I get this after a key rotation?

Because the old key was deleted while a long-running process or terminal was still holding it. Restart the process and re-export the new key. CI pipelines often hit this when only the secrets manager was updated but not the deployed runner.

### Can I tell from the error message which account the key was supposed to be in?

No. AWS deliberately does not echo the access key back in the response, and it does not say which account was queried. Use `aws sts get-caller-identity` once you have working credentials to confirm the account ID.

## Learn more

* [Pulumi ESC documentation](/docs/pulumi-cloud/esc/)
* [Configuring OIDC between Pulumi ESC and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [AWS provider reference](/registry/packages/aws/api-docs/provider/)
* [AWS IAM access key best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
