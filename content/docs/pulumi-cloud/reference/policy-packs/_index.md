---
title: Policy Packs
title_tag: "Pulumi Cloud REST API: Policy Packs"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing policy packs that define governance rules for infrastructure deployments.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 12
---

Policy Packs are collections of policies that define governance rules for infrastructure deployments. The Policy Packs API allows you to create, manage, and apply policy packs to enforce governance rules across your organization.

## Policy Pack Operations

The API provides endpoints for the following operations:

- Listing policy packs available in an organization
- Getting policy pack details at specific versions
- Creating new policy packs
- Applying policy packs to the default policy group
- Deleting policy packs and specific versions

## List Policy Packs

List policy packs by organization.

```plain
GET /api/orgs/{organization}/policypacks
```

### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/policypacks
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "policyPacks": [
    {
      "name": "aws-iso27001-compliance-ready-policies-typescript",
      "displayName": "",
      "versions": [
        1
      ],
      "versionTags": [
        "0.0.1"
      ]
    },
    {
      "name": "aws-typescript",
      "displayName": "",
      "versions": [
        1
      ],
      "versionTags": [
        "0.0.1"
      ]
    },
    {
      "name": "continuous-policy",
      "displayName": "",
      "versions": [
        3,
        2,
        1
      ],
      "versionTags": [
        "0.0.3",
        "0.0.2",
        "0.0.1"
      ]
    }
  ]
}
```

## Get Latest Policy Pack Version

Get policy pack information including config schema for the latest version.

```plain
GET /api/orgs/{organization}/policypacks/{policyPack}/latest
```

### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `policyPack`        | string | path  | policy pack name                                                                                             |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/policypacks/{policyPack}/latest
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "name": "continuous-policy",
  "displayName": "",
  "version": 3,
  "versionTag": "0.0.3",
  "policies": [
    {
      "name": "continuous-policy",
      "displayName": "",
      "description": "Continuous global policies that can be configured dynamically across the entire org using Pulumi Resource Search.",
      "enforcementLevel": "mandatory",
      "message": "",
      "configSchema": {
        "properties": {
          "enforcementLevel": {
            "enum": [
              "advisory",
              "mandatory",
              "remediate",
              "disabled"
            ],
            "type": "string"
          },
          "policies": {
            "items": {
              "properties": {
                "assertion": {
                  "properties": {
                    "operator": {
                      "enum": [
                        "eq",
                        "gt",
                        "lt",
                        "lte",
                        "gte"
                      ],
                      "type": "string"
                    },
                    "value": {
                      "type": "number"
                    }
                  },
                  "type": "object"
                },
                "label": {
                  "type": "string"
                },
                "mode": {
                  "enum": [
                    "query",
                    "ai"
                  ],
                  "type": "string"
                },
                "query": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "type": "array"
          }
        },
        "type": "object"
      }
    }
  ],
  "applied": false
}
```

## Get Policy Pack at Specific Version

Get policy pack information including config schema for a specific version.

```plain
GET /api/orgs/{organization}/policypacks/{policyPack}/versions/{version}
```

### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `policyPack`        | string | path  | policy pack name                                                                                             |
| `version`           | string | path  | version identifier                                                                                           |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/policypacks/{policyPack}/versions/{version}
```

## Get Policy Pack Schema at Specific Version

Get policy pack config schema for a specific version.

```plain
GET /api/orgs/{organization}/policypacks/{policyPack}/versions/{version}/schema
```

### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `policyPack`        | string | path  | policy pack name                                                                                             |
| `version`           | string | path  | version identifier                                                                                           |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/policypacks/{policyPack}/versions/{version}/schema
```

## Create Policy Pack

Create policy pack.

```plain
POST /api/orgs/{organization}/policypacks
```

### Parameters

| Parameter                            | Type          | In     | Description                                                                                     |
|--------------------------------------|---------------|--------|-------------------------------------------------------------------------------------------------|
| `organization`                       | string        | path   | organization name                                                                               |
| `name`                               | string        | body   | policy pack name                                                                                |
| `displayName`                        | string        | body   | policy pack display name                                                                        |
| `versionTag`                         | string        | body   | policy pack version tag name                                                                    |
| `policies`                           | array         | body   | policy pack policies - see following parameters                                                 |
| `policies[].name`                    | string        | object | policy name                                                                                     |
| `policies[].displayName`             | string        | object | policy display name                                                                             |
| `policies[].description`             | string        | object | policy description                                                                              |
| `policies[].enforcementLevel`        | string        | object | policy enforcement level - possible values are `advisory`, `mandatory`, `remediate`, `disabled` |
| `policies[].message`                 | string        | object | policy message                                                                                  |
| `policies[].configSchema`            | object        | object | policy config schema                                                                            |
| `policies[].configSchema.properties` | key/value     | object | config schema properties                                                                        |
| `policies[].configSchema.required`   | string array  | object | config schema required properties                                                               |
| `policies[].configSchema.type`       | string        | object | config schema type                                                                              |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"name":"myPolicyPack", "displayName": "My policy pack", "versionTag":"stable", "policies":[{"name": "myPolicy", "displayName": "My policy", "description": "awesome policy", "enforcementLevel": "mandatory","message":"my policy violation", "configSchema":{"properties": {"foo": "bar}, "required": "foo", "type": "object"}}]}' \
  https://api.pulumi.com/api/orgs/{organization}/policypacks
```

## Apply Policy Pack

Applies the latest version of a policy pack using the organization's default policy group.

```plain
POST /api/orgs/{organization}/policypacks/{policyPack}/latest
```

### Parameters

| Parameter                            | Type          | In     | Description                                                                                     |
|--------------------------------------|---------------|--------|-------------------------------------------------------------------------------------------------|
| `organization`                       | string        | path   | organization name                                                                               |
| `policyPack`                         | string        | path   | policy pack name                                                                                |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  https://api.pulumi.com/api/orgs/{organization}/policypacks/{policyPack}/latest
```

## Delete Policy Pack

```plain
DELETE /api/orgs/{organization}/policypacks/{policyPack}
```

| Parameter                     | Type       | In     | Description                                       |
|-------------------------------|------------|--------|---------------------------------------------------|
| `organization`                | string     | path   | organization name                                 |
| `policyPack`                  | string     | path   | policy pack name                                  |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{organization}/policypacks/{policyPack}
```

## Delete Policy Pack Version

```plain
DELETE /api/orgs/{organization}/policypacks/{policyPack}/versions/{version}
```

| Parameter                     | Type       | In     | Description                                       |
|-------------------------------|------------|--------|---------------------------------------------------|
| `organization`                | string     | path   | organization name                                 |
| `policyPack`                  | string     | path   | policy pack name                                  |
| `version`                     | number     | path   | policy pack version                               |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{organization}/policypacks/{policyPack}/versions/{version}
```
