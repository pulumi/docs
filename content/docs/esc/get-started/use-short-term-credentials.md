---
title_tag: Use Short Term Cloud Credentials | Pulumi ESC
title: Use short term cloud credentials
h1: "Use Short Term Cloud Credentials to Run Commands Without Local Secrets"
meta_desc: This page provides an overview on how to get short term cloud credeitnals and run commands without using local secrets using the "esc run" command.
weight: 6
menu:
  esc:
    parent: esc-get-started
---

Managing cloud credentials presents significant challenges for organizations of all sizes. Static, long-lived credentials, especially those stored in local environments introduce security risks and operational issues. Pulumi ESC’s built-in support for [dynamic login providers](/docs/esc/integrations/dynamic-login-credentials/), allows for best-practices like generating signed, short-term, scoped credentials issued via OIDC. These credentials can then be used in both Pulumi IaC workflows and external CLIs such as `aws`, `kubectl`.

In this example you will use the `esc run` command to execute AWS cli operations without having to manually configure AWS credentials in your local environment.

## Create the AWS OIDC configuration

To use dynamic credentials, you need to configure [OpenID Connect (OIDC)](/docs/esc/environments/configuring-oidc/) between Pulumi ESC and AWS. This requires creating two resources in AWS:

1. An IAM OIDC provider
2. An IAM role that trusts this provider and provides the necessary permissions

### Create the OIDC provider

1. Navigate to the [IAM console](https://console.aws.amazon.com/iam/)
2. In the navigation pane, choose **Identity providers**, then **Add provider**
3. Select **OpenID Connect** as the provider type
4. For the Provider URL, enter:
   ```
   https://api.pulumi.com/oidc
   ```
5. For the Audience, enter your Pulumi organization name
6. Click **Add provider**

### Create the IAM role

1. After creating the provider, click **Assign role** in the notification prompt
2. Select **Create a new role**
3. Ensure **Web identity** is selected, and verify:
   - The `api.pulumi.com/oidc` provider is selected
   - Your Pulumi organization is selected as the audience
4. Click **Next**
5. Select the permissions your role needs (**AmazonS3FullAccess** for S3 operations)
6. Click **Next**
7. Name your role (e.g., `pulumi-esc-s3-role`) and add an optional description
8. Click **Edit** on the Select trusted entities' section
9. Ensure the "Condition" subject claim includes `aws:` before your organization name (i.e.`"api.pulumi.com/oidc:aud": "aws:myorg"` )
10. Review and click **Create role**

Note the ARN of your new role as you'll need it in the next step.

{{< notes type="info" >}}
If you want to set environment level or even granular permissions in your trust policy, then we recommend using `subjectAttributes` property. See the [aws-login documentation](/docs/esc/integrations/dynamic-login-credentials/aws-login/) for more information.
{{< /notes >}}

## Create a Pulumi ESC environment

1. Navigate to the [Pulumi Cloud Console](https://app.pulumi.com/)  
2. Click **Environments** and then **Create environment**
3. Enter a name for your environment (e.g., `aws-s3-access`)
4. Click **Create environment**

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


Click **Save** to store your environment configuration.

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

## Additional OIDC authentication configurations

See the following guides to set up OIDC between Pulumi ESC and your specific cloud provider:

- [Configuring OIDC for AWS](/docs/pulumi-cloud/oidc/provider/aws/)
- [Configuring OIDC for Azure](/docs/pulumi-cloud/oidc/provider/azure/)
- [Configuring OIDC for Google Cloud](/docs/pulumi-cloud/oidc/provider/gcp/)
- [Configuring OIDC for Vault](/docs/pulumi-cloud/oidc/provider/vault/)

In the next section, you will learn how to retrieve secret values from external sources.

{{< get-started-stepper >}}
