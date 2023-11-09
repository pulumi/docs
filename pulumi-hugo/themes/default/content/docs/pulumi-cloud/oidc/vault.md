---
title_tag: Configure OpenID Connect for Vault | OIDC
meta_desc: This page describes how to configure OIDC token exchange in Vault for use with Pulumi
title: Vault
h1: Configuring OpenID Connect for Vault
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: openid-connect
        weight: 1
---

This document outlines the steps required configured to use Pulumi to use OpenID Connect to authenticate with Vault. This is accomplished using [Vault's JWT authentication method](https://developer.hashicorp.com/vault/docs/auth/jwt#jwt-authentication) to assume a role. Access to the role is authorized using a [Vault policy](https://developer.hashicorp.com/vault/docs/concepts/policies) that validates the contents of the OIDC token issued by Pulumi Cloud.

{{< notes "info" >}}
The `namespaces` functionality of Vault is not currently supported. More specifically, this configuration will only work for the `root` namespace. This means that this configuration will only work with Vault OSS at this time (Vault HCP and Enterprise are not supported).
{{< /notes >}}

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official Vault documentation](https://developer.hashicorp.com/vault/docs).
{{< /notes >}}

## Prerequisites

* You must be an admin of your Pulumi organization.
* You must have admin access to Vault.
* Pulumi Cloud must be able to access Vault.

## Login Flow

The following diagram demonstrates the high level overview of how Pulumi Cloud authenticates to Vault using the JWT OIDC login flow:

![Vault OIDC JWT login flow](./vault-login-oidc.png)

The contents of the JWT token from Pulumi is shown below:

```json
{
  "aud": "<org-name>",
  "env": "<environment-name>",
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
* `<environment-name>` is the Pulumi Cloud environment name
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

### Create Vault Policy

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

### Create Vault JWT Role

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
  "bound_claims": { "env": ["<environment-name>","<another-environment-name>"] },
  "allowed_redirect_uris": ["<vault-url>/jwt/callback"]
}
EOF
```

## Configure OIDC via the Pulumi Console

### Pulumi Deployments

You can pull vault secrets from Pulumi ESC in Deployments. To set this up:

  1. Follow the steps under [Pulumi ESC](#pulumi-esc) below to create an environment with vault secrets.
  2. Follow the [Getting Started](../esc/get-started/) guide and replace environment names to reference the environment created in Step 1.

### Pulumi ESC

To configure OIDC for Pulumi ESC, create a new environment in the [Pulumi Console](https://app.pulumi.com/). Make sure that you have the correct organization selected in the left-hand navigation menu. Then:

  1. Click the **Environments** link.
  2. Click the **Create environment** button.
  3. Provide a name for your environment.
  4. Click the  **Create environment** button.
    {{< video title="Creating a new Pulumi ESC environment" src="../aws/create-new-environment.mp4" autoplay="true" loop="true" >}}
  5. You will be presented with a split-pane editor view. Delete the default placeholder content in the editor and replace it with the following code:

      ```yaml
      values:
        vault:
          login:
            fn::open::vault-login:
              address: <your-vault-url>
              jwt:
                role: <your-role-name>
          secrets:
            fn::open::vault-secrets:
              login: ${vault.login}
              read:
                test1:
                  path: <path-to-secret>
      ```

  6. Replace `<your-vault-url>`, `<your-role-name>`, and `<path-to-secret>` with the values from the previous steps.
  7. Scroll to the bottom of the page and click **Save**.

  ![Vault environment config](./vault-environment-config.png)

{{% notes "info" %}}
If you configured the vault jwt auth method to use a different [mount path](https://developer.hashicorp.com/vault/docs/auth#enabling-disabling-auth-methods) than `jwt`, you will need to specify that path using the `mount` option of the [vault-login](../esc/providers/vault-login.md) provider.
{{% /notes %}}

You can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-environment>` command of the [ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace the values of `<your-org>` and `<your-environment>` with the values of your Pulumi organization and environment file respectively. You should see output similar to the following:

```shell
# example output
$ esc open <my-org>/<my-environment>
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

To learn more about how to set up and use the various providers in Pulumi ESC, please refer to the [relevant Pulumi documentation](/docs/pulumi-cloud/esc/providers/)
