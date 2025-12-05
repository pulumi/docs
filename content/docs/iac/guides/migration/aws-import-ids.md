---
title_tag: "Finding AWS import IDs and special cases"
meta_desc: Learn how to find AWS resource IDs and handle CloudFormation-specific edge cases when importing resources into Pulumi.
title: AWS import IDs and special cases
h1: "Finding AWS import IDs and special cases"
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
    - /docs/iac/guides/migration/migrating-to-pulumi/aws-import-ids/
menu:
    iac:
        name: Finding AWS import IDs
        parent: iac-guides-migration
        weight: 3
---

This guide explains how to discover the correct AWS resource IDs to use when importing existing CloudFormation- or CDK-managed resources into Pulumi, and calls out CloudFormation features that require special handling.

## Finding Resource IDs

Every import requires a resource ID. Whether you are running `pulumi import` for a single resource or using a bulk `import.json` file (for example, generated with `pulumi preview --import-file import.json`), you need to supply an ID value that uniquely identifies the existing AWS resource. Sometimes this is a single value like a resource `ARN`, but other times it is a composite id made up of a combination of property values. For example, to import a Lambda Permission resource you need the `functionName` and the Permission `id` and it needs to be in the format `functionName|id`.

The first place you should start is the ids from the CloudFormation stack. Most of the time the values for the import ids can be extracted from the `PhysicalResourceId` in the CloudFormation stack.

```console
$ aws cloudformation list-stack-resources --stack-name my-stack \
    --query 'StackResourceSummaries[].{Type:ResourceType,LogicalResourceId:LogicalResourceId,Physical:PhysicalResourceId}'
```

Optionally, you can use the `cdk2pulumi` tool to lookup information on the import ids. It has an `ids` subcommand that returns information on the expected import id format. For example:

```console
$ pulumi plugin run cdk2pulumi -- ids AWS::Lambda::Permission
Resource: aws-native:lambda:Permission (CFN: AWS::Lambda::Permission, provider: aws-native)
Format: {functionName}|{id}
Parts:
  - functionName (Input): The name or ARN of the Lambda function, version, or alias.
  **Name formats**
 +  *Function name* – ``my-function`` (name-only), ``my-function:v1`` (with alias).
  +  *Function ARN* – ``arn:aws:lambda:us-west-2:123456789012:function:my-function``.
  +  *Partial ARN* – ``123456789012:function:my-function``.

 You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
  - id (Output)
```

### Finding IDs Example

Lets walk through an example of finding the import ids for a couple of resources.

**1\. List the stack resources**

```console
$ aws cloudformation list-stack-resources --stack-name test-app-dev \
    --query 'StackResourceSummaries[].{ResourceType:ResourceType,LogicalResourceId:LogicalResourceId,PhysicalResourceId:PhysicalResourceId}'
[
    {
        "ResourceType": "AWS::ApiGatewayV2::Api",
        "LogicalResourceId": "Api48B32C1D",
        "PhysicalResourceId": "uzelpdmlxi"
    },
    {
        "ResourceType": "AWS::ApiGatewayV2::Stage",
        "LogicalResourceId": "ApiDefaultStageB9B75A7A",
        "PhysicalResourceId": "$default"
    },
    {
        "ResourceType": "AWS::ApiGatewayV2::Route",
        "LogicalResourceId": "ApiGEThelloF5F722C0",
        "PhysicalResourceId": "2kaoey7"
    },
    {
        "ResourceType": "AWS::ApiGatewayV2::Integration",
        "LogicalResourceId": "ApiGEThellointegration392349BE",
        "PhysicalResourceId": "qwo3s38"
    }
]

```

**2\. Find the import id format for each**

```console
$ pulumi plugin run cdk2pulumi -- ids AWS::ApiGatewayV2::Api
Resource: aws-native:apigatewayv2:Api (CFN: AWS::ApiGatewayV2::Api, provider: aws-native)
Format: {apiId}
Parts:
  - apiId (Output): The API identifier.

pulumi plugin run cdk2pulumi -- ids AWS::ApiGatewayV2::Stage
Resource: aws:apigatewayv2/stage:Stage (CFN: AWS::ApiGatewayV2::Stage, provider: aws)
Format: {apiId}/{name}
Parts:
  - apiId (Segment)
  - name (Segment)
Import doc: to import `aws_apigatewayv2_stage` using the API identifier and stage name.//{  to = aws_apigatewayv2_stage.example  id = "aabbccddee/example-stage"}

pulumi plugin run cdk2pulumi -- ids AWS::ApiGatewayV2::Route
Resource: aws-native:apigatewayv2:Route (CFN: AWS::ApiGatewayV2::Route, provider: aws-native)
Format: {apiId}|{routeId}
Parts:
  - apiId (Input): The API identifier.
  - routeId (Output): The route ID.

pulumi plugin run cdk2pulumi -- ids AWS::ApiGatewayV2::Integration
Resource: aws-native:apigatewayv2:Integration (CFN: AWS::ApiGatewayV2::Integration, provider: aws-native)
Format: {apiId}|{integrationId}
Parts:
  - apiId (Input): The API identifier.
  - integrationId (Output): The integration ID.
```

Typically if the import id consists of a single value (e.g. `apiId` in the Api example) then it will be the `PhysicalResourceId` from CloudFormation. Similarly if it is a composite id where one of the values refers to the `id`, or `name` of itself (e.g. `routeId` of the Route resource) then this will also typically be the `PhyscialResourceId`.

