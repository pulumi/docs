---
title: Module cloudwatch
---

<a href="../index.html">@pulumi/aws</a> &gt; cloudwatch

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Dashboard">class Dashboard</a>
* <a href="#EventPermission">class EventPermission</a>
* <a href="#EventRule">class EventRule</a>
* <a href="#EventRuleEventSubscription">class EventRuleEventSubscription</a>
* <a href="#EventTarget">class EventTarget</a>
* <a href="#LogDestination">class LogDestination</a>
* <a href="#LogDestinationPolicy">class LogDestinationPolicy</a>
* <a href="#LogGroup">class LogGroup</a>
* <a href="#LogGroupEventSubscription">class LogGroupEventSubscription</a>
* <a href="#LogMetricFilter">class LogMetricFilter</a>
* <a href="#LogResourcePolicy">class LogResourcePolicy</a>
* <a href="#LogStream">class LogStream</a>
* <a href="#LogSubscriptionFilter">class LogSubscriptionFilter</a>
* <a href="#MetricAlarm">class MetricAlarm</a>
* <a href="#getLogGroup">function getLogGroup</a>
* <a href="#onSchedule">function onSchedule</a>
* <a href="#DashboardArgs">interface DashboardArgs</a>
* <a href="#DashboardState">interface DashboardState</a>
* <a href="#DecodedLogGroupEvent">interface DecodedLogGroupEvent</a>
* <a href="#EventPermissionArgs">interface EventPermissionArgs</a>
* <a href="#EventPermissionState">interface EventPermissionState</a>
* <a href="#EventRuleArgs">interface EventRuleArgs</a>
* <a href="#EventRuleEvent">interface EventRuleEvent</a>
* <a href="#EventRuleEventSubscriptionArgs">interface EventRuleEventSubscriptionArgs</a>
* <a href="#EventRuleState">interface EventRuleState</a>
* <a href="#EventTargetArgs">interface EventTargetArgs</a>
* <a href="#EventTargetState">interface EventTargetState</a>
* <a href="#GetLogGroupArgs">interface GetLogGroupArgs</a>
* <a href="#GetLogGroupResult">interface GetLogGroupResult</a>
* <a href="#LogDestinationArgs">interface LogDestinationArgs</a>
* <a href="#LogDestinationPolicyArgs">interface LogDestinationPolicyArgs</a>
* <a href="#LogDestinationPolicyState">interface LogDestinationPolicyState</a>
* <a href="#LogDestinationState">interface LogDestinationState</a>
* <a href="#LogGroupArgs">interface LogGroupArgs</a>
* <a href="#LogGroupEvent">interface LogGroupEvent</a>
* <a href="#LogGroupEventRecord">interface LogGroupEventRecord</a>
* <a href="#LogGroupEventSubscriptionArgs">interface LogGroupEventSubscriptionArgs</a>
* <a href="#LogGroupState">interface LogGroupState</a>
* <a href="#LogMetricFilterArgs">interface LogMetricFilterArgs</a>
* <a href="#LogMetricFilterState">interface LogMetricFilterState</a>
* <a href="#LogResourcePolicyArgs">interface LogResourcePolicyArgs</a>
* <a href="#LogResourcePolicyState">interface LogResourcePolicyState</a>
* <a href="#LogStreamArgs">interface LogStreamArgs</a>
* <a href="#LogStreamState">interface LogStreamState</a>
* <a href="#LogSubscriptionFilterArgs">interface LogSubscriptionFilterArgs</a>
* <a href="#LogSubscriptionFilterState">interface LogSubscriptionFilterState</a>
* <a href="#MetricAlarmArgs">interface MetricAlarmArgs</a>
* <a href="#MetricAlarmState">interface MetricAlarmState</a>
* <a href="#EventRuleEventHandler">type EventRuleEventHandler</a>
* <a href="#LogGroupEventHandler">type LogGroupEventHandler</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/cloudwatchMixins.ts">cloudwatch/cloudwatchMixins.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts">cloudwatch/dashboard.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts">cloudwatch/eventPermission.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts">cloudwatch/eventRule.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts">cloudwatch/eventRuleMixins.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts">cloudwatch/eventTarget.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts">cloudwatch/getLogGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts">cloudwatch/logDestination.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts">cloudwatch/logDestinationPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts">cloudwatch/logGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts">cloudwatch/logGroupMixins.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts">cloudwatch/logMetricFilter.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts">cloudwatch/logResourcePolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts">cloudwatch/logStream.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts">cloudwatch/logSubscriptionFilter.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts">cloudwatch/metricAlarm.ts</a> 


<h2 class="pdoc-module-header" id="Dashboard">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L10">class Dashboard</a>
</h2>

Provides a CloudWatch Dashboard resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L34">constructor</a>
</h3>

```typescript
new Dashboard(name: string, args: DashboardArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Dashboard resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DashboardState): Dashboard
```


Get an existing Dashboard resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L26">property dashboardArn</a>
</h3>

