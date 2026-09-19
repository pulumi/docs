---
title_tag: "Finding AWS import IDs and special cases"
meta_desc: Learn how to find AWS resource IDs and handle CloudFormation-specific edge cases when importing resources into Pulumi.
title: AWS import IDs and special cases
h1: "Finding AWS import IDs and special cases"
aliases:
    - /docs/iac/guides/migration/migrating-to-pulumi/aws-import-ids/
menu:
    iac:
        name: Finding AWS import IDs
        parent: iac-guides-migration
        weight: 3
---

This guide explains how to discover the correct AWS resource IDs to use when importing existing CloudFormation- or CDK-managed resources into Pulumi, and calls out CloudFormation features that require special handling.

## About Pulumi import

The [`pulumi import`](/docs/iac/cli/commands/pulumi_import/) command allows you to bring a resource created outside of Pulumi under Pulumi management. This includes resources created by clicking in the AWS Console, or by other infrastructure as code tools such as Terraform, CloudFormation, and AWS CDK. Each resource to be imported requires a resource ID, along with a name for the resource, and its type. For the import workflows themselves, see [Importing resources](/docs/iac/guides/migration/import/).

## Finding resource IDs

Whether you are running `pulumi import` for a single resource or using a bulk `import.json` file (for example, generated with [`pulumi preview --import-file import.json`](/docs/iac/cli/commands/pulumi_preview/)), you need to supply an ID that uniquely identifies the existing AWS resource. Sometimes this ID is a single value such as a resource `ARN`, and sometimes a composite value made up of several property values. For example, importing a [Lambda Permission](https://www.pulumi.com/registry/packages/aws/api-docs/lambda/permission/) resource requires both the `functionName` and the Permission `id`, and the ID passed to `pulumi import` must be in the format `functionName|id`.

The first place to look for import IDs is the CloudFormation stack itself. Import IDs for most Pulumi resource types can be extracted from the `PhysicalResourceId` property in CloudFormation:

```bash
$ aws cloudformation list-stack-resources --stack-name my-stack \
    --query 'StackResourceSummaries[].{Type:ResourceType,LogicalResourceId:LogicalResourceId,Physical:PhysicalResourceId}'
```

You can also use the `cdk2pulumi` tool to look up information about import IDs. `cdk2pulumi` has an `ids` subcommand that returns the expected import ID format:

```bash
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

### Finding IDs example

The following example walks through finding the import IDs for the resources in a CloudFormation stack.

1. List the stack resources:

    ```bash
    $ aws cloudformation list-stack-resources --stack-name test-app-dev \
        --query 'StackResourceSummaries[].{ResourceType:ResourceType,LogicalResourceId:LogicalResourceId,PhysicalResourceId:PhysicalResourceId}'
    [output]
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

1. Find the import id format for each:

    ```bash
    $ pulumi plugin run cdk2pulumi -- ids AWS::ApiGatewayV2::Api
    [output]
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

    $ pulumi plugin run cdk2pulumi -- ids AWS::ApiGatewayV2::Route
    [output]
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

When the import ID consists of a single value (for example, `apiId` in the Api example), that value is typically the `PhysicalResourceId` from CloudFormation. A composite ID whose parts include the resource's own `id` or `name` (for example, `routeId` of the Route resource) typically takes that part from the `PhysicalResourceId` as well.

Next, update the `id`s in the bulk import file based on the formats and values you found:

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

### Looking up resource IDs

For some resource types, the resource ID may not be the value of its `PhysicalResourceId` in CloudFormation. In these cases, you must call the AWS API to look up the information you need:

```bash
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

Looking up the information for these two resources shows that they are not as straightforward as the previous examples.

```bash
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

Starting with the `ScalingPolicy` resource, the `arn` matches the `PhysicalResourceId`, but the `scalableDimension` is not in the CloudFormation data. The output of the `ids` command may be enough to determine which `scalableDimension` that CloudFormation resource uses; otherwise, use the `cloudcontrol` CLI commands. The `aws cloudcontrol list-resources` command lists all the resources of that type, and you can filter it with `jq` to include only entries containing the part of the identifier you already know.

```bash
$ aws cloudcontrol list-resources --type-name AWS::ApplicationAutoScaling::ScalingPolicy --resource-model '{"ServiceNamespace": "dynamodb"}' --profile dev-admin | jq '.ResourceDescriptions[] | select(.Identifier | contains("arn:aws:autoscaling:us-east-2:12345678910:scalingPolicy:c54f759a-aa04-4c0e-afbc-d45a960593a4:resource/dynamodb/table/Example-Dev-StorageDynamoTable201FACD8-1KCPDDFW2WLP6:policyName/ExampleDevStorageDynamoTableReadScalingTargetTrackingDE82FE6D")) | .Identifier'

"arn:aws:autoscaling:us-east-2:12345678910:scalingPolicy:c54f759a-aa04-4c0e-afbc-d45a960593a4:resource/dynamodb/table/Example-Dev-StorageDynamoTable201FACD8-1KCPDDFW2WLP6:policyName/ExampleDevStorageDynamoTableReadScalingTargetTrackingDE82FE6D|dynamodb:table:ReadCapacityUnits"


```

The `EIP` resource has an ID containing a value that cannot be determined from either the CloudFormation data or the template. It requires the `publicIp`, which the stack resource listing provides, and the `allocationId`, which it does not. Use the same `aws cloudcontrol list-resources` command to find the correct identifier.

```bash
$ aws cloudcontrol list-resources --type-name AWS::EC2::EIP --profile dev-admin | jq '.ResourceDescriptions[] | select(.Identifier | contains("3.150.255.6")) | .Identifier'

"3.150.255.6|eipalloc-0a79aa2cb81750a49"
```
