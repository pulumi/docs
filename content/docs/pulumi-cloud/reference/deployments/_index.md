---
title: Deployments
title_tag: "Pulumi Cloud REST API: Deployments"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for configuring and managing Pulumi Deployments to automate infrastructure updates.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 4.5
aliases:
  - /docs/pulumi-cloud/deployments/api
  - /docs/pulumi-cloud/deployments/api/
  - /docs/reference/deployments-rest-api
  - /docs/reference/deployments-rest-api/
  - /docs/intro/deployments/api
  - /docs/intro/deployments/api/
---

The Deployments API allows you to configure and manage Pulumi Deployments, which enable you to execute Pulumi updates and other operations through the Pulumi Cloud. With this API, you can configure deployment settings for your stacks, trigger deployments, view deployment status and logs, and manage deployment execution.

## Deployment Operations

The API provides endpoints for the following operations:

- Get, update, and clear deployment settings for a stack
- Create new deployments to execute Pulumi operations
- Get deployment details and logs
- List deployments for a stack or organization
- Pause and resume deployments
- Get deployment metadata
- Cancel in-progress deployments

## Get Settings

Gets the deployment settings associated with a stack.

```plain
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/settings
```

### Parameters

| Parameter     | Type   | In    | Description                                  |
|---------------|--------|-------|----------------------------------------------|
| `organization`| string | path  | **Required.** The organization name.         |
| `project`     | string | path  | **Required.** The project name.              |
| `stack`       | string | path  | **Required.** The stack name.                |

### Example

#### Request

```shell
curl -XGET -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3-folder/dev/deployments/settings"
```

#### Response

```json
{
  "sourceContext": {
    "git": {
      "repoURL": "https://github.com/pulumi/deploy-demos.git",
      "branch": "refs/heads/demo",
      "repoDir": "pulumi-programs/aws-ts-s3"
    }
  },
  "operationContext": {
    "preRunCommands": [
      "echo \"hello world\""
    ],
    "environmentVariables": {
      "AWS_REGION": "us-west-2",
      "AWS_ACCESS_KEY_ID": "$AWS_ACCESS_KEY_ID",
      "AWS_SECRET_ACCESS_KEY": "$AWS_SECRET_ACCESS_KEY",
      "AWS_SESSION_TOKEN": "$AWS_SESSION_TOKEN"
    }
  }
}
```

## Patch Settings

Patches the deployment settings associated with a stack. If no Deployment Settings exist for a stack, this operation will create new Deployment Settings with the supplied values.

```plain
POST https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/settings
```

### Parameters

| Parameter     | Type   | In    | Description                                  |
|---------------|--------|-------|----------------------------------------------|
| `organization`| string | path  | **Required.** The organization name.         |
| `project`     | string | path  | **Required.** The project name.              |
| `stack`       | string | path  | **Required.** The stack name.                |
| `settings`    | object | body  | **Required.** The deployment settings to apply. |

The final settings for the stack are calculated by merging the settings present in the request with the stack's current settings according to the following rules:

- For object properties:
  - Start with a copy of the current property value
  - Remove all properties that are explicitly set to `null` in the patch value
  - Merge all non-`null` properties from the patch value that exist in the current property value
  - Add all non-`null` properties from the patch value that do not exist in the current property value
- For other properties, replace the current value with the patch value

### Example

If the current settings for a stack are:

```json
{
  "sourceContext": {
    "git": {
      "repoURL": "https://github.com/pulumi/deploy-demos.git",
      "branch": "refs/heads/demo",
      "repoDir": "pulumi-programs/aws-ts-s3"
    }
  },
  "operationContext": {
    "preRunCommands": [
      "echo \"hello world\""
    ],
    "environmentVariables": {
      "AWS_REGION": "us-west-2",
      "AWS_ACCESS_KEY_ID": "$AWS_ACCESS_KEY_ID",
      "AWS_SECRET_ACCESS_KEY": "$AWS_SECRET_ACCESS_KEY",
      "AWS_SESSION_TOKEN": "$AWS_SESSION_TOKEN"
    }
  }
}
```

And we apply this patch:

