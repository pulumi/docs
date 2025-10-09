---
title: "Connect AWS Lambda to Private VPC Resources"
meta_desc: "Deploy Lambda functions that access private VPC resources like RDS, ElastiCache, or internal APIs with Pulumi."
canonical_url: "https://www.pulumi.com/recipes/aws/lambda-vpc-access"
date: 2025-10-08
category: "Compute"
tags: ["aws", "lambda", "vpc", "networking", "rds", "compute", "serverless"]
faq:
  - question: How do I find the correct subnet IDs for my VPC?
    answer: You can use aws.ec2.getSubnets to query subnets by VPC ID and filter by tags, or use the AWS Console to find subnet IDs in your VPC configuration. Typically, Lambda functions should be placed in private subnets.
  - question: Does Lambda in a VPC have internet access by default?
    answer: No, Lambda functions in private subnets need a NAT Gateway for outbound internet access. Public subnets can use an Internet Gateway, but it's recommended to use private subnets for Lambda.
  - question: How much does a NAT Gateway cost?
    answer: AWS NAT Gateways cost approximately $0.045/hour (about $32/month) plus $0.045/GB for data processed. This is required if your Lambda needs to access external APIs or AWS services outside your VPC.
  - question: Why are my Lambda cold starts slower with VPC?
    answer: VPC-enabled Lambda functions need to create Elastic Network Interfaces (ENIs) on cold starts, adding 1-2 seconds of latency. AWS's Hyperplane ENIs have improved this significantly in recent years.
  - question: Can I use the same security group for Lambda and RDS?
    answer: No, it's better practice to use separate security groups. Configure your RDS security group to allow inbound traffic from the Lambda security group on the database port (e.g., 5432 for PostgreSQL).
---

## How do I connect AWS Lambda to private VPC resources?

**To enable AWS Lambda to access private resources in your VPC**, configure the function's `vpcConfig` with subnet IDs and security group IDs. The following example shows how to deploy a VPC-connected Lambda function in TypeScript, Python, Go, C#, and Java.

{{< chooser language "typescript,python,go,csharp,java" >}}
{{% choosable language typescript %}}
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.lambda.Function("example", {
    code: new pulumi.asset.FileArchive("function.zip"),
    name: "example_vpc_function",
    role: exampleAwsIamRole.arn,
    handler: "app.handler",
    runtime: aws.lambda.Runtime.Python3d12,
    memorySize: 1024,
    timeout: 30,
    vpcConfig: {
        subnetIds: [
            examplePrivate1.id,
            examplePrivate2.id,
        ],
        securityGroupIds: [exampleLambda.id],
        ipv6AllowedForDualStack: true,
    },
    ephemeralStorage: {
        size: 5120,
    },
    snapStart: {
        applyOn: "PublishedVersions",
    },
});
```
{{% /choosable %}}

{{% choosable language python %}}
```python
import pulumi
import pulumi_aws as aws

example = aws.lambda_.Function("example",
    code=pulumi.FileArchive("function.zip"),
    name="example_vpc_function",
    role=example_aws_iam_role["arn"],
    handler="app.handler",
    runtime=aws.lambda_.Runtime.PYTHON3D12,
    memory_size=1024,
    timeout=30,
    vpc_config=aws.lambda_.FunctionVpcConfigArgs(
        subnet_ids=[
            example_private1["id"],
            example_private2["id"],
        ],
        security_group_ids=[example_lambda["id"]],
        ipv6_allowed_for_dual_stack=True,
    ),
    ephemeral_storage=aws.lambda_.FunctionEphemeralStorageArgs(
        size=5120,
    ),
    snap_start=aws.lambda_.FunctionSnapStartArgs(
        apply_on="PublishedVersions",
    ))
