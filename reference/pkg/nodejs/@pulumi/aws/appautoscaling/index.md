---
title: Module appautoscaling
---

<a href="../index.html">@pulumi/aws</a> &gt; appautoscaling

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

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts">appautoscaling/policy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts">appautoscaling/scheduledAction.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts">appautoscaling/target.ts</a> 


<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L10">class Policy</a>
</h2>

Provides an Application AutoScaling Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L63">constructor</a>
</h3>

```typescript
new Policy(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState): Policy
```


Get an existing Policy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L26">property adjustmentType</a>
</h3>

```typescript
public adjustmentType: pulumi.Output<string | undefined>;
```


The scaling policy's adjustment type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L27">property alarms</a>
</h3>

```typescript
public alarms: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L31">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS to the scaling policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L32">property cooldown</a>
</h3>

```typescript
public cooldown: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L33">property metricAggregationType</a>
</h3>

```typescript
public metricAggregationType: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L34">property minAdjustmentMagnitude</a>
</h3>

```typescript
public minAdjustmentMagnitude: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L42">property policyType</a>
</h3>

```typescript
public policyType: pulumi.Output<string | undefined>;
```


For DynamoDB, only `TargetTrackingScaling` is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both `StepScaling` and `TargetTrackingScaling` are supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L46">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L50">property scalableDimension</a>
</h3>

```typescript
public scalableDimension: pulumi.Output<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L54">property serviceNamespace</a>
</h3>

```typescript
public serviceNamespace: pulumi.Output<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L55">property stepAdjustments</a>
</h3>

```typescript
public stepAdjustments: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L59">property stepScalingPolicyConfigurations</a>
</h3>

```typescript
public stepScalingPolicyConfigurations: pulumi.Output<{ ... }[] | undefined>;
```


Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L63">property targetTrackingScalingPolicyConfiguration</a>
</h3>

```typescript
public targetTrackingScalingPolicyConfiguration: pulumi.Output<{ ... } | undefined>;
```


A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ScheduledAction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L10">class ScheduledAction</a>
</h2>

Provides an Application AutoScaling ScheduledAction resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L58">constructor</a>
</h3>

```typescript
new ScheduledAction(name: string, args: ScheduledActionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ScheduledAction resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ScheduledActionState): ScheduledAction
```


Get an existing ScheduledAction resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L30">property endTime</a>
</h3>

```typescript
public endTime: pulumi.Output<string | undefined>;
```


The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L38">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L42">property scalableDimension</a>
</h3>

```typescript
public scalableDimension: pulumi.Output<string | undefined>;
```


The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L46">property scalableTargetAction</a>
</h3>

```typescript
public scalableTargetAction: pulumi.Output<{ ... } | undefined>;
```


The new minimum and maximum capacity. You can set both values or just one. See below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L50">property schedule</a>
</h3>

```typescript
public schedule: pulumi.Output<string | undefined>;
```


The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L54">property serviceNamespace</a>
</h3>

```typescript
public serviceNamespace: pulumi.Output<string>;
```


The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L58">property startTime</a>
</h3>

```typescript
public startTime: pulumi.Output<string | undefined>;
```


The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Target">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L10">class Target</a>
</h2>

Provides an Application AutoScaling ScalableTarget resource. To manage policies which get attached to the target, see the [`aws_appautoscaling_policy` resource](https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L47">constructor</a>
</h3>

```typescript
new Target(name: string, args: TargetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Target resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TargetState): Target
```


Get an existing Target resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L26">property maxCapacity</a>
</h3>

```typescript
public maxCapacity: pulumi.Output<number>;
```


The max capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L30">property minCapacity</a>
</h3>

```typescript
public minCapacity: pulumi.Output<number>;
```


The min capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L34">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L39">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L43">property scalableDimension</a>
</h3>

```typescript
public scalableDimension: pulumi.Output<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L47">property serviceNamespace</a>
</h3>

```typescript
public serviceNamespace: pulumi.Output<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L171">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L175">property adjustmentType</a>
</h3>

```typescript
adjustmentType?: pulumi.Input<string>;
```


The scaling policy's adjustment type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L176">property alarms</a>
</h3>

```typescript
alarms?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L177">property cooldown</a>
</h3>

```typescript
cooldown?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L178">property metricAggregationType</a>
</h3>

```typescript
metricAggregationType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L179">property minAdjustmentMagnitude</a>
</h3>

