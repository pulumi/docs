---
title: AWS Setup
meta_desc: This page provides an overview of how to setup and configure credentials
           for the Pulumi AWS Provider.
aliases: ["/docs/reference/clouds/aws/setup/"]
---

<!-- markdownlint-disable url -->
[Pulumi AWS provider]: {{< prelref "./" >}}
[iam-user-console]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console
[iam-manage-keys]: https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html
[configure-aws-cli]: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
<!-- markdownlint-enable url -->

The [Pulumi AWS provider] uses the AWS SDK to manage and provision resources.

{{< aws-resource-note >}}

There are multiple ways to connect Pulumi to your AWS credentials.  The
[SDK instructions](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html) cover this in
detail -- including advanced options -- however we will look at the two most popular approaches below:

* Environment variables
* A shared credentials file, usually managed by the AWS CLI

## Getting Your Credentials

In either case, you will need to make sure you have an IAM user in [the AWS console][iam-user-console] with
**Programmatic access**.  The IAM user should have sufficient rights to deploy and manage your program's resources.  If
you know the precise kinds of resources you wish to create and delete, you can restrict the IAM user accordingly.
You'll also need [an access key][iam-manage-keys] for your user.

There are two parts to each key, both shown in the IAM console after creating it:

* `<YOUR_ACCESS_KEY_ID>`: your access key's ID
* `<YOUR_SECRET_ACCESS_KEY>`: your access key's secret

> No matter which option you pick, Pulumi uses the AWS SDK to authenticate requests from your computer to AWS.
> As a result, your AWS credentials are never sent to pulumi.com.

## Shared Credentials File

A credentials file is a plaintext file on your machine that contains your access keys. The file must be named
`credentials` and is located underneath `.aws/` directory in your home directory.  This approach is
recommended because it supports Amazon's recommended approach for securely managing multiple roles.

### Using the CLI

To create this file using the CLI, you must first
[install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/installing.html).  If you're using
[Homebrew](https://brew.sh/) on macOS, you can use the community-managed
[awscli](http://formulae.brew.sh/formula/awscli) via `brew install awscli`.

After installing the CLI, configure it with your IAM credentials, typically using the `aws configure` command.  For
other configuration options, see the AWS article [Configuring the AWS CLI][configure-aws-cli].

```bash
$ aws configure
AWS Access Key ID [None]: <YOUR_ACCESS_KEY_ID>
AWS Secret Access Key [None]: <YOUR_SECRET_ACCESS_KEY>
Default region name [None]:
Default output format [None]:
```

This will have created the `~/.aws/credentials` file and populated it with the expected settings.

### Creating By Hand

It is possible to create this file by hand.  For example:

```ini
[default]
aws_access_key_id = <YOUR_ACCESS_KEY_ID>
aws_secret_access_key = <YOUR_SECRET_ACCESS_KEY>
```

If you want to specify multiple profiles, those are listed in different sections:

```ini
[default]
aws_access_key_id = <YOUR_DEFAULT_ACCESS_KEY_ID>
aws_secret_access_key = <YOUR_DEFAULT_SECRET_ACCESS_KEY>

[test-account]
aws_access_key_id = <YOUR_TEST_ACCESS_KEY_ID>
aws_secret_access_key = <YOUR_TEST_SECRET_ACCESS_KEY>

[prod-account]
aws_access_key_id = <YOUR_PROD_ACCESS_KEY_ID>
aws_secret_access_key = <YOUR_PROD_SECRET_ACCESS_KEY>
```

In this case, you will need to set the `AWS_PROFILE` environment variable to the name of the profile to use.

## Environment Variables

Although credentials are recommended, the SDK will prefer environment variables over any other settings:

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`

This makes it easy to temporarily override your credentials settings, quickly switch to a different access key,
or configure AWS access from within an environment that might not have an AWS CLI, such as inside of CI.

To configure these, simply `export` them on Linux or OS X:

```bash
$ export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
$ export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>`
```

Or use the `set` command on Windows:

```bat
> set AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
> set AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```
