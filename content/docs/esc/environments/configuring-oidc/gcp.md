---
title_tag: Configure OpenID Connect for Google Cloud | Pulumi ESC
meta_desc: This page describes how to configure OIDC token exchange in Google Cloud for use with Pulumi ESC
title: Google Cloud
h1: Configuring OpenID Connect for Google Cloud
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    name: Google Cloud
    parent: esc-configuring-oidc
    weight: 1
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
8. In the **Audiences** section, select the **Allowed audiences** radio button. The value for this field is different between pulumi deployments and ESC. For Deployments enter just the name of your Pulumi organization. For ESC enter the name of your Pulumi organization prefixed with `gcp:` (e.g. `gcp:{org}`). Then click **Continue**.
  {{< notes type="info" >}}
  For environments in the `default` project the audience will use just the Pulumi organization name. This is to prevent regressions for legacy environments.
  {{< /notes >}}
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

Below is an example of a valid subject claim for the `project/development` environment of the `contoso` organization:

* `pulumi:environments:org:contoso:env:project/development`

The default format of the subject claim when `subjectAttributes` are not used is `pulumi:environments:org:<organization name>:env:<project name>/<environment name>`

{{< notes type="warning" >}}

For environments within the legacy `default` project, the project will **not** be present in the subject to preserve backwards compatibility. The format of the subject claim when `subjectAttributes` are not set is `pulumi:environments:org:<organization name>:env:<environment name>`. If `currentEnvironment.name` is used as a custom subject attribute it will resolve to only the environment name (e.g. `pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:development:pulumi.user.login:personA`). Due to this it is recommended to move your environments out of the `default` project for best security practices.

{{< /notes >}}
{{< notes type="warning" >}}

If you are integrating Pulumi ESC with Pulumi IaC, the default subject identifier of the ESC environment will not work at this time. There is a [known issue](https://github.com/pulumi/pulumi/issues/14509) with the subject identifier's value sent to Azure from Pulumi.

Use 'subjectAttributes' to customize the subject identifier to work with Pulumi IaC. Alternatively, you can use this syntax: `pulumi:environments:org:contoso:env:<yaml>` when configuring the subject claim in your cloud provider account. Make sure to replace `contoso` with the name of your Pulumi organization and use the literal value of `<yaml>` as shown.

{{< /notes >}}

### Subject customization

It is possible to customize the OIDC token subject claim by setting configuring the `subjectAttributes` setting. It expects an array of keys to include in it:

* `rootEnvironment.name`: the name of the environment that is opened first. This root environment in turn opens other imported environments
* `currentEnvironment.name`: the full name (including the project) of the environment where the ESC login provider and `subjectAttributes` are defined
* `pulumi.user.login`: the login identifier of the user opening the environment
* `pulumi.organization.login`: the login identifier of the organization

The subject always contains the following prefix `pulumi:environments:pulumi.organization.login:{ORGANIZATION_NAME}` and every key configured will be appended to this prefix. For example, consider the following environment:

```yaml
values:
  gcp:
    login:
      fn::open::gcp-login:
        oidc:
          ...
          subjectAttributes:
            - currentEnvironment.name
            - pulumi.user.login
```

The subject will be `pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:project/development:pulumi.user.login:userLogin`. Note how the keys and values are appended along with the prefix.

## Configure ESC for OIDC

To configure OIDC for Pulumi ESC, create a new environment in the [Pulumi Console](https://app.pulumi.com/). Make sure that you have the correct organization selected in the left-hand navigation menu. Then:

1. Click the **Environments** link.
2. Click the **Create environment** button.
3. Provide a project to create your new environment in and a name for your environment.
    * This should be the same as the identifier provided in the subject claim of your federated credentials.
4. Click the **Create environment** button.
  {{< video title="Creating a new Pulumi ESC environment" src="https://www.pulumi.com/uploads/create-new-environment.mp4" autoplay="true" loop="true" >}}
5. You will be presented with a split-pane document and table view. Delete the default placeholder content in the editor and replace it with the following code:

    ```yaml
    values:
      gcp:
        login:
          fn::open::gcp-login:
            project: <your-project-id>
            oidc:
              workloadPoolId: <your-pool-id>
              providerId: <your-provider-id>
              serviceAccount: <your-service-account>
      environmentVariables:
        GOOGLE_PROJECT: ${gcp.login.project}
        CLOUDSDK_AUTH_ACCESS_TOKEN: ${gcp.login.accessToken}
      pulumiConfig:
        gcp:accessToken: ${gcp.login.accessToken}
    ```

6. Replace `<your-project-id>`, `<your-pool-id>`, `<your-provider-id>`, and `<your-service-account>` with the values from the previous steps.
7. Scroll to the bottom of the page and click **Save**.

You can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-project>/<your-environment>` command of the [ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-project>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>`, `<your-project>`, and `<your-environment>` with the values of your Pulumi organization, project, and environment file respectively. You should see output similar to the following:

```bash
{
  "environmentVariables": {
    "GOOGLE_PROJECT": 111111111111
    "CLOUDSDK_AUTH_ACCESS_TOKEN": "ya29...."
  },
  "gcp": {
    "login": {
      "accessToken": "ya29.....",
      "expiry": "2023-11-09T11:12:41Z",
      "project": 111111111111,
      "tokenType": "Bearer"
    }
  },
  "pulumiConfig": {
    "gcp:accessToken": "ya29...."
  }
}
```

To learn more about how to set up and use the various providers in Pulumi ESC, please refer to the [relevant Pulumi documentation](/docs/pulumi-cloud/esc/providers/).
