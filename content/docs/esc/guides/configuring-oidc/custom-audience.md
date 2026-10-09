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

Pulumi ESC (Environments, Secrets, and Configuration) OIDC tokens for custom audiences let an environment mint an OpenID Connect (OIDC) token for any service that accepts OIDC identities. You mint the token with [`fn::open::oidc`](/docs/esc/providers/login/oidc/). The service that accepts the token is the relying party. This guide shows how to configure a relying party to trust `fn::open::oidc` tokens, with examples for Cloudsmith and Aembit. For AWS, Azure, and Google Cloud, use the vendor login providers such as [`aws-login`](/docs/esc/providers/login/aws-login/) instead; they exchange the token for cloud credentials for you.

{{< notes type="info" >}}
Pulumi is turning on `fn::open::oidc` organization by organization. To have it turned on for your organization, [contact Pulumi](/contact/).
{{< /notes >}}

`fn::open::oidc` tokens use a different issuer and subject from the tokens that the vendor login providers, such as `aws-login`, send. A relying party that you configured for a vendor login provider does not accept them. For the differences, see [Token issuers](/docs/esc/guides/configuring-oidc/#token-issuers).

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

The console and the API show the subject only for organizations that have `fn::open::oidc` turned on.

The subject uses IDs, not names, so it does not change when you rename the organization or the environment. Because of that, a wildcard such as `pulumi:org:<org-name>:*` does not match anything. To trust every environment in an organization, match the subject prefix `pulumi:org:<org-id>:env:` where the relying party supports prefix or wildcard matching.

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

## Cloudsmith

Cloudsmith exchanges an OIDC token for a short-lived Cloudsmith API token that belongs to a service account.

<!-- TODO(devon): verify the Cloudsmith settings path, field names, and exchange request against a live workspace. They come from Cloudsmith's public docs. -->

1. In Cloudsmith, open your workspace settings, then **Authentication** > **OpenID Connect**, and create a provider:
    - **Provider Name:** a name such as `pulumi-esc`.
    - **Provider URL:** `https://api.pulumi.com/oidc/v2`.
    - **Required OpenID Token Claims:** the `aud` and `sub` values from your environment:

        ```json
        {
          "aud": "https://api.cloudsmith.io",
          "sub": "pulumi:org:<org-id>:env:<environment-id>"
        }
        ```

    - **Service Accounts:** the service account that the token should act as.

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

    The response contains a `token` field. Send it to the Cloudsmith API in the `X-Api-Key: Bearer <token>` header.

## Aembit

Aembit can identify a workload by an OIDC token and then issue the credentials that the workload's access policy allows.

<!-- TODO(devon): this section is drafted from Aembit's public docs and was not exercised in a live tenant. Verify the trust provider type, attestation method, match rule names, client workload identifier, Edge API URL, and the audience Aembit expects. -->

1. In your Aembit tenant, create a trust provider of type **OIDC ID Token**:
    - **Attestation method:** **OIDC Discovery**, with the URL `https://api.pulumi.com/oidc/v2`.
    - **Match rules:** set **Issuer** to `https://api.pulumi.com/oidc/v2`, **Audience** to the audience you will use, and **Subject** to the subject of your environment.

1. Create a client workload identified by **OIDC ID Token Subject**, with the same subject.

1. In Pulumi ESC, mint a token with the same audience:

    ```yaml
    values:
      aembit:
        login:
          fn::open::oidc:
            audience: <aembit-audience>
            identityToken:
              version: v2
      environmentVariables:
        AEMBIT_OIDC_TOKEN: ${aembit.login}
    ```

1. Send the token to the Aembit Edge API, at `https://<your-aembit-edge-url>/edge/v1/auth`, in the request body as `client.oidc.identityToken`, together with your Edge SDK `clientId`. The response contains an `accessToken` to use as a bearer token in later calls.

## Vault and other services

<!-- TODO(devon): verify the Vault JWT auth settings (oidc_discovery_url, bound_issuer, bound_audiences, user_claim, bound_subject) and the one-issuer-per-mount statement against HashiCorp's docs. -->

Most other services accept OIDC tokens through a JSON Web Token (JWT) authentication method, such as the [JWT auth method](https://developer.hashicorp.com/vault/docs/auth/jwt) in HashiCorp Vault. Configure it with these values:

- **Discovery URL and bound issuer:** `https://api.pulumi.com/oidc/v2`
- **Bound audience:** your `audience` input
- **Subject:** bind the role to the exact `sub` value, or use `sub` as the user claim

If you already use [`vault-login`](/docs/esc/providers/login/vault-login/), mount a second JWT auth method for these tokens, because one mount trusts one issuer.

## Learn more

- [`oidc` provider reference](/docs/esc/providers/login/oidc/)
- [`debug-oidc-claims` provider reference](/docs/esc/providers/login/debug-oidc-claims/)
- [Configuring OpenID Connect for Pulumi ESC](/docs/esc/guides/configuring-oidc/)
