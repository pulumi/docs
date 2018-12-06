---
title: Module kinesis
---

<a href="../index.html">@pulumi/aws</a> &gt; kinesis

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AnalyticsApplication">class AnalyticsApplication</a>
* <a href="#FirehoseDeliveryStream">class FirehoseDeliveryStream</a>
* <a href="#Stream">class Stream</a>
* <a href="#StreamEventSubscription">class StreamEventSubscription</a>
* <a href="#getStream">function getStream</a>
* <a href="#AnalyticsApplicationArgs">interface AnalyticsApplicationArgs</a>
* <a href="#AnalyticsApplicationState">interface AnalyticsApplicationState</a>
* <a href="#FirehoseDeliveryStreamArgs">interface FirehoseDeliveryStreamArgs</a>
* <a href="#FirehoseDeliveryStreamState">interface FirehoseDeliveryStreamState</a>
* <a href="#GetStreamArgs">interface GetStreamArgs</a>
* <a href="#GetStreamResult">interface GetStreamResult</a>
* <a href="#StreamArgs">interface StreamArgs</a>
* <a href="#StreamEvent">interface StreamEvent</a>
* <a href="#StreamEventRecord">interface StreamEventRecord</a>
* <a href="#StreamEventSubscriptionArgs">interface StreamEventSubscriptionArgs</a>
* <a href="#StreamState">interface StreamState</a>
* <a href="#StreamEventHandler">type StreamEventHandler</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts">kinesis/analyticsApplication.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts">kinesis/firehoseDeliveryStream.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/getStream.ts">kinesis/getStream.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts">kinesis/kinesisMixins.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/stream.ts">kinesis/stream.ts</a> 


<h2 class="pdoc-module-header" id="AnalyticsApplication">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L15">class AnalyticsApplication</a>
</h2>

Provides a Kinesis Analytics Application resource. Kinesis Analytics is a managed service that
allows processing and analyzing streaming data using standard SQL.

