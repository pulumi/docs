---
title: "Pulumi AWS Cloud Control Provider is Generally Available"
allow_long_title: true
date: 2024-10-01T09:00:00-07:00
updated: 2024-03-24
draft: false
meta_desc: >-
    Discover Pulumi’s AWS Cloud Control Provider—now GA with Day 1 AWS support, extended IaC capabilities, and seamless CloudFormation migration tools.
meta_image: meta-aws.png
authors:
    - tejitha-raju
    - matt-jeffryes
tags:
    - aws
    - provider
    - cloudcontrol
---
We're excited to announce the general availability of the new [AWS Cloud Control Provider] for Pulumi (previously "AWS Native"). AWS is one of the most-used cloud providers across the Pulumi ecosystem, and we are committed to providing the fastest possible access to new AWS capabilities to all Pulumi users. This provider delivers on that promise by providing native support for all resources in the AWS Cloud Control APIs. As part of this launch, we are also renaming the provider from “AWS Native” to "AWS Cloud Control Provider," based on customer feedback during the preview phase, to provide users with a broader range of advanced cloud management tools exposed by the AWS Cloud Control API. This provider includes the following features and benefits,

* __Day 1 support for AWS Resources__: Provides full coverage of the [AWS Cloud Control API], typically on the day of the launch, ensuring users can adopt new features immediately.
* __Complementary Pulumi Experience__: Works alongside Pulumi’s AWS Provider, enhancing [Infrastructure as Code](/what-is/what-is-infrastructure-as-code/) projects with the latest AWS capabilities without requiring significant changes to existing setups.
* __Extended support for third-party resources__: Our platform offers enhanced flexibility and interoperability by supporting third-party resources available in the CloudFormation Registry, such as Atlassian, MongoDB, Datadog, and more.
* __Easy CloudFormation to Pulumi Migration__: [cf2pulumi](https://www.pulumi.com/cf2pulumi/) provides the ability to migrate existing CloudFormation templates into Pulumi programs in your favorite language.


At Pulumi, we're dedicated to empowering our customers with the tools they need to innovate and thrive in the cloud. The launch of the AWS Cloud Control Provider represents our unwavering commitment to providing best-in-class solutions that simplify cloud management, streamline operations, and drive business success. The Pulumi AWS Cloud Control Provider can be used side-by-side with the standard  Pulumi AWS provider and nearly 200  additional Pulumi resource providers that cover a wide variety of cloud and SaaS platforms.

## Using Pulumi AWS Cloud Control Provider with the Pulumi AWS Provider

Let’s walk through an example of using the AWS Cloud Control Provider alongside the Pulumi's [standard AWS Provider]. This example shows how to create an S3 bucket with the standard AWS provider and deploy a Lambda function using the AWS Cloud Control provider. The Lambda function is set up to use the S3 bucket's name and process events accordingly. This example showcases how both providers can work together, leveraging the standard AWS Provider for widely supported resources, while using AWS Cloud Control for the latest features and APIs provided by AWS.

{{< chooser language "typescript,python,csharp,go,yaml" / >}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awscc from "@pulumi/aws-native";

// ARN of the IAM role that the Lambda function will assume
const roleArn = "arn:aws:iam::YOUR_ACCOUNT_ID:role/cloudcontrol-test";

// Create an S3 bucket using the AWS provider
const bucket = new aws.s3.Bucket("myBucket");

// Create the AWS Lambda function using the AWS Cloud Control provider
const lambdaFunction = new awscc.lambda.Function("myLambdaFunction", {
    functionName: "my-lambda-function",
    role: "arn:aws:iam::YOUR_ACCOUNT_ID:role/cloudcontrol-test",
    runtime: "nodejs18.x",
    handler: "index.handler",
      code: {
        zipFile: `
            exports.handler = async function(event) {
                const bucketName = process.env.BUCKET_NAME;
                console.log("Event triggered: ", JSON.stringify(event, null, 2));
                return {
                    statusCode: 200,
                    body: JSON.stringify('Hello from Lambda!'),
                };
            };
        `,
    },
    environment: {
        variables: {
            BUCKET_NAME: bucket.bucket,
        },
    },
});

// Export the Lambda function ARN and the S3 bucket name
export const lambdaFunctionArn = lambdaFunction.arn;
export const s3BucketName = bucket.bucket;
```
{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_aws_native as aws_cloudcontrol
# Create an S3 bucket using the standard AWS provider
my_bucket = aws.s3.Bucket("myBucket")

# Create the Lambda function using the AWS Cloud Control provider
my_lambda_function = aws_cloudcontrol.lambda_.Function("myLambdaFunction",
    function_name="my-lambda-function",
    role="arn:aws:iam::YOUR_ACCOUNT_ID:role/cloudcontrol-test",
    runtime="nodejs18.x",
    handler="index.handler",
    code={
        "zip_file": """exports.handler = async function(event) {
    const bucketName = process.env.BUCKET_NAME;
    console.log("Event triggered: ", JSON.stringify(event, null, 2));
    return {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
};
""",
    },
    environment={
        "variables": {
            "BUCKET_NAME": my_bucket.bucket,
        },
    })
pulumi.export("lambdaFunctionArn", my_lambda_function.arn)  # Directly export the value, no need for a dictionary
pulumi.export("s3BucketName", my_bucket.bucket)
```
{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Aws = Pulumi.Aws;
using AwsCloudControl = Pulumi.AwsNative;

return await Deployment.RunAsync(() =>
{
    // Create an S3 bucket
    var myBucket = new Aws.S3.Bucket("myBucket");

   // Create a Lambda function using AWS Cloud Control
    var myLambdaFunction = new AwsCloudControl.Lambda.Function("myLambdaFunction", new()
    {
        FunctionName = "my-lambda-function",
        Role = "arn:aws:iam::YOUR_ACCOUNT_ID:role/cloudcontrol-test",
        Runtime = "nodejs18.x",
        Handler = "index.handler",
        Code = new AwsCloudControl.Lambda.Inputs.FunctionCodeArgs
        {
            ZipFile = @"exports.handler = async function(event) {
    const bucketName = process.env.BUCKET_NAME;
    console.log(""Event triggered: "", JSON.stringify(event, null, 2));
    return {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
};
",
        },
        Environment = new AwsCloudControl.Lambda.Inputs.FunctionEnvironmentArgs
        {
            Variables =
            {
                { "BUCKET_NAME", myBucket.BucketName },
            },
        },
    });

    // Export the Lambda function ARN and the S3 bucket name directly
    return new Dictionary<string, object?>
    {
        ["lambdaFunctionArn"] =  myLambdaFunction.Arn,
        ["s3BucketName"] = myBucket.BucketName,
        };
});
```
{{% /choosable %}}
{{% choosable language go %}}

```go

package main

import (
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/lambda"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an S3 bucket using the standard AWS provider
		myBucket, err := s3.NewBucket(ctx, "myBucket", nil)
		if err != nil {
			return err
		}
		// Create a Lambda function using AWS Cloud Control provider
		myLambdaFunction, err := lambda.NewFunction(ctx, "myLambdaFunction", &lambda.FunctionArgs{
			FunctionName: pulumi.String("my-lambda-function"),
			Role:         pulumi.String("arn:aws:iam::YOUR_ACCOUNT_ID:role/cloudcontrol-test"),
			Runtime:      pulumi.String("nodejs18.x"),
			Handler:      pulumi.String("index.handler"),
			Code: &lambda.FunctionCodeArgs{
ZipFile: pulumi.String(`exports.handler = async function(event) {
    const bucketName = process.env.BUCKET_NAME;
    console.log("Event triggered: ", JSON.stringify(event, null, 2));
    return {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
};
`),
			},
			Environment: &lambda.FunctionEnvironmentArgs{
				Variables: pulumi.StringMap{
					"BUCKET_NAME": myBucket.Bucket,
				},
			},
		})
		if err != nil {
			return err
		}
		// Export the Lambda function's ARN so that it can be referenced later
		ctx.Export("lambdaFunctionArn",myLambdaFunction.Arn)
		// Export the S3 bucket name so it can be used in other parts of the infrastructure
		ctx.Export("s3BucketName", myBucket.Bucket)
		return nil
	})
}
```
{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
name: your-project-name   # Replace with your project name
runtime: yaml

resources:
# Creating an S3 bucket using the standard AWS provider.
  myBucket:
    type: aws:s3/bucket:Bucket
    properties: {}

# Creating a Lambda function using the AWS Cloud Control provider.
  myLambdaFunction:
    type: aws-native:lambda:Function
    properties:
      functionName: my-lambda-function
      role: arn:aws:iam::YOUR_ACCOUNT_ID:role/cloudcontrol-test
      runtime: nodejs18.x
      handler: index.handler
      code:
        zipFile: |
          exports.handler = async function(event) {
              const bucketName = process.env.BUCKET_NAME;
              console.log("Event triggered: ", JSON.stringify(event, null, 2));
              return {
                  statusCode: 200,
                  body: JSON.stringify('Hello from Lambda!'),
              };
          };
# Lambda environment variables are set here.
      environment:
        variables:
          BUCKET_NAME: ${myBucket.bucket}

# Outputs section - Pulumi will output these values after deployment.
outputs:
  lambdaFunctionArn:
    value: ${myLambdaFunction.arn}
  s3BucketName:
    value: ${myBucket.bucket}
```
{{% /choosable %}}

## Leveraging AWS Cloud Control Provider for Advanced WAFv2 Configurations

The [AWS Cloud Control Provider] offers greater flexibility for handling complex configurations that may be challenging or impossible with the [standard AWS Provider]. For example, when configuring WAFv2, you can define arbitrary nested rules, which enables more advanced and customized security logic. With the Cloud Control Provider, you can compose these rules with reusable building blocks, creating configurations that are more modular and scalable. This level of granularity allows for more precise control over web traffic filtering, such as combining multiple rule sets, applying conditions across different layers of the request, and creating highly tailored security policies. This flexibility is particularly useful for organizations with complex security requirements that need to go beyond what the standard AWS Provider can offer.

For example, this configuration involves six levels of nesting rules but can be composed from reusable building blocks:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awscc from "@pulumi/aws-native";

type RuleGroupStatement = awscc.types.input.wafv2.RuleGroupStatementArgs;

// Create an AWS WAFv2 IP Set
const exampleIPSet = new awscc.wafv2.IpSet("exampleIPSet", {
  addresses: ["1.2.3.4/32", "5.6.7.8/32"],
  ipAddressVersion: "IPV4",
  scope: "REGIONAL",
});

const ipMatch: RuleGroupStatement = {
  ipSetReferenceStatement: {
    arn: exampleIPSet.arn,
  },
};

const testURIMatch: RuleGroupStatement = {
  byteMatchStatement: {
    searchString: "/test",
    fieldToMatch: {
      uriPath: {},
    },
    textTransformations: [
      {
        priority: 0,
        type: "NONE",
      },
    ],
    positionalConstraint: "EXACTLY",
  },
};

const hostMatch: RuleGroupStatement = {
  byteMatchStatement: {
    fieldToMatch: {
      singleHeader: {
        name: "host",
      },
    },
    positionalConstraint: "EXACTLY",
    searchString: "example.com",
    textTransformations: [
      {
        type: "NONE",
        priority: 0,
      },
    ],
  },
};

const internalLabelMatch: RuleGroupStatement = {
  labelMatchStatement: {
    scope: "LABEL",
    key: "internal",
  },
};
const xssMatch: RuleGroupStatement = {
  xssMatchStatement: {
    fieldToMatch: {
      body: {},
    },
    textTransformations: [
      {
        priority: 0,
        type: "NONE",
      },
    ],
  },
};

function matchNot(statement: RuleGroupStatement): RuleGroupStatement {
  return { notStatement: { statement } };
}

function matchAll(statements: RuleGroupStatement[]): RuleGroupStatement {
  return { andStatement: { statements: statements } };
}

function matchAny(statements: RuleGroupStatement[]): RuleGroupStatement {
  return { orStatement: { statements: statements } };
}

// Create an AWS WAFv2 Rule Group
const exampleRuleGroup = new awscc.wafv2.RuleGroup("exampleRuleGroup", {
  capacity: 2000,

  rules: [
    {
      action: { allow: {} },
      name: "rule-1",
      priority: 1,
      statement: matchAny([
        matchAll([ipMatch, xssMatch]),
        matchNot(
          matchAny([
            testURIMatch,
            matchAll([
              internalLabelMatch,
              matchNot(matchAll([ipMatch, hostMatch])),
            ]),
          ]),
        ),
      ]),

      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: "friendly-rule-metric-name",
        sampledRequestsEnabled: true,
      },
    },
  ],
  scope: "REGIONAL",
  visibilityConfig: {
    cloudWatchMetricsEnabled: true,
    metricName: "friendly-metric-name",
    sampledRequestsEnabled: true,
  },
});

