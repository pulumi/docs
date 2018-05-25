---
title: Module appservice
---

<a href="..">@pulumi/azure</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ActiveSlot">class ActiveSlot</a>
* <a href="#AppService">class AppService</a>
* <a href="#FunctionApp">class FunctionApp</a>
* <a href="#Plan">class Plan</a>
* <a href="#Slot">class Slot</a>
* <a href="#getAppServicePlan">function getAppServicePlan</a>
* <a href="#ActiveSlotArgs">interface ActiveSlotArgs</a>
* <a href="#ActiveSlotState">interface ActiveSlotState</a>
* <a href="#AppServiceArgs">interface AppServiceArgs</a>
* <a href="#AppServiceState">interface AppServiceState</a>
* <a href="#FunctionAppArgs">interface FunctionAppArgs</a>
* <a href="#FunctionAppState">interface FunctionAppState</a>
* <a href="#GetAppServicePlanArgs">interface GetAppServicePlanArgs</a>
* <a href="#GetAppServicePlanResult">interface GetAppServicePlanResult</a>
* <a href="#PlanArgs">interface PlanArgs</a>
* <a href="#PlanState">interface PlanState</a>
* <a href="#SlotArgs">interface SlotArgs</a>
* <a href="#SlotState">interface SlotState</a>

<a href="/appservice/activeSlot.ts">appservice/activeSlot.ts</a> <a href="/appservice/appService.ts">appservice/appService.ts</a> <a href="/appservice/functionApp.ts">appservice/functionApp.ts</a> <a href="/appservice/getAppServicePlan.ts">appservice/getAppServicePlan.ts</a> <a href="/appservice/plan.ts">appservice/plan.ts</a> <a href="/appservice/slot.ts">appservice/slot.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="ActiveSlot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L11">class ActiveSlot</a>
</h2>

Promotes an App Service Slot to Production within an App Service.

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L35">constructor</a>
</h3>

```typescript
new ActiveSlot(name: string, args: ActiveSlotArgs, opts?: pulumi.ResourceOptions)
```


Create a ActiveSlot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ActiveSlot(name: string, state?: ActiveSlotState, opts?: pulumi.ResourceOptions)
```


Create a ActiveSlot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActiveSlotState): ActiveSlot
```


Get an existing ActiveSlot resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L27">property appServiceName</a>
</h3>

```typescript
public appServiceName: pulumi.Output<string>;
```


The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L31">property appServiceSlotName</a>
</h3>

```typescript
public appServiceSlotName: pulumi.Output<string>;
```


The name of the App Service Slot which should be promoted to the Production Slot within the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L35">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AppService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L11">class AppService</a>
</h2>

Manages an App Service (within an App Service Plan).

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L79">constructor</a>
</h3>

```typescript
new AppService(name: string, args: AppServiceArgs, opts?: pulumi.ResourceOptions)
```


Create a AppService resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new AppService(name: string, state?: AppServiceState, opts?: pulumi.ResourceOptions)
```


Create a AppService resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AppServiceState): AppService
```


Get an existing AppService resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L27">property appServicePlanId</a>
</h3>

```typescript
public appServicePlanId: pulumi.Output<string>;
```


The ID of the App Service Plan within which to create this App Service. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L31">property appSettings</a>
</h3>

```typescript
public appSettings: pulumi.Output<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L35">property clientAffinityEnabled</a>
</h3>

```typescript
public clientAffinityEnabled: pulumi.Output<boolean>;
```


Should the App Service send session affinity cookies, which route client requests in the same session to the same instance? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L39">property connectionStrings</a>
</h3>

```typescript
public connectionStrings: pulumi.Output<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L43">property defaultSiteHostname</a>
</h3>

```typescript
public defaultSiteHostname: pulumi.Output<string>;
```


The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L47">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Is the App Service Enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L51">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L55">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L59">property outboundIpAddresses</a>
</h3>

