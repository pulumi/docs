---
title: Module operationalinsights
---

<a href="../index.html">@pulumi/azure</a> &gt; operationalinsights

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AnalyticsSolution">class AnalyticsSolution</a>
* <a href="#AnalyticsWorkspace">class AnalyticsWorkspace</a>
* <a href="#AnalyticsSolutionArgs">interface AnalyticsSolutionArgs</a>
* <a href="#AnalyticsSolutionState">interface AnalyticsSolutionState</a>
* <a href="#AnalyticsWorkspaceArgs">interface AnalyticsWorkspaceArgs</a>
* <a href="#AnalyticsWorkspaceState">interface AnalyticsWorkspaceState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts">operationalinsights/analyticsSolution.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts">operationalinsights/analyticsWorkspace.ts</a> 


<h2 class="pdoc-module-header" id="AnalyticsSolution">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L9">class AnalyticsSolution</a>
</h2>

Manages a Log Analytics (formally Operational Insights) Solution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L42">constructor</a>
</h3>

```typescript
new AnalyticsSolution(name: string, args: AnalyticsSolutionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AnalyticsSolution resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AnalyticsSolutionState): AnalyticsSolution
```


Get an existing AnalyticsSolution resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L29">property plan</a>
</h3>

```typescript
public plan: pulumi.Output<{ ... }>;
```


A `plan` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it's related workspace can only exist in the same resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L37">property solutionName</a>
</h3>

```typescript
public solutionName: pulumi.Output<string>;
```


Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L38">property workspaceName</a>
</h3>

```typescript
public workspaceName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L42">property workspaceResourceId</a>
</h3>

```typescript
public workspaceResourceId: pulumi.Output<string>;
```


The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AnalyticsWorkspace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L9">class AnalyticsWorkspace</a>
</h2>

Manages a Log Analytics (formally Operational Insights) Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L61">constructor</a>
</h3>

```typescript
new AnalyticsWorkspace(name: string, args: AnalyticsWorkspaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AnalyticsWorkspace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AnalyticsWorkspaceState): AnalyticsWorkspace
```


Get an existing AnalyticsWorkspace resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or '-'. The '-' shouldn't be the first or the last symbol. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L33">property portalUrl</a>
</h3>

```typescript
public portalUrl: pulumi.Output<string>;
```


The Portal URL for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L37">property primarySharedKey</a>
</h3>

```typescript
public primarySharedKey: pulumi.Output<string>;
```


The Primary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L41">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L45">property retentionInDays</a>
</h3>

```typescript
public retentionInDays: pulumi.Output<number>;
```


The workspace data retention in days. Possible values range between 30 and 730.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L49">property secondarySharedKey</a>
</h3>

```typescript
public secondarySharedKey: pulumi.Output<string>;
```


The Secondary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L53">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Specifies the Sku of the Log Analytics Workspace. Possible values are `Free`, `PerNode`, `Premium`, `Standard`, `Standalone`, `Unlimited`, and `PerGB2018` (new Sku as of `2018-04-03`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L57">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L61">property workspaceId</a>
</h3>

```typescript
public workspaceId: pulumi.Output<string>;
```


The Workspace (or Customer) ID for the Log Analytics Workspace.

<h2 class="pdoc-module-header" id="AnalyticsSolutionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L123">interface AnalyticsSolutionArgs</a>
</h2>

The set of arguments for constructing a AnalyticsSolution resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L127">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L131">property plan</a>
</h3>

```typescript
plan: pulumi.Input<{ ... }>;
```


A `plan` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L135">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it's related workspace can only exist in the same resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L139">property solutionName</a>
</h3>

```typescript
solutionName: pulumi.Input<string>;
```


Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L140">property workspaceName</a>
</h3>

```typescript
workspaceName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L144">property workspaceResourceId</a>
</h3>

```typescript
workspaceResourceId: pulumi.Input<string>;
```


The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AnalyticsSolutionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L96">interface AnalyticsSolutionState</a>
</h2>

Input properties used for looking up and filtering AnalyticsSolution resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L100">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L104">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A `plan` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L108">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it's related workspace can only exist in the same resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L112">property solutionName</a>
</h3>

```typescript
solutionName?: pulumi.Input<string>;
```


Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L113">property workspaceName</a>
</h3>

```typescript
workspaceName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L117">property workspaceResourceId</a>
</h3>

```typescript
workspaceResourceId?: pulumi.Input<string>;
```


The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AnalyticsWorkspaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L160">interface AnalyticsWorkspaceArgs</a>
</h2>

The set of arguments for constructing a AnalyticsWorkspace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L164">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L168">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or '-'. The '-' shouldn't be the first or the last symbol. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L172">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L176">property retentionInDays</a>
</h3>

```typescript
retentionInDays?: pulumi.Input<number>;
```


The workspace data retention in days. Possible values range between 30 and 730.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L180">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Specifies the Sku of the Log Analytics Workspace. Possible values are `Free`, `PerNode`, `Premium`, `Standard`, `Standalone`, `Unlimited`, and `PerGB2018` (new Sku as of `2018-04-03`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L184">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AnalyticsWorkspaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L114">interface AnalyticsWorkspaceState</a>
</h2>

Input properties used for looking up and filtering AnalyticsWorkspace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L118">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or '-'. The '-' shouldn't be the first or the last symbol. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L126">property portalUrl</a>
</h3>

```typescript
portalUrl?: pulumi.Input<string>;
```


The Portal URL for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L130">property primarySharedKey</a>
</h3>

```typescript
primarySharedKey?: pulumi.Input<string>;
```


The Primary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L134">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L138">property retentionInDays</a>
</h3>

```typescript
retentionInDays?: pulumi.Input<number>;
```


The workspace data retention in days. Possible values range between 30 and 730.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L142">property secondarySharedKey</a>
</h3>

```typescript
secondarySharedKey?: pulumi.Input<string>;
```


The Secondary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L146">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Specifies the Sku of the Log Analytics Workspace. Possible values are `Free`, `PerNode`, `Premium`, `Standard`, `Standalone`, `Unlimited`, and `PerGB2018` (new Sku as of `2018-04-03`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L150">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L154">property workspaceId</a>
</h3>

```typescript
workspaceId?: pulumi.Input<string>;
```


The Workspace (or Customer) ID for the Log Analytics Workspace.