```shell
curl -i -XPOST -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3/dev/deployments/settings" \
-d '{
  "sourceContext": {
    "git": {
      "repoURL": null,
    }
  },
  "operationContext": {
    "preRunCommands": [
      "echo \"bonjour\""
    ],
    "environmentVariables": {
      "AWS_ACCESS_KEY_ID": null,
      "AWS_SECRET_ACCESS_KEY": null,
      "AWS_SESSION_TOKEN": null
    },
    "oidc": {
      "aws": {
        "roleArn": "my-role-arn",
        "sessionName": "pulumi-deploy"
      }
    }
  },
  "gitHub": {
    "repository": "pulumi/deploy-demos"
  }
}'
```

Then the new settings for the stack are:

```json
{
  "sourceContext": {
    "git": {
      "branch": "refs/heads/demo",
      "repoDir": "pulumi-programs/aws-ts-s3"
    }
  },
  "operationContext": {
    "preRunCommands": [
      "echo \"bonjour\""
    ],
    "environmentVariables": {
      "AWS_REGION": "us-west-2"
    },
    "oidc": {
      "aws": {
        "roleArn": "my-role-arn",
        "sessionName": "pulumi-deploy"
      }
    }
  },
  "gitHub": {
    "repository": "pulumi/deploy-demos"
  }
}
```

## Clear Settings

Clears the deployment settings associated with a stack.

```plain
DELETE https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/settings
```

### Parameters

| Parameter     | Type   | In    | Description                                  |
|---------------|--------|-------|----------------------------------------------|
| `organization`| string | path  | **Required.** The organization name.         |
| `project`     | string | path  | **Required.** The project name.              |
| `stack`       | string | path  | **Required.** The stack name.                |

### Example

```shell
curl -i -XDELETE -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3/dev/deployments/settings"
```

## Create Deployment

Creates a new deployment to execute a Pulumi program via the Pulumi Cloud.

```plain
POST https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments
```

{{< notes "info" >}}
The stack **must** exist before a deployment can be created for it. If you attempt to create a deployment for a stack that does not exist, the request will return an error stating as such.
{{< /notes >}}

### Parameters

| Parameter     | Type   | In    | Description                                  |
|---------------|--------|-------|----------------------------------------------|
| `organization`| string | path  | **Required.** The organization name.         |
| `project`     | string | path  | **Required.** The project name.              |
| `stack`       | string | path  | **Required.** The stack name.                |
| `operation`   | string | body  | **Required.** The Pulumi operation to perform (update, preview, refresh, destroy). |
| `inheritSettings` | boolean | body | **Optional.** Whether to inherit stack deployment settings. Default is `true`. |
| `sourceContext` | object | body | **Optional.** Source context for the deployment. |
| `operationContext` | object | body | **Optional.** Operation context for the deployment. |
| `executorContext` | object | body | **Optional.** Executor context for the deployment. |
| `gitHub` | object | body | **Optional.** GitHub integration settings. |
| `cacheOptions` | object | body | **Optional.** Cache options for the deployment. |

### Examples

#### Stack deployment settings

The following request will create a deployment in the "my-org" Pulumi organization for "aws-ts-s3" project and "dev" stack. It will use only the settings associated with the stack.

```shell
curl -i -XPOST -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3/dev/deployments" \
-d '{
  "operation": "update"
}'
```

#### Merged stack and request deployment settings

The following request will create a deployment in the "my-org" Pulumi organization for "aws-ts-s3" project and "dev" stack. It will merge the settings associated with the stack with the settings present in the request.

```shell
curl -i -XPOST -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3/dev/deployments" \
-d '{
  "operation": "update",
  "operationContext": {
    "environmentVariables": {
      "AWS_REGION": "us-east-1"
    }
  }
}'
```

#### Request deployment settings only

The following request will create a deployment in the "my-org" Pulumi organization for "aws-ts-s3" project and "dev" stack using only the deployment settings in the request.

```shell
curl -i -XPOST -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3/dev/deployments" \
-d '{
  "operation": "update",
  "inheritSettings": false,
  "sourceContext": {
    "git": {
      "repoURL": "https://github.com/pulumi/deploy-demos.git",
      "branch": "refs/heads/demo",
      "repoDir": "pulumi-programs/aws-ts-s3"
    }
  },
  "operationContext": {
    "preRunCommands": [
      "echo \"hello world\""
    ],
    "environmentVariables": {
      "AWS_REGION": "us-west-2",
      "AWS_ACCESS_KEY_ID": "$AWS_ACCESS_KEY_ID",
      "AWS_SECRET_ACCESS_KEY": "$AWS_SECRET_ACCESS_KEY",
      "AWS_SESSION_TOKEN": "$AWS_SESSION_TOKEN"
    }
  }
}'
```

