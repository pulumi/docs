---
title_tag: Configure OIDC issuers | Pulumi Cloud
meta_desc: Register an OIDC issuer in Pulumi Cloud, configure its authorization policies, and exchange OIDC tokens for Pulumi access tokens.
title: OIDC issuers
h1: OIDC issuers
menu:
  administration:
    parent: administration-guides
    weight: 3
    identifier: administration-guides-oidc-issuers
aliases:
- /docs/administration/access-identity/oidc-client/
- /docs/pulumi-cloud/oidc/client/
- /docs/pulumi-cloud/oidc/
- /docs/administration/access-identity/oidc/client/
- /docs/administration/access-identity/oidc/
- /docs/pulumi-cloud/access-management/oidc-client/
- /docs/pulumi-cloud/access-management/oidc/
- /docs/esc/administration/oidc-authentication/
- /docs/esc/access-management/oidc-authentication/
- /docs/administration/access-identity/oidc-issuers/
---

Register an external service, such as GitHub Actions, GitLab CI, Amazon EKS, or Google Kubernetes Engine, as a trusted OIDC issuer so its workloads can exchange their own short-lived OIDC tokens for Pulumi access tokens instead of storing a long-lived Pulumi token. For how token exchange, authorization policies, and token types work, see [OIDC issuers](/docs/administration/concepts/oidc-issuers/).

## Ways to manage OIDC issuers

You can configure and manage OIDC issuers in three ways:

- **Pulumi Cloud UI** — Navigate to **Settings → Access Management → OIDC Issuers**. This page walks through the UI flow.
- **REST API** — See the [OIDC issuers REST API reference](/docs/reference/cloud-rest-api/oidc-issuers/).
- **Pulumi Service provider** — Manage OIDC issuers as code using the [`OidcIssuer`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/oidcissuer/) resource in the Pulumi Service provider.

## Configuring an OIDC issuer in the UI

### Register the OIDC issuer

Navigate to **Settings → Access Management → OIDC Issuers** and select **Register issuer**. Provide:

- **Name** — a label for the issuer.
- **URL** — the issuer URL. Pulumi Cloud fetches the OpenID configuration metadata by appending `/.well-known/openid-configuration` to this URL.
- **Max expiration** — caps the duration of Pulumi access tokens issued via this trust relationship. Defaults to 25 hours.
- **Thumbprints** *(optional)* — the SHA-256 fingerprints of the TLS certificates that the issuer uses to serve its OpenID configuration. By default, Pulumi Cloud stores the thumbprint of the certificate used at registration time. Configure thumbprints manually if the provider uses multiple serving certificates or if you need to support certificate rotation.

#### How to calculate the certificate thumbprint

1. Use OpenSSL to fetch the certificates used by the issuer. Replace `example.com` with the issuer hostname:

   ```bash
   openssl s_client -servername example.com -showcerts -connect example.com:443
   ```

1. From the output, copy the first certificate into a file named `certificate.crt`.
1. Calculate the SHA-256 fingerprint:

   ```bash
   openssl x509 -in certificate.crt -fingerprint -sha256 -noout

   > sha256 Fingerprint=2B:60:30:08:8E:8D:08:FC:D6:1B:8B:89:70:19:F2:D9:9F:4B:9A:0F:7B:46:5B:06:5C:2B:90:E1:C5:3B:C0:7D
   ```

1. Strip the colons:

   ```
   2B6030088E8D08FCD61B8B897019F2D99F4B9A0F7B465B065C2B90E1C53BC07D
   ```

1. Configure the issuer with this thumbprint. If the provider serves content from multiple certificates, add a thumbprint for each.

### Configure the authorization policies

Pulumi Cloud denies any token exchange that no allow policy matches, and a new OIDC issuer starts with no allow policies. You must add explicit **allow** policies before tokens can be exchanged.

