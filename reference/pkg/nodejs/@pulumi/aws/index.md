---
title: Package @pulumi/aws
---


Node.js:

```javascript
var aws = require("@pulumi/aws");
```

ES6 modules:

```typescript
import * as aws from "@pulumi/aws";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Provider">class Provider</a>
* <a href="#getAmi">function getAmi</a>
* <a href="#getAmiIds">function getAmiIds</a>
* <a href="#getArn">function getArn</a>
* <a href="#getAutoscalingGroups">function getAutoscalingGroups</a>
* <a href="#getAvailabilityZone">function getAvailabilityZone</a>
* <a href="#getAvailabilityZones">function getAvailabilityZones</a>
* <a href="#getBillingServiceAccount">function getBillingServiceAccount</a>
* <a href="#getCallerIdentity">function getCallerIdentity</a>
* <a href="#getCanonicalUserId">function getCanonicalUserId</a>
* <a href="#getElasticIp">function getElasticIp</a>
* <a href="#getEnv">function getEnv</a>
* <a href="#getEnvBoolean">function getEnvBoolean</a>
* <a href="#getEnvNumber">function getEnvNumber</a>
* <a href="#getIpRanges">function getIpRanges</a>
* <a href="#getPartition">function getPartition</a>
* <a href="#getPrefixList">function getPrefixList</a>
* <a href="#getRegion">function getRegion</a>
* <a href="#requireWithDefault">function requireWithDefault</a>
* <a href="#sha1hash">function sha1hash</a>
* <a href="#GetAmiArgs">interface GetAmiArgs</a>
* <a href="#GetAmiIdsArgs">interface GetAmiIdsArgs</a>
* <a href="#GetAmiIdsResult">interface GetAmiIdsResult</a>
* <a href="#GetAmiResult">interface GetAmiResult</a>
* <a href="#GetArnArgs">interface GetArnArgs</a>
* <a href="#GetArnResult">interface GetArnResult</a>
* <a href="#GetAutoscalingGroupsArgs">interface GetAutoscalingGroupsArgs</a>
* <a href="#GetAutoscalingGroupsResult">interface GetAutoscalingGroupsResult</a>
* <a href="#GetAvailabilityZoneArgs">interface GetAvailabilityZoneArgs</a>
* <a href="#GetAvailabilityZoneResult">interface GetAvailabilityZoneResult</a>
* <a href="#GetAvailabilityZonesArgs">interface GetAvailabilityZonesArgs</a>
* <a href="#GetAvailabilityZonesResult">interface GetAvailabilityZonesResult</a>
* <a href="#GetBillingServiceAccountResult">interface GetBillingServiceAccountResult</a>
* <a href="#GetCallerIdentityResult">interface GetCallerIdentityResult</a>
* <a href="#GetCanonicalUserIdResult">interface GetCanonicalUserIdResult</a>
* <a href="#GetElasticIpArgs">interface GetElasticIpArgs</a>
* <a href="#GetElasticIpResult">interface GetElasticIpResult</a>
* <a href="#GetIpRangesArgs">interface GetIpRangesArgs</a>
* <a href="#GetIpRangesResult">interface GetIpRangesResult</a>
* <a href="#GetPartitionResult">interface GetPartitionResult</a>
* <a href="#GetPrefixListArgs">interface GetPrefixListArgs</a>
* <a href="#GetPrefixListResult">interface GetPrefixListResult</a>
* <a href="#GetRegionArgs">interface GetRegionArgs</a>
* <a href="#GetRegionResult">interface GetRegionResult</a>
* <a href="#ProviderArgs">interface ProviderArgs</a>
* <a href="#Tags">interface Tags</a>
* <a href="#APNortheast1Region">let APNortheast1Region</a>
* <a href="#APNortheast2Region">let APNortheast2Region</a>
* <a href="#APSouth1Region">let APSouth1Region</a>
* <a href="#APSouthEast2Region">let APSouthEast2Region</a>
* <a href="#APSoutheast1Region">let APSoutheast1Region</a>
* <a href="#CACentralRegion">let CACentralRegion</a>
* <a href="#EUCentral1Region">let EUCentral1Region</a>
* <a href="#EUWest1Region">let EUWest1Region</a>
* <a href="#EUWest2Region">let EUWest2Region</a>
* <a href="#EUWest3Region">let EUWest3Region</a>
* <a href="#SAEast1Region">let SAEast1Region</a>
* <a href="#USEast1Region">let USEast1Region</a>
* <a href="#USEast2Region">let USEast2Region</a>
* <a href="#USWest1Region">let USWest1Region</a>
* <a href="#USWest2Region">let USWest2Region</a>
* <a href="#ARN">type ARN</a>
* <a href="#Overwrite">type Overwrite</a>
* <a href="#Region">type Region</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/arn.ts">arn.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts">getAmi.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts">getAmiIds.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts">getArn.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts">getAutoscalingGroups.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts">getAvailabilityZone.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts">getAvailabilityZones.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts">getBillingServiceAccount.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts">getCallerIdentity.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts">getCanonicalUserId.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts">getElasticIp.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts">getIpRanges.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts">getPartition.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts">getPrefixList.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts">getRegion.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts">provider.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts">region.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/tags.ts">tags.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/utilities.ts">utilities.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/utils.ts">utils.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="acm">acm</a>
* <a href="acmpca">acmpca</a>
* <a href="apigateway">apigateway</a>
* <a href="appautoscaling">appautoscaling</a>
* <a href="applicationloadbalancing">applicationloadbalancing</a>
* <a href="appsync">appsync</a>
* <a href="athena">athena</a>
* <a href="autoscaling">autoscaling</a>
* <a href="batch">batch</a>
* <a href="budgets">budgets</a>
* <a href="cfg">cfg</a>
* <a href="cloud9">cloud9</a>
* <a href="cloudformation">cloudformation</a>
* <a href="cloudfront">cloudfront</a>
* <a href="cloudhsmv2">cloudhsmv2</a>
* <a href="cloudtrail">cloudtrail</a>
* <a href="cloudwatch">cloudwatch</a>
* <a href="codebuild">codebuild</a>
* <a href="codecommit">codecommit</a>
* <a href="codedeploy">codedeploy</a>
* <a href="codepipeline">codepipeline</a>
* <a href="cognito">cognito</a>
* <a href="config">config</a>
* <a href="datasync">datasync</a>
* <a href="dax">dax</a>
* <a href="devicefarm">devicefarm</a>
* <a href="directconnect">directconnect</a>
* <a href="directoryservice">directoryservice</a>
* <a href="dlm">dlm</a>
* <a href="dms">dms</a>
* <a href="dynamodb">dynamodb</a>
* <a href="ebs">ebs</a>
* <a href="ec2">ec2</a>
* <a href="ec2transitgateway">ec2transitgateway</a>
* <a href="ecr">ecr</a>
* <a href="ecs">ecs</a>
* <a href="efs">efs</a>
* <a href="eks">eks</a>
* <a href="elasticache">elasticache</a>
* <a href="elasticbeanstalk">elasticbeanstalk</a>
* <a href="elasticloadbalancing">elasticloadbalancing</a>
* <a href="elasticloadbalancingv2">elasticloadbalancingv2</a>
* <a href="elasticsearch">elasticsearch</a>
* <a href="elastictranscoder">elastictranscoder</a>
* <a href="emr">emr</a>
* <a href="gamelift">gamelift</a>
* <a href="glacier">glacier</a>
* <a href="glue">glue</a>
* <a href="guardduty">guardduty</a>
* <a href="iam">iam</a>
* <a href="inspector">inspector</a>
* <a href="iot">iot</a>
* <a href="kinesis">kinesis</a>
* <a href="kms">kms</a>
* <a href="lambda">lambda</a>
* <a href="lightsail">lightsail</a>
* <a href="macie">macie</a>
* <a href="mediastore">mediastore</a>
* <a href="mq">mq</a>
* <a href="neptune">neptune</a>
* <a href="opsworks">opsworks</a>
* <a href="organizations">organizations</a>
* <a href="pinpoint">pinpoint</a>
* <a href="pricing">pricing</a>
* <a href="rds">rds</a>
* <a href="redshift">redshift</a>
* <a href="route53">route53</a>
* <a href="s3">s3</a>
* <a href="secretsmanager">secretsmanager</a>
* <a href="serverless">serverless</a>
* <a href="servicecatalog">servicecatalog</a>
* <a href="servicediscovery">servicediscovery</a>
* <a href="ses">ses</a>
* <a href="sfn">sfn</a>
* <a href="simpledb">simpledb</a>
* <a href="sns">sns</a>
* <a href="sqs">sqs</a>
* <a href="ssm">ssm</a>
* <a href="storagegateway">storagegateway</a>
* <a href="swf">swf</a>
* <a href="waf">waf</a>
* <a href="wafregional">wafregional</a>
* <a href="workspaces">workspaces</a>

<h2 class="pdoc-module-header" id="Provider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L12">class Provider</a>
</h2>

The provider type for the aws package

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L12">constructor</a>
</h3>

```typescript
new Provider(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions)
```


Create a Provider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getAmi">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L13">function getAmi</a>
</h2>

```typescript
getAmi(args?: GetAmiArgs, opts?: pulumi.InvokeOptions): Promise<GetAmiResult>
```


Use this data source to get the ID of a registered AMI for use in other
resources.

~> **NOTE:** The `owners` argument will be **required** in the next major version.

<h2 class="pdoc-module-header" id="getAmiIds">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L12">function getAmiIds</a>
</h2>

```typescript
getAmiIds(args?: GetAmiIdsArgs, opts?: pulumi.InvokeOptions): Promise<GetAmiIdsResult>
```


Use this data source to get a list of AMI IDs matching the specified criteria.

~> **NOTE:** The `owners` argument will be **required** in the next major version.

<h2 class="pdoc-module-header" id="getArn">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L10">function getArn</a>
</h2>

```typescript
getArn(args: GetArnArgs, opts?: pulumi.InvokeOptions): Promise<GetArnResult>
```


Parses an Amazon Resource Name (ARN) into its constituent parts.

<h2 class="pdoc-module-header" id="getAutoscalingGroups">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L11">function getAutoscalingGroups</a>
</h2>

```typescript
getAutoscalingGroups(args?: GetAutoscalingGroupsArgs, opts?: pulumi.InvokeOptions): Promise<GetAutoscalingGroupsResult>
```


The Autoscaling Groups data source allows access to the list of AWS
ASGs within a specific region. This will allow you to pass a list of AutoScaling Groups to other resources.

<h2 class="pdoc-module-header" id="getAvailabilityZone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L20">function getAvailabilityZone</a>
</h2>

```typescript
getAvailabilityZone(args?: GetAvailabilityZoneArgs, opts?: pulumi.InvokeOptions): Promise<GetAvailabilityZoneResult>
```


`aws_availability_zone` provides details about a specific availability zone (AZ)
in the current region.

This can be used both to validate an availability zone given in a variable
and to split the AZ name into its component parts of an AWS region and an
AZ identifier letter. The latter may be useful e.g. for implementing a
consistent subnet numbering scheme across several regions by mapping both
the region and the subnet letter to network numbers.

This is different from the `aws_availability_zones` (plural) data source,
which provides a list of the available zones.

<h2 class="pdoc-module-header" id="getAvailabilityZones">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L15">function getAvailabilityZones</a>
</h2>

```typescript
getAvailabilityZones(args?: GetAvailabilityZonesArgs, opts?: pulumi.InvokeOptions): Promise<GetAvailabilityZonesResult>
```


The Availability Zones data source allows access to the list of AWS
Availability Zones which can be accessed by an AWS account within the region
configured in the provider.

This is different from the `aws_availability_zone` (singular) data source,
which provides some details about a specific availability zone.

<h2 class="pdoc-module-header" id="getBillingServiceAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts#L10">function getBillingServiceAccount</a>
</h2>

```typescript
getBillingServiceAccount(opts?: pulumi.InvokeOptions): Promise<GetBillingServiceAccountResult>
```


Use this data source to get the Account ID of the [AWS Billing and Cost Management Service Account](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-getting-started.html#step-2) for the purpose of whitelisting in S3 bucket policy.

<h2 class="pdoc-module-header" id="getCallerIdentity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L11">function getCallerIdentity</a>
</h2>

```typescript
getCallerIdentity(opts?: pulumi.InvokeOptions): Promise<GetCallerIdentityResult>
```


Use this data source to get the access to the effective Account ID, User ID, and ARN in
which Terraform is authorized.

<h2 class="pdoc-module-header" id="getCanonicalUserId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts#L11">function getCanonicalUserId</a>
</h2>

```typescript
getCanonicalUserId(opts?: pulumi.InvokeOptions): Promise<GetCanonicalUserIdResult>
```


The Canonical User ID data source allows access to the [canonical user ID](http://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html)
for the effective account in which Terraform is working.

<h2 class="pdoc-module-header" id="getElasticIp">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L10">function getElasticIp</a>
</h2>

```typescript
getElasticIp(args?: GetElasticIpArgs, opts?: pulumi.InvokeOptions): Promise<GetElasticIpResult>
```


`aws_eip` provides details about a specific Elastic IP.

<h2 class="pdoc-module-header" id="getEnv">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/utilities.ts#L7">function getEnv</a>
</h2>

```typescript
getEnv(vars: string[]): string | undefined
```

<h2 class="pdoc-module-header" id="getEnvBoolean">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/utilities.ts#L17">function getEnvBoolean</a>
</h2>

```typescript
getEnvBoolean(vars: string[]): boolean | undefined
```

<h2 class="pdoc-module-header" id="getEnvNumber">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/utilities.ts#L32">function getEnvNumber</a>
</h2>

```typescript
getEnvNumber(vars: string[]): number | undefined
```

<h2 class="pdoc-module-header" id="getIpRanges">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L10">function getIpRanges</a>
</h2>

```typescript
getIpRanges(args: GetIpRangesArgs, opts?: pulumi.InvokeOptions): Promise<GetIpRangesResult>
```


Use this data source to get the [IP ranges][1] of various AWS products and services.

<h2 class="pdoc-module-header" id="getPartition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts#L10">function getPartition</a>
</h2>

```typescript
getPartition(opts?: pulumi.InvokeOptions): Promise<GetPartitionResult>
```


Use this data source to lookup current AWS partition in which Terraform is working

<h2 class="pdoc-module-header" id="getPrefixList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L16">function getPrefixList</a>
</h2>

```typescript
getPrefixList(args?: GetPrefixListArgs, opts?: pulumi.InvokeOptions): Promise<GetPrefixListResult>
```


`aws_prefix_list` provides details about a specific prefix list (PL)
in the current region.

This can be used both to validate a prefix list given in a variable
and to obtain the CIDR blocks (IP address ranges) for the associated
AWS service. The latter may be useful e.g. for adding network ACL
rules.

<h2 class="pdoc-module-header" id="getRegion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L15">function getRegion</a>
</h2>

```typescript
getRegion(args?: GetRegionArgs, opts?: pulumi.InvokeOptions): Promise<GetRegionResult>
```


`aws_region` provides details about a specific AWS region.

As well as validating a given region name this resource can be used to
discover the name of the region configured within the provider. The latter
can be useful in a child module which is inheriting an AWS provider
configuration from its parent module.

<h2 class="pdoc-module-header" id="requireWithDefault">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/utilities.ts#L43">function requireWithDefault</a>
</h2>

```typescript
requireWithDefault<T>(req: { ... }, def: T | undefined): T
```

<h2 class="pdoc-module-header" id="sha1hash">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/utils.ts#L33">function sha1hash</a>
</h2>

```typescript
sha1hash(s: string): string
```

<h2 class="pdoc-module-header" id="GetAmiArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L28">interface GetAmiArgs</a>
</h2>

A collection of arguments for invoking getAmi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L33">property executableUsers</a>
</h3>

```typescript
executableUsers?: string[];
```


Limit search to users with *explicit* launch permission on
the image. Valid items are the numeric account ID or `self`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L39">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L44">property mostRecent</a>
</h3>

```typescript
mostRecent?: boolean;
```


If more than one result is returned, use the most
recent AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L52">property nameRegex</a>
</h3>

```typescript
nameRegex?: string;
```


A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API. This
filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L57">property owners</a>
</h3>

```typescript
owners?: string[];
```


Limit search to specific AMI owners. Valid items are the numeric
account ID, `amazon`, or `self`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L58">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetAmiIdsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L26">interface GetAmiIdsArgs</a>
</h2>

A collection of arguments for invoking getAmiIds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L31">property executableUsers</a>
</h3>

```typescript
executableUsers?: string[];
```


Limit search to users with *explicit* launch
permission on  the image. Valid items are the numeric account ID or `self`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L37">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more name/value pairs to filter off of. There
are several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L45">property nameRegex</a>
</h3>

```typescript
nameRegex?: string;
```


A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API.
This filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L50">property owners</a>
</h3>

```typescript
owners?: string[];
```


Limit search to specific AMI owners. Valid items are
the numeric account ID, `amazon`, or `self`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L54">property sortAscending</a>
</h3>

```typescript
sortAscending?: boolean;
```


Used to sort AMIs by creation time.

<h2 class="pdoc-module-header" id="GetAmiIdsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L60">interface GetAmiIdsResult</a>
</h2>

A collection of values returned by getAmiIds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L65">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L61">property ids</a>
</h3>

```typescript
ids: string[];
```

<h2 class="pdoc-module-header" id="GetAmiResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L64">interface GetAmiResult</a>
</h2>

A collection of values returned by getAmi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L68">property architecture</a>
</h3>

```typescript
architecture: string;
```


The OS architecture of the AMI (ie: `i386` or `x86_64`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L86">property blockDeviceMappings</a>
</h3>

```typescript
blockDeviceMappings: { ... }[];
```


The block device mappings of the AMI.
* `block_device_mappings.#.device_name` - The physical name of the device.
* `block_device_mappings.#.ebs.delete_on_termination` - `true` if the EBS volume
will be deleted on termination.
* `block_device_mappings.#.ebs.encrypted` - `true` if the EBS volume
is encrypted.
* `block_device_mappings.#.ebs.iops` - `0` if the EBS volume is
not a provisioned IOPS image, otherwise the supported IOPS count.
* `block_device_mappings.#.ebs.snapshot_id` - The ID of the snapshot.
* `block_device_mappings.#.ebs.volume_size` - The size of the volume, in GiB.
* `block_device_mappings.#.ebs.volume_type` - The volume type.
* `block_device_mappings.#.no_device` - Suppresses the specified device
included in the block device mapping of the AMI.
* `block_device_mappings.#.virtual_name` - The virtual device name (for
instance stores).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L90">property creationDate</a>
</h3>