## Get Deployment

Gets details for a specific deployment.

```plain
// Get deployment by ID
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/{deploymentID}

// Get deployment by version
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/version/{deploymentVersion}
```

### Parameters

| Parameter     | Type   | In    | Description                                  |
|---------------|--------|-------|----------------------------------------------|
| `organization`| string | path  | **Required.** The organization name.         |
| `project`     | string | path  | **Required.** The project name.              |
| `stack`       | string | path  | **Required.** The stack name.                |
| `deploymentID`| string | path  | **Required for first endpoint.** The deployment ID. |
| `deploymentVersion`| integer | path | **Required for second endpoint.** The deployment version. |

### Example

#### Request

```shell
curl -XGET -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3-folder/dev/deployments/9e5e1331-a018-4845-8714-1598ba8dc52e"
```

#### Response

```json
{
  "id": "9e5e1331-a018-4845-8714-1598ba8dc52e",
  "created": "2022-10-17 22:12:34.834",
  "modified": "2022-10-17 22:12:42.411",
  "status": "running",
  "version": 34,
  "requestedBy": {
    "name": "my-org",
    "githubLogin": "my-org",
    "avatarUrl": "https://avatars.githubusercontent.com/u/1234567?v=4",
    "email": "example@gmail.com"
  },
  "jobs": [
    {
      "status": "running",
      "started": "2022-10-17T22:12:41.191646Z",
      "lastUpdated": "2022-10-17T22:12:42.411732Z",
      "steps": [
        {
          "name": "Download deployment executor",
          "status": "succeeded",
          "started": "2022-10-17T22:12:41.191646Z",
          "lastUpdated": "2022-10-17T22:12:42.244429Z"
        },
        {
          "name": "Get source",
          "status": "running",
          "started": "2022-10-17T22:12:42.411732Z",
          "lastUpdated": "2022-10-17T22:12:42.411732Z"
        },
        {
          "name": "Download dependencies",
          "status": "not-started",
          "started": "0001-01-01T00:00:00Z",
          "lastUpdated": "0001-01-01T00:00:00Z"
        },
        {
          "name": "Pre-run command 1",
          "status": "not-started",
          "started": "0001-01-01T00:00:00Z",
          "lastUpdated": "0001-01-01T00:00:00Z"
        },
        {
          "name": "Pulumi operation",
          "status": "not-started",
          "started": "0001-01-01T00:00:00Z",
          "lastUpdated": "0001-01-01T00:00:00Z"
        }
      ]
    }
  ],
  "latestVersion": 34,
  "configuration": {
    "environmentVariables": [
      {
        "name": "AWS_REGION",
        "value": "us-west-2",
        "secret": false
      },
      {
        "name": "AWS_SECRET_ACCESS_KEY",
        "secret": true
      },
      {
        "name": "PULUMI_CI_BUILD_ID",
        "value": "9e5e1331-a018-4845-8714-1598ba8dc52e",
        "secret": false
      },
      {
        "name": "PULUMI_CI_BUILD_NUMBER",
        "value": "34",
        "secret": false
      },
      {
        "name": "PULUMI_CI_SYSTEM",
        "value": "Pulumi Deploy",
        "secret": false
      },
      {
        "name": "AWS_ACCESS_KEY_ID",
        "secret": true
      },
      {
        "name": "PULUMI_ACCESS_TOKEN",
        "secret": true
      },
      {
        "name": "PULUMI_BACKEND_URL",
        "value": "https://api.pulumi.com/",
        "secret": false
      },
      {
        "name": "AWS_SESSION_TOKEN",
        "secret": true
      }
    ],
    "source": {
      "git": {
        "repoURL": "https://github.com/pulumi/examples.git",
        "branch": "refs/heads/master",
        "repoDir": "aws-ts-s3-folder"
      }
    }
  },
  "pulumiOperation": "update"
}
```

