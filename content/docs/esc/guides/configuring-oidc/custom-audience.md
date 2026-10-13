---
title_tag: Configure OpenID Connect for custom audiences | Pulumi ESC
meta_desc: Configure any service that accepts OpenID Connect identities to trust OIDC tokens that Pulumi ESC mints with fn::open::oidc.
title: Custom audiences
h1: Configure a relying party for custom-audience OIDC tokens
menu:
  esc:
    name: Custom audiences
    parent: esc-guides-configuring-oidc
    weight: 8
---

A Pulumi ESC environment can mint an OpenID Connect (OIDC) token for any service that accepts OIDC identities. You mint the token with [`fn::open::oidc`](/docs/esc/providers/login/oidc/). The service that accepts the token is the relying party. This guide shows how to configure a relying party to trust `fn::open::oidc` tokens, with examples for Cloudsmith, JFrog Artifactory, and Aembit. For AWS, Azure, and Google Cloud, use the vendor login providers such as [`aws-login`](/docs/esc/providers/login/aws-login/) instead; they exchange the token for cloud credentials for you.

`fn::open::oidc` tokens use a different issuer and subject from the tokens that the vendor login providers, such as `aws-login`, send. A relying party that you configured for a vendor login provider does not accept them. For the differences, see [Token formats](/docs/esc/guides/configuring-oidc/#token-formats).

## Issuer and signing keys

Configure the relying party with these values:

| Setting | Value |
|:--------|:------|
| Issuer | `https://api.pulumi.com/oidc/v2` |
| Discovery document | `https://api.pulumi.com/oidc/v2/.well-known/openid-configuration` |
| JSON Web Key Set (JWKS) | `https://api.pulumi.com/oidc/v2/.well-known/jwks` |
| Signing algorithm | `RS256` |

Most services need only the issuer URL and find the keys through the discovery document. The keys at this issuer are separate from the keys at `https://api.pulumi.com/oidc`.

## Find the subject

Each token's subject (`sub`) has the form `pulumi:org:<org-id>:env:<environment-id>`. The environment is the one whose definition contains the `fn::open::oidc` block. If you open an environment that imports the block from another environment, the token carries the subject of the environment that declares it.

To copy the subject for an environment, use one of these methods:

- **Pulumi Cloud console:** open the environment. The **OIDC subject** block above the environment editor shows the subject with a copy button.
- **REST API:** call [`GET /api/esc/environments/{orgName}/{projectName}/{envName}/metadata`](/docs/reference/cloud-rest-api/environments/) and read the `oidcSubjectV2` field.

    ```bash
    curl -s \
      -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
      https://api.pulumi.com/api/esc/environments/<org>/<project>/<environment>/metadata
    ```

Copy the subject from the environment that declares the `fn::open::oidc` block. An environment that only imports the block also shows a subject, but no token carries it.

The subject uses IDs, not names, so it does not change when you rename the organization or the environment, and a wildcard such as `pulumi:org:<org-name>:*` matches nothing.

Pin the exact subject. To share one trust entry across environments, declare the block once and [import](/docs/esc/concepts/imports/) it; every importing environment presents the same subject, and Pulumi Cloud permissions decide who may open each one. A wildcard such as `pulumi:org:<org-id>:env:*` trusts every environment in the organization, including any that a member creates later, so it gives up that boundary. If you need it anyway, use it only where the relying party supports wildcard matching, such as the `.*` suffix in Cloudsmith or a glob in JFrog.

## Token claims

| Claim | Description |
|:------|:------------|
| `iss` | `https://api.pulumi.com/oidc/v2`. |
| `sub` | `pulumi:org:<org-id>:env:<environment-id>`, for the environment that declares the block. |
| `aud` | The `audience` input, as a single string. |
| `iat`, `nbf`, `exp`, `jti` | Issued-at time, not-before time, expiry time, and a unique token ID. |
| `https://pulumi.com/org` | The organization name. |
| `https://pulumi.com/org_id` | The organization ID. |
| `https://pulumi.com/current_env` | The name of the environment that declares the block, as `<project>/<environment>`. |
| `https://pulumi.com/current_env_id` | The ID of that environment. |
| `https://pulumi.com/root_env` | The name of the environment that was opened, as `<project>/<environment>`. |
| `https://pulumi.com/root_env_id` | The ID of the environment that was opened. Omitted when that environment has no ID. |
| `https://pulumi.com/actor` | The login of the user whose credentials opened the environment. |

Base your trust rules on `iss`, `aud`, and `sub`. Names can change, but IDs do not. The `subjectAttributes` input of the vendor login providers does not apply to these tokens.

Always pin the trust rule to `sub`. Every Pulumi organization shares this issuer, and any organization can mint a token for any audience, so a rule that checks only `iss` and `aud` accepts tokens from every organization that uses the same audience. Every relying party can match `sub`; some cannot read the `https://pulumi.com/` claims at all.

## Verify the claims before you mint a token

Use [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) to see the exact claims before you configure the relying party:

1. In the environment that will hold the token, add a block with the inputs you plan to use, then save the environment:

    ```yaml
    values:
      registry:
        login:
          fn::open::debug-oidc-claims:
            audience: https://registry.example.com
            identityToken:
              version: v2
    ```

1. Open the environment and copy the `iss`, `sub`, and `aud` values from the output into the relying party.

1. Change `fn::open::debug-oidc-claims` to `fn::open::oidc` and save. The environment now returns a signed token, and you reference it as `${registry.login}`.

## Examples

Any service that accepts OIDC tokens works the same way: give it the issuer, the audience, and the subject from above. The examples below were each run end to end.

### Cloudsmith

Cloudsmith exchanges an OIDC token for a short-lived Cloudsmith API token that belongs to a service account.

1. In Cloudsmith, create the service account that the token should act as. You need the Manager or Owner role in the workspace.

1. Open your workspace settings, then **Authentication** > **OpenID Connect**, create a provider, and enable it:
    - **Provider Name:** a name such as `pulumi-esc`.
    - **Provider URL:** `https://api.pulumi.com/oidc/v2`.
    - **Required OpenID Token Claims:** the `aud` and `sub` values from your environment:

        ```json
        {
          "aud": "https://api.cloudsmith.io",
          "sub": "pulumi:org:<org-id>:env:<environment-id>"
        }
        ```

    - **Service Accounts:** the service account from step 1.

    Cloudsmith requires no particular audience; `aud` only has to match the audience you set in Pulumi ESC.

    Always include `sub`. Every Pulumi organization shares the issuer, and any organization can mint a token for any audience, so a provider that requires only `aud` accepts tokens from other organizations. Cloudsmith reads a trailing `.*` as a prefix match, so `pulumi:org:<org-id>:env:.*` trusts every environment in the organization. Read [Find the subject](#find-the-subject) before you widen the rule.

1. In Pulumi ESC, mint a token with the same audience and export it:

    ```yaml
    values:
      cloudsmith:
        oidcToken:
          fn::open::oidc:
            audience: https://api.cloudsmith.io
            identityToken:
              version: v2
      environmentVariables:
        CLOUDSMITH_OIDC_TOKEN: ${cloudsmith.oidcToken}
    ```

1. Exchange the token for a Cloudsmith API token. Replace `<workspace>` and `<service-account-slug>` with your values:

    ```bash
    pulumi env run <org>/<project>/<environment> -- sh -c '
      curl -s -X POST https://api.cloudsmith.io/openid/<workspace>/ \
        -H "Content-Type: application/json" \
        -d "{\"oidc_token\": \"$CLOUDSMITH_OIDC_TOKEN\", \"service_slug\": \"<service-account-slug>\"}"'
    ```

    Write `$CLOUDSMITH_OIDC_TOKEN`, not `${CLOUDSMITH_OIDC_TOKEN}`. `pulumi env run` interpolates the braced form itself, so the shell gets an empty value.

    The response contains a `token` field. The Cloudsmith token is valid for about two hours, whatever `duration` the `fn::open::oidc` block sets. Send it to the Cloudsmith API in the `X-Api-Key: Bearer <token>` or `Authorization: Bearer <token>` header.

If the exchange returns `401 Failed to validate token`, check the provider URL, then compare the provider's claims with the [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) output. Cloudsmith returns this error for a wrong provider URL, an expired token, and a claim mismatch alike, and does not check the URL when you save the provider.

### JFrog Artifactory

JFrog exchanges an OIDC token for a short-lived JFrog access token that acts as a JFrog user. OIDC integration needs a JFrog Enterprise X or Enterprise+ subscription.

1. In the JFrog Platform, open **Administration** > **General Management** > **Manage Integrations** and add an OpenID Connect integration:
    - **Provider Type:** Generic OpenID Connect.
    - **Provider Name:** a name such as `pulumi-esc`. You send this name in the exchange request.
    - **Provider URL:** `https://api.pulumi.com/oidc/v2`.
    - **Audience:** your instance URL, such as `https://<server>.jfrog.io`.

    Always set the audience, and use the same string in Pulumi ESC. JFrog compares it exactly, so a trailing slash or a different value fails. If you leave it blank, JFrog accepts tokens for any audience. JFrog does not check the provider URL when you save the integration; a wrong URL fails at the first exchange.

1. Add an identity mapping to the integration:
    - **Claims JSON:** the `sub` value from your environment:

        ```json
        {
          "sub": "pulumi:org:<org-id>:env:<environment-id>"
        }
        ```

    - **Token Scope:** User, and the **User Name** that the token acts as.
    - **Expiration Time:** the lifetime of the JFrog access token. `duration` does not change it.

    Always include `sub`. A mapping that matches only `aud` accepts tokens from other organizations that use the same audience. JFrog reads claim values as globs over the whole value. A value without `*` must match exactly, `pulumi:org:<org-id>:env:*` trusts every environment in the organization, and `*` alone trusts every Pulumi organization. Read [Find the subject](#find-the-subject) before you widen the rule.

1. In Pulumi ESC, mint a token with the same audience and export it:

    ```yaml
    values:
      jfrog:
        oidcToken:
          fn::open::oidc:
            audience: https://<server>.jfrog.io
            identityToken:
              version: v2
      environmentVariables:
        JFROG_OIDC_TOKEN: ${jfrog.oidcToken}
    ```

1. Exchange the token for a JFrog access token. Replace `<server>` and `pulumi-esc` with your values:

    ```bash
    pulumi env run <org>/<project>/<environment> -- sh -c '
      curl -s -X POST https://<server>.jfrog.io/access/api/v1/oidc/token \
        -H "Content-Type: application/json" \
        -d "{\"grant_type\": \"urn:ietf:params:oauth:grant-type:token-exchange\", \"subject_token_type\": \"urn:ietf:params:oauth:token-type:id_token\", \"subject_token\": \"$JFROG_OIDC_TOKEN\", \"provider_name\": \"pulumi-esc\"}"'
    ```

    Write `$JFROG_OIDC_TOKEN`, not `${JFROG_OIDC_TOKEN}`, for the reason given in the Cloudsmith section.

    The response contains an `access_token` field. Send it to Artifactory in the `Authorization: Bearer <token>` header.

If the exchange returns `400 Invalid audience`, the token's audience does not match the integration's. A `403 Forbidden` means no identity mapping matched the token's claims. JFrog rejects a token as soon as it expires and allows no grace period.

### Aembit

Aembit exchanges an OIDC token for an Edge API access token, then issues the credentials that an access policy grants to the workload.

1. In your Aembit tenant, create a trust provider of type **OIDC ID Token**:
    - **Attestation method:** **OIDC Discovery**, with the URL `https://api.pulumi.com/oidc/v2`.
    - **Match rules:** set **Issuer** to `https://api.pulumi.com/oidc/v2`, **Audience** to your tenant URL, such as `https://<tenant>.aembit.io`, and **Subject** to the `sub` value from your environment, `pulumi:org:<org-id>:env:<environment-id>`.

    Aembit requires no particular audience and checks `aud` only when the Audience rule exists. Always add the rule, and use the same string in Pulumi ESC.

    Always add the Subject rule too. A trust provider without it accepts tokens from other organizations that use the same audience. Aembit matches the subject exactly and has no wildcard form. To share one trust provider across environments, import the block from the environment that declares it.

1. Create a client workload identified by **OIDC ID Token Subject**, with the same subject. Do not identify it by audience or issuer: a trust provider without a Subject rule passes authentication for any Pulumi organization, and a workload identified that way then hands out its credentials.

1. Create a credential provider for the credential you want to issue and a server workload for the service that uses it. Then create an access policy that connects the client workload, trust provider, credential provider, and server workload, and make it active.

1. In Pulumi ESC, mint a token with the same audience and export it:

    ```yaml
    values:
      aembit:
        login:
          fn::open::oidc:
            audience: https://<tenant>.aembit.io
            identityToken:
              version: v2
      environmentVariables:
        AEMBIT_OIDC_TOKEN: ${aembit.login}
    ```

1. Exchange the token for an Edge API access token. Replace `<tenant>`, `<region>`, and `<client-id>` with your values:

    ```bash
    pulumi env run <org>/<project>/<environment> -- sh -c '
      curl -s -X POST https://<tenant>.ec.<region>.aembit.io/edge/v1/auth \
        -H "Content-Type: application/json" \
        -d "{\"clientId\": \"<client-id>\", \"client\": {\"oidc\": {\"identityToken\": \"$AEMBIT_OIDC_TOKEN\"}}}"'
    ```

    Write `$AEMBIT_OIDC_TOKEN`, not `${AEMBIT_OIDC_TOKEN}`, for the reason given in the Cloudsmith section.

    Your tenant shows the Edge API base URL, `https://<tenant>.ec.<region>.aembit.io/edge/v1`. Call it directly; the tenant URL only redirects to it. The client ID belongs to the trust provider, not the client workload. It has the form `aembit:<region>:<tenant>:identity:oidc_id_token:<trust-provider-id>` and is shown on the trust provider's page.

    The response contains an `accessToken` field. The token is valid for one hour, whatever `duration` you set.

1. Request the credential from `https://<tenant>.ec.<region>.aembit.io/edge/v1/credentials`. Send the access token in the `Authorization: Bearer <token>` header. In the body, send the OIDC token again, with the server workload's host and port and the credential type:

    ```json
    {
      "client": {"oidc": {"identityToken": "<oidc-token>"}},
      "server": {"host": "<server-host>", "port": 443},
      "credentialType": "ApiKey"
    }
    ```

    Aembit checks the OIDC token again on this call. Once that token expires, the access token no longer returns credentials, so `duration` limits how long the workload can fetch credentials without a new token.

If `/edge/v1/auth` returns `401 Failed to authenticate`, check the client ID, then compare the trust provider's match rules with the [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) output. Aembit returns this error for every rejection and does not say which rule failed. Unlike Cloudsmith and JFrog, it checks the discovery URL when you save the trust provider. If `/edge/v1/credentials` returns `credentialType: Unknown`, no active access policy matched; check the client workload's subject and the server host and port. Aembit accepts a token for about five minutes after it expires.

## Learn more

- [`oidc` provider reference](/docs/esc/providers/login/oidc/)
- [`debug-oidc-claims` provider reference](/docs/esc/providers/login/debug-oidc-claims/)
- [Configuring OpenID Connect for Pulumi ESC](/docs/esc/guides/configuring-oidc/)
