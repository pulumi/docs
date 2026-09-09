---
title: Fix AWS CLI Credential Errors and Run AWS Commands with Pulumi ESC
meta_desc: |
     Learn how Pulumi ESC's dynamic AWS credentials fix errors like ExpiredToken
     and let you run any AWS CLI command without local credential setup.
type: what-is
date: 2026-08-14T15:06:36-07:00
page_title: Fix AWS CLI Credential Errors and Run AWS Commands with Pulumi ESC
authors: ["diana-esteves", "torian-crane"]
aliases:
- /what-is/resolve-list-buckets-expired-token/
- /what-is/resolve-list-buckets-invalid-access-key-id/
- /what-is/resolve-list-buckets-invalid-client-token-id/
- /what-is/resolve-list-buckets-signature-does-not-match/
- /what-is/resolve-unable-to-locate-credentials/
- /what-is/run-aws-cloudwatch-get-metric-data-with-dynamic-credentials/
- /what-is/run-aws-dynamodb-list-tables-with-dynamic-credentials/
- /what-is/run-aws-ec2-describe-instances-with-dynamic-credentials/
- /what-is/run-aws-ec2-start-instances-with-dynamic-credentials/
- /what-is/run-aws-ec2-stop-instances-with-dynamic-credentials/
- /what-is/run-aws-iam-list-users-with-dynamic-credentials/
- /what-is/run-aws-lambda-list-functions-with-dynamic-credentials/
- /what-is/run-aws-s3-cp-with-dynamic-credentials/
- /what-is/run-aws-s3-ls-with-dynamic-credentials/
- /what-is/run-aws-s3-sync-with-dynamic-credentials/
---

Most AWS CLI credential errors, such as `ExpiredToken`, `InvalidAccessKeyId`, `InvalidClientTokenId`, `SignatureDoesNotMatch`, and "Unable to locate credentials," trace back to the same root cause: long-lived credentials that were configured locally, went stale, or were never configured correctly in the first place. Amazon Security Token Service (STS) issues temporary, limited-privilege credentials specifically to reduce this risk, but temporary credentials still require someone to generate, distribute, and refresh them by hand unless a tool does it automatically.

[Pulumi ESC (Environments, Secrets, and Configurations)](/docs/esc/) removes that manual step. With [dynamic credentials from AWS using OIDC](/blog/esc-env-run-aws/), Pulumi ESC requests short-lived AWS credentials on demand and injects them into the shell for the duration of a single command, via `pulumi env run`. There is nothing stored on disk to expire, misconfigure, or leak, and every AWS CLI command, from `aws s3 ls` to `aws sts get-caller-identity`, runs against fresh, correctly scoped credentials every time.

## Common AWS CLI credential errors and their cause

### ExpiredToken

"An error occurred (ExpiredToken) when calling the ListBuckets operation" (or any other operation) means the temporary credentials used for the call, typically issued through an IAM role or STS, have passed their expiration time. AWS expires these credentials by design; the error is expected behavior once the clock runs out, not a sign of misconfiguration.

### InvalidAccessKeyId

"An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation" means the access key ID in the request does not exist in AWS's records for the target account — commonly because the key was deleted, belongs to a different account, or was mistyped.

### InvalidClientTokenId

"An error occurred (InvalidClientTokenId) when calling the ListBuckets operation" is AWS's way of saying the security token or access key it received cannot be validated at all: malformed, revoked, or never issued. It is a closely related but distinct failure mode from an expired or merely incorrect key.

### SignatureDoesNotMatch

"An error occurred (SignatureDoesNotMatch) when calling the ListBuckets operation" means AWS could not verify the cryptographic signature computed from the secret access key. This usually points to a secret key that was copied incorrectly, is out of sync with its access key ID, or a system clock that has drifted enough to invalidate the signed request.

### Unable to locate credentials

The AWS CLI and SDKs raise "Unable to locate credentials" when they cannot find any credentials at all in the usual places: environment variables, the shared credentials file, an EC2 instance profile, or an assumed role. It is the default failure when nothing has been configured yet.

Every one of these errors disappears when credentials are generated fresh for each command rather than stored and reused. That is precisely what Pulumi ESC's dynamic credentials are designed to do.

## Using Pulumi ESC for dynamic credentials with AWS

