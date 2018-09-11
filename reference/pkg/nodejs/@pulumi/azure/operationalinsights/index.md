---
title: Module operationalinsights
---

<a href="../index.html">@pulumi/azure</a> &gt; operationalinsights

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AnalyticsSolution">class AnalyticsSolution</a>
* <a href="#AnalyticsWorkspace">class AnalyticsWorkspace</a>
* <a href="#getAnalyticsWorkspace">function getAnalyticsWorkspace</a>
* <a href="#AnalyticsSolutionArgs">interface AnalyticsSolutionArgs</a>
* <a href="#AnalyticsSolutionState">interface AnalyticsSolutionState</a>
* <a href="#AnalyticsWorkspaceArgs">interface AnalyticsWorkspaceArgs</a>
* <a href="#AnalyticsWorkspaceState">interface AnalyticsWorkspaceState</a>
* <a href="#GetAnalyticsWorkspaceArgs">interface GetAnalyticsWorkspaceArgs</a>
* <a href="#GetAnalyticsWorkspaceResult">interface GetAnalyticsWorkspaceResult</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts">operationalinsights/analyticsSolution.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts">operationalinsights/analyticsWorkspace.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts">operationalinsights/getAnalyticsWorkspace.ts</a> 


<h2 class="pdoc-module-header" id="AnalyticsSolution">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L10">class AnalyticsSolution</a>
</h2>

Manages a Log Analytics (formally Operational Insights) Solution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L43">constructor</a>
</h3>

```typescript
new AnalyticsSolution(name: string, args: AnalyticsSolutionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AnalyticsSolution resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L30">property plan</a>
</h3>

```typescript
public plan: pulumi.Output<{ ... }>;
```


A `plan` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it's related workspace can only exist in the same resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L38">property solutionName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L39">property workspaceName</a>
</h3>

```typescript
public workspaceName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L43">property workspaceResourceId</a>
</h3>

```typescript
public workspaceResourceId: pulumi.Output<string>;
```


The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AnalyticsWorkspace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L10">class AnalyticsWorkspace</a>
</h2>

Manages a Log Analytics (formally Operational Insights) Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L62">constructor</a>
</h3>

```typescript
new AnalyticsWorkspace(name: string, args: AnalyticsWorkspaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AnalyticsWorkspace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or '-'. The '-' shouldn't be the first or the last symbol. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L34">property portalUrl</a>
</h3>

```typescript
public portalUrl: pulumi.Output<string>;
```


The Portal URL for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L38">property primarySharedKey</a>
</h3>

```typescript
public primarySharedKey: pulumi.Output<string>;
```


The Primary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L42">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L46">property retentionInDays</a>
</h3>

```typescript
public retentionInDays: pulumi.Output<number>;
```


The workspace data retention in days. Possible values range between 30 and 730.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L50">property secondarySharedKey</a>
</h3>

```typescript
public secondarySharedKey: pulumi.Output<string>;
```


The Secondary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L54">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Specifies the Sku of the Log Analytics Workspace. Possible values are `Free`, `PerNode`, `Premium`, `Standard`, `Standalone`, `Unlimited`, and `PerGB2018` (new Sku as of `2018-04-03`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L58">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L62">property workspaceId</a>
</h3>

```typescript
public workspaceId: pulumi.Output<string>;
```


The Workspace (or Customer) ID for the Log Analytics Workspace.

<h2 class="pdoc-module-header" id="getAnalyticsWorkspace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L10">function getAnalyticsWorkspace</a>
</h2>

```typescript
getAnalyticsWorkspace(args: GetAnalyticsWorkspaceArgs, opts?: pulumi.InvokeOptions): Promise<GetAnalyticsWorkspaceResult>
```


Gets information about the specified Log Analytics (formally Operational Insights) Workspace.

<h2 class="pdoc-module-header" id="AnalyticsSolutionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L124">interface AnalyticsSolutionArgs</a>
</h2>

The set of arguments for constructing a AnalyticsSolution resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L128">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L132">property plan</a>
</h3>

```typescript
plan: pulumi.Input<{ ... }>;
```


A `plan` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L136">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it's related workspace can only exist in the same resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L140">property solutionName</a>
</h3>

```typescript
solutionName: pulumi.Input<string>;
```


Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L141">property workspaceName</a>
</h3>

```typescript
workspaceName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L145">property workspaceResourceId</a>
</h3>

