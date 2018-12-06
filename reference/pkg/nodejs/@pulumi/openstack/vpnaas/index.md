---
title: Module vpnaas
---

<a href="../index.html">@pulumi/openstack</a> &gt; vpnaas

<h2 class="pdoc-module-header">Index</h2>

* <a href="#EndpointGroup">class EndpointGroup</a>
* <a href="#IkePolicy">class IkePolicy</a>
* <a href="#IpSecPolicy">class IpSecPolicy</a>
* <a href="#Service">class Service</a>
* <a href="#SiteConnection">class SiteConnection</a>
* <a href="#EndpointGroupArgs">interface EndpointGroupArgs</a>
* <a href="#EndpointGroupState">interface EndpointGroupState</a>
* <a href="#IkePolicyArgs">interface IkePolicyArgs</a>
* <a href="#IkePolicyState">interface IkePolicyState</a>
* <a href="#IpSecPolicyArgs">interface IpSecPolicyArgs</a>
* <a href="#IpSecPolicyState">interface IpSecPolicyState</a>
* <a href="#ServiceArgs">interface ServiceArgs</a>
* <a href="#ServiceState">interface ServiceState</a>
* <a href="#SiteConnectionArgs">interface SiteConnectionArgs</a>
* <a href="#SiteConnectionState">interface SiteConnectionState</a>

<a href="/vpnaas/endpointGroup.ts">vpnaas/endpointGroup.ts</a> <a href="/vpnaas/ikePolicy.ts">vpnaas/ikePolicy.ts</a> <a href="/vpnaas/ipSecPolicy.ts">vpnaas/ipSecPolicy.ts</a> <a href="/vpnaas/service.ts">vpnaas/service.ts</a> <a href="/vpnaas/siteConnection.ts">vpnaas/siteConnection.ts</a> 


<h2 class="pdoc-module-header" id="EndpointGroup">
<a class="pdoc-member-name" href="/vpnaas/endpointGroup.ts#L10">class EndpointGroup</a>
</h2>

Manages a V2 Neutron Endpoint Group resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L58">constructor</a>
</h3>

```typescript
new EndpointGroup(name: string, args?: EndpointGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EndpointGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EndpointGroupState, opts?: pulumi.CustomResourceOptions): EndpointGroup
```


Get an existing EndpointGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L27">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the group.
Changing this updates the description of the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L32">property endpoints</a>
</h3>

```typescript
public endpoints: pulumi.Output<string[] | undefined>;
```


List of endpoints of the same type, for the endpoint group. The values will depend on the type.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the group. Changing this updates the name of
the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L44">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an endpoint group. If omitted, the
`region` argument of the provider is used. Changing this creates a new
group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L49">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the group. Required if admin wants to
create an endpoint group for another project. Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L54">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L58">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IkePolicy">
<a class="pdoc-member-name" href="/vpnaas/ikePolicy.ts#L10">class IkePolicy</a>
</h2>

Manages a V2 Neutron IKE policy resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L81">constructor</a>
</h3>

```typescript
new IkePolicy(name: string, args?: IkePolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IkePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IkePolicyState, opts?: pulumi.CustomResourceOptions): IkePolicy
```


Get an existing IkePolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L27">property authAlgorithm</a>
</h3>

```typescript
public authAlgorithm: pulumi.Output<string | undefined>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L37">property encryptionAlgorithm</a>
</h3>

```typescript
public encryptionAlgorithm: pulumi.Output<string | undefined>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L42">property ikeVersion</a>
</h3>

```typescript
public ikeVersion: pulumi.Output<string | undefined>;
```


The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L50">property lifetimes</a>
</h3>

```typescript
public lifetimes: pulumi.Output<{ ... }[]>;
```


The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L55">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L60">property pfs</a>
</h3>

