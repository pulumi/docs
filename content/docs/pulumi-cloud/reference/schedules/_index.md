---
title: Schedules
title_tag: "Pulumi Cloud REST API: Schedules"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing scheduled operations on Pulumi stacks.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 17
---

Schedules allow you to automate recurring operations on your Pulumi stacks. The Schedules API provides endpoints for creating and managing drift detection, time-to-live (TTL), and custom scheduled operations.

## Schedule Operations

The API provides endpoints for the following categories of operations:

- Creating and managing drift detection schedules
- Creating and managing TTL (time-to-live) schedules
- Creating and managing custom deployment schedules
- Getting, listing, pausing, resuming, and deleting schedules
- Viewing schedule execution history

## Drift Detection Schedules

### Create Drift Schedule

Create a schedule for automatic drift detection with optional remediation.

```plain
POST /api/stacks/{organization}/{project}/{stack}/deployments/drift/schedules
```

#### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `project`           | string | path  | project name                                                                                                 |
| `stack`             | string | path  | stack name                                                                                                   |
| `scheduleCron`      | string | body  | cron expression for when to run drift detection                                                              |
| `autoRemediate`     | bool   | body  | true if detected drift should be remediated automatically                                                    |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"scheduleCron":"0 0 * * 0", "autoRemediate":true}' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/drift/schedules
```

### Update Drift Schedule

Update an existing drift detection schedule.

```plain
POST /api/stacks/{organization}/{project}/{stack}/deployments/drift/schedules/{scheduleID}
```

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `project`           | string | path  | project name                                                                                                 |
| `stack`             | string | path  | stack name                                                                                                   |
| `scheduleID`        | string | path  | schedule ID that you want to update                                                                          |
| `scheduleCron`      | string | body  | cron expression for when to run drift detection                                                              |
| `autoRemediate`     | bool   | body  | true if detected drift should be remediated automatically                                                    |

## TTL Schedules

### Create TTL Schedule

Create a schedule that automatically destroys resources at a specific time.

```plain
POST /api/stacks/{organization}/{project}/{stack}/deployments/ttl/schedules
```

#### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `project`           | string | path  | project name                                                                                                 |
| `stack`             | string | path  | stack name                                                                                                   |
| `timestamp`         | string | body  | ISO 8601 timestamp specifying when to destroy the stack. Example: `2024-04-20T00:00:00.000Z`                 |
| `deleteAfterDestroy`| bool   | body  | true if the stack should be deleted after resources are destroyed                                            |

#### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"timestamp":"2024-04-20T00:00:00.000Z","deleteAfterDestroy":true}' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/ttl/schedules
```

### Update TTL Schedule

Update an existing TTL schedule.

```plain
POST /api/stacks/{organization}/{project}/{stack}/deployments/ttl/schedules/{scheduleID}
```

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `project`           | string | path  | project name                                                                                                 |
| `stack`             | string | path  | stack name                                                                                                   |
| `scheduleID`        | string | path  | schedule ID that you want to update                                                                          |
| `timestamp`         | string | body  | ISO 8601 timestamp specifying when to destroy the stack. Example: `2024-04-20T00:00:00.000Z`                 |
| `deleteAfterDestroy`| bool   | body  | true if the stack should be deleted after resources are destroyed                                            |

## Custom Deployment Schedules

### Create Raw Deployment Schedule

Create a custom scheduled deployment.

```plain
POST /api/stacks/{organization}/{project}/{stack}/deployments/schedules
```

#### Parameters

| Parameter           | Type                                                                             | In    | Description                                                                                         |
|---------------------|----------------------------------------------------------------------------------|-------|-----------------------------------------------------------------------------------------------------|
| `organization`      | string                                                                           | path  | organization name                                                                                   |
| `project`           | string                                                                           | path  | project name                                                                                        |
| `stack`             | string                                                                           | path  | stack name                                                                                          |
| `scheduleCron`      | string                                                                           | body  | cron expression for when to run the pulumi operation                                                |
| `scheduleOnce`      | string                                                                           | body  | ISO 8601 timestamp specifying when to run the pulumi operation. Example: `2024-04-20T00:00:00.000Z` |
| `request`           | [CreateDeploymentRequest](/docs/pulumi-cloud/deployments/api/#create-deployment) | body  | The create deployment request object that will be executed on every invocation                      |

Note: Exactly one of `scheduleCron` and `scheduleOnce` must be set.

### Update Raw Deployment Schedule

Update a custom deployment schedule.

```plain
POST /api/stacks/{organization}/{project}/{stack}/deployments/schedules/{scheduleID}
```

#### Parameters

| Parameter           | Type                                                                             | In    | Description                                                                                         |
|---------------------|----------------------------------------------------------------------------------|-------|-----------------------------------------------------------------------------------------------------|
| `organization`      | string                                                                           | path  | organization name                                                                                   |
| `project`           | string                                                                           | path  | project name                                                                                        |
| `stack`             | string                                                                           | path  | stack name                                                                                          |
| `scheduleID`        | string                                                                           | path  | schedule ID that you want to update                                                                 |
| `scheduleCron`      | string                                                                           | body  | cron expression for when to run the pulumi operation                                                |
| `scheduleOnce`      | string                                                                           | body  | ISO 8601 timestamp specifying when to run the pulumi operation. Example: `2024-04-20T00:00:00.000Z` |
| `request`           | [CreateDeploymentRequest](/docs/pulumi-cloud/deployments/api/#create-deployment) | body  | The create deployment request object that will be executed on every invocation                      |

## Schedule Management

### Get Schedule

Get details of a specific schedule.

```plain
GET /api/stacks/{organization}/{project}/{stack}/deployments/schedules/{scheduleID}
```

### Delete Schedule

Delete a schedule.

```plain
DELETE /api/stacks/{organization}/{project}/{stack}/deployments/schedules/{scheduleID}
```

### Pause Schedule

Pause a schedule temporarily without deleting it.

```plain
POST /api/stacks/{organization}/{project}/{stack}/deployments/schedules/{scheduleID}/pause
```

### Resume Schedule

Resume a paused schedule.

```plain
POST /api/stacks/{organization}/{project}/{stack}/deployments/schedules/{scheduleID}/resume
```

### List Schedules of a Stack

List all schedules for a specific stack.

```plain
GET /api/stacks/{organization}/{project}/{stack}/deployments/schedules
```

### List Scheduled Deployment History

Get the execution history for a specific schedule.

```plain
GET /api/stacks/{organization}/{project}/{stack}/deployments/schedules/{scheduleID}/history
```
