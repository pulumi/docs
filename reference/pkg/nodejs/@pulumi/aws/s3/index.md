---
title: Module s3
---

<a href="../index.html">@pulumi/aws</a> &gt; s3

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Bucket">class Bucket</a>
* <a href="#BucketMetric">class BucketMetric</a>
* <a href="#BucketNotification">class BucketNotification</a>
* <a href="#BucketObject">class BucketObject</a>
* <a href="#BucketPolicy">class BucketPolicy</a>
* <a href="#Inventory">class Inventory</a>
* <a href="#getBucket">function getBucket</a>
* <a href="#getBucketObject">function getBucketObject</a>
* <a href="#BucketArgs">interface BucketArgs</a>
* <a href="#BucketMetricArgs">interface BucketMetricArgs</a>
* <a href="#BucketMetricState">interface BucketMetricState</a>
* <a href="#BucketNotificationArgs">interface BucketNotificationArgs</a>
* <a href="#BucketNotificationState">interface BucketNotificationState</a>
* <a href="#BucketObjectArgs">interface BucketObjectArgs</a>
* <a href="#BucketObjectState">interface BucketObjectState</a>
* <a href="#BucketPolicyArgs">interface BucketPolicyArgs</a>
* <a href="#BucketPolicyState">interface BucketPolicyState</a>
* <a href="#BucketState">interface BucketState</a>
* <a href="#GetBucketArgs">interface GetBucketArgs</a>
* <a href="#GetBucketObjectArgs">interface GetBucketObjectArgs</a>
* <a href="#GetBucketObjectResult">interface GetBucketObjectResult</a>
* <a href="#GetBucketResult">interface GetBucketResult</a>
* <a href="#InventoryArgs">interface InventoryArgs</a>
* <a href="#InventoryState">interface InventoryState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts">s3/bucket.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts">s3/bucketMetric.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts">s3/bucketNotification.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts">s3/bucketObject.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts">s3/bucketPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts">s3/getBucket.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts">s3/getBucketObject.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts">s3/inventory.ts</a> 


<h2 class="pdoc-module-header" id="Bucket">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L12">class Bucket</a>
</h2>

Provides a S3 bucket resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L115">constructor</a>
</h3>

```typescript
new Bucket(name: string, args?: BucketArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Bucket resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketState): Bucket
```


Get an existing Bucket resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L28">property accelerationStatus</a>
</h3>

```typescript
public accelerationStatus: pulumi.Output<string>;
```


Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L32">property acl</a>
</h3>

```typescript
public acl: pulumi.Output<string | undefined>;
```


The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L36">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L40">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L44">property bucketDomainName</a>
</h3>

```typescript
public bucketDomainName: pulumi.Output<string>;
```


The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L48">property bucketPrefix</a>
</h3>

```typescript
public bucketPrefix: pulumi.Output<string | undefined>;
```


Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L52">property bucketRegionalDomainName</a>
</h3>

```typescript
public bucketRegionalDomainName: pulumi.Output<string>;
```


The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L56">property corsRules</a>
</h3>

```typescript
public corsRules: pulumi.Output<{ ... }[] | undefined>;
```


A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L60">property forceDestroy</a>
</h3>

```typescript
public forceDestroy: pulumi.Output<boolean | undefined>;
```


A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L64">property hostedZoneId</a>
</h3>

```typescript
public hostedZoneId: pulumi.Output<string>;
```


The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket's region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L68">property lifecycleRules</a>
</h3>

```typescript
public lifecycleRules: pulumi.Output<{ ... }[] | undefined>;
```


A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L72">property loggings</a>
</h3>

```typescript
public loggings: pulumi.Output<{ ... }[] | undefined>;
```


