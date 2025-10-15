---
title: Neo
title_tag: "Pulumi Cloud REST API: Neo"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for initiating and fetch tasks.
menu:
    reference:
        parent: cloud-rest-api
        weight: 4.5
aliases:
  - /docs/reference/cloud-rest-api/neo/
  - /docs/pulumi-cloud/reference/neo/
---

The Agent Tasks API allows you to create and manage AI agent tasks in Pulumi Cloud. These endpoints enable you to create tasks, monitor their status, respond to agent requests, and retrieve task events.

## Authentication

All requests must be authenticated using a token via the `Authorization` HTTP header:

```plain
Authorization: token {token}
```

## Base URL

For Managed Pulumi Cloud (app.pulumi.com):

```plain
https://api.pulumi.com
```

For Self-Hosted Pulumi Cloud, use your configured API endpoint.

---

## Create a New Task

Creates a new agent task for the specified organization.

### Endpoint

```plain
POST /preview/agents/{orgName}/tasks
```

### Parameters

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `orgName` | string | Yes | The organization name |

### Request Body

```json
{
  "content": "string",
  "entity_diff": {
    "add": [
      {
        "type": "string",
        "id": "string"
      }
    ],
    "remove": [
      {
        "type": "string",
        "id": "string"
      }
    ]
  },
  "timestamp": "2025-01-15T00:00:00Z"
}
```

#### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `content` | string | Yes | The exact natural language instruction from the user |
| `entity_diff` | object | No | Entities to add or remove from the agent |
| `timestamp` | string (ISO 8601) | Yes | When the event occurred |

### Response

```json
{
  "id": "task_abc123",
  "name": "Task name",
  "status": "pending",
  "createdAt": "2025-01-15T00:00:00Z",
  "entities": []
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the task |
| `name` | string | Human-readable name for the task |
| `status` | string | Current status of the task (pending, running, completed, failed) |
| `createdAt` | string (ISO 8601) | When the task was created |
| `entities` | array | List of entities associated with the task |

### Example Request

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/preview/agents/my-org/tasks \
  -d '{
    "content": "Help me optimize my Pulumi stack",
    "timestamp": "2025-01-15T10:30:00Z"
  }'
```

### Error Responses

- `400 Bad Request`: Missing required fields or invalid request body
- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: Insufficient permissions to create tasks in this organization

---

## Get Task Metadata

Retrieves metadata for a specific task.

### Endpoint

```
GET /preview/agents/{orgName}/tasks/{taskID}
```

### Parameters

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `orgName` | string | Yes | The organization name |
| `taskID` | string | Yes | The task identifier |

### Response

```json
{
  "id": "task_abc123",
  "name": "Task name",
  "status": "running",
  "createdAt": "2025-01-15T00:00:00Z",
  "entities": [
    {
      "type": "stack",
      "id": "my-stack"
    }
  ]
}
```

### Example Request

```bash
curl -X GET \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/preview/agents/my-org/tasks/task_abc123
```

### Error Responses

- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: Insufficient permissions to view this task
- `404 Not Found`: Task not found

---

## List Tasks

Lists all tasks for the specified organization.

### Endpoint

```
GET /preview/agents/{orgName}/tasks
```

### Parameters

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `orgName` | string | Yes | The organization name |

#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `continuationToken` | string | No | Token to fetch the next page of results |
| `pageSize` | integer | No | Number of items per page (1-1000, default: 100) |

### Response

```json
{
  "tasks": [
    {
      "id": "task_abc123",
      "name": "Task name",
      "status": "completed",
      "createdAt": "2025-01-15T00:00:00Z",
      "entities": []
    }
  ],
  "continuationToken": "next_page_token"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `tasks` | array | List of tasks for this page |
| `continuationToken` | string | Token to fetch the next page (null if no more results) |

### Example Request

```bash
curl -X GET \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  "https://api.pulumi.com/preview/agents/my-org/tasks?pageSize=50"
```

### Error Responses

- `400 Bad Request`: Invalid pageSize parameter
- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: Insufficient permissions to list tasks in this organization

---

## Respond to an Existing Task

Allows users to respond to an ongoing agent task with additional input or instructions.

### Endpoint

```
POST /preview/agents/{orgName}/tasks/{taskID}
```

### Parameters

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `orgName` | string | Yes | The organization name |
| `taskID` | string | Yes | The task identifier |

### Request Body

```json
{
  "event": {
    "type": "user_input",
    "content": "string",
    "timestamp": "2025-01-15T00:00:00Z"
  }
}
```

#### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `event` | object | Yes | The user event to append to the task |
| `event.type` | string | Yes | Type of event (e.g., "user_input") |
| `event.content` | string | Yes | The user's response or additional instructions |
| `event.timestamp` | string (ISO 8601) | Yes | When the event occurred |

### Response

Returns `202 Accepted` with no body on success.

### Example Request

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/preview/agents/my-org/tasks/task_abc123 \
  -d '{
    "event": {
      "type": "user_input",
      "content": "Yes, please proceed with the optimization",
      "timestamp": "2025-01-15T10:35:00Z"
    }
  }'
```

### Error Responses

- `400 Bad Request`: Missing event field or invalid entities mentioned
- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: Insufficient permissions to respond to this task
- `404 Not Found`: Task not found
- `409 Conflict`: Cannot respond while a request is still ongoing

---

## List Events from a Task

Retrieves the event stream for a specific task.

### Endpoint

```
GET /preview/agents/{orgName}/tasks/{taskID}/events
```

### Parameters

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `orgName` | string | Yes | The organization name |
| `taskID` | string | Yes | The task identifier |

#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `continuationToken` | string | No | Token to fetch the next page of results |
| `pageSize` | integer | No | Number of items per page (1-1000, default: 100) |

### Response

```json
{
  "events": [
    {
      "type": "console_output",
      "timestamp": "2025-01-15T10:30:00Z",
      "content": "Processing request...",
      "sequence": 1
    },
    {
      "type": "user_input",
      "timestamp": "2025-01-15T10:35:00Z",
      "content": "Continue with optimization",
      "sequence": 2
    }
  ],
  "continuationToken": "next_page_token"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `events` | array | List of console events for this page |
| `events[].type` | string | Type of event (console_output, user_input, etc.) |
| `events[].timestamp` | string (ISO 8601) | When the event occurred |
| `events[].content` | string | The event content |
| `events[].sequence` | integer | Sequence number for ordering events |
| `continuationToken` | string | Token to fetch the next page (null if no more results) |

### Example Request

```bash
curl -X GET \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  "https://api.pulumi.com/preview/agents/my-org/tasks/task_abc123/events?pageSize=50"
```

### Error Responses

- `400 Bad Request`: Invalid pageSize parameter
- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: Insufficient permissions to view events for this task
- `404 Not Found`: Task not found

---

## Authorization

The Agent Tasks API uses the following authorization requirements:

- **Read Operations** (GET endpoints): Require `AgentsReadAuth` permission
- **Write Operations** (POST endpoints): Require `AgentsReadWriteAuth` permission

Users must have the appropriate permissions for the specified organization to access these endpoints.

## Rate Limiting

API requests are subject to rate limiting. If you exceed the rate limit, you'll receive a `429 Too Many Requests` response. Please implement exponential backoff and retry logic in your applications.

## Preview Status

These endpoints are currently in preview status (`/preview/agents/...`). The API may change before general availability. Please check the documentation regularly for updates.