```
{{% /choosable %}}

{{% choosable language go %}}
```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/lambda"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := lambda.NewFunction(ctx, "example", &lambda.FunctionArgs{
			Code:       pulumi.NewFileArchive("function.zip"),
			Name:       pulumi.String("example_vpc_function"),
			Role:       pulumi.Any(exampleAwsIamRole.Arn),
			Handler:    pulumi.String("app.handler"),
			Runtime:    pulumi.String(lambda.RuntimePython3d12),
			MemorySize: pulumi.Int(1024),
			Timeout:    pulumi.Int(30),
			VpcConfig: &lambda.FunctionVpcConfigArgs{
				SubnetIds: pulumi.StringArray{
					examplePrivate1.Id,
					examplePrivate2.Id,
				},
				SecurityGroupIds: pulumi.StringArray{
					exampleLambda.Id,
				},
				Ipv6AllowedForDualStack: pulumi.Bool(true),
			},
			EphemeralStorage: &lambda.FunctionEphemeralStorageArgs{
				Size: pulumi.Int(5120),
			},
			SnapStart: &lambda.FunctionSnapStartArgs{
				ApplyOn: pulumi.String("PublishedVersions"),
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```
{{% /choosable %}}

{{% choosable language csharp %}}
```csharp
using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var example = new Aws.Lambda.Function("example", new()
    {
        Code = new FileArchive("function.zip"),
        Name = "example_vpc_function",
        Role = exampleAwsIamRole.Arn,
        Handler = "app.handler",
        Runtime = Aws.Lambda.Runtime.Python3d12,
        MemorySize = 1024,
        Timeout = 30,
        VpcConfig = new Aws.Lambda.Inputs.FunctionVpcConfigArgs
        {
            SubnetIds = new[]
            {
                examplePrivate1.Id,
                examplePrivate2.Id,
            },
            SecurityGroupIds = new[]
            {
                exampleLambda.Id,
            },
            Ipv6AllowedForDualStack = true,
        },
        EphemeralStorage = new Aws.Lambda.Inputs.FunctionEphemeralStorageArgs
        {
            Size = 5120,
        },
        SnapStart = new Aws.Lambda.Inputs.FunctionSnapStartArgs
        {
            ApplyOn = "PublishedVersions",
        },
    });
});
```
{{% /choosable %}}

{{% choosable language java %}}
```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.lambda.Function;
import com.pulumi.aws.lambda.FunctionArgs;
import com.pulumi.aws.lambda.inputs.FunctionVpcConfigArgs;
import com.pulumi.aws.lambda.inputs.FunctionEphemeralStorageArgs;
import com.pulumi.aws.lambda.inputs.FunctionSnapStartArgs;
import com.pulumi.asset.FileArchive;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var example = new Function("example", FunctionArgs.builder()
            .code(new FileArchive("function.zip"))
            .name("example_vpc_function")
            .role(exampleAwsIamRole.arn())
            .handler("app.handler")
            .runtime("python3.12")
            .memorySize(1024)
            .timeout(30)
            .vpcConfig(FunctionVpcConfigArgs.builder()
                .subnetIds(
                    examplePrivate1.id(),
                    examplePrivate2.id())
                .securityGroupIds(exampleLambda.id())
                .ipv6AllowedForDualStack(true)
                .build())
            .ephemeralStorage(FunctionEphemeralStorageArgs.builder()
                .size(5120)
                .build())
            .snapStart(FunctionSnapStartArgs.builder()
                .applyOn("PublishedVersions")
                .build())
            .build());
    }
}
```
{{% /choosable %}}
{{< /chooser >}}

## Key configuration details

**VPC Configuration**: The `vpcConfig` block specifies which subnets and security groups the Lambda function uses. Using multiple private subnets across availability zones provides high availability.

**Security Groups**: The `securityGroupIds` define network access rules. Ensure your security group allows outbound traffic to your VPC resources and that target resources (like RDS) allow inbound traffic from the Lambda security group.

**Subnet Selection**: Deploy Lambda to private subnets. If the function needs internet access, these subnets should route traffic through a NAT Gateway.

**Enhanced Networking**: The `ipv6AllowedForDualStack` option enables dual-stack networking for both IPv4 and IPv6.

**Ephemeral Storage**: The example sets ephemeral storage to 5120 MB (5 GB). The default is 512 MB, and the maximum is 10,240 MB.

**SnapStart**: This feature improves cold start performance for Java functions by reusing initialized snapshots. It only applies to Java runtimes.

## Frequently asked questions

**How do I find the correct subnet IDs for my VPC?**
You can use aws.ec2.getSubnets to query subnets by VPC ID and filter by tags, or use the AWS Console to find subnet IDs in your VPC configuration. Typically, Lambda functions should be placed in private subnets.

**Does Lambda in a VPC have internet access by default?**
No, Lambda functions in private subnets need a NAT Gateway for outbound internet access. Public subnets can use an Internet Gateway, but it's recommended to use private subnets for Lambda.

**How much does a NAT Gateway cost?**
AWS NAT Gateways cost approximately $0.045/hour (about $32/month) plus $0.045/GB for data processed. This is required if your Lambda needs to access external APIs or AWS services outside your VPC.

**Why are my Lambda cold starts slower with VPC?**
VPC-enabled Lambda functions need to create Elastic Network Interfaces (ENIs) on cold starts, adding 1-2 seconds of latency. AWS's Hyperplane ENIs have improved this significantly in recent years.

**Can I use the same security group for Lambda and RDS?**
No, it's better practice to use separate security groups. Configure your RDS security group to allow inbound traffic from the Lambda security group on the database port (e.g., 5432 for PostgreSQL).
