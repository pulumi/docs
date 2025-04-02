---
title_tag: Configure OpenID Connect for Azure | Pulumi ESC
meta_desc: This page describes how to configure OIDC token exchange in Azure for use with Pulumi
title: Azure
h1: Configuring OpenID Connect for Azure
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    name: Azure
    parent: esc-configuring-oidc
    weight: 1
---

This document outlines the steps required to configure Pulumi to use OpenID Connect to authenticate with Azure. OIDC in Azure uses [workload identity federation](https://learn.microsoft.com/en-us/azure/active-directory/develop/workload-identity-federation) to access Azure resources via a Microsoft Entra App. Access to the temporary credentials is authorized using federated credentials that validate the contents of the OIDC token issued by the Pulumi Cloud.

## Prerequisites

* You must have access in the Azure Portal to create and configure Microsoft Entra App registrations.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official Azure documentation](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal).
{{< /notes >}}

## Create a Microsoft Entra application

In the navigation pane of the [Microsoft Entra console](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview):

1. Select **App registrations** and then click **New registration**.
2. Provide a name for your application (ex: `pulumi-esc-oidc-app`).
3. In the **Supported account types** section, select **Accounts in this organizational directory only**.
4. Click **Register**.

After the Microsoft Entra application has been created, take note of the following details:

* Subscription ID
* Application (client) ID
* Directory (tenant) ID

These values will be necessary when enabling OIDC for your service.

## Add federated credentials

Once you have created your new application registration, you will be redirected to the application's **Overview** page. In the left navigation menu:

1. Navigate to the **Certificates & secrets** pane.
2. Select the **Federated credentials** tab.
3. Click on the **Add credential** button. This will start the "Add a credential" wizard.
4. In the wizard, select **Other Issuer** as the **Federated credential scenario**.
5. Fill in the remaining form fields as follows:
    * **Issuer:** `https://api.pulumi.com/oidc`
    * **Subject Identifier:** must be a valid subject claim (see examples at the end of this section).
    * **Name:** An arbitrary name for the credential, e.g. "pulumi-oidc-credentials"
    * **Audience:** This is different between Pulumi deployments and ESC. For Deployments this is only the name of your Pulumi organization. For ESC this is the name of your Pulumi organization prefixed with `azure:` (e.g. `azure:{org}`).
{{< notes type="info" >}}
For environments in the `default` project the audience will use just the Pulumi organization name. This is to prevent regressions for legacy environments.
{{< /notes >}}

## Create a service principal

To provide Pulumi services the ability to deploy, manage, and interact with Azure resources, you need to associate your Microsoft Entra application with your Subscription or Resource Group.

