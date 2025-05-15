---
title: Policy Groups
title_tag: "Pulumi Cloud REST API: Policy Groups"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing policy groups that enforce governance rules across stacks.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 11
---

Policy Groups are collections of policy packs that can be applied to stacks to enforce governance rules. The Policy Groups API allows you to create, manage, and apply policy groups to stacks.

## Policy Group Operations

The API provides endpoints for the following operations:

- Listing available policy groups
- Getting policy group details
- Creating new policy groups
- Updating policy groups (rename, add/remove stacks, add/remove policy packs)
- Deleting policy groups

## List Policy Groups

List a summaries of policy groups by organization.

```plain
GET /api/orgs/{organization}/policygroups
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
  https://api.pulumi.com/api/orgs/{organization}/policygroups
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "policyGroups": [
    {
      "name": "continuous-policy",
      "isOrgDefault": false,
      "numStacks": 1,
      "numEnabledPolicyPacks": 1
    },
    {
      "name": "default-policy-group",
      "isOrgDefault": true,
      "numStacks": 2569,
      "numEnabledPolicyPacks": 1
    }
  ]
}
```

## Get Policy Group

Get policy group information.

```plain
GET /api/orgs/{organization}/policygroups/{policyGroup}
```

### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | path  | organization name                                                                                            |
| `policyGroup`       | string | path  | policy group name                                                                                            |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/policygroups/{policyGroup}
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "name": "continuous-policy",
  "isOrgDefault": false,
  "stacks": [
    {
      "name": "global",
      "routingProject": "continuous-policy"
    }
  ],
  "appliedPolicyPacks": [
    {
      "name": "continuous-policy",
      "displayName": "",
      "version": 3,
      "versionTag": "0.0.3",
      "config": {
        "all": {
          "enforcementLevel": "mandatory"
        },
        "continuous-policy": {
          "enforcementLevel": "mandatory",
          "policies": [
            {
              "assertion": {
                "operator": "eq",
                "value": 0
              },
              "label": "No node12 Lambdas",
              "mode": "ai",
              "query": "nodejs version 12"
            }
          ]
        }
      }
    }
  ]
}
```

## Create Policy Group

Create policy group.

```plain
POST /api/orgs/{organization}/policygroups
```

### Parameters

| Parameter           | Type   | In    | Description        |
|---------------------|--------|-------|--------------------|
| `organization`      | string | path  | organization name  |
| `name`              | string | body  | policy group name  |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"name":"myPolicyGroup"}' \
  https://api.pulumi.com/api/orgs/{organization}/policygroups
```

### Default response

```plain
Status: 204 OK
```

## Update Policy Group

Update policy group, rename, add/remove stacks, add/remove policy packs.

```plain
PATCH /api/orgs/{organization}/policygroups/{policyGroup}
```

| Parameter                     | Type       | In     | Description                                       |
|-------------------------------|------------|--------|---------------------------------------------------|
| `organization`                | string     | path   | organization name                                 |
| `policyGroup`                 | string     | path   | policy group name                                 |
| `newName`                     | string     | body   | new policy group name                             |
| `addStack`                    | object     | body   | add stack reference - see following parameters    |
| `addStack.name`               | string     | object | stack name                                        |
| `addStack.routingProject`     | string     | object | stack project                                     |
| `removeStack`                 | object     | body   | remove stack reference - see following parameters |
| `removeStack.name`            | string     | object | stack name                                        |
| `removeStack.routingProject`  | string     | object | stack project                                     |
| `addPolicyPack`               | object     | body   | add policy pack - see following parameters        |
| `addPolicyPack.name`          | string     | object | policy pack name                                  |
| `addPolicyPack.displayName`   | string     | object | policy pack display name                          |
| `addPolicyPack.version`       | number     | object | policy pack version                               |
| `addPolicyPack.versionTag`    | string     | object | policy pack version tag                           |
| `addPolicyPack.config`        | key/value  | object | policy pack config                                |
| `removePolicyPack`            | object     | body   | remove policy pack - see following parameters     |
| `removePolicyPack.name`       | string     | object | policy pack name                                  |
| `removePolicyPack.version`    | int        | object | policy pack version                               |
| `removePolicyPack.versionTag` | string     | object | policy pack version tag                           |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request PATCH \
  --data '{"newName":"myRenamedPolicyGroup"}' \
  https://api.pulumi.com/orgs/{organization}/policygroups/{policyGroup}
```

### Default response

```plain
Status: 204 OK
```

## Delete Policy Group

```plain
DELETE /api/orgs/{organization}/policygroups/{policyGroup}
```

| Parameter                     | Type       | In     | Description                                       |
|-------------------------------|------------|--------|---------------------------------------------------|
| `organization`                | string     | path   | organization name                                 |
| `policyGroup`                 | string     | path   | policy group name                                 |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{organization}/policygroups/{policyGroup}
```

### Default response

```plain
Status: 204 OK
```