```typescript
public dashboardArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the dashboard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L30">property dashboardBody</a>
</h3>

```typescript
public dashboardBody: pulumi.Output<string>;
```


The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L34">property dashboardName</a>
</h3>

```typescript
public dashboardName: pulumi.Output<string>;
```


The name of the dashboard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EventPermission">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L10">class EventPermission</a>
</h2>

Provides a resource to create a CloudWatch Events permission to support cross-account events in the current account default event bus.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L34">constructor</a>
</h3>

```typescript
new EventPermission(name: string, args: EventPermissionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventPermission resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventPermissionState): EventPermission
```


Get an existing EventPermission resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L26">property action</a>
</h3>

```typescript
public action: pulumi.Output<string | undefined>;
```


The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L30">property principal</a>
</h3>

```typescript
public principal: pulumi.Output<string>;
```


The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L34">property statementId</a>
</h3>

```typescript
public statementId: pulumi.Output<string>;
```


An identifier string for the external account that you are granting permissions to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EventRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L10">class EventRule</a>
</h2>

Provides a CloudWatch Event Rule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L57">constructor</a>
</h3>

```typescript
new EventRule(name: string, args?: EventRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventRuleState): EventRule
```


Get an existing EventRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L36">property eventPattern</a>
</h3>

```typescript
public eventPattern: pulumi.Output<string | undefined>;
```


Event pattern
described a JSON object.
See full documentation of [CloudWatch Events and Event Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html) for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L40">property isEnabled</a>
</h3>

```typescript
public isEnabled: pulumi.Output<boolean | undefined>;
```


Whether the rule should be enabled (defaults to `true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The rule's name. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L48">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


The rule's name. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L52">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string | undefined>;
```


The Amazon Resource Name (ARN) associated with the role that is used for target invocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L57">property scheduleExpression</a>
</h3>

```typescript
public scheduleExpression: pulumi.Output<string | undefined>;
```


The scheduling expression.
For example, `cron(0 20 * * ? *)` or `rate(5 minutes)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EventRuleEventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L68">class EventRuleEventSubscription</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L70">constructor</a>
</h3>

```typescript
public new EventRuleEventSubscription(name: string, eventRuleOrSchedule: eventRule.EventRule | string, handler: EventRuleEventHandler, args: EventRuleEventSubscriptionArgs, opts?: pulumi.ResourceOptions)
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L69">property eventRule</a>
</h3>

```typescript
public eventRule: eventRule.EventRule;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L218">property func</a>
</h3>

```typescript
public func: LambdaFunction;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L217">property permission</a>
</h3>

```typescript
public permission: permission.Permission;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L70">property target</a>
</h3>

```typescript
public target: eventTarget.EventTarget;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EventTarget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L10">class EventTarget</a>
</h2>

Provides a CloudWatch Event Target resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L71">constructor</a>
</h3>

```typescript
new EventTarget(name: string, args: EventTargetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventTarget resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventTargetState): EventTarget
```


Get an existing EventTarget resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) associated of the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L30">property batchTarget</a>
</h3>

```typescript
public batchTarget: pulumi.Output<{ ... } | undefined>;
```


Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L34">property ecsTarget</a>
</h3>

```typescript
public ecsTarget: pulumi.Output<{ ... } | undefined>;
```


Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L38">property input</a>
</h3>

```typescript
public input: pulumi.Output<string | undefined>;
```


Valid JSON text passed to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L43">property inputPath</a>
</h3>

```typescript
public inputPath: pulumi.Output<string | undefined>;
```


The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L47">property inputTransformer</a>
</h3>

```typescript
public inputTransformer: pulumi.Output<{ ... } | undefined>;
```


Parameters used when you are providing a custom input to a target based on certain event data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L51">property kinesisTarget</a>
</h3>

```typescript
public kinesisTarget: pulumi.Output<{ ... } | undefined>;
```


Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L55">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string | undefined>;
```


The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L59">property rule</a>
</h3>

```typescript
public rule: pulumi.Output<string>;
```


The name of the rule you want to add targets to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L63">property runCommandTargets</a>
</h3>

```typescript
public runCommandTargets: pulumi.Output<{ ... }[] | undefined>;
```


Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L67">property sqsTarget</a>
</h3>

```typescript
public sqsTarget: pulumi.Output<{ ... } | undefined>;
```


Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L71">property targetId</a>
</h3>

```typescript
public targetId: pulumi.Output<string>;
```


The unique target assignment ID.  If missing, will generate a random, unique id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LogDestination">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L10">class LogDestination</a>
</h2>

Provides a CloudWatch Logs destination resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L38">constructor</a>
</h3>

```typescript
new LogDestination(name: string, args: LogDestinationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogDestination resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogDestinationState): LogDestination
```


Get an existing LogDestination resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) specifying the log destination.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the log destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L34">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L38">property targetArn</a>
</h3>

```typescript
public targetArn: pulumi.Output<string>;
```


The ARN of the target Amazon Kinesis stream or Amazon Lambda resource for the destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LogDestinationPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L10">class LogDestinationPolicy</a>
</h2>

Provides a CloudWatch Logs destination policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L30">constructor</a>
</h3>

```typescript
new LogDestinationPolicy(name: string, args: LogDestinationPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogDestinationPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogDestinationPolicyState): LogDestinationPolicy
```


