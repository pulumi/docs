---
title: Webhooks
title_tag: "Pulumi Cloud REST API: Webhooks"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for creating and managing webhooks for organizations and stacks.
menu:
    reference:
        parent: cloud-rest-api
        weight: 30
aliases:
  - /docs/reference/cloud-rest-api/webhooks/
  - /docs/pulumi-cloud/reference/webhooks/
---

The Webhooks API allows you to create and manage webhooks for organizations and stacks. Webhooks notify external services of events happening within your Pulumi organization, such as stack updates, deployments, or policy violations.

For comprehensive information about webhooks including event filtering, payload formats, and UI setup, see the [Webhooks documentation](/docs/deployments/webhooks/).

## Webhook Operations

The API provides endpoints for the following operations:

- Creating new webhooks for organizations or stacks
- Listing webhooks with filtering options
- Getting webhook details
- Updating webhook configuration
- Testing webhooks with ping functionality
- Viewing webhook delivery history
- Deleting webhooks

## Create Webhook

Create a new webhook for an organization or stack.

```plain
// To create an organization webhook
POST /api/orgs/{organization}/hooks

// To create a stack webhook
POST /api/stacks/{organization}/{project}/{stack}/hooks
```

### Parameters

| Parameter          | Type          | In   | Description                                                                                                                                                                     |
|--------------------|---------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `organization`     | string        | path | Organization name                                                                                                                                                               |
| `project`          | string        | path | **Optional.** Project name (required for stack webhooks)                                                                                                                        |
| `stack`            | string        | path | **Optional.** Stack name (required for stack webhooks)                                                                                                                          |
| `active`           | boolean       | body | Enable webhook                                                                                                                                                                  |
| `displayName`      | string        | body | Name of webhook                                                                                                                                                                 |
| `organizationName` | string        | body | Organization name                                                                                                                                                               |
| `payloadUrl`       | string        | body | URL to send request to                                                                                                                                                          |
| `projectName`      | string        | body | **Optional.** Project name (required for stack webhooks)                                                                                                                        |
| `stackName`        | string        | body | **Optional.** Stack name (required for stack webhooks)                                                                                                                          |
| `format`           | string        | body | **Optional.** Format of the payload. Possible values are `raw`, `slack`, `ms_teams` or `pulumi_deployments`. Default is `raw`.                                                  |
| `filters`          | array[string] | body | **Optional.** List of filters for events the webhook should receive. See [webhook docs](/docs/deployments/webhooks#event-filtering) for more information on what filters are available |
| `secret`           | string        | body | **Optional.** Secret used as the HMAC key. See [webhook docs](/docs/deployments/webhooks#headers) for more information                                                         |

### Example

```bash
# Create organization webhook
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"active": true, "displayName": "My Webhook", "organizationName": "myorg", "payloadUrl": "https://example.com/webhook"}' \
  https://api.pulumi.com/api/orgs/{organization}/hooks

# Create stack webhook
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"active": true, "displayName": "Stack Webhook", "organizationName": "myorg", "projectName": "myproject", "stackName": "production", "payloadUrl": "https://example.com/webhook"}' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/hooks
```

## List Webhooks

List all webhooks for an organization or stack.

```plain
// List organization webhooks
GET /api/orgs/{organization}/hooks

// List stack webhooks
GET /api/stacks/{organization}/{project}/{stack}/hooks
```

### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | Organization name                                                                                            |
| `project`           | string | path  | **Optional.** Project name (required for stack webhooks)                                                     |
| `stack`             | string | path  | **Optional.** Stack name (required for stack webhooks)                                                       |
| `continuationToken` | string | query | **Optional.** The continuation token to use for retrieving the next set of results if results were truncated |

### Example

```bash
# List organization webhooks
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/hooks

# List stack webhooks
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/hooks
```

## Get Webhook

Get details about a specific webhook.

```plain
// Get organization webhook
GET /api/orgs/{organization}/hooks/{webhookname}

// Get stack webhook
GET /api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}
```

### Parameters

| Parameter      | Type   | In   | Description                                               |
|----------------|--------|------|-----------------------------------------------------------|
| `organization` | string | path | Organization name                                         |
| `project`      | string | path | **Optional.** Project name (required for stack webhooks) |
| `stack`        | string | path | **Optional.** Stack name (required for stack webhooks)   |
| `webhookname`  | string | path | Name of the webhook                                       |

### Example

```bash
# Get organization webhook
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/hooks/{webhookname}

# Get stack webhook
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}
```

## Update Webhook

Update an existing webhook.

```plain
// Update organization webhook
PATCH /api/orgs/{organization}/hooks/{webhookname}

// Update stack webhook
PATCH /api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}
```

### Parameters

The update endpoint accepts the same body parameters as the create endpoint. Only include the fields you want to update.

### Example

```bash
# Update organization webhook
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  --data '{"active": false, "displayName": "Updated Webhook Name"}' \
  https://api.pulumi.com/api/orgs/{organization}/hooks/{webhookname}
```

## Delete Webhook

Delete a webhook.

```plain
// Delete organization webhook
DELETE /api/orgs/{organization}/hooks/{webhookname}

// Delete stack webhook
DELETE /api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}
```

### Parameters

| Parameter      | Type   | In   | Description                                               |
|----------------|--------|------|-----------------------------------------------------------|
| `organization` | string | path | Organization name                                         |
| `project`      | string | path | **Optional.** Project name (required for stack webhooks) |
| `stack`        | string | path | **Optional.** Stack name (required for stack webhooks)   |
| `webhookname`  | string | path | Name of the webhook                                       |

### Example

```bash
# Delete organization webhook
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{organization}/hooks/{webhookname}

# Delete stack webhook
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}
```

## Ping Webhook

Send a test ping to a webhook to validate it's working.

```plain
// Ping organization webhook
POST /api/orgs/{organization}/hooks/{webhookname}/ping

// Ping stack webhook
POST /api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}/ping
```

### Parameters

| Parameter      | Type   | In   | Description                                               |
|----------------|--------|------|-----------------------------------------------------------|
| `organization` | string | path | Organization name                                         |
| `project`      | string | path | **Optional.** Project name (required for stack webhooks) |
| `stack`        | string | path | **Optional.** Stack name (required for stack webhooks)   |
| `webhookname`  | string | path | Name of the webhook                                       |

### Example

```bash
# Ping organization webhook
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  https://api.pulumi.com/api/orgs/{organization}/hooks/{webhookname}/ping

# Ping stack webhook
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}/ping
```

## List Webhook Deliveries

List the delivery history for a webhook, showing details about each webhook invocation including payload, response, and timing information.

```plain
// List organization webhook deliveries
GET /api/orgs/{organization}/hooks/{webhookname}/deliveries

// List stack webhook deliveries
GET /api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}/deliveries
```

### Parameters

| Parameter      | Type   | In   | Description                                            |
|----------------|--------|------|--------------------------------------------------------|
| `organization` | string | path | organization name                                      |
| `project`      | string | path | project name (only for stack webhooks)                 |
| `stack`        | string | path | stack name (only for stack webhooks)                   |
| `webhookname`  | string | path | webhook name                                           |

### Example

```bash
# List organization webhook deliveries
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/hooks/{webhookname}/deliveries

# List stack webhook deliveries
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/hooks/{webhookname}/deliveries
```

### Default response

```plain
Status: 200 OK
```

```plain
[
  {
    "id": "ea01abd2-90b4-4670-acce-15cc019ed6e4",
    "kind": "ping",
    "payload": "{\"timestamp\":1632735487,\"message\":\"🍹 Just a friendly ping from Pulumi 🍹\"}",
    "timestamp": 1632735487,
    "duration": 196,
    "requestUrl": "{webhookurl}",
    "requestHeaders": "Content-Type: application/json\r\nPulumi-Webhook-Id: ea01abd2-90b4-4670-acce-15cc019ed6e4\r\nPulumi-Webhook-Kind: ping\r\n",
    "responseCode": 200,
    "responseHeaders": "{headersfromwebhook}",
    "responseBody": "OK"
  }
]
```
