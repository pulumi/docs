---
title: "Zero-downtime CDK to Pulumi migration with Neo"

date: 2026-01-14

draft: false

meta_desc: Learn how Neo automates CDK to Pulumi migrations with zero downtime, converting code, migrating state, and proving safety through Pulumi Preview.

meta_image: meta.png

authors:
    - neo-team

tags:
    - neo
    - aws
    - cdk
    - migration
    - ai

schema_type: auto

---

When we launched Neo, we set out to solve real infrastructure challenges that teams face every day. One of the most complex and risky operations is migrating infrastructure. Today, I'm excited to share how we've made CDK to Pulumi migrations not just possible, but safe and predictable.

<!--more-->

## The problem we're solving

Every week, we hear from teams who want to migrate from AWS CDK to Pulumi. They're attracted to Pulumi's multi-cloud capabilities, superior policy engine, and native programming language support. But they're stuck. Traditional migration approaches often require recreating infrastructure, which means:

- Service downtime during the cutover
- Risk of misconfiguration or data loss
- Complex rollback procedures if something goes wrong
- Weeks or months of careful planning and execution

We built Neo's CDK migration capabilities to eliminate these barriers entirely.

## Import, don't recreate

The strategy of importing resources isn't new, but the execution has always been painful. Manual imports require finding physical resource IDs, constructing import commands, and hoping you didn't miss anything. It's error-prone and can take weeks for complex stacks.

We've automated this entire process. What once took days of manual work now completes in minutes. Neo identifies every resource in your CloudFormation stacks, converts your CDK code to Pulumi, and imports all existing infrastructure without touching a single running resource. Your S3 buckets keep serving files, your Lambda functions keep processing requests, and your databases keep handling queries while ownership quietly transfers from CloudFormation to Pulumi.

This approach delivers three critical guarantees:

1. **Zero downtime**: Resources are never deleted or recreated
2. **Safe rollback**: Since your infrastructure hasn't changed, you can abandon the migration at any point before committing
3. **Verifiability**: Preview shows exactly zero changes before you commit

## How it works: The technical architecture

Neo's CDK migration capability combines several components to deliver a seamless experience:

### 1. Orchestration layer

Neo acts as the migration coordinator. When you ask Neo to migrate your CDK application, it:

- Verifies AWS credentials are properly configured in Pulumi ESC
- Synthesizes your CDK application to generate CloudFormation templates
- Builds a complete inventory of all resources across all stacks
- Orchestrates the conversion and import process
- Generates comprehensive migration reports for audit trails

Neo enforces strict success criteria: every CloudFormation resource must be accounted for in the final Pulumi program, and the final preview must show zero changes.

### 2. Code conversion engine

Neo transforms CDK Cloud Assemblies into Pulumi programs with high fidelity. The conversion process:

- **Preserves resource identity**: CDK logical IDs are maintained as Pulumi resource names, enabling automated import
- **Maintains relationships**: Cross-stack references are converted to Pulumi stack references automatically
- **Selects optimal providers**: Defaults to `@pulumi/aws-native` for CloudFormation compatibility, with the ability to fallback to `@pulumi/aws` when needed
- **Reports conversion coverage**: Identifies any resources requiring manual attention with specific guidance

Neo handles approximately 90% of resources automatically, providing clear guidance for edge cases.

### 3. State migration system

This is where the zero-downtime guarantee comes from. Neo:

- Reads your existing CloudFormation stack state
- Maps CloudFormation physical IDs to Pulumi import identifiers
- Performs import of all resources into Pulumi state
- Provides real-time progress tracking and error handling
- Generates import manifests for resources requiring manual intervention

The import process is idempotent and can be safely re-run if interrupted.

### 4. Edge case handling

For resources that can't be automatically imported, Neo provides:

- Import ID format specifications for any CloudFormation resource type
- Guidance on obtaining physical resource IDs from AWS APIs
- Composite ID construction for complex resources (e.g., `FunctionName|StatementId`)
- Direct Cloud Control API commands for ID retrieval

## A real migration walkthrough

Let's take a look at exactly what happens when you migrate a production CDK application.

### Starting point: Your CDK application

Consider a typical CDK stack with an API Gateway, Lambda functions, and DynamoDB:

```typescript
// lib/api-stack.ts
export class ApiStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const table = new dynamodb.Table(this, 'OrdersTable', {
      partitionKey: { name: 'orderId', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      pointInTimeRecovery: true,
    });

    const handler = new lambda.Function(this, 'OrderHandler', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'orders.handler',
      code: lambda.Code.fromAsset('lambda'),
      environment: {
        TABLE_NAME: table.tableName,
      },
    });

    table.grantReadWriteData(handler);

    const api = new apigateway.RestApi(this, 'OrdersApi', {
      deployOptions: {
        stageName: 'prod',
        loggingLevel: apigateway.MethodLoggingLevel.INFO,
      },
    });

    api.root.addMethod('POST', new apigateway.LambdaIntegration(handler));
  }
}
```

### Phase 1: Discovery and inventory

Neo begins by synthesizing your CDK application and querying CloudFormation:

```text
$ cdk synth
Successfully synthesized to cdk.out

Neo: Analyzing CloudFormation stack ApiStack-prod...
Found 7 resources:
- AWS::DynamoDB::Table (OrdersTable)
- AWS::IAM::Role (OrderHandlerServiceRole)
- AWS::Lambda::Function (OrderHandler)
- AWS::IAM::Policy (OrderHandlerServiceRoleDefaultPolicy)
- AWS::ApiGateway::RestApi (OrdersApi)
- AWS::ApiGateway::Deployment (OrdersApiDeployment)
- AWS::ApiGateway::Stage (OrdersApiProdStage)
```

