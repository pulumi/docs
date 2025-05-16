---
title_tag: Configure OpenID Connect for Google Cloud with Pulumi Deployments | OIDC
meta_desc: This page describes how to configure OIDC token exchange in Google Cloud for use with Pulumi Deployments
title: Google Cloud
h1: Configuring OpenID Connect for Google Cloud with Pulumi Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Google Cloud
    parent: pulumi-cloud-deployments-oidc
    weight: 3
    identifier: pulumi-cloud-deployments-oidc-gcp
aliases:
- /docs/guides/oidc/provider/gcp
- /docs/intro/deployments/oidc/provider/gcp/
- /docs/pulumi-cloud/deployments/oidc/provider/gcp/
- /docs/pulumi-cloud/oidc/provider/gcp/
- /docs/pulumi-cloud/oidc/gcp/
- /docs/pulumi-cloud/access-management/oidc/provider/gcp/
---

{{% notes type="info" %}}
Pulumi ESC provides a more portable and easier-to-set-up alternative to the Deployments OIDC integration described here. For most use cases, we recommend using [Pulumi ESC for Google Cloud OIDC configuration](/docs/esc/environments/configuring-oidc/gcp/).
{{% /notes %}}

This document outlines the steps required to configure Pulumi Deployments to use OpenID Connect to authenticate with Google Cloud. OIDC in Google Cloud uses [workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation) to allow access to resources. Access to the resources is authorized using attribute conditions that validate the contents of the OIDC token issued by Pulumi Cloud.

## Prerequisites

* You must create a [Google Cloud project with the required APIs enabled](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#configure)

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the official [Google Cloud documentation](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers).
{{< /notes >}}

## Create a Workload Identity Pool and Provider

1. Navigate to the [Workload Identity Pools page](https://console.cloud.google.com/projectselector2/iam-admin/workload-identity-pools) in the Google Cloud console.
2. Select your Google Cloud project.
3. Click the **Create Pool** button.
4. Provide a name and an optional description. then click **Continue**
5. In the **Add a provider to pool** dropdown, select **OpenID Connect (OIDC)**.
6. Provide a name for the provider.
7. In the **Issuer** field, enter `https://api.pulumi.com/oidc`.
8. In the **Audiences** section, select the **Allowed audiences** radio button. Enter the name of your Pulumi organization. Then click **Continue**.
9. In the **Configure provider attributes** section, provide the value of `assertion.sub` in the **OIDC 1** field. Then click **Save**.

## Configure a Service Account

Once you have created your workload identity pool and provider, you will be directed to the pool details page. If you already have an appropriate service account created, skip ahead to the steps found in the [Grant access to the service account](/docs/pulumi-cloud/oidc/provider/gcp/#grant-access-to-the-service-account) section. Otherwise, continue through the steps below to create a new one.

### Create a new service account

1. Navigate to the [Service Accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts) page.
2. Select your Google Cloud project.
3. Click "Create Service Account".
4. Enter a value for the **Service account name** field. Then click **Create And Continue**
    * The **Service account ID** field will auto-populate based on this value.
5. In the **Grant this service account access to project** section, select the role(s) that provides the relevant access to your Pulumi service. Then click **Continue**.
6. Leave the values in the next section blank and click **Done**.

### Grant access to the service account

1. In your workload identity pool's details page, click the **Grant Access** button.
2. In the **Select service account** dropdown, select the desired service account to associate with the pool.
3. Under the **Select principals** section, click the **Only identities matching the filter** radio button.
4. In the **Attribute name** dropdown, select **Subject**.
5. In the **Attribute value** field, provide a valid subject claim (see examples at the end of this section). Then click **Save**.

Make a note of the project ID, workload identity pool ID, provider ID, and service account email address from the previous steps. These will be necessary to enable OIDC for your service.

### Subject claim examples

To enable valid operations on a specific stack, Google federated credentials require an exact match on the OIDC token subject claim. Unfortunately, the subject identifier does *not* currently allow wildcards. Therefore, you must create credentials for each permutation of the subject claim that is possible for the stack.

For example, to enable all of the valid operations on a stack named `dev` of the `core` project in the `contoso` organization, you would need to create credentials for each of the following subject identifiers:

* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:preview:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:update:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:refresh:scope:write`
* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:destroy:scope:write`

## Configure OIDC in the Pulumi Console

{{% notes "info" %}}
In addition to the Pulumi Console, deployment settings including OIDC can be configured for a stack using the [pulumiservice.DeploymentSettings](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource or via the [REST API](/docs/pulumi-cloud/deployments/api/#patchsettings).
{{% /notes %}}

1. Navigate to your stack in the Pulumi Console.
2. Open the stack's "Settings" tab.
3. Choose the "Deploy" panel.
4. Under the "OpenID Connect" header, toggle "Enable Google Cloud Integration".
5. Enter the numerical ID of your Google Cloud project in the "Project Number" field.
6. Enter the workload pool ID, identity provider ID, and service account email address in the "Workload Pool ID", "Identity Provider ID", and "Service Account Email Address" fields.
7. If desired, enter the stack's Google Cloud region in the "Region" field. This is typically unnecessary.
8. If you would like to constrain the duration of the temporary Google Cloud credentials, enter a duration in the form "XhYmZs" in the "Session Duration" field.
9. Click the "Save deployment configuration" button.

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for Google Cloud credentials using the specified federated identity prior to running any pre-commands or Pulumi operations. The fetched credentials are published as a credential configuration in the `GOOGLE_CREDENTIALS` environment variable. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.
