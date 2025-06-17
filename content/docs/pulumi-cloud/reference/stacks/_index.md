---
title: Stacks
title_tag: "Pulumi Cloud REST API: Stacks"
meta_desc: Learn about the Pulumi Cloud REST API endpoints for creating, reading, updating, and deleting Pulumi stacks.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 24
---

The Stacks API allows you to create and manage Pulumi stacks, which are isolated, independently configurable instances of your Pulumi program.

## Stack Operations

The API provides endpoints for the following operations:

- Creating new stacks
- Listing available stacks with filtering options
- Getting stack details and metadata
- Accessing stack state and resources
- Transferring stacks between organizations
- Deleting stacks

## Create Stack

Creates a new stack in the Pulumi Cloud. If the project does not exist, it will also be created.

```plain
POST /api/stacks/{organization}/{project}
```

### Parameters

| Parameter      | Type   | In   | Description                                                                                      |
|----------------|--------|------|--------------------------------------------------------------------------------------------------|
| `organization` | string | path | Organization name                                                                                |
| `project`      | string | path | Name of the project to create the stack under. If the project doesn't exist, it will be created. |
| `stackName`    | string | body | Name of the stack being created.                                                                 |
| `config`       | object | body | Configuration of the stack being created - see following parameters                              |
| `config.environment` | string | body | **Optional.** The reference to the ESC environment to create for storing stack configuration. Must not exist yet. |
| `config.secretsProvider` | string | body | **Optional.** The stack's secrets provider.                                            |
| `config.encryptedKey` | string | body | **Optional.** The KMS-encrypted ciphertext for the data key used for secrets encryption. Only used for cloud-based secrets providers. |
| `config.encryptionSalt` | string | body | **Optional.** The stack's base64 encoded encryption salt. Only used for passphrase-based secrets providers. |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"stackName":"{stackName}"}' \
  https://api.pulumi.com/api/stacks/{organization}/{project}
```

## List Stacks

Lists stacks available to the authenticated user.

```plain
GET /api/user/stacks
```

### Parameters

| Parameter           | Type   | In    | Description                                                                                                  |
|---------------------|--------|-------|--------------------------------------------------------------------------------------------------------------|
| `organization`      | string | query | **Optional.** organization name to filter stacks by                                                          |
| `project`           | string | query | **Optional.** organization name to filter stacks by                                                          |
| `tagName`           | string | query | **Optional.** tag name to filter stacks by                                                                   |
| `tagValue`          | string | query | **Optional.** tag value to filter stacks by                                                                  |
| `continuationToken` | string | query | **Optional.** the continuation token to use for retrieving the next set of results if results were truncated |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/user/stacks?organization={organization}&tagName={tagName}&tagValue={tagValue}
```

### Default response

```plain
Status: 200 OK
```

```plain
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

## Get Stack

```plain
GET /api/stacks/{organization}/{project}/{stack}
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
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}
```

### Default response

```plain
Status: 200 OK
```

```plain
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

## Get Stack Downstream References

```plain
GET /api/stacks/{organization}/{project}/{stack}/downstreamreferences
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
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/downstreamreferences
```

### Default Response

```plain
Status: 200 OK
```

```plain
{
  "referencedStacks": [
    {
      "organization": "demo",
      "routingProject": "demo-aws-ts-webserver",
      "name": "dev-user1",
      "version": 3
    }
  ]
}
```

## Get Stack Metadata

```plain
GET /api/stacks/{organization}/{project}/{stack}/metadata
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
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/metadata
```

### Default Response

```plain
Status: 200 OK
```

```plain
{
  "orgName": "demo",
  "projectName": "demo-aws-ts-webserver",
  "stackName": "dev-user1",
  "userPermission": 103,
  "notificationSettings": {
    "notifyUpdateFailure": false,
    "notifyUpdateSuccess": false
  }
}
```

## Get Stack State

```plain
GET /api/stacks/{organization}/{project}/{stack}/export
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
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/export
```

### Default response

```plain
Status: 200 OK
```

