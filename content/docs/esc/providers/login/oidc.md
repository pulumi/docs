---
title_tag: oidc Pulumi ESC Provider
meta_desc: The oidc Pulumi ESC provider mints a short-lived OIDC token for an audience you choose, for any service that accepts OpenID Connect identities.
title: oidc
h1: oidc
menu:
  esc:
    identifier: oidc
    parent: esc-providers-login
    weight: 10
---

The `oidc` provider mints a short-lived OpenID Connect (OIDC) token for an audience you choose. You can exchange the token with any service that federates OIDC identities, such as an artifact registry, a secrets broker, or a cloud identity service. This feature is called Pulumi ESC (Environments, Secrets, and Configuration) OIDC tokens for custom audiences. The rest of this page calls it `fn::open::oidc`.

The vendor login providers, such as [`aws-login`](/docs/esc/providers/login/aws-login/), exchange their token for you and return that vendor's credentials. `fn::open::oidc` returns the signed token itself, so your own code or tool does the exchange.

{{< notes type="info" >}}
Pulumi is turning on `fn::open::oidc` organization by organization. To have it turned on for your organization, [contact Pulumi](/contact/).
{{< /notes >}}

## Examples

### Mint a token

Set `audience` to the value the relying party expects in the token's `aud` claim. Set `identityToken.version` to `v2`:

```yaml
values:
  registry:
    login:
      fn::open::oidc:
        audience: https://registry.example.com
        identityToken:
          version: v2
```

The provider returns the token as a secret string, so you reference it as `${registry.login}`.

### Set a shorter lifetime

Tokens live for one hour by default. Use `duration` to ask for a shorter lifetime, from `1m` to `1h`:

```yaml
values:
  registry:
    login:
      fn::open::oidc:
        audience: https://registry.example.com
        duration: 15m
        identityToken:
          version: v2
```

### Pass the token to a command

Export the token as an environment variable, then run your tool with [`pulumi env run`](/docs/iac/cli/commands/pulumi_env_run/):

```yaml
values:
  registry:
    login:
      fn::open::oidc:
        audience: https://registry.example.com
        identityToken:
          version: v2
  environmentVariables:
    REGISTRY_OIDC_TOKEN: ${registry.login}
```

If a tool reads the token from a file, use the [`files`](/docs/esc/concepts/outputs/#files) reserved property instead. `pulumi env run` writes the token to a temporary file and sets the named variable to that file's path:

```yaml
values:
  registry:
    login:
      fn::open::oidc:
        audience: https://registry.example.com
        identityToken:
          version: v2
  files:
    REGISTRY_OIDC_TOKEN_FILE: ${registry.login}
```

### Define the token once and import it

The token's subject (`sub`) names the environment that declares the `fn::open::oidc` block, not the environment you open. Define the block in one environment and [import](/docs/esc/concepts/imports/) it where you need the token. Every importing environment then gets a token with the same subject, and the relying party trusts one subject.

```yaml
# myorg/registry/login
values:
  registry:
    login:
      fn::open::oidc:
        audience: https://registry.example.com
        identityToken:
          version: v2
```

```yaml
# myorg/myapp/dev
imports:
  - registry/login

values:
  environmentVariables:
    REGISTRY_OIDC_TOKEN: ${registry.login}
```

## Token contents

`fn::open::oidc` signs its tokens with a separate issuer, `https://api.pulumi.com/oidc/v2`. The subject has the form `pulumi:org:<org-id>:env:<environment-id>` and uses the IDs of the organization and the declaring environment. For the full claim list and the steps to trust the token, see [Configure a relying party for custom-audience OIDC tokens](/docs/esc/guides/configuring-oidc/custom-audience/).

To see the claims before you mint a token, use [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) with the same inputs.

Each token that `fn::open::oidc` mints adds an entry to your organization's [audit log](/docs/administration/guides/audit-logs/). The entry records the subject, audience, environment, and lifetime of the token.

## Schema reference

### Inputs

| Property | Type | Required | Description |
|---|---|---|---|
| `audience` | string | Yes | The token's `aud` claim. One value, 1 to 512 bytes. It must not be blank. |
| `identityToken` | object | Yes | The identity token to mint. |
| `identityToken.version` | string | Yes | The token format. Only `v2` is accepted. |
| `duration` | string | No | The token's lifetime, from `1m` to `1h`, for example `15m`. Defaults to `1h`. |

The provider refuses any other input, including `subjectAttributes`. The subject of a `fn::open::oidc` token is always built from the organization ID and the ID of the environment that declares it.

### Outputs

The provider returns one value: the signed token, as a secret string. It has no properties, so reference the block itself, for example `${registry.login}`.

## Configuring OIDC

To configure a service to trust these tokens, see [Configure a relying party for custom-audience OIDC tokens](/docs/esc/guides/configuring-oidc/custom-audience/).

## Troubleshooting

### Provider not enabled for the organization

**Symptom:** opening the environment fails with `fn::open::oidc is not enabled for organization "<org>"`.

**Cause:** Pulumi has not turned on `fn::open::oidc` for your organization yet.

**Fix:** [contact Pulumi](/contact/) to have it turned on.

### Environment not saved

**Symptom:** opening fails with `fn::open::oidc cannot run in an unsaved environment document; save the environment and import it`.

**Cause:** the token's subject uses the environment's ID, and an unsaved environment document has no ID yet.

**Fix:** save the environment that declares the block, then open it, or open another environment that imports it.

### Input refused

**Symptom:** opening fails with `fn::open::oidc does not accept subjectAttributes` or `fn::open::oidc does not accept an input named "<name>"`.

**Cause:** `fn::open::oidc` accepts only `audience`, `identityToken.version`, and `duration`. The vendor login providers accept `subjectAttributes`, but this provider does not.

**Fix:** remove the input. To restrict which environments the relying party trusts, match the exact `sub` claim instead.

### Duration out of range

**Symptom:** opening fails with `duration must be between 1m0s and 1h0m0s`.

**Fix:** set `duration` to a value from `1m` to `1h`, or remove it to use the one-hour default.

### Relying party rejects the token

**Symptom:** the service you exchange the token with rejects it.

**Cause:** usually the service trusts the vendor login issuer, `https://api.pulumi.com/oidc`, or expects a different `aud` or `sub`.

**Fix:** preview the claims with [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) and compare `iss`, `aud`, and `sub` with the service's configuration. The issuer must be `https://api.pulumi.com/oidc/v2`.
