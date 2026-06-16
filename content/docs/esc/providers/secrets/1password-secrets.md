---
title: 1password-secrets
title_tag: 1password-secrets Pulumi ESC Provider
meta_desc: The `1password-secrets` provider enables you to dynamically import Secrets from 1Password into your Pulumi ESC environment.
h1: 1password-secrets
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    identifier: 1password-secrets
    parent: esc-providers-secrets
    weight: 1
aliases:
    - /docs/pulumi-cloud/esc/providers/1password-secrets/
    - /docs/esc/providers/1password-secrets/
    - /docs/esc/integrations/dynamic-secrets/1password-secrets/
    - /docs/esc/concepts/providers/secrets/1password-secrets/
---

The `1password-secrets` provider enables you to dynamically import secrets from 1Password into your environment. The provider returns a map of names to secret values, which you can then expose as configuration or environment variables. Secrets are fetched lazily at open time, so the values are never stored in the environment definition.

{{% notes type="warning" %}}
This provider is currently in **preview**. Its inputs and behavior may change in a future release.
{{% /notes %}}

## Prerequisites

The provider authenticates to 1Password with a **Service Account token**. Before you can configure it, you need to create a Service Account and grant it access to the vaults that hold the secrets you want to import:

1. In 1Password, create a Service Account and grant it **read** access to each vault that contains a referenced item. A Service Account can only read items in the vaults you explicitly share with it, so be sure to include every vault used in your `op://` references.
1. Copy the generated token. Service Account tokens begin with the prefix `ops_`.

For step-by-step instructions, see 1Password's [Get started with 1Password Service Accounts](https://developer.1password.com/docs/service-accounts/get-started/) documentation.

{{% notes type="info" %}}
The `1password-secrets` provider authenticates with Service Account tokens only. 1Password Connect is not currently supported.
{{% /notes %}}

## Example

The following environment imports four secrets from 1Password and exposes two of them as Pulumi configuration:

```yaml
values:
  1password:
    secrets:
      fn::open::1password-secrets:
        login:
          serviceAccountToken:
            fn::secret: ops_eyJzaWduSW5B...
        get:
          pagerduty_email:
            ref: "op://Management/PagerDuty/Admin/email"
          stripe_key:
            ref: "op://dev/Stripe/publishable-key"
          github_otp:
            ref: "op://development/GitHub/Security/one-time password?attribute=otp"
          deploy_ssh_key:
            ref: "op://Private/ssh keys/ssh key/private key?ssh-format=openssh"
  pulumiConfig:
    email: ${1password.secrets.pagerduty_email}
    stripeKey: ${1password.secrets.stripe_key}
```

### Don't hardcode the Service Account token

The example above wraps the token with `fn::secret`, which encrypts it at rest. That works for getting started, but it still commits a literal token to your environment definition. As a best practice, define the token once in a dedicated environment and import it wherever it's needed, so the secret lives in a single place you can rotate independently:

```yaml
# In a base environment, e.g. acme/onepassword/credentials
values:
  onepasswordToken:
    fn::secret: ops_eyJzaWduSW5B...
```

```yaml
# In the environment that imports secrets
imports:
  - onepassword/credentials
values:
  1password:
    secrets:
      fn::open::1password-secrets:
        login:
          serviceAccountToken: ${onepasswordToken}
        # ...
```

Here, `onepasswordToken` is the value exported by the imported `onepassword/credentials` environment. You can use any secret store this way — for example, a token read from another `fn::open` provider.

## Reference syntax

Each entry under `get` reads a single field from a 1Password item using a **secret reference** of the form:

```
op://<vault-name>/<item-name>/[section-name/]<field-name>
```

- **Sectionless field** — most fields live directly on an item. For example, `op://dev/Stripe/publishable-key` reads the `publishable-key` field of the `Stripe` item in the `dev` vault.
- **Sectioned field** — fields organized under a named section include the section in the path. For example, `op://Management/PagerDuty/Admin/email` reads the `email` field from the `Admin` section of the `PagerDuty` item.

You can append a query-string modifier to change how a field is returned:

- `?attribute=otp` returns the current one-time password generated from a one-time password (TOTP) field, rather than the secret itself.
- `?ssh-format=openssh` returns an SSH private key in OpenSSH format.

Vault, item, section, and field names may contain spaces (for example, `op://Private/ssh keys/ssh key/private key`). You can also reference items by their unique ID instead of their name. For the complete grammar, see 1Password's [secret reference syntax](https://developer.1password.com/docs/cli/secrets-reference-syntax) documentation.

## Verifying your configuration

Once you've saved your environment, validate that the provider resolves your secrets by running either of the following:

- `esc open <org>/<project>/<environment>` command of the [Pulumi ESC CLI](/docs/esc-cli/)
- `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<org>`, `<project>`, and `<environment>` with the values of your Pulumi organization and environment identifier respectively. You should see output similar to the following:

```json
{
  "1password": {
    "secrets": {
      "pagerduty_email": "admin@example.com",
      "stripe_key": "pk_live_...",
      "github_otp": "123456",
      "deploy_ssh_key": "-----BEGIN OPENSSH PRIVATE KEY-----\n..."
    }
  }
}
```

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Authentication fails when opening the environment | The Service Account token is missing, malformed, or has been revoked. | Confirm `serviceAccountToken` resolves to a valid token beginning with `ops_`. Generate a new token in 1Password if the old one was rotated or deleted. |
| A reference returns an "access denied" or "not found" vault error | The Service Account does not have access to the vault named in the `op://` reference. | Grant the Service Account read access to that vault in 1Password, then re-open the environment. |
| A reference returns an item or field "not found" error | The vault, item, section, or field name in the `op://` reference is misspelled, or the item lacks the named field. | Verify the reference against the item in 1Password, including spaces, section names, and the field name. |

## Inputs

| Property | Type                                                   | Description                               |
|----------|--------------------------------------------------------|-------------------------------------------|
| `login`  | [1PasswordSecretsLogin](#1passwordsecretslogin)        | Credentials used to log in to 1Password.  |
| `get`    | map[string][1PasswordSecretsGet](#1passwordsecretsget) | The secrets to get.                       |

### 1PasswordSecretsLogin

| Property              | Type   | Description                                                                   |
|-----------------------|--------|-------------------------------------------------------------------------------|
| `serviceAccountToken` | string | The [1Password Service Account token](#prerequisites) to use for authentication. |

### 1PasswordSecretsGet

| Property | Type   | Description                                  |
|----------|--------|----------------------------------------------|
| `ref`    | string | A [reference to a secret](#reference-syntax) of the form `op://vault-name/item-name/[section-name/]field-name` to read from 1Password.  |

### Outputs

| Property | Type   | Description                        |
|----------|--------|------------------------------------|
| N/A      | object | A map from names to secret values. |