Get an existing LogDestinationPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L26">property accessPolicy</a>
</h3>

```typescript
public accessPolicy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L30">property destinationName</a>
</h3>

```typescript
public destinationName: pulumi.Output<string>;
```


A name for the subscription filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LogGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L12">class LogGroup</a>
</h2>

Provides a CloudWatch Log Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L51">constructor</a>
</h3>

```typescript
new LogGroup(name: string, args?: LogGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogGroupState): LogGroup
```


Get an existing LogGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) specifying the log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L34">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string | undefined>;
```


The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the log group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L42">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L47">property retentionInDays</a>
</h3>

```typescript
public retentionInDays: pulumi.Output<number | undefined>;
```


Specifies the number of days
you want to retain log events in the specified log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L51">property tags</a>
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

<h2 class="pdoc-module-header" id="LogGroupEventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L71">class LogGroupEventSubscription</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L73">constructor</a>
</h3>

```typescript
new LogGroupEventSubscription(name: string, logGroup: logGroup.LogGroup, handler: LogGroupEventHandler, args: LogGroupEventSubscriptionArgs, opts?: pulumi.ResourceOptions)
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L218">property func</a>
</h3>

```typescript
public func: LambdaFunction;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L72">property logGroup</a>
</h3>

```typescript
public logGroup: pulumi.Output<logGroup.LogGroup>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L73">property logSubscriptionFilter</a>
</h3>

```typescript
public logSubscriptionFilter: logSubscriptionFilter.LogSubscriptionFilter;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L217">property permission</a>
</h3>

