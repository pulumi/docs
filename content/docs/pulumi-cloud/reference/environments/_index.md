---
title: Environments
title_tag: "Pulumi Cloud REST API: Environments"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing Pulumi ESC (Environments, Secrets, and Configuration).
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 5
---

Pulumi ESC (Environments, Secrets, and Configuration) provides a centralized way to manage infrastructure configuration. The Environments API allows you to create, manage, and use environments for your Pulumi deployments.

{{< notes >}}
Pulumi ESC and its associated REST API endpoints are currently in public preview.
{{< /notes >}}

## Environment Operations

The API provides endpoints for the following operations:

- Listing available environments
- Creating new environments
- Retrieving, updating, and deleting environments
- Opening environments to access their values
- Cloning environments

## List Environments

List environments available to the authenticated user.

```plain
GET /api/esc/environments/{organization}
```

### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `continuationToken` | string | query | **Optional.** the continuation token to use for retrieving the next set of results if results were truncated |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/esc/environments/{organization}
```

### Default response

```plain
Status: 200 OK
```

```plain
{
    "environments": [
        {
            "organization": "{organization}",
            "project": "my-first-project",
            "name": "my-first-environment",
            "created": "2023-10-10 11:28:01",
            "modified" :"2023-10-10 12:24:03"
        }
    ]
}
```

## Create Environment

Create a new environment.

```plain
POST /api/esc/environments/{organization}
```

### Body

| Key                 | Type   | In    | Description       |
|---------------------|--------|-------|-------------------|
| `project`           | string | path  | project name      |
| `name`              | string | path  | environment name  |

### Parameters

| Parameter           | Type   | In    | Description       |
|---------------------|--------|-------|-------------------|
| `organization`      | string | path  | organization name |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  https://api.pulumi.com/api/esc/environments/{organization}/{environment}
```

## Get Environment

Retrieve an environment's details.

```plain
GET /api/esc/environments/{organization}/{project}/{environment}
```

### Parameters

| Parameter           | Type   | In    | Description       |
|---------------------|--------|-------|-------------------|
| `organization`      | string | path  | organization name |
| `project`           | string | path  | project name      |
| `environment`       | string | path  | environment name  |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request GET \
  https://api.pulumi.com/api/esc/environments/{organization}/{project}/{environment}
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "values:
    aws:
      creds:
        fn::open::aws-login:
          oidc:
            duration: 1h
            roleArn: arn:aws:iam::12345678900:role/my-environments-oidc
            sessionName: my-environments-session
    environmentVariables:
      AWS_ACCESS_KEY_ID: ${aws.creds.accessKeyId}
      AWS_SECRET_ACCESS_KEY: ${aws.creds.secretAccessKey}
      AWS_SESSION_TOKEN: ${aws.creds.sessionToken}"
}
```

## Update Environment

Update an existing environment.

```plain
PATCH /api/esc/environments/{organization}/{project}/{environment}
```

### Parameters

| Parameter           | Type   | In    | Description       |
|---------------------|--------|-------|-------------------|
| `organization`      | string | path  | organization name |
| `project`           | string | path  | project name      |
| `environment`       | string | path  | environment name  |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  --data '<yaml content>' \
  https://api.pulumi.com/api/esc/environments/{organization}/{project}/{environment}
```

## Delete Environment

Delete an environment.

```plain
DELETE /api/esc/environments/{organization}/{project}/{environment}
```

### Parameters

| Parameter           | Type   | In    | Description       |
|---------------------|--------|-------|-------------------|
| `organization`      | string | path  | organization name |
| `project`           | string | path  | project name      |
| `environment`       | string | path  | environment name  |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/esc/environments/{organization}/{project}/{environment}
```

## Open Environment

Open an environment to access its resolved values.

```plain
POST /api/esc/environments/{organization}/{project}/{environment}/open
```

### Parameters

| Parameter           | Type   | In    | Description       |
|---------------------|--------|-------|-------------------|
| `organization`      | string | path  | organization name |
| `project`           | string | path  | project name      |
| `environment`       | string | path  | environment name  |
| `duration`          | string | query | **Optional.** open duration - A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms", "-1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  https://api.pulumi.com/api/esc/environments/{organization}/{project}/{environment}/open
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "id": 1234567,
  "diagnostics": ""
}
```

## Read Open Environment

Read values from an opened environment.

```plain
GET /api/esc/environments/{organization}/{project}/{environment}/open/{openSessionID}
```

### Parameters

| Parameter           | Type   | In    | Description       |
|---------------------|--------|-------|-------------------|
| `organization`      | string | path  | organization name |
| `project`           | string | path  | project name      |
| `environment`       | string | path  | environment name  |
| `openSessionID`     | string | path  | open session id   |
| `property`          | string | query | **Optional.** path to a specific property |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request GET \
  https://api.pulumi.com/api/esc/environments/{organization}/{project}/{environment}/open/{openSessionID}
```

### Default response

```plain
Status: 200 OK
```

```plain
"values":
  "aws":
    "creds":
      "accessKeyId": "<redacted>",
      "secretAccessKey": "<redacted>",
      "sessionToken": "<redacted>",
  "environmentVariables":
    "AWS_ACCESS_KEY_ID": "<redacted>",
    "AWS_SECRET_ACCESS_KEY": "<redacted>",
    "AWS_SESSION_TOKEN": "<redacted>""
```

## Clone Environment

Clone an environment to create a copy.

```plain
POST /api/esc/environments/{organization}/{project}/{environment}/clone
```

### Body

| Key                       | Type   | In   | Description                            |
|---------------------------|--------|------|----------------------------------------|
| `project`                 | string | body | new project name                       |
| `name`                    | string | body | new environment name                   |
| `preserveAccess`          | bool   | body | whether to preserve access permissions |
| `preserveHistory`         | bool   | body | whether to preserve history            |
| `preserveEnvironmentTags` | bool   | body | whether to preserve environment tags   |
| `preserveRevisionTags`    | bool   | body | whether to preserve version tags       |

### Parameters

| Parameter           | Type   | In    | Description       |
|---------------------|--------|-------|-------------------|
| `organization`      | string | path  | organization name |
| `project`           | string | path  | project name      |
| `environment`       | string | path  | environment name  |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  https://api.pulumi.com/api/esc/environments/{organization}/{project}/{environment}/clone
```
