---
title: An error occurred (SignatureDoesNotMatch) when calling the ListBuckets operation
allow_long_title: true
meta_desc: "The SignatureDoesNotMatch error from aws s3 ls means the request signature doesn't match. Most often a wrong AWS secret key or skewed system clock."
meta_image: /images/what-is/resolve-list-buckets-signature-does-not-match-meta.png
type: what-is
page_title: An error occurred (SignatureDoesNotMatch) when calling the ListBuckets operation
authors: ["torian-crane"]
---

**The `SignatureDoesNotMatch` error from `aws s3 ls` means the signature your client computed for the request does not match the signature AWS expected.** It almost always comes from one of three things: a wrong `AWS_SECRET_ACCESS_KEY` (typo, trailing whitespace, or truncated paste), a system clock that has drifted by more than 5 minutes, or a proxy/middlebox modifying the request after it was signed. Re-copy the secret, run an NTP sync, and disable any HTTP-rewriting proxy in front of S3.

In this article, we'll cover:

* What the `SignatureDoesNotMatch` error means
* What causes it
* How to fix it in four steps
* How to prevent it from happening again
* Common variations and related errors
* How Pulumi ESC eliminates manual secret handling
* Frequently asked questions

## What does this error mean?

AWS authenticates every API call with a [Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) signature: the client hashes the request (method, host, path, headers, body, and timestamp) using the AWS secret access key. AWS recomputes the same hash on its side; if they don't match, the request is rejected with `SignatureDoesNotMatch`.

