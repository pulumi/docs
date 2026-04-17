---
title: Neo
title_tag: "Pulumi Cloud REST API: Neo"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for creating, managing, and retrieving agent tasks.
menu:
    reference:
        parent: cloud-rest-api
        weight: 4.5
aliases:
  - /docs/reference/cloud-rest-api/neo/
  - /docs/pulumi-cloud/reference/neo/
  - /docs/reference/cloud-rest-api/copilot/
  - /docs/ai/copilot/api/
  - /docs/pulumi-cloud/copilot/api/
  - /docs/pulumi-cloud/reference/copilot/
---

The Agent Tasks API allows you to create and manage AI agent tasks in Pulumi Cloud. These endpoints enable you to create tasks, monitor their status, respond to agent requests, and retrieve task events.

## Agent Task Operations

The API provides endpoints for the following operations:

- Creating new agent tasks
- Listing available tasks
- Getting task details and metadata
- Updating task settings and metadata
- Responding to agent requests
- Retrieving task events

---

## Create a New Task

Creates a new agent task for the specified organization.

```plain
POST /api/preview/agents/{orgName}/tasks
```

### Parameters

| Parameter | Type | In | Description |
|-----------|------|----|--------------|
| `orgName` | string | path | The organization name |

### Request Body

```json
{
  "message": {
    "type": "user_message",
    "content": "Help me optimize my Pulumi stack",
    "timestamp": "2025-01-15T10:30:00Z",
    "entity_diff": {
      "add": [
        {
          "type": "stack",
          "name": "my-stack",
          "project": "my-project"
        }
      ],
      "remove": []
    }
  },
  "approvalMode": "balanced",
  "planMode": true,
  "permissionMode": "default"
}
```

