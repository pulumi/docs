---
title: Module trafficmanager
---

<a href="../index.html">@pulumi/azure</a> &gt; trafficmanager

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Endpoint">class Endpoint</a>
* <a href="#Profile">class Profile</a>
* <a href="#getGeographicalLocation">function getGeographicalLocation</a>
* <a href="#EndpointArgs">interface EndpointArgs</a>
* <a href="#EndpointState">interface EndpointState</a>
* <a href="#GetGeographicalLocationArgs">interface GetGeographicalLocationArgs</a>
* <a href="#GetGeographicalLocationResult">interface GetGeographicalLocationResult</a>
* <a href="#ProfileArgs">interface ProfileArgs</a>
* <a href="#ProfileState">interface ProfileState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts">trafficmanager/endpoint.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/getGeographicalLocation.ts">trafficmanager/getGeographicalLocation.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts">trafficmanager/profile.ts</a> 


<h2 class="pdoc-module-header" id="Endpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L10">class Endpoint</a>
</h2>

Manages a Traffic Manager Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L95">constructor</a>
</h3>

```typescript
new Endpoint(name: string, args: EndpointArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Endpoint resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L30">property endpointLocation</a>
</h3>

```typescript
public endpointLocation: pulumi.Output<string>;
```


Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the `Performance` routing method
if the Endpoint is of either type `nestedEndpoints` or `externalEndpoints`.
For Endpoints of type `azureEndpoints` the value will be taken from the
location of the Azure target resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L31">property endpointMonitorStatus</a>
</h3>

```typescript
public endpointMonitorStatus: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L36">property endpointStatus</a>
</h3>

```typescript
public endpointStatus: pulumi.Output<string>;
```


The status of the Endpoint, can be set to
either `Enabled` or `Disabled`. Defaults to `Enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L40">property geoMappings</a>
</h3>

```typescript
public geoMappings: pulumi.Output<string[] | undefined>;
```


A list of Geographic Regions used to distribute traffic, such as `WORLD`, `UK` or `DE`. The same location can't be specified in two endpoints. [See the Geographic Hierarchies documentation for more information](https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L48">property minChildEndpoints</a>
</h3>

```typescript
public minChildEndpoints: pulumi.Output<number | undefined>;
```


This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type `nestedEndpoints`
and defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L60">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<number>;
```


Specifies the priority of this Endpoint, this must be
specified for Profiles using the `Priority` traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L65">property profileName</a>
</h3>

```typescript
public profileName: pulumi.Output<string>;
```


The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L70">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the Traffic Manager endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L76">property target</a>
</h3>

```typescript
public target: pulumi.Output<string>;
```


The FQDN DNS name of the target. This argument must be
provided for an endpoint of type `externalEndpoints`, for other types it
will be computed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L82">property targetResourceId</a>
</h3>

```typescript
public targetResourceId: pulumi.Output<string | undefined>;
```


The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
`azureEndpoints` or `nestedEndpoints`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L89">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The Endpoint type, must be one of:
- `azureEndpoints`
- `externalEndpoints`
- `nestedEndpoints`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L95">property weight</a>
</h3>

```typescript
public weight: pulumi.Output<number>;
```


Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  `Weighted` traffic
routing method. Supports values between 1 and 1000.

<h2 class="pdoc-module-header" id="Profile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L10">class Profile</a>
</h2>

Manages a Traffic Manager Profile to which multiple endpoints can be attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L64">constructor</a>
</h3>

```typescript
new Profile(name: string, args: ProfileArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Profile resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L27">property dnsConfigs</a>
</h3>

```typescript
public dnsConfigs: pulumi.Output<{ ... }[]>;
```


This block specifies the DNS configuration of the
Profile, it supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L31">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


The FQDN of the created Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L36">property monitorConfigs</a>
</h3>

```typescript
public monitorConfigs: pulumi.Output<{ ... }[]>;
```


This block specifies the Endpoint monitoring
configuration for the Profile, it supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the virtual network. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L46">property profileStatus</a>
</h3>

```typescript
public profileStatus: pulumi.Output<string>;
```


The status of the profile, can be set to either
`Enabled` or `Disabled`. Defaults to `Enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L51">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L55">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L64">property trafficRoutingMethod</a>
</h3>

```typescript
public trafficRoutingMethod: pulumi.Output<string>;
```


Specifies the algorithm used to route
traffic, possible values are:
- `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
- `Performance` - Traffic is routed via the User's closest Endpoint
- `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
- `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getGeographicalLocation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/getGeographicalLocation.ts#L10">function getGeographicalLocation</a>
</h2>

```typescript
getGeographicalLocation(args: GetGeographicalLocationArgs, opts?: pulumi.InvokeOptions): Promise<GetGeographicalLocationResult>
```


Use this data source to access the ID of a specified Traffic Manager Geographical Location within the Geographical Hierarchy.

<h2 class="pdoc-module-header" id="EndpointArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L233">interface EndpointArgs</a>
</h2>

The set of arguments for constructing a Endpoint resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L241">property endpointLocation</a>
</h3>

```typescript
endpointLocation?: pulumi.Input<string>;
```


Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the `Performance` routing method
if the Endpoint is of either type `nestedEndpoints` or `externalEndpoints`.
For Endpoints of type `azureEndpoints` the value will be taken from the
location of the Azure target resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L246">property endpointStatus</a>
</h3>

```typescript
endpointStatus?: pulumi.Input<string>;
```


The status of the Endpoint, can be set to
either `Enabled` or `Disabled`. Defaults to `Enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L250">property geoMappings</a>
</h3>

