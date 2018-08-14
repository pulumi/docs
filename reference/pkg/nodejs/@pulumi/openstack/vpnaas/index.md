---
title: Module vpnaas
---

<a href="../index.html">@pulumi/openstack</a> &gt; vpnaas

<h2 class="pdoc-module-header">Index</h2>

* <a href="#EndpointGroup">class EndpointGroup</a>
* <a href="#IkePolicy">class IkePolicy</a>
* <a href="#IpsecPolicy">class IpsecPolicy</a>
* <a href="#Service">class Service</a>
* <a href="#SiteConnection">class SiteConnection</a>
* <a href="#EndpointGroupArgs">interface EndpointGroupArgs</a>
* <a href="#EndpointGroupState">interface EndpointGroupState</a>
* <a href="#IkePolicyArgs">interface IkePolicyArgs</a>
* <a href="#IkePolicyState">interface IkePolicyState</a>
* <a href="#IpsecPolicyArgs">interface IpsecPolicyArgs</a>
* <a href="#IpsecPolicyState">interface IpsecPolicyState</a>
* <a href="#ServiceArgs">interface ServiceArgs</a>
* <a href="#ServiceState">interface ServiceState</a>
* <a href="#SiteConnectionArgs">interface SiteConnectionArgs</a>
* <a href="#SiteConnectionState">interface SiteConnectionState</a>

<a href="/vpnaas/endpointGroup.ts">vpnaas/endpointGroup.ts</a> <a href="/vpnaas/ikePolicy.ts">vpnaas/ikePolicy.ts</a> <a href="/vpnaas/ipsecPolicy.ts">vpnaas/ipsecPolicy.ts</a> <a href="/vpnaas/service.ts">vpnaas/service.ts</a> <a href="/vpnaas/siteConnection.ts">vpnaas/siteConnection.ts</a> 


<h2 class="pdoc-module-header" id="EndpointGroup">
<a class="pdoc-member-name" href="/vpnaas/endpointGroup.ts#L9">class EndpointGroup</a>
</h2>

Manages a V2 Neutron Endpoint Group resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L57">constructor</a>
</h3>

```typescript
new EndpointGroup(name: string, args?: EndpointGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EndpointGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EndpointGroupState): EndpointGroup
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
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the group.
Changing this updates the description of the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L31">property endpoints</a>
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
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the group. Changing this updates the name of
the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L43">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an endpoint group. If omitted, the
`region` argument of the provider is used. Changing this creates a new
group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L48">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the group. Required if admin wants to
create an endpoint group for another project. Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L53">property type</a>
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
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L57">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IkePolicy">
<a class="pdoc-member-name" href="/vpnaas/ikePolicy.ts#L9">class IkePolicy</a>
</h2>

Manages a V2 Neutron IKE policy resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L80">constructor</a>
</h3>

```typescript
new IkePolicy(name: string, args?: IkePolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IkePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IkePolicyState): IkePolicy
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
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L26">property authAlgorithm</a>
</h3>

```typescript
public authAlgorithm: pulumi.Output<string | undefined>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L36">property encryptionAlgorithm</a>
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
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L41">property ikeVersion</a>
</h3>

```typescript
public ikeVersion: pulumi.Output<string | undefined>;
```


The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L49">property lifetimes</a>
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
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L59">property pfs</a>
</h3>

```typescript
public pfs: pulumi.Output<string | undefined>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L64">property phase1NegotiationMode</a>
</h3>

```typescript
public phase1NegotiationMode: pulumi.Output<string | undefined>;
```


The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L71">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L76">property tenantId</a>
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
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L80">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IpsecPolicy">
<a class="pdoc-member-name" href="/vpnaas/ipsecPolicy.ts#L9">class IpsecPolicy</a>
</h2>

Manages a V2 Neutron IPSec policy resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L80">constructor</a>
</h3>

```typescript
new IpsecPolicy(name: string, args?: IpsecPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IpsecPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IpsecPolicyState): IpsecPolicy
```


Get an existing IpsecPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L26">property authAlgorithm</a>
</h3>

```typescript
public authAlgorithm: pulumi.Output<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L36">property encapsulationMode</a>
</h3>

```typescript
public encapsulationMode: pulumi.Output<string>;
```


The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L41">property encryptionAlgorithm</a>
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
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L49">property lifetimes</a>
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
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L59">property pfs</a>
</h3>

```typescript
public pfs: pulumi.Output<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L66">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L71">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L76">property transformProtocol</a>
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
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L80">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="/vpnaas/service.ts#L9">class Service</a>
</h2>

Manages a V2 Neutron VPN service resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L72">constructor</a>
</h3>

