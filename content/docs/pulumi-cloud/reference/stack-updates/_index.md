---
title: Stack Updates
title_tag: "Pulumi Cloud REST API: Stack Updates"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing and monitoring stack update operations.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 22
---

Stack updates are operations that create, update, or delete resources in a Pulumi stack. The Stack Updates API allows you to list updates, check status, and view detailed events for each operation.

## Update Operations

The API provides endpoints for the following operations:

- Listing stack updates with optional pagination
- Getting the status of a specific update
- Viewing detailed events for an update
- Listing preview operations

## List Stack Updates

```plain
GET /api/stacks/{organization}/{project}/{stack}/updates
```

By default the results are not paginated. You can specify `page` and `pageSize` query parameters to paginate the results.

> `?pageSize=1&page=1` can be used to return only the most recent update.

### Parameters

| Parameter      | Type   | In    | Description                                                                                    |
|----------------|--------|-------|------------------------------------------------------------------------------------------------|
| `organization` | string | path  | organization name                                                                              |
| `project`      | string | path  | project name                                                                                   |
| `stack`        | string | path  | stack name                                                                                     |
| `page`         | number | query | **Optional.** page of the results to return                                                    |
| `pageSize`     | number | query | **Optional.** number of results per page                                                       |
| `output-type`  | number | query | **Optional.** the response format to return - possible values are `service` or `cli` (default) |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/updates?output-type=service
```

### Default response (output type = cli)

```plain
Status: 200 OK
```

```plain
{
  "updates": [
    {
      "kind": "update",
      "startTime": 1733780162,
      "message": "",
      "environment": {},
      "config": {
        "aws:region": {
          "string": "us-east-1",
          "secret": false,
          "object": false
        },
        "pulumi:template": {
          "string": "aws-typescript",
          "secret": false,
          "object": false
        }
      },
      "result": "succeeded",
      "endTime": 1733780162,
      "version": 1,
      "resourceChanges": {
        "create": 1,
        "delete": 0,
        "same": 0,
        "update": 0
      },
      "resourceCount": 1
    }
  ]
}
```

## Get Update Status

```plain
GET /api/stacks/{organization}/{project}/{stack}/update/{updateID}
```

### Parameters

| Parameter      | Type   | In   | Description                                                                                               |
|----------------|--------|------|-----------------------------------------------------------------------------------------------------------|
| `organization` | string | path | organization name                                                                                         |
| `project`      | string | path | project name                                                                                              |
| `stack`        | string | path | stack name                                                                                                |
| `updateID`     | uuid   | path | update id - UUID as retrieved from [List Stack Updates](#list-stack-updates) using `?output-type=service` |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/update/{updateID}
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "status": "succeeded",
  "events": []
}
```

## List Update Events

```plain
GET /api/stacks/{organization}/{project}/{stack}/update/{updateID}/events
```

### Parameters

| Parameter      | Type   | In   | Description                                                                                               |
|----------------|--------|------|-----------------------------------------------------------------------------------------------------------|
| `organization` | string | path | organization name                                                                                         |
| `project`      | string | path | project name                                                                                              |
| `stack`        | string | path | stack name                                                                                                |
| `updateID`     | uuid   | path | update id - UUID as retrieved from [List Stack Updates](#list-stack-updates) using `?output-type=service` |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/update/{updateID}/events
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "events": [
    {
      "timestamp": 1615872590,
      "type": "preludeEvent",
      "preludeEvent": {
        "config": {
          "aws:region": "us-west-2"
        }
      }
    },
    {
      "timestamp": 1615872590,
      "type": "resourcePreEvent",
      "resourcePreEvent": {
        "metadata": {
          "op": "create",
          "urn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:pulumi:Stack::demo-aws-ts-webserver-dev-user1",
          "type": "pulumi:pulumi:Stack",
          "old": null,
          "new": {
            "type": "pulumi:pulumi:Stack",
            "urn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:pulumi:Stack::demo-aws-ts-webserver-dev-user1",
            "id": "",
            "parent": "",
            "inputs": {},
            "outputs": {},
            "provider": ""
          },
          "logical": true,
          "provider": ""
        }
      }
    },
    {
      "timestamp": 1615872593,
      "type": "summaryEvent",
      "summaryEvent": {
        "maybeCorrupt": false,
        "durationSeconds": 4,
        "resourceChanges": {
          "create": 2
        },
        "PolicyPacks": {
          "aws": "23",
          "azure": "12",
          "azure-nextgen": "3",
          "cost-optimization": "9",
          "gcp": "19",
          "k8s": "13"
        }
      }
    }
  ],
  "continuationToken": null
}
```

## List Previews

List all previews since the last update operation.

```plain
GET /api/stacks/{organization}/{project}/{stack}/updates/latest/previews
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
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/updates/latest/previews
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "updates": [
    {
      "info": {
        "kind": "Pupdate",
        "startTime": 1624932955,
        "message": "triggered by pr #12",
        "environment": {
          "exec.kind": "cli",
          "git.author": "First Last",
          "git.author.email": "user1@example.com",
          "git.committer": "GitHub",
          "git.committer.email": "noreply@github.com",
          "git.dirty": "true",
          "git.head": "35caae8d73c3ecb0eac1256ba0e03775f24514da",
          "git.headName": "refs/heads/master",
          "vcs.kind": "github.com",
          "vcs.owner": "pulumi",
          "vcs.repo": "examples"
        },
        "config": {
          "aws:region": {
            "string": "us-west-2",
            "secret": false,
            "object": false
          }
        },
        "result": "failed",
        "endTime": 1624932956,
        "version": 1,
        "resourceChanges": {
          "create": 0,
          "delete": 0,
          "same": 0,
          "update": 0
        }
      },
      "updateID": "c30c74e6-9576-4c63-95a4-4f96e7793ebb",
      "version": 1,
      "latestVersion": 0
    }
  ],
  "itemsPerPage": 10,
  "total": 4
}
```