This inventory becomes our source of truth. Every resource must be migrated successfully.

### Phase 2: Automated conversion

Neo converts the CDK assembly to Pulumi code, preserving all resource relationships:

```typescript
// index.ts (generated)
import * as pulumi from "@pulumi/pulumi";
import * as awsnative from "@pulumi/aws-native";

const ordersTable = new awsnative.dynamodb.Table("OrdersTable", {
    keySchema: [{
        attributeName: "orderId",
        keyType: "HASH",
    }],
    attributeDefinitions: [{
        attributeName: "orderId",
        attributeType: "S",
    }],
    billingMode: "PAY_PER_REQUEST",
    pointInTimeRecoverySpecification: {
        pointInTimeRecoveryEnabled: true,
    },
});

const orderHandlerRole = new awsnative.iam.Role("OrderHandlerServiceRole", {
    assumeRolePolicyDocument: {
        Version: "2012-10-17",
        Statement: [{
            Effect: "Allow",
            Principal: { Service: "lambda.amazonaws.com" },
            Action: "sts:AssumeRole",
        }],
    },
    managedPolicyArns: [
        "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
    ],
});

// Additional resources follow the same pattern...
```

The conversion report shows 100% coverage: all 7 resources converted successfully.

### Phase 3: Zero-downtime import

Now comes the critical moment. Neo imports your existing infrastructure:

```output
[INFO] Starting import of CloudFormation stack ApiStack-prod
[INFO] Retrieved 7 resources from CloudFormation
[INFO] Importing aws-native:dynamodb:Table OrdersTable (arn:aws:dynamodb:us-east-1:123456789:table/ApiStack-OrdersTable-ABC123)
[INFO] Importing aws-native:iam:Role OrderHandlerServiceRole
[INFO] Importing aws-native:lambda:Function OrderHandler
[INFO] Importing aws-native:iam:Policy OrderHandlerServiceRoleDefaultPolicy
[INFO] Importing aws-native:apigateway:RestApi OrdersApi
[INFO] Importing aws-native:apigateway:Deployment OrdersApiDeployment
[INFO] Importing aws-native:apigateway:Stage OrdersApiProdStage
[INFO] Import complete: 7 resources imported, 0 failures
```

Your API continues serving traffic throughout this entire process.

### Phase 4: Verification

The moment of truth. Neo runs `pulumi preview` to prove nothing will change:

```text
Previewing update (prod)

     Type                                 Name                          Plan
     pulumi:pulumi:Stack                  api-prod
     ├─ aws-native:dynamodb:Table         OrdersTable                  import
     ├─ aws-native:iam:Role               OrderHandlerServiceRole       import
     ├─ aws-native:lambda:Function        OrderHandler                  import
     ├─ aws-native:iam:Policy             OrderHandlerServiceRoleDefaultPolicy  import
     ├─ aws-native:apigateway:RestApi     OrdersApi                     import
     ├─ aws-native:apigateway:Deployment  OrdersApiDeployment           import
     └─ aws-native:apigateway:Stage       OrdersApiProdStage            import

Resources:
    + 7 to import

Duration: 4s
```

Seven resources to import. Zero modifications. Your infrastructure is now managed by Pulumi without a single API call being dropped.

## Handling complexity at scale

Real-world CDK applications aren't always straightforward. Here's how Neo handles common complexities:

### Partial migrations

You can migrate specific stacks while leaving others in CDK, enabling gradual adoption. This allows teams to validate the migration process with less critical stacks before moving production workloads.

## Speed and reliability

The most striking improvement is speed. Migrations that previously required weeks of planning and execution now complete in under 15 minutes for typical applications. More complex stacks with hundreds of resources might take longer, but the hands-on time remains minimal.

## Design decisions and trade-offs

Building this system required several key architectural decisions:

### aws-native by default

We default to `@pulumi/aws-native` because it maps 1:1 with CloudFormation resource types, ensuring the highest fidelity during migration. We automatically fall back to `@pulumi/aws` when aws-native doesn't support a particular resource or feature.

### Logical IDs preservation

CDK logical IDs encode important semantic meaning about resource relationships. Preserving them ensures that imported resources maintain their identity and that dependent resources can find each other correctly.

### Human in the loop

While we could fully automate the migration, requiring human review at key checkpoints ensures that teams understand what's changing and maintain control over their infrastructure.

## Security and compliance

The migration process maintains your existing security posture:

- **No credential exposure**: AWS credentials remain in Pulumi ESC throughout
- **Audit trail**: Complete migration reports document every change
- **Policy preservation**: IAM policies and security groups migrate unchanged
- **Compliance continuity**: Resources maintain their compliance tags and configurations

## Start your migration today

If you're ready to migrate from CDK to Pulumi, here's your checklist:

1. Ensure your CDK application synthesizes cleanly
2. Configure Pulumi ESC with your AWS credentials
3. Ask Neo: "Help me migrate my CDK application to Pulumi"

Neo will guide you through each step, ensuring a safe, predictable migration with zero downtime.

The technology we've built represents a fundamental shift in how infrastructure migrations work. By focusing on import rather than recreation, we've eliminated the traditional risks and barriers. Your infrastructure keeps running, your team maintains control, and you get the benefits of Pulumi without the migration pain.

Have questions about migrating your CDK application? Join us in the [Pulumi Community Slack](https://slack.pulumi.com/) or reach out to your account team for a guided migration session.
