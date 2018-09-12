---
title: Module sqs
---

<a href="../index.html">@pulumi/aws</a> &gt; sqs

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Queue">class Queue</a>
* <a href="#QueuePolicy">class QueuePolicy</a>
* <a href="#getQueue">function getQueue</a>
* <a href="#GetQueueArgs">interface GetQueueArgs</a>
* <a href="#GetQueueResult">interface GetQueueResult</a>
* <a href="#QueueArgs">interface QueueArgs</a>
* <a href="#QueuePolicyArgs">interface QueuePolicyArgs</a>
* <a href="#QueuePolicyState">interface QueuePolicyState</a>
* <a href="#QueueState">interface QueueState</a>
* <a href="#RedrivePolicy">interface RedrivePolicy</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/getQueue.ts">sqs/getQueue.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts">sqs/queue.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts">sqs/queuePolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/redrive.ts">sqs/redrive.ts</a> 


<h2 class="pdoc-module-header" id="Queue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L9">class Queue</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L81">constructor</a>
</h3>

```typescript
new Queue(name: string, args?: QueueArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Queue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueueState): Queue
```


Get an existing Queue resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L29">property contentBasedDeduplication</a>
</h3>

```typescript
public contentBasedDeduplication: pulumi.Output<boolean | undefined>;
```


Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L33">property delaySeconds</a>
</h3>

```typescript
public delaySeconds: pulumi.Output<number | undefined>;
```


The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L37">property fifoQueue</a>
</h3>

```typescript
public fifoQueue: pulumi.Output<boolean | undefined>;
```


Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L41">property kmsDataKeyReusePeriodSeconds</a>
</h3>

```typescript
public kmsDataKeyReusePeriodSeconds: pulumi.Output<number>;
```


The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L45">property kmsMasterKeyId</a>
</h3>

```typescript
public kmsMasterKeyId: pulumi.Output<string | undefined>;
```


The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L49">property maxMessageSize</a>
</h3>

```typescript
public maxMessageSize: pulumi.Output<number | undefined>;
```


The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L53">property messageRetentionSeconds</a>
</h3>

```typescript
public messageRetentionSeconds: pulumi.Output<number | undefined>;
```


The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L57">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


This is the human-readable name of the queue. If omitted, Terraform will assign a random name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L61">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L65">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L69">property receiveWaitTimeSeconds</a>
</h3>

```typescript
public receiveWaitTimeSeconds: pulumi.Output<number | undefined>;
```


The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L73">property redrivePolicy</a>
</h3>

```typescript
public redrivePolicy: pulumi.Output<string | undefined>;
```


The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L77">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L81">property visibilityTimeoutSeconds</a>
</h3>

```typescript
public visibilityTimeoutSeconds: pulumi.Output<number | undefined>;
```


The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).

<h2 class="pdoc-module-header" id="QueuePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L11">class QueuePolicy</a>
</h2>

Allows you to set a policy of an SQS Queue
while referencing ARN of the queue within the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L31">constructor</a>
</h3>

```typescript
new QueuePolicy(name: string, args: QueuePolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a QueuePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueuePolicyState): QueuePolicy
```


Get an existing QueuePolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L27">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L31">property queueUrl</a>
</h3>

```typescript
public queueUrl: pulumi.Output<string>;
```


The URL of the SQS Queue to which to attach the policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getQueue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/getQueue.ts#L12">function getQueue</a>
</h2>

```typescript
getQueue(args: GetQueueArgs, opts?: pulumi.InvokeOptions): Promise<GetQueueResult>
```


Use this data source to get the ARN and URL of queue in AWS Simple Queue Service (SQS).
By using this data source, you can reference SQS queues without having to hardcode
the ARNs as input.

<h2 class="pdoc-module-header" id="GetQueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/getQueue.ts#L21">interface GetQueueArgs</a>
</h2>

A collection of arguments for invoking getQueue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/getQueue.ts#L25">property name</a>
</h3>

```typescript
name: string;
```


The name of the queue to match.

<h2 class="pdoc-module-header" id="GetQueueResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/getQueue.ts#L31">interface GetQueueResult</a>
</h2>

A collection of values returned by getQueue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/getQueue.ts#L35">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name (ARN) of the queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/getQueue.ts#L43">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/getQueue.ts#L39">property url</a>
</h3>

```typescript
url: string;
```


The URL of the queue.

<h2 class="pdoc-module-header" id="QueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L201">interface QueueArgs</a>
</h2>

The set of arguments for constructing a Queue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L205">property contentBasedDeduplication</a>
</h3>