```typescript
workspaceResourceId: pulumi.Input<string>;
```


The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AnalyticsSolutionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L97">interface AnalyticsSolutionState</a>
</h2>

Input properties used for looking up and filtering AnalyticsSolution resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L101">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L105">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A `plan` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L109">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it's related workspace can only exist in the same resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L113">property solutionName</a>
</h3>

```typescript
solutionName?: pulumi.Input<string>;
```


Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L114">property workspaceName</a>
</h3>

```typescript
workspaceName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsSolution.ts#L118">property workspaceResourceId</a>
</h3>

```typescript
workspaceResourceId?: pulumi.Input<string>;
```


The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AnalyticsWorkspaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L161">interface AnalyticsWorkspaceArgs</a>
</h2>

The set of arguments for constructing a AnalyticsWorkspace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L165">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L169">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or '-'. The '-' shouldn't be the first or the last symbol. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L173">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L177">property retentionInDays</a>
</h3>

```typescript
retentionInDays?: pulumi.Input<number>;
```


The workspace data retention in days. Possible values range between 30 and 730.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L181">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Specifies the Sku of the Log Analytics Workspace. Possible values are `Free`, `PerNode`, `Premium`, `Standard`, `Standalone`, `Unlimited`, and `PerGB2018` (new Sku as of `2018-04-03`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L185">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AnalyticsWorkspaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L115">interface AnalyticsWorkspaceState</a>
</h2>

Input properties used for looking up and filtering AnalyticsWorkspace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L119">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or '-'. The '-' shouldn't be the first or the last symbol. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L127">property portalUrl</a>
</h3>

```typescript
portalUrl?: pulumi.Input<string>;
```


The Portal URL for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L131">property primarySharedKey</a>
</h3>

```typescript
primarySharedKey?: pulumi.Input<string>;
```


The Primary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L135">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L139">property retentionInDays</a>
</h3>

```typescript
retentionInDays?: pulumi.Input<number>;
```


The workspace data retention in days. Possible values range between 30 and 730.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L143">property secondarySharedKey</a>
</h3>

```typescript
secondarySharedKey?: pulumi.Input<string>;
```


The Secondary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L147">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Specifies the Sku of the Log Analytics Workspace. Possible values are `Free`, `PerNode`, `Premium`, `Standard`, `Standalone`, `Unlimited`, and `PerGB2018` (new Sku as of `2018-04-03`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L151">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/analyticsWorkspace.ts#L155">property workspaceId</a>
</h3>

```typescript
workspaceId?: pulumi.Input<string>;
```


The Workspace (or Customer) ID for the Log Analytics Workspace.

<h2 class="pdoc-module-header" id="GetAnalyticsWorkspaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L20">interface GetAnalyticsWorkspaceArgs</a>
</h2>

A collection of arguments for invoking getAnalyticsWorkspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the resource group in which the Log Analytics workspace is located in.

<h2 class="pdoc-module-header" id="GetAnalyticsWorkspaceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L34">interface GetAnalyticsWorkspaceResult</a>
</h2>

A collection of values returned by getAnalyticsWorkspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L67">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L35">property location</a>
</h3>

```typescript
location: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L39">property portalUrl</a>
</h3>

```typescript
portalUrl: string;
```


The Portal URL for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L43">property primarySharedKey</a>
</h3>

```typescript
primarySharedKey: string;
```


The Primary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L47">property retentionInDays</a>
</h3>

```typescript
retentionInDays: number;
```


The workspace data retention in days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L51">property secondarySharedKey</a>
</h3>

```typescript
secondarySharedKey: string;
```


The Secondary shared key for the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L55">property sku</a>
</h3>

```typescript
sku: string;
```


The Sku of the Log Analytics Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L59">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/operationalinsights/getAnalyticsWorkspace.ts#L63">property workspaceId</a>
</h3>

```typescript
workspaceId: string;
```


The Workspace (or Customer) ID for the Log Analytics Workspace.