## List Stack Deployments

Gets a list of deployments for a stack.

```plain
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments
```

### Parameters

| Parameter     | Type    | In    | Description                                      |
|---------------|---------|-------|--------------------------------------------------|
| `organization`| string  | path  | **Required.** The organization name.             |
| `project`     | string  | path  | **Required.** The project name.                  |
| `stack`       | string  | path  | **Required.** The stack name.                    |
| `page`        | integer | query | **Optional.** The page number (min: 1, default: 1). |
| `pageSize`    | integer | query | **Optional.** Results per page (min: 1, max: 100, default: 10). |
| `asc`         | boolean | query | **Optional.** Sort in ascending order (default: false). |
| `status`      | string  | query | **Optional.** Filter by deployment status.       |

### Example

#### Request

```shell
curl -XGET -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3-folder/dev/deployments?page=1&pageSize=5"
```

#### Response

```json
{
    "deployments": [
        {
            "id": "9e007591-277d-43c6-b256-9f0af0ebdc1b",
            "created": "2023-09-19 05:49:43.002",
            "modified": "2023-09-19 05:50:48.516",
            "status": "succeeded",
            "version": 959,
            "requestedBy": {
                "name": "Beep Boop",
                "githubLogin": "beepbooplogin",
                "avatarUrl": "https://api.pulumi.com/static/avatars/12345.png",
                "email": "beep@boop.com"
            },
            "projectName": "simple-resource",
            "stackName": "dev",
            "pulumiOperation": "update",
            "updates": [
                {
                    "id": "9dc85505-113f-4c6f-a023-8f80f4bc36b8",
                    "updateID": "df60a4c7-69dc-426d-8987-39e8544fe983",
                    "version": 1217,
                    "startTime": 1694820531,
                    "endTime": 1694820540,
                    "result": "succeeded",
                    "kind": "update",
                    "message": "",
                    "environment": {
                        "key": "value",
                        "..."
                    }
                }
            ],
            "jobs": [
                {
                    "status": "succeeded",
                    "started": "2023-09-15T23:28:17.644409853Z",
                    "lastUpdated": "2023-09-15T23:29:02.883538271Z",
                    "steps": [
                        {
                            "name": "Setup",
                            "status": "succeeded",
                            "started": "2023-09-15T23:28:17.644409853Z",
                            "lastUpdated": "2023-09-15T23:28:20.730268067Z"
                        },
                        {
                            "name": "Download deployment executor",
                            "status": "succeeded",
                            "started": "2023-09-15T23:28:22.318042694Z",
                            "lastUpdated": "2023-09-15T23:28:25.36490801Z"
                        },
                        {
                            "name": "Fetch provider credentials via OIDC",
                            "status": "succeeded",
                            "started": "2023-09-15T23:28:25.519842902Z",
                            "lastUpdated": "2023-09-15T23:28:25.729177668Z"
                        },
                        {
                            "name": "Get source",
                            "status": "succeeded",
                            "started": "2023-09-15T23:28:25.890605613Z",
                            "lastUpdated": "2023-09-15T23:28:31.455532053Z"
                        },
                        {
                            "name": "Download dependencies",
                            "status": "succeeded",
                            "started": "2023-09-15T23:28:31.69949523Z",
                            "lastUpdated": "2023-09-15T23:28:50.343866319Z"
                        },
                        {
                            "name": "pulumi update",
                            "status": "succeeded",
                            "started": "2023-09-15T23:28:50.561534112Z",
                            "lastUpdated": "2023-09-15T23:29:02.883538271Z"
                        }
                    ]
                }
            ],
            "initiator": "console"
        },
        "..."
    ],
    "itemsPerPage": 5,
    "total": 67
}
```

## List Organization Deployments

Gets a list of deployments for the entire organization. Only deployments belonging to stacks that the user has access to will be returned.

```plain
GET https://api.pulumi.com/api/orgs/{organization}/deployments
```

### Parameters