```typescript
geoMappings?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Geographic Regions used to distribute traffic, such as `WORLD`, `UK` or `DE`. The same location can't be specified in two endpoints. [See the Geographic Hierarchies documentation for more information](https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L258">property minChildEndpoints</a>
</h3>

```typescript
minChildEndpoints?: pulumi.Input<number>;
```


This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type `nestedEndpoints`
and defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L263">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L270">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


Specifies the priority of this Endpoint, this must be
specified for Profiles using the `Priority` traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L275">property profileName</a>
</h3>

```typescript
profileName: pulumi.Input<string>;
```


The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L280">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the Traffic Manager endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L286">property target</a>
</h3>

```typescript
target?: pulumi.Input<string>;
```


The FQDN DNS name of the target. This argument must be
provided for an endpoint of type `externalEndpoints`, for other types it
will be computed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L292">property targetResourceId</a>
</h3>

```typescript
targetResourceId?: pulumi.Input<string>;
```


The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
`azureEndpoints` or `nestedEndpoints`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L299">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The Endpoint type, must be one of:
- `azureEndpoints`
- `externalEndpoints`
- `nestedEndpoints`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L305">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  `Weighted` traffic
routing method. Supports values between 1 and 1000.

<h2 class="pdoc-module-header" id="EndpointState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L154">interface EndpointState</a>
</h2>

Input properties used for looking up and filtering Endpoint resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L162">property endpointLocation</a>
</h3>

```typescript
endpointLocation?: pulumi.Input<string>;
```


Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the `Performance` routing method
if the Endpoint is of either type `nestedEndpoints` or `externalEndpoints`.
For Endpoints of type `azureEndpoints` the value will be taken from the
location of the Azure target resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L163">property endpointMonitorStatus</a>
</h3>

```typescript
endpointMonitorStatus?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L168">property endpointStatus</a>
</h3>

```typescript
endpointStatus?: pulumi.Input<string>;
```


The status of the Endpoint, can be set to
either `Enabled` or `Disabled`. Defaults to `Enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L172">property geoMappings</a>
</h3>

```typescript
geoMappings?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Geographic Regions used to distribute traffic, such as `WORLD`, `UK` or `DE`. The same location can't be specified in two endpoints. [See the Geographic Hierarchies documentation for more information](https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L180">property minChildEndpoints</a>
</h3>

```typescript
minChildEndpoints?: pulumi.Input<number>;
```


This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type `nestedEndpoints`
and defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L185">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L192">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


Specifies the priority of this Endpoint, this must be
specified for Profiles using the `Priority` traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L197">property profileName</a>
</h3>

```typescript
profileName?: pulumi.Input<string>;
```


The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L202">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the Traffic Manager endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L208">property target</a>
</h3>

```typescript
target?: pulumi.Input<string>;
```


The FQDN DNS name of the target. This argument must be
provided for an endpoint of type `externalEndpoints`, for other types it
will be computed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L214">property targetResourceId</a>
</h3>

```typescript
targetResourceId?: pulumi.Input<string>;
```


The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
`azureEndpoints` or `nestedEndpoints`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L221">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The Endpoint type, must be one of:
- `azureEndpoints`
- `externalEndpoints`
- `nestedEndpoints`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/endpoint.ts#L227">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  `Weighted` traffic
routing method. Supports values between 1 and 1000.

<h2 class="pdoc-module-header" id="GetGeographicalLocationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/getGeographicalLocation.ts#L19">interface GetGeographicalLocationArgs</a>
</h2>

A collection of arguments for invoking getGeographicalLocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/getGeographicalLocation.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Location, for example `World`, `Europe` or `Germany`.

<h2 class="pdoc-module-header" id="GetGeographicalLocationResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/getGeographicalLocation.ts#L29">interface GetGeographicalLocationResult</a>
</h2>

A collection of values returned by getGeographicalLocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/getGeographicalLocation.ts#L33">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="ProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L164">interface ProfileArgs</a>
</h2>

The set of arguments for constructing a Profile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L169">property dnsConfigs</a>
</h3>

```typescript
dnsConfigs: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


This block specifies the DNS configuration of the
Profile, it supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L174">property monitorConfigs</a>
</h3>

```typescript
monitorConfigs: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


This block specifies the Endpoint monitoring
configuration for the Profile, it supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L179">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual network. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L184">property profileStatus</a>
</h3>

```typescript
profileStatus?: pulumi.Input<string>;
```


The status of the profile, can be set to either
`Enabled` or `Disabled`. Defaults to `Enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L189">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L193">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L202">property trafficRoutingMethod</a>
</h3>

```typescript
trafficRoutingMethod: pulumi.Input<string>;
```


Specifies the algorithm used to route
traffic, possible values are:
- `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
- `Performance` - Traffic is routed via the User's closest Endpoint
- `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
- `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.

<h2 class="pdoc-module-header" id="ProfileState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L116">interface ProfileState</a>
</h2>

Input properties used for looking up and filtering Profile resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L121">property dnsConfigs</a>
</h3>

```typescript
dnsConfigs?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


This block specifies the DNS configuration of the
Profile, it supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L125">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The FQDN of the created Profile.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L130">property monitorConfigs</a>
</h3>

```typescript
monitorConfigs?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


This block specifies the Endpoint monitoring
configuration for the Profile, it supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual network. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L140">property profileStatus</a>
</h3>

```typescript
profileStatus?: pulumi.Input<string>;
```


The status of the profile, can be set to either
`Enabled` or `Disabled`. Defaults to `Enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L145">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L149">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/trafficmanager/profile.ts#L158">property trafficRoutingMethod</a>
</h3>

```typescript
trafficRoutingMethod?: pulumi.Input<string>;
```


Specifies the algorithm used to route
traffic, possible values are:
- `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
- `Performance` - Traffic is routed via the User's closest Endpoint
- `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
- `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.

