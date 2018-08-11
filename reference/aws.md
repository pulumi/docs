---
title: "AWS"
---

The Amazon Web Services (AWS) provider for Pulumi can be used to provision any of the cloud resources available in [AWS](https://aws.amazon.com/).  The AWS provider must be configured with credentials to deploy and update resources in AWS. 

See the [full API documentation](./pkg/nodejs/@pulumi/aws/index.html) for complete details of the available AWS provider APIs.

## Example

```javascript
const aws = require("@pulumi/aws");

const bucket = new aws.s3.Bucket("mybucket", {});
```

You can find additional examples of using AWS in [the Pulumi examples repo](https://github.com/pulumi/examples).
The [Quickstart Tutorials](/quickstarts) also cover a lot of AWS concepts, including
[containers](https://pulumi.io/quickstart/aws-containers.html),
[serverless functions](https://pulumi.io/quickstart/aws-rest-api.html),
[infrastructure](https://pulumi.io/quickstart/aws-ec2.html), and the
[intersection of all three](https://pulumi.io/quickstart/aws-extract-thumbnail.html).

## Libraries

The following pacakges are available in pacakge managers:
* JavaScript/TypeScript: https://www.npmjs.com/package/@pulumi/aws
* Python: https://pypi.org/project/pulumi-aws/
* Go: `github.com/pulumi/pulumi-aws/sdk/go/aws`

The AWS provider is open source and available in the [pulumi/pulumi-aws](https://github.com/pulumi/pulumi-aws) repo. 

## Authentication

The AWS provider supports several options for providing access to AWS credentials.  See [AWS installation page](/install/aws.html) for details.

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
