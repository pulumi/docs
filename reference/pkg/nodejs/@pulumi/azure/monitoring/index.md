---
title: Module monitoring
---

<a href="../index.html">@pulumi/azure</a> &gt; monitoring

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ActionGroup">class ActionGroup</a>
* <a href="#ActivityLogAlert">class ActivityLogAlert</a>
* <a href="#AlertRule">class AlertRule</a>
* <a href="#LogProfile">class LogProfile</a>
* <a href="#MetricAlert">class MetricAlert</a>
* <a href="#getLogProfile">function getLogProfile</a>
* <a href="#ActionGroupArgs">interface ActionGroupArgs</a>
* <a href="#ActionGroupState">interface ActionGroupState</a>
* <a href="#ActivityLogAlertArgs">interface ActivityLogAlertArgs</a>
* <a href="#ActivityLogAlertState">interface ActivityLogAlertState</a>
* <a href="#AlertRuleArgs">interface AlertRuleArgs</a>
* <a href="#AlertRuleState">interface AlertRuleState</a>
* <a href="#GetLogProfileArgs">interface GetLogProfileArgs</a>
* <a href="#GetLogProfileResult">interface GetLogProfileResult</a>
* <a href="#LogProfileArgs">interface LogProfileArgs</a>
* <a href="#LogProfileState">interface LogProfileState</a>
* <a href="#MetricAlertArgs">interface MetricAlertArgs</a>
* <a href="#MetricAlertState">interface MetricAlertState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts">monitoring/actionGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts">monitoring/activityLogAlert.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts">monitoring/alertRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts">monitoring/getLogProfile.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts">monitoring/logProfile.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts">monitoring/metricAlert.ts</a> 


<h2 class="pdoc-module-header" id="ActionGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L10">class ActionGroup</a>
</h2>

Manages an Action Group within Azure Monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L54">constructor</a>
</h3>

```typescript
new ActionGroup(name: string, args: ActionGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ActionGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActionGroupState): ActionGroup
```


Get an existing ActionGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L26">property emailReceivers</a>
</h3>

```typescript
public emailReceivers: pulumi.Output<{ ... }[] | undefined>;
```


One or more `email_receiver` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L30">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Action Group instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L42">property shortName</a>
</h3>

```typescript
public shortName: pulumi.Output<string>;
```


The short name of the action group. This will be used in SMS messages.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L46">property smsReceivers</a>
</h3>

```typescript
public smsReceivers: pulumi.Output<{ ... }[] | undefined>;
```


One or more `sms_receiver ` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L50">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L54">property webhookReceivers</a>
</h3>

```typescript
public webhookReceivers: pulumi.Output<{ ... }[] | undefined>;
```


One or more `webhook_receiver ` blocks as defined below.

<h2 class="pdoc-module-header" id="ActivityLogAlert">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L7">class ActivityLogAlert</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L27">constructor</a>
</h3>

```typescript
new ActivityLogAlert(name: string, args: ActivityLogAlertArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ActivityLogAlert resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActivityLogAlertState): ActivityLogAlert
```


Get an existing ActivityLogAlert resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L20">property actions</a>
</h3>

```typescript
public actions: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L21">property criteria</a>
</h3>

```typescript
public criteria: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L22">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L23">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L24">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L25">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L26">property scopes</a>
</h3>

