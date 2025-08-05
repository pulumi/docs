---
title: OIDC Issuers
title_tag: "Pulumi Cloud REST API: OIDC Issuers"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing OpenID Connect (OIDC) issuers for authentication with Pulumi Cloud.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 8
---

OpenID Connect (OIDC) issuers provide a way to authenticate with Pulumi Cloud using identity tokens from external providers like GitHub Actions. The OIDC Issuers API allows you to register and manage OIDC issuers for your organization.

## OIDC Issuer Operations

The API provides endpoints for the following operations:

- Registering new OIDC issuers
- Updating and deleting issuers
- Getting issuer details
- Listing all issuers for an organization
- Managing authentication policies for issuers

## Register a new issuer

Register a new OIDC issuer.

```plain
POST /api/orgs/{organization}/oidc/issuers
```

### Parameters

| Parameter           | Type          | In    | Description         |
|---------------------|---------------|-------|---------------------|
| `organization`      | string        | path  | organization name   |
| `name`              | string        | body  | oidc issuer name    |
| `url`               | string        | body  | issuer base url (this will be used as a base to build the OIDC configuration url, `url + /.well-known/openid-configuration`) |
| `thumbprints`       | array[string] | body  | **Optional.** issuer TLS certificate thumbprints |
| `maxExpiration`     | int           | body  | **Optional.** max expiration for tokens issued for this issuer in seconds    |
| `jwks`              | json ([jwks format](https://datatracker.ietf.org/doc/html/rfc7517)) | body  | **Optional.** JWK Set from the OIDC issuer    |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{ "name":"GitHub", "url": "https://token.actions.githubusercontent.com", "maxExpiration": 3600 }' \
  https://api.pulumi.com/api/orgs/{organization}/oidc/issuers
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "id": "e9a13d0e-798e-4e33-bab2-dde06da317bf",
  "name": "github",
  "url": "https://token.actions.githubusercontent.com",
  "issuer": "https://token.actions.githubusercontent.com",
  "created": "2024-04-19 15:07:54.693",
  "thumbprints": [
      "2b6030088e8d08fcd61b8b897019f2d99f4b9a0f7b465b065c2b90e1c53bc07d"
  ],
  "maxExpiration": 3600,
}
```

## Update an issuer

Update an existing OIDC issuer.

```plain
PATCH /api/orgs/{organization}/oidc/issuers/{issuerId}
```

### Parameters

| Parameter           | Type          | In    | Description         |
|---------------------|---------------|-------|---------------------|
| `organization`      | string        | path  | organization name   |
| `issuerId`          | string        | path  | issuer id to update |
| `name`              | string        | body  | oidc issuer name    |
| `thumbprints`       | array[string] | body  | **Optional.** issuer TLS certificate thumbprints |
| `maxExpiration`     | int           | body  | **Optional.** max expiration for tokens issued for this issuer in seconds    |
| `jwks`              | json ([jwks format](https://datatracker.ietf.org/doc/html/rfc7517)) | body  | **Optional.** JWK Set from the OIDC issuer    |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  --data '{ "name":"GitHub", "maxExpiration": 3600 }' \
  https://api.pulumi.com/api/orgs/{organization}/oidc/issuers/{issuerId}
```

## Delete an issuer

Delete an OIDC issuer.

```plain
DELETE /api/orgs/{organization}/oidc/issuers/{issuerId}
```

### Parameters

| Parameter           | Type          | In    | Description         |
|---------------------|---------------|-------|---------------------|
| `organization`      | string        | path  | organization name   |
| `issuerId`          | string        | path  | issuer id to update |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{organization}/oidc/issuers/{issuerId}
```

## Get an issuer

Get details about a specific OIDC issuer.

```plain
GET /api/orgs/{organization}/oidc/issuers/{issuerId}
```

### Parameters

| Parameter           | Type          | In    | Description         |
|---------------------|---------------|-------|---------------------|
| `organization`      | string        | path  | organization name   |
| `issuerId`          | string        | path  | issuer id to update |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/oidc/issuers/{issuerId}
```

## List issuers

List all OIDC issuers for an organization.

```plain
GET /api/orgs/{organization}/oidc/issuers
```

### Parameters

| Parameter           | Type          | In    | Description         |
|---------------------|---------------|-------|---------------------|
| `organization`      | string        | path  | organization name   |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/{organization}/oidc/issuers
```

## Get the issuer's auth policies

Get authentication policies for an OIDC issuer.

```plain
GET /api/orgs/{organization}/auth/policies/oidcissuers/{issuerId}
```

### Parameters

| Parameter           | Type          | In    | Description         |
|---------------------|---------------|-------|---------------------|
| `organization`      | string        | path  | organization name   |
| `issuerId`          | string        | path  | issuer id to update |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/auth/policies/oidcissuers/{issuerId}
```

## Update the issuer's auth policies

Update authentication policies for an OIDC issuer.

```plain
PATCH /api/orgs/{organization}/auth/policies/{policyId}
```

### Parameters

| Parameter           | Type          | In    | Description         |
|---------------------|---------------|-------|---------------------|
| `organization`      | string        | path  | organization name   |
| `policyId`          | string        | path  | policy id to update |
| `policies`          | array[object] | body  | array of policies   |
| `policy.decision`   | string        | body  | `deny`/`allow`   |
| `policy.tokenType`  | string        | body  | `organization`/`team`/`personal`/`runner`   |
| `policy.teamName`   | string        | body  | the team name to issue tokens on behalf of, required for team token type  |
| `policy.userLogin`  | string        | body  | the user login to issue tokens on behalf of, required for personal token type  |
| `policy.runnerID`   | string        | body  | the runner name to issue tokens for, required for runner token type  |
| `policy.authorizedPermissions`  | array[string] | body  | permissions allowed by the policy (only `admin` is supported for organization tokens)  |
| `policy.rules`      | object        | body  |  rules to match the token claims |

For more information about authorization rules, refer to [its documentation](/docs/pulumi-cloud/access-management/oidc/client/#configure-the-authorization-policies).

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  --data '{ "policies": [{ "decision": "allow", "tokenType": "organization", "rules": { "aud": "urn:pulumi:org:org-name", "sub": "repo:organization/repo:*" }}] }' \
  https://api.pulumi.com/api/orgs/{organization}/auth/policies/{policyId}
```
