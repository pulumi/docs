---
title_tag: Configure OpenID Connect for Google Cloud | OIDC
meta_desc: This page describes how to configure OIDC token exchange in Google Cloud for use with Pulumi
title: Google Cloud
h1: Configuring OpenID Connect for Google Cloud
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: openid-connect
        weight: 1

aliases:
- /docs/guides/oidc/gcp
- /docs/intro/deployments/oidc/gcp/
- /docs/pulumi-cloud/deployments/oidc/gcp/
---

This document outlines the steps required to configure Pulumi to use OpenID Connect to authenticate with Google Cloud. OIDC in Google Cloud uses [workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation) to allow access to resources. Access to the resources is authorized using attribute conditions that validate the contents of the OIDC token issued by the Pulumi Cloud.

## Prerequisites

* You must be an admin of your Pulumi organization.
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
8. In the **Audiences** section, select the **Allowed audiences** radio button. Provide the name of your Pulumi organization as the value, then click **Continue**.
9. In the **Configure provider attributes** section, provide the value of `assertion.sub` in the **OIDC 1** field. Then click **Save**.

## Configure a Service Account

Once you have created your workload identity pool and provider, you will be directed to the pool details page.

### Create a new service account

1. Navigate to the [Service Accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts) page.

WIP

### Grant access to the service account

1. Navigate to your workload identity pool's page in the console. Then click the **Grant Access** button.
2. In the **Select service account** dropdown, select the desired service account to associate with the pool.
3. Under the **Select principals** section, click the **Only identities matching the filter** radio button.
4. In the **Attribute name** dropdown, select **Subject**.
5. In the **Attribute value** field, provide a valid subject claim (see examples at the end of this section). Then click **Save**.

Make a note of the project ID, workload identity pool ID, provider ID, and service account email address from the previous steps. These will be necessary to enable OIDC for your service.

### Subject claim examples

Depending on the Pulumi service you are configuring OIDC for, the value of the subject claim will be different. You can learn more about configuring OIDC with Pulumi by referring to the [relevant documentation](/docs/pulumi-cloud/oidc/).

The below sections show examples that correspond to each OIDC-supported service.

#### Pulumi Deployments

The below is an example of a valid subject claim for the `dev` stack of the `contoso` organization:

* `pulumi:deploy:org:contoso:project:core:stack:dev:operation:*:scope:write`

#### Pulumi ESC

The below is an example of a valid subject claim for the `development` environment of the `contoso` organization:

* `pulumi:environments:org:contoso:env:development`

You can learn more about setting up OIDC for Pulumi ESC by referring to the [relevant Pulumi documentation](/docs/pulumi-cloud/esc/providers/#setting-up-oidc).

## Enabling OIDC for your Stack via the Pulumi Console

{{% notes "info" %}}
In addition to the Pulumi Console, deployment settings including OIDC can be configured for a stack using the [pulumiservice.DeploymentSettings](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource or via the [REST API](/docs/pulumi-cloud/deployments/api/#patchsettings).
{{% /notes %}}

1. Navigate to your stack in the Pulumi Console.
2. Open the stack's "Settings" tab.
3. Choose the "Deploy" panel.
4. Under the "OpenID Connect" header, toggle "Enable Google Cloud Integration".
5. Enter the numerical ID of your Google Cloud project in the "Project ID" field.
6. Enter the workload pool ID, identity provider ID, and service account email address in the "Workload Pool ID", "Identity Provider ID", and "Service Account Email Address" fields.
7. If desired, enter the stack's Google Cloud region in the "Region" field. This is typically unnecessary.
8. If you would like to constrain the duration of the temporary Google Cloud credentials, enter a duration in the form "XhYmZs" in the "Session Duration" field.
9. Click the "Save deployment configuration" button.

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for Google Cloud credentials using the specified federated identity prior to running any pre-commands or Pulumi operations. The fetched credentials are published as a credential configuration in the `GOOGLE_CREDENTIALS` environment variable. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.