```typescript
public permission: permission.Permission;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LogMetricFilter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L10">class LogMetricFilter</a>
</h2>

Provides a CloudWatch Log Metric Filter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L40">constructor</a>
</h3>

```typescript
new LogMetricFilter(name: string, args: LogMetricFilterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogMetricFilter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogMetricFilterState): LogMetricFilter
```


Get an existing LogMetricFilter resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L26">property logGroupName</a>
</h3>

```typescript
public logGroupName: pulumi.Output<string>;
```


The name of the log group to associate the metric filter with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L31">property metricTransformation</a>
</h3>

```typescript
public metricTransformation: pulumi.Output<{ ... }>;
```


A block defining collection of information
needed to define how metric data gets emitted. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the metric filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L40">property pattern</a>
</h3>

```typescript
public pattern: pulumi.Output<string>;
```


A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html)
for extracting metric data out of ingested log events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LogResourcePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L10">class LogResourcePolicy</a>
</h2>

Provides a resource to manage a CloudWatch log resource policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L30">constructor</a>
</h3>

```typescript
new LogResourcePolicy(name: string, args: LogResourcePolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogResourcePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogResourcePolicyState): LogResourcePolicy
```


Get an existing LogResourcePolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L26">property policyDocument</a>
</h3>

```typescript
public policyDocument: pulumi.Output<string>;
```


Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L30">property policyName</a>
</h3>

```typescript
public policyName: pulumi.Output<string>;
```


Name of the resource policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LogStream">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L10">class LogStream</a>
</h2>

Provides a CloudWatch Log Stream resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L34">constructor</a>
</h3>

```typescript
new LogStream(name: string, args: LogStreamArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogStream resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogStreamState): LogStream
```


Get an existing LogStream resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) specifying the log stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L30">property logGroupName</a>
</h3>

```typescript
public logGroupName: pulumi.Output<string>;
```


The name of the log group under which the log stream is to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the log stream. Must not be longer than 512 characters and must not contain `:`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LogSubscriptionFilter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L12">class LogSubscriptionFilter</a>
</h2>

Provides a CloudWatch Logs subscription filter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L48">constructor</a>
</h3>

```typescript
new LogSubscriptionFilter(name: string, args: LogSubscriptionFilterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogSubscriptionFilter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogSubscriptionFilterState): LogSubscriptionFilter
```


Get an existing LogSubscriptionFilter resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L28">property destinationArn</a>
</h3>

```typescript
public destinationArn: pulumi.Output<string>;
```


The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L32">property distribution</a>
</h3>

```typescript
public distribution: pulumi.Output<string | undefined>;
```


The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are "Random" and "ByLogStream".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L36">property filterPattern</a>
</h3>

```typescript
public filterPattern: pulumi.Output<string>;
```


A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L40">property logGroup</a>
</h3>

```typescript
public logGroup: pulumi.Output<LogGroup>;
```


The name of the log group to associate the subscription filter with

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the subscription filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L48">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested log events to the destination. If you use Lambda as a destination, you should skip this argument and use `aws_lambda_permission` resource for granting access from CloudWatch logs to the destination Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MetricAlarm">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L12">class MetricAlarm</a>
</h2>

Provides a CloudWatch Metric Alarm resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L112">constructor</a>
</h3>

```typescript
new MetricAlarm(name: string, args: MetricAlarmArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MetricAlarm resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MetricAlarmState): MetricAlarm
```


Get an existing MetricAlarm resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L28">property actionsEnabled</a>
</h3>

```typescript
public actionsEnabled: pulumi.Output<boolean | undefined>;
```


Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L32">property alarmActions</a>
</h3>

```typescript
public alarmActions: pulumi.Output<string[] | undefined>;
```


The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L36">property alarmDescription</a>
</h3>

```typescript
public alarmDescription: pulumi.Output<string | undefined>;
```


The description for the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L44">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the cloudwatch metric alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L48">property comparisonOperator</a>
</h3>

```typescript
public comparisonOperator: pulumi.Output<string>;
```


The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L52">property datapointsToAlarm</a>
</h3>

```typescript
public datapointsToAlarm: pulumi.Output<number | undefined>;
```


The number of datapoints that must be breaching to trigger the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L56">property dimensions</a>
</h3>

```typescript
public dimensions: pulumi.Output<{ ... } | undefined>;
```


The dimensions for the alarm's associated metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L65">property evaluateLowSampleCountPercentiles</a>
</h3>

```typescript
public evaluateLowSampleCountPercentiles: pulumi.Output<string>;
```


Used only for alarms
based on percentiles. If you specify `ignore`, the alarm state will not
change during periods with too few data points to be statistically significant.
If you specify `evaluate` or omit this parameter, the alarm will always be
evaluated and possibly change state no matter how many data points are available.
The following values are supported: `ignore`, and `evaluate`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L69">property evaluationPeriods</a>
</h3>

```typescript
public evaluationPeriods: pulumi.Output<number>;
```


The number of periods over which data is compared to the specified threshold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L73">property extendedStatistic</a>
</h3>

```typescript
public extendedStatistic: pulumi.Output<string | undefined>;
```


The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L77">property insufficientDataActions</a>
</h3>

```typescript
public insufficientDataActions: pulumi.Output<string[] | undefined>;
```


The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L82">property metricName</a>
</h3>

```typescript
public metricName: pulumi.Output<string>;
```


The name for the alarm's associated metric.
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L40">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The descriptive name for the alarm. This name must be unique within the user's AWS account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L87">property namespace</a>
</h3>

```typescript
public namespace: pulumi.Output<string>;
```


The namespace for the alarm's associated metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L91">property okActions</a>
</h3>

```typescript
public okActions: pulumi.Output<string[] | undefined>;
```


The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L95">property period</a>
</h3>

```typescript
public period: pulumi.Output<number>;
```


The period in seconds over which the specified `statistic` is applied.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L100">property statistic</a>
</h3>

```typescript
public statistic: pulumi.Output<string | undefined>;
```


The statistic to apply to the alarm's associated metric.
Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L104">property threshold</a>
</h3>

```typescript
public threshold: pulumi.Output<number>;
```


The value against which the specified statistic is compared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L108">property treatMissingData</a>
</h3>

```typescript
public treatMissingData: pulumi.Output<string | undefined>;
```


Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L112">property unit</a>
</h3>

```typescript
public unit: pulumi.Output<string | undefined>;
```


The unit for the alarm's associated metric.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getLogGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L10">function getLogGroup</a>
</h2>

```typescript
getLogGroup(args: GetLogGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetLogGroupResult>
```


Use this data source to get information about an AWS Cloudwatch Log Group

<h2 class="pdoc-module-header" id="onSchedule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/cloudwatchMixins.ts#L22">function onSchedule</a>
</h2>

```typescript
onSchedule(name: string, schedule: string, handler: eventRule.EventRuleEventHandler, args?: eventRule.EventRuleEventSubscriptionArgs, opts?: pulumi.ResourceOptions): eventRule.EventRuleEventSubscription
```


Creates a CloudWatch event that will fire based on the specified schedule.  This will create
an EventRule which will then invoke the provided handler every time it fires.

<h2 class="pdoc-module-header" id="DashboardArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L88">interface DashboardArgs</a>
</h2>

The set of arguments for constructing a Dashboard resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L92">property dashboardBody</a>
</h3>

```typescript
dashboardBody: pulumi.Input<string>;
```


The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L96">property dashboardName</a>
</h3>

```typescript
dashboardName: pulumi.Input<string>;
```


The name of the dashboard.

<h2 class="pdoc-module-header" id="DashboardState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L70">interface DashboardState</a>
</h2>

Input properties used for looking up and filtering Dashboard resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L74">property dashboardArn</a>
</h3>

```typescript
dashboardArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the dashboard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L78">property dashboardBody</a>
</h3>

```typescript
dashboardBody?: pulumi.Input<string>;
```


The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L82">property dashboardName</a>
</h3>

```typescript
dashboardName?: pulumi.Input<string>;
```


The name of the dashboard.

<h2 class="pdoc-module-header" id="DecodedLogGroupEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L41">interface DecodedLogGroupEvent</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L60">property logEvents</a>
</h3>

```typescript
logEvents: LogGroupEventRecord[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L46">property logGroup</a>
</h3>

```typescript
logGroup: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L49">property logStream</a>
</h3>

```typescript
logStream: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L56">property messageType</a>
</h3>

```typescript
messageType: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L43">property owner</a>
</h3>

```typescript
owner: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L52">property subscriptionFilters</a>
</h3>

```typescript
subscriptionFilters: string[];
```

<h2 class="pdoc-module-header" id="EventPermissionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L88">interface EventPermissionArgs</a>
</h2>

The set of arguments for constructing a EventPermission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L92">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L96">property principal</a>
</h3>

```typescript
principal: pulumi.Input<string>;
```


The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L100">property statementId</a>
</h3>

```typescript
statementId: pulumi.Input<string>;
```


An identifier string for the external account that you are granting permissions to.

<h2 class="pdoc-module-header" id="EventPermissionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L70">interface EventPermissionState</a>
</h2>

Input properties used for looking up and filtering EventPermission resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L74">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L78">property principal</a>
</h3>

```typescript
principal?: pulumi.Input<string>;
```


The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L82">property statementId</a>
</h3>

```typescript
statementId?: pulumi.Input<string>;
```


An identifier string for the external account that you are granting permissions to.

<h2 class="pdoc-module-header" id="EventRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L138">interface EventRuleArgs</a>
</h2>

The set of arguments for constructing a EventRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L142">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L148">property eventPattern</a>
</h3>

```typescript
eventPattern?: pulumi.Input<string>;
```


Event pattern
described a JSON object.
See full documentation of [CloudWatch Events and Event Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html) for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L152">property isEnabled</a>
</h3>

```typescript
isEnabled?: pulumi.Input<boolean>;
```


Whether the rule should be enabled (defaults to `true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The rule's name. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L160">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The rule's name. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L164">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) associated with the role that is used for target invocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L169">property scheduleExpression</a>
</h3>

```typescript
scheduleExpression?: pulumi.Input<string>;
```


The scheduling expression.
For example, `cron(0 20 * * ? *)` or `rate(5 minutes)`.

<h2 class="pdoc-module-header" id="EventRuleEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L27">interface EventRuleEvent</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L32">property account</a>
</h3>

```typescript
account: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L63">property detail</a>
</h3>

```typescript
detail: Record<string, any>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L39">property detail-type</a>
</h3>

```typescript
detail-type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L53">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L35">property region</a>
</h3>

```typescript
region: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L60">property resources</a>
</h3>

```typescript
resources: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L44">property source</a>
</h3>

```typescript
source: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L49">property time</a>
</h3>

```typescript
time: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L29">property version</a>
</h3>

```typescript
version: string;
```

<h2 class="pdoc-module-header" id="EventRuleEventSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L24">interface EventRuleEventSubscriptionArgs</a>
</h2>

Arguments to control the event rule subscription.  Currently empty, but still defined in case of
future need.

<h2 class="pdoc-module-header" id="EventRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L97">interface EventRuleState</a>
</h2>

Input properties used for looking up and filtering EventRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L101">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L105">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L111">property eventPattern</a>
</h3>

```typescript
eventPattern?: pulumi.Input<string>;
```


Event pattern
described a JSON object.
See full documentation of [CloudWatch Events and Event Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html) for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L115">property isEnabled</a>
</h3>

```typescript
isEnabled?: pulumi.Input<boolean>;
```


Whether the rule should be enabled (defaults to `true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The rule's name. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L123">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The rule's name. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L127">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) associated with the role that is used for target invocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L132">property scheduleExpression</a>
</h3>

```typescript
scheduleExpression?: pulumi.Input<string>;
```


The scheduling expression.
For example, `cron(0 20 * * ? *)` or `rate(5 minutes)`.

<h2 class="pdoc-module-header" id="EventTargetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L180">interface EventTargetArgs</a>
</h2>

The set of arguments for constructing a EventTarget resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L184">property arn</a>
</h3>

```typescript
arn: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) associated of the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L188">property batchTarget</a>
</h3>

```typescript
batchTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L192">property ecsTarget</a>
</h3>

```typescript
ecsTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L196">property input</a>
</h3>

```typescript
input?: pulumi.Input<string>;
```


Valid JSON text passed to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L201">property inputPath</a>
</h3>

```typescript
inputPath?: pulumi.Input<string>;
```


The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L205">property inputTransformer</a>
</h3>

```typescript
inputTransformer?: pulumi.Input<{ ... }>;
```


Parameters used when you are providing a custom input to a target based on certain event data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L209">property kinesisTarget</a>
</h3>

```typescript
kinesisTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L213">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L217">property rule</a>
</h3>

```typescript
rule: pulumi.Input<string>;
```


The name of the rule you want to add targets to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L221">property runCommandTargets</a>
</h3>

```typescript
runCommandTargets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L225">property sqsTarget</a>
</h3>

```typescript
sqsTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L229">property targetId</a>
</h3>

```typescript
targetId?: pulumi.Input<string>;
```


The unique target assignment ID.  If missing, will generate a random, unique id.

<h2 class="pdoc-module-header" id="EventTargetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L125">interface EventTargetState</a>
</h2>

Input properties used for looking up and filtering EventTarget resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L129">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) associated of the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L133">property batchTarget</a>
</h3>

```typescript
batchTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L137">property ecsTarget</a>
</h3>

```typescript
ecsTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L141">property input</a>
</h3>

```typescript
input?: pulumi.Input<string>;
```


Valid JSON text passed to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L146">property inputPath</a>
</h3>

```typescript
inputPath?: pulumi.Input<string>;
```


The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L150">property inputTransformer</a>
</h3>

```typescript
inputTransformer?: pulumi.Input<{ ... }>;
```


Parameters used when you are providing a custom input to a target based on certain event data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L154">property kinesisTarget</a>
</h3>

```typescript
kinesisTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L158">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L162">property rule</a>
</h3>

```typescript
rule?: pulumi.Input<string>;
```


The name of the rule you want to add targets to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L166">property runCommandTargets</a>
</h3>

```typescript
runCommandTargets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L170">property sqsTarget</a>
</h3>

```typescript
sqsTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L174">property targetId</a>
</h3>

```typescript
targetId?: pulumi.Input<string>;
```


The unique target assignment ID.  If missing, will generate a random, unique id.

<h2 class="pdoc-module-header" id="GetLogGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L19">interface GetLogGroupArgs</a>
</h2>

A collection of arguments for invoking getLogGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


The name of the Cloudwatch log group

<h2 class="pdoc-module-header" id="GetLogGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L29">interface GetLogGroupResult</a>
</h2>

A collection of values returned by getLogGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L33">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the Cloudwatch log group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L37">property creationTime</a>
</h3>

```typescript
creationTime: number;
```


The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L41">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="LogDestinationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L98">interface LogDestinationArgs</a>
</h2>

The set of arguments for constructing a LogDestination resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L102">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the log destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L106">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L110">property targetArn</a>
</h3>

```typescript
targetArn: pulumi.Input<string>;
```


The ARN of the target Amazon Kinesis stream or Amazon Lambda resource for the destination

<h2 class="pdoc-module-header" id="LogDestinationPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L78">interface LogDestinationPolicyArgs</a>
</h2>

The set of arguments for constructing a LogDestinationPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L82">property accessPolicy</a>
</h3>

```typescript
accessPolicy: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L86">property destinationName</a>
</h3>

```typescript
destinationName: pulumi.Input<string>;
```


A name for the subscription filter

<h2 class="pdoc-module-header" id="LogDestinationPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L64">interface LogDestinationPolicyState</a>
</h2>

Input properties used for looking up and filtering LogDestinationPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L68">property accessPolicy</a>
</h3>

```typescript
accessPolicy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L72">property destinationName</a>
</h3>

```typescript
destinationName?: pulumi.Input<string>;
```


A name for the subscription filter

<h2 class="pdoc-module-header" id="LogDestinationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L76">interface LogDestinationState</a>
</h2>

Input properties used for looking up and filtering LogDestination resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L80">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the log destination.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the log destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L88">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L92">property targetArn</a>
</h3>

```typescript
targetArn?: pulumi.Input<string>;
```


The ARN of the target Amazon Kinesis stream or Amazon Lambda resource for the destination

<h2 class="pdoc-module-header" id="LogGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L120">interface LogGroupArgs</a>
</h2>

The set of arguments for constructing a LogGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L126">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the log group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L134">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L139">property retentionInDays</a>
</h3>

```typescript
retentionInDays?: pulumi.Input<number>;
```


Specifies the number of days
you want to retain log events in the specified log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L143">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LogGroupEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L33">interface LogGroupEvent</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L34">property awslogs</a>
</h3>

```typescript
awslogs: { ... };
```

<h2 class="pdoc-module-header" id="LogGroupEventRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L63">interface LogGroupEventRecord</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L64">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L66">property message</a>
</h3>

```typescript
message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L65">property timestamp</a>
</h3>

```typescript
timestamp: number;
```

<h2 class="pdoc-module-header" id="LogGroupEventSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L25">interface LogGroupEventSubscriptionArgs</a>
</h2>

Arguments to control the event rule subscription.  Currently empty, but still defined in case of
future need.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L30">property filterPattern</a>
</h3>

```typescript
filterPattern?: string;
```


A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.
If not provided, the empty-string pattern will be used.

<h2 class="pdoc-module-header" id="LogGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L87">interface LogGroupState</a>
</h2>

Input properties used for looking up and filtering LogGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L91">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L97">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the log group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L105">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L110">property retentionInDays</a>
</h3>

```typescript
retentionInDays?: pulumi.Input<number>;
```


Specifies the number of days
you want to retain log events in the specified log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L114">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LogMetricFilterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L105">interface LogMetricFilterArgs</a>
</h2>

The set of arguments for constructing a LogMetricFilter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L109">property logGroupName</a>
</h3>

```typescript
logGroupName: pulumi.Input<string>;
```


The name of the log group to associate the metric filter with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L114">property metricTransformation</a>
</h3>

```typescript
metricTransformation: pulumi.Input<{ ... }>;
```


A block defining collection of information
needed to define how metric data gets emitted. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the metric filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L123">property pattern</a>
</h3>

```typescript
pattern: pulumi.Input<string>;
```


A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html)
for extracting metric data out of ingested log events.

