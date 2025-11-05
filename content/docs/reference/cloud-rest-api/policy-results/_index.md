---
title: Policy Results
title_tag: "Pulumi Cloud REST API: Policy Results"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for retrieving and analyzing policy evaluation results.
menu:
    reference:
        parent: cloud-rest-api
        weight: 13
aliases:
  - /docs/reference/cloud-rest-api/policy-results/
  - /docs/pulumi-cloud/reference/policy-results/
---

Policy Results is a part of Pulumi Insights that provides information about policy issues detected during stack updates and resource scanning. The Policy Results API allows you to retrieve information about policy issues across your organization, enabling governance and compliance monitoring through the Pulumi Insights platform.

## Policy Results Operations

The API provides endpoints for the following operations:

- Listing policy issues across an organization
- Listing policy issues with filtering and pagination
- Getting details of a specific policy issue
- Updating policy issue status, priority, and assignment

## List Policy Issues

Retrieve policy issues for an organization with support for filtering, pagination, and sorting.

```plain
POST /api/orgs/{organization}/policyresults/issues
```

### Parameters

| Parameter      | Type   | In   | Description                                                         |
| -------------- | ------ | ---- | ------------------------------------------------------------------- |
| `organization` | string | path | organization name                                                   |
| `startRow`     | number | body | Starting row index for pagination                                   |
| `endRow`       | number | body | Ending row index for pagination                                     |
| `filterModel`  | object | body | Filter criteria (see filter examples below)                         |
| `sortModel`    | array  | body | Sort configuration (array of `{colId: string, sort: "asc"/"desc"}`) |
| `rowGroupCols` | array  | body | Column grouping configuration                                       |
| `groupKeys`    | array  | body | Keys for grouped rows                                               |

#### Filter Examples

Filter by status (open or in_progress):

```json
{
    "filterType": "join",
    "type": "OR",
    "conditions": [
        {
            "filterType": "text",
            "colId": "status",
            "type": "equals",
            "filter": "open"
        },
        {
            "filterType": "text",
            "colId": "status",
            "type": "equals",
            "filter": "in_progress"
        }
    ]
}
```

### Example

```bash
curl -X POST \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -d '{
    "startRow": 0,
    "endRow": 50,
    "filterModel": {
      "type": "OR",
      "conditions": [
        {"filterType": "text", "colId": "status", "type": "equals", "filter": "open"},
        {"filterType": "text", "colId": "status", "type": "equals", "filter": "in_progress"}
      ]
    },
    "sortModel": []
  }' \
  https://api.pulumi.com/api/orgs/{organization}/policyresults/issues
```

### Default response

```plain
Status: 200 OK
```

```json
{
    "rowCount": 15709,
    "groupData": null,
    "policyIssues": [
        {
            "id": "e4584e2c-f15d-4966-88a3-b16693c41441",
            "entityType": "insights-account",
            "entityProject": "dev-sandbox",
            "entityId": "us-west-2",
            "resourceVersion": 11,
            "policyPack": "aws-hitrust",
            "policyPackTag": "0.0.2",
            "policyName": "ecs-task-definition-must-have-tags",
            "resourceURN": "urn:insights:dev-sandbox/us-west-2::aws::aws:ecs/taskDefinition:TaskDefinition::arn:aws:ecs:us-west-2:416178951233:task-definition/service-4e39feb5:1",
            "resourceProvider": "aws",
            "resourceType": "aws:ecs/taskDefinition:TaskDefinition",
            "resourceName": "arn:aws:ecs:us-west-2:416178951233:task-definition/service-4e39feb5:1",
            "observedAt": "2025-09-24T00:49:14.928Z",
            "lastModified": "2025-09-24T00:49:14.928Z",
            "level": "advisory",
            "severity": "critical",
            "status": "open",
            "kind": "audit",
            "priority": "p4",
            "policyGroupName": "production",
            "policyGroupType": "accounts"
        }
    ]
}
```

#### PolicyIssue Fields