| Parameter     | Type    | In    | Description                                      |
|---------------|---------|-------|--------------------------------------------------|
| `organization`| string  | path  | **Required.** The organization name.             |
| `page`        | integer | query | **Optional.** The page number (min: 1, default: 1). |
| `pageSize`    | integer | query | **Optional.** Results per page (min: 1, max: 100, default: 10). |
| `asc`         | boolean | query | **Optional.** Sort in ascending order (default: false). |
| `status`      | string  | query | **Optional.** Filter by deployment status.       |

### Example

#### Request

```shell
curl -XGET -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/orgs/my-org/deployments?page=1&pageSize=5"
```

#### Response

```json
{
    "deployments": [
        {
            "id": "9e007591-277d-43c6-b256-9f0af0ebdc1b",
            "created": "2023-09-19 05:49:43.002",
            "modified": "2023-09-19 05:50:48.516",
            "status": "succeeded",
            "version": 5,
            "requestedBy": {
                "name": "Beep Boop",
                "githubLogin": "beepbooplogin",
                "avatarUrl": "https://api.pulumi.com/static/avatars/12345.png",
                "email": "beep@boop.com"
            },
            "projectName": "project-1",
            "stackName": "dev",
            "pulumiOperation": "update",
            "updates": [
                {
                    "id": "9dc85505-113f-4c6f-a023-8f80f4bc36b8",
                    "updateID": "df60a4c7-69dc-426d-8987-39e8544fe983",
                    "version": 1217,
                    "startTime": 1694820531,
                    "endTime": 1694820540,
                    "result": "succeeded",
                    "kind": "update",
                    "message": "",
                    "environment": {
                        "key": "value",
                        "..."
                    }
                }
            ],
            "jobs": [
                "..."
            ],
            "initiator": "console"
        },
        "..."
    ],
    "itemsPerPage": 5,
    "total": 67
}
```

## Get Deployment Logs

Gets logs for a specific deployment.

```plain
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/{deploymentID}/logs
```

### Parameters

| Parameter     | Type    | In    | Description                                      |
|---------------|---------|-------|--------------------------------------------------|
| `organization`| string  | path  | **Required.** The organization name.             |
| `project`     | string  | path  | **Required.** The project name.                  |
| `stack`       | string  | path  | **Required.** The stack name.                    |
| `deploymentID`| string  | path  | **Required.** The deployment ID.                 |
| `continuationToken` | string | query | **Optional.** Token for streaming logs.     |
| `job`         | integer | query | **Optional.** Job number to get logs for (for step logs). |
| `step`        | integer | query | **Optional.** Step number to get logs for (for step logs). |
| `offset`      | integer | query | **Optional.** Line offset for step logs.         |
| `count`       | integer | query | **Optional.** Batch size for step logs (default: 100). |

### Streaming logs

Streaming logs provide a simple interface to get all logs for a deployment, starting at the beginning. Each response includes a `token` which can be used to get the next set of logs, until no more logs are available.

#### Example

##### Request

```shell
curl -XGET -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3-folder/dev/deployments/6b1ec06b-4f41-4cce-a7c9-13ceded14db2/logs"
```

##### Response

```json
{
    "lines": [
        {
            "header": "Download deployment executor",
            "timestamp": "0001-01-01T00:00:00Z"
        },
        {
            "timestamp": "2022-10-06T22:34:02.058756202Z",
            "line": "  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n"
        },
        "..."
    ],
    "nextToken": "0.2.1"
}
```

### Step logs

Step logs return logs for individual steps of the deployment. This is helpful to walk through logs of a single step or start requesting logs in the middle of the deployment.

There are no more logs in the step if there is no `nextOffset` included in the response.

#### Example

##### Request

```shell
# Get logs for a deployment starting at the zero offset and a count size of 10
curl -i -XGET -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3-folder/dev/deployments/2ee5b292-28bb-44a5-8532-b6ac32f4ec49/logs/?step=5&count=10&offset=0"
```

##### Response

```json
{
    "nextOffset": 10,
    "lines": [
        {
            "timestamp": "2022-09-14T18:07:26.012974756Z",
            "line": "Updating (k8s/dev)\n"
        },
        "..."
    ]
}
```

## Pause Deployments

Pauses all queued deployments for a stack or organization. Deployments that are already running are allowed to complete and are not paused. New deployments are queued, and will run when the stack or organization's deployments are resumed.

Only organization administrators can pause deployments for an organization.

Note that you can only pause deployments for a stack that has deployment settings configured.