<h2 class="pdoc-module-header" id="LogMetricFilterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L81">interface LogMetricFilterState</a>
</h2>

Input properties used for looking up and filtering LogMetricFilter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L85">property logGroupName</a>
</h3>

```typescript
logGroupName?: pulumi.Input<string>;
```


The name of the log group to associate the metric filter with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L90">property metricTransformation</a>
</h3>

```typescript
metricTransformation?: pulumi.Input<{ ... }>;
```


A block defining collection of information
needed to define how metric data gets emitted. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the metric filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L99">property pattern</a>
</h3>

```typescript
pattern?: pulumi.Input<string>;
```


A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html)
for extracting metric data out of ingested log events.

<h2 class="pdoc-module-header" id="LogResourcePolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L78">interface LogResourcePolicyArgs</a>
</h2>

The set of arguments for constructing a LogResourcePolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L82">property policyDocument</a>
</h3>

```typescript
policyDocument: pulumi.Input<string>;
```


Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L86">property policyName</a>
</h3>

```typescript
policyName: pulumi.Input<string>;
```


Name of the resource policy.

<h2 class="pdoc-module-header" id="LogResourcePolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L64">interface LogResourcePolicyState</a>
</h2>

Input properties used for looking up and filtering LogResourcePolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L68">property policyDocument</a>
</h3>