```typescript
public scopes: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L27">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AlertRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L10">class AlertRule</a>
</h2>

Manages a [metric-based alert rule](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal) in Azure Monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L78">constructor</a>
</h3>

```typescript
new AlertRule(name: string, args: AlertRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AlertRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AlertRuleState): AlertRule
```


Get an existing AlertRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L26">property aggregation</a>
</h3>

```typescript
public aggregation: pulumi.Output<string>;
```


Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


A verbose description of the alert rule that will be included in the alert email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L34">property emailAction</a>
</h3>

```typescript
public emailAction: pulumi.Output<{ ... }>;
```


A `email_action` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L38">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


If `true`, the alert rule is enabled. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L42">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L46">property metricName</a>
</h3>

```typescript
public metricName: pulumi.Output<string>;
```


The metric that defines what the rule monitors.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L54">property operator</a>
</h3>

```typescript
public operator: pulumi.Output<string>;
```


The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L58">property period</a>
</h3>

```typescript
public period: pulumi.Output<string>;
```


The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L62">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L66">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The ID of the resource monitored by the alert rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L70">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L74">property threshold</a>
</h3>

```typescript
public threshold: pulumi.Output<number>;
```


The threshold value that activates the alert.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L78">property webhookAction</a>
</h3>

```typescript
public webhookAction: pulumi.Output<{ ... }>;
```


A `webhook_action` block as defined below.

<h2 class="pdoc-module-header" id="LogProfile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L10">class LogProfile</a>
</h2>

Manages a [Log Profile](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile). A Log Profile configures how Activity Logs are exported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L47">constructor</a>
</h3>

```typescript
new LogProfile(name: string, args: LogProfileArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LogProfile resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogProfileState): LogProfile
```


Get an existing LogProfile resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L26">property categories</a>
</h3>

```typescript
public categories: pulumi.Output<string[]>;
```


List of categories of the logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L30">property locations</a>
</h3>

```typescript
public locations: pulumi.Output<string[]>;
```


List of regions for which Activity Log events are stored or streamed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Log Profile. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L39">property retentionPolicy</a>
</h3>

```typescript
public retentionPolicy: pulumi.Output<{ ... }>;
```


A `retention_policy` block as documented below. A retention policy for how long Activity Logs are retained in the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L43">property servicebusRuleId</a>
</h3>

```typescript
public servicebusRuleId: pulumi.Output<string | undefined>;
```


The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of `storage_account_id` or `servicebus_rule_id` must be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L47">property storageAccountId</a>
</h3>

```typescript
public storageAccountId: pulumi.Output<string | undefined>;
```


The resource ID of the storage account in which the Activity Log is stored. At least one of `storage_account_id` or `servicebus_rule_id` must be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MetricAlert">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L7">class MetricAlert</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L31">constructor</a>
</h3>

```typescript
new MetricAlert(name: string, args: MetricAlertArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MetricAlert resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MetricAlertState): MetricAlert
```


Get an existing MetricAlert resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L20">property actions</a>
</h3>

```typescript
public actions: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L21">property autoMitigate</a>
</h3>

```typescript
public autoMitigate: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L22">property criterias</a>
</h3>

```typescript
public criterias: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L23">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L24">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L25">property frequency</a>
</h3>

```typescript
public frequency: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L27">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L28">property scopes</a>
</h3>

```typescript
public scopes: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L29">property severity</a>
</h3>

```typescript
public severity: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L30">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L31">property windowSize</a>
</h3>

```typescript
public windowSize: pulumi.Output<string | undefined>;
```

<h2 class="pdoc-module-header" id="getLogProfile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L10">function getLogProfile</a>
</h2>

```typescript
getLogProfile(args: GetLogProfileArgs, opts?: pulumi.InvokeOptions): Promise<GetLogProfileResult>
```


Use this data source to access the properties of a Log Profile.

<h2 class="pdoc-module-header" id="ActionGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L138">interface ActionGroupArgs</a>
</h2>

The set of arguments for constructing a ActionGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L142">property emailReceivers</a>
</h3>

```typescript
emailReceivers?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `email_receiver` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L146">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L154">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Action Group instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L158">property shortName</a>
</h3>

```typescript
shortName: pulumi.Input<string>;
```


The short name of the action group. This will be used in SMS messages.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L162">property smsReceivers</a>
</h3>

```typescript
smsReceivers?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `sms_receiver ` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L166">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L170">property webhookReceivers</a>
</h3>

```typescript
webhookReceivers?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `webhook_receiver ` blocks as defined below.

<h2 class="pdoc-module-header" id="ActionGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L100">interface ActionGroupState</a>
</h2>

Input properties used for looking up and filtering ActionGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L104">property emailReceivers</a>
</h3>

