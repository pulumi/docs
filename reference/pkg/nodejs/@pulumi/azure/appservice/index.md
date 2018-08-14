---
title: Module appservice
---

<a href="../index.html">@pulumi/azure</a> &gt; appservice

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ActiveSlot">class ActiveSlot</a>
* <a href="#AppService">class AppService</a>
* <a href="#CustomHostnameBinding">class CustomHostnameBinding</a>
* <a href="#FunctionApp">class FunctionApp</a>
* <a href="#Plan">class Plan</a>
* <a href="#Slot">class Slot</a>
* <a href="#getAppService">function getAppService</a>
* <a href="#getAppServicePlan">function getAppServicePlan</a>
* <a href="#ActiveSlotArgs">interface ActiveSlotArgs</a>
* <a href="#ActiveSlotState">interface ActiveSlotState</a>
* <a href="#AppServiceArgs">interface AppServiceArgs</a>
* <a href="#AppServiceState">interface AppServiceState</a>
* <a href="#CustomHostnameBindingArgs">interface CustomHostnameBindingArgs</a>
* <a href="#CustomHostnameBindingState">interface CustomHostnameBindingState</a>
* <a href="#FunctionAppArgs">interface FunctionAppArgs</a>
* <a href="#FunctionAppState">interface FunctionAppState</a>
* <a href="#GetAppServiceArgs">interface GetAppServiceArgs</a>
* <a href="#GetAppServicePlanArgs">interface GetAppServicePlanArgs</a>
* <a href="#GetAppServicePlanResult">interface GetAppServicePlanResult</a>
* <a href="#GetAppServiceResult">interface GetAppServiceResult</a>
* <a href="#PlanArgs">interface PlanArgs</a>
* <a href="#PlanState">interface PlanState</a>
* <a href="#SlotArgs">interface SlotArgs</a>
* <a href="#SlotState">interface SlotState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts">appservice/activeSlot.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts">appservice/appService.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts">appservice/customHostnameBinding.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts">appservice/functionApp.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts">appservice/getAppService.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts">appservice/getAppServicePlan.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts">appservice/plan.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts">appservice/slot.ts</a> 


<h2 class="pdoc-module-header" id="ActiveSlot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L11">class ActiveSlot</a>
</h2>

Promotes an App Service Slot to Production within an App Service.

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L35">constructor</a>
</h3>

```typescript
new ActiveSlot(name: string, args: ActiveSlotArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ActiveSlot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActiveSlotState): ActiveSlot
```


Get an existing ActiveSlot resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L27">property appServiceName</a>
</h3>

```typescript
public appServiceName: pulumi.Output<string>;
```


The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L31">property appServiceSlotName</a>
</h3>

```typescript
public appServiceSlotName: pulumi.Output<string>;
```


The name of the App Service Slot which should be promoted to the Production Slot within the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L35">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AppService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L11">class AppService</a>
</h2>

Manages an App Service (within an App Service Plan).

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L87">constructor</a>
</h3>

```typescript
new AppService(name: string, args: AppServiceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AppService resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AppServiceState): AppService
```


Get an existing AppService resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L27">property appServicePlanId</a>
</h3>

```typescript
public appServicePlanId: pulumi.Output<string>;
```


The ID of the App Service Plan within which to create this App Service. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L31">property appSettings</a>
</h3>

```typescript
public appSettings: pulumi.Output<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L35">property clientAffinityEnabled</a>
</h3>

```typescript
public clientAffinityEnabled: pulumi.Output<boolean>;
```


Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L39">property connectionStrings</a>
</h3>

```typescript
public connectionStrings: pulumi.Output<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L43">property defaultSiteHostname</a>
</h3>

```typescript
public defaultSiteHostname: pulumi.Output<string>;
```


The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L47">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Is the App Service Enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L51">property httpsOnly</a>
</h3>

```typescript
public httpsOnly: pulumi.Output<boolean | undefined>;
```