```typescript
public pfs: pulumi.Output<string | undefined>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L65">property phase1NegotiationMode</a>
</h3>

```typescript
public phase1NegotiationMode: pulumi.Output<string | undefined>;
```


The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L72">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L77">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L81">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IpSecPolicy">
<a class="pdoc-member-name" href="/vpnaas/ipSecPolicy.ts#L10">class IpSecPolicy</a>
</h2>

Manages a V2 Neutron IPSec policy resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L81">constructor</a>
</h3>

```typescript
new IpSecPolicy(name: string, args?: IpSecPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IpSecPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IpSecPolicyState, opts?: pulumi.CustomResourceOptions): IpSecPolicy
```


Get an existing IpSecPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L27">property authAlgorithm</a>
</h3>

```typescript
public authAlgorithm: pulumi.Output<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L37">property encapsulationMode</a>
</h3>

```typescript
public encapsulationMode: pulumi.Output<string>;
```


The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L42">property encryptionAlgorithm</a>
</h3>

```typescript
public encryptionAlgorithm: pulumi.Output<string>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L50">property lifetimes</a>
</h3>

```typescript
public lifetimes: pulumi.Output<{ ... }[]>;
```


The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L55">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L60">property pfs</a>
</h3>

```typescript
public pfs: pulumi.Output<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L67">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L72">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L77">property transformProtocol</a>
</h3>

```typescript
public transformProtocol: pulumi.Output<string>;
```


The transform protocol. Valid values are ESP, AH and AH-ESP.
Changing this updates the existing policy. Default is ESP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L81">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="/vpnaas/service.ts#L10">class Service</a>
</h2>

Manages a V2 Neutron VPN service resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L73">constructor</a>
</h3>

```typescript
new Service(name: string, args: ServiceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Service resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceState, opts?: pulumi.CustomResourceOptions): Service
```


Get an existing Service resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the service.
Changing this updates the description of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L36">property externalV4Ip</a>
</h3>

```typescript
public externalV4Ip: pulumi.Output<string>;
```


The read-only external (public) IPv4 address that is used for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L40">property externalV6Ip</a>
</h3>

```typescript
public externalV6Ip: pulumi.Output<string>;
```


The read-only external (public) IPv6 address that is used for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the service. Changing this updates the name of
the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L52">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L56">property routerId</a>
</h3>

```typescript
public routerId: pulumi.Output<string>;
```


The ID of the router. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L60">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L64">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string | undefined>;
```


SubnetID is the ID of the subnet. Default is null.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L69">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the service. Required if admin wants to
create a service for another project. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L73">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SiteConnection">
<a class="pdoc-member-name" href="/vpnaas/siteConnection.ts#L10">class SiteConnection</a>
</h2>

Manages a V2 Neutron IPSec site connection resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L118">constructor</a>
</h3>

```typescript
new SiteConnection(name: string, args: SiteConnectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SiteConnection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SiteConnectionState, opts?: pulumi.CustomResourceOptions): SiteConnection
```


Get an existing SiteConnection resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the connection.
Changing this updates the description of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L39">property dpds</a>
</h3>

```typescript
public dpds: pulumi.Output<{ ... }[]>;
```


A dictionary with dead peer detection (DPD) protocol controls.
- `action` - (Optional) The dead peer detection (DPD) action.
A valid value is clear, hold, restart, disabled, or restart-by-peer.
Default value is hold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L43">property ikepolicyId</a>
</h3>

```typescript
public ikepolicyId: pulumi.Output<string>;
```


The ID of the IKE policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L47">property initiator</a>
</h3>

```typescript
public initiator: pulumi.Output<string>;
```


A valid value is response-only or bi-directional. Default is bi-directional.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L51">property ipsecpolicyId</a>
</h3>

```typescript
public ipsecpolicyId: pulumi.Output<string>;
```


The ID of the IPsec policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L58">property localEpGroupId</a>
</h3>

```typescript
public localEpGroupId: pulumi.Output<string | undefined>;
```


The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L64">property localId</a>
</h3>

```typescript
public localId: pulumi.Output<string | undefined>;
```


An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L69">property mtu</a>
</h3>

```typescript
public mtu: pulumi.Output<number>;
```


The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L74">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the connection. Changing this updates the name of
the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L78">property peerAddress</a>
</h3>

```typescript
public peerAddress: pulumi.Output<string>;
```


The peer gateway public IPv4 or IPv6 address or FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L82">property peerCidrs</a>
</h3>

```typescript
public peerCidrs: pulumi.Output<string[] | undefined>;
```


Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L88">property peerEpGroupId</a>
</h3>

```typescript
public peerEpGroupId: pulumi.Output<string | undefined>;
```


The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L94">property peerId</a>
</h3>

```typescript
public peerId: pulumi.Output<string>;
```


The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L98">property psk</a>
</h3>

```typescript
public psk: pulumi.Output<string>;
```


The pre-shared key. A valid value is any string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L105">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
`region` argument of the provider is used. Changing this creates a new
site connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L110">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the connection. Required if admin wants to
create a connection for another project. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L114">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L118">property vpnserviceId</a>
</h3>

```typescript
public vpnserviceId: pulumi.Output<string>;
```


The ID of the VPN service. Changing this creates a new connection.

<h2 class="pdoc-module-header" id="EndpointGroupArgs">
<a class="pdoc-member-name" href="/vpnaas/endpointGroup.ts#L138">interface EndpointGroupArgs</a>
</h2>

The set of arguments for constructing a EndpointGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L143">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the group.
Changing this updates the description of the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L148">property endpoints</a>
</h3>

```typescript
endpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


