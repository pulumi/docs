---
title_tag: Configure OpenID Connect for Google Cloud with Pulumi Deployments | OIDC
meta_desc: This page describes how to configure OIDC token exchange in Google Cloud for use with Pulumi Deployments
title: Google Cloud
h1: Configuring OpenID Connect for Google Cloud with Pulumi Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: Google Cloud
    parent: deployments-guides-oidc
    weight: 3
    identifier: deployments-guides-oidc-gcp
aliases:
  - /docs/administration/access-identity/oidc/provider/gcp/
  - /docs/guides/oidc/provider/gcp
  - /docs/intro/deployments/oidc/provider/gcp/
  - /docs/pulumi-cloud/access-management/oidc/provider/gcp/
  - /docs/pulumi-cloud/deployments/oidc/gcp/
  - /docs/deployments/deployments/oidc/gcp/
  - /docs/pulumi-cloud/deployments/oidc/provider/gcp/
  - /docs/pulumi-cloud/oidc/gcp/
  - /docs/pulumi-cloud/oidc/provider/gcp/
---

{{< esc-recommendation >}}

This document outlines the steps required to configure Pulumi Deployments to use OpenID Connect to authenticate with Google Cloud. OIDC in Google Cloud uses [workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation) to allow access to resources. Access to the resources is authorized using attribute conditions that validate the contents of the OIDC token issued by Pulumi Cloud.

Configuring OIDC for Google Cloud involves two sides:

1. **Google Cloud** — create a workload identity pool and OIDC provider that trust Pulumi Cloud, and a service account your deployments can impersonate. You can do this in the [Google Cloud console](#using-the-google-cloud-console) or [programmatically](#using-infrastructure-as-code).
1. **Pulumi Deployments** — enable the Google Cloud OIDC integration for your stack so that each deployment exchanges its OIDC token for credentials from that service account. You can do this in the [Pulumi Cloud console](#using-the-pulumi-cloud-console) or [programmatically with the Pulumi Service provider](#using-infrastructure-as-code-1).

## Prerequisites

* You must create a [Google Cloud project with the required APIs enabled](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#configure)

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the official [Google Cloud documentation](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers).
{{< /notes >}}

## Configure Google Cloud

### Using the Google Cloud console

#### Create a workload identity pool and provider

1. Navigate to the [Workload Identity Pools page](https://console.cloud.google.com/projectselector2/iam-admin/workload-identity-pools) in the Google Cloud console.
1. Select your Google Cloud project.
1. Click the **Create Pool** button.
1. Provide a name and an optional description, then click **Continue**
1. In the **Add a provider to pool** dropdown, select **OpenID Connect (OIDC)**.
1. Provide a name for the provider.
1. In the **Issuer** field, enter `https://api.pulumi.com/oidc`.
1. In the **Audiences** section, select the **Allowed audiences** radio button. Enter the name of your Pulumi organization. Then click **Continue**.
1. In the **Configure provider attributes** section, provide the value of `assertion.sub` in the **OIDC 1** field. Then click **Save**.

#### Configure a service account

Once you have created your workload identity pool and provider, you will be directed to the pool details page. If you already have an appropriate service account created, skip ahead to the steps found in the [Grant access to the service account](#grant-access-to-the-service-account) section. Otherwise, continue through the steps below to create a new one.

##### Create a new service account

1. Navigate to the [Service Accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts) page.
1. Select your Google Cloud project.
1. Click "Create Service Account".
1. Enter a value for the **Service account name** field. Then click **Create And Continue**
    * The **Service account ID** field will auto-populate based on this value.
1. In the **Grant this service account access to project** section, select the role(s) that provides the relevant access to your Pulumi service. Then click **Continue**.
1. Leave the values in the next section blank and click **Done**.

##### Grant access to the service account

1. In your workload identity pool's details page, click the **Grant Access** button.
1. In the **Select service account** dropdown, select the desired service account to associate with the pool.
1. Under the **Select principals** section, click the **Only identities matching the filter** radio button.
1. In the **Attribute name** dropdown, select **Subject**.
1. In the **Attribute value** field, provide a valid subject claim (see examples at the end of this section). Then click **Save**.

Make a note of the project number, workload identity pool ID, provider ID, and service account email address from the previous steps. These will be necessary to enable OIDC for your service.

##### Subject claim examples

To enable valid operations on a specific stack, Google federated credentials require an exact match on the OIDC token subject claim. Unfortunately, the subject identifier does *not* currently allow wildcards. Therefore, you must create credentials for each permutation of the subject claim that is possible for the stack.

For example, to enable all of the valid operations on a stack named `dev` of the `core` project in the `contoso` organization, you would need to create credentials for each of the following subject identifiers:

* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:preview:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:update:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:refresh:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:destroy:scope:write`

### Using infrastructure as code

You can create the workload identity pool, provider, and service account with a Pulumi program instead of the console. The following example uses TypeScript and the [Google Cloud provider](/registry/packages/gcp/); the same resources are available in every Pulumi language.

```typescript
import * as gcp from "@pulumi/gcp";
import * as pulumi from "@pulumi/pulumi";

const org = "contoso";
const project = "core";
const stack = "dev";

const gcpProjectId = "<your-gcp-project-id>";         // e.g. "my-project"
const gcpProjectNumber = "<your-gcp-project-number>"; // e.g. "123456789012"

// Create a workload identity pool and an OIDC provider that trusts Pulumi Cloud.
const pool = new gcp.iam.WorkloadIdentityPool("pulumi-deployments", {
    workloadIdentityPoolId: "pulumi-deployments",
});

const poolProvider = new gcp.iam.WorkloadIdentityPoolProvider("pulumi-deployments", {
    workloadIdentityPoolId: pool.workloadIdentityPoolId,
    workloadIdentityPoolProviderId: "pulumi-deployments",
    attributeMapping: {
        "google.subject": "assertion.sub",
    },
    oidc: {
        issuerUri: "https://api.pulumi.com/oidc",
        allowedAudiences: [org],
    },
});

// Create a service account with the permissions your deployments need.
const account = new gcp.serviceaccount.Account("pulumi-deployments", {
    accountId: "pulumi-deployments",
    displayName: "Pulumi Deployments OIDC",
});

new gcp.projects.IAMMember("pulumi-deployments-editor", {
    project: gcpProjectId,
    role: "roles/editor",
    member: pulumi.interpolate`serviceAccount:${account.email}`,
});

// Google federated credentials require an exact subject match (no wildcards), so bind
// one principal per operation to let it impersonate the service account.
for (const operation of ["preview", "update", "refresh", "destroy"]) {
    const subject = `pulumi:deploy:org:${org}:project:${project}:stack:${stack}:operation:${operation}:scope:write`;
    new gcp.serviceaccount.IAMMember(`wif-${operation}`, {
        serviceAccountId: account.name,
        role: "roles/iam.workloadIdentityUser",
        member: pulumi.interpolate`principal://iam.googleapis.com/projects/${gcpProjectNumber}/locations/global/workloadIdentityPools/${pool.workloadIdentityPoolId}/subject/${subject}`,
    });
}

export const workloadPoolId = pool.workloadIdentityPoolId;
export const providerId = poolProvider.workloadIdentityPoolProviderId;
export const serviceAccountEmail = account.email;
```

## Configure Pulumi Deployments

### Using the Pulumi Cloud console

1. Navigate to your stack in the Pulumi Console.
1. Open the stack's "Settings" tab.
1. Choose the "Deploy" panel.
1. Under the "OpenID Connect" header, toggle "Enable Google Cloud Integration".
1. Enter the numerical ID of your Google Cloud project in the "Project Number" field.
1. Enter the workload pool ID, identity provider ID, and service account email address in the "Workload Pool ID", "Identity Provider ID", and "Service Account Email Address" fields.
1. If desired, enter the stack's Google Cloud region in the "Region" field. This is typically unnecessary.
1. If you would like to constrain the duration of the temporary Google Cloud credentials, enter a duration in the form "XhYmZs" in the "Session Duration" field.
1. Click the "Save deployment configuration" button.

### Using infrastructure as code

You can manage the same deployment settings in source control with the [`pulumiservice.DeploymentSettings`](/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource (the OIDC configuration is set under `operationContext.oidc.gcp`). Deployment settings can also be configured via the [REST API](/docs/deployments/deployments/api/#patchsettings).

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

new pulumiservice.DeploymentSettings("deployment-settings", {
    organization: "contoso",
    project: "core",
    stack: "dev",
    operationContext: {
        oidc: {
            gcp: {
                projectId: "<your-gcp-project-number>", // the numerical project ID
                workloadPoolId: "pulumi-deployments",
                providerId: "pulumi-deployments",
                serviceAccount: "<service-account-email>",
                // Optional: region, tokenLifetime
            },
        },
    },
});
```

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for Google Cloud credentials using the specified federated identity prior to running any pre-commands or Pulumi operations. The fetched credentials are published as a credential configuration in the `GOOGLE_CREDENTIALS` environment variable. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.