[Pulumi ESC](https://www.pulumi.com/product/esc/) is a service that helps to alleviate the burden of managing cloud configuration and secrets by providing a centralized way to handle these critical aspects of cloud development. The `pulumi env run` command in particular helps resolve concerns around how to:

- Securely share credentials with teammates in a consistent way.
- Minimize the risks associated with locally configured, long-lived and highly privileged credentials.
- Ensure teams can easily and safely run AWS CLI commands without requiring deep security expertise.

### What is the pulumi env run command?

The [Pulumi documentation for the `pulumi env run` command](/docs/iac/cli/commands/pulumi_env_run/) states the following:

> This command opens the environment with the given name and runs the given command. If the opened environment contains a top-level 'environmentVariables' object, each key-value pair in the object is made available to the command as an environment variable.

In practice, this means any AWS CLI command, `aws sts get-caller-identity`, `aws s3 ls`, `aws ec2 describe-instances`, or dozens of others, can run without configuring AWS credentials locally beforehand. Three things follow from that:

- **Seamless command execution.** `pulumi env run` lets you execute AWS commands effortlessly, freeing you from the intricacies of managing AWS credentials on your local machine.
- **Enhanced security.** Removing local credential storage drastically reduces the risk of accidental exposure. Credentials and secrets stay securely managed within the Pulumi environment.
- **Streamlined collaboration.** Because credentials are centralized, every team member runs commands against the same secure environment, which removes the need to coordinate individual credentials and configurations.

## Getting started with pulumi env run

### Step 1: Install and log in to Pulumi ESC

Install the [Pulumi CLI](/docs/iac/download-install/), then run `pulumi login` and follow the prompts to log in.

```bash
$ pulumi login
Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser                   :
Logged in to pulumi.com as …
```

### Step 2: Create the OIDC configuration

Rather than storing AWS credentials as static secrets in an ESC environment, configure dynamic credentials so Pulumi ESC generates them on demand. Follow the [guide for configuring OIDC between Pulumi and AWS](/docs/esc/guides/configuring-oidc/aws/), and make sure the IAM role you create has sufficient permissions for the AWS operations you plan to run.

### Step 3: Create a new Pulumi ESC environment

Once OIDC is configured, create a new environment in [Pulumi Cloud](https://app.pulumi.com/signin). Make sure you have the correct organization selected in the left-hand navigation, select **Environments**, then **+ Create Environment**, and give it a name.

{{< video title="Open environment in Pulumi ESC console" src="https://www.pulumi.com/uploads/esc-create-new-env.mp4" autoplay="true" loop="true" >}}

### Step 4: Add the AWS provider integration

Clear the placeholder content in the environment editor and replace it with the following, substituting `<your-oidc-iam-role-arn>` with the IAM role ARN from the OIDC step:

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

### Step 5: Run any AWS CLI command with dynamic credentials

First, confirm your local environment has no AWS credentials configured:

```bash
$ aws configure list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key                <not set>             None    None
secret_key                <not set>             None    None
    region                <not set>             None    None
```

Then run any AWS CLI command through `pulumi env run`, replacing `<your-pulumi-org-name>`, `<your-project-name>`, and `<your-environment-name>` with your own values:

```bash
pulumi env run <your-pulumi-org-name>/<your-project-name>/<your-environment-name> -- aws s3 ls
```

The same pattern works for any AWS CLI operation. A few of the most common:

- `pulumi env run ... -- aws sts get-caller-identity` — see the [dedicated walkthrough](/what-is/run-aws-sts-get-caller-identity-with-dynamic-credentials/) for this specific command, the most-used entry point for verifying dynamic credentials are wired up correctly.
- `pulumi env run ... -- aws s3 cp <source> <destination>`
- `pulumi env run ... -- aws s3 sync <source> <destination>`
- `pulumi env run ... -- aws ec2 describe-instances`
- `pulumi env run ... -- aws ec2 start-instances --instance-ids <id>`
- `pulumi env run ... -- aws ec2 stop-instances --instance-ids <id>`
- `pulumi env run ... -- aws iam list-users`
- `pulumi env run ... -- aws lambda list-functions`
- `pulumi env run ... -- aws dynamodb list-tables`
- `pulumi env run ... -- aws cloudwatch get-metric-data --cli-input-json <file>`

## Frequently asked questions

### What causes the ExpiredToken error when calling AWS APIs?

Temporary AWS credentials, whether issued through an IAM role, STS, or Pulumi ESC's dynamic credentials, carry an expiration time by design. The `ExpiredToken` error simply means that time has passed. Requesting a fresh set of credentials for each command, which is what `pulumi env run` does automatically, prevents the error from occurring at all.

### How do I fix InvalidAccessKeyId or InvalidClientTokenId errors in the AWS CLI?

Both errors mean AWS could not validate the access key or token it received, either because it does not exist, was revoked, or was never issued correctly. Rather than debugging a specific stale key, replace static local credentials with Pulumi ESC's dynamic credentials so a correctly scoped, valid key is generated for every command.

### Why does AWS return SignatureDoesNotMatch?

This error means AWS could not verify the request's cryptographic signature, usually because a secret access key was copied incorrectly, is mismatched with its access key ID, or the system clock has drifted. Dynamic credentials from Pulumi ESC avoid the problem entirely, since the access key and secret are generated together and used immediately.

### What does "Unable to locate credentials" mean and how do I fix it?

The AWS CLI raises this error when it finds no credentials in any of the usual locations it checks: environment variables, the shared credentials file, an instance profile, or an assumed role. Running the command through `pulumi env run` supplies valid credentials as environment variables for that single invocation, so there is nothing to locate or configure beforehand.

### Can I run any AWS CLI command with Pulumi ESC dynamic credentials?

Yes. Once an environment is configured with the `aws-login` OIDC provider, `pulumi env run <org>/<project>/<environment> -- <any aws command>` works for any AWS CLI operation the underlying IAM role is permitted to perform. The command after `--` is unrestricted by Pulumi ESC itself; permissions are governed entirely by the IAM role's policy.

## Conclusion

Pulumi ESC makes it easier than ever to tame AWS credential management, from everyday commands like `aws s3 ls` to the errors that show up when credentials are stale, wrong, or missing entirely. Pulumi ESC supports dynamic credentials using OIDC across AWS, Azure, and Google Cloud. Check out the following links to learn more:

- Follow the [Getting Started](/docs/esc/get-started/) guide.
- Read the [documentation](/docs/esc/) for all the commands and features available.
- Visit the [open source](https://github.com/pulumi/esc) repo for Pulumi ESC.

Feel free to [join the Pulumi community on Slack](https://slack.pulumi.com/) and let us know what you think!
