---
title: "Pulumi Service REST API"
meta_desc: An overview of the Pulumi Service REST API for querying Organization, Stack, State, etc. information.
menu:
  reference:
    weight: 4
---

The Pulumi Service REST API is used by the Pulumi CLI to query and interact with state information, history, stack tags, etc. This API is available for end users to integrate into their own automation use cases.

{{% notes "info" %}}
While the Pulumi Service REST API is used by the Pulumi CLI and the console, Pulumi makes no guarantees about changes that might affect backwards compatibility or cause breaking changes.
{{% /notes %}}

## Endpoint URL

For the Managed Pulumi Service (i.e. [app.pulumi.com](https://app.pulumi.com/)), API endpoints are prefixed with the following url:

```
https://api.pulumi.com
```

If you are using [Self-Hosted Pulumi Service]({{< relref "docs/guides/self-hosted" >}}), then use the configured endpoint for the [Pulumi API component]({{< relref "/docs/guides/self-hosted/components/api#api-service" >}}) (e.g. `https://api.pulumi.example.com`).

## Authentication

All requests must be authenticated using a token via the `Authorization` HTTP header.

The `Authorization` header must be in the form below with the literal string `token`, then a space, then your access token value.

```
Authorization: token {token}
```

To view your access tokens, or create a new one, view the <a href="https://app.pulumi.com/account/tokens" target="_blank">Access Tokens</a> page. You will see a list of past tokens, when they were last used, and have the ability to revoke them.

The Pulumi Service REST API will return a 401 status code if the token is missing or invalid.

## Required Request Headers

The following headers are required for all operations except where explicitly noted:

```
Accept: application/vnd.pulumi+8
Content-Type: application/json
```

<!-- ###################################################################### -->

## Stacks

### List Stacks

Lists stacks available to the authenticated user.

```
GET /api/user/stacks
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | query | **Optional.** organization name to filter stacks by |
| `project` | string | query | **Optional.** organization name to filter stacks by |
| `tagName` | string | query | **Optional.** tag name to filter stacks by |
| `tagValue` | string | query | **Optional.** tag value to filter stacks by |
| `continuationToken` | string | query | **Optional.** the continuation token to use for retrieving the next set of results if results were truncated |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/user/stacks?organization={organization}&tagName={tagName}&tagValue={tagValue}
```

#### Default response

```
Status: 200 OK
```

```
{
  "stacks": [
    {
      "orgName": "org1",
      "projectName": "project1",
      "stackName": "dev",
      "lastUpdate": 1612481387,
      "resourceCount": 0
    },
    {
      "orgName": "org2",
      "projectName": "project2",
      "stackName": "prod",
      "lastUpdate": 1605474464,
      "resourceCount": 0
    }
  ],
  "continuationToken": "5-"
}
```

<!-- ###################################################################### -->

### Get Stack

```
GET /api/stacks/{organization}/{project}/{stack}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}
```

#### Default response

```
Status: 200 OK
```

```
{
  "orgName": "demo",
  "projectName": "demo-aws-ts-webserver",
  "stackName": "dev-user1",
  "currentOperation": {
    "kind": "update",
    "author": "user1",
    "started": 1615872156
  },
  "activeUpdate": "d333a711-4aa0-402f-be6d-72af9665fc37",
  "tags": {
    "gitHub:owner": "pulumi",
    "gitHub:repo": "customer-engineering",
    "pulumi:description": "A minimal AWS TypeScript Pulumi program",
    "pulumi:project": "demo-aws-ts-webserver",
    "pulumi:runtime": "nodejs",
    "pulumi:secrets_provider": "service",
    "vcs:kind": "github.com",
    "vcs:owner": "pulumi",
    "vcs:repo": "customer-engineering"
  },
  "version": 91
}
```

<!-- ###################################################################### -->

### Get Stack State

```
GET /api/stacks/{organization}/{project}/{stack}/export
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/export
```

#### Default response

```
Status: 200 OK
```

```
{
  "version": 3,
  "deployment": {
    "manifest": {
      "time": "2021-03-15T22:29:53.782994-07:00",
      "magic": "6ed32cc63f3d459cb6f52bb150bc8ff68db740bf43964d429d5ca57f52c832b1",
      "version": "v2.22.0"
    },
    "secrets_providers": {
      "type": "service",
      "state": {
        "url": "https://api.pulumi.com",
        "owner": "org1",
        "project": "demo-aws-ts-webserver",
        "stack": "dev-user1"
      }
    },
    "resources": [
      {
        "urn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:pulumi:Stack::demo-aws-ts-webserver-dev-user1",
        "custom": false,
        "type": "pulumi:pulumi:Stack",
        "outputs": {
          "vpcId": "vpc-04057e18647a66e24"
        }
      },
      {
        "urn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:providers:aws::default_3_32_0",
        "custom": true,
        "id": "d77c9fd7-1c06-427d-ba26-dbd8a8cbf91a",
        "type": "pulumi:providers:aws",
        "inputs": {
          "region": "us-west-2",
          "version": "3.32.0"
        },
        "outputs": {
          "region": "us-west-2",
          "version": "3.32.0"
        }
      },
      {
        "urn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::aws:ec2/vpc:Vpc::main",
        "custom": true,
        "id": "vpc-04057e18647a66e24",
        "type": "aws:ec2/vpc:Vpc",
        "inputs": {
          "__defaults": [
            "assignGeneratedIpv6CidrBlock",
            "enableDnsSupport",
            "instanceTenancy"
          ],
          "assignGeneratedIpv6CidrBlock": false,
          "cidrBlock": "10.0.0.0/16",
          "enableDnsSupport": true,
          "instanceTenancy": "default"
        },
        "outputs": {
          "__meta": "{\"schema_version\":\"1\"}",
          "arn": "arn:aws:ec2:us-west-2:0123456789:vpc/vpc-04057e18647a66e24",
          "assignGeneratedIpv6CidrBlock": false,
          "cidrBlock": "10.0.0.0/16",
          "defaultNetworkAclId": "acl-0b63012743b57140d",
          "defaultRouteTableId": "rtb-01c36ce5fcc3ac797",
          "defaultSecurityGroupId": "sg-072f0a9bf075de1f5",
          "dhcpOptionsId": "dopt-6db97615",
          "enableClassiclink": false,
          "enableClassiclinkDnsSupport": false,
          "enableDnsHostnames": false,
          "enableDnsSupport": true,
          "id": "vpc-04057e18647a66e24",
          "instanceTenancy": "default",
          "ipv6AssociationId": "",
          "ipv6CidrBlock": "",
          "mainRouteTableId": "rtb-01c36ce5fcc3ac797",
          "ownerId": "0123456789",
          "tags": {}
        },
        "parent": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:pulumi:Stack::demo-aws-ts-webserver-dev-user1",
        "provider": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:providers:aws::default_3_32_0::d77c9fd7-1c06-427d-ba26-dbd8a8cbf91a",
        "propertyDependencies": {
          "cidrBlock": null
        }
      }
    ]
  }
}
```

<!-- ###################################################################### -->

### Transfer Stack

Transfers the stack from one organization in the Pulumi Service to a different organization. The user calling this operation must have the necessary [stack permissions]({{< relref "/docs/intro/pulumi-service/projects-and-stacks#stack-permissions" >}}) for this operation to be successful.

This operation will return a 409 response error if an update is currently in progress.

```
POST /api/stacks/{organization}/{project}/{stack}/transfer
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |
| `toOrg` | string | body | the organization to transfer the stack _to_ |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request POST \
  --data '{"toOrg":"{toOrg}"}' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/transfer
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

### Delete Stack

```
DELETE /api/stacks/{organization}/{project}/{stack}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |
| `force` | boolean | query | flag indicating to delete the stack even if it still contains resources |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request DELETE \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

## Stack Tags

<!-- ###################################################################### -->

### Get Stack Tags

Use [Get Stack](#get-stack) to retrieve a stack's details including its tags.

<!-- ###################################################################### -->

### Set Stack Tag

```
POST /api/stacks/{organization}/{project}/{stack}/tags
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |
| `name` | string | body | tag name |
| `value` | string | body | tag value |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request POST \
  --data '{"name":"{tagName}","value":"{tagValue}"}' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/tags
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

### Delete Stack Tag

```
DELETE /api/stacks/{organization}/{project}/{stack}/tags/{tagName}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |
| `tagName` | string | path | tag name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request DELETE \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/tags/{tagName}
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

## Stack Updates

<!-- ###################################################################### -->

### List Stack Updates

```
GET /api/stacks/{organization}/{project}/{stack}/updates
```

By default the results are not paginated. You can specify `page` and `pageSize` query parameters to paginate the results.
> `?pageSize=1&page=1` can be used to return only the most recent update.

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |
| `page` | number | query | **Optional.** page of the results to return |
| `pageSize` | number | query | **Optional.** number of results per page |
| `output-type` | number | query | **Optional.** the response format to return - possible values are `service` or `cli` (default) |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/updates?output-type=service
```

#### Default response

```
Status: 200 OK
```

```
{
  "updates": [
    {
      "info": {
        "kind": "update",
        "startTime": 1615872578,
        "message": "Add `gcp-py-webserver` demo. (#160)",
        "environment": {
          "exec.kind": "cli",
          "git.author": "First Last",
          "git.author.email": "user1@example.com",
          "git.committer": "GitHub",
          "git.committer.email": "noreply@github.com",
          "git.dirty": "true",
          "git.head": "e61b846e6e8395338bce1053c2edb29ee3213b4b",
          "git.headName": "refs/heads/master",
          "github.pr.number": "160",
          "vcs.kind": "github.com",
          "vcs.owner": "org1",
          "vcs.repo": "repo1"
        },
        "config": {
          "aws:region": {
            "string": "us-west-2",
            "secret": false,
            "object": false
          }
        },
        "result": "succeeded",
        "endTime": 1615872594,
        "version": 95,
        "resourceChanges": {
          "create": 2
        }
      },
      "updateID": "938cd018-3ecc-4a9e-86dd-42e84fefcc9c",
      "githubCommitInfo": {
        "slug": "org1/repo1",
        "sha": "e61b846e6e8395338bce1053c2edb29ee3213b4b",
        "url": "https://github.com/org1/repo1/commit/e61b846e6e8395338bce1053c2edb29ee3213b4b",
        "author": {
          "name": "First Last",
          "githubLogin": "user1",
          "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
        }
      },
      "version": 95,
      "latestVersion": 95,
      "requestedBy": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
      },
      "policyPacks": [
        {
          "name": "aws",
          "displayName": "",
          "version": 23,
          "versionTag": "0.1.20201015-2",
          "config": {
            "allowed-image-owner": {
              "allowedPublishers": [
                "self",
                "099720109477"
              ]
            },
            "maximum-instance-count": {
              "maximumInstanceCount": 2
            },
            "prohibited-services": {
              "enforcementLevel": "advisory"
            },
            "require-region": {
              "allowedRegions": [
                "us-west-2"
              ]
            },
            "vpc-sizing": {
              "enforcementLevel": "advisory",
              "maxSubnetPrefixLength": 22
            }
          }
        },
        {
          "name": "azure",
          "displayName": "",
          "version": 12,
          "versionTag": "0.1.20200912",
          "config": {
            "allowed-image-owner": {
              "allowedPublishers": [
                "canonical"
              ]
            },
            "maximum-instance-count": {
              "enforcementLevel": "advisory",
              "maximumInstanceCount": 2
            },
            "prohibited-services": {
              "enforcementLevel": "advisory"
            },
            "vpc-sizing": {
              "maxSubnetPrefixLength": 22
            }
          }
        },
        {
          "name": "k8s",
          "displayName": "",
          "version": 13,
          "versionTag": "0.1.20201105-1",
          "config": {
            "replica-count": {
              "enforcementLevel": "advisory"
            }
          }
        },
        {
          "name": "cost-optimization",
          "displayName": "",
          "version": 9,
          "versionTag": "0.1.20201015-3",
          "config": {
            "aws-budget-limit": {
              "maxMonthlyCost": 50
            },
            "gcp-budget-limit": {
              "maxMonthlyCost": 50
            }
          }
        },
        {
          "name": "azure-nextgen",
          "displayName": "",
          "version": 3,
          "versionTag": "0.1.20201222-1",
          "config": {
            "allowed-image-owner": {
              "allowedPublishers": [
                "canonical"
              ]
            },
            "maximum-instance-count": {
              "maximumInstanceCount": 2
            },
            "vnet-sizing": {
              "enforcementLevel": "advisory",
              "maxSubnetPrefixLength": 22
            }
          }
        },
        {
          "name": "gcp",
          "displayName": "",
          "version": 19,
          "versionTag": "0.1.20200912",
          "config": {
            "allowed-image-owner": {
              "allowedPublishers": [
                "ubuntu-os-cloud"
              ]
            },
            "maximum-instance-count": {
              "maximumInstanceCount": 2
            },
            "subnet-sizing": {
              "maxSubnetPrefixLength": 22
            }
          }
        }
      ]
    },
    {
      "info": {
        "kind": "destroy",
        "startTime": 1615872573,
        "message": "Add `gcp-py-webserver` demo. (#160)",
        "environment": {
          "exec.kind": "cli",
          "git.author": "First Last",
          "git.author.email": "user1@example.com",
          "git.committer": "GitHub",
          "git.committer.email": "noreply@github.com",
          "git.dirty": "true",
          "git.head": "e61b846e6e8395338bce1053c2edb29ee3213b4b",
          "git.headName": "refs/heads/master",
          "github.pr.number": "160",
          "vcs.kind": "github.com",
          "vcs.owner": "org1",
          "vcs.repo": "repo1"
        },
        "config": {
          "aws:region": {
            "string": "us-west-2",
            "secret": false,
            "object": false
          }
        },
        "result": "succeeded",
        "endTime": 1615872575,
        "version": 94,
        "resourceChanges": {
          "delete": 2
        }
      },
      "updateID": "d6a21779-99b7-42b1-b1f3-0f2045baa083",
      "githubCommitInfo": {
        "slug": "org1/repo1",
        "sha": "e61b846e6e8395338bce1053c2edb29ee3213b4b",
        "url": "https://github.com/org1/repo1/commit/e61b846e6e8395338bce1053c2edb29ee3213b4b",
        "author": {
          "name": "First Last",
          "githubLogin": "user1",
          "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
        }
      },
      "version": 94,
      "latestVersion": 95,
      "requestedBy": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
      }
    }
  ],
  "itemsPerPage": 10,
  "total": 95
}
```

<!-- ###################################################################### -->

### Get Update Status

```
GET /api/stacks/{organization}/{project}/{stack}/update/{updateID}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |
| `updateID` | uuid | path | update id - UUID as retrieved from [List Stack Updates](#list-stack-updates) using `?output-type=service` |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/update/{updateID}
```

#### Default response

```
Status: 200 OK
```

```
{
  "status": "succeeded",
  "events": []
}
```

<!-- ###################################################################### -->

### List Update Events

```
GET /api/stacks/{organization}/{project}/{stack}/update/{updateID}/events
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |
| `updateID` | uuid | path | update id - UUID as retrieved from [List Stack Updates](#list-stack-updates) using `?output-type=service` |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/update/{updateID}/events
```

#### Default response

```
Status: 200 OK
```

```
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
      "type": "policyEvent",
      "policyEvent": {
        "resourceUrn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::aws:ec2/vpc:Vpc::main",
        "message": "<{%reset%}>VPCs must be of appropriate size.\nAddress space [10.0.0.0/16] is too large. Must be [/22] or smaller.<{%reset%}>\n",
        "color": "raw",
        "policyName": "vpc-sizing",
        "policyPackName": "aws",
        "policyPackVersion": "0.1.20201015-2",
        "policyPackVersionTag": "0.1.20201015-2",
        "enforcementLevel": "advisory"
      }
    },
    {
      "timestamp": 1615872593,
      "type": "resourcePreEvent",
      "resourcePreEvent": {
        "metadata": {
          "op": "create",
          "urn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::aws:ec2/vpc:Vpc::main",
          "type": "aws:ec2/vpc:Vpc",
          "old": null,
          "new": {
            "type": "aws:ec2/vpc:Vpc",
            "urn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::aws:ec2/vpc:Vpc::main",
            "custom": true,
            "id": "",
            "parent": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:pulumi:Stack::demo-aws-ts-webserver-dev-user1",
            "inputs": {
              "__defaults": [
                "assignGeneratedIpv6CidrBlock",
                "enableDnsSupport",
                "instanceTenancy"
              ],
              "assignGeneratedIpv6CidrBlock": false,
              "cidrBlock": "10.0.0.0/16",
              "enableDnsSupport": true,
              "instanceTenancy": "default"
            },
            "outputs": {},
            "provider": ""
          },
          "logical": true,
          "provider": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:providers:aws::default_3_32_0::d77c9fd7-1c06-427d-ba26-dbd8a8cbf91a"
        }
      }
    },
    {
      "timestamp": 1615872593,
      "type": "resOutputsEvent",
      "resOutputsEvent": {
        "metadata": {
          "op": "create",
          "urn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::aws:ec2/vpc:Vpc::main",
          "type": "aws:ec2/vpc:Vpc",
          "old": null,
          "new": {
            "type": "aws:ec2/vpc:Vpc",
            "urn": "urn:pulumi:dev-user1::demo-aws-ts-webserver::aws:ec2/vpc:Vpc::main",
            "custom": true,
            "id": "vpc-04057e18647a66e24",
            "parent": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:pulumi:Stack::demo-aws-ts-webserver-dev-user1",
            "inputs": {
              "__defaults": [
                "assignGeneratedIpv6CidrBlock",
                "enableDnsSupport",
                "instanceTenancy"
              ],
              "assignGeneratedIpv6CidrBlock": false,
              "cidrBlock": "10.0.0.0/16",
              "enableDnsSupport": true,
              "instanceTenancy": "default"
            },
            "outputs": {
              "__meta": "{\"schema_version\":\"1\"}",
              "arn": "arn:aws:ec2:us-west-2:0123456789:vpc/vpc-04057e18647a66e24",
              "assignGeneratedIpv6CidrBlock": false,
              "cidrBlock": "10.0.0.0/16",
              "defaultNetworkAclId": "acl-0b63012743b57140d",
              "defaultRouteTableId": "rtb-01c36ce5fcc3ac797",
              "defaultSecurityGroupId": "sg-072f0a9bf075de1f5",
              "dhcpOptionsId": "dopt-6db97615",
              "enableClassiclink": false,
              "enableClassiclinkDnsSupport": false,
              "enableDnsHostnames": false,
              "enableDnsSupport": true,
              "id": "vpc-04057e18647a66e24",
              "instanceTenancy": "default",
              "ipv6AssociationId": "",
              "ipv6CidrBlock": "",
              "mainRouteTableId": "rtb-01c36ce5fcc3ac797",
              "ownerId": "0123456789",
              "tags": {}
            },
            "provider": ""
          },
          "logical": true,
          "provider": "urn:pulumi:dev-user1::demo-aws-ts-webserver::pulumi:providers:aws::default_3_32_0::d77c9fd7-1c06-427d-ba26-dbd8a8cbf91a"
        }
      }
    },
    {
      "timestamp": 1615872593,
      "type": "resOutputsEvent",
      "resOutputsEvent": {
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
            "outputs": {
              "vpcId": "vpc-04057e18647a66e24"
            },
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

<!-- ###################################################################### -->

### List Previews

List all previews since the last update operation.

```
GET /api/stacks/{organization}/{project}/{stack}/updates/latest/previews
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/updates/latest/previews
```

#### Default response

```
Status: 200 OK
```

```
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
      "githubCommitInfo": {
        "slug": "pulumi/examples",
        "sha": "35caae8d73c3ecb0eac1256ba0e03775f24514da",
        "url": "https://github.com/pulumi/examples/commit/35caae8d73c3ecb0eac1256ba0e03775f24514da",
        "author": {
          "name": "First Last",
          "githubLogin": "user1",
          "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
        }
      },
      "version": 1,
      "latestVersion": 0,
      "requestedBy": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
      }
    },
    {
      "info": {
        "kind": "Pupdate",
        "startTime": 1624932977,
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
        "endTime": 1624932992,
        "version": 1,
        "resourceChanges": {
          "create": 1
        }
      },
      "updateID": "cf72ac80-4b87-4e26-9974-9eef3267995d",
      "githubCommitInfo": {
        "slug": "pulumi/examples",
        "sha": "35caae8d73c3ecb0eac1256ba0e03775f24514da",
        "url": "https://github.com/pulumi/examples/commit/35caae8d73c3ecb0eac1256ba0e03775f24514da",
        "author": {
          "name": "First Last",
          "githubLogin": "user1",
          "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
        }
      },
      "version": 1,
      "latestVersion": 0,
      "requestedBy": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
      }
    },
    {
      "info": {
        "kind": "Pupdate",
        "startTime": 1624932999,
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
        "result": "succeeded",
        "endTime": 1624933003,
        "version": 1,
        "resourceChanges": {
          "create": 3
        }
      },
      "updateID": "9a6ffbb0-cb82-420f-824a-efac39ac91c8",
      "githubCommitInfo": {
        "slug": "pulumi/examples",
        "sha": "35caae8d73c3ecb0eac1256ba0e03775f24514da",
        "url": "https://github.com/pulumi/examples/commit/35caae8d73c3ecb0eac1256ba0e03775f24514da",
        "author": {
          "name": "First Last",
          "githubLogin": "user1",
          "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
        }
      },
      "version": 1,
      "latestVersion": 0,
      "requestedBy": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
      }
    },
    {
      "info": {
        "kind": "Pupdate",
        "startTime": 1624933009,
        "message": "triggered by pr #13",
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
        "result": "succeeded",
        "endTime": 1624933012,
        "version": 1,
        "resourceChanges": {
          "create": 3
        }
      },
      "updateID": "4c51a52c-6344-4664-8698-02e068060e5a",
      "githubCommitInfo": {
        "slug": "pulumi/examples",
        "sha": "35caae8d73c3ecb0eac1256ba0e03775f24514da",
        "url": "https://github.com/pulumi/examples/commit/35caae8d73c3ecb0eac1256ba0e03775f24514da",
        "author": {
          "name": "First Last",
          "githubLogin": "user1",
          "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
        }
      },
      "version": 1,
      "latestVersion": 0,
      "requestedBy": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
      }
    }
  ],
  "itemsPerPage": 10,
  "total": 4
}
```

<!-- ###################################################################### -->

## Organizations

<!-- ###################################################################### -->

### List Users

{{% notes "info" %}}
In the response data `githubLogin` is synonymous with `username` and does not necessarily mean the user is from a GitHub-backed organization.

`knownToPulumi` and `virtualAdmin` are internal implementation details that should not be referenced by an end user.
{{% /notes %}}

```
GET /api/orgs/{organization}/members?type=backend
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `type` | string | query | must be set to `backend` |
| `continuationToken` | string | query | **Optional.** the continuation token to use for retrieving the next set of results if results were truncated |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/orgs/{organization}/members?type=backend
```

#### Default response

```
Status: 200 OK
```

```
{
  "members": [
    {
      "role": "member",
      "user": {
        "name": "First Last",
        "githubLogin": "user2",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300",
        "email": "user@example.com"
      },
      "knownToPulumi": true,
      "virtualAdmin": false
    },
    {
      "role": "admin",
      "user": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300",
        "email": "admin@example.com"
      },
      "knownToPulumi": true,
      "virtualAdmin": false
    }
  ]
}
```

<!-- ###################################################################### -->

### Add User to Organization

User must have already signed up for a Pulumi account and meet the [organization membership requirements]({{< relref "/docs/intro/pulumi-service/organizations#organization-types" >}}) to be added to the organization, otherwise a 4xx error will occur.

If you want to provision SSO/SAML users, please refer to the [SCIM 2.0 Integration]({{< relref "/docs/guides/scim" >}}) documentation.

```
POST /api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `username` | string | path | user name |
| `role` | string | body | The role to assign - possible values are `admin` or `member` |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request POST \
  --data '{"role":"{role}"}' \
  https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

### Remove User from Organization

```
DELETE /api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `username` | string | path | user name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Default response

```
Status: 200 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

### Create Team

{{% notes "info" %}}
For GitHub-backed organizations the `teamType` path parameter must be `github`. For all other organization types the `teamType` path parameter must be `pulumi`.
{{% /notes %}}

```
POST /api/orgs/{org}/teams/{teamType}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `teamType` | string | path | the type of team to create - valid options are `pulumi` or `github` |
| `name` | string | body | team name |
| `displayName` | string | body | **Optional.** team display name |
| `description` | string | body | **Optional.** team description |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request POST \
  --data '{"name":"example-team","displayName":"example display name","description":"example description"}' \
  https://api.pulumi.com/api/orgs/{org}/teams/pulumi
```

#### Default response

```
Status: 200 OK
```

```
{
  "kind": "pulumi",
  "name": "example-team",
  "displayName": "example display name",
  "description": "example description",
  "members": [
    {
      "name": "First Last",
      "githubLogin": "user1",
      "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
    }
  ]
}
```

<!-- ###################################################################### -->

### Delete Team

```
DELETE /api/orgs/{org}/teams/{teamName}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `teamName` | string | path | team name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{org}/teams/{teamName}
```

#### Default response

```
Status: 200 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

### Update Team Membership

{{% notes "info" %}}

- For [GitHub-backed organizations]({{< relref "docs/intro/pulumi-service/teams#github-based-teams" >}}), this operation cannot be used as membership is managed on GitHub.
- For [SCIM managed teams]({{< relref "/docs/guides/scim" >}}), this operation cannot be used as membership is managed via the SSO provider.

{{% /notes %}}

```
PATCH /api/orgs/{organization}/teams/{team}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `team` | string | path | team name |
| `memberAction` | string | body | The action for the user and team - possible values are `add` or `remove` |
| `member` | string | body | user name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request POST \
  --data '{"memberAction":"{memberAction}","member":"{username}"}' \
  https://api.pulumi.com/api/orgs/{organization}/teams/{team}
```

#### Default response

```
Status: 200 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

### Grant Stack Access to Team

```
PATCH /api/orgs/{organization}/teams/{team}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `team` | string | path | team name |
| `addStackPermission` | object | body | object specifying stack and permissions - see following parameters |
| `addStackPermission .projectName` | string | object | project name |
| `addStackPermission .stackName` | string | object | stack name |
| `addStackPermission .permission` | integer | object | number representing stack permissions: 101 (read), 102 (edit), 103 (admin) |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request PATCH \
  --data '{"addStackPermission":{"projectName":"{projectName}","stackName":"{stackName}","permission": {permission}}}' \
  https://api.pulumi.com/api/orgs/{organization}/teams/{team}
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

### Remove Stack Access from Team

```
PATCH /api/orgs/{organization}/teams/{team}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `team` | string | path | team name |
| `removeStack` | object | body | object specifying stack and permissions - see following parameters |
| `removeStack .projectName` | string | object | project name |
| `removeStack .stackName` | string | object | stack name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request PATCH \
  --data '{"removeStack":{"projectName":"{projectName}","stackName":"{stackName}"}}' \
  https://api.pulumi.com/api/orgs/{organization}/teams/{team}
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

### Update User's Role

```
PATCH /api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | query | organization name to filter stacks by |
| `username` | string | path | user name |
| `role` | string | body | The role to assign - possible values are `admin` or `member` |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request PATCH \
  --data '{"role":"{role}"}' \
  https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Default response

```
Status: 200 OK
```

```
EMPTY RESPONSE BODY
```

<!-- ###################################################################### -->

### List User Access Tokens

```
GET /api/user/tokens
```

#### Parameters

None

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/user/tokens
```

#### Default response

```
Status: 200 OK
```

```
{
  "tokens": [
    {
      "id": "b02514e2-ddf6-41dc-8e16-6abf3914e68f",
      "description": "Generated by pulumi login on workstation at 20 May 21 12:04 EDT",
      "lastUsed": 1627590233
    },
    {
      "id": "ad9f7508-493a-4fbe-9918-62f1f71a53f8",
      "description": "cicd-server",
      "lastUsed": 1606860942
    }
  ]
}
```

<!-- ###################################################################### -->

### Create User Access Token

```
POST /api/user/tokens
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `description` | string | body | Descripton of the access token |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request POST \
  --data '{"description":"{description}"}' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/tags
```

#### Default response

```
Status: 204 OK
```

```
{
  "id": "74529ccd-27c0-40f7-bc4a-589f145ba67f",
  "tokenValue": "pul-75a564ac7f3a48079a0c448c1e1ec95c4cfed141"
}
```

<!-- ###################################################################### -->

### Delete User Access Token

```
DELETE /api/user/tokens/{tokenId}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `tokenId` | string | path | the token identifier |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request DELETE \
  https://api.pulumi.com/api/user/tokens/{tokenId}
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

### Create Webhook

```
POST /api/orgs/{organization}/hooks
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `active` | boolean | body | enable webhook |
| `displayName` | string | body | name of webhook |
| `organizationName` | string | body | organization name |
| `payloadUrl` | string | body | URL to send request to |
| `secretName` | string | body | **Optional.** secret used as the HMAC key. See [webhook docs]({{< relref "/docs/intro/pulumi-service/webhooks#headers" >}}) for more information  |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request POST \
  --data '{"organizationName":"{organization}","displayName":"My Webhook","payloadUrl":"https://example.com","secret":"mysecret","active":true}' \
  https://api.pulumi.com/api/orgs/{organization}/hooks
```

#### Default response

```
Status: 201 CREATED
```

```
{
  "organizationName":"demo",
  "name":"bd7e0a35",
  "displayName":"My Webhook",
  "payloadUrl":"https://example.com",
  "active":true
}
```

### List Webhooks

```
GET /api/orgs/{organization}/hooks
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name|

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/orgs/{organization}/hooks
```

#### Default response

```
[
  {
    "organizationName":"{organization}",
    "name":"4e662b3b",
    "displayName":"MyWebhook",
    "payloadUrl":"http://example.com",
    "active":true
  },
  {
    "organizationName":"{organization}",
    "name":"7732dd4c",
    "displayName":"My secret webhook",
    "payloadUrl":"https://example.com",
    "active":true
  }
]
```

### Get Webhook

```
GET /api/orgs/{organization}/hooks/{webhookname}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `webhookname` | string | path | webhook name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/orgs/{organization}/hooks/{webhookname}
```

#### Default response

```
Status: 200 OK
```

```
{
  "organizationName":"{organization}",
  "name":"{webhookname}",
  "displayName":"My Webhook",
  "payloadUrl":"http://example.com",
  "active":true
}
```

### Delete Stack

```
DELETE /api/stacks/{organization}/{project}/{stack}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `webhookname` | string | path | webhook name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request DELETE \
  https://api.pulumi.com/api/orgs/{organization}/hooks/{webhookname}
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

### Ping Webhook

```
POST /api/orgs/{organization}/hooks/{webhookname}/ping
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `webhookname` | string | path | webhook name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --request POST \
  https://api.pulumi.com/api/orgs/{organization}/hooks/ping
```

#### Default response

```
Status: 200 OK
```

```
{
  "id":"ea01abd2-90b4-4670-acce-15cc019ed6e4",
  "kind":"ping",
  "payload":"{\"timestamp\":1632735487,\"message\":\"🍹 Just a friendly ping from Pulumi 🍹\"}","timestamp":1632735487,"duration":196,"requestUrl":"{webhookurl}",
  "requestHeaders":"Content-Type: application/json\r\nPulumi-Webhook-Id: ea01abd2-90b4-4670-acce-15cc019ed6e4\r\nPulumi-Webhook-Kind: ping\r\n",
  "responseCode":200,
  "responseHeaders":"{headersfromwebhook}",
  "responseBody":"OK"
}
```

### List Webhooks Deliveries

```
GET /api/orgs/{organization}/hooks/{webhookname}/deliveries
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name|
| `webhookname` | string | path | webhook name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  https://api.pulumi.com/api/orgs/{organization}/hooks/{webhookname}/deliveries
```

#### Default response

```
[
  {
    "id":"ea01abd2-90b4-4670-acce-15cc019ed6e4",
    "kind":"ping",
    "payload":"{\"timestamp\":1632735487,\"message\":\"🍹 Just a friendly ping from Pulumi 🍹\"}","timestamp":1632735487,"duration":196,"requestUrl":"{webhookurl}",
    "requestHeaders":"Content-Type: application/json\r\nPulumi-Webhook-Id: ea01abd2-90b4-4670-acce-15cc019ed6e4\r\nPulumi-Webhook-Kind: ping\r\n",
    "responseCode":200,
    "responseHeaders":"{headersfromwebhook}",
    "responseBody":"OK"
  }
]
```

## Audit Logs

<!-- ###################################################################### -->

### Get Audit Log Events (JSON)

```
GET /api/orgs/{organization}/auditlogs
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `startTime` | unix timestamp | query | return results that occur after this timestamp |
| `userFilter` | string | query | **Optional.** username (e.g. `user1`) to filter results by |
| `continuationToken` | string | query | **Optional.** the continuation token to use for retrieving the next set of results if results were truncated |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
  --compressed \
  https://api.pulumi.com/api/orgs/{organization}/auditlogs?startTime=1615872240
```

#### Default response

```
Status: 200 OK
```

```
{
    "continuationToken": "1615413365",
    "auditLogEvents": [
        {
            "timestamp": 1615413432,
            "sourceIP": "10.0.0.1",
            "event": "Stack Update Started",
            "description": "Started update \"6f93fd86-b972-4402-9952-264c81639794\" for stack \"project1/dev\"",
            "user": {
                "name": "First Last",
                "githubLogin": "user1",
                "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
            }
        },
        {
            "timestamp": 1615413365,
            "sourceIP": "10.0.0.1",
            "event": "Stack Exported",
            "description": "Exported stack project1/dev",
            "user": {
                "name": "First Last",
                "githubLogin": "user1",
                "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
            }
        },
        {
            "timestamp": 1615413365,
            "sourceIP": "10.0.0.1",
            "event": "Stack Update Started",
            "description": "Started update \"da85cf90-4c7b-4dc4-9286-6ca58b4196e3\" for stack \"project1/dev\"",
            "user": {
                "name": "First Last",
                "githubLogin": "user1",
                "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
            }
        }
    ]
}
```

<!-- ###################################################################### -->

### Export Audit Log Events (CSV or CEF)

{{% notes "info" %}}
This API endpoint differs from other endpoints in the following ways:

- The response data is _always_ gzip compressed.
- The `Content-Type: application/json` header is omitted.

{{% /notes %}}

```
GET /api/orgs/{organization}/auditlogs/export
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `startTime` | unix timestamp | query | return results that occur after this timestamp |
| `userFilter` | string | query | **Optional.** username (e.g. `user1`) to filter results by |
| `format` | string | query | **Optional.** the response format to return - possible values are `cef` or `csv` (default) |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+8' \
  -H 'Authorization: token $PULUMI_ACCESS_TOKEN' \
  --compressed \
  https://api.pulumi.com/api/orgs/{organization}/auditlogs/export?startTime=1615872240&format=cef
```

#### Default response

```
Status: 200 OK
```

```
Timestamp,Name,Login,Event,Description,SourceIP,RequireOrgAdmin,RequireStackAdmin,AuthenticationFailure
2021-04-11T23:51:45Z,First Last,user1,Member Role Changed,"Changed organization role for ""user2"" to admin",192.168.10.11,true,false,false
2021-04-11T23:09:36Z,First Last,user1,Member Role Changed,"Changed organization role for ""user2"" to admin",192.168.10.11,true,false,false
2021-04-11T23:09:25Z,First Last,user1,Member Role Changed,"Changed organization role for ""user3"" to admin",192.168.10.11,true,false,false
2021-04-11T21:09:52Z,First Last,user1,Secret Decrypted,"Decrypted secret value for stack ""demo-aws-ts-webserver/dev-user1"" (cipher text suffix: ""tbpiX4c="")",192.168.10.11,false,false,false
```
