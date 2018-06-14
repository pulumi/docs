---
title: Module cfg
---

<a href="../index.html">@pulumi/aws</a> &gt; cfg

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AggregateAuthorization">class AggregateAuthorization</a>
* <a href="#ConfigurationAggregator">class ConfigurationAggregator</a>
* <a href="#DeliveryChannel">class DeliveryChannel</a>
* <a href="#Recorder">class Recorder</a>
* <a href="#RecorderStatus">class RecorderStatus</a>
* <a href="#Rule">class Rule</a>
* <a href="#AggregateAuthorizationArgs">interface AggregateAuthorizationArgs</a>
* <a href="#AggregateAuthorizationState">interface AggregateAuthorizationState</a>
* <a href="#ConfigurationAggregatorArgs">interface ConfigurationAggregatorArgs</a>
* <a href="#ConfigurationAggregatorState">interface ConfigurationAggregatorState</a>
* <a href="#DeliveryChannelArgs">interface DeliveryChannelArgs</a>
* <a href="#DeliveryChannelState">interface DeliveryChannelState</a>
* <a href="#RecorderArgs">interface RecorderArgs</a>
* <a href="#RecorderState">interface RecorderState</a>
* <a href="#RecorderStatusArgs">interface RecorderStatusArgs</a>
* <a href="#RecorderStatusState">interface RecorderStatusState</a>
* <a href="#RuleArgs">interface RuleArgs</a>
* <a href="#RuleState">interface RuleState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts">cfg/aggregateAuthorization.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts">cfg/configurationAggregator.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts">cfg/deliveryChannel.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts">cfg/recorder.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts">cfg/recorderStatus.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts">cfg/rule.ts</a> 


<h2 class="pdoc-module-header" id="AggregateAuthorization">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L9">class AggregateAuthorization</a>
</h2>

Manages an AWS Config Aggregate Authorization

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L33">constructor</a>
</h3>

```typescript
new AggregateAuthorization(name: string, args: AggregateAuthorizationArgs, opts?: pulumi.ResourceOptions)
```


Create a AggregateAuthorization resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AggregateAuthorizationState): AggregateAuthorization
```


Get an existing AggregateAuthorization resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L25">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


Account ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the authorization

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L33">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


Region

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ConfigurationAggregator">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L9">class ConfigurationAggregator</a>
</h2>

Manages an AWS Config Configuration Aggregator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L37">constructor</a>
</h3>

```typescript
new ConfigurationAggregator(name: string, args?: ConfigurationAggregatorArgs, opts?: pulumi.ResourceOptions)
```


Create a ConfigurationAggregator resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationAggregatorState): ConfigurationAggregator
```


Get an existing ConfigurationAggregator resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L25">property accountAggregationSource</a>
</h3>

```typescript
public accountAggregationSource: pulumi.Output<{ ... } | undefined>;
```


The account(s) to aggregate config data from as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the aggregator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the configuration aggregator.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L37">property organizationAggregationSource</a>
</h3>

```typescript
public organizationAggregationSource: pulumi.Output<{ ... } | undefined>;
```


The organization to aggregate config data from as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DeliveryChannel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L11">class DeliveryChannel</a>
</h2>

Provides an AWS Config Delivery Channel.

~> **Note:** Delivery Channel requires a [Configuration Recorder](/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L43">constructor</a>
</h3>

```typescript
new DeliveryChannel(name: string, args: DeliveryChannelArgs, opts?: pulumi.ResourceOptions)
```


Create a DeliveryChannel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeliveryChannelState): DeliveryChannel
```


Get an existing DeliveryChannel resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L27">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L31">property s3BucketName</a>
</h3>

```typescript
public s3BucketName: pulumi.Output<string>;
```


The name of the S3 bucket used to store the configuration history.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L35">property s3KeyPrefix</a>
</h3>

```typescript
public s3KeyPrefix: pulumi.Output<string | undefined>;
```


The prefix for the specified S3 bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L39">property snapshotDeliveryProperties</a>
</h3>

```typescript
public snapshotDeliveryProperties: pulumi.Output<{ ... } | undefined>;
```


Options for how AWS Config delivers configuration snapshots. See below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L43">property snsTopicArn</a>
</h3>

```typescript
public snsTopicArn: pulumi.Output<string | undefined>;
```


The ARN of the SNS topic that AWS Config delivers notifications to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Recorder">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L11">class Recorder</a>
</h2>

Provides an AWS Config Configuration Recorder. Please note that this resource **does not start** the created recorder automatically.

~> **Note:** _Starting_ the Configuration Recorder requires a [delivery channel](/docs/providers/aws/r/config_delivery_channel.html) (while delivery channel creation requires Configuration Recorder). This is why [`aws_config_configuration_recorder_status`](/docs/providers/aws/r/config_configuration_recorder_status.html) is a separate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L37">constructor</a>
</h3>

```typescript
new Recorder(name: string, args: RecorderArgs, opts?: pulumi.ResourceOptions)
```


Create a Recorder resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecorderState): Recorder
```


