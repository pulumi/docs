---
title: Module autoscaling
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Attachment">class Attachment</a>
* <a href="#Group">class Group</a>
* <a href="#LifecycleHook">class LifecycleHook</a>
* <a href="#Notification">class Notification</a>
* <a href="#Policy">class Policy</a>
* <a href="#Schedule">class Schedule</a>
* <a href="#AttachmentArgs">interface AttachmentArgs</a>
* <a href="#AttachmentState">interface AttachmentState</a>
* <a href="#GroupArgs">interface GroupArgs</a>
* <a href="#GroupState">interface GroupState</a>
* <a href="#LifecycleHookArgs">interface LifecycleHookArgs</a>
* <a href="#LifecycleHookState">interface LifecycleHookState</a>
* <a href="#NotificationArgs">interface NotificationArgs</a>
* <a href="#NotificationState">interface NotificationState</a>
* <a href="#PolicyArgs">interface PolicyArgs</a>
* <a href="#PolicyState">interface PolicyState</a>
* <a href="#ScheduleArgs">interface ScheduleArgs</a>
* <a href="#ScheduleState">interface ScheduleState</a>

<a href="/autoscaling/attachment.ts">autoscaling/attachment.ts</a> <a href="/autoscaling/group.ts">autoscaling/group.ts</a> <a href="/autoscaling/lifecycleHook.ts">autoscaling/lifecycleHook.ts</a> <a href="/autoscaling/notification.ts">autoscaling/notification.ts</a> <a href="/autoscaling/policy.ts">autoscaling/policy.ts</a> <a href="/autoscaling/schedule.ts">autoscaling/schedule.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Attachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L16">class Attachment</a>
</h2>

Provides an AutoScaling Attachment resource.

~> **NOTE on AutoScaling Groups and ASG Attachments:** Terraform currently provides
both a standalone ASG Attachment resource (describing an ASG attached to
an ELB), and an [AutoScaling Group resource](autoscaling_group.html) with
`load_balancers` defined in-line. At this time you cannot use an ASG with in-line
load balancers in conjunction with an ASG Attachment resource. Doing so will cause a
conflict and will overwrite attachments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L40">constructor</a>
</h3>

```typescript
new Attachment(name: string, args: AttachmentArgs, opts?: pulumi.ResourceOptions)
```


Create a Attachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Attachment(name: string, state?: AttachmentState, opts?: pulumi.ResourceOptions)
```


Create a Attachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AttachmentState): Attachment
```


Get an existing Attachment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L32">property albTargetGroupArn</a>
</h3>

```typescript
public albTargetGroupArn: pulumi.Output<string | undefined>;
```


The ARN of an ALB Target Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L36">property autoscalingGroupName</a>
</h3>

```typescript
public autoscalingGroupName: pulumi.Output<string>;
```


Name of ASG to associate with the ELB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L40">property elb</a>
</h3>

```typescript
public elb: pulumi.Output<string | undefined>;
```


The name of the ELB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Group">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L9">class Group</a>
</h2>

Provides an AutoScaling Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L160">constructor</a>
</h3>

```typescript
new Group(name: string, args: GroupArgs, opts?: pulumi.ResourceOptions)
```


Create a Group resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Group(name: string, state?: GroupState, opts?: pulumi.ResourceOptions)
```


Create a Group resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState): Group
```