A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L76">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string | undefined>;
```


A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a `terraform plan`. In this case, please make sure you use the verbose/specific version of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L80">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L84">property replicationConfiguration</a>
</h3>

```typescript
public replicationConfiguration: pulumi.Output<{ ... } | undefined>;
```


A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L91">property requestPayer</a>
</h3>

```typescript
public requestPayer: pulumi.Output<string>;
```


Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L95">property serverSideEncryptionConfiguration</a>
</h3>

```typescript
public serverSideEncryptionConfiguration: pulumi.Output<{ ... } | undefined>;
```


A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L99">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Specifies object tags key and value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L103">property versioning</a>
</h3>

```typescript
public versioning: pulumi.Output<{ ... }>;
```


A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L107">property website</a>
</h3>

```typescript
public website: pulumi.Output<{ ... } | undefined>;
```


A website object (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L111">property websiteDomain</a>
</h3>

```typescript
public websiteDomain: pulumi.Output<string>;
```


The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L115">property websiteEndpoint</a>
</h3>

```typescript
public websiteEndpoint: pulumi.Output<string>;
```


The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.

<h2 class="pdoc-module-header" id="BucketMetric">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L10">class BucketMetric</a>
</h2>

Provides a S3 bucket [metrics configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html) resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L34">constructor</a>
</h3>

```typescript
new BucketMetric(name: string, args: BucketMetricArgs, opts?: pulumi.CustomResourceOptions)
```


Create a BucketMetric resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketMetricState): BucketMetric
```


Get an existing BucketMetric resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L26">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket to put metric configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L30">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<{ ... } | undefined>;
```


[Object filtering](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter) that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Unique identifier of the metrics configuration for the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BucketNotification">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L10">class BucketNotification</a>
</h2>

Provides a S3 bucket notification resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L38">constructor</a>
</h3>

```typescript
new BucketNotification(name: string, args: BucketNotificationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a BucketNotification resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketNotificationState): BucketNotification
```


Get an existing BucketNotification resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L26">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket to put notification configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L30">property lambdaFunctions</a>
</h3>

```typescript
public lambdaFunctions: pulumi.Output<{ ... }[] | undefined>;
```


Used to configure notifications to a Lambda Function (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L34">property queues</a>
</h3>

```typescript
public queues: pulumi.Output<{ ... }[] | undefined>;
```


The notification configuration to SQS Queue (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L38">property topics</a>
</h3>

```typescript
public topics: pulumi.Output<{ ... }[] | undefined>;
```


The notification configuration to SNS Topic (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BucketObject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L13">class BucketObject</a>
</h2>

Provides a S3 bucket object resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L103">constructor</a>
</h3>

```typescript
new BucketObject(name: string, args: BucketObjectArgs, opts?: pulumi.CustomResourceOptions)
```


Create a BucketObject resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketObjectState): BucketObject
```


Get an existing BucketObject resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L29">property acl</a>
</h3>

```typescript
public acl: pulumi.Output<string | undefined>;
```


The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L33">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket to put the file in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L37">property cacheControl</a>
</h3>

```typescript
public cacheControl: pulumi.Output<string | undefined>;
```


Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L41">property content</a>
</h3>

```typescript
public content: pulumi.Output<string | undefined>;
```


Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L45">property contentBase64</a>
</h3>

```typescript
public contentBase64: pulumi.Output<string | undefined>;
```


Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L49">property contentDisposition</a>
</h3>

```typescript
public contentDisposition: pulumi.Output<string | undefined>;
```


Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L53">property contentEncoding</a>
</h3>

```typescript
public contentEncoding: pulumi.Output<string | undefined>;
```


Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L57">property contentLanguage</a>
</h3>

```typescript
public contentLanguage: pulumi.Output<string | undefined>;
```


The language the content is in e.g. en-US or en-GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L61">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string>;
```


A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L66">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


Used to trigger updates. The only meaningful value is `${md5(file("path/to/file"))}`.
This attribute is not compatible with KMS encryption, `kms_key_id` or `server_side_encryption = "aws:kms"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L70">property key</a>
</h3>

```typescript
public key: pulumi.Output<string>;
```


The name of the object once it is in the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L77">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string | undefined>;
```


Specifies the AWS KMS Key ARN to use for object encryption.
This value is a fully qualified **ARN** of the KMS Key. If using `aws_kms_key`,
use the exported `arn` attribute:
`kms_key_id = "${aws_kms_key.foo.arn}"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L81">property serverSideEncryption</a>
</h3>

```typescript
public serverSideEncryption: pulumi.Output<string>;
```


