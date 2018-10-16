---
title: Module cdn
---

<a href="../index.html">@pulumi/azure</a> &gt; cdn

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Endpoint">class Endpoint</a>
* <a href="#Profile">class Profile</a>
* <a href="#getProfile">function getProfile</a>
* <a href="#EndpointArgs">interface EndpointArgs</a>
* <a href="#EndpointState">interface EndpointState</a>
* <a href="#GetProfileArgs">interface GetProfileArgs</a>
* <a href="#GetProfileResult">interface GetProfileResult</a>
* <a href="#ProfileArgs">interface ProfileArgs</a>
* <a href="#ProfileState">interface ProfileState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts">cdn/endpoint.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts">cdn/getProfile.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts">cdn/profile.ts</a> 


<h2 class="pdoc-module-header" id="Endpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L10">class Endpoint</a>
</h2>

A CDN Endpoint is the entity within a CDN Profile containing configuration information regarding caching behaviors and origins. The CDN Endpoint is exposed using the URL format <endpointname>.azureedge.net by default, but custom domains can also be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L87">constructor</a>
</h3>

```typescript
new Endpoint(name: string, args: EndpointArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Endpoint resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EndpointState): Endpoint
```


Get an existing Endpoint resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L26">property contentTypesToCompresses</a>
</h3>

```typescript
public contentTypesToCompresses: pulumi.Output<string[]>;
```


An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L30">property geoFilters</a>
</h3>

```typescript
public geoFilters: pulumi.Output<{ ... }[] | undefined>;
```


A set of Geo Filters for this CDN Endpoint. Each `geo_filter` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L31">property hostName</a>
</h3>

```typescript
public hostName: pulumi.Output<string>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L35">property isCompressionEnabled</a>
</h3>

```typescript
public isCompressionEnabled: pulumi.Output<boolean | undefined>;
```


Indicates whether compression is to be enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L39">property isHttpAllowed</a>
</h3>

```typescript
public isHttpAllowed: pulumi.Output<boolean | undefined>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L43">property isHttpsAllowed</a>
</h3>

```typescript
public isHttpsAllowed: pulumi.Output<boolean | undefined>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L47">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the CDN Endpoint. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L55">property optimizationType</a>
</h3>

```typescript
public optimizationType: pulumi.Output<string | undefined>;
```


What types of optimization should this CDN Endpoint optimize for? Possible values include `DynamicSiteAcceleration`, `GeneralMediaStreaming`, `GeneralWebDelivery`, `LargeFileDownload` and `VideoOnDemandMediaStreaming`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L63">property originHostHeader</a>
</h3>

```typescript
public originHostHeader: pulumi.Output<string>;
```


The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L67">property originPath</a>
</h3>

```typescript
public originPath: pulumi.Output<string>;
```


The path used at for origin requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L59">property origins</a>
</h3>

```typescript
public origins: pulumi.Output<{ ... }[]>;
```


The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each `origin` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L71">property probePath</a>
</h3>

```typescript
public probePath: pulumi.Output<string>;
```


the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the `origin_path`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L75">property profileName</a>
</h3>

```typescript
public profileName: pulumi.Output<string>;
```


The CDN Profile to which to attach the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L79">property querystringCachingBehaviour</a>
</h3>

```typescript
public querystringCachingBehaviour: pulumi.Output<string | undefined>;
```


Sets query string caching behavior. Allowed values are `IgnoreQueryString`, `BypassCaching` and `UseQueryString`. Defaults to `IgnoreQueryString`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L83">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L87">property tags</a>
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

<h2 class="pdoc-module-header" id="Profile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L10">class Profile</a>
</h2>

Manage a CDN Profile to create a collection of CDN Endpoints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L44">constructor</a>
</h3>

```typescript
new Profile(name: string, args: ProfileArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Profile resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProfileState): Profile
```


Get an existing Profile resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L36">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the CDN Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L40">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


The pricing related information of current CDN profile. Accepted values are `Standard_Akamai`, `Standard_ChinaCdn`, `Standard_Microsoft`, `Standard_Verizon` or `Premium_Verizon`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L44">property tags</a>
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

<h2 class="pdoc-module-header" id="getProfile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L10">function getProfile</a>
</h2>

```typescript
getProfile(args: GetProfileArgs, opts?: pulumi.InvokeOptions): Promise<GetProfileResult>
```


Use this data source to access information about a CDN Profile.

<h2 class="pdoc-module-header" id="EndpointArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L228">interface EndpointArgs</a>
</h2>

The set of arguments for constructing a Endpoint resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L232">property contentTypesToCompresses</a>
</h3>

```typescript
contentTypesToCompresses?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L236">property geoFilters</a>
</h3>

