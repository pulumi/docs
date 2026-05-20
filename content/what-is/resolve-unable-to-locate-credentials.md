---
title: Unable to locate credentials
allow_long_title: true
meta_desc: "The Unable to locate credentials error means the AWS SDK searched every source in the credential chain and found nothing. Configure a profile, role, or env vars."
meta_image: /images/what-is/resolve-unable-to-locate-credentials-meta.png
type: what-is
page_title: Unable to locate credentials
authors: ["torian-crane"]
---

**The `Unable to locate credentials` error means the AWS CLI or SDK searched every source in the credential provider chain — environment variables, `~/.aws/credentials`, EC2 or EKS instance roles, ECS task roles — and found nothing.** Either no credentials are configured for the current identity, or the SDK is looking in a different place than you expect. Fix it by setting `AWS_PROFILE`, exporting `AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY`, running `aws sso login`, or attaching an instance role.

In this article, we'll cover:

* What the error means
* The AWS credential provider chain
* What causes it
* How to fix it in four steps
* How to prevent it from happening again
* How Pulumi ESC provides credentials automatically
* Related errors
* Frequently asked questions

## What does this error mean?

Unlike `InvalidAccessKeyId` or `SignatureDoesNotMatch`, this error never reaches AWS. The SDK gives up locally because it can't find anything to sign a request with. The credential resolution chain ran to completion and every source returned empty.

The text varies slightly across SDKs (`botocore.exceptions.NoCredentialsError`, `Unable to load credentials from any of the providers in the chain`, etc.), but they all mean the same thing: nothing to send.

## The AWS credential provider chain

Most AWS SDKs check sources in this order. The first source that returns credentials wins:

