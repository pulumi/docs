---
title: Organizations
title_tag: "Pulumi Cloud REST API: Organizations"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing organizations, teams, members, and organization-level access tokens and webhooks.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 9
---

The Organizations API allows you to manage Pulumi Cloud organizations, including members, teams, access tokens, and webhooks. Organizations are the primary management boundary in Pulumi Cloud.

## Organization Operations

The API provides endpoints for the following categories of operations:

- Managing organization members (adding, updating, removing)
- Managing organization access tokens
- Creating and managing teams
- Managing team access tokens
- Creating and managing webhooks

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
| `organization` | string | query | organization name to filter stacks by                        |
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
GET /api/orgs/{org}/tokens
```

#### Parameters

| Parameter           | Type   | In    | Description                                                                                |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------|
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
Get /api/orgs/{org}/teams/{teamName}
```

#### Parameters

| Parameter      | Type   | In   | Description                                                         |
|----------------|--------|------|---------------------------------------------------------------------|
| `organization` | string | path | organization name                                                   |
| `teamName`     | string | body | team name                                                           |

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

## Webhooks

### Create Webhook

Create a new webhook for an organization or stack.

```plain
// To create an organization webhook
POST /api/orgs/{organization}/hooks

// To create a stack webhook
POST /api/stacks/{organization}/{project}/{stack}/hooks
```

#### Parameters

| Parameter          | Type          | In   | Description                                                                                                                                                                     |
|--------------------|---------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `active`           | boolean       | body | enable webhook                                                                                                                                                                  |
| `displayName`      | string        | body | name of webhook                                                                                                                                                                 |
| `organizationName` | string        | body | organization name                                                                                                                                                               |
| `payloadUrl`       | string        | body | URL to send request to                                                                                                                                                          |
| `projectName`      | string        | body | **Optional.** project name (required for stack webhooks)                                                                                                                        |
| `stackName`        | string        | body | **Optional.** stack name (required for stack webhooks)                                                                                                                          |
| `format`           | string        | body | **Optional.** format of the payload. Possible values are `raw`, `slack`, `ms_teams` or `pulumi_deployments`. Default is `raw`.                                                  |
| `filters`          | array[string] | body | **Optional.** list of filters for events the webhook should receive. See [webhook docs](/docs/pulumi-cloud/webhooks#filters) for more information on what filters are available |
| `secret`           | string        | body | **Optional.** secret used as the HMAC key. See [webhook docs](/docs/pulumi-cloud/webhooks#headers) for more information                                                         |

### List Webhooks

List all webhooks for an organization or stack.

```plain
// List organization webhooks
GET /api/orgs/{organization}/hooks

// List stack webhooks
GET /api/stacks/{organization}/{project}/{stack}/hooks
```

### Get Webhook

Get details about a specific webhook.

```plain
// Get organization webhook
GET /api/orgs/{organization}/hooks/{webhookname}

// Get stack webhook
GET /api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}
```

### Ping Webhook

Send a test ping to a webhook to validate it's working.

```plain
// Ping organization webhook
POST /api/orgs/{organization}/hooks/{webhookname}/ping

// Ping stack webhook
POST /api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}/ping
```