```typescript
geoFilters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A set of Geo Filters for this CDN Endpoint. Each `geo_filter` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L240">property isCompressionEnabled</a>
</h3>

```typescript
isCompressionEnabled?: pulumi.Input<boolean>;
```


Indicates whether compression is to be enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L244">property isHttpAllowed</a>
</h3>

```typescript
isHttpAllowed?: pulumi.Input<boolean>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L248">property isHttpsAllowed</a>
</h3>

```typescript
isHttpsAllowed?: pulumi.Input<boolean>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L252">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L256">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CDN Endpoint. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L260">property optimizationType</a>
</h3>

```typescript
optimizationType?: pulumi.Input<string>;
```


What types of optimization should this CDN Endpoint optimize for? Possible values include `DynamicSiteAcceleration`, `GeneralMediaStreaming`, `GeneralWebDelivery`, `LargeFileDownload` and `VideoOnDemandMediaStreaming`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L268">property originHostHeader</a>
</h3>

```typescript
originHostHeader?: pulumi.Input<string>;
```


The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L272">property originPath</a>
</h3>

```typescript
originPath?: pulumi.Input<string>;
```


The path used at for origin requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L264">property origins</a>
</h3>

```typescript
origins: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each `origin` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L276">property probePath</a>
</h3>

```typescript
probePath?: pulumi.Input<string>;
```


the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the `origin_path`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L280">property profileName</a>
</h3>

```typescript
profileName: pulumi.Input<string>;
```


The CDN Profile to which to attach the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L284">property querystringCachingBehaviour</a>
</h3>

```typescript
querystringCachingBehaviour?: pulumi.Input<string>;
```


Sets query string caching behavior. Allowed values are `IgnoreQueryString`, `BypassCaching` and `UseQueryString`. Defaults to `IgnoreQueryString`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L288">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L292">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EndpointState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L157">interface EndpointState</a>
</h2>

Input properties used for looking up and filtering Endpoint resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L161">property contentTypesToCompresses</a>
</h3>

```typescript
contentTypesToCompresses?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L165">property geoFilters</a>
</h3>

```typescript
geoFilters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A set of Geo Filters for this CDN Endpoint. Each `geo_filter` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L166">property hostName</a>
</h3>

```typescript
hostName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L170">property isCompressionEnabled</a>
</h3>

```typescript
isCompressionEnabled?: pulumi.Input<boolean>;
```


Indicates whether compression is to be enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L174">property isHttpAllowed</a>
</h3>

```typescript
isHttpAllowed?: pulumi.Input<boolean>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L178">property isHttpsAllowed</a>
</h3>

```typescript
isHttpsAllowed?: pulumi.Input<boolean>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L182">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L186">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CDN Endpoint. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L190">property optimizationType</a>
</h3>

```typescript
optimizationType?: pulumi.Input<string>;
```


What types of optimization should this CDN Endpoint optimize for? Possible values include `DynamicSiteAcceleration`, `GeneralMediaStreaming`, `GeneralWebDelivery`, `LargeFileDownload` and `VideoOnDemandMediaStreaming`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L198">property originHostHeader</a>
</h3>

```typescript
originHostHeader?: pulumi.Input<string>;
```


The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L202">property originPath</a>
</h3>

```typescript
originPath?: pulumi.Input<string>;
```


The path used at for origin requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L194">property origins</a>
</h3>

```typescript
origins?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each `origin` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L206">property probePath</a>
</h3>

```typescript
probePath?: pulumi.Input<string>;
```


the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the `origin_path`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L210">property profileName</a>
</h3>

```typescript
profileName?: pulumi.Input<string>;
```


The CDN Profile to which to attach the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L214">property querystringCachingBehaviour</a>
</h3>

```typescript
querystringCachingBehaviour?: pulumi.Input<string>;
```


Sets query string caching behavior. Allowed values are `IgnoreQueryString`, `BypassCaching` and `UseQueryString`. Defaults to `IgnoreQueryString`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L218">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L222">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="GetProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L20">interface GetProfileArgs</a>
</h2>

A collection of arguments for invoking getProfile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the CDN Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the resource group in which the CDN Profile exists.

<h2 class="pdoc-module-header" id="GetProfileResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L34">interface GetProfileResult</a>
</h2>

A collection of values returned by getProfile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L50">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L38">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L42">property sku</a>
</h3>

```typescript
sku: string;
```


The pricing related information of current CDN profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L46">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="ProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L115">interface ProfileArgs</a>
</h2>

The set of arguments for constructing a Profile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L119">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L129">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the CDN Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L133">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


The pricing related information of current CDN profile. Accepted values are `Standard_Akamai`, `Standard_ChinaCdn`, `Standard_Microsoft`, `Standard_Verizon` or `Premium_Verizon`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L137">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ProfileState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L87">interface ProfileState</a>
</h2>

Input properties used for looking up and filtering Profile resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L91">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L101">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the CDN Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L105">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The pricing related information of current CDN profile. Accepted values are `Standard_Akamai`, `Standard_ChinaCdn`, `Standard_Microsoft`, `Standard_Verizon` or `Premium_Verizon`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L109">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

