---
title: Module networking
---

<a href="../index.html">@pulumi/openstack</a> &gt; networking

<h2 class="pdoc-module-header">Index</h2>

* <a href="#FloatingIp">class FloatingIp</a>
* <a href="#FloatingIpAssociate">class FloatingIpAssociate</a>
* <a href="#Network">class Network</a>
* <a href="#Port">class Port</a>
* <a href="#Router">class Router</a>
* <a href="#RouterInterface">class RouterInterface</a>
* <a href="#RouterRoute">class RouterRoute</a>
* <a href="#SecGroup">class SecGroup</a>
* <a href="#SecGroupRule">class SecGroupRule</a>
* <a href="#Subnet">class Subnet</a>
* <a href="#SubnetPool">class SubnetPool</a>
* <a href="#SubnetRoute">class SubnetRoute</a>
* <a href="#getFloatingIP">function getFloatingIP</a>
* <a href="#getNetwork">function getNetwork</a>
* <a href="#getSecGroup">function getSecGroup</a>
* <a href="#getSubnet">function getSubnet</a>
* <a href="#getSubnetPool">function getSubnetPool</a>
* <a href="#FloatingIpArgs">interface FloatingIpArgs</a>
* <a href="#FloatingIpAssociateArgs">interface FloatingIpAssociateArgs</a>
* <a href="#FloatingIpAssociateState">interface FloatingIpAssociateState</a>
* <a href="#FloatingIpState">interface FloatingIpState</a>
* <a href="#GetFloatingIPArgs">interface GetFloatingIPArgs</a>
* <a href="#GetFloatingIPResult">interface GetFloatingIPResult</a>
* <a href="#GetNetworkArgs">interface GetNetworkArgs</a>
* <a href="#GetNetworkResult">interface GetNetworkResult</a>
* <a href="#GetSecGroupArgs">interface GetSecGroupArgs</a>
* <a href="#GetSecGroupResult">interface GetSecGroupResult</a>
* <a href="#GetSubnetArgs">interface GetSubnetArgs</a>
* <a href="#GetSubnetPoolArgs">interface GetSubnetPoolArgs</a>
* <a href="#GetSubnetPoolResult">interface GetSubnetPoolResult</a>
* <a href="#GetSubnetResult">interface GetSubnetResult</a>
* <a href="#NetworkArgs">interface NetworkArgs</a>
* <a href="#NetworkState">interface NetworkState</a>
* <a href="#PortArgs">interface PortArgs</a>
* <a href="#PortState">interface PortState</a>
* <a href="#RouterArgs">interface RouterArgs</a>
* <a href="#RouterInterfaceArgs">interface RouterInterfaceArgs</a>
* <a href="#RouterInterfaceState">interface RouterInterfaceState</a>
* <a href="#RouterRouteArgs">interface RouterRouteArgs</a>
* <a href="#RouterRouteState">interface RouterRouteState</a>
* <a href="#RouterState">interface RouterState</a>
* <a href="#SecGroupArgs">interface SecGroupArgs</a>
* <a href="#SecGroupRuleArgs">interface SecGroupRuleArgs</a>
* <a href="#SecGroupRuleState">interface SecGroupRuleState</a>
* <a href="#SecGroupState">interface SecGroupState</a>
* <a href="#SubnetArgs">interface SubnetArgs</a>
* <a href="#SubnetPoolArgs">interface SubnetPoolArgs</a>
* <a href="#SubnetPoolState">interface SubnetPoolState</a>
* <a href="#SubnetRouteArgs">interface SubnetRouteArgs</a>
* <a href="#SubnetRouteState">interface SubnetRouteState</a>
* <a href="#SubnetState">interface SubnetState</a>

<a href="/networking/floatingIp.ts">networking/floatingIp.ts</a> <a href="/networking/floatingIpAssociate.ts">networking/floatingIpAssociate.ts</a> <a href="/networking/getFloatingIP.ts">networking/getFloatingIP.ts</a> <a href="/networking/getNetwork.ts">networking/getNetwork.ts</a> <a href="/networking/getSecGroup.ts">networking/getSecGroup.ts</a> <a href="/networking/getSubnet.ts">networking/getSubnet.ts</a> <a href="/networking/getSubnetPool.ts">networking/getSubnetPool.ts</a> <a href="/networking/network.ts">networking/network.ts</a> <a href="/networking/port.ts">networking/port.ts</a> <a href="/networking/router.ts">networking/router.ts</a> <a href="/networking/routerInterface.ts">networking/routerInterface.ts</a> <a href="/networking/routerRoute.ts">networking/routerRoute.ts</a> <a href="/networking/secGroup.ts">networking/secGroup.ts</a> <a href="/networking/secGroupRule.ts">networking/secGroupRule.ts</a> <a href="/networking/subnet.ts">networking/subnet.ts</a> <a href="/networking/subnetPool.ts">networking/subnetPool.ts</a> <a href="/networking/subnetRoute.ts">networking/subnetRoute.ts</a> 


<h2 class="pdoc-module-header" id="FloatingIp">
<a class="pdoc-member-name" href="/networking/floatingIp.ts#L12">class FloatingIp</a>
</h2>

Manages a V2 floating IP resource within OpenStack Neutron (networking)
that can be used for load balancers.
These are similar to Nova (compute) floating IP resources,
but only compute floating IPs can be used with compute instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L70">constructor</a>
</h3>

```typescript
new FloatingIp(name: string, args: FloatingIpArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FloatingIp resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FloatingIpState): FloatingIp
```


Get an existing FloatingIp resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L31">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The actual/specific floating IP to obtain. By default,
non-admin users are not able to specify a floating IP, so you must either be
an admin user or have had a custom policy or role applied to your OpenStack
user or project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L36">property fixedIp</a>
</h3>

```typescript
public fixedIp: pulumi.Output<string>;
```


Fixed IP of the port to associate with this floating IP. Required if
the port has multiple fixed IPs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L41">property pool</a>
</h3>

```typescript
public pool: pulumi.Output<string>;
```


The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L46">property portId</a>
</h3>

```typescript
public portId: pulumi.Output<string>;
```


ID of an existing port with at least one IP address to
associate with this floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L54">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
`region` argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L59">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string | undefined>;
```


The subnet ID of the floating IP pool. Specify this if
the floating IP network has multiple subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L66">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The target tenant ID in which to allocate the floating
IP, if you specify this together with a port_id, make sure the target port
belongs to the same tenant. Changing this creates a new floating IP (which
may or may not have a different address)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L70">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="FloatingIpAssociate">
<a class="pdoc-member-name" href="/networking/floatingIpAssociate.ts#L11">class FloatingIpAssociate</a>
</h2>

Associates a floating IP to a port. This is useful for situations
where you have a pre-allocated floating IP or are unable to use the
`openstack_networking_floatingip_v2` resource to create a floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L40">constructor</a>
</h3>

```typescript
new FloatingIpAssociate(name: string, args: FloatingIpAssociateArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FloatingIpAssociate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FloatingIpAssociateState): FloatingIpAssociate
```


Get an existing FloatingIpAssociate resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L27">property floatingIp</a>
</h3>

```typescript
public floatingIp: pulumi.Output<string>;
```


IP Address of an existing floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L32">property portId</a>
</h3>

```typescript
public portId: pulumi.Output<string>;
```


ID of an existing port with at least one IP address to
associate with this floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L40">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
`region` argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Network">
<a class="pdoc-member-name" href="/networking/network.ts#L9">class Network</a>
</h2>

Manages a V2 Neutron network resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L71">constructor</a>
</h3>

```typescript
new Network(name: string, args?: NetworkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Network resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkState): Network
```


Get an existing Network resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/network.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<string>;
```


The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L34">property availabilityZoneHints</a>
</h3>

```typescript
public availabilityZoneHints: pulumi.Output<string[]>;
```


An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L40">property external</a>
</h3>