```typescript
creationDate: string;
```


The date and time the image was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L95">property description</a>
</h3>

```typescript
description: string;
```


The description of the AMI that was provided during image
creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L99">property hypervisor</a>
</h3>

```typescript
hypervisor: string;
```


The hypervisor type of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L191">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L103">property imageId</a>
</h3>

```typescript
imageId: string;
```


The ID of the AMI. Should be the same as the resource `id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L107">property imageLocation</a>
</h3>

```typescript
imageLocation: string;
```


The location of the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L112">property imageOwnerAlias</a>
</h3>

```typescript
imageOwnerAlias: string;
```


The AWS account alias (for example, `amazon`, `self`) or
the AWS account ID of the AMI owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L116">property imageType</a>
</h3>

```typescript
imageType: string;
```


The type of image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L121">property kernelId</a>
</h3>

```typescript
kernelId: string;
```


The kernel associated with the image, if any. Only applicable
for machine images.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L125">property name</a>
</h3>

```typescript
name: string;
```


The name of the AMI that was provided during image creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L129">property ownerId</a>
</h3>

```typescript
ownerId: string;
```


The AWS account ID of the image owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L133">property platform</a>
</h3>

```typescript
platform: string;
```


The value is Windows for `Windows` AMIs; otherwise blank.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L139">property productCodes</a>
</h3>

```typescript
productCodes: { ... }[];
```


Any product codes associated with the AMI.
* `product_codes.#.product_code_id` - The product code.
* `product_codes.#.product_code_type` - The type of product code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L143">property public</a>
</h3>