```typescript
public outboundIpAddresses: pulumi.Output<string>;
```


A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L63">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L67">property siteConfig</a>
</h3>

```typescript
public siteConfig: pulumi.Output<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L71">property siteCredential</a>
</h3>

```typescript
public siteCredential: pulumi.Output<{ ... }>;
```


(Optional) The site-level credential used to publish files to Azure Web App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L75">property sourceControl</a>
</h3>

```typescript
public sourceControl: pulumi.Output<{ ... }>;
```


(Optional) The default local Git source control information if deployment option is set to `LocalGit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L79">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="FunctionApp">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L9">class FunctionApp</a>
</h2>

Manages a Function App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L77">constructor</a>
</h3>

```typescript
new FunctionApp(name: string, args: FunctionAppArgs, opts?: pulumi.ResourceOptions)
```


Create a FunctionApp resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new FunctionApp(name: string, state?: FunctionAppState, opts?: pulumi.ResourceOptions)
```


Create a FunctionApp resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FunctionAppState): FunctionApp
```


Get an existing FunctionApp resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L25">property appServicePlanId</a>
</h3>

```typescript
public appServicePlanId: pulumi.Output<string>;
```


The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L29">property appSettings</a>
</h3>

```typescript
public appSettings: pulumi.Output<{ ... } | undefined>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L33">property clientAffinityEnabled</a>
</h3>

```typescript
public clientAffinityEnabled: pulumi.Output<boolean>;
```


Should the Function App send session affinity cookies, which route client requests in the same session to the same instance? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L37">property connectionStrings</a>
</h3>

```typescript
public connectionStrings: pulumi.Output<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L41">property defaultHostname</a>
</h3>

```typescript
public defaultHostname: pulumi.Output<string>;
```


The default hostname associated with the Function App - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L45">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Is the Function App enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L49">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L57">property outboundIpAddresses</a>
</h3>

```typescript
public outboundIpAddresses: pulumi.Output<string>;
```


A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L61">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Function App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L65">property siteConfig</a>
</h3>

```typescript
public siteConfig: pulumi.Output<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L69">property storageConnectionString</a>
</h3>

```typescript
public storageConnectionString: pulumi.Output<string>;
```


The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L73">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L77">property version</a>
</h3>

```typescript
public version: pulumi.Output<string | undefined>;
```


The runtime version associated with the Function App. Possible values are `~1` and `beta`. Defaults to `~1`.

<h2 class="pdoc-module-header" id="Plan">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L9">class Plan</a>
</h2>

Create an App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L53">constructor</a>
</h3>

```typescript
new Plan(name: string, args: PlanArgs, opts?: pulumi.ResourceOptions)
```


Create a Plan resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Plan(name: string, state?: PlanState, opts?: pulumi.ResourceOptions)
```


Create a Plan resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PlanState): Plan
```


Get an existing Plan resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L25">property kind</a>
</h3>

```typescript
public kind: pulumi.Output<string | undefined>;
```


The kind of the App Service Plan to create. Possible values are `Windows`, `Linux` and `FunctionApp` (for a Consumption Plan). Defaults to `Windows`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L29">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L33">property maximumNumberOfWorkers</a>
</h3>

```typescript
public maximumNumberOfWorkers: pulumi.Output<number>;
```


Maximum number of instances that can be assigned to this App Service plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L41">property properties</a>
</h3>

```typescript
public properties: pulumi.Output<{ ... }>;
```


A `properties` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L49">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L53">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Slot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L12">class Slot</a>
</h2>

Manages an App Service Slot (within an App Service).

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L72">constructor</a>
</h3>

```typescript
new Slot(name: string, args: SlotArgs, opts?: pulumi.ResourceOptions)
```


Create a Slot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Slot(name: string, state?: SlotState, opts?: pulumi.ResourceOptions)
```