```typescript
emailReceivers?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `email_receiver` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L108">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L116">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Action Group instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L120">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


The short name of the action group. This will be used in SMS messages.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L124">property smsReceivers</a>
</h3>

```typescript
smsReceivers?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `sms_receiver ` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L128">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/actionGroup.ts#L132">property webhookReceivers</a>
</h3>

```typescript
webhookReceivers?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `webhook_receiver ` blocks as defined below.

<h2 class="pdoc-module-header" id="ActivityLogAlertArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L90">interface ActivityLogAlertArgs</a>
</h2>

The set of arguments for constructing a ActivityLogAlert resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L91">property actions</a>
</h3>

```typescript
actions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L92">property criteria</a>
</h3>

```typescript
criteria: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L93">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L94">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L96">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L97">property scopes</a>
</h3>

```typescript
scopes: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L98">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ActivityLogAlertState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L76">interface ActivityLogAlertState</a>
</h2>

Input properties used for looking up and filtering ActivityLogAlert resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L77">property actions</a>
</h3>

```typescript
actions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L78">property criteria</a>
</h3>

```typescript
criteria?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L79">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L80">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L82">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L83">property scopes</a>
</h3>

```typescript
scopes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/activityLogAlert.ts#L84">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="AlertRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L216">interface AlertRuleArgs</a>
</h2>

The set of arguments for constructing a AlertRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L220">property aggregation</a>
</h3>

```typescript
aggregation: pulumi.Input<string>;
```


Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L224">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A verbose description of the alert rule that will be included in the alert email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L228">property emailAction</a>
</h3>

```typescript
emailAction?: pulumi.Input<{ ... }>;
```


A `email_action` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L232">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


If `true`, the alert rule is enabled. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L236">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L240">property metricName</a>
</h3>

```typescript
metricName: pulumi.Input<string>;
```


The metric that defines what the rule monitors.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L244">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L248">property operator</a>
</h3>

```typescript
operator: pulumi.Input<string>;
```


The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L252">property period</a>
</h3>

```typescript
period: pulumi.Input<string>;
```


The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L256">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L260">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The ID of the resource monitored by the alert rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L264">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L268">property threshold</a>
</h3>

```typescript
threshold: pulumi.Input<number>;
```


The threshold value that activates the alert.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L272">property webhookAction</a>
</h3>

```typescript
webhookAction?: pulumi.Input<{ ... }>;
```


A `webhook_action` block as defined below.

<h2 class="pdoc-module-header" id="AlertRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L154">interface AlertRuleState</a>
</h2>

Input properties used for looking up and filtering AlertRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L158">property aggregation</a>
</h3>

```typescript
aggregation?: pulumi.Input<string>;
```


Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L162">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A verbose description of the alert rule that will be included in the alert email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L166">property emailAction</a>
</h3>

```typescript
emailAction?: pulumi.Input<{ ... }>;
```


A `email_action` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L170">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


If `true`, the alert rule is enabled. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L174">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L178">property metricName</a>
</h3>

```typescript
metricName?: pulumi.Input<string>;
```


The metric that defines what the rule monitors.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L182">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L186">property operator</a>
</h3>

```typescript
operator?: pulumi.Input<string>;
```


The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L190">property period</a>
</h3>

```typescript
period?: pulumi.Input<string>;
```


The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L194">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L198">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The ID of the resource monitored by the alert rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L202">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L206">property threshold</a>
</h3>

```typescript
threshold?: pulumi.Input<number>;
```


The threshold value that activates the alert.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/alertRule.ts#L210">property webhookAction</a>
</h3>

```typescript
webhookAction?: pulumi.Input<{ ... }>;
```


A `webhook_action` block as defined below.

<h2 class="pdoc-module-header" id="GetLogProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L19">interface GetLogProfileArgs</a>
</h2>

A collection of arguments for invoking getLogProfile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the Name of the Log Profile.

<h2 class="pdoc-module-header" id="GetLogProfileResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L29">interface GetLogProfileResult</a>
</h2>

A collection of values returned by getLogProfile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L33">property categories</a>
</h3>

```typescript
categories: string[];
```


List of categories of the logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L50">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L37">property locations</a>
</h3>

```typescript
locations: string[];
```


List of regions for which Activity Log events are stored or streamed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L38">property retentionPolicy</a>
</h3>

```typescript
retentionPolicy: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L42">property servicebusRuleId</a>
</h3>