```typescript
public external: pulumi.Output<boolean>;
```


Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the network. Changing this updates the name of
the existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L52">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L56">property segments</a>
</h3>

```typescript
public segments: pulumi.Output<{ ... }[] | undefined>;
```


An array of one or more provider segment objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L62">property shared</a>
</h3>

```typescript
public shared: pulumi.Output<string>;
```


Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabalities of the
existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L67">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L71">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="Port">
<a class="pdoc-member-name" href="/networking/port.ts#L9">class Port</a>
</h2>

Manages a V2 port resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L103">constructor</a>
</h3>

```typescript
new Port(name: string, args: PortArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Port resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PortState): Port
```


Get an existing Port resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/port.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean>;
```


Administrative up/down status for the port
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L32">property allFixedIps</a>
</h3>

```typescript
public allFixedIps: pulumi.Output<string[]>;
```


The collection of Fixed IP addresses on the port in the
order returned by the Network v2 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L37">property allSecurityGroupIds</a>
</h3>

```typescript
public allSecurityGroupIds: pulumi.Output<string[]>;
```


The collection of Security Group IDs on the port
which have been explicitly and implicitly added.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L43">property allowedAddressPairs</a>
</h3>

```typescript
public allowedAddressPairs: pulumi.Output<{ ... }[] | undefined>;
```


An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L48">property deviceId</a>
</h3>

```typescript
public deviceId: pulumi.Output<string>;
```


The ID of the device attached to the port. Changing this
creates a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L53">property deviceOwner</a>
</h3>

```typescript
public deviceOwner: pulumi.Output<string>;
```


The device owner of the Port. Changing this creates
a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L58">property fixedIps</a>
</h3>

```typescript
public fixedIps: pulumi.Output<{ ... }[] | undefined>;
```


An array of desired IPs for this port. The structure is
described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L62">property macAddress</a>
</h3>

```typescript
public macAddress: pulumi.Output<string>;
```


The additional MAC address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L67">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the port. Changing this
updates the `name` of an existing port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L72">property networkId</a>
</h3>

```typescript
public networkId: pulumi.Output<string>;
```


The ID of the network to attach the port to. Changing
this creates a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L80">property noSecurityGroups</a>
</h3>

```typescript
public noSecurityGroups: pulumi.Output<boolean | undefined>;
```


If set to
`true`, then no security groups are applied to the port. If set to `false` and
no `security_group_ids` are specified, then the Port will yield to the default
behavior of the Networking service, which is to usually apply the "default"
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L87">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L94">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[] | undefined>;
```