```typescript
contentBasedDeduplication?: pulumi.Input<boolean>;
```


Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L209">property delaySeconds</a>
</h3>

```typescript
delaySeconds?: pulumi.Input<number>;
```


The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L213">property fifoQueue</a>
</h3>

```typescript
fifoQueue?: pulumi.Input<boolean>;
```


Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L217">property kmsDataKeyReusePeriodSeconds</a>
</h3>

```typescript
kmsDataKeyReusePeriodSeconds?: pulumi.Input<number>;
```


The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L221">property kmsMasterKeyId</a>
</h3>

```typescript
kmsMasterKeyId?: pulumi.Input<string>;
```


The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L225">property maxMessageSize</a>
</h3>

```typescript
maxMessageSize?: pulumi.Input<number>;
```


The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L229">property messageRetentionSeconds</a>
</h3>

```typescript
messageRetentionSeconds?: pulumi.Input<number>;
```


The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L233">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


This is the human-readable name of the queue. If omitted, Terraform will assign a random name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L237">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L241">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L245">property receiveWaitTimeSeconds</a>
</h3>

```typescript
receiveWaitTimeSeconds?: pulumi.Input<number>;
```


The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L249">property redrivePolicy</a>
</h3>

```typescript
redrivePolicy?: pulumi.Input<string>;
```


The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L253">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L257">property visibilityTimeoutSeconds</a>
</h3>

```typescript
visibilityTimeoutSeconds?: pulumi.Input<number>;
```


The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).

<h2 class="pdoc-module-header" id="QueuePolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L79">interface QueuePolicyArgs</a>
</h2>

The set of arguments for constructing a QueuePolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L83">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L87">property queueUrl</a>
</h3>

```typescript
queueUrl: pulumi.Input<string>;
```


The URL of the SQS Queue to which to attach the policy

<h2 class="pdoc-module-header" id="QueuePolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L65">interface QueuePolicyState</a>
</h2>

Input properties used for looking up and filtering QueuePolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L69">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queuePolicy.ts#L73">property queueUrl</a>
</h3>

```typescript
queueUrl?: pulumi.Input<string>;
```


The URL of the SQS Queue to which to attach the policy

<h2 class="pdoc-module-header" id="QueueState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L135">interface QueueState</a>
</h2>

Input properties used for looking up and filtering Queue resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L139">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L143">property contentBasedDeduplication</a>
</h3>

```typescript
contentBasedDeduplication?: pulumi.Input<boolean>;
```


Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L147">property delaySeconds</a>
</h3>

```typescript
delaySeconds?: pulumi.Input<number>;
```


The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L151">property fifoQueue</a>
</h3>

```typescript
fifoQueue?: pulumi.Input<boolean>;
```


Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L155">property kmsDataKeyReusePeriodSeconds</a>
</h3>

```typescript
kmsDataKeyReusePeriodSeconds?: pulumi.Input<number>;
```


The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L159">property kmsMasterKeyId</a>
</h3>

```typescript
kmsMasterKeyId?: pulumi.Input<string>;
```


The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L163">property maxMessageSize</a>
</h3>

```typescript
maxMessageSize?: pulumi.Input<number>;
```


The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L167">property messageRetentionSeconds</a>
</h3>

```typescript
messageRetentionSeconds?: pulumi.Input<number>;
```


The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


This is the human-readable name of the queue. If omitted, Terraform will assign a random name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L175">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L179">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L183">property receiveWaitTimeSeconds</a>
</h3>

```typescript
receiveWaitTimeSeconds?: pulumi.Input<number>;
```


The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L187">property redrivePolicy</a>
</h3>

```typescript
redrivePolicy?: pulumi.Input<string>;
```


The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L191">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/queue.ts#L195">property visibilityTimeoutSeconds</a>
</h3>

```typescript
visibilityTimeoutSeconds?: pulumi.Input<number>;
```


The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).

<h2 class="pdoc-module-header" id="RedrivePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/redrive.ts#L26">interface RedrivePolicy</a>
</h2>

The string that includes the parameters for the dead-letter queue functionality of the source queue. For more
information about the redrive policy and dead-letter queues, see Using Amazon SQS Dead-Letter Queues in the Amazon
Simple Queue Service Developer Guide:
http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/redrive.ts#L31">property deadLetterTargetArn</a>
</h3>

```typescript
deadLetterTargetArn: ARN;
```


The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of
`maxReceiveCount` is exceeded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/redrive.ts#L38">property maxReceiveCount</a>
</h3>

```typescript
maxReceiveCount: number;
```


The number of times a message is delivered to the source queue before being moved to the dead-letter queue.

Note: The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a
standard queue must also be a standard queue.