Get an existing Group resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN for this AutoScaling Group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L29">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[]>;
```


A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L33">property defaultCooldown</a>
</h3>

```typescript
public defaultCooldown: pulumi.Output<number>;
```


The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L39">property desiredCapacity</a>
</h3>

```typescript
public desiredCapacity: pulumi.Output<number>;
```


The number of Amazon EC2 instances that
should be running in the group. (See also [Waiting for
Capacity](#waiting-for-capacity) below.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L48">property enabledMetrics</a>
</h3>

```typescript
public enabledMetrics: pulumi.Output<string[] | undefined>;
```


A list of metrics to collect. The allowed values are `GroupMinSize`, `GroupMaxSize`, `GroupDesiredCapacity`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupTerminatingInstances`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: "10m") A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for ASG instances to be healthy before timing out.  (See also [Waiting
for Capacity](#waiting-for-capacity) below.) Setting this to "0" causes
Terraform to skip all Capacity Waiting behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L56">property forceDelete</a>
</h3>

```typescript
public forceDelete: pulumi.Output<boolean | undefined>;
```


Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it's in the process of scaling a resource. Normally, Terraform
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L60">property healthCheckGracePeriod</a>
</h3>

```typescript
public healthCheckGracePeriod: pulumi.Output<number | undefined>;
```


Time (in seconds) after instance comes into service before checking health.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L64">property healthCheckType</a>
</h3>

```typescript
public healthCheckType: pulumi.Output<string>;
```


"EC2" or "ELB". Controls how health checking is done.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L74">property initialLifecycleHooks</a>
</h3>

```typescript
public initialLifecycleHooks: pulumi.Output<{ ... }[] | undefined>;
```


One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws_autoscaling_lifecycle_hook`](/docs/providers/aws/r/autoscaling_lifecycle_hooks.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws_autoscaling_lifecycle_hook` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L78">property launchConfiguration</a>
</h3>

```typescript
public launchConfiguration: pulumi.Output<string>;
```


The name of the launch configuration to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L83">property loadBalancers</a>
</h3>

```typescript
public loadBalancers: pulumi.Output<string[]>;
```


A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L87">property maxSize</a>
</h3>

```typescript
public maxSize: pulumi.Output<number>;
```


The maximum size of the auto scale group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L91">property metricsGranularity</a>
</h3>

```typescript
public metricsGranularity: pulumi.Output<string | undefined>;
```


The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L98">property minElbCapacity</a>
</h3>

```typescript
public minElbCapacity: pulumi.Output<number | undefined>;
```


Setting this causes Terraform to wait for
this number of instances to show up healthy in the ELB only on creation.
Updates will not wait on ELB instance number changes.
(See also [Waiting for Capacity](#waiting-for-capacity) below.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L103">property minSize</a>
</h3>

```typescript
public minSize: pulumi.Output<number>;
```


The minimum size of the auto scale group.
(See also [Waiting for Capacity](#waiting-for-capacity) below.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L107">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the auto scaling group. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L112">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L116">property placementGroup</a>
</h3>

```typescript
public placementGroup: pulumi.Output<string | undefined>;
```


The name of the placement group into which you'll launch your instances, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L122">property protectFromScaleIn</a>
</h3>

```typescript
public protectFromScaleIn: pulumi.Output<boolean | undefined>;
```


Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L126">property serviceLinkedRoleArn</a>
</h3>

```typescript
public serviceLinkedRoleArn: pulumi.Output<string>;
```


The ARN of the service-linked role that the ASG will use to call other AWS services

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L131">property suspendedProcesses</a>
</h3>

```typescript
public suspendedProcesses: pulumi.Output<string[] | undefined>;
```


A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L135">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }[] | undefined>;
```


A list of tag blocks. Tags documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L139">property tagsCollection</a>
</h3>

```typescript
public tagsCollection: pulumi.Output<{ ... }[] | undefined>;
```


A list of tag blocks (maps). Tags documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L143">property targetGroupArns</a>
</h3>

```typescript
public targetGroupArns: pulumi.Output<string[]>;
```


A list of `aws_alb_target_group` ARNs, for use with Application Load Balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L147">property terminationPolicies</a>
</h3>

```typescript
public terminationPolicies: pulumi.Output<string[] | undefined>;
```


A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `Default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L151">property vpcZoneIdentifiers</a>
</h3>

```typescript
public vpcZoneIdentifiers: pulumi.Output<string[]>;
```


A list of subnet IDs to launch resources in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L152">property waitForCapacityTimeout</a>
</h3>

```typescript
public waitForCapacityTimeout: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L160">property waitForElbCapacity</a>
</h3>

```typescript
public waitForElbCapacity: pulumi.Output<number | undefined>;
```


Setting this will cause Terraform to wait
for exactly this number of healthy instances in all attached load balancers
on both create and update operations. (Takes precedence over
`min_elb_capacity` behavior.)
(See also [Waiting for Capacity](#waiting-for-capacity) below.)

<h2 class="pdoc-module-header" id="LifecycleHook">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L21">class LifecycleHook</a>
</h2>

Provides an AutoScaling Lifecycle Hook resource.

~> **NOTE:** Terraform has two types of ways you can add lifecycle hooks - via
the `initial_lifecycle_hook` attribute from the
[`aws_autoscaling_group`](/docs/providers/aws/r/autoscaling_group.html)
resource, or via this one. Hooks added via this resource will not be added
until the autoscaling group has been created, and depending on your
[capacity](/docs/providers/aws/r/autoscaling_group.html#waiting-for-capacity)
settings, after the initial instances have been launched, creating unintended
behavior. If you need hooks to run on all instances, add them with
`initial_lifecycle_hook` in
[`aws_autoscaling_group`](/docs/providers/aws/r/autoscaling_group.html),
but take care to not duplicate those hooks with this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L65">constructor</a>
</h3>

```typescript
new LifecycleHook(name: string, args: LifecycleHookArgs, opts?: pulumi.ResourceOptions)
```


Create a LifecycleHook resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new LifecycleHook(name: string, state?: LifecycleHookState, opts?: pulumi.ResourceOptions)
```


Create a LifecycleHook resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L30">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LifecycleHookState): LifecycleHook
```


Get an existing LifecycleHook resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L37">property autoscalingGroupName</a>
</h3>

```typescript
public autoscalingGroupName: pulumi.Output<string>;
```


The name of the Auto Scaling group to which you want to assign the lifecycle hook

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L41">property defaultResult</a>
</h3>

```typescript
public defaultResult: pulumi.Output<string>;
```


Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L45">property heartbeatTimeout</a>
</h3>

```typescript
public heartbeatTimeout: pulumi.Output<number | undefined>;
```


Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L49">property lifecycleTransition</a>
</h3>

```typescript
public lifecycleTransition: pulumi.Output<string>;
```


The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the lifecycle hook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L57">property notificationMetadata</a>
</h3>

```typescript
public notificationMetadata: pulumi.Output<string | undefined>;
```


Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L61">property notificationTargetArn</a>
</h3>

```typescript
public notificationTargetArn: pulumi.Output<string | undefined>;
```


The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L65">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string | undefined>;
```


The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Notification">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L11">class Notification</a>
</h2>

Provides an AutoScaling Group with Notification support, via SNS Topics. Each of
the `notifications` map to a [Notification Configuration][2] inside Amazon Web
Services, and are applied to each AutoScaling Group you supply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L36">constructor</a>
</h3>

```typescript
new Notification(name: string, args: NotificationArgs, opts?: pulumi.ResourceOptions)
```


Create a Notification resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Notification(name: string, state?: NotificationState, opts?: pulumi.ResourceOptions)
```


Create a Notification resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NotificationState): Notification
```


Get an existing Notification resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L27">property groupNames</a>
</h3>

```typescript
public groupNames: pulumi.Output<string[]>;
```


A list of AutoScaling Group Names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L32">property notifications</a>
</h3>

```typescript
public notifications: pulumi.Output<string[]>;
```


A list of Notification Types that trigger
notifications. Acceptable values are documented [in the AWS documentation here][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L36">property topicArn</a>
</h3>

```typescript
public topicArn: pulumi.Output<string>;
```


The Topic ARN for notifications to be sent through

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L15">class Policy</a>
</h2>

Provides an AutoScaling Scaling Policy resource.

~> **NOTE:** You may want to omit `desired_capacity` attribute from attached `aws_autoscaling_group`
when using autoscaling policies. It's good practice to pick either
[manual](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html)
or [dynamic](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html)
(policy-based) scaling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L75">constructor</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L24">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L31">property adjustmentType</a>
</h3>

```typescript
public adjustmentType: pulumi.Output<string | undefined>;
```


Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L35">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS to the scaling policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L39">property autoscalingGroupName</a>
</h3>

```typescript
public autoscalingGroupName: pulumi.Output<string>;
```


The name of the autoscaling group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L43">property cooldown</a>
</h3>

```typescript
public cooldown: pulumi.Output<number | undefined>;
```


The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L47">property estimatedInstanceWarmup</a>
</h3>

```typescript
public estimatedInstanceWarmup: pulumi.Output<number | undefined>;
```


The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L51">property metricAggregationType</a>
</h3>

```typescript
public metricAggregationType: pulumi.Output<string>;
```


The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L52">property minAdjustmentMagnitude</a>
</h3>

```typescript
public minAdjustmentMagnitude: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L56">property minAdjustmentStep</a>
</h3>

```typescript
public minAdjustmentStep: pulumi.Output<number | undefined>;
```


Use `min_adjustment_magnitude` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the dimension.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L64">property policyType</a>
</h3>

```typescript
public policyType: pulumi.Output<string | undefined>;
```


The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L70">property scalingAdjustment</a>
</h3>

```typescript
public scalingAdjustment: pulumi.Output<number | undefined>;
```


The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L71">property stepAdjustments</a>
</h3>

```typescript
public stepAdjustments: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L75">property targetTrackingConfiguration</a>
</h3>

```typescript
public targetTrackingConfiguration: pulumi.Output<{ ... } | undefined>;
```


A target tracking policy. These have the following structure:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Schedule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L9">class Schedule</a>
</h2>

Provides an AutoScaling Schedule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L61">constructor</a>
</h3>

```typescript
new Schedule(name: string, args: ScheduleArgs, opts?: pulumi.ResourceOptions)
```


Create a Schedule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Schedule(name: string, state?: ScheduleState, opts?: pulumi.ResourceOptions)
```


Create a Schedule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ScheduleState): Schedule
```


Get an existing Schedule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS to the autoscaling schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L29">property autoscalingGroupName</a>
</h3>

```typescript
public autoscalingGroupName: pulumi.Output<string>;
```


The name or Amazon Resource Name (ARN) of the Auto Scaling group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L33">property desiredCapacity</a>
</h3>

```typescript
public desiredCapacity: pulumi.Output<number>;
```


The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L38">property endTime</a>
</h3>

```typescript
public endTime: pulumi.Output<string>;
```


The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L43">property maxSize</a>
</h3>

```typescript
public maxSize: pulumi.Output<number>;
```


The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don't want to change the maximum size at the scheduled time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L48">property minSize</a>
</h3>

```typescript
public minSize: pulumi.Output<number>;
```


The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don't want to change the minimum size at the scheduled time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L52">property recurrence</a>
</h3>

```typescript
public recurrence: pulumi.Output<string>;
```


The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L56">property scheduledActionName</a>
</h3>

```typescript
public scheduledActionName: pulumi.Output<string>;
```


The name of this scaling action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L61">property startTime</a>
</h3>

```typescript
public startTime: pulumi.Output<string>;
```


The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L93">interface AttachmentArgs</a>
</h2>

The set of arguments for constructing a Attachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L97">property albTargetGroupArn</a>
</h3>

```typescript
albTargetGroupArn?: pulumi.Input<string>;
```


The ARN of an ALB Target Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L101">property autoscalingGroupName</a>
</h3>

```typescript
autoscalingGroupName: pulumi.Input<string>;
```


Name of ASG to associate with the ELB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L105">property elb</a>
</h3>

```typescript
elb?: pulumi.Input<string>;
```


The name of the ELB.

<h2 class="pdoc-module-header" id="AttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L75">interface AttachmentState</a>
</h2>

Input properties used for looking up and filtering Attachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L79">property albTargetGroupArn</a>
</h3>

```typescript
albTargetGroupArn?: pulumi.Input<string>;
```


The ARN of an ALB Target Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L83">property autoscalingGroupName</a>
</h3>

```typescript
autoscalingGroupName?: pulumi.Input<string>;
```


Name of ASG to associate with the ELB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/attachment.ts#L87">property elb</a>
</h3>

```typescript
elb?: pulumi.Input<string>;
```


The name of the ELB.

<h2 class="pdoc-module-header" id="GroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L396">interface GroupArgs</a>
</h2>

The set of arguments for constructing a Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L400">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L404">property defaultCooldown</a>
</h3>

```typescript
defaultCooldown?: pulumi.Input<number>;
```


The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L410">property desiredCapacity</a>
</h3>

```typescript
desiredCapacity?: pulumi.Input<number>;
```


The number of Amazon EC2 instances that
should be running in the group. (See also [Waiting for
Capacity](#waiting-for-capacity) below.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L419">property enabledMetrics</a>
</h3>

```typescript
enabledMetrics?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of metrics to collect. The allowed values are `GroupMinSize`, `GroupMaxSize`, `GroupDesiredCapacity`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupTerminatingInstances`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: "10m") A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for ASG instances to be healthy before timing out.  (See also [Waiting
for Capacity](#waiting-for-capacity) below.) Setting this to "0" causes
Terraform to skip all Capacity Waiting behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L427">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it's in the process of scaling a resource. Normally, Terraform
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L431">property healthCheckGracePeriod</a>
</h3>

```typescript
healthCheckGracePeriod?: pulumi.Input<number>;
```


Time (in seconds) after instance comes into service before checking health.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L435">property healthCheckType</a>
</h3>

```typescript
healthCheckType?: pulumi.Input<string>;
```


"EC2" or "ELB". Controls how health checking is done.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L445">property initialLifecycleHooks</a>
</h3>

```typescript
initialLifecycleHooks?: pulumi.Input<{ ... }[]>;
```


One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws_autoscaling_lifecycle_hook`](/docs/providers/aws/r/autoscaling_lifecycle_hooks.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws_autoscaling_lifecycle_hook` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L449">property launchConfiguration</a>
</h3>

```typescript
launchConfiguration: pulumi.Input<string>;
```


The name of the launch configuration to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L454">property loadBalancers</a>
</h3>

```typescript
loadBalancers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L458">property maxSize</a>
</h3>

```typescript
maxSize: pulumi.Input<number>;
```


The maximum size of the auto scale group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L462">property metricsGranularity</a>
</h3>

```typescript
metricsGranularity?: pulumi.Input<string>;
```


The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L469">property minElbCapacity</a>
</h3>

```typescript
minElbCapacity?: pulumi.Input<number>;
```


Setting this causes Terraform to wait for
this number of instances to show up healthy in the ELB only on creation.
Updates will not wait on ELB instance number changes.
(See also [Waiting for Capacity](#waiting-for-capacity) below.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L474">property minSize</a>
</h3>

```typescript
minSize: pulumi.Input<number>;
```


The minimum size of the auto scale group.
(See also [Waiting for Capacity](#waiting-for-capacity) below.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L478">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the auto scaling group. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L483">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L487">property placementGroup</a>
</h3>

```typescript
placementGroup?: pulumi.Input<string>;
```


The name of the placement group into which you'll launch your instances, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L493">property protectFromScaleIn</a>
</h3>

```typescript
protectFromScaleIn?: pulumi.Input<boolean>;
```


Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L497">property serviceLinkedRoleArn</a>
</h3>

```typescript
serviceLinkedRoleArn?: pulumi.Input<string>;
```


The ARN of the service-linked role that the ASG will use to call other AWS services

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L502">property suspendedProcesses</a>
</h3>

```typescript
suspendedProcesses?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L506">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }[]>;
```


A list of tag blocks. Tags documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L510">property tagsCollection</a>
</h3>

```typescript
tagsCollection?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of tag blocks (maps). Tags documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L514">property targetGroupArns</a>
</h3>

```typescript
targetGroupArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of `aws_alb_target_group` ARNs, for use with Application Load Balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L518">property terminationPolicies</a>
</h3>

```typescript
terminationPolicies?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `Default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L522">property vpcZoneIdentifiers</a>
</h3>

```typescript
vpcZoneIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of subnet IDs to launch resources in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L523">property waitForCapacityTimeout</a>
</h3>

```typescript
waitForCapacityTimeout?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L531">property waitForElbCapacity</a>
</h3>

```typescript
waitForElbCapacity?: pulumi.Input<number>;
```


Setting this will cause Terraform to wait
for exactly this number of healthy instances in all attached load balancers
on both create and update operations. (Takes precedence over
`min_elb_capacity` behavior.)
(See also [Waiting for Capacity](#waiting-for-capacity) below.)

<h2 class="pdoc-module-header" id="GroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L251">interface GroupState</a>
</h2>

Input properties used for looking up and filtering Group resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L255">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN for this AutoScaling Group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L259">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L263">property defaultCooldown</a>
</h3>

```typescript
defaultCooldown?: pulumi.Input<number>;
```


The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L269">property desiredCapacity</a>
</h3>

```typescript
desiredCapacity?: pulumi.Input<number>;
```


The number of Amazon EC2 instances that
should be running in the group. (See also [Waiting for
Capacity](#waiting-for-capacity) below.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L278">property enabledMetrics</a>
</h3>

```typescript
enabledMetrics?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of metrics to collect. The allowed values are `GroupMinSize`, `GroupMaxSize`, `GroupDesiredCapacity`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupTerminatingInstances`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: "10m") A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for ASG instances to be healthy before timing out.  (See also [Waiting
for Capacity](#waiting-for-capacity) below.) Setting this to "0" causes
Terraform to skip all Capacity Waiting behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L286">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it's in the process of scaling a resource. Normally, Terraform
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L290">property healthCheckGracePeriod</a>
</h3>

```typescript
healthCheckGracePeriod?: pulumi.Input<number>;
```


Time (in seconds) after instance comes into service before checking health.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L294">property healthCheckType</a>
</h3>

```typescript
healthCheckType?: pulumi.Input<string>;
```


"EC2" or "ELB". Controls how health checking is done.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L304">property initialLifecycleHooks</a>
</h3>

```typescript
initialLifecycleHooks?: pulumi.Input<{ ... }[]>;
```


One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws_autoscaling_lifecycle_hook`](/docs/providers/aws/r/autoscaling_lifecycle_hooks.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws_autoscaling_lifecycle_hook` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L308">property launchConfiguration</a>
</h3>

```typescript
launchConfiguration?: pulumi.Input<string>;
```


The name of the launch configuration to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L313">property loadBalancers</a>
</h3>

```typescript
loadBalancers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L317">property maxSize</a>
</h3>

```typescript
maxSize?: pulumi.Input<number>;
```


The maximum size of the auto scale group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L321">property metricsGranularity</a>
</h3>

```typescript
metricsGranularity?: pulumi.Input<string>;
```


The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L328">property minElbCapacity</a>
</h3>

```typescript
minElbCapacity?: pulumi.Input<number>;
```


Setting this causes Terraform to wait for
this number of instances to show up healthy in the ELB only on creation.
Updates will not wait on ELB instance number changes.
(See also [Waiting for Capacity](#waiting-for-capacity) below.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L333">property minSize</a>
</h3>

```typescript
minSize?: pulumi.Input<number>;
```


The minimum size of the auto scale group.
(See also [Waiting for Capacity](#waiting-for-capacity) below.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L337">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the auto scaling group. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L342">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L346">property placementGroup</a>
</h3>

```typescript
placementGroup?: pulumi.Input<string>;
```


The name of the placement group into which you'll launch your instances, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L352">property protectFromScaleIn</a>
</h3>

```typescript
protectFromScaleIn?: pulumi.Input<boolean>;
```


Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L356">property serviceLinkedRoleArn</a>
</h3>

```typescript
serviceLinkedRoleArn?: pulumi.Input<string>;
```


The ARN of the service-linked role that the ASG will use to call other AWS services

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L361">property suspendedProcesses</a>
</h3>

```typescript
suspendedProcesses?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L365">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }[]>;
```


A list of tag blocks. Tags documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L369">property tagsCollection</a>
</h3>

```typescript
tagsCollection?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of tag blocks (maps). Tags documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L373">property targetGroupArns</a>
</h3>

```typescript
targetGroupArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of `aws_alb_target_group` ARNs, for use with Application Load Balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L377">property terminationPolicies</a>
</h3>

```typescript
terminationPolicies?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `Default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L381">property vpcZoneIdentifiers</a>
</h3>

```typescript
vpcZoneIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of subnet IDs to launch resources in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L382">property waitForCapacityTimeout</a>
</h3>

```typescript
waitForCapacityTimeout?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/group.ts#L390">property waitForElbCapacity</a>
</h3>

```typescript
waitForElbCapacity?: pulumi.Input<number>;
```


Setting this will cause Terraform to wait
for exactly this number of healthy instances in all attached load balancers
on both create and update operations. (Takes precedence over
`min_elb_capacity` behavior.)
(See also [Waiting for Capacity](#waiting-for-capacity) below.)

<h2 class="pdoc-module-header" id="LifecycleHookArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L151">interface LifecycleHookArgs</a>
</h2>

The set of arguments for constructing a LifecycleHook resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L155">property autoscalingGroupName</a>
</h3>

```typescript
autoscalingGroupName: pulumi.Input<string>;
```


The name of the Auto Scaling group to which you want to assign the lifecycle hook

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L159">property defaultResult</a>
</h3>

```typescript
defaultResult?: pulumi.Input<string>;
```


Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L163">property heartbeatTimeout</a>
</h3>

```typescript
heartbeatTimeout?: pulumi.Input<number>;
```


Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L167">property lifecycleTransition</a>
</h3>

```typescript
lifecycleTransition: pulumi.Input<string>;
```


The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the lifecycle hook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L175">property notificationMetadata</a>
</h3>

```typescript
notificationMetadata?: pulumi.Input<string>;
```


Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L179">property notificationTargetArn</a>
</h3>

```typescript
notificationTargetArn?: pulumi.Input<string>;
```


The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L183">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.

<h2 class="pdoc-module-header" id="LifecycleHookState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L113">interface LifecycleHookState</a>
</h2>

Input properties used for looking up and filtering LifecycleHook resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L117">property autoscalingGroupName</a>
</h3>

```typescript
autoscalingGroupName?: pulumi.Input<string>;
```


The name of the Auto Scaling group to which you want to assign the lifecycle hook

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L121">property defaultResult</a>
</h3>

```typescript
defaultResult?: pulumi.Input<string>;
```


Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L125">property heartbeatTimeout</a>
</h3>

```typescript
heartbeatTimeout?: pulumi.Input<number>;
```


Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L129">property lifecycleTransition</a>
</h3>

```typescript
lifecycleTransition?: pulumi.Input<string>;
```


The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L133">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the lifecycle hook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L137">property notificationMetadata</a>
</h3>

```typescript
notificationMetadata?: pulumi.Input<string>;
```


Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L141">property notificationTargetArn</a>
</h3>

```typescript
notificationTargetArn?: pulumi.Input<string>;
```


The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/lifecycleHook.ts#L145">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.

<h2 class="pdoc-module-header" id="NotificationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L96">interface NotificationArgs</a>
</h2>

The set of arguments for constructing a Notification resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L100">property groupNames</a>
</h3>

```typescript
groupNames: pulumi.Input<pulumi.Input<string>[]>;
```


A list of AutoScaling Group Names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L105">property notifications</a>
</h3>

```typescript
notifications: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Notification Types that trigger
notifications. Acceptable values are documented [in the AWS documentation here][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L109">property topicArn</a>
</h3>

```typescript
topicArn: pulumi.Input<string>;
```


The Topic ARN for notifications to be sent through

<h2 class="pdoc-module-header" id="NotificationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L77">interface NotificationState</a>
</h2>

Input properties used for looking up and filtering Notification resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L81">property groupNames</a>
</h3>

```typescript
groupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of AutoScaling Group Names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L86">property notifications</a>
</h3>

```typescript
notifications?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Notification Types that trigger
notifications. Acceptable values are documented [in the AWS documentation here][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/notification.ts#L90">property topicArn</a>
</h3>

```typescript
topicArn?: pulumi.Input<string>;
```


The Topic ARN for notifications to be sent through

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L184">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L188">property adjustmentType</a>
</h3>

```typescript
adjustmentType?: pulumi.Input<string>;
```


Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L192">property autoscalingGroupName</a>
</h3>

```typescript
autoscalingGroupName: pulumi.Input<string>;
```


The name of the autoscaling group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L196">property cooldown</a>
</h3>

```typescript
cooldown?: pulumi.Input<number>;
```


The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L200">property estimatedInstanceWarmup</a>
</h3>

```typescript
estimatedInstanceWarmup?: pulumi.Input<number>;
```


The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L204">property metricAggregationType</a>
</h3>

```typescript
metricAggregationType?: pulumi.Input<string>;
```


The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L205">property minAdjustmentMagnitude</a>
</h3>

```typescript
minAdjustmentMagnitude?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L209">property minAdjustmentStep</a>
</h3>

```typescript
minAdjustmentStep?: pulumi.Input<number>;
```


Use `min_adjustment_magnitude` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L213">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the dimension.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L217">property policyType</a>
</h3>

```typescript
policyType?: pulumi.Input<string>;
```


The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L223">property scalingAdjustment</a>
</h3>

```typescript
scalingAdjustment?: pulumi.Input<number>;
```


The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L224">property stepAdjustments</a>
</h3>

```typescript
stepAdjustments?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L228">property targetTrackingConfiguration</a>
</h3>

```typescript
targetTrackingConfiguration?: pulumi.Input<{ ... }>;
```


A target tracking policy. These have the following structure:

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L130">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L134">property adjustmentType</a>
</h3>

```typescript
adjustmentType?: pulumi.Input<string>;
```


Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L138">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS to the scaling policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L142">property autoscalingGroupName</a>
</h3>

```typescript
autoscalingGroupName?: pulumi.Input<string>;
```


The name of the autoscaling group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L146">property cooldown</a>
</h3>

```typescript
cooldown?: pulumi.Input<number>;
```


The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L150">property estimatedInstanceWarmup</a>
</h3>

```typescript
estimatedInstanceWarmup?: pulumi.Input<number>;
```


The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L154">property metricAggregationType</a>
</h3>

```typescript
metricAggregationType?: pulumi.Input<string>;
```


The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L155">property minAdjustmentMagnitude</a>
</h3>

```typescript
minAdjustmentMagnitude?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L159">property minAdjustmentStep</a>
</h3>

```typescript
minAdjustmentStep?: pulumi.Input<number>;
```


Use `min_adjustment_magnitude` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L163">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the dimension.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L167">property policyType</a>
</h3>

```typescript
policyType?: pulumi.Input<string>;
```


The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L173">property scalingAdjustment</a>
</h3>

```typescript
scalingAdjustment?: pulumi.Input<number>;
```


The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L174">property stepAdjustments</a>
</h3>

```typescript
stepAdjustments?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/policy.ts#L178">property targetTrackingConfiguration</a>
</h3>

```typescript
targetTrackingConfiguration?: pulumi.Input<{ ... }>;
```


A target tracking policy. These have the following structure:

<h2 class="pdoc-module-header" id="ScheduleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L157">interface ScheduleArgs</a>
</h2>

The set of arguments for constructing a Schedule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L161">property autoscalingGroupName</a>
</h3>

```typescript
autoscalingGroupName: pulumi.Input<string>;
```


The name or Amazon Resource Name (ARN) of the Auto Scaling group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L165">property desiredCapacity</a>
</h3>

```typescript
desiredCapacity?: pulumi.Input<number>;
```


The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L170">property endTime</a>
</h3>

```typescript
endTime?: pulumi.Input<string>;
```


The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L175">property maxSize</a>
</h3>

```typescript
maxSize?: pulumi.Input<number>;
```


The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don't want to change the maximum size at the scheduled time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L180">property minSize</a>
</h3>

```typescript
minSize?: pulumi.Input<number>;
```


The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don't want to change the minimum size at the scheduled time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L184">property recurrence</a>
</h3>

```typescript
recurrence?: pulumi.Input<string>;
```


The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L188">property scheduledActionName</a>
</h3>

```typescript
scheduledActionName: pulumi.Input<string>;
```


The name of this scaling action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L193">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.

<h2 class="pdoc-module-header" id="ScheduleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L111">interface ScheduleState</a>
</h2>

Input properties used for looking up and filtering Schedule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L115">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS to the autoscaling schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L119">property autoscalingGroupName</a>
</h3>

```typescript
autoscalingGroupName?: pulumi.Input<string>;
```


The name or Amazon Resource Name (ARN) of the Auto Scaling group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L123">property desiredCapacity</a>
</h3>

```typescript
desiredCapacity?: pulumi.Input<number>;
```


The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L128">property endTime</a>
</h3>

```typescript
endTime?: pulumi.Input<string>;
```


The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L133">property maxSize</a>
</h3>

```typescript
maxSize?: pulumi.Input<number>;
```


The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don't want to change the maximum size at the scheduled time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L138">property minSize</a>
</h3>

```typescript
minSize?: pulumi.Input<number>;
```


The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don't want to change the minimum size at the scheduled time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L142">property recurrence</a>
</h3>

```typescript
recurrence?: pulumi.Input<string>;
```


The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L146">property scheduledActionName</a>
</h3>

```typescript
scheduledActionName?: pulumi.Input<string>;
```


The name of this scaling action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/autoscaling/schedule.ts#L151">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.

