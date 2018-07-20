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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L9">class Endpoint</a>
</h2>

A CDN Endpoint is the entity within a CDN Profile containing configuration information regarding caching behaviors and origins. The CDN Endpoint is exposed using the URL format <endpointname>.azureedge.net by default, but custom domains can also be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L89">constructor</a>
</h3>

```typescript
new Endpoint(name: string, args: EndpointArgs, opts?: pulumi.ResourceOptions)
```


Create a Endpoint resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EndpointState): Endpoint
```


Get an existing Endpoint resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L25">property contentTypesToCompresses</a>
</h3>

```typescript
public contentTypesToCompresses: pulumi.Output<string[]>;
```


An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L29">property geoFilters</a>
</h3>

```typescript
public geoFilters: pulumi.Output<{ ... }[] | undefined>;
```


A set of Geo Filters for this CDN Endpoint. Each `geo_filter` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L33">property hostName</a>
</h3>

```typescript
public hostName: pulumi.Output<string>;
```


A string that determines the hostname/IP address of the origin server. This string can be a domain name, Storage Account endpoint, Web App endpoint, IPv4 address or IPv6 address. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L37">property isCompressionEnabled</a>
</h3>

```typescript
public isCompressionEnabled: pulumi.Output<boolean | undefined>;
```


Indicates whether compression is to be enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L41">property isHttpAllowed</a>
</h3>

```typescript
public isHttpAllowed: pulumi.Output<boolean | undefined>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L45">property isHttpsAllowed</a>
</h3>

```typescript
public isHttpsAllowed: pulumi.Output<boolean | undefined>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L49">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L57">property optimizationType</a>
</h3>

```typescript
public optimizationType: pulumi.Output<string | undefined>;
```


What types of optimization should this CDN Endpoint optimize for? Possible values include `DynamicSiteAcceleration`, `GeneralMediaStreaming`, `GeneralWebDelivery`, `LargeFileDownload` and `VideoOnDemandMediaStreaming`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L65">property originHostHeader</a>
</h3>

```typescript
public originHostHeader: pulumi.Output<string>;
```


The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L69">property originPath</a>
</h3>

```typescript
public originPath: pulumi.Output<string>;
```


The path used at for origin requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L61">property origins</a>
</h3>

```typescript
public origins: pulumi.Output<{ ... }[]>;
```


The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each `origin` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L73">property probePath</a>
</h3>

```typescript
public probePath: pulumi.Output<string>;
```


the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the `origin_path`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L77">property profileName</a>
</h3>

```typescript
public profileName: pulumi.Output<string>;
```


The CDN Profile to which to attach the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L81">property querystringCachingBehaviour</a>
</h3>

```typescript
public querystringCachingBehaviour: pulumi.Output<string | undefined>;
```


Sets query string caching behavior. Allowed values are `IgnoreQueryString`, `BypassCaching` and `UseQueryString`. Defaults to `IgnoreQueryString`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L85">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L89">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L9">class Profile</a>
</h2>

Create a CDN Profile to create a collection of CDN Endpoints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L43">constructor</a>
</h3>

```typescript
new Profile(name: string, args: ProfileArgs, opts?: pulumi.ResourceOptions)
```


Create a Profile resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProfileState): Profile
```


Get an existing Profile resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L35">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the CDN Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L39">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


The pricing related information of current CDN profile. Accepted values are `Standard_Verizon`, `Standard_Akamai` or `Premium_Verizon`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L43">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L9">function getProfile</a>
</h2>

```typescript
getProfile(args: GetProfileArgs): Promise<GetProfileResult>
```


Use this data source to access information about a CDN Profile.

<h2 class="pdoc-module-header" id="EndpointArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L233">interface EndpointArgs</a>
</h2>

The set of arguments for constructing a Endpoint resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L237">property contentTypesToCompresses</a>
</h3>

```typescript
contentTypesToCompresses?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L241">property geoFilters</a>
</h3>

```typescript
geoFilters?: pulumi.Input<{ ... }[]>;
```


A set of Geo Filters for this CDN Endpoint. Each `geo_filter` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L245">property isCompressionEnabled</a>
</h3>

```typescript
isCompressionEnabled?: pulumi.Input<boolean>;
```


Indicates whether compression is to be enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L249">property isHttpAllowed</a>
</h3>

```typescript
isHttpAllowed?: pulumi.Input<boolean>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L253">property isHttpsAllowed</a>
</h3>

