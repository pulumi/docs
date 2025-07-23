---
title: Stack Config
title_tag: "Pulumi Cloud REST API: Stack Config"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing stack config.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 20
---

{{% notes type="info" %}}
Stack Config APIs return service-managed configuration only. If you are looking for stack config variables, please refer to the [Stack Updates APIs](../stack-updates/_index.md).
{{% /notes %}}

Stack config endpoints allow you to manage service-managed configuration settings for your Pulumi stacks, including environment settings and secrets management configuration. If stack configuration is returned by the API, it is used in place of the local stack config file (e.g. `Pulumi.[stack].yaml`).

## Stack Config Operations

The API provides endpoints for the following operations:

- Getting a stack's service-managed configuration
- Updating a stack's service-managed configuration
- Deleting a stack's service-managed configuration

## Get Stack Config

Retrieves the service-manated configuration settings for a specific stack.

```plain
GET /api/stacks/{organization}/{project}/{stack}/config
```

### Parameters

| Parameter      | Type   | In   | Description       |
|----------------|--------|------|-------------------|
| `organization` | string | path | organization name |
| `project`      | string | path | project name      |
| `stack`        | string | path | stack name        |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/config
```

### Default response

```plain
Status: 200 OK
```

```json
{
  "environment": "string",
  "secretsProvider": "string",
  "encryptedKey": "string",
  "encryptionSalt": "string"
}
```

## Update Stack Config

Updates the service-managed configuration settings for a specific stack.

```plain
PUT /api/stacks/{organization}/{project}/{stack}/config
```

### Parameters

| Parameter      | Type   | In   | Description       |
|----------------|--------|------|-------------------|
| `organization` | string | path | organization name |
| `project`      | string | path | project name      |
| `stack`        | string | path | stack name        |

### Request Body

The request body should be a `StackConfig` object with the following fields:

| Field             | Type   | Description                                    |
|-------------------|--------|------------------------------------------------|
| `environment`     | string | **Optional.** The reference to the ESC environment to use as stack configuration |
| `secretsProvider` | string | **Optional.** The secrets provider configuration             |
| `encryptedKey`    | string | **Optional.** The encrypted key for secrets management       |
| `encryptionSalt`  | string | **Optional.** The encryption salt used for secrets           |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PUT \
  --data '{
    "environment": "default/prod",
    "secretsProvider": "default",
    "encryptedKey": "key",
    "encryptionSalt": "salt"
  }' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/config
```

### Default response

```plain
Status: 200 OK
```

```json
{
  "environment": "default/prod",
  "secretsProvider": "default",
  "encryptedKey": "key",
  "encryptionSalt": "salt"
}
```

## Delete Stack Config

Deletes the service-managed configuration settings for a specific stack.

```plain
DELETE /api/stacks/{organization}/{project}/{stack}/config
```

### Parameters

| Parameter      | Type   | In   | Description       |
|----------------|--------|------|-------------------|
| `organization` | string | path | organization name |
| `project`      | string | path | project name      |
| `stack`        | string | path | stack name        |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/config
```

### Default response

```plain
Status: 204 No Content
```
