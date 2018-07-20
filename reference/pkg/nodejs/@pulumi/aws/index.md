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
* <a href="#getIpRanges">function getIpRanges</a>
* <a href="#getPartition">function getPartition</a>
* <a href="#getPrefixList">function getPrefixList</a>
* <a href="#getRegion">function getRegion</a>
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
* <a href="#Region">type Region</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/arn.ts">arn.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts">getAmi.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts">getAmiIds.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts">getArn.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts">getAutoscalingGroups.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts">getAvailabilityZone.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts">getAvailabilityZones.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts">getBillingServiceAccount.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts">getCallerIdentity.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts">getCanonicalUserId.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts">getElasticIp.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts">getIpRanges.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts">getPartition.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts">getPrefixList.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts">getRegion.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts">region.ts</a> 

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
* <a href="cloudtrail">cloudtrail</a>
* <a href="cloudwatch">cloudwatch</a>
* <a href="codebuild">codebuild</a>
* <a href="codecommit">codecommit</a>
* <a href="codedeploy">codedeploy</a>
* <a href="codepipeline">codepipeline</a>
* <a href="cognito">cognito</a>
* <a href="config">config</a>
* <a href="dax">dax</a>
* <a href="devicefarm">devicefarm</a>
* <a href="directconnect">directconnect</a>
* <a href="directoryservice">directoryservice</a>
* <a href="dms">dms</a>
* <a href="dynamodb">dynamodb</a>
* <a href="ebs">ebs</a>
* <a href="ec2">ec2</a>
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
* <a href="glacier">glacier</a>
* <a href="glue">glue</a>
* <a href="iam">iam</a>
* <a href="inspector">inspector</a>
* <a href="iot">iot</a>
* <a href="kinesis">kinesis</a>
* <a href="kms">kms</a>
* <a href="lambda">lambda</a>
* <a href="lightsail">lightsail</a>
* <a href="mediastore">mediastore</a>
* <a href="mq">mq</a>
* <a href="neptune">neptune</a>
* <a href="opsworks">opsworks</a>
* <a href="organizations">organizations</a>
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
* <a href="waf">waf</a>
* <a href="wafregional">wafregional</a>

<h2 class="pdoc-module-header" id="getAmi">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L10">function getAmi</a>
</h2>

```typescript
getAmi(args?: GetAmiArgs): Promise<GetAmiResult>
```


Use this data source to get the ID of a registered AMI for use in other
resources.

<h2 class="pdoc-module-header" id="getAmiIds">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L9">function getAmiIds</a>
</h2>

```typescript
getAmiIds(args?: GetAmiIdsArgs): Promise<GetAmiIdsResult>
```


Use this data source to get a list of AMI IDs matching the specified criteria.

<h2 class="pdoc-module-header" id="getArn">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L9">function getArn</a>
</h2>

```typescript
getArn(args: GetArnArgs): Promise<GetArnResult>
```


Parses an Amazon Resource Name (ARN) into its constituent parts.

<h2 class="pdoc-module-header" id="getAutoscalingGroups">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L10">function getAutoscalingGroups</a>
</h2>

```typescript
getAutoscalingGroups(args?: GetAutoscalingGroupsArgs): Promise<GetAutoscalingGroupsResult>
```


The Autoscaling Groups data source allows access to the list of AWS
ASGs within a specific region. This will allow you to pass a list of AutoScaling Groups to other resources.

<h2 class="pdoc-module-header" id="getAvailabilityZone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L19">function getAvailabilityZone</a>
</h2>

