---
title: Services
title_tag: "Pulumi Cloud REST API: Services"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing services that group related resources together.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 19
---

Services are a way to group and organize related resources in Pulumi Cloud. The Services API allows you to create, manage, and organize collections of resources that work together to provide a specific capability.

## Service Operations

The API provides endpoints for the following operations:

- Creating and managing services
- Listing available services
- Adding and removing items from services

## Create Service

Create a new service.

```plain
POST /api/orgs/{organization}/services
```

### Parameters

| Parameter           | Type   | In    | Description                                                |
|---------------------|--------|-------|------------------------------------------------------------|
| `organization`      | string | path  | organization name                                          |
| `ownerType`         | string | body  | type of the owner (e.g. "user", "team")                    |
| `ownerName`         | string | body  | name of the owner                                          |
| `name`              | string | body  | name of the service                                        |
| `description`       | string | body  | **Optional.** description of the service                   |
| `properties`        | array  | body  | **Optional.** list of properties to set on the service     |
| `items`             | array  | body  | **Optional.** list of items to add during service creation |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --X POST \
  --data '{ "ownerType": "team", "ownerName": "team1", "name": "my-cool-service", "description": "My service" }' \
  https://api.pulumi.com/api/orgs/my-org/services
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "organizationName": "org1",
  "name": "service1",
  "description": "My service",
  "itemCountSummary": {},
  "members": [
    {
      "name": "team1",
      "avatarURL": "https://example.com/avatar.png",
      "type": "team"
    }
  ],
  "properties": [],
  "owner": {
    "name": "team1",
    "avatarURL": "https://example.com/avatar.png",
    "type": "team"
  }
}
```

## List Services

List all services in an organization.

```plain
GET /api/orgs/{organization}/services
```

### Parameters

| Parameter           | Type   | In    | Description       |
|---------------------|--------|-------|-------------------|
| `organization`      | string | path  | organization name |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/my-org/services
```

## Head Service

Check if a service exists.

```plain
HEAD /api/orgs/{organization}/services/{ownerType}/{ownerName}/{serviceName}
```

### Parameters

| Parameter           | Type   | In    | Description                               |
|---------------------|--------|-------|-------------------------------------------|
| `organization`      | string | path  | organization name                         |
| `ownerType`         | string | path  | type of the owner (e.g. "user", "team")   |
| `ownerName`         | string | path  | name of the owner                         |
| `serviceName`       | string | path  | name of the service                       |

## Get Service

Get details of a specific service.

```plain
GET /api/orgs/{organization}/services/{ownerType}/{ownerName}/{serviceName}
```

### Parameters

| Parameter           | Type   | In    | Description                               |
|---------------------|--------|-------|-------------------------------------------|
| `organization`      | string | path  | organization name                         |
| `ownerType`         | string | path  | type of the owner (e.g. "user", "team")   |
| `ownerName`         | string | path  | name of the owner                         |
| `serviceName`       | string | path  | name of the service                       |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/my-org/services/team/my-team/my-service
```

## Update Service

Update an existing service.

```plain
PATCH /api/orgs/{organization}/services/{ownerType}/{ownerName}/{serviceName}
```

### Parameters

| Parameter           | Type   | In    | Description                                            |
|---------------------|--------|-------|--------------------------------------------------------|
| `organization`      | string | path  | organization name                                      |
| `ownerType`         | string | path  | type of the owner (e.g. "user", "team")                |
| `ownerName`         | string | path  | name of the owner                                      |
| `serviceName`       | string | path  | name of the service                                    |
| `name`              | string | body  | **Optional.** new name for the service                 |
| `description`       | string | body  | **Optional.** new description for the service          |
| `properties`        | array  | body  | **Optional.** list of properties to set on the service |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{ "name": "new-service-name", "description": "New description" }' \
  https://api.pulumi.com/api/orgs/my-org/services/team/my-team/my-service
```

## Delete Service

Delete a service.

```plain
DELETE /api/orgs/{organization}/services/{ownerType}/{ownerName}/{serviceName}
```

### Parameters

| Parameter           | Type    | In    | Description                                                   |
|---------------------|---------|-------|---------------------------------------------------------------|
| `organization`      | string  | path  | organization name                                             |
| `ownerType`         | string  | path  | type of the owner (e.g. "user", "team")                       |
| `ownerName`         | string  | path  | name of the owner                                             |
| `serviceName`       | string  | path  | name of the service                                           |
| `force`             | boolean | query | **Optional.** ignore protections and force delete the service |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/my-org/services/team/my-team/my-service?force=true
```

## Add Service Items

Add items to a service.

```plain
POST /api/orgs/{organization}/services/{ownerType}/{ownerName}/{serviceName}/items
```

### Parameters

| Parameter           | Type   | In    | Description                             |
|---------------------|--------|-------|-----------------------------------------|
| `organization`      | string | path  | organization name                       |
| `ownerType`         | string | path  | type of the owner (e.g. "user", "team") |
| `ownerName`         | string | path  | name of the owner                       |
| `serviceName`       | string | path  | name of the service                     |
| `items`             | array  | body  | array of items to add to the service    |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{ "items": [
    {
      "type": "stack",
      "name": "my-project/my-stack"
    },
    {
      "type": "environment",
      "name": "my-project/my-environment
    }
  ] }' \
  https://api.pulumi.com/api/orgs/my-org/services/team/my-team/my-service/items
```

## Remove Service Item

Remove an item from a service.

```plain
DELETE /api/orgs/{organization}/services/{ownerType}/{ownerName}/{serviceName}/items/{itemType}/{itemName}
```

### Parameters

| Parameter           | Type   | In    | Description                             |
|---------------------|--------|-------|-----------------------------------------|
| `organization`      | string | path  | organization name                       |
| `ownerType`         | string | path  | type of the owner (e.g. "user", "team") |
| `ownerName`         | string | path  | name of the owner                       |
| `serviceName`       | string | path  | name of the service                     |
| `itemType`          | string | path  | type of the item to remove              |
| `itemName`          | string | path  | name of the item to remove              |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/my-org/services/team/my-team/my-service/items/stack/my-project/my-stack
```
