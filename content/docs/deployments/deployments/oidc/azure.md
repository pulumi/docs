---
title_tag: Configure OpenID Connect for Azure with Pulumi Deployments | OIDC
meta_desc: This page describes how to configure OIDC token exchange in Azure for use with Pulumi Deployments
title: Azure
h1: Configuring OpenID Connect for Azure with Pulumi Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: Azure
    parent: deployments-deployments-oidc
    weight: 2
    identifier: deployments-deployments-oidc-azure
aliases:
  - /docs/administration/access-identity/oidc/provider/azure/
  - /docs/guides/oidc/provider/azure
  - /docs/intro/deployments/oidc/provider/azure/
  - /docs/pulumi-cloud/access-management/oidc/provider/azure/
  - /docs/pulumi-cloud/deployments/oidc/azure/
  - /docs/pulumi-cloud/deployments/oidc/provider/azure/
  - /docs/pulumi-cloud/oidc/azure/
  - /docs/pulumi-cloud/oidc/provider/azure/
---

{{< esc-recommendation >}}

This document outlines the steps required to configure Pulumi Deployments to use OpenID Connect to authenticate with Azure. OIDC in Azure uses [workload identity federation](https://learn.microsoft.com/en-us/azure/active-directory/develop/workload-identity-federation) to access Azure resources via a Microsoft Entra App. Access to the temporary credentials is authorized using federated credentials that validate the contents of the OIDC token issued by Pulumi Cloud.

Configuring OIDC for Azure involves two sides:

1. **Azure** — register a Microsoft Entra application with federated credentials that trust Pulumi Cloud, and grant its service principal access to your resources. You can do this in the [Azure portal](#using-the-azure-portal) or [programmatically](#using-infrastructure-as-code).
1. **Pulumi Deployments** — enable the Azure OIDC integration for your stack so that each deployment exchanges its OIDC token for credentials from that application. You can do this in the [Pulumi Cloud console](#using-the-pulumi-cloud-console) or [programmatically with the Pulumi Service provider](#using-infrastructure-as-code-1).

## Prerequisites

* You must have access in the Azure Portal to create and configure Microsoft Entra App registrations.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official Azure documentation](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal).
{{< /notes >}}

## Configure Azure

### Using the Azure portal

#### Create a Microsoft Entra application

In the navigation pane of the [Microsoft Entra console](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview):

1. Select **App registrations** and then click **New registration**.
1. Provide a name for your application (ex: `pulumi-deployments-oidc-app`).
1. In the **Supported account types** section, select **Accounts in this organizational directory only**.
1. Click **Register**.

After the Microsoft Entra application has been created, take note of the following details:

* Subscription ID
* Application (client) ID
* Directory (tenant) ID

These values will be necessary when enabling OIDC for your service.

#### Add federated credentials

Once you have created your new application registration, you will be redirected to the application's **Overview** page. In the left navigation menu:

1. Navigate to the **Certificates & secrets** pane.
1. Select the **Federated credentials** tab.
1. Click on the **Add credential** button. This will start the "Add a credential" wizard.
1. In the wizard, select **Other Issuer** as the **Federated credential scenario**.
1. Fill in the remaining form fields as follows:
    * **Issuer:** `https://api.pulumi.com/oidc`
    * **Subject Identifier:** must be a valid subject claim (see examples at the end of this section).
    * **Name:** An arbitrary name for the credential, e.g. "pulumi-oidc-credentials".
    * **Audience:** Enter the name of your Pulumi organization.

##### Subject claim examples

Because Azure's federated credentials require that the subject identifier exactly matches an OIDC token's subject claim, this process must be repeated for each permutation of the subject claim that is possible for a stack. For example, in order to enable all of the valid operations on a stack named `dev` of the `core` project in the `contoso` organization, you would need to create credentials for each of the following subject identifiers:

* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:preview:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:update:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:refresh:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:destroy:scope:write`

#### Create a service principal

To provide Pulumi services the ability to deploy, manage, and interact with Azure resources, you need to associate your Microsoft Entra application with your Subscription or Resource Group.

1. Navigate to the [Subscriptions](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBladeV1) page of the Azure portal.
1. Select the subscription to create the service principal in.
    * If you want to limit access to a specific resource group, go to the [Resource Groups](https://portal.azure.com/#view/HubsExtension/BrowseResourceGroups) page instead and select the desired resource group.
1. In the left navigation menu, select **Access control (IAM)**.
1. Click **Add** > **Add role assignment** to be taken to the **Add role assignment** wizard.
1. Under the **Job function roles** tab, select the desired role from the list, then click **Next**.
1. Select **User, group, or service principal**, then click **Select members**
1. Enter the name of the application you created in a previous step, select it from the list, then click **Select**.
1. Click **Next** and then **Review + assign**.

### Using infrastructure as code

You can create the Entra application, federated credentials, service principal, and role assignment with a Pulumi program instead of the portal. The following example uses TypeScript with the [Azure AD provider](/registry/packages/azuread/) and the [Azure Native provider](/registry/packages/azure-native/); the same resources are available in every Pulumi language.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azuread from "@pulumi/azuread";
import * as authorization from "@pulumi/azure-native/authorization";

const org = "contoso";
const project = "core";
const stack = "dev";

const current = authorization.getClientConfigOutput();

// Register an Entra application and a matching service principal.
const app = new azuread.Application("pulumi-deployments-oidc", {
    displayName: "pulumi-deployments-oidc",
});

const servicePrincipal = new azuread.ServicePrincipal("pulumi-deployments-oidc", {
    clientId: app.clientId,
});

// Grant the service principal access to your subscription. "Contributor" is shown
// here; scope this down for production.
const contributorRoleId = "b24988ac-6180-42a0-ab88-20f7382dd24c";
const subscriptionScope = pulumi.interpolate`/subscriptions/${current.subscriptionId}`;

new authorization.RoleAssignment("pulumi-deployments-contributor", {
    principalId: servicePrincipal.id,
    principalType: "ServicePrincipal",
    roleDefinitionId: pulumi.interpolate`${subscriptionScope}/providers/Microsoft.Authorization/roleDefinitions/${contributorRoleId}`,
    scope: subscriptionScope,
});

// Azure federated credentials require an exact subject match (no wildcards), so add
// one credential per operation.
for (const operation of ["preview", "update", "refresh", "destroy"]) {
    new azuread.ApplicationFederatedIdentityCredential(`cred-${operation}`, {
        applicationId: app.id,
        displayName: operation,
        issuer: "https://api.pulumi.com/oidc",
        audiences: [org],
        subject: `pulumi:deploy:org:${org}:project:${project}:stack:${stack}:operation:${operation}:scope:write`,
    });
}

export const clientId = app.clientId;
export const tenantId = current.tenantId;
export const subscriptionId = current.subscriptionId;
```

## Configure Pulumi Deployments

### Using the Pulumi Cloud console

1. Navigate to your stack in the [Pulumi Console](https://app.pulumi.com/signin).
1. Open the stack's **Settings** tab.
1. Choose the **Deploy** panel.
1. Under the **OpenID Connect** header, toggle **Enable Azure Integration**.
1. Enter the client and tenant IDs for the app registration created above in the **Client ID** and **Tenant ID** fields, respectively.
1. Enter the ID of the subscription you want to use in the **Subscription ID** field.
1. Click the **Save deployment configuration** button.

### Using infrastructure as code

You can manage the same deployment settings in source control with the [`pulumiservice.DeploymentSettings`](/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource (the OIDC configuration is set under `operationContext.oidc.azure`). Deployment settings can also be configured via the [REST API](/docs/deployments/deployments/api/#patchsettings).

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

new pulumiservice.DeploymentSettings("deployment-settings", {
    organization: "contoso",
    project: "core",
    stack: "dev",
    operationContext: {
        oidc: {
            azure: {
                clientId: "<application-client-id>",
                tenantId: "<directory-tenant-id>",
                subscriptionId: "<subscription-id>",
            },
        },
    },
});
```

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for Azure credentials using the specified AAD App prior to running any pre-commands or Pulumi operations. The fetched credentials are published in the `ARM_CLIENT_ID`, `ARM_TENANT_ID`,  and `ARM_SUBSCRIPTION_ID` environment variables. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.

For a full end-to-end example that configures both sides together, see [this TypeScript example](https://github.com/pulumi/workshops/blob/main/az-pulumi-deployments/az-oidc-setup/index.ts).