```typescript
new Service(name: string, args: ServiceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Service resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceState): Service
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
<a class="pdoc-child-name" href="/vpnaas/service.ts#L26">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the service.
Changing this updates the description of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L35">property externalV4Ip</a>
</h3>

```typescript
public externalV4Ip: pulumi.Output<string>;
```


The read-only external (public) IPv4 address that is used for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L39">property externalV6Ip</a>
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
<a class="pdoc-child-name" href="/vpnaas/service.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the service. Changing this updates the name of
the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L51">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L55">property routerId</a>
</h3>

```typescript
public routerId: pulumi.Output<string>;
```


The ID of the router. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L59">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L63">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string | undefined>;
```


SubnetID is the ID of the subnet. Default is null.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L68">property tenantId</a>
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
<a class="pdoc-child-name" href="/vpnaas/service.ts#L72">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SiteConnection">
<a class="pdoc-member-name" href="/vpnaas/siteConnection.ts#L9">class SiteConnection</a>
</h2>

Manages a V2 Neutron IPSec site connection resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L117">constructor</a>
</h3>

```typescript
new SiteConnection(name: string, args: SiteConnectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SiteConnection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SiteConnectionState): SiteConnection
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
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L26">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the connection.
Changing this updates the description of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L38">property dpds</a>
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
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L42">property ikepolicyId</a>
</h3>

```typescript
public ikepolicyId: pulumi.Output<string>;
```


The ID of the IKE policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L46">property initiator</a>
</h3>

```typescript
public initiator: pulumi.Output<string>;
```


A valid value is response-only or bi-directional. Default is bi-directional.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L50">property ipsecpolicyId</a>
</h3>

```typescript
public ipsecpolicyId: pulumi.Output<string>;
```


The ID of the IPsec policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L57">property localEpGroupId</a>
</h3>

```typescript
public localEpGroupId: pulumi.Output<string | undefined>;
```


The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L63">property localId</a>
</h3>

```typescript
public localId: pulumi.Output<string | undefined>;
```


An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L68">property mtu</a>
</h3>

```typescript
public mtu: pulumi.Output<number>;
```


The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L73">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the connection. Changing this updates the name of
the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L77">property peerAddress</a>
</h3>

```typescript
public peerAddress: pulumi.Output<string>;
```


The peer gateway public IPv4 or IPv6 address or FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L81">property peerCidrs</a>
</h3>

```typescript
public peerCidrs: pulumi.Output<string[] | undefined>;
```


Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L87">property peerEpGroupId</a>
</h3>

```typescript
public peerEpGroupId: pulumi.Output<string | undefined>;
```


The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L93">property peerId</a>
</h3>

```typescript
public peerId: pulumi.Output<string>;
```


The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L97">property psk</a>
</h3>

```typescript
public psk: pulumi.Output<string>;
```


The pre-shared key. A valid value is any string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L104">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
`region` argument of the provider is used. Changing this creates a new
site connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L109">property tenantId</a>
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
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L113">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L117">property vpnserviceId</a>
</h3>

```typescript
public vpnserviceId: pulumi.Output<string>;
```


The ID of the VPN service. Changing this creates a new connection.

<h2 class="pdoc-module-header" id="EndpointGroupArgs">
<a class="pdoc-member-name" href="/vpnaas/endpointGroup.ts#L137">interface EndpointGroupArgs</a>
</h2>

The set of arguments for constructing a EndpointGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L142">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the group.
Changing this updates the description of the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L147">property endpoints</a>
</h3>

```typescript
endpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


List of endpoints of the same type, for the endpoint group. The values will depend on the type.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L152">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the group. Changing this updates the name of
the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L159">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an endpoint group. If omitted, the
`region` argument of the provider is used. Changing this creates a new
group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L164">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the group. Required if admin wants to
create an endpoint group for another project. Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L169">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L173">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="EndpointGroupState">
<a class="pdoc-member-name" href="/vpnaas/endpointGroup.ts#L95">interface EndpointGroupState</a>
</h2>

Input properties used for looking up and filtering EndpointGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L100">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the group.
Changing this updates the description of the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L105">property endpoints</a>
</h3>

```typescript
endpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


List of endpoints of the same type, for the endpoint group. The values will depend on the type.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the group. Changing this updates the name of
the existing group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L117">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an endpoint group. If omitted, the
`region` argument of the provider is used. Changing this creates a new
group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L122">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the group. Required if admin wants to
create an endpoint group for another project. Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L127">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
Changing this creates a new group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/endpointGroup.ts#L131">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IkePolicyArgs">
<a class="pdoc-member-name" href="/vpnaas/ikePolicy.ts#L191">interface IkePolicyArgs</a>
</h2>

The set of arguments for constructing a IkePolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L196">property authAlgorithm</a>
</h3>

```typescript
authAlgorithm?: pulumi.Input<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L201">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L206">property encryptionAlgorithm</a>
</h3>