Get an existing Recorder resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L27">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the recorder. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L31">property recordingGroup</a>
</h3>

```typescript
public recordingGroup: pulumi.Output<{ ... }>;
```


Recording group - see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L37">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RecorderStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L11">class RecorderStatus</a>
</h2>

Manages status (recording / stopped) of an AWS Config Configuration Recorder.

~> **Note:** Starting Configuration Recorder requires a [Delivery Channel](/docs/providers/aws/r/config_delivery_channel.html) to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L31">constructor</a>
</h3>

```typescript
new RecorderStatus(name: string, args: RecorderStatusArgs, opts?: pulumi.ResourceOptions)
```


Create a RecorderStatus resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecorderStatusState): RecorderStatus
```


Get an existing RecorderStatus resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L27">property isEnabled</a>
</h3>

```typescript
public isEnabled: pulumi.Output<boolean>;
```


Whether the configuration recorder should be enabled or disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the recorder

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Rule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L11">class Rule</a>
</h2>

Provides an AWS Config Rule.

~> **Note:** Config Rule requires an existing [Configuration Recorder](/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` is recommended (as shown below) to avoid race conditions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L57">constructor</a>
</h3>

```typescript
new Rule(name: string, args: RuleArgs, opts?: pulumi.ResourceOptions)
```