```plain
// Pauses new deployments for a stack
POST https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/pause

// Pauses new deployments for an organization
POST https://api.pulumi.com/api/orgs/{organization}/deployments/pause
```

### Parameters

| Parameter     | Type    | In    | Description                                      |
|---------------|---------|-------|--------------------------------------------------|
| `organization`| string  | path  | **Required.** The organization name.             |
| `project`     | string  | path  | **Required for stack endpoint.** The project name. |
| `stack`       | string  | path  | **Required for stack endpoint.** The stack name. |

### Example

```shell
curl -i -XPOST -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3-folder/dev/deployments/pause"
```

## Resume Deployments

Resumes deployments for a stack or organization. This will cause queued deployments to start being processed.

```plain
// Resumes deployment for a stack
POST https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/resume

// Resumes deployments for an organization
POST https://api.pulumi.com/api/orgs/{organization}/deployments/resume
```

### Parameters

| Parameter     | Type    | In    | Description                                      |
|---------------|---------|-------|--------------------------------------------------|
| `organization`| string  | path  | **Required.** The organization name.             |
| `project`     | string  | path  | **Required for stack endpoint.** The project name. |
| `stack`       | string  | path  | **Required for stack endpoint.** The stack name. |

### Example

```shell
curl -i -XPOST -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stack/my-org/aws-ts-s3-folder/dev/deployments/resume"
```

## Get Deployments Metadata

Get metadata related to deployments for a stack or organization. This includes information such as if deployments are paused, and why they're paused.

```plain
// Get deployments metadata for a stack
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/metadata

// Get deployments metadata for an organization
GET https://api.pulumi.com/api/orgs/{organization}/deployments/metadata
```

### Parameters

| Parameter     | Type    | In    | Description                                      |
|---------------|---------|-------|--------------------------------------------------|
| `organization`| string  | path  | **Required.** The organization name.             |
| `project`     | string  | path  | **Required for stack endpoint.** The project name. |
| `stack`       | string  | path  | **Required for stack endpoint.** The stack name. |

### Example

#### Stack metadata request

```shell
curl -XGET -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stack/my-org/aws-ts-s3-folder/dev/deployments/metadata"
```

#### Response

```json
{
  "paused": true,
  "stackPaused": false,
  "organizationPaused": true
}
```

#### Organization metadata request

```shell
curl -XGET -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/orgs/my-org/deployments/metadata"
```

#### Response

```json
{
  "paused": false,
  "pausedStacks": ["aws-ts-s3-folder/dev", "aws-ts-s3-folder/staging"],
  "concurrency": 1,
  "deploymentCounts": {
    "notStarted": 2,
    "accepted": 0,
    "running": 0,
    "failed": 0,
    "succeeded": 5,
    "skipped": 0,
    "total": 7
  }
}
```

## Cancel Deployment

Cancels an in-progress deployment.

{{< notes type="warning" >}}
Canceling a deployment is a *very dangerous* action and may leave the stack in an inconsistent state if the deployment is canceled during the execution of a Pulumi operation.
{{< /notes >}}

```plain
POST https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/{deploymentID}/cancel
```

### Parameters

| Parameter     | Type    | In    | Description                                      |
|---------------|---------|-------|--------------------------------------------------|
| `organization`| string  | path  | **Required.** The organization name.             |
| `project`     | string  | path  | **Required.** The project name.                  |
| `stack`       | string  | path  | **Required.** The stack name.                    |
| `deploymentID`| string  | path  | **Required.** The deployment ID.                 |

### Example

```shell
curl -i -XPOST -H "Content-Type: application/json" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
--location "https://api.pulumi.com/api/stacks/my-org/aws-ts-s3-folder/dev/deployments/2ee5b292-28bb-44a5-8532-b6ac32f4ec49/cancel"
```

## Schema Definitions

This section documents the data schemas used by the Deployments API. Understanding these schemas helps you interpret API responses and structure API requests correctly.

### ExecutorContext

The executor context defines information about the executor where the Pulumi operation is executed. If unspecified, the default [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi) image is used.

```json
{
  "executorImage": "pulumi/pulumi-nodejs:latest"
}
```

or with credentials:

