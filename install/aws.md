---
title: "Configure Pulumi for AWS"
---

<!-- LINKS -->
[Pulumi AWS provider]: ../reference/aws.html
[iam-user-console]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console
[configure-aws-cli]: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

The [Pulumi AWS provider] uses the AWS SDK to manage and provision resources. 

{% include aws-resource-note.md %}

1.  If you haven't already, [install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/installing.html). If you're using [Homebrew](https://brew.sh/) on macOS, you can use the community-managed [awscli](http://formulae.brew.sh/formula/awscli) via `brew install awscli`.

2.  If necessary, [create an IAM user in the AWS console][iam-user-console] with type  **Programmatic access**. The IAM user should have sufficient rights to deploy and manage your program's resources. If you know the precise kinds of resources you wish to create and delete, you can restrict the IAM user accordingly.

3.  Configure the AWS CLI with the IAM credentials, such as with the `aws configure` command. For other configuration options, see the AWS article [Configuring the AWS CLI][configure-aws-cli].

    ```bash
    $ aws configure
    AWS Access Key ID [None]: AKIAI44QH8DHBEXAMPLE
    AWS Secret Access Key [None]: je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
    Default region name [None]: us-east-1
    Default output format [None]: text
    ```

Pulumi uses the AWS SDK to authenticate requests from your computer to AWS.  Your AWS credentials are never sent to
pulumi.com.
