---
title_tag: "Migrating from Serverless Framework"
meta_desc: Migrate your Serverless Framework apps to Pulumi. Import existing resources and translate serverless.yml to Pulumi code.
title: Serverless Framework
h1: "Migrating from Serverless Framework to Pulumi"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Serverless Framework
        parent: iac-guides-migration-from
        weight: 6
aliases:
- /docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-serverless/
---

If your team has already provisioned infrastructure using the Serverless Framework, and you'd like to adopt Pulumi, you have several strategies you can take:

* **[Neo](/product/neo/) (Recommended)**: Since Serverless Framework deploys via CloudFormation, Neo can automatically convert your stacks and import existing resources with zero downtime
* [**Coexist**](#referencing-stack-outputs) with resources provisioned by the Serverless Framework by referencing CloudFormation stack outputs.
* [**Import**](#importing-existing-resources) existing resources into Pulumi.
* [**Rewrite**](#resource-mapping) your `serverless.yml` definitions as Pulumi code and incrementally migrate resources.

## How Serverless Framework uses CloudFormation

Every time you run `sls deploy`, the Serverless Framework generates a CloudFormation template and deploys it as a stack. The stack is named using the pattern `{service}-{stage}`, for example, `my-api-dev` or `my-api-prod`. This stack contains all the resources defined in your `serverless.yml`, including:

* Lambda functions and their execution roles
* API Gateway REST APIs or HTTP APIs
* Event source mappings (SQS, DynamoDB Streams, Kinesis)
* CloudWatch log groups
* Any resources you define in the `resources:` section (DynamoDB tables, SQS queues, S3 buckets, etc.)

Because all Serverless Framework resources are CloudFormation resources, the CloudFormation migration strategies described in the [CloudFormation migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/) apply directly.

To find your CloudFormation stack names, run:

```bash
# Using the Serverless Framework CLI
sls info --stage dev

# Or using the AWS CLI directly
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE \
    --query "StackSummaries[?starts_with(StackName, 'my-api-')].StackName"
```

## Choosing a migration path

### Pulumi Neo (Recommended)

Because the Serverless Framework creates standard CloudFormation stacks, [Neo](/product/neo/) can convert them to Pulumi code automatically.

1. **Prerequisites**:
    * Install the [Pulumi GitHub app](/docs/iac/guides/continuous-delivery/github-app/) with access to your repository
    * Configure AWS credentials in [Pulumi ESC](/docs/esc/)
    * Have Neo access (available in [Pulumi Cloud](/product/pulumi-cloud/))

1. **Identify your CloudFormation stacks**: Find the stack names created by the Serverless Framework (e.g., `my-api-dev`, `my-api-prod`).

1. **Start the migration**:

    ```text
    "Convert my CloudFormation stack my-api-dev to Pulumi"
    ```

1. **Neo will**:
    * Parse the CloudFormation stack and its resources
    * Generate equivalent Pulumi code for all resources (Lambda functions, API Gateway, IAM roles, etc.)
    * Import existing AWS resources without touching them
    * Verify zero changes with `pulumi preview`

1. **Review and commit**:
    * Examine the generated Pulumi code
    * Confirm the preview shows no changes
    * Commit your new Pulumi program

For a detailed walkthrough, see the [Neo migration blog post](/blog/neo-migration/).

#### When to use manual migration instead

While Neo handles most CloudFormation stacks automatically, you might need manual migration for:

* Custom CloudFormation resources or macros not yet supported by Neo
* Scenarios where you want to fundamentally restructure your infrastructure during migration
* Cases where you want to adopt resources incrementally across multiple Serverless Framework services

If you want to restructure your infrastructure, we recommend completing the migration first and then refactoring your Pulumi code.

### Alternative migration paths

If Neo doesn't support your specific use case, or if you prefer manual control over the migration process, the options below provide flexibility to coexist with or migrate from the Serverless Framework at your own pace.

## Referencing stack outputs

You can reference existing Serverless Framework stacks from your Pulumi program without taking over management of their resources. This is useful when you want to build new infrastructure that depends on resources already managed by the Serverless Framework.

The Serverless Framework exports several outputs from each CloudFormation stack, including `ServiceEndpoint` (the API Gateway URL) and `{FunctionName}LambdaFunctionQualifiedArn` for each function.

The following example reads a Serverless Framework stack named `my-api-dev` and uses its API endpoint and a function ARN:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const serverlessStack = aws.cloudformation.getStackOutput({
    name: "my-api-dev",
});

const apiEndpoint = serverlessStack.outputs["ServiceEndpoint"];
const processOrderArn = serverlessStack.outputs["ProcessOrderLambdaFunctionQualifiedArn"];

// Use these values in new infrastructure
const queue = new aws.sqs.Queue("new-queue");

export const endpoint = apiEndpoint;
export const orderFunctionArn = processOrderArn;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

serverless_stack = aws.cloudformation.get_stack(
    name="my-api-dev"
)

api_endpoint = serverless_stack.outputs["ServiceEndpoint"]
process_order_arn = serverless_stack.outputs["ProcessOrderLambdaFunctionQualifiedArn"]

# Use these values in new infrastructure
queue = aws.sqs.Queue("new-queue")

pulumi.export("endpoint", api_endpoint)
pulumi.export("order_function_arn", process_order_arn)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/cloudformation"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/sqs"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		serverlessStack := cloudformation.LookupStackOutput(ctx, cloudformation.LookupStackOutputArgs{
			Name: pulumi.String("my-api-dev"),
		})

		apiEndpoint := serverlessStack.Outputs().MapIndex(pulumi.String("ServiceEndpoint"))
		processOrderArn := serverlessStack.Outputs().MapIndex(pulumi.String("ProcessOrderLambdaFunctionQualifiedArn"))

		_, err := sqs.NewQueue(ctx, "new-queue", nil)
		if err != nil {
			return err
		}

		ctx.Export("endpoint", apiEndpoint)
		ctx.Export("orderFunctionArn", processOrderArn)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;

using Pulumi;
using CloudFormation = Pulumi.Aws.CloudFormation;
using Sqs = Pulumi.Aws.Sqs;

return await Deployment.RunAsync(async () =>
{
    var serverlessStack = await CloudFormation.GetStack.InvokeAsync(
        new CloudFormation.GetStackArgs
        {
            Name = "my-api-dev",
        }
    );

    var apiEndpoint = serverlessStack.Outputs["ServiceEndpoint"];
    var processOrderArn = serverlessStack.Outputs["ProcessOrderLambdaFunctionQualifiedArn"];

    var queue = new Sqs.Queue("new-queue");

    return new Dictionary<string, object?>
    {
        { "endpoint", apiEndpoint },
        { "orderFunctionArn", processOrderArn },
    };
});
```

{{% /choosable %}}

{{< /chooser >}}

Run `pulumi up` and the Pulumi runtime queries the CloudFormation stack and retrieves its output values. The Serverless Framework stack is treated as read-only, and Pulumi will not attempt to modify it or any resources managed by it.

## Resource mapping

The following table maps common `serverless.yml` configuration to the equivalent Pulumi AWS resources. Use this as a reference when rewriting your Serverless Framework definitions as Pulumi code.

| Serverless Framework (`serverless.yml`) | Pulumi AWS resource |
|---|---|
| `functions.[name]` | [`aws.lambda.Function`](/registry/packages/aws/api-docs/lambda/function/) |
| `functions.[name].events[].httpApi` | [`aws.apigatewayv2.Api`](/registry/packages/aws/api-docs/apigatewayv2/api/) |
| `functions.[name].events[].http` | [`aws.apigateway.RestApi`](/registry/packages/aws/api-docs/apigateway/restapi/) + related resources |
| `functions.[name].events[].sqs` | [`aws.sqs.Queue`](/registry/packages/aws/api-docs/sqs/queue/) + [`aws.lambda.EventSourceMapping`](/registry/packages/aws/api-docs/lambda/eventsourcemapping/) |
| `functions.[name].events[].sns` | [`aws.sns.Topic`](/registry/packages/aws/api-docs/sns/topic/) + [`aws.sns.TopicSubscription`](/registry/packages/aws/api-docs/sns/topicsubscription/) |
| `functions.[name].events[].s3` | [`aws.s3.BucketNotification`](/registry/packages/aws/api-docs/s3/bucketnotification/) |
| `functions.[name].events[].schedule` | [`aws.cloudwatch.EventRule`](/registry/packages/aws/api-docs/cloudwatch/eventrule/) + [`aws.cloudwatch.EventTarget`](/registry/packages/aws/api-docs/cloudwatch/eventtarget/) |
| `functions.[name].events[].eventBridge` | [`aws.cloudwatch.EventRule`](/registry/packages/aws/api-docs/cloudwatch/eventrule/) + [`aws.cloudwatch.EventTarget`](/registry/packages/aws/api-docs/cloudwatch/eventtarget/) |
| `provider.iam.role.statements` | [`aws.iam.Role`](/registry/packages/aws/api-docs/iam/role/) + [`aws.iam.RolePolicy`](/registry/packages/aws/api-docs/iam/rolepolicy/) |
| `provider.environment` | `environment` argument on [`aws.lambda.Function`](/registry/packages/aws/api-docs/lambda/function/) |
| `resources.Resources` (DynamoDB) | [`aws.dynamodb.Table`](/registry/packages/aws/api-docs/dynamodb/table/) |
| `resources.Resources` (S3) | [`aws.s3.BucketV2`](/registry/packages/aws/api-docs/s3/bucketv2/) |
| `resources.Resources` (SES) | [`aws.ses.DomainIdentity`](/registry/packages/aws/api-docs/ses/domainidentity/), [`aws.ses.EmailIdentity`](/registry/packages/aws/api-docs/ses/emailidentity/) |
| Stages (`--stage dev`) | [Pulumi stacks](/docs/concepts/stack/) (`pulumi stack select dev`) |

## Migration example

The following example shows a typical `serverless.yml` excerpt and its equivalent Pulumi program. This example defines a Lambda function with an HTTP API endpoint and a DynamoDB table.

### Serverless Framework (`serverless.yml`)

```yaml
service: my-api

provider:
  name: aws
  runtime: nodejs20.x
  stage: dev
  environment:
    ORDERS_TABLE: !Ref OrdersTable

functions:
  createOrder:
    handler: src/handlers/createOrder.handler
    events:
      - httpApi:
          path: /orders
          method: post

resources:
  Resources:
    OrdersTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: ${self:service}-orders-${self:provider.stage}
        BillingMode: PAY_PER_REQUEST
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: S
        KeySchema:
          - AttributeName: id
            KeyType: HASH
```

### Pulumi equivalent

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const stage = pulumi.getStack();

// DynamoDB table
const ordersTable = new aws.dynamodb.Table("orders-table", {
    name: `my-api-orders-${stage}`,
    billingMode: "PAY_PER_REQUEST",
    hashKey: "id",
    attributes: [
        { name: "id", type: "S" },
    ],
});

// IAM role for the Lambda function
const lambdaRole = new aws.iam.Role("create-order-role", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
        Service: "lambda.amazonaws.com",
    }),
    managedPolicyArns: [
        aws.iam.ManagedPolicy.AWSLambdaBasicExecutionRole,
    ],
});

const lambdaPolicy = new aws.iam.RolePolicy("create-order-policy", {
    role: lambdaRole.id,
    policy: ordersTable.arn.apply(arn => JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Effect: "Allow",
            Action: [
                "dynamodb:PutItem",
                "dynamodb:GetItem",
                "dynamodb:Query",
            ],
            Resource: arn,
        }],
    })),
});

// Lambda function
const createOrderFn = new aws.lambda.Function("create-order", {
    runtime: aws.lambda.Runtime.NodeJS20dX,
    handler: "src/handlers/createOrder.handler",
    role: lambdaRole.arn,
    code: new pulumi.asset.FileArchive("./app"),
    environment: {
        variables: {
            ORDERS_TABLE: ordersTable.name,
        },
    },
});

// HTTP API (API Gateway v2)
const api = new aws.apigatewayv2.Api("api", {
    protocolType: "HTTP",
});

const integration = new aws.apigatewayv2.Integration("create-order-integration", {
    apiId: api.id,
    integrationType: "AWS_PROXY",
    integrationUri: createOrderFn.arn,
    payloadFormatVersion: "2.0",
});

const route = new aws.apigatewayv2.Route("create-order-route", {
    apiId: api.id,
    routeKey: "POST /orders",
    target: pulumi.interpolate`integrations/${integration.id}`,
});

const apiStage = new aws.apigatewayv2.Stage("api-stage", {
    apiId: api.id,
    name: "$default",
    autoDeploy: true,
});

const lambdaPermission = new aws.lambda.Permission("api-lambda-permission", {
    action: "lambda:InvokeFunction",
    function: createOrderFn.name,
    principal: "apigateway.amazonaws.com",
    sourceArn: pulumi.interpolate`${api.executionArn}/*/*`,
});

export const endpoint = api.apiEndpoint;
export const tableName = ordersTable.name;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import json

import pulumi
import pulumi_aws as aws

stage = pulumi.get_stack()

# DynamoDB table
orders_table = aws.dynamodb.Table("orders-table",
    name=f"my-api-orders-{stage}",
    billing_mode="PAY_PER_REQUEST",
    hash_key="id",
    attributes=[
        aws.dynamodb.TableAttributeArgs(name="id", type="S"),
    ],
)

# IAM role for the Lambda function
lambda_role = aws.iam.Role("create-order-role",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
        }],
    }),
    managed_policy_arns=[
        aws.iam.ManagedPolicy.AWS_LAMBDA_BASIC_EXECUTION_ROLE,
    ],
)

lambda_policy = aws.iam.RolePolicy("create-order-policy",
    role=lambda_role.id,
    policy=orders_table.arn.apply(lambda arn: json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:GetItem",
                "dynamodb:Query",
            ],
            "Resource": arn,
        }],
    })),
)

# Lambda function
create_order_fn = aws.lambda_.Function("create-order",
    runtime=aws.lambda_.Runtime.NODE_JS20D_X,
    handler="src/handlers/createOrder.handler",
    role=lambda_role.arn,
    code=pulumi.FileArchive("./app"),
    environment=aws.lambda_.FunctionEnvironmentArgs(
        variables={"ORDERS_TABLE": orders_table.name},
    ),
)

# HTTP API (API Gateway v2)
api = aws.apigatewayv2.Api("api",
    protocol_type="HTTP",
)

integration = aws.apigatewayv2.Integration("create-order-integration",
    api_id=api.id,
    integration_type="AWS_PROXY",
    integration_uri=create_order_fn.arn,
    payload_format_version="2.0",
)

route = aws.apigatewayv2.Route("create-order-route",
    api_id=api.id,
    route_key="POST /orders",
    target=integration.id.apply(lambda id: f"integrations/{id}"),
)

api_stage = aws.apigatewayv2.Stage("api-stage",
    api_id=api.id,
    name="$default",
    auto_deploy=True,
)

lambda_permission = aws.lambda_.Permission("api-lambda-permission",
    action="lambda:InvokeFunction",
    function=create_order_fn.name,
    principal="apigateway.amazonaws.com",
    source_arn=api.execution_arn.apply(lambda arn: f"{arn}/*/*"),
)

pulumi.export("endpoint", api.api_endpoint)
pulumi.export("table_name", orders_table.name)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"encoding/json"
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/apigatewayv2"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/dynamodb"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/lambda"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		stage := ctx.Stack()

		// DynamoDB table
		ordersTable, err := dynamodb.NewTable(ctx, "orders-table", &dynamodb.TableArgs{
			Name:        pulumi.Sprintf("my-api-orders-%s", stage),
			BillingMode: pulumi.String("PAY_PER_REQUEST"),
			HashKey:     pulumi.String("id"),
			Attributes: dynamodb.TableAttributeArray{
				&dynamodb.TableAttributeArgs{
					Name: pulumi.String("id"),
					Type: pulumi.String("S"),
				},
			},
		})
		if err != nil {
			return err
		}

		// IAM role for the Lambda function
		assumeRolePolicy, _ := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				{
					"Action":    "sts:AssumeRole",
					"Effect":    "Allow",
					"Principal": map[string]string{"Service": "lambda.amazonaws.com"},
				},
			},
		})

		lambdaRole, err := iam.NewRole(ctx, "create-order-role", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.String(string(assumeRolePolicy)),
			ManagedPolicyArns: pulumi.StringArray{
				iam.ManagedPolicyAWSLambdaBasicExecutionRole,
			},
		})
		if err != nil {
			return err
		}

		_, err = iam.NewRolePolicy(ctx, "create-order-policy", &iam.RolePolicyArgs{
			Role: lambdaRole.ID(),
			Policy: ordersTable.Arn.ApplyT(func(arn string) (string, error) {
				policy, _ := json.Marshal(map[string]interface{}{
					"Version": "2012-10-17",
					"Statement": []map[string]interface{}{
						{
							"Effect":   "Allow",
							"Action":   []string{"dynamodb:PutItem", "dynamodb:GetItem", "dynamodb:Query"},
							"Resource": arn,
						},
					},
				})
				return string(policy), nil
			}).(pulumi.StringOutput),
		})
		if err != nil {
			return err
		}

		// Lambda function
		createOrderFn, err := lambda.NewFunction(ctx, "create-order", &lambda.FunctionArgs{
			Runtime: pulumi.String("nodejs20.x"),
			Handler: pulumi.String("src/handlers/createOrder.handler"),
			Role:    lambdaRole.Arn,
			Code:    pulumi.NewFileArchive("./app"),
			Environment: &lambda.FunctionEnvironmentArgs{
				Variables: pulumi.StringMap{
					"ORDERS_TABLE": ordersTable.Name,
				},
			},
		})
		if err != nil {
			return err
		}

		// HTTP API (API Gateway v2)
		api, err := apigatewayv2.NewApi(ctx, "api", &apigatewayv2.ApiArgs{
			ProtocolType: pulumi.String("HTTP"),
		})
		if err != nil {
			return err
		}

		integration, err := apigatewayv2.NewIntegration(ctx, "create-order-integration", &apigatewayv2.IntegrationArgs{
			ApiId:                api.ID(),
			IntegrationType:      pulumi.String("AWS_PROXY"),
			IntegrationUri:       createOrderFn.Arn,
			PayloadFormatVersion: pulumi.String("2.0"),
		})
		if err != nil {
			return err
		}

		_, err = apigatewayv2.NewRoute(ctx, "create-order-route", &apigatewayv2.RouteArgs{
			ApiId:    api.ID(),
			RouteKey: pulumi.String("POST /orders"),
			Target:   pulumi.Sprintf("integrations/%s", integration.ID()),
		})
		if err != nil {
			return err
		}

		_, err = apigatewayv2.NewStage(ctx, "api-stage", &apigatewayv2.StageArgs{
			ApiId:      api.ID(),
			Name:       pulumi.String("$default"),
			AutoDeploy: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		_, err = lambda.NewPermission(ctx, "api-lambda-permission", &lambda.PermissionArgs{
			Action:    pulumi.String("lambda:InvokeFunction"),
			Function:  createOrderFn.Name,
			Principal: pulumi.String("apigateway.amazonaws.com"),
			SourceArn: api.ExecutionArn.ApplyT(func(arn string) string {
				return fmt.Sprintf("%s/*/*", arn)
			}).(pulumi.StringOutput),
		})
		if err != nil {
			return err
		}

		ctx.Export("endpoint", api.ApiEndpoint)
		ctx.Export("tableName", ordersTable.Name)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Text.Json;

using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var stage = Deployment.Instance.StackName;

    // DynamoDB table
    var ordersTable = new Aws.DynamoDB.Table("orders-table", new()
    {
        Name = $"my-api-orders-{stage}",
        BillingMode = "PAY_PER_REQUEST",
        HashKey = "id",
        Attributes = new[]
        {
            new Aws.DynamoDB.Inputs.TableAttributeArgs
            {
                Name = "id",
                Type = "S",
            },
        },
    });

    // IAM role for the Lambda function
    var lambdaRole = new Aws.Iam.Role("create-order-role", new()
    {
        AssumeRolePolicy = JsonSerializer.Serialize(new
        {
            Version = "2012-10-17",
            Statement = new[]
            {
                new
                {
                    Action = "sts:AssumeRole",
                    Effect = "Allow",
                    Principal = new { Service = "lambda.amazonaws.com" },
                },
            },
        }),
        ManagedPolicyArns = new[]
        {
            "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
        },
    });

    var lambdaPolicy = new Aws.Iam.RolePolicy("create-order-policy", new()
    {
        Role = lambdaRole.Id,
        Policy = ordersTable.Arn.Apply(arn => JsonSerializer.Serialize(new
        {
            Version = "2012-10-17",
            Statement = new[]
            {
                new
                {
                    Effect = "Allow",
                    Action = new[] { "dynamodb:PutItem", "dynamodb:GetItem", "dynamodb:Query" },
                    Resource = arn,
                },
            },
        })),
    });

    // Lambda function
    var createOrderFn = new Aws.Lambda.Function("create-order", new()
    {
        Runtime = Aws.Lambda.Runtime.NodeJS20dX,
        Handler = "src/handlers/createOrder.handler",
        Role = lambdaRole.Arn,
        Code = new FileArchive("./app"),
        Environment = new Aws.Lambda.Inputs.FunctionEnvironmentArgs
        {
            Variables = { { "ORDERS_TABLE", ordersTable.Name } },
        },
    });

    // HTTP API (API Gateway v2)
    var api = new Aws.ApiGatewayV2.Api("api", new()
    {
        ProtocolType = "HTTP",
    });

    var integration = new Aws.ApiGatewayV2.Integration("create-order-integration", new()
    {
        ApiId = api.Id,
        IntegrationType = "AWS_PROXY",
        IntegrationUri = createOrderFn.Arn,
        PayloadFormatVersion = "2.0",
    });

    var route = new Aws.ApiGatewayV2.Route("create-order-route", new()
    {
        ApiId = api.Id,
        RouteKey = "POST /orders",
        Target = integration.Id.Apply(id => $"integrations/{id}"),
    });

    var apiStage = new Aws.ApiGatewayV2.Stage("api-stage", new()
    {
        ApiId = api.Id,
        Name = "$default",
        AutoDeploy = true,
    });

    var lambdaPermission = new Aws.Lambda.Permission("api-lambda-permission", new()
    {
        Action = "lambda:InvokeFunction",
        Function = createOrderFn.Name,
        Principal = "apigateway.amazonaws.com",
        SourceArn = api.ExecutionArn.Apply(arn => $"{arn}/*/*"),
    });

    return new Dictionary<string, object?>
    {
        { "endpoint", api.ApiEndpoint },
        { "tableName", ordersTable.Name },
    };
});
```

{{% /choosable %}}

{{< /chooser >}}

With Pulumi, you get the full power of a programming language. You can create reusable functions, use loops to create multiple similar resources, add conditional logic, and write tests for your infrastructure code.

## Importing existing resources

If you have existing resources created by the Serverless Framework that you want to bring under Pulumi's management without recreating them, use [Pulumi's import feature](/docs/using-pulumi/adopting-pulumi/import/).

### Step 1: Identify your resources

List the resources in your Serverless Framework CloudFormation stack:

```bash
aws cloudformation list-stack-resources --stack-name my-api-dev \
    --query "StackResourceSummaries[].{Type:ResourceType,LogicalId:LogicalResourceId,PhysicalId:PhysicalResourceId}" \
    --output table