We would then update the `id`s in the bulk import file based on the format and values.

```json
{
  "resources": [
    {
      "type": "aws-native:apigatewayv2:Api",
      "name": "Api48B32C1D",
      "id": "uzelpdmlxi"
    },
    {
      "type": "aws-native:apigatewayv2:Integration",
      "name": "ApiGEThellointegration392349BE",
      "id": "uzelpdmlxi|qwo3s38"
    },
    {
      "type": "aws-native:apigatewayv2:Route",
      "name": "ApiGEThelloF5F722C0",
      "id": "uzelpdmlxi|2kaoey7"
    },
    {
      "type": "aws:apigatewayv2/stage:Stage",
      "name": "ApiDefaultStageB9B75A7A",
      "id": "uzelpdmlxi/$default"
    }
  ]
}
```

### Looking up Resource IDs

Sometimes part of the resource ID is not a `PhysicalResourceId`. In these cases it is necessary to perform AWS API calls to look up the necessary information.

```console
$ aws cloudformation list-stack-resources --stack-name test-app-dev \
    --query 'StackResourceSummaries[].{ResourceType:ResourceType,Logical:LogicalResourceId,PhysicalResourceId:PhysicalResourceId}'
[
    {
        "ResourceType": "AWS::EC2::EIP",
        "LogicalResourceId": "VpcPublicSubnet1EIPD7E02669",
        "PhysicalResourceId": "3.150.255.6"
    },
    {
        "ResourceType": "AWS::ApplicationAutoScaling::ScalingPolicy",
        "LogicalResourceId": "StorageDynamoTableReadScalingTargetTrackingDB061E27",
        "PhysicalResourceId": "arn:aws:autoscaling:us-east-2:12345678910:scalingPolicy:c54f759a-aa04-4c0e-afbc-d45a960593a4:resource/dynamodb/table/Example-Dev-StorageDynamoTable201FACD8-1KCPDDFW2WLP6:policyName/ExampleDevStorageDynamoTableReadScalingTargetTrackingDE82FE6D"
    }
]

```

If we look up the information on these two resources we will see these are not as straightforward as the previous examples.

```console
$ pulumi plugin run cdk2pulumi -- ids AWS::ApplicationAutoScaling::ScalingPolicy
Resource: aws-native:applicationautoscaling:ScalingPolicy (CFN: AWS::ApplicationAutoScaling::ScalingPolicy, provider: aws-native)
Format: {arn}|{scalableDimension}
Parts:
  - arn (Output): Returns the ARN of a scaling policy.
  - scalableDimension (Input): The scalable dimension. This string consists of the service namespace, resource type, and scaling property.
  +  ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
  +  ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
  +  ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
  +  ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
  + ... # truncated for brevity

pulumi plugin run cdk2pulumi -- ids AWS::EC2::EIP
Resource: aws-native:ec2:Eip (CFN: AWS::EC2::EIP, provider: aws-native)
Format: {publicIp}|{allocationId}
Parts:
  - publicIp (Output): The Elastic IP address.
  - allocationId (Output): The ID that AWS assigns to represent the allocation of the address for use with Amazon VPC. This is returned only for VPC elastic IP addresses. For example, `eipalloc-5723d13e` .

```

Starting with the `ScalingPolicy` resource we can see that we need the `arn` which matches the `PhysicalResourceId`, but we also need the `scalableDimension` which is not in the CloudFormation data. Based on the information provided from the `ids` command we might be able to look at that CloudFormation resource and figure out which `scalableDimension` to use, otherwise we can use the `cloudcontrol` CLI commands. The `aws cloudcontrol list-resources` command will list all the resources of that type, which we can filter using `jq` to only include entries that have the part of the identifier that we know.

```console
$ aws cloudcontrol list-resources --type-name AWS::ApplicationAutoScaling::ScalingPolicy --resource-model '{"ServiceNamespace": "dynamodb"}' --profile dev-admin | jq '.ResourceDescriptions[] | select(.Identifier | contains("arn:aws:autoscaling:us-east-2:12345678910:scalingPolicy:c54f759a-aa04-4c0e-afbc-d45a960593a4:resource/dynamodb/table/Example-Dev-StorageDynamoTable201FACD8-1KCPDDFW2WLP6:policyName/ExampleDevStorageDynamoTableReadScalingTargetTrackingDE82FE6D")) | .Identifier'

"arn:aws:autoscaling:us-east-2:12345678910:scalingPolicy:c54f759a-aa04-4c0e-afbc-d45a960593a4:resource/dynamodb/table/Example-Dev-StorageDynamoTable201FACD8-1KCPDDFW2WLP6:policyName/ExampleDevStorageDynamoTableReadScalingTargetTrackingDE82FE6D|dynamodb:table:ReadCapacityUnits"


```

The `EIP` resource is an example of a resource which has an id containing a value that cannot be determined by either the CloudFormation data or the template. It requires the `publicIp`, which we have, and the `allocationId` which we do not. We can use the same `aws cloudcontrol list-resources` command to find the correct identifier.

```console
$ aws cloudcontrol list-resources --type-name AWS::EC2::EIP --profile dev-admin | jq '.ResourceDescriptions[] | select(.Identifier | contains("3.150.255.6")) | .Identifier'

"3.150.255.6|eipalloc-0a79aa2cb81750a49"
```