| Field              | Type   | Description                                                           |
| ------------------ | ------ | --------------------------------------------------------------------- |
| `id`               | string | Unique identifier for the policy issue                                |
| `entityType`       | string | Type of entity (e.g., "insights-account", "stack")                    |
| `entityProject`    | string | Project or parent account name                                        |
| `entityId`         | string | Entity identifier                                                     |
| `stackVersion`     | number | Stack version (if applicable)                                         |
| `resourceVersion`  | number | Resource version (if applicable)                                      |
| `policyPack`       | string | Name of the policy pack                                               |
| `policyPackTag`    | string | Version tag of the policy pack                                        |
| `policyName`       | string | Name of the specific policy                                           |
| `resourceURN`      | string | URN of the resource                                                   |
| `resourceProvider` | string | Cloud provider (e.g., "aws", "azure")                                 |
| `resourceType`     | string | Type of the resource                                                  |
| `resourceName`     | string | Name of the resource                                                  |
| `message`          | string | Policy violation message                                              |
| `observedAt`       | string | ISO 8601 timestamp when the issue was first observed                  |
| `lastModified`     | string | ISO 8601 timestamp when the issue was last modified                   |
| `level`            | string | Severity level from policy definition (e.g., "advisory", "mandatory") |
| `severity`         | string | Additional severity classification                                    |
| `status`           | string | Issue status: `open`, `in_progress`, `by_design`, `fixed`, `ignored`  |
| `kind`             | string | Issue kind: `audit` or `preventative`                                 |
| `priority`         | string | Priority level: `p0`, `p1`, `p2`, `p3`, `p4`                          |
| `assignedTo`       | object | User assigned to this issue (optional)                                |
| `policyGroupName`  | string | Name of the policy group (optional)                                   |
| `policyGroupType`  | string | Type of policy group (optional)                                       |

## Get Policy Issue

Retrieve detailed information about a specific policy issue, including the policy definition and policy pack metadata.

```plain
GET /api/orgs/{organization}/policyresults/issues/{issueId}
```

### Parameters

| Parameter      | Type   | In   | Description                    |
| -------------- | ------ | ---- | ------------------------------ |
| `organization` | string | path | organization name              |
| `issueId`      | string | path | unique identifier of the issue |

### Example

```bash
curl \
  -H "Accept: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/policyresults/issues/{issueId}
```

### Default response

```plain
Status: 200 OK
```

```json
{
    "policyIssue": {
        "id": "b807f797-70b8-4add-9449-773ce22666c7",
        "entityType": "insights-account",
        "entityProject": "dev-sandbox",
        "entityId": "us-west-2",
        "resourceVersion": 11,
        "policyPack": "aws-hitrust",
        "policyPackTag": "0.0.5",
        "policyName": "ecs-task-definition-must-have-tags",
        "resourceURN": "urn:insights:dev-sandbox/us-west-2::aws::aws:ecs/taskDefinition:TaskDefinition::arn:aws:ecs:us-west-2:416178951233:task-definition/service-4e39feb5:1",
        "resourceProvider": "aws",
        "resourceType": "aws:ecs/taskDefinition:TaskDefinition",
        "resourceName": "arn:aws:ecs:us-west-2:416178951233:task-definition/service-4e39feb5:1",
        "message": "ECS task definitions must have tags\nECS task definition must have tags",
        "observedAt": "2025-09-24T00:49:14.928Z",
        "lastModified": "2025-09-24T17:06:15.131Z",
        "level": "advisory",
        "severity": "critical",
        "status": "open",
        "kind": "audit",
        "priority": "p4",
        "policyGroupName": "default-accounts-policy-group",
        "policyGroupType": "accounts"
    },
    "policy": {
        "name": "ecs-task-definition-must-have-tags",
        "description": "ECS task definitions must have tags",
        "enforcementLevel": "advisory",
        "message": "ESC "
    },
    "policyPack": {
        "source": "private",
        "publisher": "pulumi_local",
        "name": "aws-hitrust",
        "version": "0.0.5",
        "displayName": "Super Policy Pack Local",
        "accessLevel": "",
        "enforcementLevels": null
    }
}
```

## Update Policy Issue

Update the status, priority, or assignment of a policy issue.

```plain
PATCH /api/orgs/{organization}/policyresults/issues/{issueId}
```

### Parameters

All body fields are optional. Only provide the fields you want to update:

