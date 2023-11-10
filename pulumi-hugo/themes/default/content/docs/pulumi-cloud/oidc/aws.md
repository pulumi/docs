---
title_tag: Configure OpenID Connect for AWS | OIDC
meta_desc: This page describes how to configure OIDC token exchange in AWS for use with Pulumi Cloud
title: AWS
h1: Configuring OpenID Connect for AWS
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: openid-connect
        weight: 1

aliases:
- /docs/guides/oidc/aws
- /docs/intro/deployments/oidc/aws/
- /docs/pulumi-cloud/deployments/oidc/aws/
---

This document outlines the steps required to configure Pulumi to use OpenID Connect to authenticate with AWS. OIDC in AWS uses a web identity provider to assume an IAM role. Access to the IAM role is authorized using a trust policy that validates the contents of the OIDC token issued by the Pulumi Cloud.

## Prerequisites

* You must be an admin of your Pulumi organization.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).
{{< /notes >}}

## Create the Identity Provider

1. In the navigation pane of the [IAM console](https://console.aws.amazon.com/iam/), choose **Identity providers**, and then choose **Add provider**.
  {{< video title="Starting the Create Identity Provider wizard" src="./create-idp-start.mp4" autoplay="true" loop="true" >}}
2. In the **Provider type** section, click the radio button next to **OpenID Connect**.
3. For the **Provider URL**, provide the following URL: `https://api.pulumi.com/oidc`
4. Click the **Get thumbprint** button.
  {{< notes type="info" >}}
  The AWS console generates the thumbprint value on your behalf. However, if you are creating the OIDC provider programmatically, you will need to generate this value yourself and provide the thumbprint value as a part of your resource definition. You can learn more about what a thumbprint is and how to generate/verify it by referring to the [relevant AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html).
  {{< /notes >}}
5. For the **Audience** field, provide the name of your Pulumi organization. Then click **Add provider**.

## Configure the IAM Role and Trust Policy

Once you have created the identity provider, you will see a notification at the top of your screen prompting you to assign an IAM role.

1. Click the **Assign role** button.
2. Select the **Create a new role** option, then click **Next**.
  {{< video title="Prompt for assigning IAM role" src="./assign-iam-role-prompt.mp4" autoplay="true" loop="true" >}}
3. On the IAM **Create role** page, ensure the **Web identity** radio button is selected.
4. In the **Web identity** section:
    * Select `api.pulumi.com/oidc` under **Identity provider**.
    * Select the name of your Pulumi organization under **Audience**. Then click **Next**.
  {{< video title="Create IAM role wizard" src="./create-role-wizard.mp4" autoplay="true" loop="true" >}}
5. On the **Add permissions** page, select the permissions that you want to grant to your Pulumi service. Then click **Next**.
  {{< video title="Adding S3 permissions to IAM role" src="./create-role-add-perms.mp4" autoplay="true" loop="true" >}}
6. Provide a name and optional description for the IAM role. Then click **Create role**.
  {{< video title="Adding name and description to role then creating it" src="./create-role.mp4" autoplay="true" loop="true" >}}

Make a note of the IAM role's ARN; it will be necessary to enable OIDC for your service.

### Subject claim configuration and examples

For more granular access control, edit the trust policy of your IAM role to add the `sub` claim to the policy's conditions with a valid pattern as shown below.

#### Pulumi Deployments

In the following example, the role may only be assumed by stacks within the `Core` project of the `contoso` organization:

```json
"Condition": {
  "StringLike": {
    "api.pulumi.com/oidc:aud": "contoso",
    "api.pulumi.com/oidc:sub": "pulumi:deploy:org:contoso:project:Core:*"
  }
}
```

#### Pulumi ESC

In the following example, the role may only be assumed by the `development` environment within the `contoso` organization:

```json
"Condition": {
  "StringLike": {
    "api.pulumi.com/oidc:aud": "contoso",
    "api.pulumi.com/oidc:sub": "pulumi:environments:org:contoso:env:development"
  }
}
```

## Configure OIDC via the Pulumi Console

### Pulumi Deployments

{{% notes "info" %}}
In addition to the Pulumi Console, deployment settings including OIDC can be configured for a stack using the [pulumiservice.DeploymentSettings](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource or via the [REST API](/docs/pulumi-cloud/deployments/api/#patchsettings).
{{% /notes %}}

1. Navigate to your stack in the Pulumi Console.
2. Open the stack's "Settings" tab.
3. Choose the "Deploy" panel.
4. Under the "OpenID Connect" header, toggle "Enable AWS Integration".
5. Enter the ARN of the IAM role to created above in the "Role ARN" field.
6. Enter a name for the assumed role session in the "Session Name" field.
7. If you would like to use additional policies to further constrain the session's capabilities, enter the policies' ARNs separated by commas in the "Policy ARNs" field.
8. If you would like to constrain the duration of the assumed role session, enter a duration in the form "XhYmZs" in the "Session Duration" field.
9. Click the "Save deployment configuration" button.

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for AWS credentials using the specified IAM role prior to running any pre-commands or Pulumi operations. The fetched credentials are published in the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.

### Pulumi ESC

To configure OIDC for Pulumi ESC, create a new environment in the [Pulumi Console](https://app.pulumi.com/). Make sure that you have the correct organization selected in the left-hand navigation menu. Then:

1. Click the **Environments** link.
2. Click the **Create environment** button.
3. Provide a name for your environment.
4. Click the  **Create environment** button.
  {{< video title="Creating a new Pulumi ESC environment" src="./create-new-environment.mp4" autoplay="true" loop="true" >}}
5. You will be presented with a split-pane editor view. Delete the default placeholder content in the editor and replace it with the following code:

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

6. Replace `<your-oidc-iam-role-arn>` with the value from the previous steps.
7. Scroll to the bottom of the page and click **Save**.

{{< video title="Adding configuration to Pulumi ESC environment" src="./add-environment-config.mp4" autoplay="true" loop="true" >}}

You can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-environment>` command of the [ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>` and `<your-environment>` with the values of your Pulumi organization and environment file respectively. You should see output similar to the following:

```bash
{
  "aws": {
    "login": {
      "accessKeyId": "ASIA....",
      "secretAccessKey": "rtBS....",
      "sessionToken": "Fwo...."
    }
  },
  "environmentVariables": {
    "AWS_ACCESS_KEY_ID": "ASIA....",
    "AWS_SECRET_ACCESS_KEY": "rtBS....",
    "AWS_SESSION_TOKEN": "Fwo...."
  }
}
```

To learn more about how to set up and use the various providers in Pulumi ESC, please refer to the [relevant Pulumi documentation](/docs/pulumi-cloud/esc/providers/)

## Automate OIDC Configuration

Our [Examples](https://github.com/pulumi/examples) repository provides a wide variety of automations using Pulumi Infrastructure as Code (IaC). If you want to automate the configuration and deployment of OIDC between Pulumi and AWS, take a look at the following examples to help you get started:

* [Configure OIDC for ESC in Pulumi Python](https://github.com/pulumi/examples/tree/master/aws-py-oidc-provider-pulumi-cloud)
