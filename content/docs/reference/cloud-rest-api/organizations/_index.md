---
title: Organizations
title_tag: "Pulumi Cloud REST API: Organizations"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing organizations, teams, members, and organization-level access tokens.
menu:
    reference:
        parent: cloud-rest-api
        weight: 9
aliases:
  - /docs/reference/cloud-rest-api/organizations/
  - /docs/pulumi-cloud/reference/organizations/
---

The Organizations API allows you to manage Pulumi Cloud organizations, including members, teams, access tokens, and webhooks. Organizations are the primary management boundary in Pulumi Cloud.

## Organization Operations

The API provides endpoints for the following categories of operations:

- Managing organization members (adding, updating, removing)
- Managing organization access tokens
- Creating and managing teams
- Managing team access tokens

## User Management

### List Users

List all members of an organization.

```plain
GET /api/orgs/{organization}/members
```

#### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `continuationToken` | string | query | **Optional.** the continuation token to use for retrieving the next set of results if results were truncated |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/members
```

#### Default response

```plain
Status: 200 OK
```

```plain
{
  "members": [
    {
      "role": "member",
      "user": {
        "name": "First Last",
        "githubLogin": "user2",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300",
        "email": "user@example.com"
      },
      "knownToPulumi": true,
      "virtualAdmin": false
    },
    {
      "role": "admin",
      "user": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300",
        "email": "admin@example.com"
      },
      "knownToPulumi": true,
      "virtualAdmin": false
    }
  ]
}
```

### Add User to Organization

Add a user to an organization. The user must have already signed up for a Pulumi account and meet the organization membership requirements to be added.

```plain
POST /api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter      | Type   | In   | Description                                                  |
|----------------|--------|------|--------------------------------------------------------------|
| `organization` | string | path | organization name                                            |
| `username`     | string | path | user name                                                    |
| `role`         | string | body | The role to assign - possible values are `admin` or `member` |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"role":"{role}"}' \
  https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

### Update User's Role

Update a user's role in an organization.

```plain
PATCH /api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter      | Type   | In    | Description                                                  |
|----------------|--------|-------|--------------------------------------------------------------|
| `organization` | string | path  | organization name to filter stacks by                        |
| `username`     | string | path  | user name                                                    |
| `role`         | string | body  | The role to assign - possible values are `admin` or `member` |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  --data '{"role":"{role}"}' \
  https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

### Remove User from Organization

Remove a user from an organization.

```plain
DELETE /api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter      | Type   | In   | Description       |
|----------------|--------|------|-------------------|
| `organization` | string | path | organization name |
| `username`     | string | path | user name         |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

## Organization Access Tokens

### List Organization Access Tokens

List all access tokens for an organization.

```plain
GET /api/orgs/{organization}/tokens
```

#### Parameters

| Parameter           | Type   | In    | Description                                                                                |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------|
| `organization`.     | string | path  | Organization to list the access tokens for.                                                |
| `show_expired`      | string | query | **Optional.** whether to return previously expired tokens with results. Defaults to false. |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{org}/tokens?show_expired=true
```

### Create Organization Access Token

Create a new access token for an organization.

```plain
POST /api/orgs/{org}/tokens
```

#### Parameters

| Parameter     | Type   | In   | Description                                                                                                                        |
|---------------|--------|------|------------------------------------------------------------------------------------------------------------------------------------|
| `description` | string | body | Description of the access token.                                                                                                   |
| `name`        | string | body | Unique name of the access token, up to 40 characters. Must be unique across the org, including deleted tokens.                     |
| `expires`     | int    | body | **Optional.** unix epoch timestamp at which the token should expire, up to two years from present. 0 for no expiry. Defaults to 0. |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"description": "{description}", "name": "{unique_name}", "expires": 0}' \
  https://api.pulumi.com/api/orgs/{org}/tokens
```

### Delete Organization Access Token

Delete an organization access token.

```plain
DELETE /api/orgs/{org}/tokens/{tokenId}
```

#### Parameters

| Parameter | Type   | In   | Description          |
|-----------|--------|------|----------------------|
| `tokenId` | string | path | the token identifier |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{org}/tokens/{tokenId}
```

## Teams

### List Teams

List all teams in an organization.

```plain
GET /api/orgs/{organization}/teams
```

#### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/teams
```

### Create Team

Create a new team in an organization.

```plain
POST /api/orgs/{org}/teams/{teamType}
```

#### Parameters

| Parameter      | Type   | In   | Description                                                         |
|----------------|--------|------|---------------------------------------------------------------------|
| `organization` | string | path | organization name                                                   |
| `teamType`     | string | path | the type of team to create - valid options are `pulumi` or `github` |
| `name`         | string | body | team name                                                           |
| `displayName`  | string | body | **Optional.** team display name                                     |
| `description`  | string | body | **Optional.** team description                                      |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"name":"example-team","displayName":"example display name","description":"example description"}' \
  https://api.pulumi.com/api/orgs/{org}/teams/pulumi
```

### Get Team

Get details about a specific team.

```plain
GET /api/orgs/{org}/teams/{teamName}
```

#### Parameters

| Parameter      | Type   | In   | Description                                                         |
|----------------|--------|------|---------------------------------------------------------------------|
| `organization` | string | path | organization name                                                   |
| `teamName`     | string | path | team name                                                           |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request GET \
  https://api.pulumi.com/api/orgs/{org}/teams/{teamName}
```

### Delete Team

Delete a team from an organization.

```plain
DELETE /api/orgs/{org}/teams/{teamName}
```

#### Parameters

| Parameter      | Type   | In   | Description       |
|----------------|--------|------|-------------------|
| `organization` | string | path | organization name |
| `teamName`     | string | path | team name         |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{org}/teams/{teamName}
```

## Team Management

### Update Team Membership

Add or remove a member of the organization to or from a team

```plain
PATCH /api/orgs/{organization}/teams/{team}
```

#### Parameters

| Parameter      | Type   | In   | Description                                                        |
|----------------|--------|------|--------------------------------------------------------------------|
| `organization` | string | path | organization name                                                  |
| `team`         | string | path | team name                                                          |
| `member`       | string | body | user name                                                          |
| `memberAction` | string | body | add or remove user (available values are `add` or `remove`)        |

#### Example

```bash

// To add an organization member to a team:
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  -d '{ "memberAction": "add", "member": "{username}" }' \
  https://api.pulumi.com/api/orgs/{org}/teams/{teamName}

// To remove an organization member from a team:
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  -d '{ "memberAction": "remove", "member": "{username}" }' \
  https://api.pulumi.com/api/orgs/{org}/teams/{teamName}
```

## Webhooks

For comprehensive information about webhooks including setup, configuration, event filtering, and complete API reference, see the [Webhooks documentation](/docs/deployments/webhooks/) and [Webhooks REST API reference](/docs/reference/cloud-rest-api/webhooks/).