// Create an AWS WAFv2 WebACL
const exampleWebACL = new awscc.wafv2.WebAcl("exampleWebACL", {
  defaultAction: { allow: {} },
  rules: [
    {
      name: "example-rule-1",
      overrideAction: { count: {} },
      priority: 1,
      statement: {
        ruleGroupReferenceStatement: {
          arn: exampleRuleGroup.arn,
        },
      },
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: "friendly-rule-metric-name",
        sampledRequestsEnabled: true,
      },
    },
  ],
  scope: "REGIONAL",
  visibilityConfig: {
    cloudWatchMetricsEnabled: true,
    metricName: "friendly-metric-name",
    sampledRequestsEnabled: true,
  },
});
```

## Conclusion

The [AWS Cloud Control Provider] for Pulumi is a major step forward in fully and faithfully supporting the AWS Cloud Control API and its ecosystem in Pulumi. By closely collaborating with AWS, we’ve created a provider that enables Pulumi users to leverage the latest AWS features as soon as they are released - without waiting for upstream provider changes to arrive in the standard Pulumi AWS Provider.

Our goal is to continually improve and simplify the Pulumi experience, empowering developers with the tools they need to manage cloud infrastructure seamlessly. This new provider represents our commitment to delivering cutting-edge capabilities as quickly as possible.

We look forward to your feedback and encourage you to explore the full potential of the Pulumi AWS Cloud Control Provider. Don’t hesitate to reach out via our [Pulumi AWS Cloud Control Provider GitHub repository](https://github.com/pulumi/pulumi-aws-native) with any questions or suggestions as we continue to refine and enhance this experience.

[AWS Cloud Control Provider]: https://www.pulumi.com/registry/packages/aws-native/
[Pulumi AWS Provider]: https://www.pulumi.com/registry/packages/aws/
[Standard AWS Provider]: https://www.pulumi.com/registry/packages/aws/
[AWS Cloud Control API]: https://aws.amazon.com/cloudcontrolapi/
