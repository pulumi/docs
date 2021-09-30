---
title: AWS-Native
meta_desc: 'This page provides an overview of the AWS Native Provider for Pulumi: AWS-Native.'
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-aws-native
    weight: 1

aliases: ["/docs/reference/clouds/aws-native/"]
---
{{% notes type="info" %}}
The AWS Native provider is currently in public preview
{{% /notes %}}

<img src="/logos/tech/aws.svg" align="right" class="h-16 px-8 pb-4">

The AWS Native provider offers same-day support for all new AWS features and releases covered by the newly released AWS Cloud Control API, which typically supports new AWS features on the day of launch. Resources available in the Pulumi AWS Native provider are based on the resources defined in the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html).  Today, hundreds of AWS resources are available from this registry via Cloud Control API and the Pulumi AWS Native provider. As AWS Cloud Control API adds additional coverage for resources in the CloudFormation Registry, AWS Native provider will pick them up and continue to expand its coverage.

The AWS Native provider must be configured with credentials to deploy and update resources in AWS.

See the [full API documentation]({{< relref "/docs/reference/pkg/aws-native" >}}) for complete details of the available AWS Native provider APIs and resource coverage.

## Setup

The AWS Native provider supports several options for providing access to AWS credentials.  See [AWS Native setup page]({{< relref "setup" >}}) for details.

## Getting Started

{{< youtube oKxaZCyu2OQ >}}

