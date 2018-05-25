---
title: Module appautoscaling
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Policy">class Policy</a>
* <a href="#ScheduledAction">class ScheduledAction</a>
* <a href="#Target">class Target</a>
* <a href="#PolicyArgs">interface PolicyArgs</a>
* <a href="#PolicyState">interface PolicyState</a>
* <a href="#ScheduledActionArgs">interface ScheduledActionArgs</a>
* <a href="#ScheduledActionState">interface ScheduledActionState</a>
* <a href="#TargetArgs">interface TargetArgs</a>
* <a href="#TargetState">interface TargetState</a>

<a href="/appautoscaling/policy.ts">appautoscaling/policy.ts</a> <a href="/appautoscaling/scheduledAction.ts">appautoscaling/scheduledAction.ts</a> <a href="/appautoscaling/target.ts">appautoscaling/target.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L9">class Policy</a>
</h2>

Provides an Application AutoScaling Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L62">constructor</a>
</h3>

```typescript
new Policy(name: string, args: PolicyArgs, opts?: pulumi.ResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Policy(name: string, state?: PolicyState, opts?: pulumi.ResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState): Policy
```


Get an existing Policy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L25">property adjustmentType</a>
</h3>

```typescript
public adjustmentType: pulumi.Output<string | undefined>;
```


The scaling policy's adjustment type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L26">property alarms</a>
</h3>

```typescript
public alarms: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS to the scaling policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L31">property cooldown</a>
</h3>

```typescript
public cooldown: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L32">property metricAggregationType</a>
</h3>

```typescript
public metricAggregationType: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L33">property minAdjustmentMagnitude</a>
</h3>

```typescript
public minAdjustmentMagnitude: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L41">property policyType</a>
</h3>

```typescript
public policyType: pulumi.Output<string | undefined>;
```


For DynamoDB, only `TargetTrackingScaling` is supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L45">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L49">property scalableDimension</a>
</h3>

```typescript
public scalableDimension: pulumi.Output<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L53">property serviceNamespace</a>
</h3>

```typescript
public serviceNamespace: pulumi.Output<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L54">property stepAdjustments</a>
</h3>

```typescript
public stepAdjustments: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L58">property stepScalingPolicyConfigurations</a>
</h3>

```typescript
public stepScalingPolicyConfigurations: pulumi.Output<{ ... }[] | undefined>;
```


Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L62">property targetTrackingScalingPolicyConfiguration</a>
</h3>

```typescript
public targetTrackingScalingPolicyConfiguration: pulumi.Output<{ ... } | undefined>;
```


A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ScheduledAction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L9">class ScheduledAction</a>
</h2>

Provides an Application AutoScaling ScheduledAction resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L57">constructor</a>
</h3>

```typescript
new ScheduledAction(name: string, args: ScheduledActionArgs, opts?: pulumi.ResourceOptions)
```


Create a ScheduledAction resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ScheduledAction(name: string, state?: ScheduledActionState, opts?: pulumi.ResourceOptions)
```


Create a ScheduledAction resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ScheduledActionState): ScheduledAction
```


Get an existing ScheduledAction resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L29">property endTime</a>
</h3>

```typescript
public endTime: pulumi.Output<string | undefined>;
```


The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L37">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L41">property scalableDimension</a>
</h3>

```typescript
public scalableDimension: pulumi.Output<string | undefined>;
```


The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L45">property scalableTargetAction</a>
</h3>

```typescript
public scalableTargetAction: pulumi.Output<{ ... } | undefined>;
```


The new minimum and maximum capacity. You can set both values or just one. See [below](#scalable-target-action-arguments)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L49">property schedule</a>
</h3>

```typescript
public schedule: pulumi.Output<string | undefined>;
```


The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L53">property serviceNamespace</a>
</h3>

```typescript
public serviceNamespace: pulumi.Output<string>;
```


The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L57">property startTime</a>
</h3>

```typescript
public startTime: pulumi.Output<string | undefined>;
```


The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Target">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L9">class Target</a>
</h2>

Provides an Application AutoScaling ScalableTarget resource. To manage policies which get attached to the target, see the [`aws_appautoscaling_policy` resource](/docs/providers/aws/r/appautoscaling_policy.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L46">constructor</a>
</h3>

```typescript
new Target(name: string, args: TargetArgs, opts?: pulumi.ResourceOptions)
```


Create a Target resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Target(name: string, state?: TargetState, opts?: pulumi.ResourceOptions)
```


Create a Target resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TargetState): Target
```


Get an existing Target resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L25">property maxCapacity</a>
</h3>

```typescript
public maxCapacity: pulumi.Output<number>;
```


The max capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L29">property minCapacity</a>
</h3>

```typescript
public minCapacity: pulumi.Output<number>;
```


The min capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L33">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L38">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L42">property scalableDimension</a>
</h3>

```typescript
public scalableDimension: pulumi.Output<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L46">property serviceNamespace</a>
</h3>

```typescript
public serviceNamespace: pulumi.Output<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L172">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L176">property adjustmentType</a>
</h3>

```typescript
adjustmentType?: pulumi.Input<string>;
```


The scaling policy's adjustment type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L177">property alarms</a>
</h3>

```typescript
alarms?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L178">property cooldown</a>
</h3>