Specifies server-side encryption of the object in S3. Valid values are "`AES256`" and "`aws:kms`".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L85">property source</a>
</h3>

```typescript
public source: pulumi.Output<pulumi.asset.Asset | undefined>;
```


The path to a file that will be read and uploaded as raw bytes for the object content.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L90">property storageClass</a>
</h3>

```typescript
public storageClass: pulumi.Output<string>;
```


Specifies the desired [Storage Class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html)
for the object. Can be either "`STANDARD`", "`REDUCED_REDUNDANCY`", "`ONEZONE_IA`", or "`STANDARD_IA`". Defaults to "`STANDARD`".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L94">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L99">property versionId</a>
</h3>

```typescript
public versionId: pulumi.Output<string>;
```


A unique version ID value for the object, if bucket versioning
is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L103">property websiteRedirect</a>
</h3>

```typescript
public websiteRedirect: pulumi.Output<string | undefined>;
```


Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html).

<h2 class="pdoc-module-header" id="BucketPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L12">class BucketPolicy</a>
</h2>

Attaches a policy to an S3 bucket resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L32">constructor</a>
</h3>

```typescript
new BucketPolicy(name: string, args: BucketPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a BucketPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketPolicyState): BucketPolicy
```


Get an existing BucketPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L28">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket to which to apply the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L32">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The text of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Inventory">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L10">class Inventory</a>
</h2>

Provides a S3 bucket [inventory configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html) resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L54">constructor</a>
</h3>

```typescript
new Inventory(name: string, args: InventoryArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Inventory resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InventoryState): Inventory
```


Get an existing Inventory resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L26">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The S3 bucket configuration where inventory results are published (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L30">property destination</a>
</h3>

```typescript
public destination: pulumi.Output<{ ... }>;
```