```

### Step 2: Import resources into Pulumi

You can import resources using the `pulumi import` CLI command or the `import` resource option in code.

Using the CLI:

```bash
# Import a Lambda function
pulumi import aws:lambda/function:Function create-order my-api-dev-createOrder

# Import a DynamoDB table
pulumi import aws:dynamodb/table:Table orders-table my-api-orders-dev

# Import an API Gateway v2 API
pulumi import aws:apigatewayv2/api:Api api abc123def
```

Using the import option in code (TypeScript example):

```typescript
const ordersTable = new aws.dynamodb.Table("orders-table", {
    name: "my-api-orders-dev",
    billingMode: "PAY_PER_REQUEST",
    hashKey: "id",
    attributes: [
        { name: "id", type: "S" },
    ],
}, { import: "my-api-orders-dev" });
```

After the import completes and `pulumi preview` shows no changes, remove the `import` option from your code. Pulumi now manages the resource.

### Step 3: Remove resources from CloudFormation

Before deleting your Serverless Framework CloudFormation stack, update the resources to use a `DeletionPolicy` of `Retain` so that AWS doesn't delete them when the stack is removed. You can do this by adding the policy to your `serverless.yml`:

```yaml
resources:
  Resources:
    OrdersTable:
      Type: AWS::DynamoDB::Table
      DeletionPolicy: Retain
      Properties:
        # ... existing properties
