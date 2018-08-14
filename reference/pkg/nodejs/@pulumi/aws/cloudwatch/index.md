---
title: Module cloudwatch
---

<a href="../index.html">@pulumi/aws</a> &gt; cloudwatch

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Dashboard">class Dashboard</a>
* <a href="#EventPermission">class EventPermission</a>
* <a href="#EventRule">class EventRule</a>
* <a href="#EventTarget">class EventTarget</a>
* <a href="#LogDestination">class LogDestination</a>
* <a href="#LogDestinationPolicy">class LogDestinationPolicy</a>
* <a href="#LogGroup">class LogGroup</a>
* <a href="#LogMetricFilter">class LogMetricFilter</a>
* <a href="#LogResourcePolicy">class LogResourcePolicy</a>
* <a href="#LogStream">class LogStream</a>
* <a href="#LogSubscriptionFilter">class LogSubscriptionFilter</a>
* <a href="#MetricAlarm">class MetricAlarm</a>
* <a href="#getLogGroup">function getLogGroup</a>
* <a href="#DashboardArgs">interface DashboardArgs</a>
* <a href="#DashboardState">interface DashboardState</a>
* <a href="#EventPermissionArgs">interface EventPermissionArgs</a>
* <a href="#EventPermissionState">interface EventPermissionState</a>
* <a href="#EventRuleArgs">interface EventRuleArgs</a>
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

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts">cloudwatch/dashboard.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts">cloudwatch/eventPermission.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts">cloudwatch/eventRule.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts">cloudwatch/eventTarget.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts">cloudwatch/getLogGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts">cloudwatch/logDestination.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts">cloudwatch/logDestinationPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts">cloudwatch/logGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts">cloudwatch/logMetricFilter.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts">cloudwatch/logResourcePolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts">cloudwatch/logStream.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts">cloudwatch/logSubscriptionFilter.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts">cloudwatch/metricAlarm.ts</a> 


<h2 class="pdoc-module-header" id="Dashboard">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L9">class Dashboard</a>
</h2>

Provides a CloudWatch Dashboard resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L33">constructor</a>
</h3>

```typescript
new Dashboard(name: string, args: DashboardArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Dashboard resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L25">property dashboardArn</a>
</h3>

```typescript
public dashboardArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the dashboard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L29">property dashboardBody</a>
</h3>

```typescript
public dashboardBody: pulumi.Output<string>;
```


The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L33">property dashboardName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L9">class EventPermission</a>
</h2>

Provides a resource to create a CloudWatch Events permission to support cross-account events in the current account default event bus.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L33">constructor</a>
</h3>