Can the App Service only be accessed via HTTPS? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L55">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<{ ... }>;
```


A Managed Service Identity block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L59">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L63">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L67">property outboundIpAddresses</a>
</h3>

```typescript
public outboundIpAddresses: pulumi.Output<string>;
```


A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L71">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L75">property siteConfig</a>
</h3>

```typescript
public siteConfig: pulumi.Output<{ ... }>;
```


A `site_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L79">property siteCredential</a>
</h3>

```typescript
public siteCredential: pulumi.Output<{ ... }>;
```


A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L83">property sourceControl</a>
</h3>

```typescript
public sourceControl: pulumi.Output<{ ... }>;
```


A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L87">property tags</a>
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

<h2 class="pdoc-module-header" id="CustomHostnameBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L9">class CustomHostnameBinding</a>
</h2>

Manages a Hostname Binding within an App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L33">constructor</a>
</h3>

```typescript
new CustomHostnameBinding(name: string, args: CustomHostnameBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CustomHostnameBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomHostnameBindingState): CustomHostnameBinding
```


Get an existing CustomHostnameBinding resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L25">property appServiceName</a>
</h3>

```typescript
public appServiceName: pulumi.Output<string>;
```


The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L29">property hostname</a>
</h3>

```typescript
public hostname: pulumi.Output<string>;
```


Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="FunctionApp">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L9">class FunctionApp</a>
</h2>

Manages a Function App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L89">constructor</a>
</h3>

```typescript
new FunctionApp(name: string, args: FunctionAppArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FunctionApp resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FunctionAppState): FunctionApp
```


Get an existing FunctionApp resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L25">property appServicePlanId</a>
</h3>

```typescript
public appServicePlanId: pulumi.Output<string>;
```


The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L29">property appSettings</a>
</h3>

```typescript
public appSettings: pulumi.Output<{ ... } | undefined>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L33">property clientAffinityEnabled</a>
</h3>

```typescript
public clientAffinityEnabled: pulumi.Output<boolean>;
```


Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L37">property connectionStrings</a>
</h3>

```typescript
public connectionStrings: pulumi.Output<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L41">property defaultHostname</a>
</h3>

```typescript
public defaultHostname: pulumi.Output<string>;
```


The default hostname associated with the Function App - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L45">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Is the Function App enabled?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L49">property httpsOnly</a>
</h3>

```typescript
public httpsOnly: pulumi.Output<boolean | undefined>;
```


Can the Function App only be accessed via HTTPS? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L53">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<{ ... }>;
```


An `identity` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L57">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L65">property outboundIpAddresses</a>
</h3>

```typescript
public outboundIpAddresses: pulumi.Output<string>;
```


A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L69">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Function App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L73">property siteConfig</a>
</h3>

```typescript
public siteConfig: pulumi.Output<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L77">property siteCredential</a>
</h3>

```typescript
public siteCredential: pulumi.Output<{ ... }>;
```


A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L81">property storageConnectionString</a>
</h3>

```typescript
public storageConnectionString: pulumi.Output<string>;
```


The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L85">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L89">property version</a>
</h3>

```typescript
public version: pulumi.Output<string | undefined>;
```


The runtime version associated with the Function App. Possible values are `~1` and `beta`. Defaults to `~1`.

<h2 class="pdoc-module-header" id="Plan">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L9">class Plan</a>
</h2>

Create an App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L53">constructor</a>
</h3>

```typescript
new Plan(name: string, args: PlanArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Plan resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PlanState): Plan
```


Get an existing Plan resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L25">property kind</a>
</h3>

```typescript
public kind: pulumi.Output<string | undefined>;
```


The kind of the App Service Plan to create. Possible values are `Windows` (also available as `App`), `Linux` and `FunctionApp` (for a Consumption Plan). Defaults to `Windows`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L29">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L33">property maximumNumberOfWorkers</a>
</h3>

```typescript
public maximumNumberOfWorkers: pulumi.Output<number>;
```


Maximum number of instances that can be assigned to this App Service plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L41">property properties</a>
</h3>

```typescript
public properties: pulumi.Output<{ ... }>;
```


A `properties` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L49">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L53">property tags</a>
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

<h2 class="pdoc-module-header" id="Slot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L12">class Slot</a>
</h2>

Manages an App Service Slot (within an App Service).

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L80">constructor</a>
</h3>

