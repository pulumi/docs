---
title_tag: doppler-login Pulumi ESC Provider
meta_desc: The doppler-login Pulumi ESC Provider enables you to log in to Doppler using OIDC.
title: doppler-login
h1: doppler-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    identifier: doppler-login
    parent: esc-dynamic-login-credentials
    weight: 3
aliases:
  - /docs/pulumi-cloud/esc/providers/doppler-login/
  - /docs/esc/providers/doppler-login/
---

The `doppler-login` provider enables you to log in to Doppler using OpenID Connect.
The provider will return a set of credentials that can be used to run Doppler CLI commands using
the [esc run](/docs/esc/cli/commands/esc_run/) command and also pull in secrets from Doppler using the
`doppler-secrets` provider.

## Example

```yaml
values:
  doppler:
    login:
      fn::open::doppler-login:
        oidc:
          identityId: 00000000-0000-0000-0000-000000000000
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Doppler, see
the [OpenID Connect integration](/docs/esc/environments/configuring-oidc/doppler/) documentation.

## Inputs

| Property  | Type                                          | Description                                                                                                                |
|-----------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `oidc`    | [DopplerLoginOIDC](#dopplerloginoidc)     | OIDC configuration to log in to Doppler.                                                                    |

### DopplerLoginOIDC

| Property            | Type     | Description                                                                                                                                                                                              |
|---------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `identityId`        | string   | The identityId of the Doppler service account identity to assume.                                                                                                                                                                |
| `subjectAttributes` | string[] | [Optional] - Subject attributes to be included in the OIDC token. For more information see the [OpenID subject customization](/docs/esc/environments/configuring-oidc/#custom-token-claim) documentation |

## Outputs

| Property      | Type   | Description                                                                                                               |
|---------------|--------|---------------------------------------------------------------------------------------------------------------------------|
| `accessToken` | string | The short lived access token to use for authentication.                                                                               |