```typescript
getAvailabilityZone(args?: GetAvailabilityZoneArgs): Promise<GetAvailabilityZoneResult>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L14">function getAvailabilityZones</a>
</h2>

```typescript
getAvailabilityZones(args?: GetAvailabilityZonesArgs): Promise<GetAvailabilityZonesResult>
```


The Availability Zones data source allows access to the list of AWS
Availability Zones which can be accessed by an AWS account within the region
configured in the provider.

This is different from the `aws_availability_zone` (singular) data source,
which provides some details about a specific availability zone.

<h2 class="pdoc-module-header" id="getBillingServiceAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts#L9">function getBillingServiceAccount</a>
</h2>

```typescript
getBillingServiceAccount(): Promise<GetBillingServiceAccountResult>
```


Use this data source to get the Account ID of the [AWS Billing and Cost Management Service Account](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-getting-started.html#step-2) for the purpose of whitelisting in S3 bucket policy.

<h2 class="pdoc-module-header" id="getCallerIdentity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L10">function getCallerIdentity</a>
</h2>

```typescript
getCallerIdentity(): Promise<GetCallerIdentityResult>
```


Use this data source to get the access to the effective Account ID, User ID, and ARN in
which Terraform is authorized.

<h2 class="pdoc-module-header" id="getCanonicalUserId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts#L10">function getCanonicalUserId</a>
</h2>

```typescript
getCanonicalUserId(): Promise<GetCanonicalUserIdResult>
```


The Canonical User ID data source allows access to the [canonical user ID](http://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html)
for the effective account in which Terraform is working.

<h2 class="pdoc-module-header" id="getElasticIp">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L12">function getElasticIp</a>
</h2>

```typescript
getElasticIp(args?: GetElasticIpArgs): Promise<GetElasticIpResult>
```


`aws_eip` provides details about a specific Elastic IP.

This resource can prove useful when a module accepts an allocation ID or
public IP as an input variable and needs to determine the other.

<h2 class="pdoc-module-header" id="getIpRanges">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L9">function getIpRanges</a>
</h2>

```typescript
getIpRanges(args: GetIpRangesArgs): Promise<GetIpRangesResult>
```


Use this data source to get the [IP ranges][1] of various AWS products and services.

<h2 class="pdoc-module-header" id="getPartition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts#L9">function getPartition</a>
</h2>

```typescript
getPartition(): Promise<GetPartitionResult>
```


Use this data source to lookup current AWS partition in which Terraform is working

<h2 class="pdoc-module-header" id="getPrefixList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L15">function getPrefixList</a>
</h2>

```typescript
getPrefixList(args?: GetPrefixListArgs): Promise<GetPrefixListResult>
```


`aws_prefix_list` provides details about a specific prefix list (PL)
in the current region.

This can be used both to validate a prefix list given in a variable
and to obtain the CIDR blocks (IP address ranges) for the associated
AWS service. The latter may be useful e.g. for adding network ACL
rules.

<h2 class="pdoc-module-header" id="getRegion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L14">function getRegion</a>
</h2>

```typescript
getRegion(args?: GetRegionArgs): Promise<GetRegionResult>
```


`aws_region` provides details about a specific AWS region.

As well as validating a given region name this resource can be used to
discover the name of the region configured within the provider. The latter
can be useful in a child module which is inheriting an AWS provider
configuration from its parent module.

<h2 class="pdoc-module-header" id="GetAmiArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L25">interface GetAmiArgs</a>
</h2>

A collection of arguments for invoking getAmi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L30">property executableUsers</a>
</h3>

```typescript
executableUsers?: pulumi.Input<pulumi.Input<string>[]>;
```


Limit search to users with *explicit* launch permission on
the image. Valid items are the numeric account ID or `self`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L36">property filters</a>
</h3>

```typescript
filters?: pulumi.Input<{ ... }[]>;
```


One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L41">property mostRecent</a>
</h3>

```typescript
mostRecent?: pulumi.Input<boolean>;
```


If more than one result is returned, use the most
recent AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L49">property nameRegex</a>
</h3>

```typescript
nameRegex?: pulumi.Input<string>;
```


A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API. This
filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L54">property owners</a>
</h3>

```typescript
owners?: pulumi.Input<pulumi.Input<string>[]>;
```


Limit search to specific AMI owners. Valid items are the numeric
account ID, `amazon`, or `self`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L55">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="GetAmiIdsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L22">interface GetAmiIdsArgs</a>
</h2>

A collection of arguments for invoking getAmiIds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L27">property executableUsers</a>
</h3>

```typescript
executableUsers?: pulumi.Input<pulumi.Input<string>[]>;
```


Limit search to users with *explicit* launch
permission on  the image. Valid items are the numeric account ID or `self`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L33">property filters</a>
</h3>

```typescript
filters?: pulumi.Input<{ ... }[]>;
```


One or more name/value pairs to filter off of. There
are several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L41">property nameRegex</a>
</h3>

```typescript
nameRegex?: pulumi.Input<string>;
```


A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API.
This filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L46">property owners</a>
</h3>

```typescript
owners?: pulumi.Input<pulumi.Input<string>[]>;
```


Limit search to specific AMI owners. Valid items are
the numeric account ID, `amazon`, or `self`.

<h2 class="pdoc-module-header" id="GetAmiIdsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L52">interface GetAmiIdsResult</a>
</h2>

A collection of values returned by getAmiIds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L57">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmiIds.ts#L53">property ids</a>
</h3>

```typescript
ids: string[];
```

<h2 class="pdoc-module-header" id="GetAmiResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L61">interface GetAmiResult</a>
</h2>

A collection of values returned by getAmi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L65">property architecture</a>
</h3>

```typescript
architecture: string;
```


The OS architecture of the AMI (ie: `i386` or `x86_64`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L83">property blockDeviceMappings</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L87">property creationDate</a>
</h3>

```typescript
creationDate: string;
```


The date and time the image was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L92">property description</a>
</h3>

```typescript
description: string;
```


The description of the AMI that was provided during image
creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L96">property hypervisor</a>
</h3>

```typescript
hypervisor: string;
```


The hypervisor type of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L188">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L100">property imageId</a>
</h3>

```typescript
imageId: string;
```


The ID of the AMI. Should be the same as the resource `id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L104">property imageLocation</a>
</h3>