A list
of security group IDs to apply to the port. The security groups must be
specified by ID and not name (as opposed to how they are configured with
the Compute Instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L99">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L103">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="Router">
<a class="pdoc-member-name" href="/networking/router.ts#L9">class Router</a>
</h2>

Manages a V2 router resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L93">constructor</a>
</h3>

```typescript
new Router(name: string, args?: RouterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Router resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouterState): Router
```


Get an existing Router resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/router.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean>;
```


Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L33">property availabilityZoneHints</a>
</h3>

```typescript
public availabilityZoneHints: pulumi.Output<string[]>;
```


An availability zone is used to make
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L39">property distributed</a>
</h3>

```typescript
public distributed: pulumi.Output<boolean>;
```


Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L45">property enableSnat</a>
</h3>

```typescript
public enableSnat: pulumi.Output<boolean>;
```


Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L52">property externalFixedIps</a>
</h3>

```typescript
public externalFixedIps: pulumi.Output<{ ... }[]>;
```


An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L60">property externalGateway</a>
</h3>

```typescript
public externalGateway: pulumi.Output<string>;
```


The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L67">property externalNetworkId</a>
</h3>

```typescript
public externalNetworkId: pulumi.Output<string>;
```


The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L72">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the router. Changing this
updates the `name` of an existing router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L79">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L84">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L88">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional driver-specific options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L93">property vendorOptions</a>
</h3>

```typescript
public vendorOptions: pulumi.Output<{ ... } | undefined>;
```


Map of additional vendor-specific options.
Supported options are described below.

<h2 class="pdoc-module-header" id="RouterInterface">
<a class="pdoc-member-name" href="/networking/routerInterface.ts#L9">class RouterInterface</a>
</h2>

Manages a V2 router interface resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L43">constructor</a>
</h3>

```typescript
new RouterInterface(name: string, args: RouterInterfaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RouterInterface resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouterInterfaceState): RouterInterface
```


Get an existing RouterInterface resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L26">property portId</a>
</h3>

```typescript
public portId: pulumi.Output<string>;
```


ID of the port this interface connects to. Changing
this creates a new router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L33">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L38">property routerId</a>
</h3>

```typescript
public routerId: pulumi.Output<string>;
```


ID of the router this interface belongs to. Changing
this creates a new router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L43">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


ID of the subnet this interface connects to. Changing
this creates a new router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RouterRoute">
<a class="pdoc-member-name" href="/networking/routerRoute.ts#L9">class RouterRoute</a>
</h2>

Creates a routing entry on a OpenStack V2 router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L43">constructor</a>
</h3>

```typescript
new RouterRoute(name: string, args: RouterRouteArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RouterRoute resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouterRouteState): RouterRoute
```


Get an existing RouterRoute resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L26">property destinationCidr</a>
</h3>

```typescript
public destinationCidr: pulumi.Output<string>;
```


CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L31">property nextHop</a>
</h3>

```typescript
public nextHop: pulumi.Output<string>;
```


IP address of the next hop gateway.  Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L38">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L43">property routerId</a>
</h3>

```typescript
public routerId: pulumi.Output<string>;
```


ID of the router this routing entry belongs to. Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SecGroup">
<a class="pdoc-member-name" href="/networking/secGroup.ts#L11">class SecGroup</a>
</h2>

Manages a V2 neutron security group resource within OpenStack.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L50">constructor</a>
</h3>

```typescript
new SecGroup(name: string, args?: SecGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecGroupState): SecGroup
```


Get an existing SecGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/secGroup.ts#L29">property deleteDefaultRules</a>
</h3>

```typescript
public deleteDefaultRules: pulumi.Output<boolean | undefined>;
```


Whether or not to delete the default
egress security rules. This is `false` by default. See the below note
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


A unique name for the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L44">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L50">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SecGroupRule">
<a class="pdoc-member-name" href="/networking/secGroupRule.ts#L11">class SecGroupRule</a>
</h2>

Manages a V2 neutron security group rule resource within OpenStack.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L100">constructor</a>
</h3>

```typescript
new SecGroupRule(name: string, args: SecGroupRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecGroupRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecGroupRuleState): SecGroupRule
```


Get an existing SecGroupRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L28">property direction</a>
</h3>

```typescript
public direction: pulumi.Output<string>;
```


The direction of the rule, valid values are __ingress__
or __egress__. Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L33">property ethertype</a>
</h3>

```typescript
public ethertype: pulumi.Output<string>;
```


The layer 3 protocol type, valid values are __IPv4__
or __IPv6__. Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L39">property portRangeMax</a>
</h3>

```typescript
public portRangeMax: pulumi.Output<number>;
```


The higher part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L45">property portRangeMin</a>
</h3>

```typescript
public portRangeMin: pulumi.Output<number>;
```


The lower part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L70">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.
* __tcp__
* __udp__
* __icmp__
* __ah__
* __dccp__
* __egp__
* __esp__
* __gre__
* __igmp__
* __ipv6-encap__
* __ipv6-frag__
* __ipv6-icmp__
* __ipv6-nonxt__
* __ipv6-opts__
* __ipv6-route__
* __ospf__
* __pgm__
* __rsvp__
* __sctp__
* __udplite__
* __vrrp__

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L77">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L83">property remoteGroupId</a>
</h3>

```typescript
public remoteGroupId: pulumi.Output<string>;
```


The remote group id, the value needs to be an
Openstack ID of a security group in the same tenant. Changing this creates
a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L88">property remoteIpPrefix</a>
</h3>

```typescript
public remoteIpPrefix: pulumi.Output<string>;
```


The remote CIDR, the value needs to be a valid
CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L94">property securityGroupId</a>
</h3>

```typescript
public securityGroupId: pulumi.Output<string>;
```


The security group id the rule should belong
to, the value needs to be an Openstack ID of a security group in the same
tenant. Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L100">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Subnet">
<a class="pdoc-member-name" href="/networking/subnet.ts#L9">class Subnet</a>
</h2>

Manages a V2 Neutron subnet resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L109">constructor</a>
</h3>

```typescript
new Subnet(name: string, args: SubnetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Subnet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetState): Subnet
```


Get an existing Subnet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/subnet.ts#L27">property allocationPools</a>
</h3>

```typescript
public allocationPools: pulumi.Output<{ ... }[]>;
```


An array of sub-ranges of CIDR available for
dynamic allocation to ports. The allocation_pool object structure is
documented below. Changing this creates a new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L33">property cidr</a>
</h3>

```typescript
public cidr: pulumi.Output<string>;
```


CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L39">property dnsNameservers</a>
</h3>

```typescript
public dnsNameservers: pulumi.Output<string[] | undefined>;
```


An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L45">property enableDhcp</a>
</h3>

```typescript
public enableDhcp: pulumi.Output<boolean | undefined>;
```


The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L52">property gatewayIp</a>
</h3>

```typescript
public gatewayIp: pulumi.Output<string>;
```


Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L59">property hostRoutes</a>
</h3>

```typescript
public hostRoutes: pulumi.Output<{ ... }[] | undefined>;
```


An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L64">property ipVersion</a>
</h3>

```typescript
public ipVersion: pulumi.Output<number | undefined>;
```


IP version, either 4 (default) or 6. Changing this creates a
new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L69">property ipv6AddressMode</a>
</h3>

```typescript
public ipv6AddressMode: pulumi.Output<string>;
```


The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L74">property ipv6RaMode</a>
</h3>

```typescript
public ipv6RaMode: pulumi.Output<string>;
```


The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L79">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the subnet. Changing this updates the name of
the existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L84">property networkId</a>
</h3>

```typescript
public networkId: pulumi.Output<string>;
```


The UUID of the parent network. Changing this
creates a new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L89">property noGateway</a>
</h3>

```typescript
public noGateway: pulumi.Output<boolean | undefined>;
```


Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L96">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L100">property subnetpoolId</a>
</h3>

```typescript
public subnetpoolId: pulumi.Output<string | undefined>;
```


The ID of the subnetpool associated with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L105">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L109">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SubnetPool">
<a class="pdoc-member-name" href="/networking/subnetPool.ts#L9">class SubnetPool</a>
</h2>

Manages a V2 Neutron subnetpool resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L115">constructor</a>
</h3>

```typescript
new SubnetPool(name: string, args: SubnetPoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetPoolState): SubnetPool
```


Get an existing SubnetPool resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L27">property addressScopeId</a>
</h3>

```typescript
public addressScopeId: pulumi.Output<string | undefined>;
```


The Neutron address scope to assign to the
subnetpool. Changing this updates the address scope id of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L31">property createdAt</a>
</h3>

```typescript
public createdAt: pulumi.Output<string>;
```


The time at which subnetpool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L38">property defaultPrefixlen</a>
</h3>

```typescript
public defaultPrefixlen: pulumi.Output<number>;
```


The size of the prefix to allocate when the cidr
or prefixlen attributes are omitted when you create the subnet. Defaults to the
MinPrefixLen. Changing this updates the default prefixlen of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L44">property defaultQuota</a>
</h3>

```typescript
public defaultQuota: pulumi.Output<number | undefined>;
```


The per-project quota on the prefix space that can be
allocated from the subnetpool for project subnets. Changing this updates the
default quota of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L49">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The human-readable description for the subnetpool.
Changing this updates the description of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L53">property ipVersion</a>
</h3>

```typescript
public ipVersion: pulumi.Output<number>;
```


The IP protocol version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L59">property isDefault</a>
</h3>

```typescript
public isDefault: pulumi.Output<boolean | undefined>;
```


Indicates whether the subnetpool is default
subnetpool or not. Changing this updates the default status of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L66">property maxPrefixlen</a>
</h3>

```typescript
public maxPrefixlen: pulumi.Output<number>;
```


The maximum prefix size that can be allocated from
the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools,
default is 128. Changing this updates the max prefixlen of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L72">property minPrefixlen</a>
</h3>

```typescript
public minPrefixlen: pulumi.Output<number>;
```


The smallest prefix that can be allocated from a
subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default
is 64. Changing this updates the min prefixlen of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L77">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the subnetpool. Changing this updates the name of
the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L85">property prefixes</a>
</h3>

```typescript
public prefixes: pulumi.Output<string[]>;
```


A list of subnet prefixes to assign to the subnetpool.
Neutron API merges adjacent prefixes and treats them as a single prefix. Each
subnet prefix must be unique among all subnet prefixes in all subnetpools that
are associated with the address scope. Changing this updates the prefixes list
of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L90">property projectId</a>
</h3>

```typescript
public projectId: pulumi.Output<string>;
```


The owner of the subnetpool. Required if admin wants to
create a subnetpool for another project. Changing this creates a new subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L97">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnetpool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L101">property revisionNumber</a>
</h3>

```typescript
public revisionNumber: pulumi.Output<number>;
```


The revision number of the subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L107">property shared</a>
</h3>

```typescript
public shared: pulumi.Output<boolean | undefined>;
```


Indicates whether this subnetpool is shared across
all projects. Changing this updates the shared status of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L111">property updatedAt</a>
</h3>

```typescript
public updatedAt: pulumi.Output<string>;
```


The time at which subnetpool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L115">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SubnetRoute">
<a class="pdoc-member-name" href="/networking/subnetRoute.ts#L9">class SubnetRoute</a>
</h2>

Creates a routing entry on a OpenStack V2 subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L43">constructor</a>
</h3>

```typescript
new SubnetRoute(name: string, args: SubnetRouteArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetRoute resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetRouteState): SubnetRoute
```


Get an existing SubnetRoute resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L26">property destinationCidr</a>
</h3>

```typescript
public destinationCidr: pulumi.Output<string>;
```


CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L31">property nextHop</a>
</h3>

```typescript
public nextHop: pulumi.Output<string>;
```


IP address of the next hop gateway.  Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L38">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L43">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


ID of the subnet this routing entry belongs to. Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getFloatingIP">
<a class="pdoc-member-name" href="/networking/getFloatingIP.ts#L9">function getFloatingIP</a>
</h2>

```typescript
getFloatingIP(args?: GetFloatingIPArgs, opts?: pulumi.InvokeOptions): Promise<GetFloatingIPResult>
```


Use this data source to get the ID of an available OpenStack floating IP.

<h2 class="pdoc-module-header" id="getNetwork">
<a class="pdoc-member-name" href="/networking/getNetwork.ts#L9">function getNetwork</a>
</h2>

```typescript
getNetwork(args?: GetNetworkArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkResult>
```


Use this data source to get the ID of an available OpenStack network.

<h2 class="pdoc-module-header" id="getSecGroup">
<a class="pdoc-member-name" href="/networking/getSecGroup.ts#L9">function getSecGroup</a>
</h2>

```typescript
getSecGroup(args?: GetSecGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetSecGroupResult>
```


Use this data source to get the ID of an available OpenStack security group.

<h2 class="pdoc-module-header" id="getSubnet">
<a class="pdoc-member-name" href="/networking/getSubnet.ts#L9">function getSubnet</a>
</h2>

```typescript
getSubnet(args?: GetSubnetArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetResult>
```


Use this data source to get the ID of an available OpenStack subnet.

<h2 class="pdoc-module-header" id="getSubnetPool">
<a class="pdoc-member-name" href="/networking/getSubnetPool.ts#L9">function getSubnetPool</a>
</h2>

```typescript
getSubnetPool(args?: GetSubnetPoolArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetPoolResult>
```


Use this data source to get the ID of an available OpenStack subnetpool.

<h2 class="pdoc-module-header" id="FloatingIpArgs">
<a class="pdoc-member-name" href="/networking/floatingIp.ts#L165">interface FloatingIpArgs</a>
</h2>

The set of arguments for constructing a FloatingIp resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L172">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The actual/specific floating IP to obtain. By default,
non-admin users are not able to specify a floating IP, so you must either be
an admin user or have had a custom policy or role applied to your OpenStack
user or project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L177">property fixedIp</a>
</h3>

```typescript
fixedIp?: pulumi.Input<string>;
```


Fixed IP of the port to associate with this floating IP. Required if
the port has multiple fixed IPs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L182">property pool</a>
</h3>

```typescript
pool: pulumi.Input<string>;
```


The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L187">property portId</a>
</h3>

```typescript
portId?: pulumi.Input<string>;
```


ID of an existing port with at least one IP address to
associate with this floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L195">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
`region` argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L200">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The subnet ID of the floating IP pool. Specify this if
the floating IP network has multiple subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L207">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The target tenant ID in which to allocate the floating
IP, if you specify this together with a port_id, make sure the target port
belongs to the same tenant. Changing this creates a new floating IP (which
may or may not have a different address)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L211">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="FloatingIpAssociateArgs">
<a class="pdoc-member-name" href="/networking/floatingIpAssociate.ts#L99">interface FloatingIpAssociateArgs</a>
</h2>

The set of arguments for constructing a FloatingIpAssociate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L103">property floatingIp</a>
</h3>

```typescript
floatingIp: pulumi.Input<string>;
```


IP Address of an existing floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L108">property portId</a>
</h3>

```typescript
portId: pulumi.Input<string>;
```


ID of an existing port with at least one IP address to
associate with this floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L116">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
`region` argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).

<h2 class="pdoc-module-header" id="FloatingIpAssociateState">
<a class="pdoc-member-name" href="/networking/floatingIpAssociate.ts#L76">interface FloatingIpAssociateState</a>
</h2>

Input properties used for looking up and filtering FloatingIpAssociate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L80">property floatingIp</a>
</h3>

```typescript
floatingIp?: pulumi.Input<string>;
```


IP Address of an existing floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L85">property portId</a>
</h3>

```typescript
portId?: pulumi.Input<string>;
```


ID of an existing port with at least one IP address to
associate with this floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIpAssociate.ts#L93">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
`region` argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).

<h2 class="pdoc-module-header" id="FloatingIpState">
<a class="pdoc-member-name" href="/networking/floatingIp.ts#L113">interface FloatingIpState</a>
</h2>

Input properties used for looking up and filtering FloatingIp resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L120">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The actual/specific floating IP to obtain. By default,
non-admin users are not able to specify a floating IP, so you must either be
an admin user or have had a custom policy or role applied to your OpenStack
user or project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L125">property fixedIp</a>
</h3>

```typescript
fixedIp?: pulumi.Input<string>;
```


Fixed IP of the port to associate with this floating IP. Required if
the port has multiple fixed IPs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L130">property pool</a>
</h3>

```typescript
pool?: pulumi.Input<string>;
```


The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L135">property portId</a>
</h3>

```typescript
portId?: pulumi.Input<string>;
```


ID of an existing port with at least one IP address to
associate with this floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L143">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
`region` argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L148">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The subnet ID of the floating IP pool. Specify this if
the floating IP network has multiple subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L155">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The target tenant ID in which to allocate the floating
IP, if you specify this together with a port_id, make sure the target port
belongs to the same tenant. Changing this creates a new floating IP (which
may or may not have a different address)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/floatingIp.ts#L159">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="GetFloatingIPArgs">
<a class="pdoc-member-name" href="/networking/getFloatingIP.ts#L25">interface GetFloatingIPArgs</a>
</h2>

A collection of arguments for invoking getFloatingIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getFloatingIP.ts#L29">property address</a>
</h3>

```typescript
address?: string;
```


The IP address of the floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getFloatingIP.ts#L33">property fixedIp</a>
</h3>

```typescript
fixedIp?: string;
```


The specific IP address of the internal port which should be associated with the floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getFloatingIP.ts#L37">property pool</a>
</h3>

```typescript
pool?: string;
```


The name of the pool from which the floating IP belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getFloatingIP.ts#L41">property portId</a>
</h3>

```typescript
portId?: string;
```


The ID of the port the floating IP is attached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getFloatingIP.ts#L47">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve floating IP ids. If omitted, the
`region` argument of the provider is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getFloatingIP.ts#L48">property status</a>
</h3>

```typescript
status?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getFloatingIP.ts#L52">property tenantId</a>
</h3>

```typescript
tenantId?: string;
```


The owner of the floating IP.

<h2 class="pdoc-module-header" id="GetFloatingIPResult">
<a class="pdoc-member-name" href="/networking/getFloatingIP.ts#L58">interface GetFloatingIPResult</a>
</h2>

A collection of values returned by getFloatingIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getFloatingIP.ts#L62">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetNetworkArgs">
<a class="pdoc-member-name" href="/networking/getNetwork.ts#L25">interface GetNetworkArgs</a>
</h2>

A collection of arguments for invoking getNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L29">property external</a>
</h3>

```typescript
external?: boolean;
```


The external routing facility of the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L33">property matchingSubnetCidr</a>
</h3>

```typescript
matchingSubnetCidr?: string;
```


The CIDR of a subnet within the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L37">property name</a>
</h3>

```typescript
name?: string;
```


The name of the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L41">property networkId</a>
</h3>

```typescript
networkId?: string;
```


The ID of the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L47">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve networks ids. If omitted, the
`region` argument of the provider is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L51">property status</a>
</h3>

```typescript
status?: string;
```


The status of the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L55">property tenantId</a>
</h3>

```typescript
tenantId?: string;
```


The owner of the network.

<h2 class="pdoc-module-header" id="GetNetworkResult">
<a class="pdoc-member-name" href="/networking/getNetwork.ts#L61">interface GetNetworkResult</a>
</h2>

A collection of values returned by getNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L65">property adminStateUp</a>
</h3>

```typescript
adminStateUp: string;
```


(Optional) The administrative state of the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L69">property availabilityZoneHints</a>
</h3>

```typescript
availabilityZoneHints: string[];
```


(Optional) The availability zone candidates for the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L82">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L73">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getNetwork.ts#L78">property shared</a>
</h3>

```typescript
shared: string;
```


(Optional)  Specifies whether the network resource can be accessed
by any tenant or not.

<h2 class="pdoc-module-header" id="GetSecGroupArgs">
<a class="pdoc-member-name" href="/networking/getSecGroup.ts#L22">interface GetSecGroupArgs</a>
</h2>

A collection of arguments for invoking getSecGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSecGroup.ts#L26">property name</a>
</h3>

```typescript
name?: string;
```


The name of the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSecGroup.ts#L32">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve security groups ids. If omitted, the
`region` argument of the provider is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSecGroup.ts#L36">property secgroupId</a>
</h3>

```typescript
secgroupId?: string;
```


The ID of the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSecGroup.ts#L40">property tenantId</a>
</h3>

```typescript
tenantId?: string;
```


The owner of the security group.

<h2 class="pdoc-module-header" id="GetSecGroupResult">
<a class="pdoc-member-name" href="/networking/getSecGroup.ts#L46">interface GetSecGroupResult</a>
</h2>

A collection of values returned by getSecGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSecGroup.ts#L55">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSecGroup.ts#L50">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSecGroup.ts#L51">property tenantId</a>
</h3>

```typescript
tenantId: string;
```

<h2 class="pdoc-module-header" id="GetSubnetArgs">
<a class="pdoc-member-name" href="/networking/getSubnet.ts#L31">interface GetSubnetArgs</a>
</h2>

A collection of arguments for invoking getSubnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L35">property cidr</a>
</h3>

```typescript
cidr?: string;
```


The CIDR of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L39">property dhcpDisabled</a>
</h3>

```typescript
dhcpDisabled?: boolean;
```


If the subnet has DHCP disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L43">property dhcpEnabled</a>
</h3>

```typescript
dhcpEnabled?: boolean;
```


If the subnet has DHCP enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L47">property gatewayIp</a>
</h3>

```typescript
gatewayIp?: string;
```


The IP of the subnet's gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L51">property ipVersion</a>
</h3>

```typescript
ipVersion?: number;
```


The IP version of the subnet (either 4 or 6).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L56">property ipv6AddressMode</a>
</h3>

```typescript
ipv6AddressMode?: string;
```


The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L61">property ipv6RaMode</a>
</h3>

```typescript
ipv6RaMode?: string;
```


The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L65">property name</a>
</h3>

```typescript
name?: string;
```


The name of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L69">property networkId</a>
</h3>

```typescript
networkId?: string;
```


The ID of the network the subnet belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L75">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve subnet ids. If omitted, the
`region` argument of the provider is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L79">property subnetId</a>
</h3>

```typescript
subnetId?: string;
```


The ID of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L83">property subnetpoolId</a>
</h3>

```typescript
subnetpoolId?: string;
```


The ID of the subnetpool associated with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L87">property tenantId</a>
</h3>

```typescript
tenantId?: string;
```


The owner of the subnet.

<h2 class="pdoc-module-header" id="GetSubnetPoolArgs">
<a class="pdoc-member-name" href="/networking/getSubnetPool.ts#L30">interface GetSubnetPoolArgs</a>
</h2>

A collection of arguments for invoking getSubnetPool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L35">property addressScopeId</a>
</h3>

```typescript
addressScopeId?: string;
```


The Neutron address scope that subnetpools
is assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L40">property defaultPrefixlen</a>
</h3>

```typescript
defaultPrefixlen?: number;
```


The size of the subnetpool default prefix
length.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L45">property defaultQuota</a>
</h3>

```typescript
defaultQuota?: number;
```


The per-project quota on the prefix space that
can be allocated from the subnetpool for project subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L49">property description</a>
</h3>

```typescript
description?: string;
```


The human-readable description for the subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L53">property ipVersion</a>
</h3>

```typescript
ipVersion?: number;
```


The IP protocol version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L57">property isDefault</a>
</h3>

```typescript
isDefault?: boolean;
```


Whether the subnetpool is default subnetpool or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L61">property maxPrefixlen</a>
</h3>

```typescript
maxPrefixlen?: number;
```


The size of the subnetpool max prefix length.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L65">property minPrefixlen</a>
</h3>

```typescript
minPrefixlen?: number;
```


The size of the subnetpool min prefix length.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L69">property name</a>
</h3>

```typescript
name?: string;
```


The name of the subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L73">property projectId</a>
</h3>

```typescript
projectId?: string;
```


The owner of the subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L79">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to retrieve a subnetpool id. If omitted, the
`region` argument of the provider is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L83">property shared</a>
</h3>

```typescript
shared?: boolean;
```


Whether this subnetpool is shared across all projects.

<h2 class="pdoc-module-header" id="GetSubnetPoolResult">
<a class="pdoc-member-name" href="/networking/getSubnetPool.ts#L89">interface GetSubnetPoolResult</a>
</h2>

A collection of values returned by getSubnetPool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L94">property addressScopeId</a>
</h3>

```typescript
addressScopeId: string;
```


See Argument Reference above.
* `ip_version` -The IP protocol version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L98">property createdAt</a>
</h3>

```typescript
createdAt: string;
```


The time at which subnetpool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L102">property defaultPrefixlen</a>
</h3>

```typescript
defaultPrefixlen: number;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L106">property defaultQuota</a>
</h3>

```typescript
defaultQuota: number;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L110">property description</a>
</h3>

```typescript
description: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L155">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L111">property ipVersion</a>
</h3>

```typescript
ipVersion: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L115">property isDefault</a>
</h3>

```typescript
isDefault: boolean;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L119">property maxPrefixlen</a>
</h3>

```typescript
maxPrefixlen: number;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L123">property minPrefixlen</a>
</h3>

```typescript
minPrefixlen: number;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L127">property name</a>
</h3>

```typescript
name: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L131">property prefixes</a>
</h3>

```typescript
prefixes: string[];
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L135">property projectId</a>
</h3>

```typescript
projectId: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L139">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L143">property revisionNumber</a>
</h3>

```typescript
revisionNumber: number;
```


The revision number of the subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L147">property shared</a>
</h3>

```typescript
shared: boolean;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnetPool.ts#L151">property updatedAt</a>
</h3>

```typescript
updatedAt: string;
```


The time at which subnetpool was created.

<h2 class="pdoc-module-header" id="GetSubnetResult">
<a class="pdoc-member-name" href="/networking/getSubnet.ts#L93">interface GetSubnetResult</a>
</h2>

A collection of values returned by getSubnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L97">property allocationPools</a>
</h3>

```typescript
allocationPools: { ... }[];
```


Allocation pools of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L98">property cidr</a>
</h3>

```typescript
cidr: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L102">property dnsNameservers</a>
</h3>

```typescript
dnsNameservers: string[];
```


DNS Nameservers of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L106">property enableDhcp</a>
</h3>

```typescript
enableDhcp: boolean;
```


Whether the subnet has DHCP enabled or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L107">property gatewayIp</a>
</h3>

```typescript
gatewayIp: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L111">property hostRoutes</a>
</h3>

```typescript
hostRoutes: { ... }[];
```


Host Routes of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L127">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L112">property ipVersion</a>
</h3>

```typescript
ipVersion: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L113">property ipv6AddressMode</a>
</h3>

```typescript
ipv6AddressMode: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L114">property ipv6RaMode</a>
</h3>

```typescript
ipv6RaMode: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L115">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L116">property networkId</a>
</h3>

```typescript
networkId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L120">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L121">property subnetId</a>
</h3>

```typescript
subnetId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L122">property subnetpoolId</a>
</h3>

```typescript
subnetpoolId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/getSubnet.ts#L123">property tenantId</a>
</h3>

```typescript
tenantId: string;
```

<h2 class="pdoc-module-header" id="NetworkArgs">
<a class="pdoc-member-name" href="/networking/network.ts#L169">interface NetworkArgs</a>
</h2>

The set of arguments for constructing a Network resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L175">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<string>;
```


The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L182">property availabilityZoneHints</a>
</h3>

```typescript
availabilityZoneHints?: pulumi.Input<pulumi.Input<string>[]>;
```


An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L188">property external</a>
</h3>

```typescript
external?: pulumi.Input<boolean>;
```


Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L193">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the network. Changing this updates the name of
the existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L200">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L204">property segments</a>
</h3>

```typescript
segments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of one or more provider segment objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L210">property shared</a>
</h3>

```typescript
shared?: pulumi.Input<string>;
```


Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabalities of the
existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L215">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L219">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="NetworkState">
<a class="pdoc-member-name" href="/networking/network.ts#L113">interface NetworkState</a>
</h2>

Input properties used for looking up and filtering Network resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L119">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<string>;
```


The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L126">property availabilityZoneHints</a>
</h3>

```typescript
availabilityZoneHints?: pulumi.Input<pulumi.Input<string>[]>;
```


An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L132">property external</a>
</h3>

```typescript
external?: pulumi.Input<boolean>;
```


Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the network. Changing this updates the name of
the existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L144">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L148">property segments</a>
</h3>

```typescript
segments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of one or more provider segment objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L154">property shared</a>
</h3>

```typescript
shared?: pulumi.Input<string>;
```


Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabalities of the
existing network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L159">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/network.ts#L163">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="PortArgs">
<a class="pdoc-member-name" href="/networking/port.ts#L248">interface PortArgs</a>
</h2>

The set of arguments for constructing a Port resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L254">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


Administrative up/down status for the port
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L260">property allowedAddressPairs</a>
</h3>

```typescript
allowedAddressPairs?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L265">property deviceId</a>
</h3>

```typescript
deviceId?: pulumi.Input<string>;
```


The ID of the device attached to the port. Changing this
creates a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L270">property deviceOwner</a>
</h3>

```typescript
deviceOwner?: pulumi.Input<string>;
```


The device owner of the Port. Changing this creates
a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L275">property fixedIps</a>
</h3>

```typescript
fixedIps?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of desired IPs for this port. The structure is
described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L279">property macAddress</a>
</h3>

```typescript
macAddress?: pulumi.Input<string>;
```


The additional MAC address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L284">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the port. Changing this
updates the `name` of an existing port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L289">property networkId</a>
</h3>

```typescript
networkId: pulumi.Input<string>;
```


The ID of the network to attach the port to. Changing
this creates a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L297">property noSecurityGroups</a>
</h3>

```typescript
noSecurityGroups?: pulumi.Input<boolean>;
```


If set to
`true`, then no security groups are applied to the port. If set to `false` and
no `security_group_ids` are specified, then the Port will yield to the default
behavior of the Networking service, which is to usually apply the "default"
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L304">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L311">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list
of security group IDs to apply to the port. The security groups must be
specified by ID and not name (as opposed to how they are configured with
the Compute Instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L316">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L320">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="PortState">
<a class="pdoc-member-name" href="/networking/port.ts#L160">interface PortState</a>
</h2>

Input properties used for looking up and filtering Port resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L166">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


Administrative up/down status for the port
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L171">property allFixedIps</a>
</h3>

```typescript
allFixedIps?: pulumi.Input<pulumi.Input<string>[]>;
```


The collection of Fixed IP addresses on the port in the
order returned by the Network v2 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L176">property allSecurityGroupIds</a>
</h3>

```typescript
allSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The collection of Security Group IDs on the port
which have been explicitly and implicitly added.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L182">property allowedAddressPairs</a>
</h3>

```typescript
allowedAddressPairs?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L187">property deviceId</a>
</h3>

```typescript
deviceId?: pulumi.Input<string>;
```


The ID of the device attached to the port. Changing this
creates a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L192">property deviceOwner</a>
</h3>

```typescript
deviceOwner?: pulumi.Input<string>;
```


The device owner of the Port. Changing this creates
a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L197">property fixedIps</a>
</h3>

```typescript
fixedIps?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of desired IPs for this port. The structure is
described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L201">property macAddress</a>
</h3>

```typescript
macAddress?: pulumi.Input<string>;
```


The additional MAC address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L206">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the port. Changing this
updates the `name` of an existing port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L211">property networkId</a>
</h3>

```typescript
networkId?: pulumi.Input<string>;
```


The ID of the network to attach the port to. Changing
this creates a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L219">property noSecurityGroups</a>
</h3>

```typescript
noSecurityGroups?: pulumi.Input<boolean>;
```


If set to
`true`, then no security groups are applied to the port. If set to `false` and
no `security_group_ids` are specified, then the Port will yield to the default
behavior of the Networking service, which is to usually apply the "default"
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L226">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L233">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list
of security group IDs to apply to the port. The security groups must be
specified by ID and not name (as opposed to how they are configured with
the Compute Instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L238">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/port.ts#L242">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="RouterArgs">
<a class="pdoc-member-name" href="/networking/router.ts#L219">interface RouterArgs</a>
</h2>

The set of arguments for constructing a Router resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L225">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L231">property availabilityZoneHints</a>
</h3>

```typescript
availabilityZoneHints?: pulumi.Input<pulumi.Input<string>[]>;
```


An availability zone is used to make
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L237">property distributed</a>
</h3>

```typescript
distributed?: pulumi.Input<boolean>;
```


Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L243">property enableSnat</a>
</h3>

```typescript
enableSnat?: pulumi.Input<boolean>;
```


Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L250">property externalFixedIps</a>
</h3>

```typescript
externalFixedIps?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L258">property externalGateway</a>
</h3>

```typescript
externalGateway?: pulumi.Input<string>;
```


The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L265">property externalNetworkId</a>
</h3>

```typescript
externalNetworkId?: pulumi.Input<string>;
```


The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L270">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the router. Changing this
updates the `name` of an existing router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L277">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L282">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L286">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional driver-specific options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L291">property vendorOptions</a>
</h3>

```typescript
vendorOptions?: pulumi.Input<{ ... }>;
```


Map of additional vendor-specific options.
Supported options are described below.

<h2 class="pdoc-module-header" id="RouterInterfaceArgs">
<a class="pdoc-member-name" href="/networking/routerInterface.ts#L106">interface RouterInterfaceArgs</a>
</h2>

The set of arguments for constructing a RouterInterface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L111">property portId</a>
</h3>

```typescript
portId?: pulumi.Input<string>;
```


ID of the port this interface connects to. Changing
this creates a new router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L118">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L123">property routerId</a>
</h3>

```typescript
routerId: pulumi.Input<string>;
```


ID of the router this interface belongs to. Changing
this creates a new router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L128">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


ID of the subnet this interface connects to. Changing
this creates a new router interface.

<h2 class="pdoc-module-header" id="RouterInterfaceState">
<a class="pdoc-member-name" href="/networking/routerInterface.ts#L78">interface RouterInterfaceState</a>
</h2>

Input properties used for looking up and filtering RouterInterface resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L83">property portId</a>
</h3>

```typescript
portId?: pulumi.Input<string>;
```


ID of the port this interface connects to. Changing
this creates a new router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L90">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L95">property routerId</a>
</h3>

```typescript
routerId?: pulumi.Input<string>;
```


ID of the router this interface belongs to. Changing
this creates a new router interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerInterface.ts#L100">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


ID of the subnet this interface connects to. Changing
this creates a new router interface.

<h2 class="pdoc-module-header" id="RouterRouteArgs">
<a class="pdoc-member-name" href="/networking/routerRoute.ts#L112">interface RouterRouteArgs</a>
</h2>

The set of arguments for constructing a RouterRoute resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L117">property destinationCidr</a>
</h3>

```typescript
destinationCidr: pulumi.Input<string>;
```


CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L122">property nextHop</a>
</h3>

```typescript
nextHop: pulumi.Input<string>;
```


IP address of the next hop gateway.  Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L129">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L134">property routerId</a>
</h3>

```typescript
routerId: pulumi.Input<string>;
```


ID of the router this routing entry belongs to. Changing
this creates a new routing entry.

<h2 class="pdoc-module-header" id="RouterRouteState">
<a class="pdoc-member-name" href="/networking/routerRoute.ts#L84">interface RouterRouteState</a>
</h2>

Input properties used for looking up and filtering RouterRoute resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L89">property destinationCidr</a>
</h3>

```typescript
destinationCidr?: pulumi.Input<string>;
```


CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L94">property nextHop</a>
</h3>

```typescript
nextHop?: pulumi.Input<string>;
```


IP address of the next hop gateway.  Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L101">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/routerRoute.ts#L106">property routerId</a>
</h3>

```typescript
routerId?: pulumi.Input<string>;
```


ID of the router this routing entry belongs to. Changing
this creates a new routing entry.

<h2 class="pdoc-module-header" id="RouterState">
<a class="pdoc-member-name" href="/networking/router.ts#L141">interface RouterState</a>
</h2>

Input properties used for looking up and filtering Router resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L147">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L153">property availabilityZoneHints</a>
</h3>

```typescript
availabilityZoneHints?: pulumi.Input<pulumi.Input<string>[]>;
```


An availability zone is used to make
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L159">property distributed</a>
</h3>

```typescript
distributed?: pulumi.Input<boolean>;
```


Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L165">property enableSnat</a>
</h3>

```typescript
enableSnat?: pulumi.Input<boolean>;
```


Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L172">property externalFixedIps</a>
</h3>

```typescript
externalFixedIps?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L180">property externalGateway</a>
</h3>

```typescript
externalGateway?: pulumi.Input<string>;
```


The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L187">property externalNetworkId</a>
</h3>

```typescript
externalNetworkId?: pulumi.Input<string>;
```


The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L192">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the router. Changing this
updates the `name` of an existing router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L199">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L204">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L208">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional driver-specific options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/router.ts#L213">property vendorOptions</a>
</h3>

```typescript
vendorOptions?: pulumi.Input<{ ... }>;
```


Map of additional vendor-specific options.
Supported options are described below.

<h2 class="pdoc-module-header" id="SecGroupArgs">
<a class="pdoc-member-name" href="/networking/secGroup.ts#L117">interface SecGroupArgs</a>
</h2>

The set of arguments for constructing a SecGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L123">property deleteDefaultRules</a>
</h3>

```typescript
deleteDefaultRules?: pulumi.Input<boolean>;
```


Whether or not to delete the default
egress security rules. This is `false` by default. See the below note
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L127">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A unique name for the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L131">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L138">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L144">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group.

<h2 class="pdoc-module-header" id="SecGroupRuleArgs">
<a class="pdoc-member-name" href="/networking/secGroupRule.ts#L236">interface SecGroupRuleArgs</a>
</h2>

The set of arguments for constructing a SecGroupRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L241">property direction</a>
</h3>

```typescript
direction: pulumi.Input<string>;
```


The direction of the rule, valid values are __ingress__
or __egress__. Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L246">property ethertype</a>
</h3>

```typescript
ethertype: pulumi.Input<string>;
```


The layer 3 protocol type, valid values are __IPv4__
or __IPv6__. Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L252">property portRangeMax</a>
</h3>

```typescript
portRangeMax?: pulumi.Input<number>;
```


The higher part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L258">property portRangeMin</a>
</h3>

```typescript
portRangeMin?: pulumi.Input<number>;
```


The lower part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L283">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.
* __tcp__
* __udp__
* __icmp__
* __ah__
* __dccp__
* __egp__
* __esp__
* __gre__
* __igmp__
* __ipv6-encap__
* __ipv6-frag__
* __ipv6-icmp__
* __ipv6-nonxt__
* __ipv6-opts__
* __ipv6-route__
* __ospf__
* __pgm__
* __rsvp__
* __sctp__
* __udplite__
* __vrrp__

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L290">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L296">property remoteGroupId</a>
</h3>

```typescript
remoteGroupId?: pulumi.Input<string>;
```


The remote group id, the value needs to be an
Openstack ID of a security group in the same tenant. Changing this creates
a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L301">property remoteIpPrefix</a>
</h3>

```typescript
remoteIpPrefix?: pulumi.Input<string>;
```


The remote CIDR, the value needs to be a valid
CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L307">property securityGroupId</a>
</h3>

```typescript
securityGroupId: pulumi.Input<string>;
```


The security group id the rule should belong
to, the value needs to be an Openstack ID of a security group in the same
tenant. Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L313">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group rule.

<h2 class="pdoc-module-header" id="SecGroupRuleState">
<a class="pdoc-member-name" href="/networking/secGroupRule.ts#L153">interface SecGroupRuleState</a>
</h2>

Input properties used for looking up and filtering SecGroupRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L158">property direction</a>
</h3>

```typescript
direction?: pulumi.Input<string>;
```


The direction of the rule, valid values are __ingress__
or __egress__. Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L163">property ethertype</a>
</h3>

```typescript
ethertype?: pulumi.Input<string>;
```


The layer 3 protocol type, valid values are __IPv4__
or __IPv6__. Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L169">property portRangeMax</a>
</h3>

```typescript
portRangeMax?: pulumi.Input<number>;
```


The higher part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L175">property portRangeMin</a>
</h3>

```typescript
portRangeMin?: pulumi.Input<number>;
```


The lower part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L200">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.
* __tcp__
* __udp__
* __icmp__
* __ah__
* __dccp__
* __egp__
* __esp__
* __gre__
* __igmp__
* __ipv6-encap__
* __ipv6-frag__
* __ipv6-icmp__
* __ipv6-nonxt__
* __ipv6-opts__
* __ipv6-route__
* __ospf__
* __pgm__
* __rsvp__
* __sctp__
* __udplite__
* __vrrp__

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L207">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L213">property remoteGroupId</a>
</h3>

```typescript
remoteGroupId?: pulumi.Input<string>;
```


The remote group id, the value needs to be an
Openstack ID of a security group in the same tenant. Changing this creates
a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L218">property remoteIpPrefix</a>
</h3>

```typescript
remoteIpPrefix?: pulumi.Input<string>;
```


The remote CIDR, the value needs to be a valid
CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L224">property securityGroupId</a>
</h3>

```typescript
securityGroupId?: pulumi.Input<string>;
```


The security group id the rule should belong
to, the value needs to be an Openstack ID of a security group in the same
tenant. Changing this creates a new security group rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroupRule.ts#L230">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group rule.

<h2 class="pdoc-module-header" id="SecGroupState">
<a class="pdoc-member-name" href="/networking/secGroup.ts#L84">interface SecGroupState</a>
</h2>

Input properties used for looking up and filtering SecGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L90">property deleteDefaultRules</a>
</h3>

```typescript
deleteDefaultRules?: pulumi.Input<boolean>;
```


Whether or not to delete the default
egress security rules. This is `false` by default. See the below note
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L94">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A unique name for the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L105">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/secGroup.ts#L111">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group.

<h2 class="pdoc-module-header" id="SubnetArgs">
<a class="pdoc-member-name" href="/networking/subnet.ts#L262">interface SubnetArgs</a>
</h2>

The set of arguments for constructing a Subnet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L268">property allocationPools</a>
</h3>

```typescript
allocationPools?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of sub-ranges of CIDR available for
dynamic allocation to ports. The allocation_pool object structure is
documented below. Changing this creates a new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L274">property cidr</a>
</h3>

```typescript
cidr?: pulumi.Input<string>;
```


CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L280">property dnsNameservers</a>
</h3>

```typescript
dnsNameservers?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L286">property enableDhcp</a>
</h3>

```typescript
enableDhcp?: pulumi.Input<boolean>;
```


The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L293">property gatewayIp</a>
</h3>

```typescript
gatewayIp?: pulumi.Input<string>;
```


Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L300">property hostRoutes</a>
</h3>

```typescript
hostRoutes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L305">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<number>;
```


IP version, either 4 (default) or 6. Changing this creates a
new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L310">property ipv6AddressMode</a>
</h3>

```typescript
ipv6AddressMode?: pulumi.Input<string>;
```


The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L315">property ipv6RaMode</a>
</h3>

```typescript
ipv6RaMode?: pulumi.Input<string>;
```


The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L320">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet. Changing this updates the name of
the existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L325">property networkId</a>
</h3>

```typescript
networkId: pulumi.Input<string>;
```


The UUID of the parent network. Changing this
creates a new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L330">property noGateway</a>
</h3>

```typescript
noGateway?: pulumi.Input<boolean>;
```


Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L337">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L341">property subnetpoolId</a>
</h3>

```typescript
subnetpoolId?: pulumi.Input<string>;
```


The ID of the subnetpool associated with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L346">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L350">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SubnetPoolArgs">
<a class="pdoc-member-name" href="/networking/subnetPool.ts#L276">interface SubnetPoolArgs</a>
</h2>

The set of arguments for constructing a SubnetPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L282">property addressScopeId</a>
</h3>

```typescript
addressScopeId?: pulumi.Input<string>;
```


The Neutron address scope to assign to the
subnetpool. Changing this updates the address scope id of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L289">property defaultPrefixlen</a>
</h3>

```typescript
defaultPrefixlen?: pulumi.Input<number>;
```


The size of the prefix to allocate when the cidr
or prefixlen attributes are omitted when you create the subnet. Defaults to the
MinPrefixLen. Changing this updates the default prefixlen of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L295">property defaultQuota</a>
</h3>

```typescript
defaultQuota?: pulumi.Input<number>;
```


The per-project quota on the prefix space that can be
allocated from the subnetpool for project subnets. Changing this updates the
default quota of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L300">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the subnetpool.
Changing this updates the description of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L304">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<number>;
```


The IP protocol version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L310">property isDefault</a>
</h3>

```typescript
isDefault?: pulumi.Input<boolean>;
```


Indicates whether the subnetpool is default
subnetpool or not. Changing this updates the default status of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L317">property maxPrefixlen</a>
</h3>

```typescript
maxPrefixlen?: pulumi.Input<number>;
```


The maximum prefix size that can be allocated from
the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools,
default is 128. Changing this updates the max prefixlen of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L323">property minPrefixlen</a>
</h3>

```typescript
minPrefixlen?: pulumi.Input<number>;
```


The smallest prefix that can be allocated from a
subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default
is 64. Changing this updates the min prefixlen of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L328">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnetpool. Changing this updates the name of
the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L336">property prefixes</a>
</h3>

```typescript
prefixes: pulumi.Input<pulumi.Input<string>[]>;
```


A list of subnet prefixes to assign to the subnetpool.
Neutron API merges adjacent prefixes and treats them as a single prefix. Each
subnet prefix must be unique among all subnet prefixes in all subnetpools that
are associated with the address scope. Changing this updates the prefixes list
of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L341">property projectId</a>
</h3>

```typescript
projectId?: pulumi.Input<string>;
```


The owner of the subnetpool. Required if admin wants to
create a subnetpool for another project. Changing this creates a new subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L348">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnetpool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L354">property shared</a>
</h3>

```typescript
shared?: pulumi.Input<boolean>;
```


Indicates whether this subnetpool is shared across
all projects. Changing this updates the shared status of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L358">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SubnetPoolState">
<a class="pdoc-member-name" href="/networking/subnetPool.ts#L176">interface SubnetPoolState</a>
</h2>

Input properties used for looking up and filtering SubnetPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L182">property addressScopeId</a>
</h3>

```typescript
addressScopeId?: pulumi.Input<string>;
```


The Neutron address scope to assign to the
subnetpool. Changing this updates the address scope id of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L186">property createdAt</a>
</h3>

```typescript
createdAt?: pulumi.Input<string>;
```


The time at which subnetpool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L193">property defaultPrefixlen</a>
</h3>

```typescript
defaultPrefixlen?: pulumi.Input<number>;
```


The size of the prefix to allocate when the cidr
or prefixlen attributes are omitted when you create the subnet. Defaults to the
MinPrefixLen. Changing this updates the default prefixlen of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L199">property defaultQuota</a>
</h3>

```typescript
defaultQuota?: pulumi.Input<number>;
```


The per-project quota on the prefix space that can be
allocated from the subnetpool for project subnets. Changing this updates the
default quota of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L204">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The human-readable description for the subnetpool.
Changing this updates the description of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L208">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<number>;
```


The IP protocol version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L214">property isDefault</a>
</h3>

```typescript
isDefault?: pulumi.Input<boolean>;
```


Indicates whether the subnetpool is default
subnetpool or not. Changing this updates the default status of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L221">property maxPrefixlen</a>
</h3>

```typescript
maxPrefixlen?: pulumi.Input<number>;
```


The maximum prefix size that can be allocated from
the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools,
default is 128. Changing this updates the max prefixlen of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L227">property minPrefixlen</a>
</h3>

```typescript
minPrefixlen?: pulumi.Input<number>;
```


The smallest prefix that can be allocated from a
subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default
is 64. Changing this updates the min prefixlen of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L232">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnetpool. Changing this updates the name of
the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L240">property prefixes</a>
</h3>

```typescript
prefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of subnet prefixes to assign to the subnetpool.
Neutron API merges adjacent prefixes and treats them as a single prefix. Each
subnet prefix must be unique among all subnet prefixes in all subnetpools that
are associated with the address scope. Changing this updates the prefixes list
of the existing subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L245">property projectId</a>
</h3>

```typescript
projectId?: pulumi.Input<string>;
```


The owner of the subnetpool. Required if admin wants to
create a subnetpool for another project. Changing this creates a new subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L252">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnetpool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L256">property revisionNumber</a>
</h3>

```typescript
revisionNumber?: pulumi.Input<number>;
```


The revision number of the subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L262">property shared</a>
</h3>

```typescript
shared?: pulumi.Input<boolean>;
```


Indicates whether this subnetpool is shared across
all projects. Changing this updates the shared status of the existing
subnetpool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L266">property updatedAt</a>
</h3>

```typescript
updatedAt?: pulumi.Input<string>;
```


The time at which subnetpool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetPool.ts#L270">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SubnetRouteArgs">
<a class="pdoc-member-name" href="/networking/subnetRoute.ts#L112">interface SubnetRouteArgs</a>
</h2>

The set of arguments for constructing a SubnetRoute resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L117">property destinationCidr</a>
</h3>

```typescript
destinationCidr: pulumi.Input<string>;
```


CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L122">property nextHop</a>
</h3>

```typescript
nextHop: pulumi.Input<string>;
```


IP address of the next hop gateway.  Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L129">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L134">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


ID of the subnet this routing entry belongs to. Changing
this creates a new routing entry.

<h2 class="pdoc-module-header" id="SubnetRouteState">
<a class="pdoc-member-name" href="/networking/subnetRoute.ts#L84">interface SubnetRouteState</a>
</h2>

Input properties used for looking up and filtering SubnetRoute resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L89">property destinationCidr</a>
</h3>

```typescript
destinationCidr?: pulumi.Input<string>;
```


CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L94">property nextHop</a>
</h3>

```typescript
nextHop?: pulumi.Input<string>;
```


IP address of the next hop gateway.  Changing
this creates a new routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L101">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
routing entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnetRoute.ts#L106">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


ID of the subnet this routing entry belongs to. Changing
this creates a new routing entry.

<h2 class="pdoc-module-header" id="SubnetState">
<a class="pdoc-member-name" href="/networking/subnet.ts#L168">interface SubnetState</a>
</h2>

Input properties used for looking up and filtering Subnet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L174">property allocationPools</a>
</h3>

```typescript
allocationPools?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of sub-ranges of CIDR available for
dynamic allocation to ports. The allocation_pool object structure is
documented below. Changing this creates a new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L180">property cidr</a>
</h3>

```typescript
cidr?: pulumi.Input<string>;
```


CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L186">property dnsNameservers</a>
</h3>

```typescript
dnsNameservers?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L192">property enableDhcp</a>
</h3>

```typescript
enableDhcp?: pulumi.Input<boolean>;
```


The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L199">property gatewayIp</a>
</h3>

```typescript
gatewayIp?: pulumi.Input<string>;
```


Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L206">property hostRoutes</a>
</h3>

```typescript
hostRoutes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L211">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<number>;
```


IP version, either 4 (default) or 6. Changing this creates a
new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L216">property ipv6AddressMode</a>
</h3>

```typescript
ipv6AddressMode?: pulumi.Input<string>;
```


The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L221">property ipv6RaMode</a>
</h3>

```typescript
ipv6RaMode?: pulumi.Input<string>;
```


The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L226">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet. Changing this updates the name of
the existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L231">property networkId</a>
</h3>

```typescript
networkId?: pulumi.Input<string>;
```


The UUID of the parent network. Changing this
creates a new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L236">property noGateway</a>
</h3>

```typescript
noGateway?: pulumi.Input<boolean>;
```


Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L243">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L247">property subnetpoolId</a>
</h3>

```typescript
subnetpoolId?: pulumi.Input<string>;
```


The ID of the subnetpool associated with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L252">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/networking/subnet.ts#L256">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

