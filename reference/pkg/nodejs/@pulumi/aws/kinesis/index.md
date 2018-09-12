---
title: Module kinesis
---

<a href="../index.html">@pulumi/aws</a> &gt; kinesis

<h2 class="pdoc-module-header">Index</h2>

* <a href="#FirehoseDeliveryStream">class FirehoseDeliveryStream</a>
* <a href="#Stream">class Stream</a>
* <a href="#getStream">function getStream</a>
* <a href="#FirehoseDeliveryStreamArgs">interface FirehoseDeliveryStreamArgs</a>
* <a href="#FirehoseDeliveryStreamState">interface FirehoseDeliveryStreamState</a>
* <a href="#GetStreamArgs">interface GetStreamArgs</a>
* <a href="#GetStreamResult">interface GetStreamResult</a>
* <a href="#StreamArgs">interface StreamArgs</a>
* <a href="#StreamState">interface StreamState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts">kinesis/firehoseDeliveryStream.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts">kinesis/getStream.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts">kinesis/stream.ts</a> 


<h2 class="pdoc-module-header" id="FirehoseDeliveryStream">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L12">class FirehoseDeliveryStream</a>
</h2>

Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.

For more details, see the [Amazon Kinesis Firehose Documentation][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L63">constructor</a>
</h3>

```typescript
new FirehoseDeliveryStream(name: string, args: FirehoseDeliveryStreamArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FirehoseDeliveryStream resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirehoseDeliveryStreamState): FirehoseDeliveryStream
```


Get an existing FirehoseDeliveryStream resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) specifying the Stream

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L32">property destination</a>
</h3>

```typescript
public destination: pulumi.Output<string>;
```


This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L33">property destinationId</a>
</h3>

```typescript
public destinationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L34">property elasticsearchConfiguration</a>
</h3>

```typescript
public elasticsearchConfiguration: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L38">property extendedS3Configuration</a>
</h3>

```typescript
public extendedS3Configuration: pulumi.Output<{ ... } | undefined>;
```


Enhanced configuration options for the s3 destination. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L42">property kinesisSourceConfiguration</a>
</h3>

```typescript
public kinesisSourceConfiguration: pulumi.Output<{ ... } | undefined>;
```


Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L47">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L53">property redshiftConfiguration</a>
</h3>

```typescript
public redshiftConfiguration: pulumi.Output<{ ... } | undefined>;
```


Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L58">property s3Configuration</a>
</h3>

```typescript
public s3Configuration: pulumi.Output<{ ... } | undefined>;
```


Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L59">property splunkConfiguration</a>
</h3>

```typescript
public splunkConfiguration: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L63">property versionId</a>
</h3>

```typescript
public versionId: pulumi.Output<string>;
```


Specifies the table version for the output data schema. Defaults to `LATEST`.

<h2 class="pdoc-module-header" id="Stream">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L15">class Stream</a>
</h2>

Provides a Kinesis Stream resource. Amazon Kinesis is a managed service that
scales elastically for real-time processing of streaming big data.

For more details, see the [Amazon Kinesis Documentation][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L62">constructor</a>
</h3>

```typescript
new Stream(name: string, args: StreamArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Stream resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StreamState): Stream
```


Get an existing Stream resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L31">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) specifying the Stream (same as `id`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L35">property encryptionType</a>
</h3>

```typescript
public encryptionType: pulumi.Output<string | undefined>;
```


The encryption type to use. The only acceptable values are `NONE` or `KMS`. The default value is `NONE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L39">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string | undefined>;
```


The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias aws/kinesis.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L48">property retentionPeriod</a>
</h3>

```typescript
public retentionPeriod: pulumi.Output<number | undefined>;
```


Length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours. Minimum value is 24. Default is 24.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L54">property shardCount</a>
</h3>

```typescript
public shardCount: pulumi.Output<number>;
```


The number of shards that the stream will use.
Amazon has guidlines for specifying the Stream size that should be referenced
when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L58">property shardLevelMetrics</a>
</h3>

```typescript
public shardLevelMetrics: pulumi.Output<string[] | undefined>;
```


A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L62">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getStream">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L13">function getStream</a>
</h2>

```typescript
getStream(args: GetStreamArgs, opts?: pulumi.InvokeOptions): Promise<GetStreamResult>
```


Use this data source to get information about a Kinesis Stream for use in other
resources.

For more details, see the [Amazon Kinesis Documentation][1].

<h2 class="pdoc-module-header" id="FirehoseDeliveryStreamArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L157">interface FirehoseDeliveryStreamArgs</a>
</h2>

The set of arguments for constructing a FirehoseDeliveryStream resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L161">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the Stream

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L165">property destination</a>
</h3>

```typescript
destination: pulumi.Input<string>;
```


This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L166">property destinationId</a>
</h3>

```typescript
destinationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L167">property elasticsearchConfiguration</a>
</h3>