List of endpoints of the same type, for the endpoint group. The values will depend on the type.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L153">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the group. Changing this updates the name of
the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L160">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an endpoint group. If omitted, the
`region` argument of the provider is used. Changing this creates a new
group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L165">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the group. Required if admin wants to
create an endpoint group for another project. Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L170">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L174">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="EndpointGroupState">
<a class="pdoc-member-name" href="/vpnaas/endpointGroup.ts#L96">interface EndpointGroupState</a>
</h2>

Input properties used for looking up and filtering EndpointGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L101">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the group.
Changing this updates the description of the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L106">property endpoints</a>
</h3>

```typescript
endpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


List of endpoints of the same type, for the endpoint group. The values will depend on the type.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the group. Changing this updates the name of
the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L118">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an endpoint group. If omitted, the
`region` argument of the provider is used. Changing this creates a new
group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L123">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the group. Required if admin wants to
create an endpoint group for another project. Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L128">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L132">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IkePolicyArgs">
<a class="pdoc-member-name" href="/vpnaas/ikePolicy.ts#L192">interface IkePolicyArgs</a>
</h2>

The set of arguments for constructing a IkePolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L197">property authAlgorithm</a>
</h3>

```typescript
authAlgorithm?: pulumi.Input<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L202">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L207">property encryptionAlgorithm</a>
</h3>

```typescript
encryptionAlgorithm?: pulumi.Input<string>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L212">property ikeVersion</a>
</h3>

```typescript
ikeVersion?: pulumi.Input<string>;
```


The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L220">property lifetimes</a>
</h3>

```typescript
lifetimes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L225">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L230">property pfs</a>
</h3>

```typescript
pfs?: pulumi.Input<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L235">property phase1NegotiationMode</a>
</h3>

```typescript
phase1NegotiationMode?: pulumi.Input<string>;
```


The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L242">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L247">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L251">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IkePolicyState">
<a class="pdoc-member-name" href="/vpnaas/ikePolicy.ts#L127">interface IkePolicyState</a>
</h2>

Input properties used for looking up and filtering IkePolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L132">property authAlgorithm</a>
</h3>

```typescript
authAlgorithm?: pulumi.Input<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L137">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L142">property encryptionAlgorithm</a>
</h3>

```typescript
encryptionAlgorithm?: pulumi.Input<string>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L147">property ikeVersion</a>
</h3>

```typescript
ikeVersion?: pulumi.Input<string>;
```


The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L155">property lifetimes</a>
</h3>

```typescript
lifetimes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L160">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L165">property pfs</a>
</h3>

