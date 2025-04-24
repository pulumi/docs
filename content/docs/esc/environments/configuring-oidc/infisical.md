---
title_tag: Configure OpenID Connect for Infisical | Pulumi ESC
meta_desc: This page describes how to configure OIDC token exchange in Infisical for use with Pulumi
title: Infisical
h1: Configuring OpenID Connect for Infisical
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    name: Infisical
    parent: esc-configuring-oidc
    weight: 1
---

This document outlines the steps required to configure Pulumi to use OpenID Connect to authenticate with Infisical. OIDC
in Infisical uses [identities](https://infisical.com/docs/documentation/platform/identities/oidc-auth/general) to access
Infisical resources. Access to the temporary credentials is authorized using identities that validate the contents of
the OIDC token issued by the Pulumi Cloud.

## Prerequisites

* You must be an admin of your Infisical organization to create and configure identities.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is
subject to change. For the most current and precise information, always refer to
the [official Infisical documentation](https://infisical.com/docs/documentation/platform/identities/oidc-auth/general).
{{< /notes >}}

## Creating an Identity

In the navigation pane of the [Infisical app](https://app.infisical.com):

1. Select **Admin**, **Access Control**, **Identities** and then click **Create Identity**.
2. Provide a name for your application (ex: `pulumi-esc-oidc-app`).
3. Select a **Role** for the identity.
4. Click **Create**.

After the Identity has been created, take note of the following details:

* Identity ID

This value will be necessary when enabling OIDC for your service.

## Add OIDC Authentication

Once you have created your new identity, you will be redirected to the identity's **Overview** page. In the
Authentication section:

1. Remove the existing Universal Auth configuration.
2. Click on the **Add Auth Method** button. This will start an "Add Auth Method" wizard.
3. In the wizard, select **OIDC Auth** as the **Auth Method**.
4. Fill in the remaining form fields as follows:
    * **OIDC Discovery URL:** `https://api.pulumi.com/oidc`
    * **Issuer:** `https://api.pulumi.com/oidc`
    * **Subject:** This can be left empty. If it's empty, all ESC Environments of your organization would be able to assume this identity. We recommend configuring the subject claim for finer permission. (see examples at the end of this section).
    * **Audiences:** This is different between Pulumi deployments and ESC. For Deployments this is only the name of your Pulumi organization. For ESC this is the name of your Pulumi organization prefixed with `infisical:` (e.g. `infisical:{org}`).
{{< notes type="info" >}}
For environments in the `default` project the audience will use just the Pulumi organization name. This is to
prevent regressions for legacy environments.
{{< /notes >}}

## Configure ESC for OIDC

To configure OIDC for Pulumi ESC, create a new environment in the [Pulumi Console](https://app.pulumi.com/). Make sure
that you have the correct organization selected in the left-hand navigation menu. Then:

1. Click the **Environments** link.
2. Click the **Create environment** button.
3. Provide a project to create your new environment in and a name for your environment.
    * This should be the same as the identifier provided in the subject claim of your federated credentials.
4. Click the  **Create environment** button.
5. You will be presented with a split-pane view. Delete the default placeholder content in the editor and replace it
   with the following code:

    ```yaml
    values:
      infisical:
        login:
          fn::open::infisical-login:
            oidc:
              identityId: <your-identity-id>
      environmentVariables:
        INFISICAL_TOKEN: ${infisical.login.accessToken}
    ```

6. Replace `<your-identity-id>` with the value from the previous steps.
7. Scroll to the bottom of the page and click **Save**.

You can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-project>/<your-environment>` command of the [ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-project>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>`, `<your-project>`, and `<your-environment>` with the values of your Pulumi
organization, project, and environment file respectively. You should see output similar to the following:

```json
{
  "infisical": {
    "login": {
      "accessToken": "eyJh...."
    }
  },
  "environmentVariables": {
    "INFISICAL_TOKEN": "eyJh...."
  }
}
```

To learn more about how to set up and use the various providers in Pulumi ESC, please refer to
the [relevant Pulumi documentation](/docs/esc/integrations/)

## Subject claim customization

You can [customize](/docs/esc/environments/customizing-oidc-claims/) the subject claim in the OIDC token to control
which Pulumi environments or users are allowed to assume a given identity. This allows for more granular access control
than the default organization-level permissions.

This is done by configuring the `subjectAttributes` setting. It expects an array of keys to include in it:

* `rootEnvironment.name`: the name of the environment that is opened first. This root environment in turn opens other
  imported environments
* `currentEnvironment.name`: the full name (including the project) of the environment where the ESC login provider and
  `subjectAttributes` are defined
* `pulumi.user.login`: the login identifier of the user opening the environment
* `pulumi.organization.login`: the login identifier of the organization

The subject always contains the following prefix `pulumi:environments:pulumi.organization.login:{ORGANIZATION_NAME}` and
every key configured will be appended to this prefix. For example, consider the following environment:

```yaml
values:
  infisical:
    login:
      fn::open::infisical-login:
        oidc:
          identityId: <your-identity-id>
          subjectAttributes:
            - currentEnvironment.name
            - pulumi.user.login
```

The subject will be
`pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:project/development:pulumi.user.login:userLogin`.
Note how the keys and values are appended along with the prefix.

{{< notes type="warning" >}}

If not customized, the subject claim has the following format by default:

`pulumi:environments:org:<organization name>:env:<project name>/<environment name>`

{{< /notes >}}

{{< notes type="warning" >}}

For environments within the legacy `default` project, the project will **not** be present in the subject to preserve
backwards compatibility. The format of the subject claim when `subjectAttributes` are not set is
`pulumi:environments:org:<organization name>:env:<environment name>`. If `currentEnvironment.name` is used as a custom
subject attribute it will resolve to only the environment name (e.g.
`pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:development:pulumi.user.login:personA`).
Due to this it is recommended to move your environments out of the `default` project for best security practices.

{{< /notes >}}

## Subject claim example

Here is an example of a valid, not customized subject claim for the `project/development` environment of the `contoso`
organization:

* `pulumi:environments:org:contoso:env:project/development`

{{< notes type="warning" >}}

If you are integrating Pulumi ESC with Pulumi IaC, the default subject identifier of the ESC environment will not work
at this time. There is a [known issue](https://github.com/pulumi/pulumi/issues/14509) with the subject identifier's
value sent to Infisical from Pulumi.

Use 'subjectAttributes' to customize the subject identifier to work with Pulumi IaC. Alternatively, you can use this
syntax: `pulumi:environments:org:contoso:env:<yaml>` when configuring the subject claim in your cloud provider account.
Make sure to replace `contoso` with the name of your Pulumi organization and use the literal value of `<yaml>` as shown.

{{< /notes >}}