For more details, see the [Amazon Kinesis Analytics Documentation][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L77">constructor</a>
</h3>

```typescript
new AnalyticsApplication(name: string, args?: AnalyticsApplicationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AnalyticsApplication resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AnalyticsApplicationState): AnalyticsApplication
```


Get an existing AnalyticsApplication resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L31">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<ARN>;
```


The ARN of the Kinesis Analytics Appliation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L36">property cloudwatchLoggingOptions</a>
</h3>

```typescript
public cloudwatchLoggingOptions: pulumi.Output<{ ... } | undefined>;
```


The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L40">property code</a>
</h3>

```typescript
public code: pulumi.Output<string | undefined>;
```


SQL Code to transform input data, and generate output.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L44">property createTimestamp</a>
</h3>

```typescript
public createTimestamp: pulumi.Output<string>;
```


The Timestamp when the application version was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L48">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L52">property inputs</a>
</h3>

```typescript
public inputs: pulumi.Output<{ ... } | undefined>;
```


Input configuration of the application. See Inputs below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L56">property lastUpdateTimestamp</a>
</h3>

```typescript
public lastUpdateTimestamp: pulumi.Output<string>;
```


The Timestamp when the application was last updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the Kinesis Analytics Application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L64">property outputs</a>
</h3>

```typescript
public outputs: pulumi.Output<{ ... }[] | undefined>;
```


Output destination configuration of the application. See Outputs below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L69">property referenceDataSources</a>
</h3>

```typescript
public referenceDataSources: pulumi.Output<{ ... } | undefined>;
```


An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L73">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The Status of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L77">property version</a>
</h3>

```typescript
public version: pulumi.Output<number>;
```


The Version of the application.

<h2 class="pdoc-module-header" id="FirehoseDeliveryStream">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L12">class FirehoseDeliveryStream</a>
</h2>

Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.

For more details, see the [Amazon Kinesis Firehose Documentation][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L67">constructor</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L63">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
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

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L67">property versionId</a>
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

<h2 class="pdoc-module-header" id="StreamEventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L66">class StreamEventSubscription</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L68">constructor</a>
</h3>

```typescript
new StreamEventSubscription(name: string, stream: stream.Stream, handler: StreamEventHandler, args: StreamEventSubscriptionArgs, opts?: pulumi.ComponentResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L68">property eventSourceMapping</a>
</h3>

```typescript
public eventSourceMapping: lambda.EventSourceMapping;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L227">property func</a>
</h3>

```typescript
public func: LambdaFunction;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L226">property permission</a>
</h3>

```typescript
public permission: permission.Permission;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L67">property stream</a>
</h3>

```typescript
public stream: pulumi.Output<stream.Stream>;
```

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

<h2 class="pdoc-module-header" id="AnalyticsApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L181">interface AnalyticsApplicationArgs</a>
</h2>

The set of arguments for constructing a AnalyticsApplication resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L186">property cloudwatchLoggingOptions</a>
</h3>

```typescript
cloudwatchLoggingOptions?: pulumi.Input<{ ... }>;
```


The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L190">property code</a>
</h3>

```typescript
code?: pulumi.Input<string>;
```


SQL Code to transform input data, and generate output.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L194">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L198">property inputs</a>
</h3>

```typescript
inputs?: pulumi.Input<{ ... }>;
```


Input configuration of the application. See Inputs below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L202">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the Kinesis Analytics Application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L206">property outputs</a>
</h3>

```typescript
outputs?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Output destination configuration of the application. See Outputs below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L211">property referenceDataSources</a>
</h3>

```typescript
referenceDataSources?: pulumi.Input<{ ... }>;
```


An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.

<h2 class="pdoc-module-header" id="AnalyticsApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L125">interface AnalyticsApplicationState</a>
</h2>

Input properties used for looking up and filtering AnalyticsApplication resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L129">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<ARN>;
```


The ARN of the Kinesis Analytics Appliation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L134">property cloudwatchLoggingOptions</a>
</h3>

```typescript
cloudwatchLoggingOptions?: pulumi.Input<{ ... }>;
```


The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L138">property code</a>
</h3>

```typescript
code?: pulumi.Input<string>;
```


SQL Code to transform input data, and generate output.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L142">property createTimestamp</a>
</h3>

```typescript
createTimestamp?: pulumi.Input<string>;
```


The Timestamp when the application version was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L146">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L150">property inputs</a>
</h3>

```typescript
inputs?: pulumi.Input<{ ... }>;
```


Input configuration of the application. See Inputs below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L154">property lastUpdateTimestamp</a>
</h3>

```typescript
lastUpdateTimestamp?: pulumi.Input<string>;
```


The Timestamp when the application was last updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L158">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the Kinesis Analytics Application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L162">property outputs</a>
</h3>

```typescript
outputs?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Output destination configuration of the application. See Outputs below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L167">property referenceDataSources</a>
</h3>

```typescript
referenceDataSources?: pulumi.Input<{ ... }>;
```


An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L171">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The Status of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/analyticsApplication.ts#L175">property version</a>
</h3>

```typescript
version?: pulumi.Input<number>;
```


The Version of the application.

<h2 class="pdoc-module-header" id="FirehoseDeliveryStreamArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L167">interface FirehoseDeliveryStreamArgs</a>
</h2>

The set of arguments for constructing a FirehoseDeliveryStream resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L171">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the Stream

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L175">property destination</a>
</h3>

```typescript
destination: pulumi.Input<string>;
```


This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L176">property destinationId</a>
</h3>

```typescript
destinationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L177">property elasticsearchConfiguration</a>
</h3>

```typescript
elasticsearchConfiguration?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L181">property extendedS3Configuration</a>
</h3>

```typescript
extendedS3Configuration?: pulumi.Input<{ ... }>;
```


Enhanced configuration options for the s3 destination. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L185">property kinesisSourceConfiguration</a>
</h3>

```typescript
kinesisSourceConfiguration?: pulumi.Input<{ ... }>;
```


Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L190">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L196">property redshiftConfiguration</a>
</h3>

```typescript
redshiftConfiguration?: pulumi.Input<{ ... }>;
```


Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L201">property s3Configuration</a>
</h3>

```typescript
s3Configuration?: pulumi.Input<{ ... }>;
```


Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L202">property splunkConfiguration</a>
</h3>

```typescript
splunkConfiguration?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L206">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L210">property versionId</a>
</h3>

```typescript
versionId?: pulumi.Input<string>;
```


Specifies the table version for the output data schema. Defaults to `LATEST`.

<h2 class="pdoc-module-header" id="FirehoseDeliveryStreamState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L118">interface FirehoseDeliveryStreamState</a>
</h2>

Input properties used for looking up and filtering FirehoseDeliveryStream resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L122">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the Stream

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L126">property destination</a>
</h3>

```typescript
destination?: pulumi.Input<string>;
```


This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L127">property destinationId</a>
</h3>

```typescript
destinationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L128">property elasticsearchConfiguration</a>
</h3>

```typescript
elasticsearchConfiguration?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L132">property extendedS3Configuration</a>
</h3>

```typescript
extendedS3Configuration?: pulumi.Input<{ ... }>;
```


Enhanced configuration options for the s3 destination. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L136">property kinesisSourceConfiguration</a>
</h3>

```typescript
kinesisSourceConfiguration?: pulumi.Input<{ ... }>;
```


Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L147">property redshiftConfiguration</a>
</h3>

```typescript
redshiftConfiguration?: pulumi.Input<{ ... }>;
```


Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L152">property s3Configuration</a>
</h3>

```typescript
s3Configuration?: pulumi.Input<{ ... }>;
```


Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L153">property splunkConfiguration</a>
</h3>

```typescript
splunkConfiguration?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L157">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/firehoseDeliveryStream.ts#L161">property versionId</a>
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

<h2 class="pdoc-module-header" id="StreamEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L44">interface StreamEvent</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L45">property Records</a>
</h3>

```typescript
Records: StreamEventRecord[];
```

<h2 class="pdoc-module-header" id="StreamEventRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L48">interface StreamEventRecord</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L61">property awsRegion</a>
</h3>

```typescript
awsRegion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L56">property eventID</a>
</h3>

```typescript
eventID: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L59">property eventName</a>
</h3>

```typescript
eventName: aws:kinesis:record;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L55">property eventSource</a>
</h3>

```typescript
eventSource: aws:kinesis;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L60">property eventSourceARN</a>
</h3>

```typescript
eventSourceARN: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L58">property eventVersion</a>
</h3>

```typescript
eventVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L57">property invokeIdentityArn</a>
</h3>

```typescript
invokeIdentityArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L49">property kinesis</a>
</h3>

```typescript
kinesis: { ... };
```

<h2 class="pdoc-module-header" id="StreamEventSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L20">interface StreamEventSubscriptionArgs</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L25">property batchSize</a>
</h3>

```typescript
batchSize?: number;
```


The largest number of records that Lambda will retrieve from your event source at the time of
invocation. Defaults to `100` for Kinesis.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L32">property startingPosition</a>
</h3>

```typescript
startingPosition: TRIM_HORIZON | LATEST | AT_TIMESTAMP;
```


The position in the stream where AWS Lambda should start reading. Must be one of either
`TRIM_HORIZON`, `LATEST` or `AT_TIMESTAMP`.  If `AT_TIMESTAMP` is provided,
[startingPositionTimestamp] must be provided as well.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L41">property startingPositionTimestamp</a>
</h3>

```typescript
startingPositionTimestamp?: string;
```


A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of the
data record which to start reading when using `starting_position` set to `AT_TIMESTAMP`.
If a record with this exact timestamp does not exist, the next later record is chosen.
If the timestamp is older than the current trim horizon, the oldest available record is
chosen.

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

<h2 class="pdoc-module-header" id="StreamEventHandler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts#L64">type StreamEventHandler</a>
</h2>

```typescript
type StreamEventHandler = lambda.EventHandler<StreamEvent, void>;
```