```typescript
new Slot(name: string, args: SlotArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Slot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SlotState): Slot
```


Get an existing Slot resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L28">property appServiceName</a>
</h3>

```typescript
public appServiceName: pulumi.Output<string>;
```


The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L32">property appServicePlanId</a>
</h3>

```typescript
public appServicePlanId: pulumi.Output<string>;
```


The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L36">property appSettings</a>
</h3>

```typescript
public appSettings: pulumi.Output<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L40">property clientAffinityEnabled</a>
</h3>

```typescript
public clientAffinityEnabled: pulumi.Output<boolean>;
```


Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L44">property connectionStrings</a>
</h3>

```typescript
public connectionStrings: pulumi.Output<{ ... }[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L48">property defaultSiteHostname</a>
</h3>

```typescript
public defaultSiteHostname: pulumi.Output<string>;
```


The Default Hostname associated with the App Service Slot - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L52">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Is the App Service Slot Enabled?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L56">property httpsOnly</a>
</h3>

```typescript
public httpsOnly: pulumi.Output<boolean | undefined>;
```


Can the App Service Slot only be accessed via HTTPS? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L60">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<{ ... } | undefined>;
```


A Managed Service Identity block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L64">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L68">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L72">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the App Service Slot component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L76">property siteConfig</a>
</h3>

```typescript
public siteConfig: pulumi.Output<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L80">property tags</a>
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

<h2 class="pdoc-module-header" id="getAppService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L9">function getAppService</a>
</h2>

```typescript
getAppService(args: GetAppServiceArgs, opts?: pulumi.InvokeOptions): Promise<GetAppServiceResult>
```


Use this data source to obtain information about an App Service.

<h2 class="pdoc-module-header" id="getAppServicePlan">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L9">function getAppServicePlan</a>
</h2>

```typescript
getAppServicePlan(args: GetAppServicePlanArgs, opts?: pulumi.InvokeOptions): Promise<GetAppServicePlanResult>
```


Use this data source to obtain information about an App Service Plan (formerly known as a `Server Farm`).

<h2 class="pdoc-module-header" id="ActiveSlotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L92">interface ActiveSlotArgs</a>
</h2>

The set of arguments for constructing a ActiveSlot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L96">property appServiceName</a>
</h3>

```typescript
appServiceName: pulumi.Input<string>;
```


The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L100">property appServiceSlotName</a>
</h3>

```typescript
appServiceSlotName: pulumi.Input<string>;
```


The name of the App Service Slot which should be promoted to the Production Slot within the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L104">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ActiveSlotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L74">interface ActiveSlotState</a>
</h2>

Input properties used for looking up and filtering ActiveSlot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L78">property appServiceName</a>
</h3>

```typescript
appServiceName?: pulumi.Input<string>;
```


The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L82">property appServiceSlotName</a>
</h3>

```typescript
appServiceSlotName?: pulumi.Input<string>;
```


The name of the App Service Slot which should be promoted to the Production Slot within the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/activeSlot.ts#L86">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AppServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L222">interface AppServiceArgs</a>
</h2>

The set of arguments for constructing a AppService resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L226">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this App Service. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L230">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L234">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L238">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L242">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the App Service Enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L246">property httpsOnly</a>
</h3>

```typescript
httpsOnly?: pulumi.Input<boolean>;
```


Can the App Service only be accessed via HTTPS? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L250">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


A Managed Service Identity block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L254">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L258">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L262">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L266">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L270">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AppServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L152">interface AppServiceState</a>
</h2>

Input properties used for looking up and filtering AppService resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L156">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId?: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this App Service. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L160">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L164">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L168">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L172">property defaultSiteHostname</a>
</h3>

```typescript
defaultSiteHostname?: pulumi.Input<string>;
```


The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L176">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the App Service Enabled? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L180">property httpsOnly</a>
</h3>

```typescript
httpsOnly?: pulumi.Input<boolean>;
```


Can the App Service only be accessed via HTTPS? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L184">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


A Managed Service Identity block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L188">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L192">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L196">property outboundIpAddresses</a>
</h3>

```typescript
outboundIpAddresses?: pulumi.Input<string>;
```


A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L200">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L204">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L208">property siteCredential</a>
</h3>

```typescript
siteCredential?: pulumi.Input<{ ... }>;
```


A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L212">property sourceControl</a>
</h3>

```typescript
sourceControl?: pulumi.Input<{ ... }>;
```


A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/appService.ts#L216">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="CustomHostnameBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L90">interface CustomHostnameBindingArgs</a>
</h2>

The set of arguments for constructing a CustomHostnameBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L94">property appServiceName</a>
</h3>

```typescript
appServiceName: pulumi.Input<string>;
```


The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L98">property hostname</a>
</h3>

```typescript
hostname: pulumi.Input<string>;
```


Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L102">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CustomHostnameBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L72">interface CustomHostnameBindingState</a>
</h2>

Input properties used for looking up and filtering CustomHostnameBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L76">property appServiceName</a>
</h3>

```typescript
appServiceName?: pulumi.Input<string>;
```


The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L80">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/customHostnameBinding.ts#L84">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="FunctionAppArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L233">interface FunctionAppArgs</a>
</h2>

The set of arguments for constructing a FunctionApp resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L237">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L241">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L245">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L249">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L253">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the Function App enabled?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L257">property httpsOnly</a>
</h3>

```typescript
httpsOnly?: pulumi.Input<boolean>;
```


Can the Function App only be accessed via HTTPS? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L261">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


An `identity` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L265">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L269">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L273">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Function App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L277">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L281">property storageConnectionString</a>
</h3>

```typescript
storageConnectionString: pulumi.Input<string>;
```


The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L285">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L289">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The runtime version associated with the Function App. Possible values are `~1` and `beta`. Defaults to `~1`.

<h2 class="pdoc-module-header" id="FunctionAppState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L159">interface FunctionAppState</a>
</h2>

Input properties used for looking up and filtering FunctionApp resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L163">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId?: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L167">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L171">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L175">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L179">property defaultHostname</a>
</h3>

```typescript
defaultHostname?: pulumi.Input<string>;
```


The default hostname associated with the Function App - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L183">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the Function App enabled?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L187">property httpsOnly</a>
</h3>

```typescript
httpsOnly?: pulumi.Input<boolean>;
```


Can the Function App only be accessed via HTTPS? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L191">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


An `identity` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L195">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L199">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L203">property outboundIpAddresses</a>
</h3>

```typescript
outboundIpAddresses?: pulumi.Input<string>;
```


A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L207">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Function App.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L211">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L215">property siteCredential</a>
</h3>

```typescript
siteCredential?: pulumi.Input<{ ... }>;
```


A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L219">property storageConnectionString</a>
</h3>

```typescript
storageConnectionString?: pulumi.Input<string>;
```


The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L223">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/functionApp.ts#L227">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The runtime version associated with the Function App. Possible values are `~1` and `beta`. Defaults to `~1`.

<h2 class="pdoc-module-header" id="GetAppServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L20">interface GetAppServiceArgs</a>
</h2>

A collection of arguments for invoking getAppService.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The Name of the Resource Group where the App Service exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L29">property siteConfig</a>
</h3>

```typescript
siteConfig?: { ... };
```

<h2 class="pdoc-module-header" id="GetAppServicePlanArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L19">interface GetAppServicePlanArgs</a>
</h2>

A collection of arguments for invoking getAppServicePlan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


The name of the App Service Plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The Name of the Resource Group where the App Service Plan exists.

<h2 class="pdoc-module-header" id="GetAppServicePlanResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L33">interface GetAppServicePlanResult</a>
</h2>

A collection of values returned by getAppServicePlan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L61">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L37">property kind</a>
</h3>

```typescript
kind: string;
```


The Operating System type of the App Service Plan

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L41">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the App Service Plan exists

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L45">property maximumNumberOfWorkers</a>
</h3>

```typescript
maximumNumberOfWorkers: number;
```


Maximum number of instances that can be assigned to this App Service plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L49">property properties</a>
</h3>

```typescript
properties: { ... }[];
```


A `properties` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L53">property sku</a>
</h3>

```typescript
sku: { ... };
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppServicePlan.ts#L57">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="GetAppServiceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L35">interface GetAppServiceResult</a>
</h2>

A collection of values returned by getAppService.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L39">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId: string;
```


The ID of the App Service Plan within which the App Service exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L43">property appSettings</a>
</h3>

```typescript
appSettings: { ... };
```


A key-value pair of App Settings for the App Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L47">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled: boolean;
```


Does the App Service send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L51">property connectionStrings</a>
</h3>

```typescript
connectionStrings: { ... }[];
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L52">property defaultSiteHostname</a>
</h3>

```typescript
defaultSiteHostname: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L56">property enabled</a>
</h3>

```typescript
enabled: boolean;
```


Is the App Service Enabled?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L60">property httpsOnly</a>
</h3>

```typescript
httpsOnly: boolean;
```


Can the App Service only be accessed via HTTPS?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L79">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L64">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the App Service exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L65">property outboundIpAddresses</a>
</h3>

```typescript
outboundIpAddresses: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L69">property siteConfig</a>
</h3>

```typescript
siteConfig: { ... };
```


A `site_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L70">property siteCredentials</a>
</h3>

```typescript
siteCredentials: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L71">property sourceControls</a>
</h3>

```typescript
sourceControls: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/getAppService.ts#L75">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="PlanArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L140">interface PlanArgs</a>
</h2>

The set of arguments for constructing a Plan resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L144">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


The kind of the App Service Plan to create. Possible values are `Windows` (also available as `App`), `Linux` and `FunctionApp` (for a Consumption Plan). Defaults to `Windows`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L148">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L152">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L156">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```


A `properties` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L160">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L164">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L168">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="PlanState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L102">interface PlanState</a>
</h2>

Input properties used for looking up and filtering Plan resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L106">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


The kind of the App Service Plan to create. Possible values are `Windows` (also available as `App`), `Linux` and `FunctionApp` (for a Consumption Plan). Defaults to `Windows`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L110">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L114">property maximumNumberOfWorkers</a>
</h3>

```typescript
maximumNumberOfWorkers?: pulumi.Input<number>;
```


Maximum number of instances that can be assigned to this App Service plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L122">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```


A `properties` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L126">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Plan component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L130">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/plan.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SlotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L206">interface SlotArgs</a>
</h2>

The set of arguments for constructing a Slot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L210">property appServiceName</a>
</h3>

```typescript
appServiceName: pulumi.Input<string>;
```


The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L214">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L218">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L222">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L226">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L230">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the App Service Slot Enabled?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L234">property httpsOnly</a>
</h3>

```typescript
httpsOnly?: pulumi.Input<boolean>;
```


Can the App Service Slot only be accessed via HTTPS? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L238">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


A Managed Service Identity block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L242">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L246">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L250">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Slot component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L254">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L258">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SlotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L144">interface SlotState</a>
</h2>

Input properties used for looking up and filtering Slot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L148">property appServiceName</a>
</h3>

```typescript
appServiceName?: pulumi.Input<string>;
```


The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L152">property appServicePlanId</a>
</h3>

```typescript
appServicePlanId?: pulumi.Input<string>;
```


The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L156">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Input<{ ... }>;
```


A key-value pair of App Settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L160">property clientAffinityEnabled</a>
</h3>

```typescript
clientAffinityEnabled?: pulumi.Input<boolean>;
```


Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L164">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An `connection_string` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L168">property defaultSiteHostname</a>
</h3>

```typescript
defaultSiteHostname?: pulumi.Input<string>;
```


The Default Hostname associated with the App Service Slot - such as `mysite.azurewebsites.net`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L172">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is the App Service Slot Enabled?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L176">property httpsOnly</a>
</h3>

```typescript
httpsOnly?: pulumi.Input<boolean>;
```


Can the App Service Slot only be accessed via HTTPS? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L180">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


A Managed Service Identity block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L184">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L188">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Connection String.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L192">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the App Service Slot component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L196">property siteConfig</a>
</h3>

```typescript
siteConfig?: pulumi.Input<{ ... }>;
```


A `site_config` object as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/appservice/slot.ts#L200">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

