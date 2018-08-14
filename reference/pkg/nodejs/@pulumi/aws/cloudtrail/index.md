---
title: Module cloudtrail
---

<a href="../index.html">@pulumi/aws</a> &gt; cloudtrail

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Trail">class Trail</a>
* <a href="#getServiceAccount">function getServiceAccount</a>
* <a href="#GetServiceAccountArgs">interface GetServiceAccountArgs</a>
* <a href="#GetServiceAccountResult">interface GetServiceAccountResult</a>
* <a href="#TrailArgs">interface TrailArgs</a>
* <a href="#TrailState">interface TrailState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/getServiceAccount.ts">cloudtrail/getServiceAccount.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts">cloudtrail/trail.ts</a> 


<h2 class="pdoc-module-header" id="Trail">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L11">class Trail</a>
</h2>

Provides a CloudTrail resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L91">constructor</a>
</h3>

```typescript
new Trail(name: string, args: TrailArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Trail resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TrailState): Trail
```


Get an existing Trail resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name of the trail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L32">property cloudWatchLogsGroupArn</a>
</h3>

```typescript
public cloudWatchLogsGroupArn: pulumi.Output<string | undefined>;
```


Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L37">property cloudWatchLogsRoleArn</a>
</h3>

```typescript
public cloudWatchLogsRoleArn: pulumi.Output<string | undefined>;
```


Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L42">property enableLogFileValidation</a>
</h3>

```typescript
public enableLogFileValidation: pulumi.Output<boolean | undefined>;
```


Specifies whether log file integrity validation is enabled.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L47">property enableLogging</a>
</h3>

```typescript
public enableLogging: pulumi.Output<boolean | undefined>;
```


Enables logging for the trail. Defaults to `true`.
Setting this to `false` will pause logging.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L51">property eventSelectors</a>
</h3>

```typescript
public eventSelectors: pulumi.Output<{ ... }[] | undefined>;
```


Specifies an event selector for enabling data event logging. Fields documented below. Please note the [CloudTrail limits](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html) when configuring these.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L55">property homeRegion</a>
</h3>

```typescript
public homeRegion: pulumi.Output<string>;
```


The region in which the trail was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L60">property includeGlobalServiceEvents</a>
</h3>

```typescript
public includeGlobalServiceEvents: pulumi.Output<boolean | undefined>;
```


Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L65">property isMultiRegionTrail</a>
</h3>

```typescript
public isMultiRegionTrail: pulumi.Output<boolean | undefined>;
```


