---
title_tag: Configure access | AWS
title: Configure access to AWS
linkTitle: Configure access
h1: "Configure access to AWS"
meta_desc: This page provides an overview on how to get started with Pulumi when starting an AWS project.
weight: 3
menu:
    iac:
        name: Configure access
        parent: aws-get-started
        weight: 3
        identifier: aws-get-started.configure
aliases:
    - /docs/iac/get-started/aws/b/configure/
---

The Pulumi CLI needs access to your AWS account to manage cloud resources. For this tutorial, you'll need an IAM user with [programmatic access](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html) and rights to manage S3 buckets.

If you've previously <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html" target="_blank">installed</a> and <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html" target="_blank">configured</a> the AWS CLI, Pulumi will respect and use those settings, which you can test with the CLI directly:

```bash
$ aws sts get-caller-identity

{
    "UserId": "BXO3...",
    "Account": "9263...",
    "Arn": "arn:aws:sts::9263..."
}
```

If your user ID, account, and ARN are printed, you're configured correctly.

The AWS CLI is convenient, but not required. You can also configure Pulumi with environment variables — for example, with <a href="https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys" target="_blank">your access key ID and secret access key</a>, or a named <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles" target="_blank">AWS profile</a>:

{{% choosable os "linux,macos" %}}

```bash
$ export AWS_ACCESS_KEY_ID="<YOUR_ACCESS_KEY_ID>"
$ export AWS_SECRET_ACCESS_KEY="<YOUR_SECRET_ACCESS_KEY>"
```

```bash
$ export AWS_PROFILE=<YOUR_PROFILE>
```

{{% /choosable %}}
{{% choosable os windows %}}

```powershell
> $env:AWS_ACCESS_KEY_ID = "<YOUR_ACCESS_KEY_ID>"
> $env:AWS_SECRET_ACCESS_KEY = "<YOUR_SECRET_ACCESS_KEY>"
```

```powershell
> $env:AWS_PROFILE = "<YOUR_PROFILE>"
```

{{% /choosable %}}

For additional configuration options, see [AWS Setup](/registry/packages/aws/installation-configuration/).

{{< get-started-stepper >}}