1. **Environment variables** — `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, optionally `AWS_SESSION_TOKEN`.
1. **AWS SSO / IAM Identity Center cache** — populated by `aws sso login`.
1. **Shared credentials file** — `~/.aws/credentials` (and `~/.aws/config` for profiles), selected via `AWS_PROFILE` or `--profile`.
1. **Container credentials** — ECS task role, served on `169.254.170.2`.
1. **Instance metadata** — EC2 instance profile or EKS pod identity, served on `169.254.169.254`.

If you see this error, every source above was checked and came back empty.

## What causes it?

| Cause | Symptom | Fix |
|---|---|---|
| No profile configured | `~/.aws/credentials` missing or empty | `aws configure` or `aws sso login` |
| Wrong `AWS_PROFILE` | `aws --profile other` works, plain `aws` doesn't | `export AWS_PROFILE=other` |
| Container has no IAM role | ECS task without a task role | Attach a task role |
| EC2 IMDSv2 hop limit too low | Container on EC2 cannot reach `169.254.169.254` | Raise `HttpPutResponseHopLimit` to 2 |
| SSO session not initialized | `~/.aws/sso/cache/` empty | `aws sso login --profile <name>` |
| Wrong user running the command | `sudo` strips environment variables | Use `sudo -E` or set the profile globally |
| `AWS_PROFILE` set to a profile that doesn't exist | Silent fallthrough to "no credentials" | Check spelling in `~/.aws/config` |

## How to fix it

Follow these steps in order. Each one is copy-pasteable.

1. **Ask the SDK what it sees.**

   ```bash
   aws configure list
   env | grep -E '^AWS_'
   ```

   The `Source` column points at exactly which source the CLI is consulting, or `<not set>` if nothing is configured. This is usually enough to identify the gap.

1. **Pick a credential source and configure it.** For a developer laptop with SSO:

   ```bash
   aws configure sso
   aws sso login
   ```

   For a long-lived IAM user (not recommended for humans, but fine for tests):

   ```bash
   aws configure
   ```

   For a CI runner, prefer OIDC into AWS rather than static keys.

1. **For containers and EC2 instances, attach a role.** Servers and containers should never read static keys. Attach an IAM instance profile (EC2), task role (ECS), or service account (EKS with IRSA or EKS Pod Identity). The SDK picks them up automatically.

1. **Verify.**

   ```bash
   aws sts get-caller-identity
   aws s3 ls
   ```

   If `get-caller-identity` works, credentials are loaded correctly. If it still fails, the SDK is still finding the wrong source — re-check `AWS_PROFILE` and the environment variables.

## How to prevent it

* **Use one credential source per environment.** Mixing env vars, profiles, and instance roles is the leading source of "wait, which credentials is it using?" confusion.
* **Don't run AWS commands under `sudo`.** `sudo` strips `AWS_*` environment variables by default. Use `sudo -E` if you really need to elevate.
* **Adopt OIDC for CI.** Static keys in CI are the largest source of leaked credentials. GitHub Actions, GitLab, and CircleCI all support short-lived OIDC into AWS.
* **Document where credentials come from.** Even a single sentence in the README about which profile or role is expected prevents this for newcomers.

## How Pulumi ESC provides credentials automatically

[Pulumi ESC](/product/esc/) (Environments, Secrets, and Configurations) brokers OIDC-issued AWS credentials and injects them as environment variables for the duration of a command. As long as you're logged into Pulumi (`pulumi login` / `esc login`), `Unable to locate credentials` cannot occur — `esc run` always exports a complete credential triple.

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

Then run any AWS command without configuring credentials locally:

```bash
esc run my-org/aws/dev -- aws s3 ls
```

For Pulumi programs themselves, the AWS provider's [`assumeRole` configuration](/registry/packages/aws/api-docs/provider/) supplies credentials inside a deployment, so a `pulumi up` never depends on the operator's shell.

## Related errors

* [InvalidAccessKeyId](/what-is/resolve-list-buckets-invalid-access-key-id/) — credentials *were* found, but the key isn't recognized by AWS.
* [SignatureDoesNotMatch](/what-is/resolve-list-buckets-signature-does-not-match/) — credentials were found and the key exists, but the secret is wrong.
* [InvalidClientTokenId](/what-is/resolve-list-buckets-invalid-client-token-id/) — temporary credentials present but inconsistent.
* [ExpiredToken](/what-is/resolve-list-buckets-expired-token/) — temporary credentials present but past their lifetime.

## Frequently asked questions

### Why does `aws --profile foo` work but plain `aws` does not?

Because the default chain didn't find anything. Either `AWS_PROFILE` is unset (so `default` is the implicit profile, and `default` is empty), or environment variables are partially set. Set `AWS_PROFILE=foo` in your shell to make the working profile the default.

### Why does it work in my terminal but not in cron or systemd?

Cron and systemd have minimal environments. They don't inherit your interactive shell's `AWS_PROFILE` or `AWS_*` exports. Set credentials in the unit's `Environment=` directive or load them from a credentials file inside the service.

### My code runs on EC2 but still says "Unable to locate credentials". Why?

Either the instance has no IAM role attached, or the metadata service is unreachable. From a container on EC2, the hop limit is the usual culprit: AWS sets `HttpPutResponseHopLimit` to 1 by default, which doesn't reach inside Docker. Increase it to 2.

### How is this different from `NoCredentialProviders`?

It isn't — `NoCredentialProviders` is the Go SDK's version of the same error. The Python SDK calls it `NoCredentialsError`. They all mean the chain returned empty.

### Do I need to set `AWS_REGION` too?

Not for this error, but yes for most operations. `Unable to locate credentials` is strictly about credentials. Region-related failures show up as `You must specify a region` or as a 301 redirect when calling S3.

### Will `aws configure` fix this on a server?

It will, but you shouldn't. Servers should use instance roles, ECS task roles, or EKS Pod Identity instead of static keys. Static keys on servers are a credential-leak waiting to happen.

## Learn more

* [Pulumi ESC documentation](/docs/pulumi-cloud/esc/)
* [Configuring OIDC between Pulumi ESC and AWS](/docs/esc/environments/configuring-oidc/aws/)
* [AWS provider reference](/registry/packages/aws/api-docs/provider/)
* [AWS CLI configuration and credential files](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