Create a Slot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SlotState): Slot
```


Get an existing Slot resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L28">property appServiceName</a>
</h3>

```typescript
public appServiceName: pulumi.Output<string>;
```


The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L32">property appServicePlanId</a>
</h3>

```typescript
public appServicePlanId: pulumi.Output<string>;
```


The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L36">property appSettings</a>
</h3>

```typescript
public appSettings: pulumi.Output<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L40">property clientAffinityEnabled</a>
</h3>

```typescript
public clientAffinityEnabled: pulumi.Output<boolean>;
```


Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L44">property connectionStrings</a>
</h3>

```typescript
public connectionStrings: pulumi.Output<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L48">property defaultSiteHostname</a>
</h3>

```typescript
public defaultSiteHostname: pulumi.Output<string>;
```


The Default Hostname associated with the App Service Slot - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L52">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Is the App Service Slot Enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L56">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L64">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the App Service Slot component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L68">property siteConfig</a>
</h3>

```typescript
public siteConfig: pulumi.Output<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L72">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getAppServicePlan">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L9">function getAppServicePlan</a>
</h2>

```typescript
getAppServicePlan(args: GetAppServicePlanArgs): Promise<GetAppServicePlanResult>
```


Use this data source to obtain information about an App Service Plan (formerly known as a `Server Farm`).

<h2 class="pdoc-module-header" id="ActiveSlotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L94">interface ActiveSlotArgs</a>
</h2>

The set of arguments for constructing a ActiveSlot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L98">property appServiceName</a>
</h3>

```typescript
appServiceName: pulumi.Input<string>;
```


The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L102">property appServiceSlotName</a>
</h3>

```typescript
appServiceSlotName: pulumi.Input<string>;
```


The name of the App Service Slot which should be promoted to the Production Slot within the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L106">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ActiveSlotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L76">interface ActiveSlotState</a>
</h2>

Input properties used for looking up and filtering ActiveSlot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L80">property appServiceName</a>
</h3>

```typescript
appServiceName?: pulumi.Input<string>;
```


The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L84">property appServiceSlotName</a>
</h3>

```typescript
appServiceSlotName?: pulumi.Input<string>;
```


The name of the App Service Slot which should be promoted to the Production Slot within the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/activeSlot.ts#L88">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AppServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L204">interface AppServiceArgs</a>
</h2>

The set of arguments for constructing a AppService resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L208">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this App Service. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L212">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L216">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the App Service send session affinity cookies, which route client requests in the same session to the same instance? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L220">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L224">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the App Service Enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L228">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L232">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L236">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L240">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L244">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AppServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L142">interface AppServiceState</a>
</h2>

Input properties used for looking up and filtering AppService resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L146">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId?: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this App Service. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L150">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L154">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the App Service send session affinity cookies, which route client requests in the same session to the same instance? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L158">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L162">property defaultSiteHostname</a>
</h3>

```typescript
defaultSiteHostname?: pulumi.Input<string>;
```


The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L166">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the App Service Enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L170">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L174">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L178">property outboundIpAddresses</a>
</h3>

```typescript
outboundIpAddresses?: pulumi.Input<string>;
```


A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L182">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L186">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L190">property siteCredential</a>
</h3>

```typescript
siteCredential?: pulumi.Input<{ ... }>;
```


(Optional) The site-level credential used to publish files to Azure Web App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L194">property sourceControl</a>
</h3>

```typescript
sourceControl?: pulumi.Input<{ ... }>;
```