```typescript
policyDocument?: pulumi.Input<string>;
```


Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L72">property policyName</a>
</h3>

```typescript
policyName?: pulumi.Input<string>;
```


Name of the resource policy.

<h2 class="pdoc-module-header" id="LogStreamArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L85">interface LogStreamArgs</a>
</h2>

The set of arguments for constructing a LogStream resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L89">property logGroupName</a>
</h3>

```typescript
logGroupName: pulumi.Input<string>;
```


The name of the log group under which the log stream is to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the log stream. Must not be longer than 512 characters and must not contain `:`

<h2 class="pdoc-module-header" id="LogStreamState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L67">interface LogStreamState</a>
</h2>

Input properties used for looking up and filtering LogStream resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L71">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the log stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L75">property logGroupName</a>
</h3>

```typescript
logGroupName?: pulumi.Input<string>;
```


The name of the log group under which the log stream is to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the log stream. Must not be longer than 512 characters and must not contain `:`

<h2 class="pdoc-module-header" id="LogSubscriptionFilterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L123">interface LogSubscriptionFilterArgs</a>
</h2>

The set of arguments for constructing a LogSubscriptionFilter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L127">property destinationArn</a>
</h3>

```typescript
destinationArn: pulumi.Input<string>;
```


The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L131">property distribution</a>
</h3>

