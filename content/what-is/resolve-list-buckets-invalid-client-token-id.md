---
title: An error occurred (InvalidClientTokenId) when calling the ListBuckets operation
allow_long_title: true
meta_desc: "The InvalidClientTokenId error from aws s3 ls means the security token in your request isn't valid. Usually a mismatched or stale AWS_SESSION_TOKEN."
meta_image: /images/what-is/resolve-list-buckets-invalid-client-token-id-meta.png
type: what-is
page_title: An error occurred (InvalidClientTokenId) when calling the ListBuckets operation
authors: ["torian-crane"]
---

**The `InvalidClientTokenId` error from `aws s3 ls` means the security token included in the request is not valid for the access key the SDK is using.** It almost always comes from a mismatched or partially-exported set of temporary credentials: an `AWS_SESSION_TOKEN` left over from a previous role, or an `AWS_ACCESS_KEY_ID` that no longer corresponds to the token. Re-fetch a fresh set of credentials together with `aws sso login` or `aws sts assume-role`, and re-export all three values in one go.

In this article, we'll cover:

* What the `InvalidClientTokenId` error means
* What causes it
* How to fix it in four steps
* How to prevent it from happening again
* Common variations and related errors
* How Pulumi ESC eliminates manual session-token juggling
* Frequently asked questions

## What does this error mean?

`InvalidClientTokenId` is an AWS Security Token Service (STS) authentication error. AWS validates every signed request by looking up the access key ID, computing the expected signature with the matching secret, and (for temporary credentials) verifying the session token. When the session token doesn't match the access key/secret pair AWS expects, the request is rejected with `InvalidClientTokenId`.

The wording is misleading. It's not "your token is malformed." It's "the token you sent does not go with this access key." That distinction is what makes this error tricky: each of the three values may look correct in isolation, yet still produce the error when combined.

## What causes it?

| Cause | Symptom | Fix |
|---|---|---|
| Stale `AWS_SESSION_TOKEN` from a previous role | Switched roles and re-exported only two of three vars | Re-export all three together; unset first |
| `AKIA…` long-lived key with a session token attached | Combined IAM-user key with a leftover STS token | `unset AWS_SESSION_TOKEN` |
| Partial paste from STS output | Newline or space inside the token | Re-copy from a fresh `assume-role` call |
| Region mismatch for STS | Used a regional STS endpoint that doesn't recognize the token | Use the global endpoint or the same region that issued it |
| Mixed env vars and `~/.aws/credentials` | Profile has IAM-user keys, shell has STS token | Pick one source; unset the other |
| Cross-partition (commercial vs GovCloud) | Token issued in one partition used against the other | Use the matching partition's STS |

## How to fix it

Follow these steps in order. Each one is copy-pasteable.

1. **Inspect what the SDK is reading.** The credential chain decides everything; check it first.

   ```bash
   aws configure list
   env | grep -E '^AWS_(ACCESS_KEY_ID|SECRET_ACCESS_KEY|SESSION_TOKEN)' | cut -d= -f1
   ```

   If you see `AWS_SESSION_TOKEN` set alongside an `AKIA…` access key (visible via the first command), that's almost certainly the problem.

1. **Clear the slate.** Unset the three environment variables so the next refresh produces a coherent set:

   ```bash
   unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
   ```

1. **Get a fresh, matching set of credentials.** Use the same flow that issued the temporary credentials originally:

   ```bash
   aws sso login --profile my-profile
   ```

   Or, for a direct `assume-role`:

   ```bash
   aws sts assume-role \
     --role-arn arn:aws:iam::123456789012:role/MyRole \
     --role-session-name my-session
   ```

   Export all three returned values — `AccessKeyId`, `SecretAccessKey`, and `SessionToken` — in the same shell.

1. **Verify.**

   ```bash
   aws sts get-caller-identity
   aws s3 ls
   ```

   `get-caller-identity` returns immediately when authentication succeeds, which makes it a clean smoke test before you run anything that matters.

## How to prevent it

