---
title: OAuth Token Exchange
title_tag: "Pulumi Cloud REST API: OAuth Token Exchange"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for exchanging external tokens for Pulumi access tokens.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 7
---

The OAuth Token Exchange API allows you to exchange external identity tokens (like those from OIDC providers) for Pulumi access tokens. This enables automated workflows to authenticate with Pulumi Cloud without storing long-lived credentials.

## Token Exchange Operations

The API provides an endpoint for exchanging tokens:

- Exchanging external tokens for Pulumi access tokens of various types

## Exchange Token

Exchange an external token for a Pulumi token via an OIDC issuer trust relationship.

```plain
POST /api/oauth/token
```

### Parameters

| Parameter              | Type   | In    | Description                                                                                                      |
|------------------------|--------|-------|------------------------------------------------------------------------------------------------------------------|
| `audience`             | string | body  | OAuth audience in the form `urn:pulumi:org:ORG_NAME`                                                             |
| `grant_type`           | string | body  | OAuth grant type (only `urn:ietf:params:oauth:grant-type:token-exchange` is supported)                           |
| `subject_token_type`   | string | body  | OAuth subject token type (only `urn:ietf:params:oauth:token-type:id_token` is supported)                         |
| `requested_token_type` | string | body  | OAuth requested token type (prefix of `urn:pulumi:token-type:access_token:TOKEN_TYPE` where TOKEN_TYPE is `organization`, `team`, `personal`, or `runner`) |
| `expiration`           | number | body  | OAuth token expiration in seconds                                                                                |
| `scope`                | string | body  | OAuth scope as a comma-separated array. This depends on the requested token type. For requested token type `organization`, scopes must be empty or `admin`. For `team`, the scope must be `team:TEAM_NAME`. For `personal`, it must be `user:USER_LOGIN`. For `runner`, it must be `runner:RUNNER_NAME`. |
| `subject_token`        | string | body  | The external token to exchange (usually from your OIDC provider)                                                |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  --request POST \
  --data '{"audience":"urn:pulumi:org:ORG_NAME","grant_type":"urn:ietf:params:oauth:grant-type:token-exchange","subject_token_type":"urn:ietf:params:oauth:token-type:id_token","requested_token_type":"urn:pulumi:token-type:access_token:organization","expiration":7200,"scope":"","subject_token":"$SOURCE_TOKEN"}' \
  https://api.pulumi.com/api/oauth/token
```

### Default response

```plain
Status: 200 OK
```

```json
{
  "access_token": "redacted",
  "issued_token_type": "urn:pulumi:token-type:access_token:organization",
  "token_type": "token",
  "expires_in": 7200,
  "scope": "",
  "refresh_token": ""
}
```