```typescript
imageLocation: string;
```


The location of the AMI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L109">property imageOwnerAlias</a>
</h3>

```typescript
imageOwnerAlias: string;
```


The AWS account alias (for example, `amazon`, `self`) or
the AWS account ID of the AMI owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L113">property imageType</a>
</h3>

```typescript
imageType: string;
```


The type of image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L118">property kernelId</a>
</h3>

```typescript
kernelId: string;
```


The kernel associated with the image, if any. Only applicable
for machine images.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L122">property name</a>
</h3>

```typescript
name: string;
```


The name of the AMI that was provided during image creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L126">property ownerId</a>
</h3>

```typescript
ownerId: string;
```


The AWS account ID of the image owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L130">property platform</a>
</h3>

```typescript
platform: string;
```


The value is Windows for `Windows` AMIs; otherwise blank.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L136">property productCodes</a>
</h3>

```typescript
productCodes: { ... }[];
```


Any product codes associated with the AMI.
* `product_codes.#.product_code_id` - The product code.
* `product_codes.#.product_code_type` - The type of product code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L140">property public</a>
</h3>

```typescript
public: boolean;
```


`true` if the image has public launch permissions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L145">property ramdiskId</a>
</h3>

```typescript
ramdiskId: string;
```


The RAM disk associated with the image, if any. Only applicable
for machine images.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L149">property rootDeviceName</a>
</h3>

```typescript
rootDeviceName: string;
```


The device name of the root device.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L153">property rootDeviceType</a>
</h3>

```typescript
rootDeviceType: string;
```