| Parameter      | Type   | In   | Description                                                        |
| -------------- | ------ | ---- | ------------------------------------------------------------------ |
| `organization` | string | path | organization name                                                  |
| `issueId`      | string | path | unique identifier of the issue                                     |
| `status`       | string | body | New status: `open`, `in_progress`, `by_design`, `fixed`, `ignored` |
| `priority`     | string | body | New priority: `p0`, `p1`, `p2`, `p3`, `p4`                         |
| `assignedTo`   | string | body | Username to assign the issue to (or `null` to unassign)            |

### Example

```bash
curl -X PATCH \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  -d '{
    "status": "in_progress",
    "priority": "p1",
    "assignedTo": "engineer@example.com"
  }' \
  https://api.pulumi.com/api/orgs/{organization}/policyresults/issues/{issueId}
```

### Default response

```plain
Status: 200 OK
```

Returns the updated policy issue:

```json
{
    "policyIssue": {
        "id": "b807f797-70b8-4add-9449-773ce22666c7",
        "entityType": "insights-account",
        "entityProject": "dev-sandbox",
        "entityId": "us-west-2",
        "resourceVersion": 11,
        "policyPack": "aws-hitrust",
        "policyPackTag": "0.0.5",
        "policyName": "ecs-task-definition-must-have-tags",
        "resourceURN": "urn:insights:dev-sandbox/us-west-2::aws::aws:ecs/taskDefinition:TaskDefinition::arn:aws:ecs:us-west-2:416178951233:task-definition/service-4e39feb5:1",
        "resourceProvider": "aws",
        "resourceType": "aws:ecs/taskDefinition:TaskDefinition",
        "resourceName": "arn:aws:ecs:us-west-2:416178951233:task-definition/service-4e39feb5:1",
        "message": "ECS task definitions must have tags\nECS task definition must have tags",
        "observedAt": "2025-09-24T00:49:14.928Z",
        "lastModified": "2025-10-20T16:30:00Z",
        "level": "advisory",
        "severity": "critical",
        "status": "in_progress",
        "kind": "audit",
        "priority": "p1",
        "assignedTo": {
            "name": "Engineer Name",
            "githubLogin": "engineer@example.com",
            "avatarUrl": "https://..."
        },
        "policyGroupName": "default-accounts-policy-group",
        "policyGroupType": "accounts"
    }
}
```

## List Policy Violations. **Deprecated** (TODO: need to make this standard)

Retrieve all policy issues for an organization.

```plain
GET /api/orgs/{organization}/policyresults/violationsv2
```

### Parameters

| Parameter      | Type   | In   | Description       |
| -------------- | ------ | ---- | ----------------- |
| `organization` | string | path | organization name |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/policyresults/violationsv2
```

### Default response

```plain
Status: 200 OK
```

```plain
{
    "policyViolations": [
        {
            "projectName": "pulumi-k8s-test",
            "stackName": "test",
            "stackVersion": 11,
            "policyPack": "kubernetes",
            "policyPackTag": "0.0.2",
            "policyName": "minimum-replica-count",
            "resourceURN": "urn:pulumi:test::pulumi-k8s-test::kubernetes:apps/v1:Deployment::nginx",
            "resourceType": "kubernetes:apps/v1:Deployment",
            "resourceName": "nginx",
            "message": "Checks that Kubernetes Deployments and ReplicaSets have at least three replicas.\nKubernetes Deployments should have at least three replicas.\n",
            "observedAt": "2025-01-16T23:44:13Z",
            "level": "advisory"
        },
        {
            "projectName": "test",
            "accountName": "us-west-1",
            "resourceVersion": 1,
            "policyPack": "aws-typescript",
            "policyPackTag": "0.0.1",
            "policyName": "s3-no-public-read",
            "resourceURN": "urn:insights:test/us-west-1::aws::aws:s3/bucket:Bucket::my-super-bucket-1234567890",
            "resourceType": "aws:s3/bucket:Bucket",
            "resourceName": "my-super-bucket-1234567890",
            "message": "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.\nTest violation",
            "observedAt": "2025-01-16T23:08:28Z",
            "level": "advisory"
        }
    ],
    "continuationToken": ""
}
```