```typescript
servicebusRuleId: string;
```


The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/getLogProfile.ts#L46">property storageAccountId</a>
</h3>

```typescript
storageAccountId: string;
```


The resource id of the storage account in which the Activity Log is stored.

<h2 class="pdoc-module-header" id="LogProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L123">interface LogProfileArgs</a>
</h2>

The set of arguments for constructing a LogProfile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L127">property categories</a>
</h3>

```typescript
categories: pulumi.Input<pulumi.Input<string>[]>;
```


List of categories of the logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L131">property locations</a>
</h3>

```typescript
locations: pulumi.Input<pulumi.Input<string>[]>;
```


List of regions for which Activity Log events are stored or streamed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Log Profile. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L140">property retentionPolicy</a>
</h3>

```typescript
retentionPolicy: pulumi.Input<{ ... }>;
```


A `retention_policy` block as documented below. A retention policy for how long Activity Logs are retained in the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L144">property servicebusRuleId</a>
</h3>

```typescript
servicebusRuleId?: pulumi.Input<string>;
```


The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of `storage_account_id` or `servicebus_rule_id` must be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L148">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


The resource ID of the storage account in which the Activity Log is stored. At least one of `storage_account_id` or `servicebus_rule_id` must be set.

<h2 class="pdoc-module-header" id="LogProfileState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L92">interface LogProfileState</a>
</h2>

Input properties used for looking up and filtering LogProfile resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L96">property categories</a>
</h3>

```typescript
categories?: pulumi.Input<pulumi.Input<string>[]>;
```


List of categories of the logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L100">property locations</a>
</h3>

```typescript
locations?: pulumi.Input<pulumi.Input<string>[]>;
```


List of regions for which Activity Log events are stored or streamed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Log Profile. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L109">property retentionPolicy</a>
</h3>

```typescript
retentionPolicy?: pulumi.Input<{ ... }>;
```


A `retention_policy` block as documented below. A retention policy for how long Activity Logs are retained in the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L113">property servicebusRuleId</a>
</h3>

```typescript
servicebusRuleId?: pulumi.Input<string>;
```


The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of `storage_account_id` or `servicebus_rule_id` must be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/logProfile.ts#L117">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


The resource ID of the storage account in which the Activity Log is stored. At least one of `storage_account_id` or `servicebus_rule_id` must be set.

<h2 class="pdoc-module-header" id="MetricAlertArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L106">interface MetricAlertArgs</a>
</h2>

The set of arguments for constructing a MetricAlert resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L107">property actions</a>
</h3>

```typescript
actions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L108">property autoMitigate</a>
</h3>

```typescript
autoMitigate?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L109">property criterias</a>
</h3>

```typescript
criterias: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L110">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L111">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L112">property frequency</a>
</h3>

```typescript
frequency?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L114">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L115">property scopes</a>
</h3>

```typescript
scopes: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L116">property severity</a>
</h3>

```typescript
severity?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L117">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L118">property windowSize</a>
</h3>

```typescript
windowSize?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="MetricAlertState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L88">interface MetricAlertState</a>
</h2>

Input properties used for looking up and filtering MetricAlert resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L89">property actions</a>
</h3>

```typescript
actions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L90">property autoMitigate</a>
</h3>

```typescript
autoMitigate?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L91">property criterias</a>
</h3>

```typescript
criterias?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L92">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L93">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L94">property frequency</a>
</h3>

```typescript
frequency?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L96">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L97">property scopes</a>
</h3>

```typescript
scopes?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L98">property severity</a>
</h3>

```typescript
severity?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L99">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/monitoring/metricAlert.ts#L100">property windowSize</a>
</h3>

```typescript
windowSize?: pulumi.Input<string>;
```

