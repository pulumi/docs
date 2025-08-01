---
title_tag: Configure OpenID Connect for Vault | Pulumi ESC
meta_desc: This page describes how to configure OIDC token exchange in Vault for use with Pulumi ESC
title: Vault
h1: Configuring OpenID Connect for Vault
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    name: Vault
    parent: esc-configuring-oidc
    weight: 7
aliases:
  - /docs/pulumi-cloud/oidc/provider/vault
  - /docs/pulumi-cloud/oidc/provider/vault/
  - /docs/pulumi-cloud/access-management/oidc/provider/vault
  - /docs/pulumi-cloud/access-management/oidc/provider/vault/
---

This document outlines the steps required to use Pulumi with OpenID Connect to authenticate with Vault. This is accomplished using [Vault's JWT authentication method](https://developer.hashicorp.com/vault/docs/auth/jwt#jwt-authentication) to assume a role. Access to the role is authorized using a [Vault policy](https://developer.hashicorp.com/vault/docs/concepts/policies) that validates the contents of the OIDC token issued by Pulumi Cloud.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official Vault documentation](https://developer.hashicorp.com/vault/docs).
{{< /notes >}}

## Prerequisites

* You must have admin access to Vault.
* Pulumi Cloud must be able to access Vault.

## Login Flow

The following diagram demonstrates the high level overview of how Pulumi Cloud authenticates to Vault using the JWT OIDC login flow:

![Vault OIDC JWT login flow](/docs/esc/assets/vault-login-oidc.png)

The contents of the JWT token from Pulumi is shown below:

```json
{
  "aud": "<org-name>",
  "env": "<project-name>/<environment-name>",
  "exp": 1699300519,
  "iat": 1699296919,
  "iss": "https://api.pulumi.com/oidc",
  "nbf": 1699296919,
  "org": "<org-name>",
  "sub": "<subject-identifier>"
}
```

Where:

* `<org-name>` is your Pulumi Cloud organization name (or your username if not part of an organization)
* `<project-name>/<environment-name>` is the Pulumi Cloud environment identifier
* `<subject-identifier>` is the subject identifier of the Pulumi service requesting access

## Configure Vault JWT OIDC Auth

### Enable JWT Auth Method in Vault

To enable the [JWT auth method](https://developer.hashicorp.com/vault/docs/auth/jwt) in Vault:

```
$ vault auth enable -path=jwt jwt
Success! Enabled jwt auth method at: jwt/

$ vault write auth/jwt/config \
    oidc_discovery_url="https://api.pulumi.com/oidc" \
    bound_issuer="https://api.pulumi.com/oidc"
Success! Data written to: auth/jwt/config
```

{{% notes "info" %}}
Vault and Pulumi Cloud use the `jwt` path by default.
{{% /notes %}}

### Create Vault policy

For our example we will create a simple readonly policy (called `reader`) that allows read/list permissions to the `secret` path in Vault.

```shell
vault policy write reader -<<EOF
# read secrets only
path "/secret/*" {
 capabilities = ["read","list"]
}
EOF
```

For more advanced use cases see [Vault documentation](https://developer.hashicorp.com/vault/docs/concepts/policies).

### Create Vault JWT role

To create a [role](https://developer.hashicorp.com/vault/api-docs/auth/jwt#create-update-role) using the CLI:

```shell
vault write auth/jwt/role/<role-name> \
  bound_audiences="<org-name>"
  user_claim="sub" \
  token_policies="<policy-name>" \
  allowed_redirect_uris="<vault-url>/jwt/callback" \
  role_type="jwt"
```

{{% notes "warning" %}}
You must ensure that `role_type` is set to `jwt` and not `oidc`.
{{% /notes %}}

Replace:

* `<role-name>` with your own role name
* `<policy-name>` with your policy (for example the `reader` policy above)
* `<org-name>` with your Pulumi Cloud organization name (or your username if you are not part of an organization)
* `<vault-url>` with your Vault URL (Pulumi Cloud must be able to access this URL)

If you want to use `bound_claims` you'll need to specify the role configuration [as JSON](https://developer.hashicorp.com/vault/docs/auth/jwt#oidc-configuration-troubleshooting):

```shell
$ vault write auth/jwt/role/<role-name> -<<EOF
{
  "user_claim": "sub",
  "bound_audiences": "<org-name>",
  "role_type": "jwt",
  "policies": "<policy-name>",
  "bound_claims": { "env": ["<project-name>/<environment-name>","<project-name>/<another-environment-name>"] },
  "allowed_redirect_uris": ["<vault-url>/jwt/callback"]
}
EOF
```

## Configure ESC for OIDC

To configure OIDC for Pulumi ESC, create a new environment in the [Pulumi Cloud console](https://app.pulumi.com/). Make sure that you have the correct organization selected in the left-hand navigation menu. Then:

  1. Click the **Environments** link.
  2. Click the **Create environment** button.
  3. Provide a project to create your new environment in and a name for your environment.
  4. Click the **Create environment** button.
  5. You will be presented with a split-pane document view. Delete the default placeholder content in the editor and replace it with the following code:

      ```yaml
      values:
        vault:
          login:
            fn::open::vault-login:
              address: <your-vault-url>
              jwt:
                role: <your-role-name>
              namespace: <your-namespace> # namespace is only supported for Vault Enterprise
          secrets:
            fn::open::vault-secrets:
              login: ${vault.login}
              read:
                test1:
                  path: <path-to-secret>
      ```

  6. Replace `<your-vault-url>`, `<your-role-name>`, `<your-namespace>`, and `<path-to-secret>` with the values from the previous steps.
  7. Click **Save**.

{{% notes "info" %}}
If you configured the Vault JWT auth method to use a different [mount path](https://developer.hashicorp.com/vault/docs/auth#enabling-disabling-auth-methods) than `jwt`, you will need to specify that path using the `mount` option of the [vault-login](/docs/pulumi-cloud/esc/providers/vault-login/) provider.
{{% /notes %}}

You can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-project>/<your-environment>` command of the [ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-project>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace the values of `<your-org>`, `<your-project>`, and `<your-environment>` with the values of your Pulumi organization, project, and environment file respectively. You should see output similar to the following:

```shell
# example output
$ esc open <my-org>/<my-project>/<my-environment>
{
  "vault": {
    "login": {
      "address": "***",
      "token": "***"
    },
    "secrets": {
      "test1": {
        "data": {
          "keyA": "valA",
          "keyB": "valB"
        },
        "metadata": {
          "created_time": "2023-11-06T18:24:05.784222Z",
          "custom_metadata": null,
          "deletion_time": "",
          "destroyed": false,
          "version": 1
        }
      }
    }
  }
}
```

To learn more about how to set up and use the various providers in Pulumi ESC, please refer to the [Pulumi ESC providers documentation](/docs/pulumi-cloud/esc/providers/).

## Subject claim customization

You can [customize](/docs/esc/environments/configuring-oidc/#customizing-oidc-claims) the subject claim in the OIDC token to control which Pulumi environments or users are allowed to assume a given IAM role. This allows for more granular access control than the default organization-level permissions.

You do so by configuring the `subjectAttributes` setting. It expects an array of keys to include in it:

* `rootEnvironment.name`: the name of the root environment being evaluated
* `currentEnvironment.name`: the name of the current environment being evaluated
* `pulumi.user.login`: the login identifier of the user opening the environment
* `pulumi.organization.login`: the login identifier of the organization

The subject always contains the following prefix `pulumi:environments:pulumi.organization.login:{ORGANIZATION_NAME}` and every key configured will be appended to this prefix. For example, consider the following environment:

```yaml
values:
  vault:
    login:
      fn::open::vault-login:
        ...
        jwt:
          ...
          subjectAttributes:
            - currentEnvironment.name
            - pulumi.user.login
```

The subject will be `pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:project/development:pulumi.user.login:userLogin`. Note how the keys and values are appended along with the prefix.
