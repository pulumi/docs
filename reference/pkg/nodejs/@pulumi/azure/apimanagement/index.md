---
title: Module apimanagement
---

<a href="../index.html">@pulumi/azure</a> &gt; apimanagement

<h2 class="pdoc-module-header">Index</h2>

* <a href="#API">class API</a>
* <a href="#getAPI">function getAPI</a>
* <a href="#APIArgs">interface APIArgs</a>
* <a href="#APIState">interface APIState</a>
* <a href="#GetAPIArgs">interface GetAPIArgs</a>
* <a href="#GetAPIResult">interface GetAPIResult</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts">apimanagement/aPI.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts">apimanagement/getAPI.ts</a> 


<h2 class="pdoc-module-header" id="API">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L10">class API</a>
</h2>

Manages an API Management Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L98">constructor</a>
</h3>

```typescript
new API(name: string, args: APIArgs, opts?: pulumi.CustomResourceOptions)
```


Create a API resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: APIState): API
```


Get an existing API resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L26">property additionalLocation</a>
</h3>

```typescript
public additionalLocation: pulumi.Output<{ ... } | undefined>;
```


One or more `additional_location` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L30">property certificates</a>
</h3>

```typescript
public certificates: pulumi.Output<{ ... }[] | undefined>;
```


One or more (up to 10) `certificate` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L34">property gatewayRegionalUrl</a>
</h3>

```typescript
public gatewayRegionalUrl: pulumi.Output<string>;
```


The URL of the Regional Gateway for the API Management Service in the specified region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L38">property gatewayUrl</a>
</h3>

```typescript
public gatewayUrl: pulumi.Output<string>;
```


The URL of the Gateway for the API Management Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L42">property hostnameConfiguration</a>
</h3>

```typescript
public hostnameConfiguration: pulumi.Output<{ ... }>;
```


A `hostname_configuration` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L46">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<{ ... } | undefined>;
```


An `identity` block is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L50">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The Azure location where the API Management Service exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L54">property managementApiUrl</a>
</h3>

```typescript
public managementApiUrl: pulumi.Output<string>;
```


The URL for the Management API associated with this API Management service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L58">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the API Management Service. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L62">property notificationSenderEmail</a>
</h3>

```typescript
public notificationSenderEmail: pulumi.Output<string>;
```


Email address from which the notification will be sent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L66">property portalUrl</a>
</h3>

```typescript
public portalUrl: pulumi.Output<string>;
```


The URL for the Publisher Portal associated with this API Management service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L70">property publicIpAddresses</a>
</h3>

```typescript
public publicIpAddresses: pulumi.Output<string[]>;
```


Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L74">property publisherEmail</a>
</h3>

```typescript
public publisherEmail: pulumi.Output<string>;
```


The email of publisher/company.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L78">property publisherName</a>
</h3>

```typescript
public publisherName: pulumi.Output<string>;
```


The name of publisher/company.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L82">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L86">property scmUrl</a>
</h3>

```typescript
public scmUrl: pulumi.Output<string>;
```


The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L90">property security</a>
</h3>

```typescript
public security: pulumi.Output<{ ... }>;
```


A `security` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L94">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L98">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getAPI">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L10">function getAPI</a>
</h2>

```typescript
getAPI(args: GetAPIArgs, opts?: pulumi.InvokeOptions): Promise<GetAPIResult>
```


Use this data source to access information about an existing API Management Service.

<h2 class="pdoc-module-header" id="APIArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L257">interface APIArgs</a>
</h2>

The set of arguments for constructing a API resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L261">property additionalLocation</a>
</h3>

```typescript
additionalLocation?: pulumi.Input<{ ... }>;
```


One or more `additional_location` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L265">property certificates</a>
</h3>

```typescript
certificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more (up to 10) `certificate` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L269">property hostnameConfiguration</a>
</h3>

```typescript
hostnameConfiguration?: pulumi.Input<{ ... }>;
```


A `hostname_configuration` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L273">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


An `identity` block is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L277">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The Azure location where the API Management Service exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L281">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the API Management Service. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L285">property notificationSenderEmail</a>
</h3>

```typescript
notificationSenderEmail?: pulumi.Input<string>;
```


Email address from which the notification will be sent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L289">property publisherEmail</a>
</h3>

```typescript
publisherEmail: pulumi.Input<string>;
```


The email of publisher/company.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L293">property publisherName</a>
</h3>

```typescript
publisherName: pulumi.Input<string>;
```


The name of publisher/company.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L297">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L301">property security</a>
</h3>

```typescript
security?: pulumi.Input<{ ... }>;
```


A `security` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L305">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L309">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="APIState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L175">interface APIState</a>
</h2>

Input properties used for looking up and filtering API resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L179">property additionalLocation</a>
</h3>

```typescript
additionalLocation?: pulumi.Input<{ ... }>;
```


One or more `additional_location` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L183">property certificates</a>
</h3>

```typescript
certificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more (up to 10) `certificate` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L187">property gatewayRegionalUrl</a>
</h3>