Some [examples](https://github.com/pulumi/pulumi-aws-native/tree/master/examples) are available complete with instructions to try AWS Native provider in action. Also note that the AWS Native provider interoperates seemlessly with [AWS Classic provider]({{< relref "/docs/reference/pkg/aws" >}}) as illustrated by the following example:

## Example

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsclassic from "@pulumi/aws";
import * as awsnative from "@pulumi/aws-native";

const bucket = new awsclassic.s3.Bucket("source");
const checkpointObject = new awsclassic.s3.BucketObject("checkpoint", {
   bucket: bucket.id,
   key: "dev.json",
   source: new pulumi.asset.FileAsset("stack.json"),
});

const accessPoint = new awsclassic.s3.AccessPoint("ap", {
   bucket: bucket.id,
});

const objectlambda = new awsnative.s3objectlambda.AccessPoint("objectlambda-ap", {
   objectLambdaConfiguration: {
       supportingAccessPoint: accessPoint.arn,
       transformationConfigurations: [{
           actions: ["GetObject"],
           contentTransformation: {
               AwsLambda: {
                   FunctionArn: fn.arn,
               },
           },
       }]
   }
});

```

More examples of using AWS Native will be available in [the Pulumi examples repo](https://github.com/pulumi/examples) soon.

## Libraries

The following packages are available in package managers:

* JavaScript/TypeScript: [`@pulumi/aws-native`](https://www.npmjs.com/package/@pulumi/aws-native)
* Python: [`pulumi-aws-native`](https://pypi.org/project/pulumi-aws-native/)
* Go: [`github.com/pulumi/pulumi-aws-native/sdk/go/aws`](https://github.com/pulumi/pulumi-aws-native/tree/master/sdk/go/aws)
* .NET: [`Pulumi.AwsNative`](https://www.nuget.org/packages/Pulumi.AwsNative)

The AWS Native provider is open source and available in the [pulumi/pulumi-aws-native](https://github.com/pulumi/pulumi-aws-native) repo.

## Configuration

The AWS Native provider accepts the following configuration settings.  These can be provided to the default AWS Native provider via `pulumi config set aws-native:<option>`, or explicitly passed to the constructor (if supported) in your chosen language to construct a specific instance of the AWS Native provider.

* `region`: (Required) The region where AWS operations will take place. Examples are `us-east-1`, `us-west-2`, etc. It can also be sourced from the following environment variables: `AWS_REGION`, `AWS_DEFAULT_REGION`.
* `accessKey`: (Optional) The access key for API operations. You can retrieve this from the ‘Security & Credentials’ section of the AWS console. It can also be sourced from the following environment variable: `AWS_ACCESS_KEY_ID`
* `assumeRole`: (Optional) A JSON object representing an IAM role to assume.  To set these nested properties, see docs on  [structured configuration]({{< relref "/docs/intro/concepts/config#structured-configuration">}}), for example `pulumi config set --path aws-native:assumeRole.roleArn arn:aws:iam::058111598222:role/OrganizationAccountAccessRole`.  The object contains the following properties:
  * `durationSeconds`: (Optional) Number of seconds to restrict the assume role session duration.
  * `externalId`: (Optional) External identifier to use when assuming the role.
  * `policy`: (Optional) IAM Policy JSON describing further restricting permissions for the IAM Role being assumed.
  * `policyArns`: (Optional) Set of Amazon Resource Names (ARNs) of IAM Policies describing further restricting permissions for the IAM Role being assumed.
  * `roleArn`: (Optional) Amazon Resource Name (ARN) of the IAM Role to assume.
  * `sessionName`: (Optional) Session name to use when assuming the role.
  * `tags`: (Optional) Map of assume role session tags.
  * `transitiveTagKeys`: (Optional) A list of keys for session tags that you want to set as transitive. If you set a tag key as transitive, the corresponding key and value passes to subsequent sessions in a role chain.
* `profile`: (Optional) The profile for API operations. If not set, the default profile created with `aws configure` will be used. It can also be sourced from the following environment variable: `AWS_PROFILE`
* `secretKey`: (Optional) The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console. It can also be sourced from the following environment variable: `AWS_SECRET_ACCESS_KEY`
* `sharedCredentialsFile`: (Optional) The path to the shared credentials file. If not set this defaults to the `credentials` file in your home directory. It can also be sourced from the following environment variable: `AWS_SHARED_CREDENTIALS_FILE`
* `token`: (Optional) Session token for validating temporary credentials. Typically provided after successful identity federation or Multi-Factor Authentication (MFA) login. With MFA login, this is the session token provided afterward, not the 6 digit MFA code used to get temporary credentials. It can also be sourced from the following environment variable: `AWS_SESSION_TOKEN`

<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/105
* `allowedAccountIds`: (Optional) List of allowed AWS account IDs to prevent you from mistakenly using an incorrect one (and potentially end up destroying a live environment). Conflicts with `forbiddenAccountIds`.
* -->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/107
* `defaultTags`: (Optional) Configuration block with resource tag settings to apply across all resources handled by this provider. This is designed to replace redundant per-resource `tags` configurations. Provider tags can be overridden with new values, but not excluded from specific resources. To override provider tag values, use the `tags` argument within a resource to configure new tag values for matching keys.
  * `tags`: A key value pair of tags to apply across all resources.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/108
* `endpoints`: (Optional) Configuration block for customizing service endpoints.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/109
* `forbiddenAccountIds`: (Optional) List of forbidden AWS account IDs to prevent you from mistakenly using the wrong one (and potentially end up destroying a live environment). Conflicts with `allowedAccountIds`.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/110
* `ignoreTags`: (Optional) Configuration block with resource tag settings to ignore across all resources handled by this provider (except any individual service tag resources such as `ec2.Tag`) for situations where external systems are managing certain resource tags.
  * `keys`: A list of exact resource tag keys to ignore across all resources handled by this provider. This configuration prevents Pulumi from returning the tag in any `tags` properties and displaying any diffs for the tag value. If any resource still has this tag key configured in the `tags` argument, it will display a perpetual diff until the tag is removed from the argument or `ignoreChanges` is also used.
  * `keyPrefixes`: A list of resource tag key prefixes to ignore across all resources handled by this provider. This configuration prevents Pulumi from returning the tag in any `tags` properties and displaying any diffs for the tag value. If any resource still has this tag key configured in the `tags` argument, it will display a perpetual diff until the tag is removed from the argument or `ignoreChanges` is also used.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/111
* `insecure`: (Optional) Explicitly allow the provider to perform "insecure" SSL requests. If omitted, the default value is `false`.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/112
* `maxRetries`: (Optional) The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/113
* `s3ForcePathStyle`: (Optional) Set this to true to force the request to use path-style addressing, i.e., `http://s3.amazonaws.com/BUCKET/KEY`. By default, the S3 client will use virtual hosted bucket addressing when possible (`http://BUCKET.s3.amazonaws.com/KEY`). Specific to the Amazon S3 service.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/114
* `skipCredentialsValidation`: (Optional) Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS available/implemented.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/115
* `skipGetEc2Platforms`: (Optional) Skip getting the supported EC2 platforms. Used by users that don't have `ec2:DescribeAccountAttributes` permissions.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/116
* `skipMetadataApiCheck`: (Optional) Skip the AWS Metadata API check. Useful for AWS API implementations that do not have a metadata API endpoint. Setting to true prevents Pulumi from authenticating via the Metadata API. You may need to use other authentication methods like static credentials, configuration variables, or environment variables.
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/117
* `skipRegionValidation`: (Optional) Skip static validation of region name. Used by users of alternative AWS-like APIs or users w/ access to regions that are not public (yet).
-->
<!-- Not supported: https://github.com/pulumi/pulumi-aws-native/issues/118
* `skipRequestingAccountId`: (Optional) Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.
-->

In addition, several more configuration options are planned to be added soon to provide parity with the [Classic AWS provider]({{< relref "/docs/reference/pkg/aws" >}}), check the [Github Issues](https://github.com/pulumi/pulumi-aws-native/issues?q=is%3Aissue+is%3Aopen+label%3Aprovider-config) for more details.
