---
title_tag: Configure OpenID Connect for Azure | OIDC
meta_desc: This page describes how to configure OIDC token exchange in Azure for use with Pulumi
title: Azure
h1: Configuring OpenID Connect for Azure
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: openid-connect-provider
        weight: 1

aliases:
- /docs/guides/oidc/provider/azure
- /docs/intro/deployments/oidc/provider/azure/
- /docs/pulumi-cloud/deployments/oidc/provider/azure/
- /docs/pulumi-cloud/oidc/provider/azure/
- /docs/pulumi-cloud/oidc/azure/ 
---

This document outlines the steps required to configure Pulumi to use OpenID Connect to authenticate with Azure. OIDC in Azure uses [workload identity federation](https://learn.microsoft.com/en-us/azure/active-directory/develop/workload-identity-federation) to access Azure resources via a Microsoft Entra App. Access to the temporary credentials is authorized using federated credentials that validate the contents of the OIDC token issued by the Pulumi Cloud.

## Prerequisites

* You must be an admin of your Pulumi organization.
* You must have access in the Azure Portal to create and configure Microsoft Entra App registrations.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official Azure documentation](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal).
{{< /notes >}}

## Create a Microsoft Entra Application

In the navigation pane of the [Microsoft Entra console](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview):

1. Select **App registrations** and then click **New registration**.
2. Provide a name for your application (ex: `pulumi-esc-oidc-app`).
3. In the **Supported account types** section, select **Accounts in this organizational directory only**.
4. Click **Register**.

After the Microsoft Entra App has been created, take note of the following details:

* Subscription ID
* Application (client) ID
* Directory (tenant) ID

These values will be necessary when enabling OIDC for your service.

## Add Federated Credentials

Once you have created your new application registration, you will be redirected to the application's **Overview** page. In the left navigation menu:

1. Navigate to the **Certificates & secrets** pane.
2. Select the **Federated credentials** tab.
3. Click on the **Add credential** button. This will start the "Add a credential" wizard.
4. In the wizard, select **Other Issuer** as the **Federated credential scenario**.
5. Fill in the remaining form fields as follows:
    * **Issuer:** `https://api.pulumi.com/oidc`
    * **Subject Identifier:** must be a valid subject claim (see examples at the end of this section).
    * **Name:** An arbitrary name for the credential, e.g. "pulumi-oidc-credentials"
    * **Audience:** The name of your Pulumi organization.

### Subject claim examples

Depending on the Pulumi service you are configuring OIDC for, the value of the subject claim will be different. You can learn more about configuring OIDC with Pulumi by referring to the [relevant documentation](/docs/pulumi-cloud/oidc/).

The below sections show examples that correspond to each OIDC-supported service.

#### Pulumi Deployments

Because Azure's federated credentials require that the subject identifier exactly matches an OIDC token's subject claim, this process must be repeated for each permutation of the subject claim that is possible for a stack. For example, in order to enable all of the valid operations on a stack named `dev` of the `core` project in the `contoso` organization, you would need to create credentials for each of the following subject identifiers:

* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:preview:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:update:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:refresh:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:destroy:scope:write`

#### Pulumi ESC

The below is an example of a valid subject claim for the `development` environment of the `contoso` organization:

* `pulumi:environments:org:contoso:env:development`

{{< notes type="warning" >}}

If you are integrating Pulumi ESC with Pulumi IaC, the default subject identifier of the ESC environment will not work at this time. There is a [known issue](https://github.com/pulumi/pulumi/issues/14509) with the subject identifier's value sent to Azure from Pulumi.

Use 'subjectAttributes' to customize the subject identifier to work with Pulumi IaC. Alternatively, you can use this syntax: `pulumi:environments:org:contoso:env:<yaml>` when configuring the subject claim in your cloud provider account. Make sure to replace `contoso` with the name of your Pulumi organization and use the literal value of `<yaml>` as shown.

{{< /notes >}}

##### Subject customization

It is possible to customize the OIDC token subject claim by setting configuring the `subjectAttributes` setting. It expects an array of keys to include in it:

* `rootEnvironment.name`: the name of the root evironment being evaluated
* `currentEnvironment.name`: the name of the current environment being evaluated
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

The subject will be `pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:development:pulumi.user.login:userLogin`. Note how the keys and values are appended along with the prefix.

## Create a Service Principal

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

## Configure OIDC in the Pulumi Console

### Pulumi Deployments

{{% notes "info" %}}
In addition to the Pulumi Console, deployment settings including OIDC can be configured for a stack using the [pulumiservice.DeploymentSettings](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource or via the [REST API](/docs/pulumi-cloud/deployments/api/#patchsettings).
{{% /notes %}}

1. Navigate to your stack in the [Pulumi Console](https://app.pulumi.com/).
2. Open the stack's "Settings" tab.
3. Choose the "Deploy" panel.
4. Under the "OpenID Connect" header, toggle "Enable Azure Integration".
5. Enter the client and tenant IDs for the app registration created above in the "Client ID" and "Tenant ID" fields, repsectively.
6. Enter the ID of the subscription you want to use in the "Subscription ID" field.
7. Click the "Save deployment configuration" button.

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for Azure credentials using the specified AAD App prior to running any pre-commands or Pulumi operations. The fetched credentials are published in the `ARM_CLIENT_ID`, `ARM_TENANT_ID`,  and `ARM_SUBSCRIPTION_ID` environment variables. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.

### Pulumi ESC

To configure OIDC for Pulumi ESC, create a new environment in the [Pulumi Console](https://app.pulumi.com/). Make sure that you have the correct organization selected in the left-hand navigation menu. Then:

1. Click the **Environments** link.
2. Click the **Create environment** button.
3. Provide a name for your environment.
    * This should be the same as the name provided in the subject claim of your federated credentials.
4. Click the  **Create environment** button.
  {{< video title="Creating a new Pulumi ESC environment" src="https://www.pulumi.com/uploads/create-new-environment.mp4" autoplay="true" loop="true" >}}
5. You will be presented with a split-pane editor view. Delete the default placeholder content in the editor and replace it with the following code:

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

* `esc open <your-org>/<your-environment>` command of the [ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>` and `<your-environment>` with the values of your Pulumi organization and environment file respectively. You should see output similar to the following:

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

To learn more about how to set up and use the various providers in Pulumi ESC, please refer to the [relevant Pulumi documentation](/docs/pulumi-cloud/esc/providers/)

## Automate OIDC Configuration

Our [Examples](https://github.com/pulumi/examples) repository provides a wide variety of automations using Pulumi Infrastructure as Code (IaC). If you want to automate the configuration and deployment of OIDC between Pulumi and Azure, take a look at the following examples to help you get started:

* [Configure OIDC for ESC in Pulumi Python](https://github.com/pulumi/examples/tree/master/azure-py-oidc-provider-pulumi-cloud)
* [Configure OIDC for Deployments in Pulumi TypeScript](https://github.com/pulumi/workshops/blob/main/az-pulumi-deployments/az-oidc-setup/index.ts)