```typescript
cooldown?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L179">property metricAggregationType</a>
</h3>

```typescript
metricAggregationType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L180">property minAdjustmentMagnitude</a>
</h3>

```typescript
minAdjustmentMagnitude?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L184">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L188">property policyType</a>
</h3>

```typescript
policyType?: pulumi.Input<string>;
```


For DynamoDB, only `TargetTrackingScaling` is supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L192">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L196">property scalableDimension</a>
</h3>

```typescript
scalableDimension: pulumi.Input<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L200">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace: pulumi.Input<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L201">property stepAdjustments</a>
</h3>

```typescript
stepAdjustments?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L205">property stepScalingPolicyConfigurations</a>
</h3>

```typescript
stepScalingPolicyConfigurations?: pulumi.Input<{ ... }[]>;
```


Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L209">property targetTrackingScalingPolicyConfiguration</a>
</h3>

```typescript
targetTrackingScalingPolicyConfiguration?: pulumi.Input<{ ... }>;
```


A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L125">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L129">property adjustmentType</a>
</h3>

```typescript
adjustmentType?: pulumi.Input<string>;
```


The scaling policy's adjustment type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L130">property alarms</a>
</h3>

```typescript
alarms?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L134">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS to the scaling policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L135">property cooldown</a>
</h3>

```typescript
cooldown?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L136">property metricAggregationType</a>
</h3>

```typescript
metricAggregationType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L137">property minAdjustmentMagnitude</a>
</h3>

```typescript
minAdjustmentMagnitude?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L145">property policyType</a>
</h3>

```typescript
policyType?: pulumi.Input<string>;
```


For DynamoDB, only `TargetTrackingScaling` is supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L149">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L153">property scalableDimension</a>
</h3>

```typescript
scalableDimension?: pulumi.Input<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L157">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace?: pulumi.Input<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L158">property stepAdjustments</a>
</h3>

```typescript
stepAdjustments?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L162">property stepScalingPolicyConfigurations</a>
</h3>

```typescript
stepScalingPolicyConfigurations?: pulumi.Input<{ ... }[]>;
```


Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/policy.ts#L166">property targetTrackingScalingPolicyConfiguration</a>
</h3>

```typescript
targetTrackingScalingPolicyConfiguration?: pulumi.Input<{ ... }>;
```


A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.

<h2 class="pdoc-module-header" id="ScheduledActionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L149">interface ScheduledActionArgs</a>
</h2>

The set of arguments for constructing a ScheduledAction resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L153">property endTime</a>
</h3>

```typescript
endTime?: pulumi.Input<string>;
```


The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L157">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L161">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L165">property scalableDimension</a>
</h3>

```typescript
scalableDimension?: pulumi.Input<string>;
```


The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L169">property scalableTargetAction</a>
</h3>

```typescript
scalableTargetAction?: pulumi.Input<{ ... }>;
```


The new minimum and maximum capacity. You can set both values or just one. See [below](#scalable-target-action-arguments)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L173">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<string>;
```


The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L177">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace: pulumi.Input<string>;
```


The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L181">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z

<h2 class="pdoc-module-header" id="ScheduledActionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L107">interface ScheduledActionState</a>
</h2>

Input properties used for looking up and filtering ScheduledAction resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L111">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L115">property endTime</a>
</h3>

```typescript
endTime?: pulumi.Input<string>;
```


The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L123">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L127">property scalableDimension</a>
</h3>

```typescript
scalableDimension?: pulumi.Input<string>;
```


The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L131">property scalableTargetAction</a>
</h3>

```typescript
scalableTargetAction?: pulumi.Input<{ ... }>;
```


The new minimum and maximum capacity. You can set both values or just one. See [below](#scalable-target-action-arguments)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L135">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<string>;
```


The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L139">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace?: pulumi.Input<string>;
```


The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/scheduledAction.ts#L143">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z

<h2 class="pdoc-module-header" id="TargetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L130">interface TargetArgs</a>
</h2>

The set of arguments for constructing a Target resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L134">property maxCapacity</a>
</h3>

```typescript
maxCapacity: pulumi.Input<number>;
```


The max capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L138">property minCapacity</a>
</h3>

```typescript
minCapacity: pulumi.Input<number>;
```


The min capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L142">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L147">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L151">property scalableDimension</a>
</h3>

```typescript
scalableDimension: pulumi.Input<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L155">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace: pulumi.Input<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h2 class="pdoc-module-header" id="TargetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L99">interface TargetState</a>
</h2>

Input properties used for looking up and filtering Target resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L103">property maxCapacity</a>
</h3>

```typescript
maxCapacity?: pulumi.Input<number>;
```


The max capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L107">property minCapacity</a>
</h3>

```typescript
minCapacity?: pulumi.Input<number>;
```


The min capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L111">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L116">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L120">property scalableDimension</a>
</h3>

```typescript
scalableDimension?: pulumi.Input<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appautoscaling/target.ts#L124">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace?: pulumi.Input<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

