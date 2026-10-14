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

The `oidc` provider mints a short-lived OpenID Connect (OIDC) token for an audience you choose. You can exchange the token with any service that federates OIDC identities, such as an artifact registry, a secrets broker, or a cloud identity service. For the steps to configure a service to trust these tokens, see [Configure a relying party for custom-audience OIDC tokens](/docs/esc/guides/configuring-oidc/custom-audience/).

The vendor login providers, such as [`aws-login`](/docs/esc/providers/login/aws-login/), exchange their token for you and return that vendor's credentials. `fn::open::oidc` returns the signed token itself, so your own code or tool does the exchange.

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

The relying party applies its own clock-skew allowance, so it may accept a token for a few minutes after `exp`. The relying party, not `duration`, sets the lifetime of the credential you exchange the token for.

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

Write `$REGISTRY_OIDC_TOKEN`, not `${REGISTRY_OIDC_TOKEN}`, inside a command you pass to `pulumi env run`. The CLI expands `${NAME}` itself before the command runs, so the shell gets an empty value.

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

{{< notes type="warning" >}}
Pin the subject in every trust policy. Every Pulumi organization shares the `https://api.pulumi.com/oidc/v2` issuer, and any organization can mint a token for any audience, so a policy that checks only the issuer and the audience accepts tokens from other organizations. Copy the subject from the **OIDC subject** block above the environment editor.
{{< /notes >}}

To see the claims before you mint a token, use [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) with the same inputs.

Each token that `fn::open::oidc` mints adds an entry to your organization's [audit log](/docs/administration/guides/audit-logs/). The entry records the subject, audience, environment, and lifetime of the token. Its event name is `environment-oidc-token-issued`.

## Schema reference

### Inputs

| Property | Type | Required | Description |
|---|---|---|---|
| `audience` | string | Yes | The token's `aud` claim. One value, 1 to 255 bytes. It must not be blank. |
| `identityToken` | object | Yes | The identity token to mint. |
| `identityToken.version` | string | Yes | The token format. Set `v2`. |
| `duration` | string | No | The token's lifetime, from `1m` to `1h`, for example `15m`. Defaults to `1h`. |

`identityToken.version` pins the token format an environment depends on: `v2` is the format this provider mints, with the ID-based subject, and the vendor login providers mint the earlier format on the `/oidc` issuer. The input has no default so that a later format can ship without changing the tokens an existing environment mints or breaking the trust policies that pin them.

The provider refuses any other input, including `subjectAttributes`. The subject of a `fn::open::oidc` token is always built from the organization ID and the ID of the environment that declares it.

### Outputs

The provider returns one value: the signed token, as a secret string. It has no properties, so reference the block itself, for example `${registry.login}`.

## Configuring OIDC

To configure a service to trust these tokens, see [Configure a relying party for custom-audience OIDC tokens](/docs/esc/guides/configuring-oidc/custom-audience/).

## Troubleshooting

Pulumi checks the inputs against the schema when you save the environment, and runs the provider's own checks when you open it. Some errors below appear at save, in the console editor or from `esc env edit`, and others only at open.

### Environment not saved

**Symptom:** opening fails with `fn::open::oidc cannot run in an unsaved environment document; save the environment and import it`.

**Cause:** the token's subject uses the environment's ID, and an unsaved environment document has no ID yet.

**Fix:** save the environment that declares the block, then open it, or open another environment that imports it.

### Input refused

**Symptom:** saving fails with `missing required properties: audience`, `expected a string of at most length 255`, or `expected "v2"`. Opening fails with `fn::open::oidc does not accept subjectAttributes: a v2 token's subject is always the environment's ID`, `fn::open::oidc does not accept an input named "<name>"`, or `audience must not be blank`.

**Cause:** `fn::open::oidc` accepts only `audience`, `identityToken.version`, and `duration`, and the `audience` must be 1 to 255 bytes and not blank. The vendor login providers accept `subjectAttributes`, but this provider does not.

**Fix:** add the missing input, or remove the refused one. To restrict which environments the relying party trusts, match the exact `sub` claim instead.

### Duration out of range

**Symptom:** saving fails with `string must match the pattern "^([0-9]+h)?([0-9]+m)?([0-9]+s)?$"`, or opening fails with `duration must be between 1m0s and 1h0m0s`.

**Fix:** write `duration` as hours, minutes, and seconds, such as `15m` or `1h`, from `1m` to `1h`, or remove it to use the one-hour default.

### Relying party rejects the token

**Symptom:** the service you exchange the token with rejects it.

**Cause:** usually the service trusts the vendor login issuer, `https://api.pulumi.com/oidc`, or expects a different `aud` or `sub`.

**Fix:** preview the claims with [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) and compare `iss`, `aud`, and `sub` with the service's configuration. The issuer must be `https://api.pulumi.com/oidc/v2`.