```plain
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

## Get Stack Resource Count

```plain
GET /api/stacks/{organization}/{project}/{stack}/resources/count
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
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/resources/count
```

### Default response

```plain
Status: 200 OK
```

```plain
{
  "resourceCount": 2,
  "version": 5
}
```

## Get (Latest) Current Stack Resources

```plain
GET /api/stacks/{organization}/{project}/{stack}/resources/latest
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
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/resources/latest
```

### Default response

```
Status: 200 OK
```

```
{
  "resources": [
    {
      "resource": {
        "type": "pulumi:pulumi:Stack",
        "urn": "urn:pulumi:dev::prog-aws-typescript::pulumi:pulumi:Stack::prog-aws-typescript-dev",
        "custom": false,
        "delete": false,
        "dependencies": [],
        "outputs": {}
      }
    },
    {
      "resource": {
        "id": "my-bucket-a4a3a07",
        "type": "aws:s3/bucket:Bucket",
        "urn": "urn:pulumi:dev::prog-aws-typescript::aws:s3/bucket:Bucket::my-bucket",
        "custom": true,
        "delete": false,
        "dependencies": [],
        "parent": "urn:pulumi:dev::prog-aws-typescript::pulumi:pulumi:Stack::prog-aws-typescript-dev",
        "additionalSecretOutputs": [
          "tags"
        ],
        "inputs": {
          "__defaults": [
            "acl",
            "bucket",
            "forceDestroy"
          ],
          "acl": "private",
          "bucket": "my-bucket-a4a3a07",
          "forceDestroy": false,
          "tags": {
            "__defaults": [],
            "anyone-can-delete-me": "true",
            "owner": "my-pulumi-login"
          }
        },
        "outputs": {
          "accelerationStatus": "",
          "acl": "private",
          "arn": "arn:aws:s3:::my-bucket-a4a3a07",
          "bucket": "my-bucket-a4a3a07",
          "bucketDomainName": "my-bucket-a4a3a07.s3.amazonaws.com",
          "bucketRegionalDomainName": "my-bucket-a4a3a07.s3.amazonaws.com",
          "corsRules": [],
          "forceDestroy": false,
          "grants": [],
          "hostedZoneId": "Z3AQBSTGFYJSTF",
          "id": "my-bucket-a4a3a07",
          "lifecycleRules": [],
          "loggings": [],
          "objectLockConfiguration": null,
          "region": "us-east-1",
          "replicationConfiguration": null,
          "requestPayer": "BucketOwner",
          "serverSideEncryptionConfiguration": {
            "rule": {
              "applyServerSideEncryptionByDefault": {
                "kmsMasterKeyId": "",
                "sseAlgorithm": "AES256"
              },
              "bucketKeyEnabled": false
            }
          },
          "tags": {
            "4dabf18193072939515e22adb298388d": "1b47061264138c4ac30d75fd1eb44270",
            "ciphertext": "v1:4MBM2acrauXVfXK0:N6Bv7P+Zt27+pP+N9z+VHWllSYtqi9/K9HXQ7lkGRjGfdReLz5lW8QBpF3sLRFK8jvqf11SUy2ueBNBGd2MIgq8j6//305ZM1l0="
          },
          "tagsAll": {
            "anyone-can-delete-me": "true",
            "owner": "my-pulumi-login"
          },
          "versioning": {
            "enabled": false,
            "mfaDelete": false
          },
          "website": null
        },
        "providerInputs": {
          "region": "us-east-1",
          "version": "5.31.0"
        }
      }
    }
  ],
  "region": "us-east-1",
  "version": 5
}
```

## Get Stack Resources For Version

```plain
GET /api/stacks/{organization}/{project}/{stack}/resources/{version}
```

### Parameters

| Parameter      | Type   | In   | Description          |
|----------------|--------|------|----------------------|
| `organization` | string | path | organization name    |
| `project`      | string | path | project name         |
| `stack`        | string | path | stack name           |
| `version`      | number | path | stack update version |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/resources/{version}
```

### Default response

```
Status: 200 OK
```

