---
title_tag: debug-oidc-claims Pulumi ESC Provider
meta_desc: The debug-oidc-claims Pulumi ESC provider previews the claims of an OIDC token without signing one, so you can configure a relying party first.
title: debug-oidc-claims
h1: debug-oidc-claims
menu:
  esc:
    identifier: debug-oidc-claims
    parent: esc-providers-login
    weight: 11
---

The `debug-oidc-claims` provider previews the claims of an OpenID Connect (OIDC) token from Pulumi ESC (Environments, Secrets, and Configuration). It signs nothing and returns no credential. Use it to find the `iss`, `sub`, and `aud` values that a relying party must trust before you mint a real token with [`fn::open::oidc`](/docs/esc/providers/login/oidc/).

{{< notes type="info" >}}
Pulumi is turning on `debug-oidc-claims` together with `fn::open::oidc`, organization by organization. To have them turned on for your organization, [contact Pulumi](/contact/).
{{< /notes >}}

## Workflow

1. Add a `fn::open::debug-oidc-claims` block with the inputs you plan to give `fn::open::oidc`, and save the environment:

    ```yaml
    values:
      registry:
        login:
          fn::open::debug-oidc-claims:
            audience: https://registry.example.com
            identityToken:
              version: v2
    ```

1. Open the environment, in the Pulumi Cloud console or with [`pulumi env open`](/docs/iac/cli/commands/pulumi_env_open/), and read the claims:

    ```json
    {
      "registry": {
        "login": {
          "aud": "https://registry.example.com",
          "https://pulumi.com/actor": "<user-login>",
          "https://pulumi.com/current_env": "<project>/<environment>",
          "https://pulumi.com/current_env_id": "<environment-id>",
          "https://pulumi.com/org": "<org-name>",
          "https://pulumi.com/org_id": "<org-id>",
          "https://pulumi.com/root_env": "<project>/<environment>",
          "https://pulumi.com/root_env_id": "<environment-id>",
          "iss": "https://api.pulumi.com/oidc/v2",
          "sub": "pulumi:org:<org-id>:env:<environment-id>"
        }
      }
    }
    ```

1. Copy `iss`, `sub`, and `aud` into the relying party's trust configuration. For examples, see [Configure a relying party for custom-audience OIDC tokens](/docs/esc/guides/configuring-oidc/custom-audience/).

1. Change `fn::open::debug-oidc-claims` to `fn::open::oidc`. Keep the other inputs as they are. The environment now returns a signed token with the claims you previewed.

The preview leaves out `iat`, `nbf`, `exp`, and `jti`. Pulumi sets those claims when it signs a token. For what each claim means, see [Token claims](/docs/esc/guides/configuring-oidc/custom-audience/#token-claims).

## Schema reference

### Inputs

With `identityToken.version` set to `v2`, the provider takes the same inputs as [`fn::open::oidc`](/docs/esc/providers/login/oidc/#inputs), with the same rules:

| Property | Type | Required | Description |
|---|---|---|---|
| `audience` | string | Yes | The `aud` claim to preview. One value, 1 to 512 bytes. |
| `identityToken` | object | Yes | Selects the token to preview. |
| `identityToken.version` | string | Yes | The token format. Only `v2` is accepted. |
| `duration` | string | No | Accepted so that the block moves to `fn::open::oidc` unchanged, from `1m` to `1h`. The preview has no lifetime. |

### Outputs

An object keyed by claim name, holding the claims a token would carry. Nothing is signed.

## Preview the vendor login claims

Without `identityToken`, the provider previews the claims that the vendor login providers, such as [`aws-login`](/docs/esc/providers/login/aws-login/), send from the `https://api.pulumi.com/oidc` issuer. [Default token claim](/docs/esc/guides/configuring-oidc/#default-token-claim) describes those claims. In this form, set `audiencePrefix` (required) and optionally `subjectAttributes`. The provider refuses `audience` and `duration` here.

```yaml
values:
  preview:
    fn::open::debug-oidc-claims:
      audiencePrefix: aws
```