```typescript
distribution?: pulumi.Input<string>;
```


The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are "Random" and "ByLogStream".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L135">property filterPattern</a>
</h3>

```typescript
filterPattern: pulumi.Input<string>;
```


A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L139">property logGroup</a>
</h3>

```typescript
logGroup: pulumi.Input<LogGroup>;
```


The name of the log group to associate the subscription filter with

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L143">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the subscription filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L147">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested log events to the destination. If you use Lambda as a destination, you should skip this argument and use `aws_lambda_permission` resource for granting access from CloudWatch logs to the destination Lambda function.

<h2 class="pdoc-module-header" id="LogSubscriptionFilterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L93">interface LogSubscriptionFilterState</a>
</h2>

Input properties used for looking up and filtering LogSubscriptionFilter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L97">property destinationArn</a>
</h3>

```typescript
destinationArn?: pulumi.Input<string>;
```


The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L101">property distribution</a>
</h3>

```typescript
distribution?: pulumi.Input<string>;
```


The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are "Random" and "ByLogStream".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L105">property filterPattern</a>
</h3>

```typescript
filterPattern?: pulumi.Input<string>;
```


A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L109">property logGroup</a>
</h3>

```typescript
logGroup?: pulumi.Input<LogGroup>;
```


The name of the log group to associate the subscription filter with

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the subscription filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L117">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested log events to the destination. If you use Lambda as a destination, you should skip this argument and use `aws_lambda_permission` resource for granting access from CloudWatch logs to the destination Lambda function.

<h2 class="pdoc-module-header" id="MetricAlarmArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L288">interface MetricAlarmArgs</a>
</h2>

The set of arguments for constructing a MetricAlarm resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L292">property actionsEnabled</a>
</h3>

```typescript
actionsEnabled?: pulumi.Input<boolean>;
```


Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L296">property alarmActions</a>
</h3>

```typescript
alarmActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L300">property alarmDescription</a>
</h3>

```typescript
alarmDescription?: pulumi.Input<string>;
```


The description for the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L308">property comparisonOperator</a>
</h3>

```typescript
comparisonOperator: pulumi.Input<string>;
```


The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L312">property datapointsToAlarm</a>
</h3>

```typescript
datapointsToAlarm?: pulumi.Input<number>;
```


The number of datapoints that must be breaching to trigger the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L316">property dimensions</a>
</h3>

```typescript
dimensions?: pulumi.Input<{ ... }>;
```


The dimensions for the alarm's associated metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L325">property evaluateLowSampleCountPercentiles</a>
</h3>

```typescript
evaluateLowSampleCountPercentiles?: pulumi.Input<string>;
```


Used only for alarms
based on percentiles. If you specify `ignore`, the alarm state will not
change during periods with too few data points to be statistically significant.
If you specify `evaluate` or omit this parameter, the alarm will always be
evaluated and possibly change state no matter how many data points are available.
The following values are supported: `ignore`, and `evaluate`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L329">property evaluationPeriods</a>
</h3>

```typescript
evaluationPeriods: pulumi.Input<number>;
```


The number of periods over which data is compared to the specified threshold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L333">property extendedStatistic</a>
</h3>

```typescript
extendedStatistic?: pulumi.Input<string>;
```


The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L337">property insufficientDataActions</a>
</h3>

```typescript
insufficientDataActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L342">property metricName</a>
</h3>