Each policy states the **Token type** it applies to (Organization, Team, Personal, or Deployment Runner) and, for team, personal, and deployment runner tokens, the team, user, or runner the token acts as. An allow policy issues that token. The token types available depend on your edition; see [Token types](/docs/administration/concepts/oidc-issuers/#token-types).

We recommend verifying the token's audience and subject claims against the provider's security guidance. For example, a GitHub Actions policy commonly checks `aud` against `urn:pulumi:org:<org-name>` and `sub` against `repo:<organization>/<repo>:*`.

When an exchange request matches more than one policy, deny always takes precedence over allow. A deny policy only matches requests for its own token type, team, user, or runner. See [Authorization policies](/docs/administration/concepts/oidc-issuers/#authorization-policies).

To target nested claims, define the claim path. Given this token payload:

```json
{
  "kubernetes.io": {
    "pod": {
      "name": "runner-ddfaa34e-dfrjh",
      "uid": "b99b58df-cce5-405a-a33d-49a4cf8cf7bd"
    }
  }
}
```

You can target the pod name with the claim path `"kubernetes.io".pod.name`. Quote dotted object keys.

Claim values and team scopes support wildcards:

- `*` — match zero or more characters
- `?` — match zero or one character
- `.` — match exactly one character

For example, `runner-*` matches any pod name beginning with `runner-`.

When the policy is complete, set the **Decision** to **Allow** and select **Save policies**.

## Exchanging OIDC tokens

### Using the Pulumi CLI

The Pulumi CLI supports OIDC token exchange natively through `pulumi login`. This is the recommended approach for most use cases:

```bash
pulumi login --oidc-token <token> --oidc-org <org-name>
```

The `--oidc-token` flag accepts either a raw token string or a file path prefixed with `file://`. You can also pass `--oidc-team`, `--oidc-user`, or `--oidc-expiration`. For more details, see the [`pulumi login` documentation](/docs/iac/cli/commands/pulumi_login/#oidc-token-exchange).

{{% notes type="warning" %}}
If you see an error like:

`OIDC token exchange failed: Post "/api/oauth/token": unsupported protocol scheme ""`

Include the backend URL explicitly: `pulumi login https://api.pulumi.com --oidc-token <token> --oidc-org <org-name>` (or the equivalent URL for a self-hosted backend).
{{% /notes %}}

### Using the REST API directly

For advanced scenarios where you need direct control over the token exchange process, call the OAuth 2.0 token endpoint with the token-exchange grant type. The endpoint accepts both `application/json` and `application/x-www-form-urlencoded` content types.

Parameters:

- `audience`: `urn:pulumi:org:{ORG_NAME}`
- `grant_type`: `urn:ietf:params:oauth:grant-type:token-exchange`
- `subject_token_type`: `urn:ietf:params:oauth:token-type:id_token`
- `requested_token_type`:
    - Organization token: `urn:pulumi:token-type:access_token:organization`
    - Team token (scope required): `urn:pulumi:token-type:access_token:team`
    - Personal token (scope required): `urn:pulumi:token-type:access_token:personal`
- `scope`: a single scope used when requesting a team or personal token, identifying the target team or user. Format: `team:{TEAM_NAME}` (for example, `team:OPS_AUTOMATIONS`) or `user:{USER_LOGIN}` (for example, `user:djohn`).
- `expiration`: token expiration in seconds. Defaults to 2 hours.
- `subject_token`: the id_token issued by the OIDC provider.

Example:

```bash
curl -X POST  \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'audience=urn:pulumi:org:test' \
    -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
    -d 'subject_token_type=urn:ietf:params:oauth:token-type:id_token' \
    -d 'requested_token_type=urn:pulumi:token-type:access_token:organization' \
    -d 'subject_token='...' \
    https://api.pulumi.com/api/oauth/token

{"access_token":"...","issued_token_type":"urn:pulumi:token-type:access_token:organization","token_type":"token","expires_in":7200,"scope":""}
```

## Provider-specific guides

- [Configuring OIDC for GitHub](/docs/administration/guides/oidc-issuers/github/)
- [Configuring OIDC for GitLab](/docs/administration/guides/oidc-issuers/gitlab/)
- [Configuring OIDC for Amazon EKS](/docs/administration/guides/oidc-issuers/kubernetes-eks/)
- [Configuring OIDC for Google Kubernetes Engine](/docs/administration/guides/oidc-issuers/kubernetes-gke/)