```typescript
public: boolean;
```


`true` if the image has public launch permissions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L148">property ramdiskId</a>
</h3>

```typescript
ramdiskId: string;
```


The RAM disk associated with the image, if any. Only applicable
for machine images.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L152">property rootDeviceName</a>
</h3>

```typescript
rootDeviceName: string;
```


The device name of the root device.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L156">property rootDeviceType</a>
</h3>

```typescript
rootDeviceType: string;
```


The type of root device (ie: `ebs` or `instance-store`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L161">property rootSnapshotId</a>
</h3>

```typescript
rootSnapshotId: string;
```


The snapshot id associated with the root device, if any
(only applies to `ebs` root devices).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L165">property sriovNetSupport</a>
</h3>

```typescript
sriovNetSupport: string;
```


Specifies whether enhanced networking is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L170">property state</a>
</h3>

```typescript
state: string;
```


The current state of the AMI. If the state is `available`, the image
is successfully registered and can be used to launch an instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L176">property stateReason</a>
</h3>

```typescript
stateReason: { ... };
```


Describes a state change. Fields are `UNSET` if not available.
* `state_reason.code` - The reason code for the state change.
* `state_reason.message` - The message for the state change.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L182">property tags</a>
</h3>

```typescript
tags: { ... };
```


Any tags assigned to the image.
* `tags.#.key` - The key name of the tag.
* `tags.#.value` - The value of the tag.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L187">property virtualizationType</a>
</h3>

```typescript
virtualizationType: string;
```


The type of virtualization of the AMI (ie: `hvm` or
`paravirtual`).

<h2 class="pdoc-module-header" id="GetArnArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L19">interface GetArnArgs</a>
</h2>

A collection of arguments for invoking getArn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L23">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN to parse.

<h2 class="pdoc-module-header" id="GetArnResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L29">interface GetArnResult</a>
</h2>

A collection of values returned by getArn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L33">property account</a>
</h3>

```typescript
account: string;
```


The [ID](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html) of the AWS account that owns the resource, without the hyphens.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L55">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L37">property partition</a>
</h3>

```typescript
partition: string;
```


The partition that the resource is in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L42">property region</a>
</h3>

```typescript
region: string;
```


The region the resource resides in.
Note that the ARNs for some resources do not require a region, so this component might be omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L47">property resource</a>
</h3>

```typescript
resource: string;
```


The content of this part of the ARN varies by service.
It often includes an indicator of the type of resource—for example, an IAM user or Amazon RDS database —followed by a slash (/) or a colon (:), followed by the resource name itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L51">property service</a>
</h3>

```typescript
service: string;
```


The [service namespace](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces) that identifies the AWS product.

<h2 class="pdoc-module-header" id="GetAutoscalingGroupsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L21">interface GetAutoscalingGroupsArgs</a>
</h2>

A collection of arguments for invoking getAutoscalingGroups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L25">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


A filter used to scope the list e.g. by tags. See [related docs](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_Filter.html).

<h2 class="pdoc-module-header" id="GetAutoscalingGroupsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L31">interface GetAutoscalingGroupsResult</a>
</h2>

A collection of values returned by getAutoscalingGroups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L35">property arns</a>
</h3>

```typescript
arns: string[];
```


A list of the Autoscaling Groups Arns in the current region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L43">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L39">property names</a>
</h3>

```typescript
names: string[];
```


A list of the Autoscaling Groups in the current region.

<h2 class="pdoc-module-header" id="GetAvailabilityZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L31">interface GetAvailabilityZoneArgs</a>
</h2>

A collection of arguments for invoking getAvailabilityZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L35">property name</a>
</h3>

```typescript
name?: string;
```


The full name of the availability zone to select.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L40">property state</a>
</h3>

```typescript
state?: string;
```


A specific availability zone state to require. May
be any of `"available"`, `"information"` or `"impaired"`.

<h2 class="pdoc-module-header" id="GetAvailabilityZoneResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L46">interface GetAvailabilityZoneResult</a>
</h2>

A collection of values returned by getAvailabilityZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L69">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L50">property name</a>
</h3>

```typescript
name: string;
```


The name of the selected availability zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L55">property nameSuffix</a>
</h3>

```typescript
nameSuffix: string;
```


The part of the AZ name that appears after the region name,
uniquely identifying the AZ within its region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L61">property region</a>
</h3>

```typescript
region: string;
```


The region where the selected availability zone resides.
This is always the region selected on the provider, since this data source
searches only within that region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L65">property state</a>
</h3>

```typescript
state: string;
```


The current state of the AZ.

<h2 class="pdoc-module-header" id="GetAvailabilityZonesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L25">interface GetAvailabilityZonesArgs</a>
</h2>

A collection of arguments for invoking getAvailabilityZones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L32">property state</a>
</h3>

```typescript
state?: string;
```


Allows to filter list of Availability Zones based on their
current state. Can be either `"available"`, `"information"`, `"impaired"` or
`"unavailable"`. By default the list includes a complete set of Availability Zones
to which the underlying AWS account has access, regardless of their state.

<h2 class="pdoc-module-header" id="GetAvailabilityZonesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L38">interface GetAvailabilityZonesResult</a>
</h2>

A collection of values returned by getAvailabilityZones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L46">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L42">property names</a>
</h3>

```typescript
names: string[];
```


A list of the Availability Zone names available to the account.

<h2 class="pdoc-module-header" id="GetBillingServiceAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts#L18">interface GetBillingServiceAccountResult</a>
</h2>

A collection of values returned by getBillingServiceAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts#L22">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the AWS billing service account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts#L26">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetCallerIdentityResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L19">interface GetCallerIdentityResult</a>
</h2>

A collection of values returned by getCallerIdentity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L23">property accountId</a>
</h3>

```typescript
accountId: string;
```


The AWS Account ID number of the account that owns or contains the calling entity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L27">property arn</a>
</h3>

```typescript
arn: string;
```


The AWS ARN associated with the calling entity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L35">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L31">property userId</a>
</h3>

```typescript
userId: string;
```


The unique identifier of the calling entity.

<h2 class="pdoc-module-header" id="GetCanonicalUserIdResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts#L19">interface GetCanonicalUserIdResult</a>
</h2>

A collection of values returned by getCanonicalUserId.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts#L23">property displayName</a>
</h3>

```typescript
displayName: string;
```


The human-friendly name linked to the canonical user ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts#L27">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetElasticIpArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L23">interface GetElasticIpArgs</a>
</h2>

A collection of arguments for invoking getElasticIp.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L27">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more name/value pairs to use as filters. There are several valid keys, for a full reference, check out the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L31">property id</a>
</h3>

```typescript
id?: string;
```


The allocation id of the specific VPC EIP to retrieve. If a classic EIP is required, do NOT set `id`, only set `public_ip`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L35">property publicIp</a>
</h3>

```typescript
publicIp?: string;
```


The public IP of the specific EIP to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L39">property tags</a>
</h3>

```typescript
tags?: { ... };
```


A mapping of tags, each pair of which must exactly match a pair on the desired Elastic IP

<h2 class="pdoc-module-header" id="GetElasticIpResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L45">interface GetElasticIpResult</a>
</h2>

A collection of values returned by getElasticIp.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L49">property associationId</a>
</h3>

```typescript
associationId: string;
```


The ID representing the association of the address with an instance in a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L53">property domain</a>
</h3>

```typescript
domain: string;
```


Indicates whether the address is for use in EC2-Classic (standard) or in a VPC (vpc).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L57">property id</a>
</h3>

```typescript
id: string;
```


If VPC Elastic IP, the allocation identifier. If EC2-Classic Elastic IP, the public IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L61">property instanceId</a>
</h3>

```typescript
instanceId: string;
```


The ID of the instance that the address is associated with (if any).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L65">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: string;
```


The ID of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L69">property networkInterfaceOwnerId</a>
</h3>

```typescript
networkInterfaceOwnerId: string;
```


The ID of the AWS account that owns the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L73">property privateIp</a>
</h3>

```typescript
privateIp: string;
```


The private IP address associated with the Elastic IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L77">property publicIp</a>
</h3>

```typescript
publicIp: string;
```


Public IP address of Elastic IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L81">property publicIpv4Pool</a>
</h3>

```typescript
publicIpv4Pool: string;
```


The ID of an address pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L85">property tags</a>
</h3>

```typescript
tags: { ... };
```


Key-value map of tags associated with Elastic IP.

<h2 class="pdoc-module-header" id="GetIpRangesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L20">interface GetIpRangesArgs</a>
</h2>

A collection of arguments for invoking getIpRanges.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L26">property regions</a>
</h3>

```typescript
regions?: string[];
```


Filter IP ranges by regions (or include all regions, if
omitted). Valid items are `global` (for `cloudfront`) as well as all AWS regions
(e.g. `eu-central-1`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L31">property services</a>
</h3>

```typescript
services: string[];
```


Filter IP ranges by services. Valid items are `amazon`
(for amazon.com), `cloudfront`, `codebuild`, `ec2`, `route53`, `route53_healthchecks` and `S3`.

<h2 class="pdoc-module-header" id="GetIpRangesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L37">interface GetIpRangesResult</a>
</h2>

A collection of values returned by getIpRanges.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L41">property cidrBlocks</a>
</h3>

```typescript
cidrBlocks: string[];
```


The lexically ordered list of CIDR blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L45">property createDate</a>
</h3>

```typescript
createDate: string;
```


The publication time of the IP ranges (e.g. `2016-08-03-23-46-05`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L58">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L49">property ipv6CidrBlocks</a>
</h3>

```typescript
ipv6CidrBlocks: string[];
```


The lexically ordered list of IPv6 CIDR blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L54">property syncToken</a>
</h3>

```typescript
syncToken: number;
```


The publication time of the IP ranges, in Unix epoch time format
(e.g. `1470267965`).

<h2 class="pdoc-module-header" id="GetPartitionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts#L18">interface GetPartitionResult</a>
</h2>

A collection of values returned by getPartition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts#L23">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts#L19">property partition</a>
</h3>

```typescript
partition: string;
```

<h2 class="pdoc-module-header" id="GetPrefixListArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L27">interface GetPrefixListArgs</a>
</h2>

A collection of arguments for invoking getPrefixList.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L31">property name</a>
</h3>

```typescript
name?: string;
```


The name of the prefix list to select.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L35">property prefixListId</a>
</h3>

```typescript
prefixListId?: string;
```


The ID of the prefix list to select.

<h2 class="pdoc-module-header" id="GetPrefixListResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L41">interface GetPrefixListResult</a>
</h2>

A collection of values returned by getPrefixList.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L46">property cidrBlocks</a>
</h3>

```typescript
cidrBlocks: string[];
```


The list of CIDR blocks for the AWS service associated
with the prefix list.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L54">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L50">property name</a>
</h3>

```typescript
name: string;
```


The name of the selected prefix list.

<h2 class="pdoc-module-header" id="GetRegionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L27">interface GetRegionArgs</a>
</h2>

A collection of arguments for invoking getRegion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L28">property current</a>
</h3>

```typescript
current?: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L32">property endpoint</a>
</h3>

```typescript
endpoint?: string;
```


The EC2 endpoint of the region to select.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L36">property name</a>
</h3>

```typescript
name?: string;
```


The full name of the region to select.

<h2 class="pdoc-module-header" id="GetRegionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L42">interface GetRegionResult</a>
</h2>

A collection of values returned by getRegion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L47">property current</a>
</h3>

```typescript
current: boolean;
```


`true` if the selected region is the one configured on the
provider, or `false` otherwise.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L51">property description</a>
</h3>

```typescript
description: string;
```


The region's description in this format: "Location (Region name)".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L55">property endpoint</a>
</h3>

```typescript
endpoint: string;
```


The EC2 endpoint for the selected region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L63">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L59">property name</a>
</h3>

```typescript
name: string;
```


The name of the selected region.

<h2 class="pdoc-module-header" id="ProviderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L50">interface ProviderArgs</a>
</h2>

The set of arguments for constructing a Provider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L55">property accessKey</a>
</h3>

```typescript
accessKey?: pulumi.Input<string>;
```


The access key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS
console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L56">property allowedAccountIds</a>
</h3>

```typescript
allowedAccountIds?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L57">property assumeRole</a>
</h3>

```typescript
assumeRole?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L58">property endpoints</a>
</h3>

```typescript
endpoints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L59">property forbiddenAccountIds</a>
</h3>

```typescript
forbiddenAccountIds?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L63">property insecure</a>
</h3>

```typescript
insecure?: pulumi.Input<boolean>;
```


Explicitly allow the provider to perform "insecure" SSL requests. If omitted,default value is `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L68">property maxRetries</a>
</h3>

```typescript
maxRetries?: pulumi.Input<number>;
```


The maximum number of times an AWS API request is being executed. If the API request still fails, an error is
thrown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L72">property profile</a>
</h3>

```typescript
profile?: pulumi.Input<string>;
```


The profile for API operations. If not set, the default profile created with `aws configure` will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L76">property region</a>
</h3>

```typescript
region?: pulumi.Input<Region>;
```


The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L82">property s3ForcePathStyle</a>
</h3>

```typescript
s3ForcePathStyle?: pulumi.Input<boolean>;
```


Set this to true to force the request to use path-style addressing, i.e., http://s3.amazonaws.com/BUCKET/KEY. By
default, the S3 client will use virtual hosted bucket addressing when possible (http://BUCKET.s3.amazonaws.com/KEY).
Specific to the Amazon S3 service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L87">property secretKey</a>
</h3>

```typescript
secretKey?: pulumi.Input<string>;
```


The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS
console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L91">property sharedCredentialsFile</a>
</h3>

```typescript
sharedCredentialsFile?: pulumi.Input<string>;
```


The path to the shared credentials file. If not set this defaults to ~/.aws/credentials.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L96">property skipCredentialsValidation</a>
</h3>

```typescript
skipCredentialsValidation?: pulumi.Input<boolean>;
```


Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS
available/implemented.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L100">property skipGetEc2Platforms</a>
</h3>

```typescript
skipGetEc2Platforms?: pulumi.Input<boolean>;
```


Skip getting the supported EC2 platforms. Used by users that don't have ec2:DescribeAccountAttributes permissions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L101">property skipMetadataApiCheck</a>
</h3>

```typescript
skipMetadataApiCheck?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L106">property skipRegionValidation</a>
</h3>

```typescript
skipRegionValidation?: pulumi.Input<boolean>;
```


Skip static validation of region name. Used by users of alternative AWS-like APIs or users w/ access to regions that
are not public (yet).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L110">property skipRequestingAccountId</a>
</h3>

```typescript
skipRequestingAccountId?: pulumi.Input<boolean>;
```


Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/provider.ts#L114">property token</a>
</h3>

```typescript
token?: pulumi.Input<string>;
```


session token. A session token is only required if you are using temporary security credentials.

<h2 class="pdoc-module-header" id="Tags">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/tags.ts#L19">interface Tags</a>
</h2>

Tags represents a set of key-value string pairs to which can be applied
to an AWS resource.

<h2 class="pdoc-module-header" id="APNortheast1Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L15">let APNortheast1Region</a>
</h2>

```typescript
let APNortheast1Region: Region = "ap-northeast-1";
```

<h2 class="pdoc-module-header" id="APNortheast2Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L16">let APNortheast2Region</a>
</h2>

```typescript
let APNortheast2Region: Region = "ap-northeast-2";
```

<h2 class="pdoc-module-header" id="APSouth1Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L17">let APSouth1Region</a>
</h2>

```typescript
let APSouth1Region: Region = "ap-south-1";
```

<h2 class="pdoc-module-header" id="APSouthEast2Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L18">let APSouthEast2Region</a>
</h2>

```typescript
let APSouthEast2Region: Region = "ap-southeast-2";
```

<h2 class="pdoc-module-header" id="APSoutheast1Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L19">let APSoutheast1Region</a>
</h2>

```typescript
let APSoutheast1Region: Region = "ap-southeast-1";
```

<h2 class="pdoc-module-header" id="CACentralRegion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L20">let CACentralRegion</a>
</h2>

```typescript
let CACentralRegion: Region = "ca-central-1";
```

<h2 class="pdoc-module-header" id="EUCentral1Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L21">let EUCentral1Region</a>
</h2>

```typescript
let EUCentral1Region: Region = "eu-central-1";
```

<h2 class="pdoc-module-header" id="EUWest1Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L22">let EUWest1Region</a>
</h2>

```typescript
let EUWest1Region: Region = "eu-west-1";
```

<h2 class="pdoc-module-header" id="EUWest2Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L23">let EUWest2Region</a>
</h2>

```typescript
let EUWest2Region: Region = "eu-west-2";
```

<h2 class="pdoc-module-header" id="EUWest3Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L24">let EUWest3Region</a>
</h2>

```typescript
let EUWest3Region: Region = "eu-west-3";
```

<h2 class="pdoc-module-header" id="SAEast1Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L25">let SAEast1Region</a>
</h2>

```typescript
let SAEast1Region: Region = "sa-east-1";
```

<h2 class="pdoc-module-header" id="USEast1Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L26">let USEast1Region</a>
</h2>

```typescript
let USEast1Region: Region = "us-east-1";
```

<h2 class="pdoc-module-header" id="USEast2Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L27">let USEast2Region</a>
</h2>

```typescript
let USEast2Region: Region = "us-east-2";
```

<h2 class="pdoc-module-header" id="USWest1Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L28">let USWest1Region</a>
</h2>

```typescript
let USWest1Region: Region = "us-west-1";
```

<h2 class="pdoc-module-header" id="USWest2Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L29">let USWest2Region</a>
</h2>

```typescript
let USWest2Region: Region = "us-west-2";
```

<h2 class="pdoc-module-header" id="ARN">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/arn.ts#L18">type ARN</a>
</h2>

```typescript
type ARN = string;
```


An ARN is an Amazon Resource Name, and uniquely identifies a region globally across all accounts and regions.

<h2 class="pdoc-module-header" id="Overwrite">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/utils.ts#L29">type Overwrite</a>
</h2>

```typescript
type Overwrite = Pick<T, Diff<keyof T, keyof U>> & U;
```

<h2 class="pdoc-module-header" id="Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L34">type Region</a>
</h2>

```typescript
type Region = ap-northeast-1 | ap-northeast-2 | ap-south-1 | ap-southeast-2 | ap-southeast-1 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | sa-east-1 | us-east-1 | us-east-2 | us-west-1 | us-west-2;
```


A Region represents any valid Amazon region that may be targeted with deployments.