#### Request fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `message` | object | Yes | The user event message to start the task |
| `message.type` | string | Yes | Type of event (must be "user_message") |
| `message.content` | string | Yes | The exact natural language instruction from the user |
| `message.timestamp` | string (ISO 8601) | Yes | When the event occurred |
| `message.entity_diff` | object | No | Entities to add or remove from the agent. See [Entity Types](#entity-types) for details. Note: Pull request entities cannot be added via this API. |
| `approvalMode` | string | No | Approval mode override for this task. If omitted, the organization default is used. See [approval modes](#approval-modes) for valid values. |
| `planMode` | boolean | No | Whether to enable plan mode for this task. In plan mode, the agent performs detailed research before execution and allows user iteration on the plan. |
| `permissionMode` | string | No | Controls the permission scope for the task. Valid values: `default` (the agent uses the creating user's full permissions), `read-only`. Defaults to `default` if omitted. |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"message":{"type":"user_message","content":"Help me optimize my Pulumi stack","timestamp":"2025-01-15T10:30:00Z"},"approvalMode":"balanced","planMode":true}' \
  https://api.pulumi.com/api/preview/agents/my-org/tasks
```

### Response

```plain
Status: 201 Created
```

```json
{
  "taskId": "task_abc123"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `taskId` | string | Unique identifier for the created task |

### Error Responses

- `400 Bad Request`: Missing required fields or invalid request body
- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: Insufficient permissions to create tasks in this organization

---

## Get Task Metadata

Retrieves metadata for a specific task.

```plain
GET /api/preview/agents/{orgName}/tasks/{taskID}
```

### Parameters

| Parameter | Type | In | Description |
|-----------|------|----|--------------|
| `orgName` | string | path | The organization name |
| `taskID` | string | path | The task identifier |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/preview/agents/my-org/tasks/task_abc123
```

### Response

```plain
Status: 200 OK
```

```json
{
  "id": "task_abc123",
  "name": "Task name",
  "status": "running",
  "createdAt": "2025-01-15T00:00:00Z",
  "approvalMode": "balanced",
  "entities": [
    {
      "type": "stack",
      "name": "my-stack",
      "project": "my-project"
    }
  ],
  "planMode": true,
  "isShared": false,
  "createdBy": {
    "name": "Jane Doe",
    "githubLogin": "janedoe",
    "avatarUrl": "https://api.pulumi.com/static/avatars/J-E91E63.png"
  },
  "permissionMode": "default",
  "runtimePhase": "ready",
  "contextUsedTokens": 43272,
  "contextWindowTokens": 1000000
}
```

#### Response fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the task |
| `name` | string | Human-readable name for the task |
| `status` | string | Current status of the task (`running` or `idle`) |
| `createdAt` | string (ISO 8601) | When the task was created |
| `approvalMode` | string | Approval mode for this task. See [approval modes](#approval-modes) for values. |
| `entities` | array | List of entities associated with the task |
| `planMode` | boolean | Whether the task is in plan mode |
| `isShared` | boolean | Whether this task is shared with other organization members |
| `sharedAt` | string (ISO 8601) | When the task was first shared (null if never shared) |
| `createdBy` | object | Information about the user who created this task |
| `permissionMode` | string | The permission scope for the task (`default` or `read-only`) |
| `runtimePhase` | string | The current runtime phase (`booting`, `ready`, or `running`). Null until the runtime checks in. |
| `contextUsedTokens` | integer | Total input tokens consumed across all model invocations for this task |
| `contextWindowTokens` | integer | Maximum context window size in tokens for the primary model used by this task |

### Error Responses

- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: Insufficient permissions to view this task
- `404 Not Found`: Task not found

---

## List Tasks

Lists all tasks for the specified organization.

```plain
GET /api/preview/agents/{orgName}/tasks
```

### Parameters

| Parameter | Type | In | Description |
|-----------|------|----|--------------|
| `orgName` | string | path | The organization name |
| `continuationToken` | string | query | Optional. Token to fetch the next page of results |
| `pageSize` | integer | query | Optional. Number of items per page (1-1000, default: 100) |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/preview/agents/my-org/tasks?pageSize=50
```

### Response

```plain
Status: 200 OK
```

```json
{
  "tasks": [
    {
      "id": "task_abc123",
      "name": "Task name",
      "status": "running",
      "createdAt": "2025-01-15T00:00:00Z",
      "approvalMode": "balanced",
      "entities": [],
      "planMode": true,
      "isShared": false,
      "createdBy": {
        "name": "Jane Doe",
        "githubLogin": "janedoe",
        "avatarUrl": "https://api.pulumi.com/static/avatars/J-E91E63.png"
      },
      "permissionMode": "default",
      "runtimePhase": "ready"
    }
  ],
  "continuationToken": "next_page_token"
}
```

#### Response fields

| Field | Type | Description |
|-------|------|-------------|
| `tasks` | array | List of tasks for this page. Each task object has the same fields as the [Get Task Metadata](#get-task-metadata) response. |
| `continuationToken` | string | Token to fetch the next page (null if no more results) |

### Error Responses

- `400 Bad Request`: Invalid pageSize parameter
- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: Insufficient permissions to list tasks in this organization

---

## Update a task

Updates the settings or metadata of an existing task. Only the user who created the task can modify it.

```plain
PATCH /api/preview/agents/{orgName}/tasks/{taskID}
```

### Parameters

| Parameter | Type | In | Description |
|-----------|------|----|--------------|
| `orgName` | string | path | The organization name |
| `taskID` | string | path | The task identifier |

### Request body

All fields are optional. Omitted fields are left unchanged.

```json
{
  "name": "New task name",
  "isShared": true,
  "approvalMode": "auto",
  "permissionMode": "read-only"
}
```

#### Request fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | No | A new display name for the task. Must be between 1 and 255 characters after trimming whitespace. |
| `isShared` | boolean | No | Whether to share the task with other organization members. |
| `approvalMode` | string | No | Approval mode for this task. See [approval modes](#approval-modes) for valid values. |
| `permissionMode` | string | No | The permission scope for the task. Valid values: `default`, `read-only`. |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  --data '{"approvalMode":"auto","isShared":true}' \
  https://api.pulumi.com/api/preview/agents/my-org/tasks/task_abc123
```

### Response

```plain
Status: 200 OK
```

Returns the updated task object with the same fields as the [Get Task Metadata](#get-task-metadata) response.

```json
{
  "id": "task_abc123",
  "name": "New task name",
  "status": "running",
  "createdAt": "2025-01-15T00:00:00Z",
  "approvalMode": "auto",
  "entities": [],
  "planMode": false,
  "isShared": true,
  "sharedAt": "2025-01-15T10:40:00Z",
  "createdBy": {
    "name": "Jane Doe",
    "githubLogin": "janedoe",
    "avatarUrl": "https://api.pulumi.com/static/avatars/J-E91E63.png"
  },
  "permissionMode": "read-only",
  "runtimePhase": "ready",
  "contextUsedTokens": 43272,
  "contextWindowTokens": 1000000
}
```

### Error responses

- `403 Forbidden`: Feature not enabled for organization
- `404 Not Found`: Task not found or not owned by user

---

## Respond to an Existing Task

Allows users to respond to an ongoing agent task with additional input or instructions.

```plain
POST /api/preview/agents/{orgName}/tasks/{taskID}
```

### Parameters

| Parameter | Type | In | Description |
|-----------|------|----|--------------|
| `orgName` | string | path | The organization name |
| `taskID` | string | path | The task identifier |

### Request Body

The request body contains an `event` object with different subtypes based on the type of response. See the [User Event Types](#user-event-types) section for detailed information about each event type.

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"event":{"type":"user_message","content":"Yes, please proceed with the optimization","timestamp":"2025-01-15T10:35:00Z"}}' \
  https://api.pulumi.com/api/preview/agents/my-org/tasks/task_abc123
```

### Response

```plain
Status: 202 Accepted
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

```plain
GET /api/preview/agents/{orgName}/tasks/{taskID}/events
```

### Parameters

| Parameter | Type | In | Description |
|-----------|------|----|--------------|
| `orgName` | string | path | The organization name |
| `taskID` | string | path | The task identifier |
| `continuationToken` | string | query | Optional. Token to fetch the next page of results |
| `pageSize` | integer | query | Optional. Number of items per page (1-1000, default: 100) |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/preview/agents/my-org/tasks/task_abc123/events?pageSize=50
```

### Response

```plain
Status: 200 OK
```

```json
{
  "events": [
    {
      "id": "event_123",
      "type": "agentResponse",
      "eventBody": {
        "content": "I'll help you optimize your Pulumi stack. Let me analyze the current configuration...",
        "timestamp": "2025-01-15T10:30:00Z"
      }
    },
    {
      "id": "event_124",
      "type": "userInput",
      "eventBody": {
        "content": "Continue with optimization",
        "timestamp": "2025-01-15T10:35:00Z"
      }
    }
  ],
  "continuationToken": "next_page_token"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `events` | array | List of events for this page |
| `events[].id` | string | Unique identifier for the event |
| `events[].type` | string | Type of event ("agentResponse" or "userInput") |
| `events[].eventBody` | object | The event content and metadata |
| `continuationToken` | string | Token to fetch the next page (null if no more results) |

### Error Responses

- `400 Bad Request`: Invalid pageSize parameter
- `401 Unauthorized`: Invalid or missing authentication token
- `403 Forbidden`: Insufficient permissions to view events for this task
- `404 Not Found`: Task not found

---

## User Event Types

When responding to agent tasks, you can send different types of user events. Each event type has specific fields and use cases.

### User Message Event

Send a user message event to provide additional instructions or responses to the agent.

```json
{
  "event": {
    "type": "user_message",
    "content": "Yes, please proceed with the optimization",
    "timestamp": "2025-01-15T10:35:00Z",
    "entity_diff": {
      "add": [
        {
          "type": "stack",
          "name": "my-stack",
          "project": "my-project"
        }
      ],
      "remove": []
    }
  }
}
```

#### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be "user_message" |
| `content` | string | Yes | The user's response or additional instructions |
| `timestamp` | string (ISO 8601) | Yes | When the event occurred |
| `entity_diff` | object | No | Entities to add or remove from the agent context. See [Entity Types](#entity-types) for details. Note: Pull request entities cannot be added via this API. |

### User Confirmation Event

Send a user confirmation event to respond to an agent's approval request.

```json
{
  "event": {
    "type": "user_confirmation",
    "approval_request_id": "req_123",
    "timestamp": "2025-01-15T10:35:00Z"
  }
}
```

#### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be "user_confirmation" |
| `approval_request_id` | string | Yes | ID to correlate the question the user is responding to |
| `timestamp` | string (ISO 8601) | Yes | When the event occurred |

### User Cancel Event

Send a user cancel event to cancel the current agent task.

```json
{
  "event": {
    "type": "user_cancel",
    "timestamp": "2025-01-15T10:35:00Z"
  }
}
```

#### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be "user_cancel" |
| `timestamp` | string (ISO 8601) | Yes | When the event occurred |

---

## Entity Types

Entities represent resources that the agent can work with. Different entity types provide different capabilities and context to the agent.

### Stack Entity

Represents a Pulumi stack that the agent can analyze and modify.

```json
{
  "type": "stack",
  "name": "my-stack",
  "project": "my-project"
}
```

#### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be "stack" |
| `name` | string | Yes | The name of the Pulumi stack |
| `project` | string | Yes | The project name containing the stack |

### Repository Entity

Represents a source code repository that the agent can analyze and work with.

```json
{
  "type": "repository",
  "name": "my-repo",
  "org": "my-org",
  "forge": "github"
}
```

#### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be "repository" |
| `name` | string | Yes | The name of the repository |
| `org` | string | Yes | The organization owning the repository |
| `forge` | string | Yes | The forge/provider where the repository is hosted (e.g., "github") |

### Pull Request Entity

Represents a pull request that the agent can analyze and work with.

**Note**: Pull request entities cannot be added using the create task or respond to task APIs. They are managed by the system and associated with tasks through other mechanisms.

```json
{
  "type": "pull_request",
  "number": 123,
  "repository": {
    "name": "my-repo",
    "org": "my-org",
    "forge": "github"
  },
  "merged": true
}
```

#### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be "pull_request" |
| `number` | integer | Yes | The pull request number |
| `merged` | boolean | Yes | If the PR has been merged already |
| `repository` | object | Yes | The repository information |
| `repository.name` | string | Yes | The name of the repository |
| `repository.org` | string | Yes | The organization owning the repository |
| `repository.forge` | string | Yes | The forge/provider where the repository is hosted |

### Policy Issue Entity

Represents a policy issue that the agent can analyze and help resolve.

```json
{
  "type": "policy_issue",
  "id": "issue_123"
}
```

#### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be "policy_issue" |
| `id` | string | Yes | The unique identifier for the policy issue |

---

## Approval modes

Approval modes control how much autonomy the agent has during task execution.

| Value | Description |
|-------|-------------|
| `manual` | The agent requests approval before running `pulumi preview`, running `pulumi up`, and opening a pull request. This is the most conservative mode. |
| `balanced` | The agent requests approval only before running `pulumi up`. Previews and pull requests proceed without approval. |
| `auto` | The agent does not request any approvals and executes the entire task autonomously. |

For more details, see [task modes](/docs/ai/tasks/#task-modes).

---

## Preview Status

These endpoints are currently in preview status (`/api/preview/agents/...`). The API may change before general availability. Please check the documentation regularly for updates.