```typescript
metricName: pulumi.Input<string>;
```


The name for the alarm's associated metric.
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L304">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The descriptive name for the alarm. This name must be unique within the user's AWS account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L347">property namespace</a>
</h3>

```typescript
namespace: pulumi.Input<string>;
```


The namespace for the alarm's associated metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L351">property okActions</a>
</h3>

```typescript
okActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L355">property period</a>
</h3>

```typescript
period: pulumi.Input<number>;
```


The period in seconds over which the specified `statistic` is applied.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L360">property statistic</a>
</h3>

```typescript
statistic?: pulumi.Input<string>;
```


The statistic to apply to the alarm's associated metric.
Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L364">property threshold</a>
</h3>

```typescript
threshold: pulumi.Input<number>;
```


The value against which the specified statistic is compared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L368">property treatMissingData</a>
</h3>

```typescript
treatMissingData?: pulumi.Input<string>;
```


Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L372">property unit</a>
</h3>

```typescript
unit?: pulumi.Input<string>;
```


The unit for the alarm's associated metric.

<h2 class="pdoc-module-header" id="MetricAlarmState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L194">interface MetricAlarmState</a>
</h2>

Input properties used for looking up and filtering MetricAlarm resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L198">property actionsEnabled</a>
</h3>

```typescript
actionsEnabled?: pulumi.Input<boolean>;
```


Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L202">property alarmActions</a>
</h3>

```typescript
alarmActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L206">property alarmDescription</a>
</h3>

```typescript
alarmDescription?: pulumi.Input<string>;
```


The description for the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L214">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the cloudwatch metric alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L218">property comparisonOperator</a>
</h3>

```typescript
comparisonOperator?: pulumi.Input<string>;
```


The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L222">property datapointsToAlarm</a>
</h3>

```typescript
datapointsToAlarm?: pulumi.Input<number>;
```


The number of datapoints that must be breaching to trigger the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L226">property dimensions</a>
</h3>

```typescript
dimensions?: pulumi.Input<{ ... }>;
```


The dimensions for the alarm's associated metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L235">property evaluateLowSampleCountPercentiles</a>
</h3>

```typescript
evaluateLowSampleCountPercentiles?: pulumi.Input<string>;
```


Used only for alarms
based on percentiles. If you specify `ignore`, the alarm state will not
change during periods with too few data points to be statistically significant.
If you specify `evaluate` or omit this parameter, the alarm will always be
evaluated and possibly change state no matter how many data points are available.
The following values are supported: `ignore`, and `evaluate`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L239">property evaluationPeriods</a>
</h3>

```typescript
evaluationPeriods?: pulumi.Input<number>;
```


The number of periods over which data is compared to the specified threshold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L243">property extendedStatistic</a>
</h3>

```typescript
extendedStatistic?: pulumi.Input<string>;
```


The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L247">property insufficientDataActions</a>
</h3>

```typescript
insufficientDataActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L252">property metricName</a>
</h3>

```typescript
metricName?: pulumi.Input<string>;
```


The name for the alarm's associated metric.
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L210">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The descriptive name for the alarm. This name must be unique within the user's AWS account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L257">property namespace</a>
</h3>

```typescript
namespace?: pulumi.Input<string>;
```


The namespace for the alarm's associated metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L261">property okActions</a>
</h3>

```typescript
okActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L265">property period</a>
</h3>

```typescript
period?: pulumi.Input<number>;
```


The period in seconds over which the specified `statistic` is applied.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L270">property statistic</a>
</h3>

```typescript
statistic?: pulumi.Input<string>;
```


The statistic to apply to the alarm's associated metric.
Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L274">property threshold</a>
</h3>

```typescript
threshold?: pulumi.Input<number>;
```


The value against which the specified statistic is compared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L278">property treatMissingData</a>
</h3>

```typescript
treatMissingData?: pulumi.Input<string>;
```


Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L282">property unit</a>
</h3>

```typescript
unit?: pulumi.Input<string>;
```


The unit for the alarm's associated metric.

<h2 class="pdoc-module-header" id="EventRuleEventHandler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts#L66">type EventRuleEventHandler</a>
</h2>

```typescript
type EventRuleEventHandler = lambda.EventHandler<EventRuleEvent, void>;
```

<h2 class="pdoc-module-header" id="LogGroupEventHandler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts#L69">type LogGroupEventHandler</a>
</h2>

```typescript
type LogGroupEventHandler = lambda.EventHandler<LogGroupEvent, void>;
```