```json
{
  "executorImage": {
    "reference": "myregistry.azurecr.io/myimage:latest",
    "credentials": {
      "username": "my-username",
      "password": {
        "secret": "my-secret-password"
      }
    }
  }
}
```

#### Properties

| Name          | Type           | Description                                      |
|---------------|----------------|--------------------------------------------------|
| `executorImage` | string\|object | **Optional.** The image to use for execution.   |
| `executorImage.reference` | string | **Required when executorImage is an object.** The reference to the image. |
| `executorImage.credentials` | object | **Optional.** Credentials for private registry. |
| `executorImage.credentials.username` | string | **Required when credentials are provided.** Username for authentication. |
| `executorImage.credentials.password` | Secret | **Required when credentials are provided.** Password for authentication. |

### SourceContext

The source context contains information about where the source code for your project is located. Currently, only git repos are supported as a source.

```json
{
  "git": {
    "repoURL": "https://github.com/pulumi/examples.git",
    "branch": "refs/heads/master",
    "repoDir": "aws-ts-s3-folder"
  }
}
```

#### Properties

| Name          | Type           | Description                                      |
|---------------|----------------|--------------------------------------------------|
| `git.repoURL` | string | **Optional.** URL of the git repository. |
| `git.branch` | string | **Optional.** Repository branch to use. |
| `git.repoDir` | string | **Optional.** Directory where Pulumi.yaml is located. |
| `git.commit` | string | **Optional.** Hash of the commit to deploy. Mutually exclusive with branch. |
| `git.gitAuth` | object | **Optional.** Authentication information for the git repo. |

### OperationContext

The operation context describes any context required for Pulumi operations to execute such as pre-run commands and environment variables.

```json
{
  "preRunCommands": [
    "echo \"hello world\""
  ],
  "environmentVariables": {
    "AWS_REGION": "us-west-2",
    "MY_PASSWORD": {
      "secret": "my-secret-password"
    }
  },
  "options": {
    "skipInstallDependencies": false,
    "skipIntermediateDeployments": false,
    "deleteAfterDestroy": false
  },
  "oidc": {
    "aws": {
      "roleArn": "arn:aws:iam::123456789000:role/pulumi-deploy-role",
      "sessionName": "pulumi-deploy-session"
    }
  }
}
```

#### Properties

| Name               | Type           | Description                                      |
|--------------------|----------------|--------------------------------------------------|
| `preRunCommands`   | string[] | **Optional.** Commands to run before Pulumi execution. |
| `environmentVariables` | object | **Optional.** Environment variables for the operation. |
| `options` | object | **Optional.** Operation context options. |
| `options.skipInstallDependencies` | boolean | **Optional.** Skip automated dependency installation. |
| `options.skipIntermediateDeployments` | boolean | **Optional.** Skip intermediate deployments. |
| `options.deleteAfterDestroy` | boolean | **Optional.** Delete stack after destroy operation. |
| `oidc` | object | **Optional.** OIDC configuration for cloud provider authentication. |

### GitHub

The GitHub block describes settings for Pulumi Deployments' GitHub integration.

```json
{
  "repository": "pulumi/deploy-demos",
  "deployCommits": true,
  "previewPullRequests": true,
  "pullRequestTemplate": false,
  "paths": [ "pulumi-programs/bucket-time/**", "!pulumi/programs/bucket-time/README.md" ]
}
```

#### Properties

| Name                | Type           | Description                                      |
|---------------------|----------------|--------------------------------------------------|
| `repository`        | string | **Required.** The GitHub repository containing the Pulumi program. |
| `deployCommits`     | boolean | **Optional.** Run update deployments for commits to the configured branch. |
| `previewPullRequests` | boolean | **Optional.** Run preview deployments for PRs targeting the configured branch. |
| `pullRequestTemplate` | boolean | **Optional.** Enable Review Stacks for this branch. |
| `paths`             | string[] | **Optional.** Path filters for triggering deployments. |

### CacheOptions

The cache options block defines settings related to dependency caching during deployments.

```json
{
  "cacheOptions": {
    "enable": "true"
  }
}
```

#### Properties

| Name      | Type    | Description                                      |
|-----------|---------|--------------------------------------------------|
| `enable`  | boolean | **Required.** Whether to use dependency caching. |
