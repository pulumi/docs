---
title: Module sqs
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Queue">class Queue</a>
* <a href="#QueuePolicy">class QueuePolicy</a>
* <a href="#QueueArgs">interface QueueArgs</a>
* <a href="#QueuePolicyArgs">interface QueuePolicyArgs</a>
* <a href="#QueuePolicyState">interface QueuePolicyState</a>
* <a href="#QueueState">interface QueueState</a>
* <a href="#RedrivePolicy">interface RedrivePolicy</a>

<a href="/sqs/queue.ts">sqs/queue.ts</a> <a href="/sqs/queuePolicy.ts">sqs/queuePolicy.ts</a> <a href="/sqs/redrive.ts">sqs/redrive.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Queue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L6">class Queue</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L78">constructor</a>
</h3>

```typescript
new Queue(name: string, args?: QueueArgs, opts?: pulumi.ResourceOptions)
```


Create a Queue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Queue(name: string, state?: QueueState, opts?: pulumi.ResourceOptions)
```


Create a Queue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueueState): Queue
```


Get an existing Queue resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L22">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L26">property contentBasedDeduplication</a>
</h3>

```typescript
public contentBasedDeduplication: pulumi.Output<boolean | undefined>;
```


Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L30">property delaySeconds</a>
</h3>

```typescript
public delaySeconds: pulumi.Output<number | undefined>;
```


The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L34">property fifoQueue</a>
</h3>

```typescript
public fifoQueue: pulumi.Output<boolean | undefined>;
```


Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L38">property kmsDataKeyReusePeriodSeconds</a>
</h3>

```typescript
public kmsDataKeyReusePeriodSeconds: pulumi.Output<number>;
```


The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L42">property kmsMasterKeyId</a>
</h3>

```typescript
public kmsMasterKeyId: pulumi.Output<string | undefined>;
```


The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L46">property maxMessageSize</a>
</h3>

```typescript
public maxMessageSize: pulumi.Output<number | undefined>;
```


The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L50">property messageRetentionSeconds</a>
</h3>

```typescript
public messageRetentionSeconds: pulumi.Output<number | undefined>;
```


The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


This is the human-readable name of the queue. If omitted, Terraform will assign a random name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L58">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L62">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L66">property receiveWaitTimeSeconds</a>
</h3>

```typescript
public receiveWaitTimeSeconds: pulumi.Output<number | undefined>;
```


The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L70">property redrivePolicy</a>
</h3>

```typescript
public redrivePolicy: pulumi.Output<string | undefined>;
```


The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L74">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L78">property visibilityTimeoutSeconds</a>
</h3>

```typescript
public visibilityTimeoutSeconds: pulumi.Output<number | undefined>;
```


The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).

<h2 class="pdoc-module-header" id="QueuePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L10">class QueuePolicy</a>
</h2>

Allows you to set a policy of an SQS Queue
while referencing ARN of the queue within the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L30">constructor</a>
</h3>

```typescript
new QueuePolicy(name: string, args: QueuePolicyArgs, opts?: pulumi.ResourceOptions)
```


Create a QueuePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new QueuePolicy(name: string, state?: QueuePolicyState, opts?: pulumi.ResourceOptions)
```


Create a QueuePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueuePolicyState): QueuePolicy
```


Get an existing QueuePolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L26">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L30">property queueUrl</a>
</h3>

```typescript
public queueUrl: pulumi.Output<string>;
```


The URL of the SQS Queue to which to attach the policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="QueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L200">interface QueueArgs</a>
</h2>

The set of arguments for constructing a Queue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L204">property contentBasedDeduplication</a>
</h3>

```typescript
contentBasedDeduplication?: pulumi.Input<boolean>;
```


Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L208">property delaySeconds</a>
</h3>

```typescript
delaySeconds?: pulumi.Input<number>;
```


The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L212">property fifoQueue</a>
</h3>

```typescript
fifoQueue?: pulumi.Input<boolean>;
```


Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L216">property kmsDataKeyReusePeriodSeconds</a>
</h3>

```typescript
kmsDataKeyReusePeriodSeconds?: pulumi.Input<number>;
```


The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L220">property kmsMasterKeyId</a>
</h3>

