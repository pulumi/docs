---
title: "Pulumi Service API"
meta_desc: An overview of the Pulumi Service API for querying Organization, Stack, State, etc. information
---

The Pulumi Service API is used by the Pulumi CLI and the Pulumi Console to query and interact with state information, history, stack tags, etc. This API is available for end users to integrate into their own automation use cases.

{{% notes "info" %}}
While the Pulumi Service API is used by the Pulumi CLI and Pulumi Console, Pulumi makes no guarantees about changes that might affect backwards compatibility or cause breaking changes.
{{% /notes %}}

## Authentication

All requests must be authenticated using a token via the `Authorization` HTTP header. If the token is missing or invalid, the Pulumi Service API will return a 4xx status code.

The `Authorization` header must be in the form below with the literal string `token`, then a space, then your access token value.

```
Authorization: token {token}
```

{{% notes "info" %}}
As of June 28, 2019, Pulumi access tokens contain the prefix `pul-`, which should be included as part of the token value in the header.
{{% /notes %}}

To view your access tokens, or create a new one manually, view the <a href="https://app.pulumi.com/account/tokens" target="_blank">Access Tokens</a> page. You will see a list of past tokens, when they were last used, as well as the ability to revoke them.

## Required Request Headers

TODO: Add more info.

```
Accept: application/vnd.pulumi+3
Content-Type: application/json
```

<!-- ###################################################################### -->

## Stacks

### List Stacks

```
GET https://api.pulumi.com/api/user/stacks
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | query | organization name to filter stacks by |
| `project` | string | query | organization name to filter stacks by |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
  https://api.pulumi.com/api/user/stacks
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
  ]
}
```

### Get Stack

```
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}
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
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
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

### Get Stack State

```
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/export
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
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
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

## Stack Updates

### List Stack Updates

```
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/updates
```

By default the results are not paginated. You can specify `page` and `pageSize` query parameters to paginate the results.
> `?pageSize=1&page=1` can be used to return only the most recent update.

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `project` | string | path | project name |
| `stack` | string | path | stack name |
| `page` | number | query | page of the results to return |
| `pageSize` | number | query | number of results per page |
| `output-type` | number | query | the response format to return - possible values are `service` or `cli` (default) |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
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

### Get Update Status

```
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/update/{updateID}
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
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
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

### List Update Events

```
GET https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/update/{updateID}/events
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
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
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

## Organizations

### Add User to Organization

Users are not just-in-time provisioned. They must sign in to the Pulumi console first (they will receive an error that they're not a member) and then they can be added to the organization.

TODO: Add note about SAML.

```
POST https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `username` | string | path | user name |
| `role` | string | body | **Required.** The role to assign - possible values are `admin` or `member` |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
  --request POST \
  --data '{ "role": "{role}" }' \
  https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Default response

```
Status: 204 OK
```

```
EMPTY RESPONSE BODY
```

### Remove User from Organization

```
DELETE https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `username` | string | path | user name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
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

### Create Team

TODO: Add note about different backends
TODO: what is `/pulumi`

```
POST https://api.pulumi.com/api/orgs/{org}/teams/pulumi
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `name` | string | body | **Required.** team name |
| `displayName` | string | body | team display name |
| `description` | string | body | team description |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
  --request POST \
  --data '{ "name": "example-team", "displayName": "example display name", "description": "example description" }' \
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

### Delete Team

```
DELETE https://api.pulumi.com/api/orgs/{org}/teams/{teamName}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `teamName` | string | path | team name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
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

### Update Team Membership

```
PATCH https://api.pulumi.com/api/orgs/{organization}/teams/{team}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `team` | string | path | team name |
| `memberAction` | string | body | **Required.** The action for the user and team - possible values are `add` or `remove` |
| `member` | string | body | **Required.** user name |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
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

### Update User's Role

```
PATCH https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | query | organization name to filter stacks by |
| `username` | string | path | user name |
| `role` | string | body | **Required.** The role to assign - possible values are `admin` or `member` |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
  --request PATCH \
  --data '{ "role": "{role}" }' \
  https://api.pulumi.com/api/orgs/{organization}/members/{username}
```

#### Default response

```
Status: 200 OK
```

```
EMPTY RESPONSE BODY
```

### Get Audit Log Events

TODO: Add `.../auditlogs/export` endpoint with `csv` and `cef` formats

```
GET https://api.pulumi.com/api/orgs/{organization}/auditlogs
```

#### Parameters

| Parameter | Type | In | Description |
| --------- | ---------- | ---------- | ---------- |
| `organization` | string | path | organization name |
| `startTime` | unix timestamp | query | return results that occur after this timestamp |

#### Example

```bash
curl \
  -H 'Accept: application/vnd.pulumi+3' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token pul-abcdefghijklmnopqrstuvwxyz' \
  https://api.pulumi.com/api/orgs/{organization}/auditlogs?1615872240
```

#### Default response

```
Status: 200 OK
```

```
{
  "continuationToken": "1615413886",
  "auditLogEvents": [
    {
      "timestamp": 1615875715,
      "sourceIP": "1.1.1.1",
      "event": "Member Role Changed",
      "description": "Changed organization role for \"user2\" to member",
      "user": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
      },
      "reqOrgAdmin": true
    },
    {
      "timestamp": 1615874593,
      "sourceIP": "1.1.1.1",
      "event": "Stack Exported",
      "description": "Exported stack demo-aws-ts-webserver/dev-user1",
      "user": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
      }
    },
    {
      "timestamp": 1615874593,
      "sourceIP": "1.1.1.1",
      "event": "Stack Update Started",
      "description": "Started update \"398fe477-6c03-4c29-9348-beddbc5b34e7\" for stack \"demo-aws-ts-webserver/dev-user1\"",
      "user": {
        "name": "First Last",
        "githubLogin": "user1",
        "avatarUrl": "https://en.gravatar.com/userimage/17756222/cabc55626abae89ebe2d8ae946521e15.png?size=300"
      }
    }
  ]
}
```