1. Navigate to the [Subscriptions](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV1) page of the Azure portal.
2. Select the subscription to create the service principal in.
    * If you want to limit access to a specific resource group, go to the [Resource Groups](https://portal.azure.com/#view/HubsExtension/BrowseResourceGroups) page instead and select the desired resource group.
3. In the left navigation menu, select **Access control (IAM)**.
4. Click **Add** > **Add role assignment** to be taken to the **Add role assignment** wizard.
5. Under the **Job function roles** tab, select the desired role from the list, then click **Next**.
6. Select **User, group, or service principal**, then click **Select members**
7. Enter the name of the application you created in a previous step, select it from the list, then click **Select**.
8. Click **Next** and then **Review + assign**.

## Configure ESC for OIDC

To configure OIDC for Pulumi ESC, create a new environment in the [Pulumi Console](https://app.pulumi.com/). Make sure that you have the correct organization selected in the left-hand navigation menu. Then:

1. Click the **Environments** link.
2. Click the **Create environment** button.
3. Provide a project to create your new environment in and a name for your environment.
    * This should be the same as the identifier provided in the subject claim of your federated credentials.
4. Click the  **Create environment** button.
5. You will be presented with a split-pane view. Delete the default placeholder content in the editor and replace it with the following code:

    ```yaml
    values:
      azure:
        login:
          fn::open::azure-login:
            clientId: <your-client-id>
            tenantId: <your-tenant-id>
            subscriptionId: /subscriptions/<your-subscription-id>
            oidc: true
      environmentVariables:
        ARM_USE_OIDC: 'true'
        ARM_CLIENT_ID: ${azure.login.clientId}
        ARM_TENANT_ID: ${azure.login.tenantId}
        ARM_OIDC_TOKEN: ${azure.login.oidc.token}
        ARM_SUBSCRIPTION_ID: ${azure.login.subscriptionId}
    ```

6. Replace `<your-client-id>`, `<your-tenant-id>`, and `<your-subscription-id>` with the values from the previous steps.
7. Scroll to the bottom of the page and click **Save**.

You can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-project>/<your-environment>` command of the [ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-project>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>`, `<your-project>`, and `<your-environment>` with the values of your Pulumi organization, project, and environment file respectively. You should see output similar to the following:

```bash
{
  "azure": {
    "login": {
      "clientId": "b537....",
      "oidc": {
        "token": "eyJh...."
      },
      "subscriptionId": "0282....",
      "tenantId": "7061...."
    }
  },
  "environmentVariables": {
    "ARM_CLIENT_ID": "b537....",
    "ARM_OIDC_TOKEN": "eyJh....",
    "ARM_SUBSCRIPTION_ID": "0282....",
    "ARM_TENANT_ID": "7061....",
    "ARM_USE_OIDC": "true"
  }
}
```

To learn more about how to set up and use the various providers in Pulumi ESC, please refer to the [relevant Pulumi documentation](/docs/esc/integrations/)

## Subject claim customization

You can [customize](/docs/esc/environments/customizing-oidc-claims/) the subject claim in the OIDC token to control which Pulumi environments or users are allowed to assume a given IAM role. This allows for more granular access control than the default organization-level permissions

This is done by configuring the `subjectAttributes` setting. It expects an array of keys to include in it:

* `rootEnvironment.name`: the name of the environment that is opened first. This root environment in turn opens other imported environments
* `currentEnvironment.name`: the full name (including the project) of the environment where the ESC login provider and `subjectAttributes` are defined
* `pulumi.user.login`: the login identifier of the user opening the environment
* `pulumi.organization.login`: the login identifier of the organization

The subject always contains the following prefix `pulumi:environments:pulumi.organization.login:{ORGANIZATION_NAME}` and every key configured will be appended to this prefix. For example, consider the following environment:

```yaml
values:
  azure:
    login:
      fn::open::azure-login:
        ...
        subjectAttributes:
          - currentEnvironment.name
          - pulumi.user.login
```

The subject will be `pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:project/development:pulumi.user.login:userLogin`. Note how the keys and values are appended along with the prefix.

{{< notes type="warning" >}}

For environments within the legacy `default` project, the project will **not** be present in the subject to preserve backwards compatibility. The format of the subject claim when `subjectAttributes` are not set is `pulumi:environments:org:<organization name>:env:<environment name>`. If `currentEnvironment.name` is used as a custom subject attribute it will resolve to only the environment name (e.g. `pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:development:pulumi.user.login:personA`). Due to this it is recommended to move your environments out of the `default` project for best security practices.

{{< /notes >}}

## Subject claim example

Here is an example of a valid subject claim for the `project/development` environment of the `contoso` organization:

* `pulumi:environments:org:contoso:env:project/development`

The default format of the subject claim when `subjectAttributes` are not used is `pulumi:environments:org:<organization name>:env:<project name>/<environment name>`

{{< notes type="warning" >}}

If you are integrating Pulumi ESC with Pulumi IaC, the default subject identifier of the ESC environment will not work at this time. There is a [known issue](https://github.com/pulumi/pulumi/issues/14509) with the subject identifier's value sent to Azure from Pulumi.

Use 'subjectAttributes' to customize the subject identifier to work with Pulumi IaC. Alternatively, you can use this syntax: `pulumi:environments:org:contoso:env:<yaml>` when configuring the subject claim in your cloud provider account. Make sure to replace `contoso` with the name of your Pulumi organization and use the literal value of `<yaml>` as shown.

{{< /notes >}}