```

Deploy the change with `sls deploy`, then remove the Serverless Framework stack with `sls remove`. The resources will remain in AWS, now managed entirely by Pulumi.

For detailed AWS import ID formats and troubleshooting, see [AWS import IDs and special cases](/docs/iac/guides/migration/aws-import-ids/).

## Managing stages with Pulumi stacks

The Serverless Framework uses `--stage` to deploy the same service to multiple environments. In Pulumi, this maps directly to [stacks](/docs/concepts/stack/):

```bash
# Create stacks for each stage
pulumi stack init dev
pulumi stack init staging
pulumi stack init prod

# Set stage-specific configuration
pulumi config set --stack dev aws:region us-east-1
pulumi config set --stack prod aws:region us-west-2
```

In your Pulumi program, use `pulumi.getStack()` (or equivalent) to get the current stack name, which replaces the Serverless Framework `${self:provider.stage}` variable.

Stage-specific variables from `serverless.yml`'s `custom:` section become Pulumi config values:

```bash
# Instead of serverless.yml custom variables:
# custom:
#   tableName:
#     dev: my-table-dev
#     prod: my-table-prod

pulumi config set --stack dev tableName my-table-dev
pulumi config set --stack prod tableName my-table-prod
```

```typescript
const config = new pulumi.Config();
const tableName = config.require("tableName");
```

For more advanced environment management, consider [Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) which provides hierarchical configuration, secrets management, and environment composition.

## Key differences and benefits

Migrating from the Serverless Framework to Pulumi gives you:

* **Real programming languages** instead of YAML configuration, with IDE support, type checking, and testing
* **Full cloud coverage**: manage Lambda functions alongside databases, queues, VPCs, DNS, CDNs, and any other cloud resource, all in one program
* **Built-in state management**: no separate CloudFormation dependency or stack limits
* **[Policy as code](/docs/using-pulumi/crossguard/)**: enforce compliance and security rules across all your infrastructure
* **Multi-cloud support**: use the same tool and workflows across AWS, Azure, Google Cloud, and [100+ providers](/registry/)
* **[Pulumi ESC](/docs/esc/)**: centralized secrets and configuration management that replaces scattered environment variable management

To learn more about how Pulumi compares to the Serverless Framework, see the [Pulumi vs. Serverless Framework comparison](/docs/iac/comparisons/serverless/).