Destination bucket where inventory list files are written (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L34">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Specifies whether the inventory is enabled or disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L38">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<{ ... } | undefined>;
```


Object filtering that accepts a prefix (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L42">property includedObjectVersions</a>
</h3>

```typescript
public includedObjectVersions: pulumi.Output<string>;
```


Object filtering that accepts a prefix (documented below). Can be `All` or `Current`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Unique identifier of the inventory configuration for the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L50">property optionalFields</a>
</h3>

```typescript
public optionalFields: pulumi.Output<string[] | undefined>;
```


Contains the optional fields that are included in the inventory results.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L54">property schedule</a>
</h3>

```typescript
public schedule: pulumi.Output<{ ... }>;
```


Contains the frequency for generating inventory results (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getBucket">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L13">function getBucket</a>
</h2>

```typescript
getBucket(args: GetBucketArgs, opts?: pulumi.InvokeOptions): Promise<GetBucketResult>
```


Provides details about a specific S3 bucket.

This resource may prove useful when setting up a Route53 record, or an origin for a CloudFront
Distribution.

<h2 class="pdoc-module-header" id="getBucketObject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L13">function getBucketObject</a>
</h2>

```typescript
getBucketObject(args: GetBucketObjectArgs, opts?: pulumi.InvokeOptions): Promise<GetBucketObjectResult>
```


The S3 object data source allows access to the metadata and
_optionally_ (see below) content of an object stored inside S3 bucket.

~> **Note:** The content of an object (`body` field) is available only for objects which have a human-readable `Content-Type` (`text/*` and `application/json`). This is to prevent printing unsafe characters and potentially downloading large amount of data which would be thrown away in favour of metadata.

<h2 class="pdoc-module-header" id="BucketArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L280">interface BucketArgs</a>
</h2>

The set of arguments for constructing a Bucket resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L284">property accelerationStatus</a>
</h3>

```typescript
accelerationStatus?: pulumi.Input<string>;
```


Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L288">property acl</a>
</h3>

```typescript
acl?: pulumi.Input<string>;
```


The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L292">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L296">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L300">property bucketPrefix</a>
</h3>

```typescript
bucketPrefix?: pulumi.Input<string>;
```


Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L304">property corsRules</a>
</h3>

```typescript
corsRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L308">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L312">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId?: pulumi.Input<string>;
```


The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket's region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L316">property lifecycleRules</a>
</h3>

```typescript
lifecycleRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L320">property loggings</a>
</h3>

```typescript
loggings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L324">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a `terraform plan`. In this case, please make sure you use the verbose/specific version of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L328">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L332">property replicationConfiguration</a>
</h3>

```typescript
replicationConfiguration?: pulumi.Input<{ ... }>;
```


A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L339">property requestPayer</a>
</h3>

```typescript
requestPayer?: pulumi.Input<string>;
```


Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L343">property serverSideEncryptionConfiguration</a>
</h3>

```typescript
serverSideEncryptionConfiguration?: pulumi.Input<{ ... }>;
```


A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L347">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Specifies object tags key and value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L351">property versioning</a>
</h3>

```typescript
versioning?: pulumi.Input<{ ... }>;
```


A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L355">property website</a>
</h3>

```typescript
website?: pulumi.Input<{ ... }>;
```


A website object (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L359">property websiteDomain</a>
</h3>

```typescript
websiteDomain?: pulumi.Input<string>;
```


The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L363">property websiteEndpoint</a>
</h3>

```typescript
websiteEndpoint?: pulumi.Input<string>;
```


The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.

<h2 class="pdoc-module-header" id="BucketMetricArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L85">interface BucketMetricArgs</a>
</h2>

The set of arguments for constructing a BucketMetric resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L89">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket to put metric configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L93">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<{ ... }>;
```


[Object filtering](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter) that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique identifier of the metrics configuration for the bucket.

<h2 class="pdoc-module-header" id="BucketMetricState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L67">interface BucketMetricState</a>
</h2>

Input properties used for looking up and filtering BucketMetric resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L71">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the bucket to put metric configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L75">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<{ ... }>;
```


[Object filtering](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter) that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketMetric.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique identifier of the metrics configuration for the bucket.

<h2 class="pdoc-module-header" id="BucketNotificationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L95">interface BucketNotificationArgs</a>
</h2>

The set of arguments for constructing a BucketNotification resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L99">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket to put notification configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L103">property lambdaFunctions</a>
</h3>

```typescript
lambdaFunctions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Used to configure notifications to a Lambda Function (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L107">property queues</a>
</h3>

```typescript
queues?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The notification configuration to SQS Queue (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L111">property topics</a>
</h3>

```typescript
topics?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The notification configuration to SNS Topic (documented below).

<h2 class="pdoc-module-header" id="BucketNotificationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L73">interface BucketNotificationState</a>
</h2>

Input properties used for looking up and filtering BucketNotification resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L77">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the bucket to put notification configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L81">property lambdaFunctions</a>
</h3>

```typescript
lambdaFunctions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Used to configure notifications to a Lambda Function (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L85">property queues</a>
</h3>

```typescript
queues?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The notification configuration to SQS Queue (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketNotification.ts#L89">property topics</a>
</h3>

```typescript
topics?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The notification configuration to SNS Topic (documented below).

<h2 class="pdoc-module-header" id="BucketObjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L250">interface BucketObjectArgs</a>
</h2>

The set of arguments for constructing a BucketObject resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L254">property acl</a>
</h3>

```typescript
acl?: pulumi.Input<string>;
```


The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L258">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string | Bucket>;
```


The name of the bucket to put the file in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L262">property cacheControl</a>
</h3>

```typescript
cacheControl?: pulumi.Input<string>;
```


Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L266">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L270">property contentBase64</a>
</h3>

```typescript
contentBase64?: pulumi.Input<string>;
```


Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L274">property contentDisposition</a>
</h3>

```typescript
contentDisposition?: pulumi.Input<string>;
```


Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L278">property contentEncoding</a>
</h3>

```typescript
contentEncoding?: pulumi.Input<string>;
```


Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L282">property contentLanguage</a>
</h3>

```typescript
contentLanguage?: pulumi.Input<string>;
```


The language the content is in e.g. en-US or en-GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L286">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L291">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


Used to trigger updates. The only meaningful value is `${md5(file("path/to/file"))}`.
This attribute is not compatible with KMS encryption, `kms_key_id` or `server_side_encryption = "aws:kms"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L295">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


The name of the object once it is in the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L302">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


Specifies the AWS KMS Key ARN to use for object encryption.
This value is a fully qualified **ARN** of the KMS Key. If using `aws_kms_key`,
use the exported `arn` attribute:
`kms_key_id = "${aws_kms_key.foo.arn}"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L306">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: pulumi.Input<string>;
```


Specifies server-side encryption of the object in S3. Valid values are "`AES256`" and "`aws:kms`".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L310">property source</a>
</h3>

```typescript
source?: pulumi.Input<pulumi.asset.Asset>;
```


The path to a file that will be read and uploaded as raw bytes for the object content.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L315">property storageClass</a>
</h3>

```typescript
storageClass?: pulumi.Input<string>;
```


Specifies the desired [Storage Class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html)
for the object. Can be either "`STANDARD`", "`REDUCED_REDUNDANCY`", "`ONEZONE_IA`", or "`STANDARD_IA`". Defaults to "`STANDARD`".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L319">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L323">property websiteRedirect</a>
</h3>

```typescript
websiteRedirect?: pulumi.Input<string>;
```


Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html).

<h2 class="pdoc-module-header" id="BucketObjectState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L166">interface BucketObjectState</a>
</h2>

Input properties used for looking up and filtering BucketObject resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L170">property acl</a>
</h3>

```typescript
acl?: pulumi.Input<string>;
```


The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L174">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string | Bucket>;
```


The name of the bucket to put the file in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L178">property cacheControl</a>
</h3>

```typescript
cacheControl?: pulumi.Input<string>;
```


Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L182">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L186">property contentBase64</a>
</h3>

```typescript
contentBase64?: pulumi.Input<string>;
```


Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L190">property contentDisposition</a>
</h3>

```typescript
contentDisposition?: pulumi.Input<string>;
```


Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L194">property contentEncoding</a>
</h3>

```typescript
contentEncoding?: pulumi.Input<string>;
```


Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L198">property contentLanguage</a>
</h3>

```typescript
contentLanguage?: pulumi.Input<string>;
```


The language the content is in e.g. en-US or en-GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L202">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L207">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


Used to trigger updates. The only meaningful value is `${md5(file("path/to/file"))}`.
This attribute is not compatible with KMS encryption, `kms_key_id` or `server_side_encryption = "aws:kms"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L211">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


The name of the object once it is in the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L218">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


Specifies the AWS KMS Key ARN to use for object encryption.
This value is a fully qualified **ARN** of the KMS Key. If using `aws_kms_key`,
use the exported `arn` attribute:
`kms_key_id = "${aws_kms_key.foo.arn}"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L222">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: pulumi.Input<string>;
```


Specifies server-side encryption of the object in S3. Valid values are "`AES256`" and "`aws:kms`".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L226">property source</a>
</h3>

```typescript
source?: pulumi.Input<pulumi.asset.Asset>;
```


The path to a file that will be read and uploaded as raw bytes for the object content.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L231">property storageClass</a>
</h3>

```typescript
storageClass?: pulumi.Input<string>;
```


Specifies the desired [Storage Class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html)
for the object. Can be either "`STANDARD`", "`REDUCED_REDUNDANCY`", "`ONEZONE_IA`", or "`STANDARD_IA`". Defaults to "`STANDARD`".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L235">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L240">property versionId</a>
</h3>

```typescript
versionId?: pulumi.Input<string>;
```


A unique version ID value for the object, if bucket versioning
is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketObject.ts#L244">property websiteRedirect</a>
</h3>

```typescript
websiteRedirect?: pulumi.Input<string>;
```


Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html).

<h2 class="pdoc-module-header" id="BucketPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L80">interface BucketPolicyArgs</a>
</h2>

The set of arguments for constructing a BucketPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L84">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket to which to apply the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L88">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string | PolicyDocument>;
```


The text of the policy.

<h2 class="pdoc-module-header" id="BucketPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L66">interface BucketPolicyState</a>
</h2>

Input properties used for looking up and filtering BucketPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L70">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the bucket to which to apply the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucketPolicy.ts#L74">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string | PolicyDocument>;
```


The text of the policy.

<h2 class="pdoc-module-header" id="BucketState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L183">interface BucketState</a>
</h2>

Input properties used for looking up and filtering Bucket resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L187">property accelerationStatus</a>
</h3>

```typescript
accelerationStatus?: pulumi.Input<string>;
```


Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L191">property acl</a>
</h3>

```typescript
acl?: pulumi.Input<string>;
```


The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L195">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L199">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L203">property bucketDomainName</a>
</h3>

```typescript
bucketDomainName?: pulumi.Input<string>;
```


The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L207">property bucketPrefix</a>
</h3>

```typescript
bucketPrefix?: pulumi.Input<string>;
```


Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L211">property bucketRegionalDomainName</a>
</h3>

```typescript
bucketRegionalDomainName?: pulumi.Input<string>;
```


The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L215">property corsRules</a>
</h3>

```typescript
corsRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L219">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L223">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId?: pulumi.Input<string>;
```


The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket's region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L227">property lifecycleRules</a>
</h3>

```typescript
lifecycleRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L231">property loggings</a>
</h3>

```typescript
loggings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L235">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a `terraform plan`. In this case, please make sure you use the verbose/specific version of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L239">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L243">property replicationConfiguration</a>
</h3>

```typescript
replicationConfiguration?: pulumi.Input<{ ... }>;
```


A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L250">property requestPayer</a>
</h3>

```typescript
requestPayer?: pulumi.Input<string>;
```


Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L254">property serverSideEncryptionConfiguration</a>
</h3>

```typescript
serverSideEncryptionConfiguration?: pulumi.Input<{ ... }>;
```


A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L258">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Specifies object tags key and value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L262">property versioning</a>
</h3>

```typescript
versioning?: pulumi.Input<{ ... }>;
```


A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L266">property website</a>
</h3>

```typescript
website?: pulumi.Input<{ ... }>;
```


A website object (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L270">property websiteDomain</a>
</h3>

```typescript
websiteDomain?: pulumi.Input<string>;
```


The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/bucket.ts#L274">property websiteEndpoint</a>
</h3>

```typescript
websiteEndpoint?: pulumi.Input<string>;
```


The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.

<h2 class="pdoc-module-header" id="GetBucketArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L22">interface GetBucketArgs</a>
</h2>

A collection of arguments for invoking getBucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L26">property bucket</a>
</h3>

```typescript
bucket: string;
```


The name of the bucket

<h2 class="pdoc-module-header" id="GetBucketObjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L26">interface GetBucketObjectArgs</a>
</h2>

A collection of arguments for invoking getBucketObject.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L30">property bucket</a>
</h3>

```typescript
bucket: string;
```


The name of the bucket to read the object from

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L34">property key</a>
</h3>

```typescript
key: string;
```


The full path to the object inside the bucket

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L35">property range</a>
</h3>

```typescript
range?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L36">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L40">property versionId</a>
</h3>

```typescript
versionId?: string;
```


Specific version ID of the object returned (defaults to latest version)

<h2 class="pdoc-module-header" id="GetBucketObjectResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L46">interface GetBucketObjectResult</a>
</h2>

A collection of values returned by getBucketObject.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L50">property body</a>
</h3>

```typescript
body: string;
```


Object data (see **limitations above** to understand cases in which this field is actually available)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L54">property cacheControl</a>
</h3>

```typescript
cacheControl: string;
```


Specifies caching behavior along the request/reply chain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L58">property contentDisposition</a>
</h3>

```typescript
contentDisposition: string;
```


Specifies presentational information for the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L62">property contentEncoding</a>
</h3>

```typescript
contentEncoding: string;
```


Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L66">property contentLanguage</a>
</h3>

```typescript
contentLanguage: string;
```


The language the content is in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L70">property contentLength</a>
</h3>

```typescript
contentLength: number;
```


Size of the body in bytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L74">property contentType</a>
</h3>

```typescript
contentType: string;
```


A standard MIME type describing the format of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L78">property etag</a>
</h3>

```typescript
etag: string;
```


[ETag](https://en.wikipedia.org/wiki/HTTP_ETag) generated for the object (an MD5 sum of the object content in case it's not encrypted)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L82">property expiration</a>
</h3>

```typescript
expiration: string;
```


If the object expiration is configured (see [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html)), the field includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L86">property expires</a>
</h3>

```typescript
expires: string;
```


The date and time at which the object is no longer cacheable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L122">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L90">property lastModified</a>
</h3>

```typescript
lastModified: string;
```


Last modified date of the object in RFC1123 format (e.g. `Mon, 02 Jan 2006 15:04:05 MST`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L94">property metadata</a>
</h3>

```typescript
metadata: { ... };
```


A map of metadata stored with the object in S3

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L98">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption: string;
```


If the object is stored using server-side encryption (KMS or Amazon S3-managed encryption key), this field includes the chosen encryption and algorithm used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L102">property sseKmsKeyId</a>
</h3>

```typescript
sseKmsKeyId: string;
```


If present, specifies the ID of the Key Management Service (KMS) master encryption key that was used for the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L106">property storageClass</a>
</h3>

```typescript
storageClass: string;
```


[Storage class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) information of the object. Available for all objects except for `Standard` storage class objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L110">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L114">property versionId</a>
</h3>

```typescript
versionId: string;
```


The latest version ID of the object returned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucketObject.ts#L118">property websiteRedirectLocation</a>
</h3>

```typescript
websiteRedirectLocation: string;
```


If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

<h2 class="pdoc-module-header" id="GetBucketResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L32">interface GetBucketResult</a>
</h2>

A collection of values returned by getBucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L36">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L40">property bucketDomainName</a>
</h3>

```typescript
bucketDomainName: string;
```


The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L44">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId: string;
```


The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket's region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L60">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L48">property region</a>
</h3>

```typescript
region: string;
```


The AWS region this bucket resides in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L52">property websiteDomain</a>
</h3>

```typescript
websiteDomain: string;
```


The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/getBucket.ts#L56">property websiteEndpoint</a>
</h3>

```typescript
websiteEndpoint: string;
```


The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.

<h2 class="pdoc-module-header" id="InventoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L144">interface InventoryArgs</a>
</h2>

The set of arguments for constructing a Inventory resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L148">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The S3 bucket configuration where inventory results are published (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L152">property destination</a>
</h3>

```typescript
destination: pulumi.Input<{ ... }>;
```


Destination bucket where inventory list files are written (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L156">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether the inventory is enabled or disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L160">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<{ ... }>;
```


Object filtering that accepts a prefix (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L164">property includedObjectVersions</a>
</h3>

```typescript
includedObjectVersions: pulumi.Input<string>;
```


Object filtering that accepts a prefix (documented below). Can be `All` or `Current`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L168">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique identifier of the inventory configuration for the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L172">property optionalFields</a>
</h3>

```typescript
optionalFields?: pulumi.Input<pulumi.Input<string>[]>;
```


Contains the optional fields that are included in the inventory results.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L176">property schedule</a>
</h3>

```typescript
schedule: pulumi.Input<{ ... }>;
```


Contains the frequency for generating inventory results (documented below).

<h2 class="pdoc-module-header" id="InventoryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L106">interface InventoryState</a>
</h2>

Input properties used for looking up and filtering Inventory resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L110">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The S3 bucket configuration where inventory results are published (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L114">property destination</a>
</h3>

```typescript
destination?: pulumi.Input<{ ... }>;
```


Destination bucket where inventory list files are written (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L118">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether the inventory is enabled or disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L122">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<{ ... }>;
```


Object filtering that accepts a prefix (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L126">property includedObjectVersions</a>
</h3>

```typescript
includedObjectVersions?: pulumi.Input<string>;
```


Object filtering that accepts a prefix (documented below). Can be `All` or `Current`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique identifier of the inventory configuration for the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L134">property optionalFields</a>
</h3>

```typescript
optionalFields?: pulumi.Input<pulumi.Input<string>[]>;
```


Contains the optional fields that are included in the inventory results.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/inventory.ts#L138">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<{ ... }>;
```


Contains the frequency for generating inventory results (documented below).

