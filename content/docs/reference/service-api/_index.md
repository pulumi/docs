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

### List Stacks for the authenticated user

```
GET https://api.pulumi.com/api/user/stacks
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | query | organization name to filter stacks by |
| `project` | string | query | organization name to filter stacks by |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
  https://api.pulumi.com/api/user/stacks
```

#### Default response

```
Status: 200 OK
```

```
{
  "stacks": [
    {
      "orgName": "org1",
      "projectName": "project1",
      "stackName": "dev",
      "lastUpdate": 1612481387,
      "resourceCount": 0
    },
    {
      "orgName": "org2",
      "projectName": "project2",
      "stackName": "prod",
      "lastUpdate": 1605474464,
      "resourceCount": 0
    }
  ]
}
```

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

```
POST https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `username` | string | path | user name |
| `role` | string | body | **Required.** The role to assign - possible values are `admin` or `member` |

#### Example

```bash
curl \
  --request POST \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
  https://api.pulumi.com/api/orgs/{organization}/members/{username} \
  --data '{ "role": "{role}" }'
```

#### Default response

```
Status: 200 OK
```

### Remove User from Organization

### Add User to Team

### Change User's Role

### Get Audit Log Events
