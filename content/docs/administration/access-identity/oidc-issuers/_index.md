---
title_tag: OIDC Issuers integration for Pulumi Cloud
meta_desc: This page provides an overview of how to configure OIDC Issuers in Pulumi Cloud
           to establish trust relationships with third-party OIDC providers.
title: OIDC Issuers
h1: OIDC Issuers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    parent: administration-access-identity
    weight: 4
    identifier: administration-access-identity-oidc-issuers
aliases:
- /docs/administration/access-identity/oidc-client/
- /docs/pulumi-cloud/oidc/client/
- /docs/pulumi-cloud/oidc/
- /docs/administration/access-identity/oidc/client/
- /docs/administration/access-identity/oidc/
- /docs/pulumi-cloud/access-management/oidc-client/
- /docs/pulumi-cloud/access-management/oidc/
---

**OIDC Issuers let outside services securely obtain Pulumi Cloud access tokens via OIDC.** Instead of provisioning a long-lived Pulumi access token and storing it as a secret in your CI system, build runner, or Kubernetes cluster, you register that external service as a trusted OIDC Issuer in Pulumi Cloud. Workloads on the service then present their own short-lived OIDC id_tokens and receive short-lived Pulumi access tokens in exchange — no hardcoded credentials.

## Overview

Any third-party service that can issue OIDC id_tokens — GitHub Actions, GitLab CI, AWS EKS, Google GKE, and others — can be registered in Pulumi Cloud as a trusted **OIDC Issuer**. The flow is always the same:

1. The external workload obtains an OIDC id_token from its host service.
1. The workload exchanges that id_token with Pulumi Cloud for a short-lived Pulumi access token.
1. The workload uses the Pulumi access token to run Pulumi operations.

This direction matters: OIDC Issuers configure how *inbound* tokens from external services are accepted and translated into Pulumi tokens. They are not used to issue tokens *from* Pulumi Cloud to other services.

## Ways to manage OIDC Issuers

You can configure and manage OIDC Issuers in three ways:

- **Pulumi Cloud UI** — Navigate to **Settings → Access Management → OIDC Issuers**. This page walks through the UI flow.
- **REST API** — See the [OIDC Issuers REST API reference](/docs/reference/cloud-rest-api/oidc-issuers/).
- **Pulumi Service provider** — Manage OIDC Issuers as code using the [`OidcIssuer`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/oidcissuer/) resource in the Pulumi Service provider.

## Token types by edition

The available OIDC token types vary by Pulumi edition:

- **Individual**: `personal`
- **Team**: `personal`, `organization`
- **Enterprise**: `personal`, `organization`, `team`
- **Business Critical**: `personal`, `organization`, `team`, `deployment-runner`

When configuring authorization policies and requesting tokens, ensure you select a token type that is available for your edition.

## Configuring an OIDC Issuer in the UI

### Register the OIDC Issuer

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

When you register a new OIDC Issuer, Pulumi Cloud provisions a default authorization policy that denies every token exchange. You must add explicit **allow** policies before tokens can be exchanged.

Each policy must state the **Token type** the policy issues (Organization, Team, Personal, or Deployment Runner) and the team or user the token is scoped to.

We recommend verifying the token's audience and subject claims against the provider's security guidance. For example, a GitHub Actions policy commonly checks `aud` against `urn:pulumi:org:<org-name>` and `sub` against `repo:<organization>/<repo>:*`.

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

- [Configuring OIDC for GitHub](/docs/administration/access-identity/oidc-issuers/github/)
- [Configuring OIDC for GitLab](/docs/administration/access-identity/oidc-issuers/gitlab/)
- [Configuring OIDC for Amazon EKS](/docs/administration/access-identity/oidc-issuers/kubernetes-eks/)
- [Configuring OIDC for Google Kubernetes Engine](/docs/administration/access-identity/oidc-issuers/kubernetes-gke/)
