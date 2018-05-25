---
title: Module monitoring
---

<a href="..">@pulumi/azure</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AlertRule">class AlertRule</a>
* <a href="#AlertRuleArgs">interface AlertRuleArgs</a>
* <a href="#AlertRuleState">interface AlertRuleState</a>

<a href="/monitoring/alertRule.ts">monitoring/alertRule.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="AlertRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L9">class AlertRule</a>
</h2>

Manages a [metric-based alert rule](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal) in Azure Monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L77">constructor</a>
</h3>

```typescript
new AlertRule(name: string, args: AlertRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a AlertRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new AlertRule(name: string, state?: AlertRuleState, opts?: pulumi.ResourceOptions)
```


Create a AlertRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AlertRuleState): AlertRule
```


Get an existing AlertRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L25">property aggregation</a>
</h3>

```typescript
public aggregation: pulumi.Output<string>;
```


Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


A verbose description of the alert rule that will be included in the alert email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L33">property emailAction</a>
</h3>

```typescript
public emailAction: pulumi.Output<{ ... }>;
```


A `email_action` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L37">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


If `true`, the alert rule is enabled. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L41">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L45">property metricName</a>
</h3>

```typescript
public metricName: pulumi.Output<string>;
```


The metric that defines what the rule monitors.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L53">property operator</a>
</h3>

```typescript
public operator: pulumi.Output<string>;
```


The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L57">property period</a>
</h3>

```typescript
public period: pulumi.Output<string>;
```


The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L61">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L65">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The ID of the resource monitored by the alert rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L69">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L73">property threshold</a>
</h3>

```typescript
public threshold: pulumi.Output<number>;
```


The threshold value that activates the alert.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L77">property webhookAction</a>
</h3>

```typescript
public webhookAction: pulumi.Output<{ ... }>;
```


A `webhook_action` block as defined below.

<h2 class="pdoc-module-header" id="AlertRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L217">interface AlertRuleArgs</a>
</h2>

The set of arguments for constructing a AlertRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L221">property aggregation</a>
</h3>

```typescript
aggregation: pulumi.Input<string>;
```


Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L225">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A verbose description of the alert rule that will be included in the alert email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L229">property emailAction</a>
</h3>

```typescript
emailAction?: pulumi.Input<{ ... }>;
```


A `email_action` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L233">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


If `true`, the alert rule is enabled. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L237">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L241">property metricName</a>
</h3>

```typescript
metricName: pulumi.Input<string>;
```


The metric that defines what the rule monitors.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L245">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L249">property operator</a>
</h3>

```typescript
operator: pulumi.Input<string>;
```


The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L253">property period</a>
</h3>

```typescript
period: pulumi.Input<string>;
```


The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L257">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L261">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The ID of the resource monitored by the alert rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L265">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L269">property threshold</a>
</h3>

```typescript
threshold: pulumi.Input<number>;
```


The threshold value that activates the alert.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L273">property webhookAction</a>
</h3>

```typescript
webhookAction?: pulumi.Input<{ ... }>;
```


A `webhook_action` block as defined below.

<h2 class="pdoc-module-header" id="AlertRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L155">interface AlertRuleState</a>
</h2>

Input properties used for looking up and filtering AlertRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L159">property aggregation</a>
</h3>

```typescript
aggregation?: pulumi.Input<string>;
```


Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L163">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A verbose description of the alert rule that will be included in the alert email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L167">property emailAction</a>
</h3>

```typescript
emailAction?: pulumi.Input<{ ... }>;
```


A `email_action` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L171">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


If `true`, the alert rule is enabled. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L175">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L179">property metricName</a>
</h3>

```typescript
metricName?: pulumi.Input<string>;
```


The metric that defines what the rule monitors.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L183">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L187">property operator</a>
</h3>

```typescript
operator?: pulumi.Input<string>;
```


The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L191">property period</a>
</h3>

```typescript
period?: pulumi.Input<string>;
```


The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L195">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L199">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The ID of the resource monitored by the alert rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L203">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L207">property threshold</a>
</h3>

```typescript
threshold?: pulumi.Input<number>;
```


The threshold value that activates the alert.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/monitoring/alertRule.ts#L211">property webhookAction</a>
</h3>

```typescript
webhookAction?: pulumi.Input<{ ... }>;
```


A `webhook_action` block as defined below.

