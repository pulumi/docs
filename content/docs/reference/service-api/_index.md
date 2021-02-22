---
title: "Pulumi Service API"
meta_desc: An overview of the Pulumi Service API for querying Organization, Stack, State, etc. information
---

The Pulumi Service API is used by the Pulumi CLI and the Pulumi Console to query and interact with state information, history, stack tags, etc. This API is available for end users to integrate into their own automation use cases.

{{% notes "info" %}}
While the Pulumi Service API is used by the Pulumi CLI and Pulumi Console, Pulumi makes no guarantees about changes that might affect backwards compatibility or cause breaking changes.
{{% /notes %}}

## Authentication

All requests must be authenticated using a token via the `Authorization` HTTP header. If the token is missing or invalid, the Pulumi Service API will return a 4xx status code.

The `Authorization` header must be in the form below with the literal string `token`, then a space, then your access token value. 

```
Authorization: token {token}
```

{{% notes "info" %}}
As of June 28, 2019, Pulumi access tokens contain the prefix `pul-`, which should be included as part of the token value in the header.
{{% /notes %}}

To view your access tokens, or create a new one manually, view the <a href="https://app.pulumi.com/account/tokens" target="_blank">Access Tokens</a> page. You will see a list of past tokens, when they were last used, as well as the ability to revoke them.

## Required Request Headers

TODO: Add more info.

```
Accept: application/vnd.pulumi+3
Content-Type: application/json
```

## Stacks

<!-- ###################################################################### -->

### List Stacks

### Get Stack

### Get Stack State

## Stack Updates

### List Stack Updates

### Get Update Status

### List Update Events

## Organizations

### Add User to Organization

Users are not just-in-time provisioned. They must sign in to the Pulumi console first (they will receive an error that they're not a member) and then they can be added to the organization.

TODO: Add note about SAML.

#### HTTP Request

```
POST https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Path Parameters

| Parameter | Type | Description |
| --------- | ---------- | ---------- |
| `organization` | string | organization name |
| `username` | string | user name |

#### Query Parameters

| Parameter | Type | Description |
| --------- | ---------- | ---------- |
| `none` | string (optional) | none description |

#### Request Body

| Parameter | Type | Description |
| --------- | ---------- | ---------- |
| `role` | string | role to assign - possible values are `admin` or `member` |

#### Sample Payload

```
{ "role": "{role}" }
```

#### Curl Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
  --request POST \
  --data @payload.json \
  https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

### Remove User from Organization

### Add User to Team

### Change User's Role

### Get Audit Log Events