```typescript
encryptionAlgorithm?: pulumi.Input<string>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L211">property ikeVersion</a>
</h3>

```typescript
ikeVersion?: pulumi.Input<string>;
```


The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L219">property lifetimes</a>
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
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L224">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L229">property pfs</a>
</h3>

```typescript
pfs?: pulumi.Input<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L234">property phase1NegotiationMode</a>
</h3>

```typescript
phase1NegotiationMode?: pulumi.Input<string>;
```


The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L241">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L246">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L250">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IkePolicyState">
<a class="pdoc-member-name" href="/vpnaas/ikePolicy.ts#L126">interface IkePolicyState</a>
</h2>

Input properties used for looking up and filtering IkePolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L131">property authAlgorithm</a>
</h3>

```typescript
authAlgorithm?: pulumi.Input<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L136">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L141">property encryptionAlgorithm</a>
</h3>

```typescript
encryptionAlgorithm?: pulumi.Input<string>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L146">property ikeVersion</a>
</h3>

```typescript
ikeVersion?: pulumi.Input<string>;
```


The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L154">property lifetimes</a>
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
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L164">property pfs</a>
</h3>

```typescript
pfs?: pulumi.Input<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L169">property phase1NegotiationMode</a>
</h3>

```typescript
phase1NegotiationMode?: pulumi.Input<string>;
```


The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L176">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L181">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ikePolicy.ts#L185">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IpsecPolicyArgs">
<a class="pdoc-member-name" href="/vpnaas/ipsecPolicy.ts#L191">interface IpsecPolicyArgs</a>
</h2>

The set of arguments for constructing a IpsecPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L196">property authAlgorithm</a>
</h3>

```typescript
authAlgorithm?: pulumi.Input<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L201">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L206">property encapsulationMode</a>
</h3>

```typescript
encapsulationMode?: pulumi.Input<string>;
```


The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L211">property encryptionAlgorithm</a>
</h3>

```typescript
encryptionAlgorithm?: pulumi.Input<string>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L219">property lifetimes</a>
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
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L224">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L229">property pfs</a>
</h3>

```typescript
pfs?: pulumi.Input<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L236">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L241">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L246">property transformProtocol</a>
</h3>

```typescript
transformProtocol?: pulumi.Input<string>;
```


The transform protocol. Valid values are ESP, AH and AH-ESP.
Changing this updates the existing policy. Default is ESP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L250">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="IpsecPolicyState">
<a class="pdoc-member-name" href="/vpnaas/ipsecPolicy.ts#L126">interface IpsecPolicyState</a>
</h2>

Input properties used for looking up and filtering IpsecPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L131">property authAlgorithm</a>
</h3>

```typescript
authAlgorithm?: pulumi.Input<string>;
```


The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L136">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the policy.
Changing this updates the description of the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L141">property encapsulationMode</a>
</h3>

```typescript
encapsulationMode?: pulumi.Input<string>;
```


The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L146">property encryptionAlgorithm</a>
</h3>

```typescript
encryptionAlgorithm?: pulumi.Input<string>;
```


The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L154">property lifetimes</a>
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
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy. Changing this updates the name of
the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L164">property pfs</a>
</h3>

```typescript
pfs?: pulumi.Input<string>;
```


The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L171">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L176">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L181">property transformProtocol</a>
</h3>

```typescript
transformProtocol?: pulumi.Input<string>;
```


The transform protocol. Valid values are ESP, AH and AH-ESP.
Changing this updates the existing policy. Default is ESP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/ipsecPolicy.ts#L185">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="ServiceArgs">
<a class="pdoc-member-name" href="/vpnaas/service.ts#L178">interface ServiceArgs</a>
</h2>

The set of arguments for constructing a Service resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L183">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L188">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the service.
Changing this updates the description of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L193">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the service. Changing this updates the name of
the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L200">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L204">property routerId</a>
</h3>

```typescript
routerId: pulumi.Input<string>;
```


The ID of the router. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L208">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


SubnetID is the ID of the subnet. Default is null.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L213">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the service. Required if admin wants to
create a service for another project. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L217">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="ServiceState">
<a class="pdoc-member-name" href="/vpnaas/service.ts#L121">interface ServiceState</a>
</h2>

Input properties used for looking up and filtering Service resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L126">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L131">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the service.
Changing this updates the description of the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L135">property externalV4Ip</a>
</h3>

```typescript
externalV4Ip?: pulumi.Input<string>;
```


The read-only external (public) IPv4 address that is used for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L139">property externalV6Ip</a>
</h3>

```typescript
externalV6Ip?: pulumi.Input<string>;
```


The read-only external (public) IPv6 address that is used for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L144">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the service. Changing this updates the name of
the existing service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L151">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L155">property routerId</a>
</h3>

```typescript
routerId?: pulumi.Input<string>;
```


The ID of the router. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L159">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L163">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


