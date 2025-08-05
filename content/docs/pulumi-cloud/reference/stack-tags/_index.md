---
title: Stack Tags
title_tag: "Pulumi Cloud REST API: Stack Tags"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing stack tags and metadata.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 22
---

Stack tags are key-value metadata attached to Pulumi stacks. They can be used for organization, filtering, and to store additional information about your stacks.

## Tag Operations

The API provides endpoints for the following operations:

- Getting all tags for a stack
- Setting a specific tag value
- Deleting tags from a stack

## Get Stack Tags

Use [Get Stack](/docs/pulumi-cloud/reference/stacks/#get-stack) to retrieve a stack's details including its tags.

## Set Stack Tag

```plain
POST /api/stacks/{organization}/{project}/{stack}/tags
```

### Parameters

| Parameter      | Type   | In   | Description       |
|----------------|--------|------|-------------------|
| `organization` | string | path | organization name |
| `project`      | string | path | project name      |
| `stack`        | string | path | stack name        |
| `name`         | string | body | tag name          |
| `value`        | string | body | tag value         |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"name":"{tagName}","value":"{tagValue}"}' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/tags
```

### Default response

```plain
Status: 204 OK
```

```plain
EMPTY RESPONSE BODY
```

## Delete Stack Tag

```plain
DELETE /api/stacks/{organization}/{project}/{stack}/tags/{tagName}
```

### Parameters

| Parameter      | Type   | In   | Description       |
|----------------|--------|------|-------------------|
| `organization` | string | path | organization name |
| `project`      | string | path | project name      |
| `stack`        | string | path | stack name        |
| `tagName`      | string | path | tag name          |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/tags/{tagName}
```

### Default response

```plain
Status: 204 OK
```

```plain
EMPTY RESPONSE BODY
```