```typescript
kmsMasterKeyId?: pulumi.Input<string>;
```


The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L224">property maxMessageSize</a>
</h3>

```typescript
maxMessageSize?: pulumi.Input<number>;
```


The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L228">property messageRetentionSeconds</a>
</h3>

```typescript
messageRetentionSeconds?: pulumi.Input<number>;
```


The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L232">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


This is the human-readable name of the queue. If omitted, Terraform will assign a random name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L236">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L240">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L244">property receiveWaitTimeSeconds</a>
</h3>

```typescript
receiveWaitTimeSeconds?: pulumi.Input<number>;
```


The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L248">property redrivePolicy</a>
</h3>

```typescript
redrivePolicy?: pulumi.Input<string>;
```


The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L252">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L256">property visibilityTimeoutSeconds</a>
</h3>

```typescript
visibilityTimeoutSeconds?: pulumi.Input<number>;
```


The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).

<h2 class="pdoc-module-header" id="QueuePolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L80">interface QueuePolicyArgs</a>
</h2>

The set of arguments for constructing a QueuePolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L84">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L88">property queueUrl</a>
</h3>

```typescript
queueUrl: pulumi.Input<string>;
```


The URL of the SQS Queue to which to attach the policy

<h2 class="pdoc-module-header" id="QueuePolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L66">interface QueuePolicyState</a>
</h2>

Input properties used for looking up and filtering QueuePolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L70">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queuePolicy.ts#L74">property queueUrl</a>
</h3>

```typescript
queueUrl?: pulumi.Input<string>;
```


The URL of the SQS Queue to which to attach the policy

<h2 class="pdoc-module-header" id="QueueState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L134">interface QueueState</a>
</h2>

Input properties used for looking up and filtering Queue resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L138">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L142">property contentBasedDeduplication</a>
</h3>

```typescript
contentBasedDeduplication?: pulumi.Input<boolean>;
```


Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L146">property delaySeconds</a>
</h3>

```typescript
delaySeconds?: pulumi.Input<number>;
```


The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L150">property fifoQueue</a>
</h3>

```typescript
fifoQueue?: pulumi.Input<boolean>;
```


Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L154">property kmsDataKeyReusePeriodSeconds</a>
</h3>

```typescript
kmsDataKeyReusePeriodSeconds?: pulumi.Input<number>;
```


The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L158">property kmsMasterKeyId</a>
</h3>

```typescript
kmsMasterKeyId?: pulumi.Input<string>;
```


The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L162">property maxMessageSize</a>
</h3>

```typescript
maxMessageSize?: pulumi.Input<number>;
```


The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L166">property messageRetentionSeconds</a>
</h3>

```typescript
messageRetentionSeconds?: pulumi.Input<number>;
```


The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L170">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


This is the human-readable name of the queue. If omitted, Terraform will assign a random name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L174">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L178">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The JSON policy for the SQS queue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L182">property receiveWaitTimeSeconds</a>
</h3>

```typescript
receiveWaitTimeSeconds?: pulumi.Input<number>;
```


The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L186">property redrivePolicy</a>
</h3>

```typescript
redrivePolicy?: pulumi.Input<string>;
```


The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L190">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/queue.ts#L194">property visibilityTimeoutSeconds</a>
</h3>

```typescript
visibilityTimeoutSeconds?: pulumi.Input<number>;
```


The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).

<h2 class="pdoc-module-header" id="RedrivePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/redrive.ts#L26">interface RedrivePolicy</a>
</h2>

The string that includes the parameters for the dead-letter queue functionality of the source queue. For more
information about the redrive policy and dead-letter queues, see Using Amazon SQS Dead-Letter Queues in the Amazon
Simple Queue Service Developer Guide:
http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/redrive.ts#L31">property deadLetterTargetArn</a>
</h3>

```typescript
deadLetterTargetArn: ARN;
```


The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of
`maxReceiveCount` is exceeded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sqs/redrive.ts#L38">property maxReceiveCount</a>
</h3>

```typescript
maxReceiveCount: number;
```


The number of times a message is delivered to the source queue before being moved to the dead-letter queue.

Note: The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a
standard queue must also be a standard queue.