```
{
  "resources": [
    {
      "resource": {
        "type": "pulumi:pulumi:Stack",
        "urn": "urn:pulumi:dev::prog-aws-typescript::pulumi:pulumi:Stack::prog-aws-typescript-dev",
        "custom": false,
        "delete": false,
        "dependencies": [],
        "outputs": {}
      }
    },
    {
      "resource": {
        "id": "my-bucket-a4a3a07",
        "type": "aws:s3/bucket:Bucket",
        "urn": "urn:pulumi:dev::prog-aws-typescript::aws:s3/bucket:Bucket::my-bucket",
        "custom": true,
        "delete": false,
        "dependencies": [],
        "parent": "urn:pulumi:dev::prog-aws-typescript::pulumi:pulumi:Stack::prog-aws-typescript-dev",
        "additionalSecretOutputs": [
          "tags"
        ],
        "inputs": {
          "__defaults": [
            "acl",
            "bucket",
            "forceDestroy"
          ],
          "acl": "private",
          "bucket": "my-bucket-a4a3a07",
          "forceDestroy": false,
          "tags": {
            "__defaults": [],
            "anyone-can-delete-me": "true",
            "owner": "my-pulumi-login"
          }
        },
        "outputs": {
          "accelerationStatus": "",
          "acl": "private",
          "arn": "arn:aws:s3:::my-bucket-a4a3a07",
          "bucket": "my-bucket-a4a3a07",
          "bucketDomainName": "my-bucket-a4a3a07.s3.amazonaws.com",
          "bucketRegionalDomainName": "my-bucket-a4a3a07.s3.amazonaws.com",
          "corsRules": [],
          "forceDestroy": false,
          "grants": [],
          "hostedZoneId": "Z3AQBSTGFYJSTF",
          "id": "my-bucket-a4a3a07",
          "lifecycleRules": [],
          "loggings": [],
          "objectLockConfiguration": null,
          "region": "us-east-1",
          "replicationConfiguration": null,
          "requestPayer": "BucketOwner",
          "serverSideEncryptionConfiguration": {
            "rule": {
              "applyServerSideEncryptionByDefault": {
                "kmsMasterKeyId": "",
                "sseAlgorithm": "AES256"
              },
              "bucketKeyEnabled": false
            }
          },
          "tags": {
            "4dabf18193072939515e22adb298388d": "1b47061264138c4ac30d75fd1eb44270",
            "ciphertext": "v1:4MBM2acrauXVfXK0:N6Bv7P+Zt27+pP+N9z+VHWllSYtqi9/K9HXQ7lkGRjGfdReLz5lW8QBpF3sLRFK8jvqf11SUy2ueBNBGd2MIgq8j6//305ZM1l0="
          },
          "tagsAll": {
            "anyone-can-delete-me": "true",
            "owner": "my-pulumi-login"
          },
          "versioning": {
            "enabled": false,
            "mfaDelete": false
          },
          "website": null
        },
        "providerInputs": {
          "region": "us-east-1",
          "version": "5.31.0"
        }
      }
    }
  ],
  "region": "us-east-1",
  "version": 2
}
```

## Transfer Stack

Transfers the stack from one organization in the Pulumi Cloud to a different organization. The user calling this operation must have the necessary [stack permissions](/docs/pulumi-cloud/projects-and-stacks#stack-permissions) for this operation to be successful.

This operation will return a 409 response error if an update is currently in progress.

```plain
POST /api/stacks/{organization}/{project}/{stack}/transfer
```

### Parameters

| Parameter      | Type   | In   | Description                                 |
|----------------|--------|------|---------------------------------------------|
| `organization` | string | path | organization name                           |
| `project`      | string | path | project name                                |
| `stack`        | string | path | stack name                                  |
| `toOrg`        | string | body | the organization to transfer the stack _to_ |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"toOrg":"{toOrg}"}' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/transfer
```

### Default response

```plain
Status: 204 OK
```

```plain
EMPTY RESPONSE BODY
```

## Delete Stack

```plain
DELETE /api/stacks/{organization}/{project}/{stack}
```

### Parameters

| Parameter      | Type    | In    | Description                                                             |
|----------------|---------|-------|-------------------------------------------------------------------------|
| `organization` | string  | path  | organization name                                                       |
| `project`      | string  | path  | project name                                                            |
| `stack`        | string  | path  | stack name                                                              |
| `force`        | boolean | query | flag indicating to delete the stack even if it still contains resources |

### Example

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request DELETE \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}
```

### Default response

```plain
Status: 204 OK
```

```plain
EMPTY RESPONSE BODY
```
