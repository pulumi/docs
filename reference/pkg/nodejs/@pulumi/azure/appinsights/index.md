---
title: Module appinsights
---

<a href="../index.html">@pulumi/azure</a> &gt; appinsights

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Insights">class Insights</a>
* <a href="#InsightsArgs">interface InsightsArgs</a>
* <a href="#InsightsState">interface InsightsState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts">appinsights/insights.ts</a> 


<h2 class="pdoc-module-header" id="Insights">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L9">class Insights</a>
</h2>

Create an Application Insights component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L51">constructor</a>
</h3>

```typescript
new Insights(name: string, args: InsightsArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Insights resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InsightsState): Insights
```


Get an existing Insights resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L25">property appId</a>
</h3>

```typescript
public appId: pulumi.Output<string>;
```


The App ID associated with this Application Insights component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L29">property applicationType</a>
</h3>

```typescript
public applicationType: pulumi.Output<string>;
```


Specifies the type of Application Insights to create. Valid values are `Web`, `Java`, `Phone`, `Store`, `iOS` and `Other`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L33">property instrumentationKey</a>
</h3>

```typescript
public instrumentationKey: pulumi.Output<string>;
```


The Instrumentation Key for this Application Insights component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L37">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Application Insights component. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L47">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the Application Insights component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L51">property tags</a>
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

<h2 class="pdoc-module-header" id="InsightsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L134">interface InsightsArgs</a>
</h2>

The set of arguments for constructing a Insights resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L138">property applicationType</a>
</h3>

```typescript
applicationType: pulumi.Input<string>;
```


Specifies the type of Application Insights to create. Valid values are `Web`, `Java`, `Phone`, `Store`, `iOS` and `Other`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L142">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L147">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Application Insights component. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L152">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the Application Insights component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L156">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="InsightsState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L98">interface InsightsState</a>
</h2>

Input properties used for looking up and filtering Insights resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L102">property appId</a>
</h3>

```typescript
appId?: pulumi.Input<string>;
```


The App ID associated with this Application Insights component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L106">property applicationType</a>
</h3>

```typescript
applicationType?: pulumi.Input<string>;
```


Specifies the type of Application Insights to create. Valid values are `Web`, `Java`, `Phone`, `Store`, `iOS` and `Other`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L110">property instrumentationKey</a>
</h3>

```typescript
instrumentationKey?: pulumi.Input<string>;
```


The Instrumentation Key for this Application Insights component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L114">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Application Insights component. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L124">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the Application Insights component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appinsights/insights.ts#L128">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

