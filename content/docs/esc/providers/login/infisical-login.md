---
title_tag: infisical-login Pulumi ESC Provider
meta_desc: The infisical-login Pulumi ESC Provider enables you to log in to Infisical using OIDC or static credentials.
title: infisical-login
h1: infisical-login
menu:
  esc:
    identifier: infisical-login
    parent: esc-providers-login
    weight: 7
aliases:
  - /docs/pulumi-cloud/esc/providers/infisical-login/
  - /docs/esc/providers/infisical-login/
  - /docs/esc/integrations/dynamic-login-credentials/infisical-login/
  - /docs/esc/concepts/providers/login/infisical-login/
---

The `infisical-login` provider enables you to log in to Infisical using OpenID Connect or by providing static
credentials. The provider will return a set of credentials that can be used to run Infisical CLI commands using
the [pulumi env run](/docs/iac/cli/commands/pulumi_env_run/) command and also pull in secrets from Infisical using the
`infisical-secrets` provider.

## Example

```yaml
values:
  infisical:
    login:
      fn::open::infisical-login:
        oidc:
          identityId: aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
  environmentVariables:
    # Consumed by the Infisical CLI for authentication
    INFISICAL_TOKEN: ${infisical.login.accessToken}
```

## Schema reference

{{< esc-schema-updated >}}

### Inputs

{{< esc-schema type="provider" name="infisical-login" section="inputs" >}}

### Outputs

{{< esc-schema type="provider" name="infisical-login" section="outputs" >}}

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and Infisical, see
the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/infisical/) documentation.

## Static credentials

To use static credentials instead of OIDC, add a new Auth method on your Infisical Identity and
select `Universal Auth`. Create a new client secret, then supply the `clientId` and `clientSecret`
from Universal Auth as the provider's static credentials.