```typescript
elasticsearchConfiguration?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L171">property extendedS3Configuration</a>
</h3>

```typescript
extendedS3Configuration?: pulumi.Input<{ ... }>;
```


Enhanced configuration options for the s3 destination. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L175">property kinesisSourceConfiguration</a>
</h3>

```typescript
kinesisSourceConfiguration?: pulumi.Input<{ ... }>;
```


Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L180">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L186">property redshiftConfiguration</a>
</h3>

```typescript
redshiftConfiguration?: pulumi.Input<{ ... }>;
```


Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L191">property s3Configuration</a>
</h3>

```typescript
s3Configuration?: pulumi.Input<{ ... }>;
```


Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L192">property splunkConfiguration</a>
</h3>

```typescript
splunkConfiguration?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L196">property versionId</a>
</h3>

```typescript
versionId?: pulumi.Input<string>;
```


Specifies the table version for the output data schema. Defaults to `LATEST`.

<h2 class="pdoc-module-header" id="FirehoseDeliveryStreamState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L112">interface FirehoseDeliveryStreamState</a>
</h2>

Input properties used for looking up and filtering FirehoseDeliveryStream resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L116">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the Stream

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L120">property destination</a>
</h3>

```typescript
destination?: pulumi.Input<string>;
```


This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L121">property destinationId</a>
</h3>

```typescript
destinationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L122">property elasticsearchConfiguration</a>
</h3>

```typescript
elasticsearchConfiguration?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L126">property extendedS3Configuration</a>
</h3>

```typescript
extendedS3Configuration?: pulumi.Input<{ ... }>;
```


Enhanced configuration options for the s3 destination. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L130">property kinesisSourceConfiguration</a>
</h3>

```typescript
kinesisSourceConfiguration?: pulumi.Input<{ ... }>;
```


Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L141">property redshiftConfiguration</a>
</h3>

```typescript
redshiftConfiguration?: pulumi.Input<{ ... }>;
```


Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L146">property s3Configuration</a>
</h3>

```typescript
s3Configuration?: pulumi.Input<{ ... }>;
```


Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L147">property splunkConfiguration</a>
</h3>

```typescript
splunkConfiguration?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L151">property versionId</a>
</h3>

```typescript
versionId?: pulumi.Input<string>;
```


Specifies the table version for the output data schema. Defaults to `LATEST`.

<h2 class="pdoc-module-header" id="GetStreamArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L22">interface GetStreamArgs</a>
</h2>

A collection of arguments for invoking getStream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L26">property name</a>
</h3>

```typescript
name: string;
```


The name of the Kinesis Stream.

<h2 class="pdoc-module-header" id="GetStreamResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L32">interface GetStreamResult</a>
</h2>

A collection of values returned by getStream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L36">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name (ARN) of the Kinesis Stream (same as id).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L40">property closedShards</a>
</h3>

```typescript
closedShards: string[];
```


The list of shard ids in the CLOSED state. See [Shard State][2] for more.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L44">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp: number;
```


The approximate UNIX timestamp that the stream was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L68">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L48">property openShards</a>
</h3>

```typescript
openShards: string[];
```


The list of shard ids in the OPEN state. See [Shard State][2] for more.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L52">property retentionPeriod</a>
</h3>

```typescript
retentionPeriod: number;
```


Length of time (in hours) data records are accessible after they are added to the stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L56">property shardLevelMetrics</a>
</h3>

```typescript
shardLevelMetrics: string[];
```


A list of shard-level CloudWatch metrics which are enabled for the stream. See [Monitoring with CloudWatch][3] for more.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L60">property status</a>
</h3>

```typescript
status: string;
```


The current status of the stream. The stream status is one of CREATING, DELETING, ACTIVE, or UPDATING.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts#L64">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assigned to the stream.

<h2 class="pdoc-module-header" id="StreamArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L146">interface StreamArgs</a>
</h2>

The set of arguments for constructing a Stream resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L150">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the Stream (same as `id`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L154">property encryptionType</a>
</h3>

```typescript
encryptionType?: pulumi.Input<string>;
```


The encryption type to use. The only acceptable values are `NONE` or `KMS`. The default value is `NONE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L158">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias aws/kinesis.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L163">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L167">property retentionPeriod</a>
</h3>

```typescript
retentionPeriod?: pulumi.Input<number>;
```


Length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours. Minimum value is 24. Default is 24.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L173">property shardCount</a>
</h3>

```typescript
shardCount: pulumi.Input<number>;
```


The number of shards that the stream will use.
Amazon has guidlines for specifying the Stream size that should be referenced
when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L177">property shardLevelMetrics</a>
</h3>

```typescript
shardLevelMetrics?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L181">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="StreamState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L105">interface StreamState</a>
</h2>

Input properties used for looking up and filtering Stream resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L109">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the Stream (same as `id`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L113">property encryptionType</a>
</h3>

```typescript
encryptionType?: pulumi.Input<string>;
```


The encryption type to use. The only acceptable values are `NONE` or `KMS`. The default value is `NONE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L117">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias aws/kinesis.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L126">property retentionPeriod</a>
</h3>

```typescript
retentionPeriod?: pulumi.Input<number>;
```


Length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours. Minimum value is 24. Default is 24.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L132">property shardCount</a>
</h3>

```typescript
shardCount?: pulumi.Input<number>;
```


The number of shards that the stream will use.
Amazon has guidlines for specifying the Stream size that should be referenced
when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L136">property shardLevelMetrics</a>
</h3>

```typescript
shardLevelMetrics?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts#L140">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

