---
title: "Deploying Lambda Function URLs"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-04-06T13:00:03-07:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
meta_desc: Today, the AWS team announced HTTPS endpoint support for your Lambda functions. Learn how to deploy a Lambda URL with Pulumi!

meta_image: aws_meta.png

authors:
  - kat-cosgrove

tags:
  - aws
  - features
  - launches
---

Since its introduction in 2014, the AWS Lambda service has steadily grown from ‘functions as a service’ to a powerful serverless platform that enables cloud engineers to run code without provisioning or managing underlying infrastructure.

<!--more-->

In the past 18 months, the platform has expanded to include support for [persistent storage using Amazon Elastic File System (EFS)](https://www.pulumi.com/blog/aws-lambda-efs) as well as [container-based functions](https://www.pulumi.com/blog/aws-lambda-container-support). More recently, the team added support for [AWS Graviton2 processors](https://www.pulumi.com/blog/aws-lambda-functions-powered-by-graviton2) - improving the price performance of AWS Lambda functions.

Today, the AWS team announced [AWS Lambda Function URLs](http://aws.amazon.com/blogs/aws/announcing-aws-lambda-function-urls-built-in-https-endpoints-for-single-function-microservices) - HTTPS endpoint support for your Lambda functions. This means that once you’ve added and configured a function URL, you can invoke your Lambda function from a webapp, curl, Postman, or whatever HTTP client you prefer. It’s also our first feature to take full advantage of the new [AWS Cloud Control API](https://aws.amazon.com/cloudcontrolapi) for same-day feature support.

### Why Use Function URLs for AWS Lambda?

Embedding URL support into Lambda functions is a big productivity boost compared to alternative methods such as configuring Amazon API Gateway to provide an HTTPS endpoint for your Lambda functions. Here are some common use cases for configuring, monitoring, and observing your function URLs:

#### Easy-to-configure monitoring

Since AWS Lambda is integrated with AWS CloudTrail, you can view recent events in event history or deliver CloudTrail events to an Amazon S3 bucket. For each request to AWS Lambda authorized via IAM, you can track useful information such as the IP address and the user/role or the requestor. Aggregated metrics are also sent to Amazon CloudWatch - enabling you to track the number of requests to each URL, errors by status code (4xx and 5xx), and function latency.

#### Simplified throttling

You can configure [reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) to prevent abuse of your function or avoid overloading down-stream resources. By setting reserved concurrency to zero, you can even disable your URL completely.

#### Simple access controls

By default, Lambda URLs use AWS Identity and Access Management (IAM) for authorization, but you can also disable IAM authentication - enabling your function code to handle auth however you like. Function URLs also support Cross Origin Resource Sharing configuration options.

In short, Lambda Function URLs give you an easier way to configure, deploy and manage an HTTPS endpoint for your functions than setting up a full API Gateway. If you need more advanced options such as [per-client throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html), then it’s worth exploring API Gateway features for managing endpoints for your Lambda functions.

### Example: Setting up an AWS Lambda Function URL

Ready to try out Function URLs for yourself? A function URL can be applied to any function alias from the AWS Console, CLI, or other Lambda API -- including from your Pulumi programs! Let’s see what that looks like:

{{< chooser language "typescript, python, csharp, go" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsnative from "@pulumi/aws-native";

const lambdaRole = new awsnative.iam.Role("lambdaRole", {
  assumeRolePolicyDocument: {
    Version: "2012-10-17",
    Statement: [
      {
        Action: "sts:AssumeRole",
        Principal: {
          Service: "lambda.amazonaws.com",
        },
        Effect: "Allow",
        Sid: "",
      },
    ],
  },
});

const lambdaRoleAttachment = new aws.iam.RolePolicyAttachment(
  "lambdaRoleAttachment",
  {
    role: pulumi.interpolate`${lambdaRole.roleName}`,
    policyArn: aws.iam.ManagedPolicy.AWSLambdaBasicExecutionRole,
  }
);

const helloFunction = new awsnative.lambda.Function("helloFunction", {
  role: lambdaRole.arn,
  runtime: "nodejs14.x",
  handler: "index.handler",
  code: {
    zipFile: `exports.handler = function(event, context, callback){ callback(null, {"response": "Hello "}); };`,
  },
});

const lambdaUrl = new awsnative.lambda.Url("test", {
  targetFunctionArn: helloFunction.arn,
  authType: awsnative.lambda.UrlAuthType.None,
});

export const url = lambdaUrl.functionUrl;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import json
import pulumi
import pulumi_aws as aws
import pulumi_aws_native as aws_native

lambda_role = aws_native.iam.Role("lambda_role",
                                  assume_role_policy_document=json.dumps({
                                      "Version": "2012-10-17",
                                      "Statement": [
                                          {
                                              "Action": "sts:AssumeRole",
                                              "Principal": {
                                                  "Service": "lambda.amazonaws.com",
                                              },
                                              "Effect": "Allow",
                                              "Sid": "",
                                          },
                                      ],
                                  })
                                  )

lambda_role_attachment = aws.iam.RolePolicyAttachment("lambda_role_attachment",
                                                      role=pulumi.Output.concat(
                                                          lambda_role.role_name),
                                                      policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
                                                      )

hello_function = aws_native.lambda_.Function("test",
                                             runtime="nodejs14.x",
                                             role=lambda_role.arn,
                                             handler="index.handler",
                                             code=aws_native.lambda_.FunctionCodeArgs(
                                                 zip_file="exports.handler = function(event, context, callback){ callback(null, {'response': 'Hello'}); };",
                                             ),
                                             )

lambda_url = aws_native.lambda_.Url("test",
                                    target_function_arn=hello_function.arn,
                                    auth_type=aws_native.lambda_.UrlAuthType.NONE
                                    )

pulumi.export("url", lambda_url.function_url)

```

{{% /choosable %}}

{{% choosable language csharp%}}

```csharp
using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;
using AwsNative = Pulumi.AwsNative;

class MyStack : Stack
{
    public MyStack()
    {
        var lambdaRole = new AwsNative.IAM.Role("lambdaRole", new AwsNative.IAM.RoleArgs
        {
            AssumeRolePolicyDocument = JsonSerializer.Serialize(new Dictionary<string, object?>
            {
                { "Version", "2012-10-17" },
                { "Statement", new[]
                    {
                        new Dictionary<string, object?>
                        {
                            { "Action", "sts:AssumeRole" },
                            { "Effect", "Allow" },
                            { "Sid", "" },
                            { "Principal", new Dictionary<string, object?>
                            {
                                { "Service", "lambda.amazonaws.com" },
                            } },
                        },
                    }
                 },
            }),
        });

        var lambdaRoleAttachment = new Aws.Iam.RolePolicyAttachment("lambdaRoleAttachment", new Aws.Iam.RolePolicyAttachmentArgs
        {
            Role = Pulumi.Output.Format($"{lambdaRole.RoleName}"),
            PolicyArn = Aws.Iam.ManagedPolicy.AWSLambdaBasicExecutionRole.ToString()
        });

        var helloFunction = new AwsNative.Lambda.Function("hellofunction", new AwsNative.Lambda.FunctionArgs
        {
            Role = lambdaRole.Arn,
            Runtime = "nodejs14.x",
            Handler = "index.handler",
            Code = new AwsNative.Lambda.Inputs.FunctionCodeArgs
            {
                ZipFile = "exports.handler = function(event, context, callback){ callback(null, {\"response\": \"Hello \"}); };"
            }
        });

        var lambdaUrl = new AwsNative.Lambda.Url("test", new AwsNative.Lambda.UrlArgs
        {
            TargetFunctionArn = helloFunction.Arn,
            AuthType = AwsNative.Lambda.UrlAuthType.None
        });

        this.Url = lambdaUrl.FunctionUrl;
    }

    [Output]
    public Output<string> Url { get; set; }
}

```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/iam"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/lambda"
	awsiam "github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		lambdaAssumeRolePolicy, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				map[string]interface{}{
					"Action": "sts:AssumeRole",
					"Effect": "Allow",
					"Sid":    "",
					"Principal": map[string]interface{}{
						"Service": "lambda.amazonaws.com",
					},
				},
			}})
		if err != nil {
			return err
		}

		lambdaRole, err := iam.NewRole(ctx, "lambdaRole", &iam.RoleArgs{
			AssumeRolePolicyDocument: pulumi.String(lambdaAssumeRolePolicy),
		})
		if err != nil {
			return err
		}

		_, err = awsiam.NewRolePolicyAttachment(ctx, "lambdaRoleAttachment", &awsiam.RolePolicyAttachmentArgs{
			Role:      lambdaRole.RoleName,
			PolicyArn: awsiam.ManagedPolicyAWSLambdaBasicExecutionRole,
		})
		if err != nil {
			return err
		}

		helloFunction, err := lambda.NewFunction(ctx, "helloFunction", &lambda.FunctionArgs{
			Role:    lambdaRole.Arn,
			Runtime: pulumi.String("nodejs14.x"),
			Handler: pulumi.String("index.handler"),
			Code: &lambda.FunctionCodeArgs{
				ZipFile: pulumi.String("exports.handler = function(event, context, callback){ callback(null, {\"response\": \"Hello \"}); };"),
			},
		})
		if err != nil {
			return err
		}

		url, err := lambda.NewUrl(ctx, "test", &lambda.UrlArgs{
			TargetFunctionArn: helloFunction.Arn,
			AuthType:          lambda.UrlAuthTypeNone,
		})

		// Export the name of the bucket
		ctx.Export("url", url.FunctionUrl)
		return nil
	})
}

```

{{% /choosable %}}

In the above code, we’re doing a couple of things:

1. Creating a role for the Lambda function to use and assigning an AWS managed policy to it
1. Creating a Lambda function and configuring a function URL for it

Using Pulumi to do this brings your infrastructure into a format much more familiar for most developers. This approach will work for any of the modern programming languages Pulumi supports.

We’ve named the Lambda function `helloFunction`, selected a runtime of nodeJS, and given it a tiny bit of code to run -- a single function that, when called, returns “Hello.” Next, we’re giving it a function URL with no authorization and exporting the URL.

Run `pulumi up` and this is what we get:

```
    Type                           Name               Status
 +   pulumi:pulumi:Stack            functions-dev
 +   └─ aws-native:lambda:Url       test               created
Outputs:
  + url: "https://ppxrysls1a.lambda-url.eu-south-1.on.aws/"
```

Our function has a public endpoint! Hit it with curl (or just visit that URL in a browser) to make sure it works:

```
# curl $(pulumi stack output url)
{"response":"Hello "}
```

Success! A Lambda was created and a function URL was configured for it in just a few lines of code. The function URL allows us to invoke that Lambda from anywhere. Pretty neat!

### Conclusion

AWS Lambda functions are an incredibly easy and powerful way to stand up serverless capabilities which is why they are easily one of the most popular resources deployed by Pulumi users today. With the addition of Lambda Function URLs, end-users no longer need to set up an [Amazon API Gateway](https://aws.amazon.com/api-gateway) to provide an HTTPS endpoint for their functions - further simplifying deployments. You can learn more about Lambda Function URLs by reading the AWS and Pulumi documentation:

[Pulumi API Documentation](https://www.pulumi.com/registry/packages/aws-native/api-docs/lambda/url/)

[Configuring URLs](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-urls.html)

[Invoking URLs](https://docs.aws.amazon.com/lambda/latest/dg/invocation-urls.html)

[Payload format](https://docs.aws.amazon.com/lambda/latest/dg/invocation-urls.html#urls-payloads)
