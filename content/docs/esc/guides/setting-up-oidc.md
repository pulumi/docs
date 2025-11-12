---
title_tag: Setting Up OIDC | Pulumi ESC
title: Setting Up OIDC
h1: Setting Up OIDC with Pulumi ESC
meta_desc: Learn how to configure OpenID Connect (OIDC) with Pulumi ESC to generate short-lived cloud credentials dynamically.
menu:
  esc:
    parent: esc-guides
    identifier: esc-guides-setting-up-oidc
    weight: 4
aliases:
  - /docs/esc/get-started/use-short-term-credentials/
  - /docs/pulumi-cloud/esc/get-started/use-short-term-credentials/
---

This guide shows you how to configure OpenID Connect (OIDC) between Pulumi ESC and AWS to generate short-lived credentials dynamically. Using [dynamic login providers](/docs/esc/integrations/dynamic-login-credentials/), you can eliminate static credentials and generate temporary, scoped credentials on demand. These credentials work with CLI workflows, CI/CD pipelines, Pulumi IaC, and any tool that uses AWS credentials.

This guide demonstrates using `esc run` to execute AWS CLI commands with dynamically generated credentials, without configuring static AWS credentials locally.

## Prerequisites

- [Pulumi account](https://app.pulumi.com/signup) created
- [ESC CLI](/docs/esc-cli/) installed
- AWS account with administrative access to create IAM roles and OIDC providers
- [AWS CLI](https://aws.amazon.com/cli/) installed (for testing the integration)

## Create the AWS OIDC configuration

To use dynamic credentials, you need to configure OpenID Connect (OIDC) between Pulumi ESC and AWS. This requires creating two resources in AWS:

1. An IAM OIDC provider
2. An IAM role that trusts this provider and provides the necessary permissions

### Create the OIDC provider

1. Navigate to the [AWS IAM console](https://console.aws.amazon.com/iam/)
2. In the navigation pane, choose **Identity providers**, then **Add provider**
3. Select **OpenID Connect** as the provider type
4. For the Provider URL, enter: `https://api.pulumi.com/oidc`
5. For the Audience, enter the name of your Pulumi organization prefixed with `aws:` (e.g. `aws:{org}`)
   - **Note:** For legacy ESC environments in the `default` project, use just the Pulumi organization name without the `aws:` prefix
6. Select **Add provider**

### Create the IAM role

1. After creating the provider, select **Assign role** in the notification prompt
2. Select **Create a new role**
3. Ensure **Web identity** is selected, and verify that
   - `api.pulumi.com/oidc` provider is selected
   - Your Pulumi organization (prefixed with `aws:`) is selected as the audience
4. Select **Next**
5. Select the permissions your role needs (e.g. **AmazonS3FullAccess** for S3 operations)
6. Select **Next**
7. Name your role (e.g., `pulumi-esc-s3-role`) and add an optional description
8. Select **Edit** on the Select trusted entities' section
9. Ensure the Condition checks the audience claim with `aws:` before your organization name (i.e. `"api.pulumi.com/oidc:aud": "aws:myorg"`, or just `myorg` for legacy default project environments)
10. Review and select **Create role**

Example trust policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::123456789123:oidc-provider/api.pulumi.com/oidc"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "api.pulumi.com/oidc:aud": "aws:my-org"
                }
            }
        }
    ]
}
```

Note the ARN of your new role as you'll need it in the next step.

{{< notes type="info" >}}
If you want to set environment level or even granular permissions in your trust policy, then we recommend using `subjectAttributes` property. See the [aws-login documentation](/docs/esc/integrations/dynamic-login-credentials/aws-login/) for more information.
{{< /notes >}}

## Create a Pulumi ESC environment

1. Navigate to the [Pulumi Cloud Console](https://app.pulumi.com/)  
2. Select **Environments** and then **Create environment**
3. Enter a name for your environment (e.g., `aws-s3-access`)
4. Select **Create environment**

## Configure the AWS Provider integration

In the environment editor, replace the default content with:

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

Be sure to replace `<your-oidc-iam-role-arn>` with the ARN of the IAM role you created.

![An image of the ESC environment editor role trust policy](/docs/esc/assets/esc-environment-editor.png)

Select **Save** to store your environment configuration.

## Use esc run to execute AWS commands

`esc run` is a [Pulumi ESC command](/docs/esc/cli/commands/esc_run/) that securely injects environment variables, including secrets and dynamically generated credentials, into a command’s execution environment. Now you can use it to run AWS CLI commands without local credential configuration:

```bash
esc run <your-org-name>/<your-project-name>/<your-environment-name> aws s3 ls
```

You should be presented with a list of S3 buckets in the account associated with your credentials.

```bash

# example command and output
esc run pulumi/my-project/dev-environment aws s3 ls

2023-12-10 02:52:46 my-bucket-4a67543
2023-11-16 21:37:40 my-bucket-4b1e6cb
2023-10-27 21:04:59 my-bucket-50da4ad
2023-11-02 18:57:36 my-bucket-51385eb
```

Behind the scenes, Pulumi ESC dynamically generated short-lived AWS credentials by assuming the IAM role you configured. These credentials are injected into the command environment as variables, allowing the AWS CLI to use them for authentication.

ESC dynamic credentials and the `esc run` command can be used for various scenarios:

- **CI/CD pipelines**: Use dynamic credentials in your automation workflows
- **Application testing**: Run tests against cloud resources without managing credentials
- **Secure script execution**: Execute scripts that interact with AWS without embedding credentials
- **Team collaboration**: Provide team members with secure, scoped access to resources

## Next steps

- [Integrate with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/) - Use dynamic credentials in your infrastructure code
- [Running commands with esc run](/docs/esc/guides/running-commands-with-esc/) - Learn more about injecting secrets into commands
- [Integrating external secrets](/docs/esc/guides/external-secrets/) - Pull secrets from cloud vaults

### Provider-specific OIDC configuration

For detailed OIDC setup instructions for other cloud providers:

- [Configuring OIDC for AWS](/docs/esc/environments/configuring-oidc/aws/)
- [Configuring OIDC for Azure](/docs/esc/environments/configuring-oidc/azure/)
- [Configuring OIDC for Google Cloud](/docs/esc/environments/configuring-oidc/gcp/)
- [Configuring OIDC for Vault](/docs/esc/environments/configuring-oidc/vault/)
