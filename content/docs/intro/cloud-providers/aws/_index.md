---
title: AWS
meta_desc: This page provides an overview of the AWS Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-aws
    weight: 1

aliases: ["/docs/reference/clouds/aws/"]
---

<img src="/logos/tech/aws.svg" align="right" class="h-16 px-8 pb-4">

The Amazon Web Services (AWS) provider for Pulumi can be used to provision any of the cloud resources available in [AWS](https://aws.amazon.com/).  The AWS provider must be configured with credentials to deploy and update resources in AWS.

See the [full API documentation]({{< prelref "/docs/reference/pkg/aws" >}}) for complete details of the available AWS provider APIs.

Additionally, higher-level libraries offering simpler interfaces and higher-productivity APIs for many areas of AWS are available in the [awsx]({{< prelref "/docs/reference/pkg/nodejs/pulumi/awsx" >}}) and [eks]({{< prelref "/docs/reference/pkg/nodejs/pulumi/eks" >}}) packages.

## Setup

The AWS provider supports several options for providing access to AWS credentials.  See [AWS setup page]({{< prelref "setup" >}}) for details.

## Getting Started

The quickest way to get started with AWS is to follow the [Get Started]({{< prelref "/docs/get-started/aws" >}}) guide.

Additionally, there are several tutorials available to follow:

* [Containers on ECS "Fargate"]({{< prelref "/docs/tutorials/aws/ecs-fargate" >}}): Deploy containers to Amazon
* [EC2 Linux WebServer VM]({{< prelref "/docs/tutorials/aws/ec2-webserver" >}}): Create an EC2 Linux Web Server virtual machine
* [Serverless REST API Gateways using Lambda]({{< prelref "/docs/tutorials/aws/rest-api" >}}): Create simple RESTful web server using AWS Lambdas
* [Serve a Static Website from S3]({{< prelref "/docs/tutorials/aws/s3-website" >}}): Serve a static website out of content in an S3 bucket
* [Serverless + Containers + Infrastructure]({{< prelref "/docs/tutorials/aws/video-thumbnailer" >}}): Deploy a complete  application using a combination of buckets, serverless functions and containers.

In addition to the tutorials, several interesting examples are available complete with instructions:

* [Ruby on Rails in EC2](https://github.com/pulumi/examples/tree/master/aws-ts-ruby-on-rails): Run a Ruby on Rails
    WebServer using EC2 instances
* [SQS-Triggered Lambdas](https://github.com/pulumi/examples/tree/master/aws-js-sqs-slack): Post to Slack using a Lambda
    anytime a SQS message arrives
* [Static Website in CloudFront and S3](https://github.com/pulumi/examples/tree/master/aws-ts-static-website): Create a
    static website serving content out of S3, fronted by a CloudFront CDN
* [Provision an Elastic Kubernetes Service Cluster](https://github.com/pulumi/examples/tree/master/aws-ts-eks): Stand up
    a managed EKS cluster

## Introducing Pulumi Crosswalk for AWS

<a href="{{< prelref "/docs/guides/crosswalk/aws" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" width="150" align="right" style="margin-left: 16px">
</a>

Use Pulumi Crosswalk for AWS to easily use the best of what AWS has to offer, with
well-architected best practices, for the entire AWS cloud. Go to production
with containers, Kubernetes, and serverless applications.

<a href="{{< prelref "/docs/guides/crosswalk/aws" >}}">Get Started with Crosswalk for AWS Now</a>

## Example

```javascript
const aws = require("@pulumi/aws");

const bucket = new aws.s3.Bucket("mybucket");
```

You can find additional examples of using AWS in [the Pulumi examples repo](https://github.com/pulumi/examples).

## Libraries

The following packages are available in package managers:

* JavaScript/TypeScript: [`@pulumi/aws`](https://www.npmjs.com/package/@pulumi/aws)
* Python: [`pulumi-aws`](https://pypi.org/project/pulumi-aws/)
* Go: [`github.com/pulumi/pulumi-aws/sdk/go/aws`](https://github.com/pulumi/pulumi-aws)
* .NET: [`Pulumi.Aws`](https://www.nuget.org/packages/Pulumi.Aws)

The AWS provider is open source and available in the [pulumi/pulumi-aws](https://github.com/pulumi/pulumi-aws) repo.

## Configuration

The AWS provider accepts the following configuration settings.  These can be provided to the default AWS provider via `pulumi config set aws:<option>`, or passed to the constructor of `new aws.Provider` to construct a specific instance of the AWS provider.

* `region`: (Required) The region where AWS operations will take place. Examples are `us-east-1`, `us-west-2`, etc.
* `accessKey`: (Optional) The access key for API operations. You can retrieve this from the ‘Security & Credentials’ section of the AWS console.
* `dynamodbEndpoint`: (Optional) Use this to override the default endpoint URL constructed from the `region`. It’s typically used to connect to dynamodb-local.
* `insecure`: (Optional) Explicitly allow the provider to perform "insecure" SSL requests. If omitted, the default value is `false`.
* `kinesisEndpoint`: (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to kinesalite.
* `maxRetries`: (Optional) The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown.
* `profile`: (Optional) The profile for API operations. If not set, the default profile created with `aws configure` will be used.
* `s3ForcePathStyle`: (Optional) Set this to true to force the request to use path-style addressing, i.e., `http://s3.amazonaws.com/BUCKET/KEY`. By default, the S3 client will use virtual hosted bucket addressing when possible (`http://BUCKET.s3.amazonaws.com/KEY`). Specific to the Amazon S3 service.
* `secretKey`: (Optional) The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
* `sharedCredentialsFile`: (Optional) The path to the shared credentials file. If not set this defaults to `~/.aws/credentials`.
* `skipCredentialsValidation`: (Optional) Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS available/implemented.
* `skipGetEc2Platforms`: (Optional) Skip getting the supported EC2 platforms. Used by users that don't have `ec2:DescribeAccountAttributes` permissions.
* `skipMetadataApiCheck`: (Optional) Skip the AWS Metadata API check. Useful for AWS API implementations that do not have a metadata API endpoint. Setting to true prevents Terraform from authenticating via the Metadata API. You may need to use other authentication methods like static credentials, configuration variables, or environment variables.
* `skipRegionValidation`: (Optional) Skip static validation of region name. Used by users of alternative AWS-like APIs or users w/ access to regions that are not public (yet).
* `skipRequestingAccountId`: (Optional) Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.
* `token`: (Optional) Use this to set an MFA token. It can also be sourced from the `AWS_SESSION_TOKEN` environment variable.