```typescript
isHttpsAllowed?: pulumi.Input<boolean>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L257">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L261">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L265">property optimizationType</a>
</h3>

```typescript
optimizationType?: pulumi.Input<string>;
```


What types of optimization should this CDN Endpoint optimize for? Possible values include `DynamicSiteAcceleration`, `GeneralMediaStreaming`, `GeneralWebDelivery`, `LargeFileDownload` and `VideoOnDemandMediaStreaming`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L273">property originHostHeader</a>
</h3>

```typescript
originHostHeader?: pulumi.Input<string>;
```


The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L277">property originPath</a>
</h3>

```typescript
originPath?: pulumi.Input<string>;
```


The path used at for origin requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L269">property origins</a>
</h3>

```typescript
origins: pulumi.Input<{ ... }[]>;
```


The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each `origin` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L281">property probePath</a>
</h3>

```typescript
probePath?: pulumi.Input<string>;
```


the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the `origin_path`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L285">property profileName</a>
</h3>

```typescript
profileName: pulumi.Input<string>;
```


The CDN Profile to which to attach the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L289">property querystringCachingBehaviour</a>
</h3>

```typescript
querystringCachingBehaviour?: pulumi.Input<string>;
```


Sets query string caching behavior. Allowed values are `IgnoreQueryString`, `BypassCaching` and `UseQueryString`. Defaults to `IgnoreQueryString`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L293">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L297">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EndpointState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L159">interface EndpointState</a>
</h2>

Input properties used for looking up and filtering Endpoint resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L163">property contentTypesToCompresses</a>
</h3>

```typescript
contentTypesToCompresses?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L167">property geoFilters</a>
</h3>

```typescript
geoFilters?: pulumi.Input<{ ... }[]>;
```


A set of Geo Filters for this CDN Endpoint. Each `geo_filter` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L171">property hostName</a>
</h3>

```typescript
hostName?: pulumi.Input<string>;
```


A string that determines the hostname/IP address of the origin server. This string can be a domain name, Storage Account endpoint, Web App endpoint, IPv4 address or IPv6 address. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L175">property isCompressionEnabled</a>
</h3>

```typescript
isCompressionEnabled?: pulumi.Input<boolean>;
```


Indicates whether compression is to be enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L179">property isHttpAllowed</a>
</h3>

```typescript
isHttpAllowed?: pulumi.Input<boolean>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L183">property isHttpsAllowed</a>
</h3>

```typescript
isHttpsAllowed?: pulumi.Input<boolean>;
```


Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L187">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L191">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L195">property optimizationType</a>
</h3>

```typescript
optimizationType?: pulumi.Input<string>;
```


What types of optimization should this CDN Endpoint optimize for? Possible values include `DynamicSiteAcceleration`, `GeneralMediaStreaming`, `GeneralWebDelivery`, `LargeFileDownload` and `VideoOnDemandMediaStreaming`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L203">property originHostHeader</a>
</h3>

```typescript
originHostHeader?: pulumi.Input<string>;
```


The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L207">property originPath</a>
</h3>

```typescript
originPath?: pulumi.Input<string>;
```


The path used at for origin requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L199">property origins</a>
</h3>

```typescript
origins?: pulumi.Input<{ ... }[]>;
```


The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each `origin` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L211">property probePath</a>
</h3>

```typescript
probePath?: pulumi.Input<string>;
```


the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the `origin_path`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L215">property profileName</a>
</h3>

```typescript
profileName?: pulumi.Input<string>;
```


The CDN Profile to which to attach the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L219">property querystringCachingBehaviour</a>
</h3>

```typescript
querystringCachingBehaviour?: pulumi.Input<string>;
```


Sets query string caching behavior. Allowed values are `IgnoreQueryString`, `BypassCaching` and `UseQueryString`. Defaults to `IgnoreQueryString`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L223">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the CDN Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/endpoint.ts#L227">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="GetProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L19">interface GetProfileArgs</a>
</h2>

A collection of arguments for invoking getProfile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the CDN Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the CDN Profile exists.

<h2 class="pdoc-module-header" id="GetProfileResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L33">interface GetProfileResult</a>
</h2>

A collection of values returned by getProfile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L49">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L37">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L41">property sku</a>
</h3>

```typescript
sku: string;
```


The pricing related information of current CDN profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/getProfile.ts#L45">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="ProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L114">interface ProfileArgs</a>
</h2>

The set of arguments for constructing a Profile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L118">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L128">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the CDN Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L132">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


The pricing related information of current CDN profile. Accepted values are `Standard_Verizon`, `Standard_Akamai` or `Premium_Verizon`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L136">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ProfileState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L86">interface ProfileState</a>
</h2>

Input properties used for looking up and filtering Profile resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L90">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L100">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the CDN Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L104">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The pricing related information of current CDN profile. Accepted values are `Standard_Verizon`, `Standard_Akamai` or `Premium_Verizon`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cdn/profile.ts#L108">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

