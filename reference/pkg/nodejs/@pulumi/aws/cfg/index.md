---
title: Module cfg
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#DeliveryChannel">class DeliveryChannel</a>
* <a href="#Recorder">class Recorder</a>
* <a href="#RecorderStatus">class RecorderStatus</a>
* <a href="#Rule">class Rule</a>
* <a href="#DeliveryChannelArgs">interface DeliveryChannelArgs</a>
* <a href="#DeliveryChannelState">interface DeliveryChannelState</a>
* <a href="#RecorderArgs">interface RecorderArgs</a>
* <a href="#RecorderState">interface RecorderState</a>
* <a href="#RecorderStatusArgs">interface RecorderStatusArgs</a>
* <a href="#RecorderStatusState">interface RecorderStatusState</a>
* <a href="#RuleArgs">interface RuleArgs</a>
* <a href="#RuleState">interface RuleState</a>

<a href="/cfg/deliveryChannel.ts">cfg/deliveryChannel.ts</a> <a href="/cfg/recorder.ts">cfg/recorder.ts</a> <a href="/cfg/recorderStatus.ts">cfg/recorderStatus.ts</a> <a href="/cfg/rule.ts">cfg/rule.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="DeliveryChannel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L11">class DeliveryChannel</a>
</h2>

Provides an AWS Config Delivery Channel.