(Optional) The default local Git source control information if deployment option is set to `LocalGit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/appService.ts#L198">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="FunctionAppArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L205">interface FunctionAppArgs</a>
</h2>

The set of arguments for constructing a FunctionApp resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L209">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L213">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L217">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the Function App send session affinity cookies, which route client requests in the same session to the same instance? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L221">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L225">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the Function App enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L229">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L233">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L237">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Function App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L241">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L245">property storageConnectionString</a>
</h3>

```typescript
storageConnectionString: pulumi.Input<string>;
```


The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L249">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L253">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The runtime version associated with the Function App. Possible values are `~1` and `beta`. Defaults to `~1`.

<h2 class="pdoc-module-header" id="FunctionAppState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L143">interface FunctionAppState</a>
</h2>

Input properties used for looking up and filtering FunctionApp resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L147">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId?: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L151">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L155">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the Function App send session affinity cookies, which route client requests in the same session to the same instance? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L159">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L163">property defaultHostname</a>
</h3>

```typescript
defaultHostname?: pulumi.Input<string>;
```


The default hostname associated with the Function App - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L167">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the Function App enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L171">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L175">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L179">property outboundIpAddresses</a>
</h3>

```typescript
outboundIpAddresses?: pulumi.Input<string>;
```


A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L183">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Function App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L187">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L191">property storageConnectionString</a>
</h3>

```typescript
storageConnectionString?: pulumi.Input<string>;
```


The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L195">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/functionApp.ts#L199">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The runtime version associated with the Function App. Possible values are `~1` and `beta`. Defaults to `~1`.

<h2 class="pdoc-module-header" id="GetAppServicePlanArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L19">interface GetAppServicePlanArgs</a>
</h2>

A collection of arguments for invoking getAppServicePlan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the App Service Plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The Name of the Resource Group where the App Service Plan exists.

<h2 class="pdoc-module-header" id="GetAppServicePlanResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L33">interface GetAppServicePlanResult</a>
</h2>

A collection of values returned by getAppServicePlan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L37">property kind</a>
</h3>

```typescript
kind: string;
```


The Operating System type of the App Service Plan

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L41">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the App Service Plan exists

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L45">property maximumNumberOfWorkers</a>
</h3>

```typescript
maximumNumberOfWorkers: number;
```


Maximum number of instances that can be assigned to this App Service plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L49">property properties</a>
</h3>

```typescript
properties: { ... }[];
```


A `properties` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L53">property sku</a>
</h3>

```typescript
sku: { ... }[];
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/getAppServicePlan.ts#L57">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="PlanArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L142">interface PlanArgs</a>
</h2>

The set of arguments for constructing a Plan resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L146">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


The kind of the App Service Plan to create. Possible values are `Windows`, `Linux` and `FunctionApp` (for a Consumption Plan). Defaults to `Windows`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L150">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L154">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L158">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```


A `properties` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L162">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L166">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L170">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="PlanState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L104">interface PlanState</a>
</h2>

Input properties used for looking up and filtering Plan resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L108">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


The kind of the App Service Plan to create. Possible values are `Windows`, `Linux` and `FunctionApp` (for a Consumption Plan). Defaults to `Windows`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L112">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L116">property maximumNumberOfWorkers</a>
</h3>

```typescript
maximumNumberOfWorkers?: pulumi.Input<number>;
```


Maximum number of instances that can be assigned to this App Service plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L124">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```


A `properties` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L128">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L132">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/plan.ts#L136">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SlotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L188">interface SlotArgs</a>
</h2>

The set of arguments for constructing a Slot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L192">property appServiceName</a>
</h3>

```typescript
appServiceName: pulumi.Input<string>;
```


The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L196">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L200">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L204">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L208">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L212">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the App Service Slot Enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L216">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L220">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L224">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Slot component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L228">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L232">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SlotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L134">interface SlotState</a>
</h2>

Input properties used for looking up and filtering Slot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L138">property appServiceName</a>
</h3>

```typescript
appServiceName?: pulumi.Input<string>;
```


The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L142">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId?: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L146">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L150">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L154">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L158">property defaultSiteHostname</a>
</h3>

```typescript
defaultSiteHostname?: pulumi.Input<string>;
```


The Default Hostname associated with the App Service Slot - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L162">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the App Service Slot Enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L166">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L170">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L174">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Slot component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L178">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/appservice/slot.ts#L182">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

