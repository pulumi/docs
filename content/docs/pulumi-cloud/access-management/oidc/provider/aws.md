---
title_tag: Configure OpenID Connect for AWS | OIDC
meta_desc: This page describes how to configure OIDC token exchange in AWS for use with Pulumi Cloud
title: AWS
h1: Configuring OpenID Connect for AWS
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: AWS
    parent: pulumi-cloud-access-management-oidc-provider
    weight: 1
    identifier: pulumi-cloud-access-management-oidc-provider-aws
aliases:
- /docs/guides/oidc/provider/aws
- /docs/intro/deployments/oidc/provider/aws/
- /docs/pulumi-cloud/deployments/oidc/provider/aws/
- /docs/pulumi-cloud/oidc/provider/aws/
- /docs/pulumi-cloud/oidc/aws/
---

This document outlines the steps required to configure Pulumi to use OpenID Connect to authenticate with AWS. OIDC in AWS uses a web identity provider to assume an IAM role. Access to the IAM role is authorized using a trust policy that validates the contents of the OIDC token issued by the Pulumi Cloud.

## Prerequisites

* You must be an admin of your Pulumi organization.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).
{{< /notes >}}

## Create the identity provider

1. In the navigation pane of the [IAM console](https://console.aws.amazon.com/iam/), choose **Identity providers**, and then choose **Add provider**.
  {{< video title="Starting the Create Identity Provider wizard" src="https://www.pulumi.com/uploads/create-idp-start.mp4" autoplay="true" loop="true" >}}
2. In the **Provider type** section, click the radio button next to **OpenID Connect**.
3. For the **Provider URL**, provide the following URL: `https://api.pulumi.com/oidc`
4. For the **Audience** field, the value will differ between Pulumi deployments and ESC. For Deployments the value is only the name of your Pulumi organization. For ESC the value is the name of your Pulumi organization prefixed with `aws:` (e.g. `aws:{org}`). Then click **Add provider**.
  {{< notes type="info" >}}
  For environments in the `default` project, the audience will use just the Pulumi organization name. This is to prevent regressions for legacy environments.
  {{< /notes >}}

## Configure the IAM role and trust policy

Once you have created the identity provider, you will see a notification at the top of your screen prompting you to assign an IAM role.

1. Click the **Assign role** button.
2. Select the **Create a new role** option, then click **Next**.
  {{< video title="Prompt for assigning IAM role" src="https://www.pulumi.com/uploads/assign-iam-role-prompt.mp4" autoplay="true" loop="true" >}}
3. On the IAM **Create role** page, ensure the **Web identity** radio button is selected.
4. In the **Web identity** section:
    * Select `api.pulumi.com/oidc` under **Identity provider**.
    * Select the name of your Pulumi organization under **Audience** (or if using ESC, prefixed with `aws:`). Then click **Next**.
  {{< video title="Create IAM role wizard" src="https://www.pulumi.com/uploads/create-role-wizard.mp4" autoplay="true" loop="true" >}}
5. On the **Add permissions** page, select the permissions that you want to grant to your Pulumi service. Then click **Next**.
  {{< notes type="info" >}}
  For setting up an AWS Pulumi insights account, you can use the role `ReadOnlyAccess` managed by [aws](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html).
  {{< /notes >}}
  {{< video title="Adding S3 permissions to IAM role" src="https://www.pulumi.com/uploads/create-role-add-perms.mp4" autoplay="true" loop="true" >}}
6. Provide a name and optional description for the IAM role. Then click **Create role**.
  {{< video title="Adding name and description to role then creating it" src="https://www.pulumi.com/uploads/create-role.mp4" autoplay="true" loop="true" >}}

Make a note of the IAM role's ARN; it will be necessary to enable OIDC for your service.

For more granular access control, edit the trust policy of your IAM role with [Token claims](/docs/pulumi-cloud/access-management/oidc/provider/#custom-claims) for each service. The `sub` claim can be customized as shown below.

### Pulumi Deployments

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

### Pulumi ESC

Consider the following ESC definition for `project/development` environment opened by user `personA`:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          ...
          subjectAttributes:
            - currentEnvironment.name
            - pulumi.user.login
```

The OIDC subject claim for this environment would be `pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:project/development:pulumi.user.login:personA`. The role may only be assumed by `project/development` environment and user `personA` within the `contoso` organization:

```json
"Condition": {
  "StringEquals": {
    "api.pulumi.com/oidc:aud": "aws:contoso",
    "api.pulumi.com/oidc:sub": "pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:project/development:pulumi.user.login:personA"
  }
}
```

The subject always contains the prefix `pulumi:environments:pulumi.organization.login:{ORGANIZATION_NAME}` and every key configured will be appended to this prefix. The list of all possible options for `subjectAttributes` are:

* `rootEnvironment.name`: the name of the environment that is opened first. This root environment in turn opens other imported environments
* `currentEnvironment.name`: the full name (including the project) of the environment where the ESC login provider and `subjectAttributes` are defined
* `pulumi.user.login`: the login identifier of the user opening the environment
* `pulumi.organization.login`: the login identifier of the organization

When importing multiple environments into Pulumi IaC Stack Config, each environment is resolved separately. For example, if you import multiple environments into your Pulumi Stack with `rootEnvironment.name` attribute defined in all of them, then each `rootEnvironment.name` will resolve to the environment name where it is defined.

The default format of the subject claim when `subjectAttributes` are not used is `pulumi:environments:org:<organization name>:env:<project name>/<environment name>`

{{< notes type="warning" >}}

For environments within the legacy `default` project, the project will **not** be present in the subject to preserve backwards compatibility. The format of the subject claim when `subjectAttributes` are not set is `pulumi:environments:org:<organization name>:env:<environment name>`. If `currentEnvironment.name` is used as a custom subject attribute it will resolve to only the environment name (e.g. `pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:development:pulumi.user.login:personA`). Due to this it is recommended to move your environments out of the `default` project for best security practices.

{{< /notes >}}

{{< notes type="info" >}}

If you are integrating Pulumi ESC with Pulumi IaC, the default subject identifier of the environment will be `pulumi:environments:org:contoso:env:<yaml>`.  The literal value of `<yaml>` need to be used and will be the same for all environments. Hence, for best security practices we recommend using `subjectAttributes`. If you want to set environment level or even granular permissions in your trust policy, then we recommend using `subjectAttributes` property.

{{< /notes >}}

## Configure OIDC via the Pulumi console

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
3. Provide a project to create your new environment in and a name for your environment.
4. Click the **Create environment** button.
  {{< video title="Creating a new Pulumi ESC environment" src="https://www.pulumi.com/uploads/create-new-environment.mp4" autoplay="true" loop="true" >}}
5. You will be presented with a split-pane editor. Delete the default placeholder content in the editor and replace it with the following code:

    ```yaml
    values:
      aws:
        login:
          fn::open::aws-login:
            oidc:
              duration: 1h
              roleArn: <your-oidc-iam-role-arn>
              sessionName: pulumi-environments-session
              subjectAttributes:
                - currentEnvironment.name
                - pulumi.user.login
      environmentVariables:
        AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
        AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
        AWS_SESSION_TOKEN: ${aws.login.sessionToken}
    ```

6. Replace `<your-oidc-iam-role-arn>` with the value from the previous steps.
7. Scroll to the bottom of the page and click **Save**.

{{< video title="Adding configuration to Pulumi ESC environment" src="https://www.pulumi.com/uploads/add-environment-config.mp4" autoplay="true" loop="true" >}}

You can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-project>/<your-environment>` command of the [ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-project>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>`, `<your-project>`, and `<your-environment>` with the values of your Pulumi organization, project, and environment file respectively. You should see output similar to the following:

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

To learn more about how to set up and use the various providers in Pulumi ESC, please refer to the [relevant Pulumi documentation](/docs/esc/integrations/)

## Automate OIDC configuration

Our [Examples](https://github.com/pulumi/examples) repository provides a wide variety of automations using Pulumi Infrastructure as Code (IaC). If you want to automate the configuration and deployment of OIDC between Pulumi and AWS, take a look at the following examples to help you get started:

* [Configure OIDC for ESC in Pulumi Python](https://github.com/pulumi/examples/tree/master/aws-py-oidc-provider-pulumi-cloud)
