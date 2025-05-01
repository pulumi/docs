---
title_tag: Configure access | AWS
title: Configure access
h1: "Get started with Pulumi and AWS"
meta_desc: This page provides an overview on how to get started with Pulumi when starting an AWS project.
weight: 3
menu:
    iac:
        name: Configure access
        parent: aws-b-get-started
        weight: 3

aliases:
- /docs/iac/get-started/aws/b/configure/
---

## Configure access to AWS

Pulumi's CLI needs access to your AWS account to manage cloud resources.

If you've already <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html" target="_blank">installed</a> and <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html" target="_blank">configured</a> the AWS CLI, Pulumi will respect and use your configuration settings.

You must use an IAM user account that has [programmatic access](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html) with rights to deploy and manage S3 buckets.

### Testing access

To test that your AWS access is configured properly, run:

{{% choosable os "linux,macos" %}}

```bash
$ aws sts get-caller-identity
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> aws sts get-caller-identity
```

{{% /choosable %}}

If your AWS user ID, account, and ARN are printed, you are good to go. If not, read on:

```
{
    "UserId": "BXO3165...ZP36NYY5FOU:my-session",
    "Account": "9263...9123",
    "Arn": "arn:aws:sts::9263...9123:assumed-role/.../my-session"
}
```

### Alternative approaches

If you don't have the AWS CLI installed, or you plan on using Pulumi in a CI/CD pipeline, <a href="https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys" target="_blank">retrieve your access key ID and secret access key</a> and then set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables on your workstation:

{{% choosable os "linux,macos" %}}

```bash
$ export AWS_ACCESS_KEY_ID="<YOUR_ACCESS_KEY_ID>"
$ export AWS_SECRET_ACCESS_KEY="<YOUR_SECRET_ACCESS_KEY>"
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:AWS_ACCESS_KEY_ID = "<YOUR_ACCESS_KEY_ID>"
> $env:AWS_SECRET_ACCESS_KEY = "<YOUR_SECRET_ACCESS_KEY>"
```

{{% /choosable %}}

{{% notes type="info" %}}
Consider using [Pulumi ESC's AWS login support](/docs/esc/integrations/dynamic-login-credentials/aws-login) for dynamic,
short-lived AWS credentials via OpenID Connect (OIDC) instead of long-lived static credentials. This is a security best practice.
{{% /notes %}}

You may optionally use AWS profiles if your configuration requires them:

{{% choosable os "linux,macos" %}}

```bash
$ export AWS_PROFILE="<YOUR_PROFILE_NAME>"
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:AWS_PROFILE = "<YOUR_PROFILE_NAME>"
```

{{% /choosable %}}

For detailed information on Pulumi's use of AWS credentials, see [AWS Setup](/registry/packages/aws/installation-configuration/).

{{< get-started-stepper >}}