~> **Note:** Delivery Channel requires a [Configuration Recorder](/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L43">constructor</a>
</h3>

```typescript
new DeliveryChannel(name: string, args: DeliveryChannelArgs, opts?: pulumi.ResourceOptions)
```


Create a DeliveryChannel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new DeliveryChannel(name: string, state?: DeliveryChannelState, opts?: pulumi.ResourceOptions)
```


Create a DeliveryChannel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeliveryChannelState): DeliveryChannel
```


Get an existing DeliveryChannel resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L27">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L31">property s3BucketName</a>
</h3>

```typescript
public s3BucketName: pulumi.Output<string>;
```


The name of the S3 bucket used to store the configuration history.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L35">property s3KeyPrefix</a>
</h3>

```typescript
public s3KeyPrefix: pulumi.Output<string | undefined>;
```


The prefix for the specified S3 bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L39">property snapshotDeliveryProperties</a>
</h3>

```typescript
public snapshotDeliveryProperties: pulumi.Output<{ ... } | undefined>;
```


Options for how AWS Config delivers configuration snapshots. See below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L43">property snsTopicArn</a>
</h3>

```typescript
public snsTopicArn: pulumi.Output<string | undefined>;
```


The ARN of the SNS topic that AWS Config delivers notifications to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Recorder">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L11">class Recorder</a>
</h2>

Provides an AWS Config Configuration Recorder. Please note that this resource **does not start** the created recorder automatically.

~> **Note:** _Starting_ the Configuration Recorder requires a [delivery channel](/docs/providers/aws/r/config_delivery_channel.html) (while delivery channel creation requires Configuration Recorder). This is why [`aws_config_configuration_recorder_status`](/docs/providers/aws/r/config_configuration_recorder_status.html) is a separate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L37">constructor</a>
</h3>

```typescript
new Recorder(name: string, args: RecorderArgs, opts?: pulumi.ResourceOptions)
```


Create a Recorder resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Recorder(name: string, state?: RecorderState, opts?: pulumi.ResourceOptions)
```


Create a Recorder resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecorderState): Recorder
```


Get an existing Recorder resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L27">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the recorder. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L31">property recordingGroup</a>
</h3>

```typescript
public recordingGroup: pulumi.Output<{ ... }>;
```


Recording group - see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L37">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RecorderStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L11">class RecorderStatus</a>
</h2>

Manages status (recording / stopped) of an AWS Config Configuration Recorder.

~> **Note:** Starting Configuration Recorder requires a [Delivery Channel](/docs/providers/aws/r/config_delivery_channel.html) to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L31">constructor</a>
</h3>

```typescript
new RecorderStatus(name: string, args: RecorderStatusArgs, opts?: pulumi.ResourceOptions)
```


Create a RecorderStatus resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new RecorderStatus(name: string, state?: RecorderStatusState, opts?: pulumi.ResourceOptions)
```


Create a RecorderStatus resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecorderStatusState): RecorderStatus
```


Get an existing RecorderStatus resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L27">property isEnabled</a>
</h3>

```typescript
public isEnabled: pulumi.Output<boolean>;
```


Whether the configuration recorder should be enabled or disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the recorder

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Rule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L11">class Rule</a>
</h2>

Provides an AWS Config Rule.

~> **Note:** Config Rule requires an existing [Configuration Recorder](/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` is recommended (as shown below) to avoid race conditions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L57">constructor</a>
</h3>

```typescript
new Rule(name: string, args: RuleArgs, opts?: pulumi.ResourceOptions)
```


Create a Rule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Rule(name: string, state?: RuleState, opts?: pulumi.ResourceOptions)
```


Create a Rule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RuleState): Rule
```


Get an existing Rule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the config rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L35">property inputParameters</a>
</h3>

```typescript
public inputParameters: pulumi.Output<string | undefined>;
```


A string in JSON format that is passed to the AWS Config rule Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L40">property maximumExecutionFrequency</a>
</h3>

```typescript
public maximumExecutionFrequency: pulumi.Output<string | undefined>;
```


The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L48">property ruleId</a>
</h3>

```typescript
public ruleId: pulumi.Output<string>;
```


The ID of the config rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L52">property scope</a>
</h3>

```typescript
public scope: pulumi.Output<{ ... } | undefined>;
```


Scope defines which resources can trigger an evaluation for the rule as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L57">property source</a>
</h3>

```typescript
public source: pulumi.Output<{ ... }>;
```


Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DeliveryChannelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L108">interface DeliveryChannelArgs</a>
</h2>

The set of arguments for constructing a DeliveryChannel resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L116">property s3BucketName</a>
</h3>

```typescript
s3BucketName: pulumi.Input<string>;
```


The name of the S3 bucket used to store the configuration history.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L120">property s3KeyPrefix</a>
</h3>

```typescript
s3KeyPrefix?: pulumi.Input<string>;
```


The prefix for the specified S3 bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L124">property snapshotDeliveryProperties</a>
</h3>

```typescript
snapshotDeliveryProperties?: pulumi.Input<{ ... }>;
```


Options for how AWS Config delivers configuration snapshots. See below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L128">property snsTopicArn</a>
</h3>

```typescript
snsTopicArn?: pulumi.Input<string>;
```


The ARN of the SNS topic that AWS Config delivers notifications to.

<h2 class="pdoc-module-header" id="DeliveryChannelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L82">interface DeliveryChannelState</a>
</h2>

Input properties used for looking up and filtering DeliveryChannel resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L90">property s3BucketName</a>
</h3>

```typescript
s3BucketName?: pulumi.Input<string>;
```


The name of the S3 bucket used to store the configuration history.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L94">property s3KeyPrefix</a>
</h3>

```typescript
s3KeyPrefix?: pulumi.Input<string>;
```


The prefix for the specified S3 bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L98">property snapshotDeliveryProperties</a>
</h3>

```typescript
snapshotDeliveryProperties?: pulumi.Input<{ ... }>;
```


Options for how AWS Config delivers configuration snapshots. See below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/deliveryChannel.ts#L102">property snsTopicArn</a>
</h3>

```typescript
snsTopicArn?: pulumi.Input<string>;
```


The ARN of the SNS topic that AWS Config delivers notifications to.

<h2 class="pdoc-module-header" id="RecorderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L92">interface RecorderArgs</a>
</h2>

The set of arguments for constructing a Recorder resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the recorder. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L100">property recordingGroup</a>
</h3>

```typescript
recordingGroup?: pulumi.Input<{ ... }>;
```


Recording group - see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L106">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.

<h2 class="pdoc-module-header" id="RecorderState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L72">interface RecorderState</a>
</h2>

Input properties used for looking up and filtering Recorder resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the recorder. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L80">property recordingGroup</a>
</h3>

```typescript
recordingGroup?: pulumi.Input<{ ... }>;
```


Recording group - see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorder.ts#L86">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.

<h2 class="pdoc-module-header" id="RecorderStatusArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L78">interface RecorderStatusArgs</a>
</h2>

The set of arguments for constructing a RecorderStatus resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L82">property isEnabled</a>
</h3>

```typescript
isEnabled: pulumi.Input<boolean>;
```


Whether the configuration recorder should be enabled or disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the recorder

<h2 class="pdoc-module-header" id="RecorderStatusState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L64">interface RecorderStatusState</a>
</h2>

Input properties used for looking up and filtering RecorderStatus resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L68">property isEnabled</a>
</h3>

```typescript
isEnabled?: pulumi.Input<boolean>;
```


Whether the configuration recorder should be enabled or disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/recorderStatus.ts#L72">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the recorder

<h2 class="pdoc-module-header" id="RuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L142">interface RuleArgs</a>
</h2>

The set of arguments for constructing a Rule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L146">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L150">property inputParameters</a>
</h3>

```typescript
inputParameters?: pulumi.Input<string>;
```


A string in JSON format that is passed to the AWS Config rule Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L155">property maximumExecutionFrequency</a>
</h3>

```typescript
maximumExecutionFrequency?: pulumi.Input<string>;
```


The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L163">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<{ ... }>;
```


Scope defines which resources can trigger an evaluation for the rule as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L168">property source</a>
</h3>

```typescript
source: pulumi.Input<{ ... }>;
```


Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.

<h2 class="pdoc-module-header" id="RuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L102">interface RuleState</a>
</h2>

Input properties used for looking up and filtering Rule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L106">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the config rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L110">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L114">property inputParameters</a>
</h3>

```typescript
inputParameters?: pulumi.Input<string>;
```


A string in JSON format that is passed to the AWS Config rule Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L119">property maximumExecutionFrequency</a>
</h3>

```typescript
maximumExecutionFrequency?: pulumi.Input<string>;
```


The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L127">property ruleId</a>
</h3>

```typescript
ruleId?: pulumi.Input<string>;
```


The ID of the config rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L131">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<{ ... }>;
```


Scope defines which resources can trigger an evaluation for the rule as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cfg/rule.ts#L136">property source</a>
</h3>

```typescript
source?: pulumi.Input<{ ... }>;
```


Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.

