---
title_tag: infisical-login Pulumi ESC Provider
meta_desc: The infisical-login Pulumi ESC Provider enables you to log in to Infisical using OIDC or static credentials.
title: infisical-login
h1: infisical-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    identifier: infisical-login
    parent: esc-dynamic-login-credentials
    weight: 7
aliases:
  - /docs/pulumi-cloud/esc/providers/infisical-login/
  - /docs/esc/providers/infisical-login/
---

The `infisical-login` provider enables you to log in to Infisical using OpenID Connect or by providing static
credentials. The provider will return a set of credentials that can be used to run Infisical CLI commands using
the [esc run](/docs/esc/cli/commands/esc_run/) command and also pull in secrets from Infisical using the
`infisical-secrets` provider.

## Example

```yaml
values:
  infisical:
    login:
      fn::open::infisical-login:
        oidc:
          identityId: aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Infisical, see
the [OpenID Connect integration](/docs/esc/environments/configuring-oidc/infisical/) documentation.

## Inputs

| Property  | Type                                          | Description                                                                                                                |
|-----------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `siteUrl` | string                                        | [Optional] - The base URL of the Infisical instance you want to connect to. May be omitted if default US instance is used. |
| `oidc`    | [InfisicalLoginOIDC](#infisicalloginoidc)     | [Optional] - OIDC configuration to log in to Infisical.                                                                    |
| `static`  | [InfisicalLoginStatic](#infisicalloginstatic) | [Optional] - A static set of credentials to use to log in to Infisical.                                                    |

### InfisicalLoginOIDC

| Property            | Type     | Description                                                                                                                                                                                              |
|---------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `identityId`        | string   | The identityId of the Identity to assume.                                                                                                                                                                |
| `subjectAttributes` | string[] | [Optional] - Subject attributes to be included in the OIDC token. For more information see the [OpenID subject customization](/docs/esc/environments/configuring-oidc/#custom-token-claim) documentation |

### InfisicalLoginStatic

On your Infisical Identity, add a new Auth method and select `Universal Auth`. Create a new Client secret and copy both
the clientID and clientSecret from Universal Auth.
| Property | Type | Description |
|----------------|--------|-----------------------------------|
| `clientId`     | string | The Universal Auth client id. |
| `clientSecret` | string | The Universal Auth client secret. |

## Outputs

| Property      | Type   | Description                                                                                                               |
|---------------|--------|---------------------------------------------------------------------------------------------------------------------------|
| `siteUrl`     | string | [Optional] - The base URL of the Infisical instance you authenticated to. May be omitted if default US instance was used. |
| `accessToken` | string | The access token to use for authentication.                                                                               |