The type of root device (ie: `ebs` or `instance-store`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L158">property rootSnapshotId</a>
</h3>

```typescript
rootSnapshotId: string;
```


The snapshot id associated with the root device, if any
(only applies to `ebs` root devices).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L162">property sriovNetSupport</a>
</h3>

```typescript
sriovNetSupport: string;
```


Specifies whether enhanced networking is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L167">property state</a>
</h3>

```typescript
state: string;
```


The current state of the AMI. If the state is `available`, the image
is successfully registered and can be used to launch an instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L173">property stateReason</a>
</h3>

```typescript
stateReason: { ... };
```


Describes a state change. Fields are `UNSET` if not available.
* `state_reason.code` - The reason code for the state change.
* `state_reason.message` - The message for the state change.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L179">property tags</a>
</h3>

```typescript
tags: { ... };
```


Any tags assigned to the image.
* `tags.#.key` - The key name of the tag.
* `tags.#.value` - The value of the tag.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAmi.ts#L184">property virtualizationType</a>
</h3>

```typescript
virtualizationType: string;
```


The type of virtualization of the AMI (ie: `hvm` or
`paravirtual`).

<h2 class="pdoc-module-header" id="GetArnArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L18">interface GetArnArgs</a>
</h2>

A collection of arguments for invoking getArn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L22">property arn</a>
</h3>

```typescript
arn: pulumi.Input<string>;
```


The ARN to parse.

<h2 class="pdoc-module-header" id="GetArnResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L28">interface GetArnResult</a>
</h2>

A collection of values returned by getArn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L32">property account</a>
</h3>

```typescript
account: string;
```


The [ID](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html) of the AWS account that owns the resource, without the hyphens.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L54">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L36">property partition</a>
</h3>

```typescript
partition: string;
```


The partition that the resource is in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L41">property region</a>
</h3>

```typescript
region: string;
```


The region the resource resides in.
Note that the ARNs for some resources do not require a region, so this component might be omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L46">property resource</a>
</h3>

```typescript
resource: string;
```


The content of this part of the ARN varies by service.
It often includes an indicator of the type of resource—for example, an IAM user or Amazon RDS database —followed by a slash (/) or a colon (:), followed by the resource name itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getArn.ts#L50">property service</a>
</h3>

```typescript
service: string;
```


The [service namespace](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces) that identifies the AWS product.

<h2 class="pdoc-module-header" id="GetAutoscalingGroupsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L20">interface GetAutoscalingGroupsArgs</a>
</h2>

A collection of arguments for invoking getAutoscalingGroups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L24">property filters</a>
</h3>

```typescript
filters?: pulumi.Input<{ ... }[]>;
```


A filter used to scope the list e.g. by tags. See [related docs](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_Filter.html).

<h2 class="pdoc-module-header" id="GetAutoscalingGroupsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L30">interface GetAutoscalingGroupsResult</a>
</h2>

A collection of values returned by getAutoscalingGroups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L38">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAutoscalingGroups.ts#L34">property names</a>
</h3>

```typescript
names: string[];
```


A list of the Autoscaling Groups in the current region.

<h2 class="pdoc-module-header" id="GetAvailabilityZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L30">interface GetAvailabilityZoneArgs</a>
</h2>

A collection of arguments for invoking getAvailabilityZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L34">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The full name of the availability zone to select.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L39">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


A specific availability zone state to require. May
be any of `"available"`, `"information"` or `"impaired"`.

<h2 class="pdoc-module-header" id="GetAvailabilityZoneResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L45">interface GetAvailabilityZoneResult</a>
</h2>

A collection of values returned by getAvailabilityZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L68">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L49">property name</a>
</h3>

```typescript
name: string;
```


The name of the selected availability zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L54">property nameSuffix</a>
</h3>

```typescript
nameSuffix: string;
```


The part of the AZ name that appears after the region name,
uniquely identifying the AZ within its region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L60">property region</a>
</h3>

```typescript
region: string;
```


The region where the selected availability zone resides.
This is always the region selected on the provider, since this data source
searches only within that region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZone.ts#L64">property state</a>
</h3>

```typescript
state: string;
```


The current state of the AZ.

<h2 class="pdoc-module-header" id="GetAvailabilityZonesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L24">interface GetAvailabilityZonesArgs</a>
</h2>

A collection of arguments for invoking getAvailabilityZones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L31">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


Allows to filter list of Availability Zones based on their
current state. Can be either `"available"`, `"information"`, `"impaired"` or
`"unavailable"`. By default the list includes a complete set of Availability Zones
to which the underlying AWS account has access, regardless of their state.

<h2 class="pdoc-module-header" id="GetAvailabilityZonesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L37">interface GetAvailabilityZonesResult</a>
</h2>

A collection of values returned by getAvailabilityZones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L45">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getAvailabilityZones.ts#L41">property names</a>
</h3>

```typescript
names: string[];
```


A list of the Availability Zone names available to the account.

<h2 class="pdoc-module-header" id="GetBillingServiceAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts#L17">interface GetBillingServiceAccountResult</a>
</h2>

A collection of values returned by getBillingServiceAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts#L21">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the AWS billing service account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getBillingServiceAccount.ts#L25">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetCallerIdentityResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L18">interface GetCallerIdentityResult</a>
</h2>

A collection of values returned by getCallerIdentity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L22">property accountId</a>
</h3>

```typescript
accountId: string;
```


The AWS Account ID number of the account that owns or contains the calling entity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L26">property arn</a>
</h3>

```typescript
arn: string;
```


The AWS ARN associated with the calling entity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L34">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCallerIdentity.ts#L30">property userId</a>
</h3>

```typescript
userId: string;
```


The unique identifier of the calling entity.

<h2 class="pdoc-module-header" id="GetCanonicalUserIdResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts#L18">interface GetCanonicalUserIdResult</a>
</h2>

A collection of values returned by getCanonicalUserId.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts#L22">property displayName</a>
</h3>

```typescript
displayName: string;
```


The human-friendly name linked to the canonical user ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getCanonicalUserId.ts#L26">property id</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L27">property id</a>
</h3>

```typescript
id?: pulumi.Input<string>;
```


The allocation id of the specific EIP to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L31">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The public IP of the specific EIP to retrieve.

<h2 class="pdoc-module-header" id="GetElasticIpResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L37">interface GetElasticIpResult</a>
</h2>

A collection of values returned by getElasticIp.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L38">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getElasticIp.ts#L39">property publicIp</a>
</h3>

```typescript
publicIp: string;
```

<h2 class="pdoc-module-header" id="GetIpRangesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L19">interface GetIpRangesArgs</a>
</h2>

A collection of arguments for invoking getIpRanges.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L25">property regions</a>
</h3>

```typescript
regions?: pulumi.Input<pulumi.Input<string>[]>;
```


Filter IP ranges by regions (or include all regions, if
omitted). Valid items are `global` (for `cloudfront`) as well as all AWS regions
(e.g. `eu-central-1`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L30">property services</a>
</h3>

```typescript
services: pulumi.Input<pulumi.Input<string>[]>;
```


Filter IP ranges by services. Valid items are `amazon`
(for amazon.com), `cloudfront`, `codebuild`, `ec2`, `route53`, `route53_healthchecks` and `S3`.

<h2 class="pdoc-module-header" id="GetIpRangesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L36">interface GetIpRangesResult</a>
</h2>

A collection of values returned by getIpRanges.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L40">property cidrBlocks</a>
</h3>

```typescript
cidrBlocks: string[];
```


The lexically ordered list of CIDR blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L44">property createDate</a>
</h3>

```typescript
createDate: string;
```


The publication time of the IP ranges (e.g. `2016-08-03-23-46-05`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L53">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getIpRanges.ts#L49">property syncToken</a>
</h3>

```typescript
syncToken: number;
```


The publication time of the IP ranges, in Unix epoch time format
(e.g. `1470267965`).

<h2 class="pdoc-module-header" id="GetPartitionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts#L17">interface GetPartitionResult</a>
</h2>

A collection of values returned by getPartition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts#L22">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPartition.ts#L18">property partition</a>
</h3>

```typescript
partition: string;
```

<h2 class="pdoc-module-header" id="GetPrefixListArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L26">interface GetPrefixListArgs</a>
</h2>

A collection of arguments for invoking getPrefixList.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L30">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the prefix list to select.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L34">property prefixListId</a>
</h3>

```typescript
prefixListId?: pulumi.Input<string>;
```


The ID of the prefix list to select.

<h2 class="pdoc-module-header" id="GetPrefixListResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L40">interface GetPrefixListResult</a>
</h2>

A collection of values returned by getPrefixList.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L45">property cidrBlocks</a>
</h3>

```typescript
cidrBlocks: string[];
```


The list of CIDR blocks for the AWS service associated
with the prefix list.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L53">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getPrefixList.ts#L49">property name</a>
</h3>

```typescript
name: string;
```


The name of the selected prefix list.

<h2 class="pdoc-module-header" id="GetRegionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L26">interface GetRegionArgs</a>
</h2>

A collection of arguments for invoking getRegion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L27">property current</a>
</h3>

```typescript
current?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L31">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The EC2 endpoint of the region to select.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L35">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The full name of the region to select.

<h2 class="pdoc-module-header" id="GetRegionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L41">interface GetRegionResult</a>
</h2>

A collection of values returned by getRegion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L46">property current</a>
</h3>

```typescript
current: boolean;
```


`true` if the selected region is the one configured on the
provider, or `false` otherwise.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L50">property endpoint</a>
</h3>

```typescript
endpoint: string;
```


The EC2 endpoint for the selected region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L58">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/getRegion.ts#L54">property name</a>
</h3>

```typescript
name: string;
```


The name of the selected region.

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

<h2 class="pdoc-module-header" id="Region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/region.ts#L34">type Region</a>
</h2>

```typescript
type Region = ap-northeast-1 | ap-northeast-2 | ap-south-1 | ap-southeast-2 | ap-southeast-1 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | sa-east-1 | us-east-1 | us-east-2 | us-west-1 | us-west-2;
```


A Region represents any valid Amazon region that may be targeted with deployments.