* **Never export `AWS_SESSION_TOKEN` by itself.** It always travels with its `ACCESS_KEY_ID` and `SECRET_ACCESS_KEY`. If you switch identities, replace all three.
* **Use profiles instead of raw env vars.** Named profiles in `~/.aws/credentials` and `~/.aws/config` keep the three values atomically grouped, which removes most "I exported the wrong two" cases.
* **Use a credential helper.** `aws-vault`, `granted`, and `aws sso login` manage the three values as a unit. Manual shell exports are how this error gets created in the first place.
* **Adopt OIDC for CI.** GitHub Actions, GitLab, and other runners mint short-lived role credentials per job, eliminating the manual export step entirely.

## Common variations

The same root cause produces a few closely related messages:

* `An error occurred (InvalidClientTokenId) when calling the GetCallerIdentity operation: The security token included in the request is invalid.`
* `InvalidClientTokenId: The security token included in the request is expired.` — actually `ExpiredToken` territory; check session lifetime first.
* `InvalidClientTokenId` against STS itself — the credentials you're trying to use to *call* STS are themselves invalid; you need to re-authenticate at the source.

The fix is always the same: re-fetch a complete, fresh set of credentials.

## Related errors

* [InvalidAccessKeyId](/what-is/resolve-list-buckets-invalid-access-key-id/) — the access key doesn't exist; this error is about token mismatch instead.
* [SignatureDoesNotMatch](/what-is/resolve-list-buckets-signature-does-not-match/) — the secret is wrong (or clock is skewed).
* [ExpiredToken](/what-is/resolve-list-buckets-expired-token/) — the token is well-formed but past its lifetime.
* [Unable to locate credentials](/what-is/resolve-unable-to-locate-credentials/) — the SDK found no credentials at all.

## How Pulumi ESC eliminates manual session-token juggling

[Pulumi ESC](/product/esc/) (Environments, Secrets, and Configurations) manages the three credential values as a single atomic set. Each invocation of `esc run` calls AWS STS via OIDC and exports a fresh, internally-consistent triple, so the mismatched-token case literally cannot happen.

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

Then run any AWS command with credentials that are always coherent:

```bash
esc run my-org/aws/dev -- aws s3 ls
```

For Pulumi programs that need to operate across accounts, the AWS provider's [`assumeRole` configuration](/registry/packages/aws/api-docs/provider/) handles the equivalent role-chain logic inside a deployment, without exposing the underlying STS calls to the operator.

## Frequently asked questions

### What's the difference between `InvalidClientTokenId` and `ExpiredToken`?

`InvalidClientTokenId` means the session token doesn't match the access key. `ExpiredToken` means the credentials are well-formed and known to AWS but are past their lifetime. Practically, the diagnostic is the same — refresh the credentials — but the underlying cause is different.

### Why do I see this only after switching profiles?

Because environment variables override profile lookups. When you ran `assume-role` once, `AWS_SESSION_TOKEN` got exported. The next time you used `aws --profile other`, the SDK picked up the profile's access key and secret but kept the stale session token from your shell. Unset `AWS_SESSION_TOKEN` before switching profiles.

### Can `InvalidClientTokenId` happen with IAM-user keys?

Yes, but only if you accidentally combine them with a session token. IAM-user keys (`AKIA…`) are not paired with a session token; setting `AWS_SESSION_TOKEN` while using them produces this exact error.

### Does this error indicate a security incident?

Almost never. It is overwhelmingly a configuration mistake. AWS does return this error if someone tampered with the request signature in flight, but the realistic cause for an interactive user is mismatched env vars.

### Why doesn't AWS tell me which value is wrong?

For security reasons. AWS does not echo back which part of the credential triple it rejected. Use `aws sts get-caller-identity` once you have a fresh set; if that fails, you know the whole triple is still broken.

### Will using `aws configure` to re-set my access key fix this?

Only if you also remove the stale session token. `aws configure` writes profile values; it does not unset environment variables. After re-running it, run `unset AWS_SESSION_TOKEN` (or close and reopen your shell).

## Learn more

* [Pulumi ESC documentation](/docs/pulumi-cloud/esc/)
* [Configuring OIDC between Pulumi ESC and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [AWS provider reference](/registry/packages/aws/api-docs/provider/)
* [AWS STS temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