```typescript
pfs?: pulumi.Input<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L170">property phase1NegotiationMode</a>
</h3>

```typescript
phase1NegotiationMode?: pulumi.Input<string>;
```


The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L177">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L182">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L186">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IpSecPolicyArgs">
<a class="pdoc-member-name" href="/vpnaas/ipSecPolicy.ts#L192">interface IpSecPolicyArgs</a>
</h2>

The set of arguments for constructing a IpSecPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L197">property authAlgorithm</a>
</h3>

```typescript
authAlgorithm?: pulumi.Input<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L202">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L207">property encapsulationMode</a>
</h3>

```typescript
encapsulationMode?: pulumi.Input<string>;
```


The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L212">property encryptionAlgorithm</a>
</h3>

```typescript
encryptionAlgorithm?: pulumi.Input<string>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L220">property lifetimes</a>
</h3>

```typescript
lifetimes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L225">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L230">property pfs</a>
</h3>

```typescript
pfs?: pulumi.Input<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L237">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L242">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L247">property transformProtocol</a>
</h3>

```typescript
transformProtocol?: pulumi.Input<string>;
```


The transform protocol. Valid values are ESP, AH and AH-ESP.
Changing this updates the existing policy. Default is ESP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L251">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IpSecPolicyState">
<a class="pdoc-member-name" href="/vpnaas/ipSecPolicy.ts#L127">interface IpSecPolicyState</a>
</h2>

Input properties used for looking up and filtering IpSecPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L132">property authAlgorithm</a>
</h3>

```typescript
authAlgorithm?: pulumi.Input<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L137">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L142">property encapsulationMode</a>
</h3>

```typescript
encapsulationMode?: pulumi.Input<string>;
```


The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L147">property encryptionAlgorithm</a>
</h3>

```typescript
encryptionAlgorithm?: pulumi.Input<string>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L155">property lifetimes</a>
</h3>

```typescript
lifetimes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L160">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L165">property pfs</a>
</h3>

```typescript
pfs?: pulumi.Input<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L172">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L177">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L182">property transformProtocol</a>
</h3>

```typescript
transformProtocol?: pulumi.Input<string>;
```


The transform protocol. Valid values are ESP, AH and AH-ESP.
Changing this updates the existing policy. Default is ESP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipSecPolicy.ts#L186">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="ServiceArgs">
<a class="pdoc-member-name" href="/vpnaas/service.ts#L179">interface ServiceArgs</a>
</h2>

The set of arguments for constructing a Service resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L184">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L189">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the service.
Changing this updates the description of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L194">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the service. Changing this updates the name of
the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L201">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L205">property routerId</a>
</h3>

```typescript
routerId: pulumi.Input<string>;
```


The ID of the router. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L209">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


SubnetID is the ID of the subnet. Default is null.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L214">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the service. Required if admin wants to
create a service for another project. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L218">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="ServiceState">
<a class="pdoc-member-name" href="/vpnaas/service.ts#L122">interface ServiceState</a>
</h2>

Input properties used for looking up and filtering Service resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L127">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L132">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the service.
Changing this updates the description of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L136">property externalV4Ip</a>
</h3>

```typescript
externalV4Ip?: pulumi.Input<string>;
```


The read-only external (public) IPv4 address that is used for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L140">property externalV6Ip</a>
</h3>

```typescript
externalV6Ip?: pulumi.Input<string>;
```


The read-only external (public) IPv6 address that is used for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L145">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the service. Changing this updates the name of
the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L152">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L156">property routerId</a>
</h3>

```typescript
routerId?: pulumi.Input<string>;
```


The ID of the router. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L160">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L164">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


SubnetID is the ID of the subnet. Default is null.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L169">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the service. Required if admin wants to
create a service for another project. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L173">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SiteConnectionArgs">
<a class="pdoc-member-name" href="/vpnaas/siteConnection.ts#L300">interface SiteConnectionArgs</a>
</h2>

The set of arguments for constructing a SiteConnection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L305">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L310">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the connection.
Changing this updates the description of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L317">property dpds</a>
</h3>

```typescript
dpds?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A dictionary with dead peer detection (DPD) protocol controls.
- `action` - (Optional) The dead peer detection (DPD) action.
A valid value is clear, hold, restart, disabled, or restart-by-peer.
Default value is hold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L321">property ikepolicyId</a>
</h3>