The error means AWS *recognized your access key* (otherwise you'd get `InvalidAccessKeyId`) but rejected the signature itself. That narrows the cause to either the secret used to compute the signature, the inputs to the signature (most commonly the timestamp), or someone modifying the request in flight.

## What causes it?

| Cause | Symptom | Fix |
|---|---|---|
| Wrong or truncated secret key | First key works, second fails identically | Re-copy from IAM console; mind trailing whitespace |
| Special characters in secret | Secret contains `/`, `+`, or `=` and got shell-escaped | Quote the value: `export AWS_SECRET_ACCESS_KEY='...'` |
| Clock skew (> 5 minutes) | Works on one machine, fails on another | `sudo sntp -sS time.apple.com` or `w32tm /resync` |
| Corporate proxy modifying headers | Works at home, fails on VPN | Bypass the proxy for S3 endpoints |
| Wrong signing region | S3 path-style URL with mismatched region | Use the correct region for the bucket |
| AWS_SECRET_ACCESS_KEY exported with quotes | Quotes ended up *inside* the value | Re-export without surrounding quotes |

## How to fix it

Follow these steps in order. Each one is copy-pasteable.

1. **Check the clock.** AWS rejects any request whose `X-Amz-Date` is more than 5 minutes off server time.

   ```bash
   date -u
   # compare to:
   curl -sI https://s3.amazonaws.com | grep -i ^date
   ```

   If the two values differ by more than 5 minutes, sync NTP (`sudo sntp -sS time.apple.com` on macOS, `sudo timedatectl set-ntp on` on Linux, `w32tm /resync` on Windows).

1. **Verify the secret is exactly what AWS gave you.** Length is the fastest check; AWS secret keys are 40 characters.

   ```bash
   echo "Secret length: ${#AWS_SECRET_ACCESS_KEY}"
   ```

   If the value isn't 40 characters, re-copy it from the IAM console or from your secrets manager. Special characters (`/`, `+`, `=`) must be inside single quotes when exporting.

1. **Strip out interfering middleware.** If you're behind a corporate proxy or TLS-inspecting firewall, temporarily disable it:

   ```bash
   curl --noproxy '*' https://s3.amazonaws.com/
   ```

   Any proxy that rewrites headers or query strings will break the signature.

1. **Verify.**

   ```bash
   aws sts get-caller-identity
   aws s3 ls
   ```

   If `get-caller-identity` works but `s3 ls` still fails, the problem is region-specific signing — set `AWS_REGION` to the bucket's home region.

## How to prevent it

* **Pull secrets from a manager, not from copy/paste.** AWS Secrets Manager, HashiCorp Vault, and [Pulumi ESC](/product/esc/) all keep the secret out of clipboards and shell histories, eliminating the truncation and whitespace cases.
* **Keep clocks in sync.** Enable NTP on every machine that talks to AWS. Containers in particular tend to inherit the host clock, which silently breaks signatures when the host drifts.
* **Avoid TLS-inspecting proxies in front of S3.** If you must use one, exclude S3 hosts from inspection.
* **Don't use long-lived keys.** OIDC-issued temporary credentials never get copy-pasted, so the whole class of "the secret was wrong" disappears.

## Common variations

The same root cause produces a few closely related messages:

* `The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method.`
* `An error occurred (SignatureDoesNotMatch) when calling the PutObject operation` — same problem, different operation; usually a content-hash mismatch from middleware re-encoding the body.
* `RequestTimeTooSkewed` — the related "clock is off by more than 5 minutes" error. Fix the same way (NTP).

## Related errors

* [InvalidAccessKeyId](/what-is/resolve-list-buckets-invalid-access-key-id/) — the access key doesn't exist at all.
* [InvalidClientTokenId](/what-is/resolve-list-buckets-invalid-client-token-id/) — the session token doesn't match the access key.
* [ExpiredToken](/what-is/resolve-list-buckets-expired-token/) — the credential is past its lifetime.
* [Unable to locate credentials](/what-is/resolve-unable-to-locate-credentials/) — the SDK found no credentials at all.

## How Pulumi ESC eliminates manual secret handling

[Pulumi ESC](/product/esc/) (Environments, Secrets, and Configurations) issues short-lived AWS credentials via OIDC. There's no 40-character secret to copy, paste, or accidentally truncate. ESC delivers a coherent triple (access key, secret, session token) into the environment for the lifetime of the command.

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

Then run any AWS command with credentials that won't drift, expire, or get truncated:

```bash
esc run my-org/aws/dev -- aws s3 ls
```

For Pulumi programs, the AWS provider's [`assumeRole` configuration](/registry/packages/aws/api-docs/provider/) gives you the same OIDC-backed, no-secrets-in-code workflow inside a deployment.

## Frequently asked questions

### How much clock skew does AWS tolerate?

Five minutes. AWS rejects any request whose `X-Amz-Date` header differs from server time by more than 5 minutes (the related error is `RequestTimeTooSkewed`). NTP keeps most machines comfortably inside this window.

### Why does my secret work on one machine but not another?

Almost always a copy/paste artifact. Trailing newlines, smart quotes, or the secret being re-typed instead of pasted are the usual suspects. The fact that the same access key works elsewhere confirms it isn't an identity problem.

### Can a proxy actually cause this?

Yes. SigV4 hashes the request headers and body. Any HTTP-aware proxy that adds, removes, or rewrites headers (a corporate `Via` header, a content-rewriting filter) will break the signature. TLS-inspecting firewalls are the most common offender.

### What if I'm using `boto3` or another SDK, not the CLI?

The same error and the same causes. SDKs construct the SigV4 signature locally before sending the request; everything that breaks the CLI's signature also breaks the SDK's.

### Does this error mean my key is compromised?

No. `SignatureDoesNotMatch` is a client-side configuration error. It does not indicate that anyone has tried to use your key fraudulently. If you suspect compromise, audit CloudTrail for `AccessDenied` and unexpected `GetCallerIdentity` calls.

### Does this affect non-S3 calls?

Yes. SigV4 is used for nearly every AWS service. The same `SignatureDoesNotMatch` symptom appears on `aws ec2 describe-instances`, `aws sts get-caller-identity`, and so on, with the same root causes.

## Learn more

* [Pulumi ESC documentation](/docs/pulumi-cloud/esc/)
* [Configuring OIDC between Pulumi ESC and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [AWS provider reference](/registry/packages/aws/api-docs/provider/)
* [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