```typescript
minAdjustmentMagnitude?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L183">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L187">property policyType</a>
</h3>

```typescript
policyType?: pulumi.Input<string>;
```


For DynamoDB, only `TargetTrackingScaling` is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both `StepScaling` and `TargetTrackingScaling` are supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L191">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L195">property scalableDimension</a>
</h3>

```typescript
scalableDimension: pulumi.Input<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L199">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace: pulumi.Input<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L200">property stepAdjustments</a>
</h3>

```typescript
stepAdjustments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L204">property stepScalingPolicyConfigurations</a>
</h3>

```typescript
stepScalingPolicyConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L208">property targetTrackingScalingPolicyConfiguration</a>
</h3>

```typescript
targetTrackingScalingPolicyConfiguration?: pulumi.Input<{ ... }>;
```


A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L124">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L128">property adjustmentType</a>
</h3>

```typescript
adjustmentType?: pulumi.Input<string>;
```


The scaling policy's adjustment type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L129">property alarms</a>
</h3>

```typescript
alarms?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L133">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS to the scaling policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L134">property cooldown</a>
</h3>

```typescript
cooldown?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L135">property metricAggregationType</a>
</h3>

```typescript
metricAggregationType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L136">property minAdjustmentMagnitude</a>
</h3>

```typescript
minAdjustmentMagnitude?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L144">property policyType</a>
</h3>

```typescript
policyType?: pulumi.Input<string>;
```


For DynamoDB, only `TargetTrackingScaling` is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both `StepScaling` and `TargetTrackingScaling` are supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L148">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L152">property scalableDimension</a>
</h3>

```typescript
scalableDimension?: pulumi.Input<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L156">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace?: pulumi.Input<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L157">property stepAdjustments</a>
</h3>

```typescript
stepAdjustments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L161">property stepScalingPolicyConfigurations</a>
</h3>

```typescript
stepScalingPolicyConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/policy.ts#L165">property targetTrackingScalingPolicyConfiguration</a>
</h3>

```typescript
targetTrackingScalingPolicyConfiguration?: pulumi.Input<{ ... }>;
```


A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.

<h2 class="pdoc-module-header" id="ScheduledActionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L148">interface ScheduledActionArgs</a>
</h2>

The set of arguments for constructing a ScheduledAction resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L152">property endTime</a>
</h3>

```typescript
endTime?: pulumi.Input<string>;
```


The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L160">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L164">property scalableDimension</a>
</h3>

```typescript
scalableDimension?: pulumi.Input<string>;
```


The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L168">property scalableTargetAction</a>
</h3>

```typescript
scalableTargetAction?: pulumi.Input<{ ... }>;
```


The new minimum and maximum capacity. You can set both values or just one. See below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L172">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<string>;
```


The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L176">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace: pulumi.Input<string>;
```


The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L180">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z

<h2 class="pdoc-module-header" id="ScheduledActionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L106">interface ScheduledActionState</a>
</h2>

Input properties used for looking up and filtering ScheduledAction resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L110">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L114">property endTime</a>
</h3>

```typescript
endTime?: pulumi.Input<string>;
```


The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the scheduled action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L122">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L126">property scalableDimension</a>
</h3>

```typescript
scalableDimension?: pulumi.Input<string>;
```


The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L130">property scalableTargetAction</a>
</h3>

```typescript
scalableTargetAction?: pulumi.Input<{ ... }>;
```


The new minimum and maximum capacity. You can set both values or just one. See below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L134">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<string>;
```


The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L138">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace?: pulumi.Input<string>;
```


The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/scheduledAction.ts#L142">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z

<h2 class="pdoc-module-header" id="TargetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L129">interface TargetArgs</a>
</h2>

The set of arguments for constructing a Target resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L133">property maxCapacity</a>
</h3>

```typescript
maxCapacity: pulumi.Input<number>;
```


The max capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L137">property minCapacity</a>
</h3>

```typescript
minCapacity: pulumi.Input<number>;
```


The min capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L141">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L146">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L150">property scalableDimension</a>
</h3>

```typescript
scalableDimension: pulumi.Input<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L154">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace: pulumi.Input<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h2 class="pdoc-module-header" id="TargetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L98">interface TargetState</a>
</h2>

Input properties used for looking up and filtering Target resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L102">property maxCapacity</a>
</h3>

```typescript
maxCapacity?: pulumi.Input<number>;
```


The max capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L106">property minCapacity</a>
</h3>

```typescript
minCapacity?: pulumi.Input<number>;
```


The min capacity of the scalable target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L110">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L115">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L119">property scalableDimension</a>
</h3>

```typescript
scalableDimension?: pulumi.Input<string>;
```


The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appautoscaling/target.ts#L123">property serviceNamespace</a>
</h3>

```typescript
serviceNamespace?: pulumi.Input<string>;
```


The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters)