Specifies whether the trail is created in the current
region or in all regions. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L69">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string | undefined>;
```


Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L73">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the trail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L77">property s3BucketName</a>
</h3>

```typescript
public s3BucketName: pulumi.Output<string>;
```


Specifies the name of the S3 bucket designated for publishing log files.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L82">property s3KeyPrefix</a>
</h3>

```typescript
public s3KeyPrefix: pulumi.Output<string | undefined>;
```


Specifies the S3 key prefix that precedes
the name of the bucket you have designated for log file delivery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L87">property snsTopicName</a>
</h3>

```typescript
public snsTopicName: pulumi.Output<string | undefined>;
```


Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L91">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the trail

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getServiceAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/getServiceAccount.ts#L10">function getServiceAccount</a>
</h2>

```typescript
getServiceAccount(args?: GetServiceAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceAccountResult>
```


Use this data source to get the Account ID of the [AWS CloudTrail Service Account](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-supported-regions.html)
in a given region for the purpose of allowing CloudTrail to store trail data in S3.

<h2 class="pdoc-module-header" id="GetServiceAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/getServiceAccount.ts#L20">interface GetServiceAccountArgs</a>
</h2>

A collection of arguments for invoking getServiceAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/getServiceAccount.ts#L25">property region</a>
</h3>

```typescript
region?: string;
```


Name of the region whose AWS CloudTrail account ID is desired.
Defaults to the region from the AWS provider configuration.

<h2 class="pdoc-module-header" id="GetServiceAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/getServiceAccount.ts#L31">interface GetServiceAccountResult</a>
</h2>

A collection of values returned by getServiceAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/getServiceAccount.ts#L35">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the AWS CloudTrail service account in the selected region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/getServiceAccount.ts#L39">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="TrailArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L222">interface TrailArgs</a>
</h2>

The set of arguments for constructing a Trail resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L227">property cloudWatchLogsGroupArn</a>
</h3>

```typescript
cloudWatchLogsGroupArn?: pulumi.Input<string>;
```


Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L232">property cloudWatchLogsRoleArn</a>
</h3>

```typescript
cloudWatchLogsRoleArn?: pulumi.Input<string>;
```


Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L237">property enableLogFileValidation</a>
</h3>

```typescript
enableLogFileValidation?: pulumi.Input<boolean>;
```


Specifies whether log file integrity validation is enabled.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L242">property enableLogging</a>
</h3>

```typescript
enableLogging?: pulumi.Input<boolean>;
```


Enables logging for the trail. Defaults to `true`.
Setting this to `false` will pause logging.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L246">property eventSelectors</a>
</h3>

```typescript
eventSelectors?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an event selector for enabling data event logging. Fields documented below. Please note the [CloudTrail limits](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html) when configuring these.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L251">property includeGlobalServiceEvents</a>
</h3>

```typescript
includeGlobalServiceEvents?: pulumi.Input<boolean>;
```


Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L256">property isMultiRegionTrail</a>
</h3>

```typescript
isMultiRegionTrail?: pulumi.Input<boolean>;
```


Specifies whether the trail is created in the current
region or in all regions. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L260">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L264">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the trail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L268">property s3BucketName</a>
</h3>

```typescript
s3BucketName: pulumi.Input<string>;
```


Specifies the name of the S3 bucket designated for publishing log files.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L273">property s3KeyPrefix</a>
</h3>

```typescript
s3KeyPrefix?: pulumi.Input<string>;
```


Specifies the S3 key prefix that precedes
the name of the bucket you have designated for log file delivery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L278">property snsTopicName</a>
</h3>

```typescript
snsTopicName?: pulumi.Input<string>;
```


Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L282">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the trail

<h2 class="pdoc-module-header" id="TrailState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L148">interface TrailState</a>
</h2>

Input properties used for looking up and filtering Trail resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L152">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name of the trail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L157">property cloudWatchLogsGroupArn</a>
</h3>

```typescript
cloudWatchLogsGroupArn?: pulumi.Input<string>;
```


Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L162">property cloudWatchLogsRoleArn</a>
</h3>

```typescript
cloudWatchLogsRoleArn?: pulumi.Input<string>;
```


Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L167">property enableLogFileValidation</a>
</h3>

```typescript
enableLogFileValidation?: pulumi.Input<boolean>;
```


Specifies whether log file integrity validation is enabled.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L172">property enableLogging</a>
</h3>

```typescript
enableLogging?: pulumi.Input<boolean>;
```


Enables logging for the trail. Defaults to `true`.
Setting this to `false` will pause logging.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L176">property eventSelectors</a>
</h3>

```typescript
eventSelectors?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies an event selector for enabling data event logging. Fields documented below. Please note the [CloudTrail limits](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html) when configuring these.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L180">property homeRegion</a>
</h3>

```typescript
homeRegion?: pulumi.Input<string>;
```


The region in which the trail was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L185">property includeGlobalServiceEvents</a>
</h3>

```typescript
includeGlobalServiceEvents?: pulumi.Input<boolean>;
```


Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L190">property isMultiRegionTrail</a>
</h3>

```typescript
isMultiRegionTrail?: pulumi.Input<boolean>;
```


Specifies whether the trail is created in the current
region or in all regions. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L194">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L198">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the trail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L202">property s3BucketName</a>
</h3>

```typescript
s3BucketName?: pulumi.Input<string>;
```


Specifies the name of the S3 bucket designated for publishing log files.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L207">property s3KeyPrefix</a>
</h3>

```typescript
s3KeyPrefix?: pulumi.Input<string>;
```


Specifies the S3 key prefix that precedes
the name of the bucket you have designated for log file delivery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L212">property snsTopicName</a>
</h3>

```typescript
snsTopicName?: pulumi.Input<string>;
```


Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudtrail/trail.ts#L216">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the trail