SubnetID is the ID of the subnet. Default is null.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L168">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the service. Required if admin wants to
create a service for another project. Changing this creates a new service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/service.ts#L172">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SiteConnectionArgs">
<a class="pdoc-member-name" href="/vpnaas/siteConnection.ts#L299">interface SiteConnectionArgs</a>
</h2>

The set of arguments for constructing a SiteConnection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L304">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L309">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the connection.
Changing this updates the description of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L316">property dpds</a>
</h3>

```typescript
dpds?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A dictionary with dead peer detection (DPD) protocol controls.
- `action` - (Optional) The dead peer detection (DPD) action.
A valid value is clear, hold, restart, disabled, or restart-by-peer.
Default value is hold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L320">property ikepolicyId</a>
</h3>

```typescript
ikepolicyId: pulumi.Input<string>;
```


The ID of the IKE policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L324">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


A valid value is response-only or bi-directional. Default is bi-directional.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L328">property ipsecpolicyId</a>
</h3>

```typescript
ipsecpolicyId: pulumi.Input<string>;
```


The ID of the IPsec policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L335">property localEpGroupId</a>
</h3>

```typescript
localEpGroupId?: pulumi.Input<string>;
```


The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L341">property localId</a>
</h3>

```typescript
localId?: pulumi.Input<string>;
```


An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L346">property mtu</a>
</h3>

```typescript
mtu?: pulumi.Input<number>;
```


The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L351">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection. Changing this updates the name of
the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L355">property peerAddress</a>
</h3>

```typescript
peerAddress: pulumi.Input<string>;
```


The peer gateway public IPv4 or IPv6 address or FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L359">property peerCidrs</a>
</h3>

```typescript
peerCidrs?: pulumi.Input<pulumi.Input<string>[]>;
```


Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L365">property peerEpGroupId</a>
</h3>

```typescript
peerEpGroupId?: pulumi.Input<string>;
```


The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L371">property peerId</a>
</h3>

```typescript
peerId: pulumi.Input<string>;
```


The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L375">property psk</a>
</h3>

```typescript
psk: pulumi.Input<string>;
```


The pre-shared key. A valid value is any string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L382">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
`region` argument of the provider is used. Changing this creates a new
site connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L387">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the connection. Required if admin wants to
create a connection for another project. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L391">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L395">property vpnserviceId</a>
</h3>

```typescript
vpnserviceId: pulumi.Input<string>;
```


The ID of the VPN service. Changing this creates a new connection.

<h2 class="pdoc-module-header" id="SiteConnectionState">
<a class="pdoc-member-name" href="/vpnaas/siteConnection.ts#L197">interface SiteConnectionState</a>
</h2>

Input properties used for looking up and filtering SiteConnection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L202">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L207">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the connection.
Changing this updates the description of the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L214">property dpds</a>
</h3>

```typescript
dpds?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A dictionary with dead peer detection (DPD) protocol controls.
- `action` - (Optional) The dead peer detection (DPD) action.
A valid value is clear, hold, restart, disabled, or restart-by-peer.
Default value is hold.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L218">property ikepolicyId</a>
</h3>

```typescript
ikepolicyId?: pulumi.Input<string>;
```


The ID of the IKE policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L222">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


A valid value is response-only or bi-directional. Default is bi-directional.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L226">property ipsecpolicyId</a>
</h3>

```typescript
ipsecpolicyId?: pulumi.Input<string>;
```


The ID of the IPsec policy. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L233">property localEpGroupId</a>
</h3>

```typescript
localEpGroupId?: pulumi.Input<string>;
```


The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L239">property localId</a>
</h3>

```typescript
localId?: pulumi.Input<string>;
```


An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L244">property mtu</a>
</h3>

```typescript
mtu?: pulumi.Input<number>;
```


The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L249">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection. Changing this updates the name of
the existing connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L253">property peerAddress</a>
</h3>

```typescript
peerAddress?: pulumi.Input<string>;
```


The peer gateway public IPv4 or IPv6 address or FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L257">property peerCidrs</a>
</h3>

```typescript
peerCidrs?: pulumi.Input<pulumi.Input<string>[]>;
```


Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L263">property peerEpGroupId</a>
</h3>

```typescript
peerEpGroupId?: pulumi.Input<string>;
```


The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L269">property peerId</a>
</h3>

```typescript
peerId?: pulumi.Input<string>;
```


The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L273">property psk</a>
</h3>

```typescript
psk?: pulumi.Input<string>;
```


The pre-shared key. A valid value is any string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L280">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
`region` argument of the provider is used. Changing this creates a new
site connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L285">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the connection. Required if admin wants to
create a connection for another project. Changing this creates a new connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L289">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vpnaas/siteConnection.ts#L293">property vpnserviceId</a>
</h3>

```typescript
vpnserviceId?: pulumi.Input<string>;
```


The ID of the VPN service. Changing this creates a new connection.