Create a Rule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RuleState): Rule
```


Get an existing Rule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the config rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L35">property inputParameters</a>
</h3>

```typescript
public inputParameters: pulumi.Output<string | undefined>;
```


A string in JSON format that is passed to the AWS Config rule Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L40">property maximumExecutionFrequency</a>
</h3>

```typescript
public maximumExecutionFrequency: pulumi.Output<string | undefined>;
```


The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L48">property ruleId</a>
</h3>

```typescript
public ruleId: pulumi.Output<string>;
```


The ID of the config rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L52">property scope</a>
</h3>

```typescript
public scope: pulumi.Output<{ ... } | undefined>;
```


Scope defines which resources can trigger an evaluation for the rule as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L57">property source</a>
</h3>

```typescript
public source: pulumi.Output<{ ... }>;
```


Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AggregateAuthorizationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L87">interface AggregateAuthorizationArgs</a>
</h2>

The set of arguments for constructing a AggregateAuthorization resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L91">property accountId</a>
</h3>

```typescript
accountId: pulumi.Input<string>;
```


Account ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L95">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


Region

<h2 class="pdoc-module-header" id="AggregateAuthorizationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L69">interface AggregateAuthorizationState</a>
</h2>

Input properties used for looking up and filtering AggregateAuthorization resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L73">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


Account ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L77">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the authorization

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/aggregateAuthorization.ts#L81">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Region

<h2 class="pdoc-module-header" id="ConfigurationAggregatorArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L91">interface ConfigurationAggregatorArgs</a>
</h2>

The set of arguments for constructing a ConfigurationAggregator resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L95">property accountAggregationSource</a>
</h3>

```typescript
accountAggregationSource?: pulumi.Input<{ ... }>;
```


The account(s) to aggregate config data from as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the configuration aggregator.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L103">property organizationAggregationSource</a>
</h3>

```typescript
organizationAggregationSource?: pulumi.Input<{ ... }>;
```


The organization to aggregate config data from as documented below.

<h2 class="pdoc-module-header" id="ConfigurationAggregatorState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L69">interface ConfigurationAggregatorState</a>
</h2>

Input properties used for looking up and filtering ConfigurationAggregator resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L73">property accountAggregationSource</a>
</h3>

```typescript
accountAggregationSource?: pulumi.Input<{ ... }>;
```


The account(s) to aggregate config data from as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L77">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the aggregator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the configuration aggregator.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/configurationAggregator.ts#L85">property organizationAggregationSource</a>
</h3>

```typescript
organizationAggregationSource?: pulumi.Input<{ ... }>;
```


The organization to aggregate config data from as documented below.

<h2 class="pdoc-module-header" id="DeliveryChannelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L106">interface DeliveryChannelArgs</a>
</h2>

The set of arguments for constructing a DeliveryChannel resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L114">property s3BucketName</a>
</h3>

```typescript
s3BucketName: pulumi.Input<string>;
```


The name of the S3 bucket used to store the configuration history.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L118">property s3KeyPrefix</a>
</h3>

```typescript
s3KeyPrefix?: pulumi.Input<string>;
```


The prefix for the specified S3 bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L122">property snapshotDeliveryProperties</a>
</h3>

```typescript
snapshotDeliveryProperties?: pulumi.Input<{ ... }>;
```


Options for how AWS Config delivers configuration snapshots. See below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L126">property snsTopicArn</a>
</h3>

```typescript
snsTopicArn?: pulumi.Input<string>;
```


The ARN of the SNS topic that AWS Config delivers notifications to.

<h2 class="pdoc-module-header" id="DeliveryChannelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L80">interface DeliveryChannelState</a>
</h2>

Input properties used for looking up and filtering DeliveryChannel resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L88">property s3BucketName</a>
</h3>

```typescript
s3BucketName?: pulumi.Input<string>;
```


The name of the S3 bucket used to store the configuration history.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L92">property s3KeyPrefix</a>
</h3>

```typescript
s3KeyPrefix?: pulumi.Input<string>;
```


The prefix for the specified S3 bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L96">property snapshotDeliveryProperties</a>
</h3>

```typescript
snapshotDeliveryProperties?: pulumi.Input<{ ... }>;
```


Options for how AWS Config delivers configuration snapshots. See below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/deliveryChannel.ts#L100">property snsTopicArn</a>
</h3>

```typescript
snsTopicArn?: pulumi.Input<string>;
```


The ARN of the SNS topic that AWS Config delivers notifications to.

<h2 class="pdoc-module-header" id="RecorderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L90">interface RecorderArgs</a>
</h2>

The set of arguments for constructing a Recorder resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the recorder. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L98">property recordingGroup</a>
</h3>

```typescript
recordingGroup?: pulumi.Input<{ ... }>;
```


Recording group - see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L104">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.

<h2 class="pdoc-module-header" id="RecorderState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L70">interface RecorderState</a>
</h2>

Input properties used for looking up and filtering Recorder resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L74">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the recorder. Defaults to `default`. Changing it recreates the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L78">property recordingGroup</a>
</h3>

```typescript
recordingGroup?: pulumi.Input<{ ... }>;
```


Recording group - see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorder.ts#L84">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.

<h2 class="pdoc-module-header" id="RecorderStatusArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L76">interface RecorderStatusArgs</a>
</h2>

The set of arguments for constructing a RecorderStatus resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L80">property isEnabled</a>
</h3>

```typescript
isEnabled: pulumi.Input<boolean>;
```


Whether the configuration recorder should be enabled or disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the recorder

<h2 class="pdoc-module-header" id="RecorderStatusState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L62">interface RecorderStatusState</a>
</h2>

Input properties used for looking up and filtering RecorderStatus resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L66">property isEnabled</a>
</h3>

```typescript
isEnabled?: pulumi.Input<boolean>;
```


Whether the configuration recorder should be enabled or disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/recorderStatus.ts#L70">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the recorder

<h2 class="pdoc-module-header" id="RuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L140">interface RuleArgs</a>
</h2>

The set of arguments for constructing a Rule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L144">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L148">property inputParameters</a>
</h3>

```typescript
inputParameters?: pulumi.Input<string>;
```


A string in JSON format that is passed to the AWS Config rule Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L153">property maximumExecutionFrequency</a>
</h3>

```typescript
maximumExecutionFrequency?: pulumi.Input<string>;
```


The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L157">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L161">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<{ ... }>;
```


Scope defines which resources can trigger an evaluation for the rule as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L166">property source</a>
</h3>

```typescript
source: pulumi.Input<{ ... }>;
```


Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.

<h2 class="pdoc-module-header" id="RuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L100">interface RuleState</a>
</h2>

Input properties used for looking up and filtering Rule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L104">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the config rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L108">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L112">property inputParameters</a>
</h3>

```typescript
inputParameters?: pulumi.Input<string>;
```


A string in JSON format that is passed to the AWS Config rule Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L117">property maximumExecutionFrequency</a>
</h3>

```typescript
maximumExecutionFrequency?: pulumi.Input<string>;
```


The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L125">property ruleId</a>
</h3>

```typescript
ruleId?: pulumi.Input<string>;
```


The ID of the config rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L129">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<{ ... }>;
```


Scope defines which resources can trigger an evaluation for the rule as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cfg/rule.ts#L134">property source</a>
</h3>

```typescript
source?: pulumi.Input<{ ... }>;
```


Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.