```typescript
gatewayRegionalUrl?: pulumi.Input<string>;
```


The URL of the Regional Gateway for the API Management Service in the specified region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L191">property gatewayUrl</a>
</h3>

```typescript
gatewayUrl?: pulumi.Input<string>;
```


The URL of the Gateway for the API Management Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L195">property hostnameConfiguration</a>
</h3>

```typescript
hostnameConfiguration?: pulumi.Input<{ ... }>;
```


A `hostname_configuration` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L199">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


An `identity` block is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L203">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The Azure location where the API Management Service exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L207">property managementApiUrl</a>
</h3>

```typescript
managementApiUrl?: pulumi.Input<string>;
```


The URL for the Management API associated with this API Management service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L211">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the API Management Service. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L215">property notificationSenderEmail</a>
</h3>

```typescript
notificationSenderEmail?: pulumi.Input<string>;
```


Email address from which the notification will be sent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L219">property portalUrl</a>
</h3>

```typescript
portalUrl?: pulumi.Input<string>;
```


The URL for the Publisher Portal associated with this API Management service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L223">property publicIpAddresses</a>
</h3>

```typescript
publicIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
```


Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L227">property publisherEmail</a>
</h3>

```typescript
publisherEmail?: pulumi.Input<string>;
```


The email of publisher/company.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L231">property publisherName</a>
</h3>

```typescript
publisherName?: pulumi.Input<string>;
```


The name of publisher/company.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L235">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L239">property scmUrl</a>
</h3>

```typescript
scmUrl?: pulumi.Input<string>;
```


The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L243">property security</a>
</h3>

```typescript
security?: pulumi.Input<{ ... }>;
```


A `security` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L247">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/aPI.ts#L251">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="GetAPIArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L20">interface GetAPIArgs</a>
</h2>

A collection of arguments for invoking getAPI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the API Management service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The Name of the Resource Group in which the API Management Service exists.

<h2 class="pdoc-module-header" id="GetAPIResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L34">interface GetAPIResult</a>
</h2>

A collection of values returned by getAPI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L38">property additionalLocations</a>
</h3>

```typescript
additionalLocations: { ... }[];
```


One or more `additional_location` blocks as defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L42">property gatewayRegionalUrl</a>
</h3>

```typescript
gatewayRegionalUrl: string;
```


Gateway URL of the API Management service in the Region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L46">property gatewayUrl</a>
</h3>

```typescript
gatewayUrl: string;
```


The URL for the API Management Service's Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L50">property hostnameConfigurations</a>
</h3>

```typescript
hostnameConfigurations: { ... }[];
```


A `hostname_configuration` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L94">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L54">property location</a>
</h3>

```typescript
location: string;
```


The location name of the additional region among Azure Data center regions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L58">property managementApiUrl</a>
</h3>

```typescript
managementApiUrl: string;
```


The URL for the Management API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L62">property notificationSenderEmail</a>
</h3>

```typescript
notificationSenderEmail: string;
```


The email address from which the notification will be sent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L66">property portalUrl</a>
</h3>

```typescript
portalUrl: string;
```


The URL of the Publisher Portal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L70">property publicIpAddresses</a>
</h3>

```typescript
publicIpAddresses: string[];
```


Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L74">property publisherEmail</a>
</h3>

```typescript
publisherEmail: string;
```


The email of Publisher/Company of the API Management Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L78">property publisherName</a>
</h3>

```typescript
publisherName: string;
```


The name of the Publisher/Company of the API Management Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L82">property scmUrl</a>
</h3>

```typescript
scmUrl: string;
```


The SCM (Source Code Management) endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L86">property sku</a>
</h3>

```typescript
sku: { ... };
```


A `sku` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/apimanagement/getAPI.ts#L90">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

