---
title_tag: doppler-login Pulumi ESC Provider
meta_desc: The doppler-login Pulumi ESC Provider enables you to log in to Doppler using OIDC.
title: doppler-login
h1: doppler-login
menu:
  esc:
    identifier: doppler-login
    parent: esc-providers-login
    weight: 3
aliases:
  - /docs/pulumi-cloud/esc/providers/doppler-login/
  - /docs/esc/providers/doppler-login/
  - /docs/esc/integrations/dynamic-login-credentials/doppler-login/
  - /docs/esc/concepts/providers/login/doppler-login/
---

The `doppler-login` provider enables you to log in to Doppler using OpenID Connect.
The provider will return a set of credentials that can be used to run Doppler CLI commands using
the [pulumi env run](/docs/iac/cli/commands/pulumi_env_run/) command and also pull in secrets from Doppler using the
`doppler-secrets` provider.

## Example

```yaml
values:
  doppler:
    login:
      fn::open::doppler-login:
        oidc:
          identityId: 00000000-0000-0000-0000-000000000000
  environmentVariables:
    # Consumed by the Doppler CLI for authentication
    DOPPLER_TOKEN: ${doppler.login.accessToken}
```

## Schema reference

{{< esc-schema-updated >}}

### Inputs

{{< esc-schema type="provider" name="doppler-login" section="inputs" >}}

### Outputs

{{< esc-schema type="provider" name="doppler-login" section="outputs" >}}

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Doppler, see
the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/doppler/) documentation.
