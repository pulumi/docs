---
title_tag: Configure OpenID Connect for AWS with Pulumi Deployments | OIDC
meta_desc: This page describes how to configure OIDC token exchange in AWS for use with Pulumi Deployments
title: AWS
h1: Configuring OpenID Connect for AWS with Pulumi Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: AWS
    parent: pulumi-cloud-deployments-oidc
    weight: 1
    identifier: pulumi-cloud-deployments-oidc-aws
aliases:
- /docs/guides/oidc/provider/aws
- /docs/intro/deployments/oidc/provider/aws/
- /docs/pulumi-cloud/deployments/oidc/provider/aws/
- /docs/pulumi-cloud/oidc/provider/aws/
- /docs/pulumi-cloud/oidc/aws/
- /docs/pulumi-cloud/access-management/oidc/provider/aws/
---

{{% notes type="info" %}}
Pulumi ESC provides a more portable and easier-to-set-up alternative to the Deployments OIDC integration described here. For most use cases, we recommend using [Pulumi ESC for AWS OIDC configuration](/docs/esc/environments/configuring-oidc/aws/).
{{% /notes %}}

This document outlines the steps required to configure Pulumi Deployments to use OpenID Connect to authenticate with AWS. OIDC in AWS uses a web identity provider to assume an IAM role. Access to the IAM role is authorized using a trust policy that validates the contents of the OIDC token issued by Pulumi Cloud.

## Create the identity provider

1. In the navigation pane of the [IAM console](https://console.aws.amazon.com/iam/), choose **Identity providers**, and then choose **Add provider**.
  {{< video title="Starting the Create Identity Provider wizard" src="https://www.pulumi.com/uploads/create-idp-start.mp4" autoplay="true" loop="true" >}}
2. In the **Provider type** section, click the radio button next to **OpenID Connect**.
3. For the **Provider URL**, provide the following URL: `https://api.pulumi.com/oidc`
4. For the **Audience** field, enter the name of your Pulumi organization. Then click **Add provider**.

## Configure the IAM role and trust policy

Once you have created the identity provider, you will see a notification at the top of your screen prompting you to assign an IAM role.

1. Click the **Assign role** button.
2. Select the **Create a new role** option, then click **Next**.
  {{< video title="Prompt for assigning IAM role" src="https://www.pulumi.com/uploads/assign-iam-role-prompt.mp4" autoplay="true" loop="true" >}}
3. On the IAM **Create role** page, ensure the **Web identity** radio button is selected.
4. In the **Web identity** section:
    * Select `api.pulumi.com/oidc` under **Identity provider**.
    * Select the name of your Pulumi organization under **Audience**. Then click **Next**.
  {{< video title="Create IAM role wizard" src="https://www.pulumi.com/uploads/create-role-wizard.mp4" autoplay="true" loop="true" >}}
5. On the **Add permissions** page, select the permissions that you want to grant to your Pulumi deployments. Then click **Next**.
  {{< video title="Adding S3 permissions to IAM role" src="https://www.pulumi.com/uploads/create-role-add-perms.mp4" autoplay="true" loop="true" >}}
6. Provide a name and optional description for the IAM role. Then click **Create role**.
  {{< video title="Adding name and description to role then creating it" src="https://www.pulumi.com/uploads/create-role.mp4" autoplay="true" loop="true" >}}

Make a note of the IAM role's ARN; it will be necessary to enable OIDC for your deployment.

For more granular access control, edit the trust policy of your IAM role with [Token claims](/docs/pulumi-cloud/deployments/oidc/#custom-claims). The `sub` claim can be customized as shown below.

In the following example, the role may only be assumed by stacks within the `Core` project of the `contoso` organization:

```json
"Condition": {
  "StringEquals": {
    "api.pulumi.com/oidc:aud": "contoso"
  },
  "StringLike": {
    "api.pulumi.com/oidc:sub": "pulumi:deploy:org:contoso:project:Core:*"
  }
}
```

## Configure OIDC via the Pulumi console

{{% notes "info" %}}
In addition to the Pulumi Console, deployment settings including OIDC can be configured for a stack using the [pulumiservice.DeploymentSettings](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource or via the [REST API](/docs/pulumi-cloud/deployments/api/#patchsettings).
{{% /notes %}}

1. Navigate to your stack in the Pulumi Console.
2. Open the stack's "Settings" tab.
3. Choose the "Deploy" panel.
4. Under the "OpenID Connect" header, toggle "Enable AWS Integration".
5. Enter the ARN of the IAM role created above in the "Role ARN" field.
6. Enter a name for the assumed role session in the "Session Name" field.
7. If you would like to use additional policies to further constrain the session's capabilities, enter the policies' ARNs separated by commas in the "Policy ARNs" field.
8. If you would like to constrain the duration of the assumed role session, enter a duration in the form "XhYmZs" in the "Session Duration" field.
9. Click the "Save deployment configuration" button.

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for AWS credentials using the specified IAM role prior to running any pre-commands or Pulumi operations. The fetched credentials are published in the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.
