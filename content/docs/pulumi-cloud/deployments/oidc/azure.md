---
title_tag: Configure OpenID Connect for Azure | OIDC
meta_desc: This page describes how to configure OIDC token exchange in Azure for use with Pulumi Deployments
title: Azure
h1: Configuring OpenID Connect for Azure
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Azure
    parent: pulumi-cloud-deployments-oidc
    weight: 2
    identifier: pulumi-cloud-deployments-oidc-azure
aliases:
- /docs/guides/oidc/provider/azure
- /docs/intro/deployments/oidc/provider/azure/
- /docs/pulumi-cloud/deployments/oidc/provider/azure/
- /docs/pulumi-cloud/oidc/provider/azure/
- /docs/pulumi-cloud/oidc/azure/
- /docs/pulumi-cloud/access-management/oidc/provider/azure/ 
---

{{< notes type="info" >}}
Pulumi ESC should be the preferred approach over the Deployments OIDC integrations since it's more portable and easier to set up. For ESC OIDC setup instructions, see [Configuring OIDC for Azure in ESC](/docs/esc/environments/configuring-oidc/azure/).
{{< /notes >}}

This document outlines the steps required to configure Pulumi Deployments to use OpenID Connect to authenticate with Azure. OIDC in Azure uses [workload identity federation](https://learn.microsoft.com/en-us/azure/active-directory/develop/workload-identity-federation) to access Azure resources via a Microsoft Entra App. Access to the temporary credentials is authorized using federated credentials that validate the contents of the OIDC token issued by the Pulumi Cloud.

## Prerequisites

* You must have access in the Azure Portal to create and configure Microsoft Entra App registrations.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official Azure documentation](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal).
{{< /notes >}}

## Create a Microsoft Entra application

In the navigation pane of the [Microsoft Entra console](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview):

1. Select **App registrations** and then click **New registration**.
2. Provide a name for your application (ex: `pulumi-deployments-oidc-app`).
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
    * **Audience:** The name of your Pulumi organization.

### Subject claim examples

Because Azure's federated credentials require that the subject identifier exactly matches an OIDC token's subject claim, this process must be repeated for each permutation of the subject claim that is possible for a stack. For example, in order to enable all of the valid operations on a stack named `dev` of the `core` project in the `contoso` organization, you would need to create credentials for each of the following subject identifiers:

* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:preview:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:update:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:refresh:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:destroy:scope:write`

## Create a service principal

To provide Pulumi Deployments the ability to deploy, manage, and interact with Azure resources, you need to associate your Microsoft Entra application with your Subscription or Resource Group.

1. Navigate to the [Subscriptions](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV1) page of the Azure portal.
2. Select the subscription to create the service principal in.
    * If you want to limit access to a specific resource group, go to the [Resource Groups](https://portal.azure.com/#view/HubsExtension/BrowseResourceGroups) page instead and select the desired resource group.
3. In the left navigation menu, select **Access control (IAM)**.
4. Click **Add** > **Add role assignment** to be taken to the **Add role assignment** wizard.
5. Under the **Job function roles** tab, select the desired role from the list, then click **Next**.
6. Select **User, group, or service principal**, then click **Select members**
7. Enter the name of the application you created in a previous step, select it from the list, then click **Select**.
8. Click **Next** and then **Review + assign**.

## Configure OIDC in the Pulumi console

{{% notes "info" %}}
In addition to the Pulumi Console, deployment settings including OIDC can be configured for a stack using the [pulumiservice.DeploymentSettings](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource or via the [REST API](/docs/pulumi-cloud/deployments/api/#patchsettings).
{{% /notes %}}

1. Navigate to your stack in the [Pulumi Console](https://app.pulumi.com/).
2. Open the stack's **Settings** tab.
3. Choose the **Deploy** panel.
4. Under the **OpenID Connect** header, toggle **Enable Azure Integration**.
5. Enter the client and tenant IDs for the app registration created above in the **Client ID** and **Tenant ID** fields, respectively.
6. Enter the ID of the subscription you want to use in the **Subscription ID** field.
7. Click the **Save deployment configuration** button.

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for Azure credentials using the specified AAD App prior to running any pre-commands or Pulumi operations. The fetched credentials are published in the `ARM_CLIENT_ID`, `ARM_TENANT_ID`,  and `ARM_SUBSCRIPTION_ID` environment variables. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.