```typescript
new EventPermission(name: string, args: EventPermissionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventPermission resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L25">property action</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L29">property principal</a>
</h3>

```typescript
public principal: pulumi.Output<string>;
```


The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L33">property statementId</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L9">class EventRule</a>
</h2>

Provides a CloudWatch Event Rule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L56">constructor</a>
</h3>

```typescript
new EventRule(name: string, args?: EventRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L35">property eventPattern</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L39">property isEnabled</a>
</h3>

```typescript
public isEnabled: pulumi.Output<boolean | undefined>;
```


Whether the rule should be enabled (defaults to `true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The rule's name. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L47">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


The rule's name. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L51">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string | undefined>;
```


The Amazon Resource Name (ARN) associated with the role that is used for target invocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L56">property scheduleExpression</a>
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

<h2 class="pdoc-module-header" id="EventTarget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L9">class EventTarget</a>
</h2>

Provides a CloudWatch Event Target resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L70">constructor</a>
</h3>

```typescript
new EventTarget(name: string, args: EventTargetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventTarget resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) associated of the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L29">property batchTarget</a>
</h3>

```typescript
public batchTarget: pulumi.Output<{ ... } | undefined>;
```


Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L33">property ecsTarget</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L37">property input</a>
</h3>

```typescript
public input: pulumi.Output<string | undefined>;
```


Valid JSON text passed to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L42">property inputPath</a>
</h3>

```typescript
public inputPath: pulumi.Output<string | undefined>;
```


The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L46">property inputTransformer</a>
</h3>

```typescript
public inputTransformer: pulumi.Output<{ ... } | undefined>;
```


Parameters used when you are providing a custom input to a target based on certain event data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L50">property kinesisTarget</a>
</h3>

```typescript
public kinesisTarget: pulumi.Output<{ ... } | undefined>;
```


Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L54">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string | undefined>;
```


The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L58">property rule</a>
</h3>

```typescript
public rule: pulumi.Output<string>;
```


The name of the rule you want to add targets to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L62">property runCommandTargets</a>
</h3>

```typescript
public runCommandTargets: pulumi.Output<{ ... }[] | undefined>;
```


Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L66">property sqsTarget</a>
</h3>

```typescript
public sqsTarget: pulumi.Output<{ ... } | undefined>;
```


Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L70">property targetId</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L9">class LogDestination</a>
</h2>

Provides a CloudWatch Logs destination resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L37">constructor</a>
</h3>

```typescript
new LogDestination(name: string, args: LogDestinationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogDestination resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L25">property arn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the log destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L33">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L37">property targetArn</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L9">class LogDestinationPolicy</a>
</h2>

Provides a CloudWatch Logs destination policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L29">constructor</a>
</h3>

```typescript
new LogDestinationPolicy(name: string, args: LogDestinationPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogDestinationPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L25">property accessPolicy</a>
</h3>

```typescript
public accessPolicy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L29">property destinationName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L11">class LogGroup</a>
</h2>

Provides a CloudWatch Log Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L50">constructor</a>
</h3>

```typescript
new LogGroup(name: string, args?: LogGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L27">property arn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L33">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string | undefined>;
```


The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the log group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L41">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L46">property retentionInDays</a>
</h3>

```typescript
public retentionInDays: pulumi.Output<number | undefined>;
```


Specifies the number of days
you want to retain log events in the specified log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L50">property tags</a>
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

<h2 class="pdoc-module-header" id="LogMetricFilter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L9">class LogMetricFilter</a>
</h2>

Provides a CloudWatch Log Metric Filter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L39">constructor</a>
</h3>

```typescript
new LogMetricFilter(name: string, args: LogMetricFilterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogMetricFilter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L25">property logGroupName</a>
</h3>

```typescript
public logGroupName: pulumi.Output<string>;
```


The name of the log group to associate the metric filter with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L30">property metricTransformation</a>
</h3>

```typescript
public metricTransformation: pulumi.Output<{ ... }>;
```


A block defining collection of information
needed to define how metric data gets emitted. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the CloudWatch metric to which the monitored log information should be published (e.g. `ErrorCount`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L39">property pattern</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L9">class LogResourcePolicy</a>
</h2>

Provides a resource to manage a CloudWatch log resource policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L29">constructor</a>
</h3>

```typescript
new LogResourcePolicy(name: string, args: LogResourcePolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogResourcePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L25">property policyDocument</a>
</h3>

```typescript
public policyDocument: pulumi.Output<string>;
```


Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L29">property policyName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L9">class LogStream</a>
</h2>

Provides a CloudWatch Log Stream resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L33">constructor</a>
</h3>

```typescript
new LogStream(name: string, args: LogStreamArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogStream resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L25">property arn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L29">property logGroupName</a>
</h3>

```typescript
public logGroupName: pulumi.Output<string>;
```


The name of the log group under which the log stream is to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L33">property name</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L11">class LogSubscriptionFilter</a>
</h2>

Provides a CloudWatch Logs subscription filter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L47">constructor</a>
</h3>

```typescript
new LogSubscriptionFilter(name: string, args: LogSubscriptionFilterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogSubscriptionFilter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L27">property destinationArn</a>
</h3>

```typescript
public destinationArn: pulumi.Output<string>;
```


The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L31">property distribution</a>
</h3>

```typescript
public distribution: pulumi.Output<string | undefined>;
```


The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are "Random" and "ByLogStream".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L35">property filterPattern</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L39">property logGroup</a>
</h3>

```typescript
public logGroup: pulumi.Output<LogGroup>;
```


The name of the log group to associate the subscription filter with

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the subscription filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L47">property roleArn</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L11">class MetricAlarm</a>
</h2>

Provides a CloudWatch Metric Alarm resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L107">constructor</a>
</h3>

```typescript
new MetricAlarm(name: string, args: MetricAlarmArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MetricAlarm resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L27">property actionsEnabled</a>
</h3>

```typescript
public actionsEnabled: pulumi.Output<boolean | undefined>;
```


Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L31">property alarmActions</a>
</h3>

```typescript
public alarmActions: pulumi.Output<string[] | undefined>;
```


The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L35">property alarmDescription</a>
</h3>

```typescript
public alarmDescription: pulumi.Output<string | undefined>;
```


The description for the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L43">property comparisonOperator</a>
</h3>

```typescript
public comparisonOperator: pulumi.Output<string>;
```


The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L47">property datapointsToAlarm</a>
</h3>

```typescript
public datapointsToAlarm: pulumi.Output<number | undefined>;
```


The number of datapoints that must be breaching to trigger the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L51">property dimensions</a>
</h3>

```typescript
public dimensions: pulumi.Output<{ ... } | undefined>;
```


The dimensions for the alarm's associated metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L60">property evaluateLowSampleCountPercentiles</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L64">property evaluationPeriods</a>
</h3>

```typescript
public evaluationPeriods: pulumi.Output<number>;
```


The number of periods over which data is compared to the specified threshold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L68">property extendedStatistic</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L72">property insufficientDataActions</a>
</h3>

```typescript
public insufficientDataActions: pulumi.Output<string[] | undefined>;
```


The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L77">property metricName</a>
</h3>

```typescript
public metricName: pulumi.Output<string>;
```


The name for the alarm's associated metric.
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The descriptive name for the alarm. This name must be unique within the user's AWS account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L82">property namespace</a>
</h3>

```typescript
public namespace: pulumi.Output<string>;
```


The namespace for the alarm's associated metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L86">property okActions</a>
</h3>

```typescript
public okActions: pulumi.Output<string[] | undefined>;
```


The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L90">property period</a>
</h3>

```typescript
public period: pulumi.Output<number>;
```


The period in seconds over which the specified `statistic` is applied.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L95">property statistic</a>
</h3>

```typescript
public statistic: pulumi.Output<string | undefined>;
```


The statistic to apply to the alarm's associated metric.
Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L99">property threshold</a>
</h3>

```typescript
public threshold: pulumi.Output<number>;
```


The value against which the specified statistic is compared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L103">property treatMissingData</a>
</h3>

```typescript
public treatMissingData: pulumi.Output<string | undefined>;
```


Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L107">property unit</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L9">function getLogGroup</a>
</h2>

```typescript
getLogGroup(args: GetLogGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetLogGroupResult>
```


Use this data source to get information about an AWS Cloudwatch Log Group

<h2 class="pdoc-module-header" id="DashboardArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L87">interface DashboardArgs</a>
</h2>

The set of arguments for constructing a Dashboard resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L91">property dashboardBody</a>
</h3>

```typescript
dashboardBody: pulumi.Input<string>;
```


The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L95">property dashboardName</a>
</h3>

```typescript
dashboardName: pulumi.Input<string>;
```


The name of the dashboard.

<h2 class="pdoc-module-header" id="DashboardState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L69">interface DashboardState</a>
</h2>

Input properties used for looking up and filtering Dashboard resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L73">property dashboardArn</a>
</h3>

```typescript
dashboardArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the dashboard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L77">property dashboardBody</a>
</h3>

```typescript
dashboardBody?: pulumi.Input<string>;
```


The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/dashboard.ts#L81">property dashboardName</a>
</h3>

```typescript
dashboardName?: pulumi.Input<string>;
```


The name of the dashboard.

<h2 class="pdoc-module-header" id="EventPermissionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L87">interface EventPermissionArgs</a>
</h2>

The set of arguments for constructing a EventPermission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L91">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L95">property principal</a>
</h3>

```typescript
principal: pulumi.Input<string>;
```


The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L99">property statementId</a>
</h3>

```typescript
statementId: pulumi.Input<string>;
```


An identifier string for the external account that you are granting permissions to.

<h2 class="pdoc-module-header" id="EventPermissionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L69">interface EventPermissionState</a>
</h2>

Input properties used for looking up and filtering EventPermission resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L73">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L77">property principal</a>
</h3>

```typescript
principal?: pulumi.Input<string>;
```


The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventPermission.ts#L81">property statementId</a>
</h3>

```typescript
statementId?: pulumi.Input<string>;
```


An identifier string for the external account that you are granting permissions to.

<h2 class="pdoc-module-header" id="EventRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L137">interface EventRuleArgs</a>
</h2>

The set of arguments for constructing a EventRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L141">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L147">property eventPattern</a>
</h3>

```typescript
eventPattern?: pulumi.Input<string>;
```


Event pattern
described a JSON object.
See full documentation of [CloudWatch Events and Event Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html) for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L151">property isEnabled</a>
</h3>

```typescript
isEnabled?: pulumi.Input<boolean>;
```


Whether the rule should be enabled (defaults to `true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L155">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The rule's name. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L159">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The rule's name. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L163">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) associated with the role that is used for target invocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L168">property scheduleExpression</a>
</h3>

```typescript
scheduleExpression?: pulumi.Input<string>;
```


The scheduling expression.
For example, `cron(0 20 * * ? *)` or `rate(5 minutes)`.

<h2 class="pdoc-module-header" id="EventRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L96">interface EventRuleState</a>
</h2>

Input properties used for looking up and filtering EventRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L100">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L104">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L110">property eventPattern</a>
</h3>

```typescript
eventPattern?: pulumi.Input<string>;
```


Event pattern
described a JSON object.
See full documentation of [CloudWatch Events and Event Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html) for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L114">property isEnabled</a>
</h3>

```typescript
isEnabled?: pulumi.Input<boolean>;
```


Whether the rule should be enabled (defaults to `true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The rule's name. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L122">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The rule's name. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L126">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) associated with the role that is used for target invocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRule.ts#L131">property scheduleExpression</a>
</h3>

```typescript
scheduleExpression?: pulumi.Input<string>;
```


The scheduling expression.
For example, `cron(0 20 * * ? *)` or `rate(5 minutes)`.

<h2 class="pdoc-module-header" id="EventTargetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L179">interface EventTargetArgs</a>
</h2>

The set of arguments for constructing a EventTarget resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L183">property arn</a>
</h3>

```typescript
arn: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) associated of the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L187">property batchTarget</a>
</h3>

```typescript
batchTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L191">property ecsTarget</a>
</h3>

```typescript
ecsTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L195">property input</a>
</h3>

```typescript
input?: pulumi.Input<string>;
```


Valid JSON text passed to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L200">property inputPath</a>
</h3>

```typescript
inputPath?: pulumi.Input<string>;
```


The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L204">property inputTransformer</a>
</h3>

```typescript
inputTransformer?: pulumi.Input<{ ... }>;
```


Parameters used when you are providing a custom input to a target based on certain event data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L208">property kinesisTarget</a>
</h3>

```typescript
kinesisTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L212">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L216">property rule</a>
</h3>

```typescript
rule: pulumi.Input<string>;
```


The name of the rule you want to add targets to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L220">property runCommandTargets</a>
</h3>

```typescript
runCommandTargets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L224">property sqsTarget</a>
</h3>

```typescript
sqsTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L228">property targetId</a>
</h3>

```typescript
targetId?: pulumi.Input<string>;
```


The unique target assignment ID.  If missing, will generate a random, unique id.

<h2 class="pdoc-module-header" id="EventTargetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L124">interface EventTargetState</a>
</h2>

Input properties used for looking up and filtering EventTarget resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L128">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) associated of the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L132">property batchTarget</a>
</h3>

```typescript
batchTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L136">property ecsTarget</a>
</h3>

```typescript
ecsTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L140">property input</a>
</h3>

```typescript
input?: pulumi.Input<string>;
```


Valid JSON text passed to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L145">property inputPath</a>
</h3>

```typescript
inputPath?: pulumi.Input<string>;
```


The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L149">property inputTransformer</a>
</h3>

```typescript
inputTransformer?: pulumi.Input<{ ... }>;
```


Parameters used when you are providing a custom input to a target based on certain event data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L153">property kinesisTarget</a>
</h3>

```typescript
kinesisTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L157">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L161">property rule</a>
</h3>

```typescript
rule?: pulumi.Input<string>;
```


The name of the rule you want to add targets to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L165">property runCommandTargets</a>
</h3>

```typescript
runCommandTargets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L169">property sqsTarget</a>
</h3>

```typescript
sqsTarget?: pulumi.Input<{ ... }>;
```


Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventTarget.ts#L173">property targetId</a>
</h3>

```typescript
targetId?: pulumi.Input<string>;
```


The unique target assignment ID.  If missing, will generate a random, unique id.

<h2 class="pdoc-module-header" id="GetLogGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L18">interface GetLogGroupArgs</a>
</h2>

A collection of arguments for invoking getLogGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L22">property name</a>
</h3>

```typescript
name: string;
```


The name of the Cloudwatch log group

<h2 class="pdoc-module-header" id="GetLogGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L28">interface GetLogGroupResult</a>
</h2>

A collection of values returned by getLogGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L32">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the Cloudwatch log group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L36">property creationTime</a>
</h3>

```typescript
creationTime: number;
```


The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/getLogGroup.ts#L40">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="LogDestinationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L97">interface LogDestinationArgs</a>
</h2>

The set of arguments for constructing a LogDestination resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the log destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L105">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L109">property targetArn</a>
</h3>

```typescript
targetArn: pulumi.Input<string>;
```


The ARN of the target Amazon Kinesis stream or Amazon Lambda resource for the destination

<h2 class="pdoc-module-header" id="LogDestinationPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L77">interface LogDestinationPolicyArgs</a>
</h2>

The set of arguments for constructing a LogDestinationPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L81">property accessPolicy</a>
</h3>

```typescript
accessPolicy: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L85">property destinationName</a>
</h3>

```typescript
destinationName: pulumi.Input<string>;
```


A name for the subscription filter

<h2 class="pdoc-module-header" id="LogDestinationPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L63">interface LogDestinationPolicyState</a>
</h2>

Input properties used for looking up and filtering LogDestinationPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L67">property accessPolicy</a>
</h3>

```typescript
accessPolicy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestinationPolicy.ts#L71">property destinationName</a>
</h3>

```typescript
destinationName?: pulumi.Input<string>;
```


A name for the subscription filter

<h2 class="pdoc-module-header" id="LogDestinationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L75">interface LogDestinationState</a>
</h2>

Input properties used for looking up and filtering LogDestination resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L79">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the log destination.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L83">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the log destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L87">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logDestination.ts#L91">property targetArn</a>
</h3>

```typescript
targetArn?: pulumi.Input<string>;
```


The ARN of the target Amazon Kinesis stream or Amazon Lambda resource for the destination

<h2 class="pdoc-module-header" id="LogGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L119">interface LogGroupArgs</a>
</h2>

The set of arguments for constructing a LogGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L125">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the log group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L133">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L138">property retentionInDays</a>
</h3>

```typescript
retentionInDays?: pulumi.Input<number>;
```


Specifies the number of days
you want to retain log events in the specified log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L142">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LogGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L86">interface LogGroupState</a>
</h2>

Input properties used for looking up and filtering LogGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L90">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L96">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the log group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L104">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L109">property retentionInDays</a>
</h3>

```typescript
retentionInDays?: pulumi.Input<number>;
```


Specifies the number of days
you want to retain log events in the specified log group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroup.ts#L113">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LogMetricFilterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L104">interface LogMetricFilterArgs</a>
</h2>

The set of arguments for constructing a LogMetricFilter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L108">property logGroupName</a>
</h3>

```typescript
logGroupName: pulumi.Input<string>;
```


The name of the log group to associate the metric filter with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L113">property metricTransformation</a>
</h3>

```typescript
metricTransformation: pulumi.Input<{ ... }>;
```


A block defining collection of information
needed to define how metric data gets emitted. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L117">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the CloudWatch metric to which the monitored log information should be published (e.g. `ErrorCount`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L122">property pattern</a>
</h3>

```typescript
pattern: pulumi.Input<string>;
```


A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html)
for extracting metric data out of ingested log events.

<h2 class="pdoc-module-header" id="LogMetricFilterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L80">interface LogMetricFilterState</a>
</h2>

Input properties used for looking up and filtering LogMetricFilter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L84">property logGroupName</a>
</h3>

```typescript
logGroupName?: pulumi.Input<string>;
```


The name of the log group to associate the metric filter with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L89">property metricTransformation</a>
</h3>

```typescript
metricTransformation?: pulumi.Input<{ ... }>;
```


A block defining collection of information
needed to define how metric data gets emitted. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the CloudWatch metric to which the monitored log information should be published (e.g. `ErrorCount`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logMetricFilter.ts#L98">property pattern</a>
</h3>

```typescript
pattern?: pulumi.Input<string>;
```


A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html)
for extracting metric data out of ingested log events.

<h2 class="pdoc-module-header" id="LogResourcePolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L77">interface LogResourcePolicyArgs</a>
</h2>

The set of arguments for constructing a LogResourcePolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L81">property policyDocument</a>
</h3>

```typescript
policyDocument: pulumi.Input<string>;
```


Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L85">property policyName</a>
</h3>

```typescript
policyName: pulumi.Input<string>;
```


Name of the resource policy.

<h2 class="pdoc-module-header" id="LogResourcePolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L63">interface LogResourcePolicyState</a>
</h2>

Input properties used for looking up and filtering LogResourcePolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L67">property policyDocument</a>
</h3>

```typescript
policyDocument?: pulumi.Input<string>;
```


Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logResourcePolicy.ts#L71">property policyName</a>
</h3>

```typescript
policyName?: pulumi.Input<string>;
```


Name of the resource policy.

<h2 class="pdoc-module-header" id="LogStreamArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L84">interface LogStreamArgs</a>
</h2>

The set of arguments for constructing a LogStream resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L88">property logGroupName</a>
</h3>

```typescript
logGroupName: pulumi.Input<string>;
```


The name of the log group under which the log stream is to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L92">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the log stream. Must not be longer than 512 characters and must not contain `:`

<h2 class="pdoc-module-header" id="LogStreamState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L66">interface LogStreamState</a>
</h2>

Input properties used for looking up and filtering LogStream resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L70">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) specifying the log stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L74">property logGroupName</a>
</h3>

```typescript
logGroupName?: pulumi.Input<string>;
```


The name of the log group under which the log stream is to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logStream.ts#L78">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the log stream. Must not be longer than 512 characters and must not contain `:`

<h2 class="pdoc-module-header" id="LogSubscriptionFilterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L122">interface LogSubscriptionFilterArgs</a>
</h2>

The set of arguments for constructing a LogSubscriptionFilter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L126">property destinationArn</a>
</h3>

```typescript
destinationArn: pulumi.Input<string>;
```


The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L130">property distribution</a>
</h3>

```typescript
distribution?: pulumi.Input<string>;
```


The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are "Random" and "ByLogStream".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L134">property filterPattern</a>
</h3>

```typescript
filterPattern: pulumi.Input<string>;
```


A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L138">property logGroup</a>
</h3>

```typescript
logGroup: pulumi.Input<LogGroup>;
```


The name of the log group to associate the subscription filter with

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L142">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the subscription filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L146">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested log events to the destination. If you use Lambda as a destination, you should skip this argument and use `aws_lambda_permission` resource for granting access from CloudWatch logs to the destination Lambda function.

<h2 class="pdoc-module-header" id="LogSubscriptionFilterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L92">interface LogSubscriptionFilterState</a>
</h2>

Input properties used for looking up and filtering LogSubscriptionFilter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L96">property destinationArn</a>
</h3>

```typescript
destinationArn?: pulumi.Input<string>;
```


The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L100">property distribution</a>
</h3>

```typescript
distribution?: pulumi.Input<string>;
```


The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are "Random" and "ByLogStream".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L104">property filterPattern</a>
</h3>

```typescript
filterPattern?: pulumi.Input<string>;
```


A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L108">property logGroup</a>
</h3>

```typescript
logGroup?: pulumi.Input<LogGroup>;
```


The name of the log group to associate the subscription filter with

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the subscription filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logSubscriptionFilter.ts#L116">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested log events to the destination. If you use Lambda as a destination, you should skip this argument and use `aws_lambda_permission` resource for granting access from CloudWatch logs to the destination Lambda function.

<h2 class="pdoc-module-header" id="MetricAlarmArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L277">interface MetricAlarmArgs</a>
</h2>

The set of arguments for constructing a MetricAlarm resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L281">property actionsEnabled</a>
</h3>

```typescript
actionsEnabled?: pulumi.Input<boolean>;
```


Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L285">property alarmActions</a>
</h3>

```typescript
alarmActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L289">property alarmDescription</a>
</h3>

```typescript
alarmDescription?: pulumi.Input<string>;
```


The description for the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L297">property comparisonOperator</a>
</h3>

```typescript
comparisonOperator: pulumi.Input<string>;
```


The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L301">property datapointsToAlarm</a>
</h3>

```typescript
datapointsToAlarm?: pulumi.Input<number>;
```


The number of datapoints that must be breaching to trigger the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L305">property dimensions</a>
</h3>

```typescript
dimensions?: pulumi.Input<{ ... }>;
```


The dimensions for the alarm's associated metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L314">property evaluateLowSampleCountPercentiles</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L318">property evaluationPeriods</a>
</h3>

```typescript
evaluationPeriods: pulumi.Input<number>;
```


The number of periods over which data is compared to the specified threshold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L322">property extendedStatistic</a>
</h3>

```typescript
extendedStatistic?: pulumi.Input<string>;
```


The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L326">property insufficientDataActions</a>
</h3>

```typescript
insufficientDataActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L331">property metricName</a>
</h3>

```typescript
metricName: pulumi.Input<string>;
```


The name for the alarm's associated metric.
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L293">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The descriptive name for the alarm. This name must be unique within the user's AWS account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L336">property namespace</a>
</h3>

```typescript
namespace: pulumi.Input<string>;
```


The namespace for the alarm's associated metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L340">property okActions</a>
</h3>

```typescript
okActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L344">property period</a>
</h3>

```typescript
period: pulumi.Input<number>;
```


The period in seconds over which the specified `statistic` is applied.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L349">property statistic</a>
</h3>

```typescript
statistic?: pulumi.Input<string>;
```


The statistic to apply to the alarm's associated metric.
Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L353">property threshold</a>
</h3>

```typescript
threshold: pulumi.Input<number>;
```


The value against which the specified statistic is compared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L357">property treatMissingData</a>
</h3>

```typescript
treatMissingData?: pulumi.Input<string>;
```


Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L361">property unit</a>
</h3>

```typescript
unit?: pulumi.Input<string>;
```


The unit for the alarm's associated metric.

<h2 class="pdoc-module-header" id="MetricAlarmState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L187">interface MetricAlarmState</a>
</h2>

Input properties used for looking up and filtering MetricAlarm resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L191">property actionsEnabled</a>
</h3>

```typescript
actionsEnabled?: pulumi.Input<boolean>;
```


Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L195">property alarmActions</a>
</h3>

```typescript
alarmActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L199">property alarmDescription</a>
</h3>

```typescript
alarmDescription?: pulumi.Input<string>;
```


The description for the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L207">property comparisonOperator</a>
</h3>

```typescript
comparisonOperator?: pulumi.Input<string>;
```


The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L211">property datapointsToAlarm</a>
</h3>

```typescript
datapointsToAlarm?: pulumi.Input<number>;
```


The number of datapoints that must be breaching to trigger the alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L215">property dimensions</a>
</h3>

```typescript
dimensions?: pulumi.Input<{ ... }>;
```


The dimensions for the alarm's associated metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L224">property evaluateLowSampleCountPercentiles</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L228">property evaluationPeriods</a>
</h3>

```typescript
evaluationPeriods?: pulumi.Input<number>;
```


The number of periods over which data is compared to the specified threshold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L232">property extendedStatistic</a>
</h3>

```typescript
extendedStatistic?: pulumi.Input<string>;
```


The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L236">property insufficientDataActions</a>
</h3>

```typescript
insufficientDataActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L241">property metricName</a>
</h3>

```typescript
metricName?: pulumi.Input<string>;
```


The name for the alarm's associated metric.
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L203">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The descriptive name for the alarm. This name must be unique within the user's AWS account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L246">property namespace</a>
</h3>

```typescript
namespace?: pulumi.Input<string>;
```


The namespace for the alarm's associated metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L250">property okActions</a>
</h3>

```typescript
okActions?: pulumi.Input<pulumi.Input<string | Topic>[]>;
```


The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Number (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L254">property period</a>
</h3>

```typescript
period?: pulumi.Input<number>;
```


The period in seconds over which the specified `statistic` is applied.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L259">property statistic</a>
</h3>

```typescript
statistic?: pulumi.Input<string>;
```


The statistic to apply to the alarm's associated metric.
Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L263">property threshold</a>
</h3>

```typescript
threshold?: pulumi.Input<number>;
```


The value against which the specified statistic is compared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L267">property treatMissingData</a>
</h3>

```typescript
treatMissingData?: pulumi.Input<string>;
```


Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/metricAlarm.ts#L271">property unit</a>
</h3>

```typescript
unit?: pulumi.Input<string>;
```


The unit for the alarm's associated metric.

