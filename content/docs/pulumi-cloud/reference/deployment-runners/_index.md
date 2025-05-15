---
title: Deployment Runners
title_tag: "Pulumi Cloud REST API: Deployment Runners"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing deployment runner pools for private environments.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 4
---

Deployment Runners execute Pulumi deployments in private, controlled environments. The Deployment Runners API allows you to manage runner pools, which are groups of deployment runners that can handle Pulumi operations.

## Deployment Runner Operations

The API provides endpoints for the following operations:

- Registering new deployment runner pools
- Updating and deleting pools
- Getting pool details
- Listing registered pools

## Register a new pool

Create a new deployment runner pool.

```plain
POST /api/orgs/{organization}/agent-pools
```

### Parameters

| Parameter           | Type      | In    | Description         |
|---------------------|-----------|-------|---------------------|
| `organization`      | string    | path  | organization name   |
| `name`              | string    | body  | pool name           |
| `description`       | string    | body  | pool description    |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{ "name":"Production", "description": "Pool for the production account" }' \
  https://api.pulumi.com/api/orgs/{organization}/agent-pools
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "id": "12345678-8102-447f-b246-e9ec85786e23",
  "tokenValue": "pul-75a564ac7f3a48079a0c448c1e1ec95c4cfed141"
}
```

## Update a pool

Update an existing deployment runner pool.

```plain
PATCH /api/orgs/{organization}/agent-pools/{poolId}
```

### Parameters

| Parameter           | Type      | In    | Description         |
|---------------------|-----------|-------|---------------------|
| `organization`      | string    | path  | organization name   |
| `poolId`            | string    | path  | pool id to update   |
| `name`              | string    | body  | pool name           |
| `description`       | string    | body  | pool description    |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  --data '{ "name":"Production", "description": "Pool for the production account" }' \
  https://api.pulumi.com/api/orgs/{organization}/agent-pools/{poolId}
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "name":"Production",
  "description": "Pool for the production account"
}
```

## Delete a pool

Delete a deployment runner pool.

```plain
DELETE /api/orgs/{organization}/agent-pools/{poolId}
```

### Parameters

| Parameter           | Type      | In    | Description         |
|---------------------|-----------|-------|---------------------|
| `organization`      | string    | path  | organization name   |
| `poolId`            | string    | path  | pool id to delete   |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{organization}/agent-pools/{poolId}
```

### Default response

```plain
Status: 204 OK
```

## Get pool details

Get details about a specific deployment runner pool.

```plain
GET /api/orgs/{organization}/agent-pools/{poolId}
```

### Parameters

| Parameter           | Type      | In    | Description         |
|---------------------|-----------|-------|---------------------|
| `organization`      | string    | path  | organization name   |
| `poolId`            | string    | path  | pool id to fetch    |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/agent-pools/{poolId}
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "created": 1715701863000,
  "id": "12345678-8102-447f-b246-e9ec85786e23",
  "name":"Production",
  "description": "Pool for the production account",
  "agents": [
    {
      "version": "v1.1.0",
      "hostname": "private-ipv4-address.kind.internal",
      "ip": "192.168.0.17",
      "pid": "58188",
      "lastSeen": 1719498194000,
      "status": "online"
    }
  ]
}
```

## List registered pools

List all deployment runner pools for an organization.

```plain
GET /api/orgs/{organization}/agent-pools
```

### Parameters

| Parameter           | Type      | In    | Description         |
|---------------------|-----------|-------|---------------------|
| `organization`      | string    | path  | organization name   |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/agent-pools
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "agentPools": [
    {
      "created": 1715701863000,
      "id": "12345678-8102-447f-b246-e9ec85786e23",
      "name":"Production",
      "description": "Pool for the production account",
      "lastSeen": 1715796999,
      "status": "online",
      "lastDeployment": 1715796961
    }
  ]
}
```
