---
title: "Announcing the General Availability of Pulumi’s AWS Cloud Control Provider (formerly AWS Native) "
allow_long_title: true
date: 2024-04-25T09:00:00-07:00
draft: false
meta_desc: >-
    Pulumi announces the GA of its AWS Cloud Control Provider, offering Day 1 support for new AWS features and enhancing cloud management tools.
meta_image: 
authors:
    - tejitha-raju
    - matt-jeffryes
tags:
    - aws 
    - provider 
    - cloudcontrol 
---
We're excited to announce the general availability of the new [AWS Cloud Control Provider] for Pulumi, previously AWS Native. AWS is one of the most-used cloud providers across the Pulumi ecosystem, and with this launch, we are focused on delivering Day 1 availability and faster access to new AWS capabilities to all Pulumi users. As part of this launch, we are also renaming the provider from “AWS Native” to "AWS Cloud Control Provider," based on customer feedback during the preview phase, to provide users with a broader range of advanced cloud management tools exposed by the AWS Cloud Control API. This provider includes the following features and benefits, 

* __Day 1 support for AWS Resources__: Provides full coverage of the [AWS Cloud Control API], typically on the day of the launch, ensuring users can adopt new features immediately. 
* __Complementary Pulumi Experience__: Works alongside Pulumi’s AWS Provider, enhancing Infrastructure as Code (IaC) projects with the latest AWS capabilities without requiring significant changes to existing setups. 
* __Extended support for third-party resources__: Our platform offers enhanced flexibility and interoperability by supporting third-party resources available in the CloudFormation Registry, such as Atlassian, MongoDB, Datadog, and more.
* __Easy CloudFormation to Pulumi Migration__: [cf2pulumi](https://www.pulumi.com/cf2pulumi/) provides the ability to migrate existing CloudFormation templates into Pulumi programs in your favorite language. 


At Pulumi, we're dedicated to empowering our customers with the tools they need to innovate and thrive in the cloud. The launch of the AWS Cloud Control Provider represents our unwavering commitment to providing best-in-class solutions that simplify cloud management, streamline operations, and drive business success. The Pulumi AWS Cloud Control Provider can be used side-by-side with the standard  Pulumi AWS provider and nearly 200  additional Pulumi resource providers that cover a wide variety of cloud and SaaS platforms.  

## Using Pulumi AWS Cloud Control Provider with the Pulumi AWS Provider

Let’s walk through an example of using Pulumi AWS Cloud Control Provider alongside the [standard AWS Provider]. Here, we can see how the new AWS S3 Object Lambda feature can be used via the AWS Cloud Control provider, with access to the full API defined by the S3 team at AWS.

```typescript
import * as pulumi from "@Pulumi Service (isabel)/pulumi";
import * as aws from "@Pulumi Service (isabel)/aws";
import * as awsx from "@Pulumi Service (isabel)/aws-native";

// Create an S3 bucket using the AWS provider
const bucket = new aws.s3.Bucket("myBucket");

// Define the Lambda function code
const lambdaCode = `
exports.handler = async (event) => {
    console.log("Processing new S3 object:", event.Records[0].s3.object.key);
    // Add your processing logic here
};
`;

// Create the AWS Lambda function using the AWS Cloud Control provider
const lambdaFunction = new awsx.lambda.Function("myLambdaFunction", {
    functionName: "my-lambda-function",
    runtime: "nodejs14.x",
    handler: "index.handler",
    code: new pulumi.asset.StringAsset(lambdaCode),
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

## Leveraging AWS Cloud Control Provider for Advanced WAFv2 Configurations

[The Cloud Control Provider] offers greater flexibility for handling complex configurations that may be challenging or impossible with the [standard AWS Provider]. For example, when configuring WAFv2, you can define arbitrary nested rules, which enables more advanced and customized security logic. With the Cloud Control Provider, you can compose these rules with reusable building blocks, creating configurations that are more modular and scalable. This level of granularity allows for more precise control over web traffic filtering, such as combining multiple rule sets, applying conditions across different layers of the request, and creating highly tailored security policies. This flexibility is particularly useful for organizations with complex security requirements that need to go beyond what the standard AWS Provider can offer.

For example, this configuration involves six levels of nesting rules but can be composed from reusable building blocks:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws_native from "@pulumi/aws-native";

type RuleGroupStatement = aws_native.types.input.wafv2.RuleGroupStatementArgs;

// Create an AWS WAFv2 IP Set
const exampleIPSet = new aws_native.wafv2.IpSet("exampleIPSet", {
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
const exampleRuleGroup = new aws_native.wafv2.RuleGroup("exampleRuleGroup", {
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
const exampleWebACL = new aws_native.wafv2.WebAcl("exampleWebACL", {
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

We look forward to your feedback and encourage you to explore the full potential of the Pulumi AWS Cloud Control Provider. Don’t hesitate to reach out via our [GitHub repository](https://github.com/pulumi/pulumi-aws-native) with any questions or suggestions as we continue to refine and enhance this experience.

[AWS Cloud Control Provider]: https://www.pulumi.com/registry/packages/aws-native/
[Pulumi AWS Provider]: https://www.pulumi.com/registry/packages/aws/
[standard AWS Provider]: https://www.pulumi.com/registry/packages/aws/
[AWS Cloud Control API]: https://aws.amazon.com/cloudcontrolapi/