```typescript
ikepolicyId: pulumi.Input<string>;
```


The ID of the IKE policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L325">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


A valid value is response-only or bi-directional. Default is bi-directional.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L329">property ipsecpolicyId</a>
</h3>

```typescript
ipsecpolicyId: pulumi.Input<string>;
```


The ID of the IPsec policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L336">property localEpGroupId</a>
</h3>

```typescript
localEpGroupId?: pulumi.Input<string>;
```


The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L342">property localId</a>
</h3>

```typescript
localId?: pulumi.Input<string>;
```


An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L347">property mtu</a>
</h3>

```typescript
mtu?: pulumi.Input<number>;
```


The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L352">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection. Changing this updates the name of
the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L356">property peerAddress</a>
</h3>

```typescript
peerAddress: pulumi.Input<string>;
```


The peer gateway public IPv4 or IPv6 address or FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L360">property peerCidrs</a>
</h3>

```typescript
peerCidrs?: pulumi.Input<pulumi.Input<string>[]>;
```


Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L366">property peerEpGroupId</a>
</h3>

```typescript
peerEpGroupId?: pulumi.Input<string>;
```


The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L372">property peerId</a>
</h3>

```typescript
peerId: pulumi.Input<string>;
```


The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L376">property psk</a>
</h3>

```typescript
psk: pulumi.Input<string>;
```


The pre-shared key. A valid value is any string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L383">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
`region` argument of the provider is used. Changing this creates a new
site connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L388">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the connection. Required if admin wants to
create a connection for another project. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L392">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L396">property vpnserviceId</a>
</h3>

```typescript
vpnserviceId: pulumi.Input<string>;
```


The ID of the VPN service. Changing this creates a new connection.

<h2 class="pdoc-module-header" id="SiteConnectionState">
<a class="pdoc-member-name" href="/vpnaas/siteConnection.ts#L198">interface SiteConnectionState</a>
</h2>

Input properties used for looking up and filtering SiteConnection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L203">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L208">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the connection.
Changing this updates the description of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L215">property dpds</a>
</h3>

```typescript
dpds?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A dictionary with dead peer detection (DPD) protocol controls.
- `action` - (Optional) The dead peer detection (DPD) action.
A valid value is clear, hold, restart, disabled, or restart-by-peer.
Default value is hold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L219">property ikepolicyId</a>
</h3>

```typescript
ikepolicyId?: pulumi.Input<string>;
```


The ID of the IKE policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L223">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


A valid value is response-only or bi-directional. Default is bi-directional.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L227">property ipsecpolicyId</a>
</h3>

```typescript
ipsecpolicyId?: pulumi.Input<string>;
```


The ID of the IPsec policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L234">property localEpGroupId</a>
</h3>

```typescript
localEpGroupId?: pulumi.Input<string>;
```


The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L240">property localId</a>
</h3>

```typescript
localId?: pulumi.Input<string>;
```


An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L245">property mtu</a>
</h3>

```typescript
mtu?: pulumi.Input<number>;
```


The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L250">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection. Changing this updates the name of
the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L254">property peerAddress</a>
</h3>

```typescript
peerAddress?: pulumi.Input<string>;
```


The peer gateway public IPv4 or IPv6 address or FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L258">property peerCidrs</a>
</h3>

```typescript
peerCidrs?: pulumi.Input<pulumi.Input<string>[]>;
```


Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L264">property peerEpGroupId</a>
</h3>

```typescript
peerEpGroupId?: pulumi.Input<string>;
```


The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L270">property peerId</a>
</h3>

```typescript
peerId?: pulumi.Input<string>;
```


The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L274">property psk</a>
</h3>

```typescript
psk?: pulumi.Input<string>;
```


The pre-shared key. A valid value is any string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L281">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
`region` argument of the provider is used. Changing this creates a new
site connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L286">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the connection. Required if admin wants to
create a connection for another project. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L290">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L294">property vpnserviceId</a>
</h3>

```typescript
vpnserviceId?: pulumi.Input<string>;
```


The ID of the VPN service. Changing this creates a new connection.

