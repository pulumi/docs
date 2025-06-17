---
title: Stack Policy
title_tag: "Pulumi Cloud REST API: Stack Policy"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for managing policy enforcement on Pulumi stacks.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 21
---

Stack policy APIs allow you to retrieve information about policy groups and policy packs associated with a Pulumi stack. Policies define governance rules that are enforced during stack updates.

## Policy Operations

The API provides endpoints for the following operations:

- Getting policy groups associated with a stack
- Getting policy packs associated with a stack

## Get Stack Policy Groups

Get Policy Groups associated with a stack.

```plain
GET /api/stacks/{organization}/{project}/{stack}/policygroups
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
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/policygroups
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
    }
  ]
}
```

## Get Stack Policy Packs

Get Policy Packs associated with a stack.

```plain
GET /api/stacks/{organization}/{project}/{stack}/policypacks
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
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/policypacks
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "requiredPolicies": [
    {
      "name": "continuous-policy",
      "version": 3,
      "versionTag": "0.0.3",
      "displayName": "",
      "packLocation": "REDACTED",
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
