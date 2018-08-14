---
title: Module loadbalancer
---

<a href="../index.html">@pulumi/openstack</a> &gt; loadbalancer

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Listener">class Listener</a>
* <a href="#LoadBalancer">class LoadBalancer</a>
* <a href="#Member">class Member</a>
* <a href="#MemberV1">class MemberV1</a>
* <a href="#Monitor">class Monitor</a>
* <a href="#MonitorV1">class MonitorV1</a>
* <a href="#Pool">class Pool</a>
* <a href="#PoolV1">class PoolV1</a>
* <a href="#Vip">class Vip</a>
* <a href="#ListenerArgs">interface ListenerArgs</a>
* <a href="#ListenerState">interface ListenerState</a>
* <a href="#LoadBalancerArgs">interface LoadBalancerArgs</a>
* <a href="#LoadBalancerState">interface LoadBalancerState</a>
* <a href="#MemberArgs">interface MemberArgs</a>
* <a href="#MemberState">interface MemberState</a>
* <a href="#MemberV1Args">interface MemberV1Args</a>
* <a href="#MemberV1State">interface MemberV1State</a>
* <a href="#MonitorArgs">interface MonitorArgs</a>
* <a href="#MonitorState">interface MonitorState</a>
* <a href="#MonitorV1Args">interface MonitorV1Args</a>
* <a href="#MonitorV1State">interface MonitorV1State</a>
* <a href="#PoolArgs">interface PoolArgs</a>
* <a href="#PoolState">interface PoolState</a>
* <a href="#PoolV1Args">interface PoolV1Args</a>
* <a href="#PoolV1State">interface PoolV1State</a>
* <a href="#VipArgs">interface VipArgs</a>
* <a href="#VipState">interface VipState</a>

<a href="/loadbalancer/listener.ts">loadbalancer/listener.ts</a> <a href="/loadbalancer/loadBalancer.ts">loadbalancer/loadBalancer.ts</a> <a href="/loadbalancer/member.ts">loadbalancer/member.ts</a> <a href="/loadbalancer/memberV1.ts">loadbalancer/memberV1.ts</a> <a href="/loadbalancer/monitor.ts">loadbalancer/monitor.ts</a> <a href="/loadbalancer/monitorV1.ts">loadbalancer/monitorV1.ts</a> <a href="/loadbalancer/pool.ts">loadbalancer/pool.ts</a> <a href="/loadbalancer/poolV1.ts">loadbalancer/poolV1.ts</a> <a href="/loadbalancer/vip.ts">loadbalancer/vip.ts</a> 


<h2 class="pdoc-module-header" id="Listener">
<a class="pdoc-member-name" href="/loadbalancer/listener.ts#L9">class Listener</a>
</h2>

Manages a V2 listener resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L88">constructor</a>
</h3>

```typescript
new Listener(name: string, args: ListenerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Listener resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ListenerState): Listener
```


Get an existing Listener resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L26">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L31">property connectionLimit</a>
</h3>

```typescript
public connectionLimit: pulumi.Output<number>;
```


The maximum number of connections allowed
for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L36">property defaultPoolId</a>
</h3>

```typescript
public defaultPoolId: pulumi.Output<string>;
```


The ID of the default pool with which the
Listener is associated. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L44">property defaultTlsContainerRef</a>
</h3>

```typescript
public defaultTlsContainerRef: pulumi.Output<string | undefined>;
```


A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L48">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Human-readable description for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L53">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The load balancer on which to provision this
Listener. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L58">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Human-readable name for the Listener. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L63">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol - can either be TCP, HTTP, HTTPS or TERMINATED_HTTPS.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L68">property protocolPort</a>
</h3>

```typescript
public protocolPort: pulumi.Output<number>;
```


The port on which to listen for client traffic.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L75">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L82">property sniContainerRefs</a>
</h3>

```typescript
public sniContainerRefs: pulumi.Output<string[] | undefined>;
```


A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L88">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LoadBalancer">
<a class="pdoc-member-name" href="/loadbalancer/loadBalancer.ts#L9">class LoadBalancer</a>
</h2>

Manages a V2 loadbalancer resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L80">constructor</a>
</h3>

```typescript
new LoadBalancer(name: string, args: LoadBalancerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LoadBalancer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerState): LoadBalancer
```


Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L26">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Human-readable description for the Loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L35">property flavor</a>
</h3>

```typescript
public flavor: pulumi.Output<string | undefined>;
```


The UUID of a flavor. Changing this creates a new
loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L40">property loadbalancerProvider</a>
</h3>

```typescript
public loadbalancerProvider: pulumi.Output<string>;
```


The name of the provider. Changing this
creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Human-readable name for the Loadbalancer. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L52">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L58">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[]>;
```


A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L64">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


Required for admins. The UUID of the tenant who owns
the Loadbalancer.  Only administrative users can specify a tenant UUID
other than their own.  Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L69">property vipAddress</a>
</h3>

```typescript
public vipAddress: pulumi.Output<string>;
```


The ip address of the load balancer.
Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L73">property vipPortId</a>
</h3>

```typescript
public vipPortId: pulumi.Output<string>;
```


The Port ID of the Load Balancer IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L80">property vipSubnetId</a>
</h3>

```typescript
public vipSubnetId: pulumi.Output<string>;
```


The network on which to allocate the
Loadbalancer's address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.

<h2 class="pdoc-module-header" id="Member">
<a class="pdoc-member-name" href="/loadbalancer/member.ts#L9">class Member</a>
</h2>

Manages a V2 member resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L69">constructor</a>
</h3>

```typescript
new Member(name: string, args: MemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Member resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MemberState): Member
```


Get an existing Member resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L26">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L31">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the member.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Human-readable name for the member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L40">property poolId</a>
</h3>

```typescript
public poolId: pulumi.Output<string>;
```


The id of the pool that this member will be
assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L45">property protocolPort</a>
</h3>

```typescript
public protocolPort: pulumi.Output<number>;
```


The port on which to listen for client traffic.
Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L52">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L56">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string | undefined>;
```


The subnet in which to access the member

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L62">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


Required for admins. The UUID of the tenant who owns
the member.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L69">property weight</a>
</h3>

```typescript
public weight: pulumi.Output<number>;
```


A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.

<h2 class="pdoc-module-header" id="MemberV1">
<a class="pdoc-member-name" href="/loadbalancer/memberV1.ts#L9">class MemberV1</a>
</h2>

Manages a V1 load balancer member resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L59">constructor</a>
</h3>

```typescript
new MemberV1(name: string, args: MemberV1Args, opts?: pulumi.CustomResourceOptions)
```


Create a MemberV1 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MemberV1State): MemberV1
```


Get an existing MemberV1 resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L26">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The IP address of the member. Changing this creates a
new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L32">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean>;
```


The administrative state of the member.
Acceptable values are 'true' and 'false'. Changing this value updates the
state of the existing member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L37">property poolId</a>
</h3>

```typescript
public poolId: pulumi.Output<string>;
```


The ID of the LB pool. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L42">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


An integer representing the port on which the member is
hosted. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L49">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L54">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string | undefined>;
```


The owner of the member. Required if admin wants to
create a member for another tenant. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L59">property weight</a>
</h3>

```typescript
public weight: pulumi.Output<number>;
```


The load balancing weight of the member. This is currently unable
to be set through Terraform.

<h2 class="pdoc-module-header" id="Monitor">
<a class="pdoc-member-name" href="/loadbalancer/monitor.ts#L9">class Monitor</a>
</h2>

Manages a V2 monitor resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L86">constructor</a>
</h3>

```typescript
new Monitor(name: string, args: MonitorArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Monitor resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MonitorState): Monitor
```


Get an existing Monitor resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L26">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L30">property delay</a>
</h3>

```typescript
public delay: pulumi.Output<number>;
```


The time, in seconds, between sending probes to members.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L36">property expectedCodes</a>
</h3>

```typescript
public expectedCodes: pulumi.Output<string>;
```


Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L42">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it
defaults to "GET".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L48">property maxRetries</a>
</h3>

```typescript
public maxRetries: pulumi.Output<number>;
```


Number of permissible ping failures before
changing the member's status to INACTIVE. Must be a number between 1
and 10..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L52">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The Name of the Monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L56">property poolId</a>
</h3>

```typescript
public poolId: pulumi.Output<string>;
```


The id of the pool that this monitor will be assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L63">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L69">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L75">property timeout</a>
</h3>

```typescript
public timeout: pulumi.Output<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L81">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the load balancer to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L86">property urlPath</a>
</h3>

```typescript
public urlPath: pulumi.Output<string>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MonitorV1">
<a class="pdoc-member-name" href="/loadbalancer/monitorV1.ts#L9">class MonitorV1</a>
</h2>

Manages a V1 load balancer monitor resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L81">constructor</a>
</h3>

```typescript
new MonitorV1(name: string, args: MonitorV1Args, opts?: pulumi.CustomResourceOptions)
```


Create a MonitorV1 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MonitorV1State): MonitorV1
```


Get an existing MonitorV1 resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<string>;
```


The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L32">property delay</a>
</h3>

```typescript
public delay: pulumi.Output<number>;
```


The time, in seconds, between sending probes to members.
Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L39">property expectedCodes</a>
</h3>

```typescript
public expectedCodes: pulumi.Output<string | undefined>;
```


equired for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L45">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string | undefined>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L51">property maxRetries</a>
</h3>

```typescript
public maxRetries: pulumi.Output<number>;
```


Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L58">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L63">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L69">property timeout</a>
</h3>

```typescript
public timeout: pulumi.Output<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L75">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L81">property urlPath</a>
</h3>

```typescript
public urlPath: pulumi.Output<string | undefined>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Pool">
<a class="pdoc-member-name" href="/loadbalancer/pool.ts#L9">class Pool</a>
</h2>

Manages a V2 pool resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L75">constructor</a>
</h3>

```typescript
new Pool(name: string, args: PoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Pool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PoolState): Pool
```


Get an existing Pool resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L26">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the pool.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Human-readable description for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L36">property lbMethod</a>
</h3>

```typescript
public lbMethod: pulumi.Output<string>;
```


The load balancing algorithm to
distribute traffic to the pool's members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L42">property listenerId</a>
</h3>

```typescript
public listenerId: pulumi.Output<string | undefined>;
```


The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L48">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string | undefined>;
```


The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L52">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Human-readable name for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L58">property persistences</a>
</h3>

```typescript
public persistences: pulumi.Output<{ ... }[] | undefined>;
```


Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L62">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L69">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L75">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


Required for admins. The UUID of the tenant who owns
the pool.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PoolV1">
<a class="pdoc-member-name" href="/loadbalancer/poolV1.ts#L9">class PoolV1</a>
</h2>

Manages a V1 load balancer pool resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L65">constructor</a>
</h3>

```typescript
new PoolV1(name: string, args: PoolV1Args, opts?: pulumi.CustomResourceOptions)
```


Create a PoolV1 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PoolV1State): PoolV1
```


Get an existing PoolV1 resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L27">property lbMethod</a>
</h3>

```typescript
public lbMethod: pulumi.Output<string>;
```


The algorithm used to distribute load between the
members of the pool. The current specification supports 'ROUND_ROBIN' and
'LEAST_CONNECTIONS' as valid values for this attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L32">property lbProvider</a>
</h3>

```typescript
public lbProvider: pulumi.Output<string>;
```


The backend load balancing provider. For example:
`haproxy`, `F5`, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L37">property monitorIds</a>
</h3>

```typescript
public monitorIds: pulumi.Output<string[] | undefined>;
```


A list of IDs of monitors to associate with the
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the pool. Changing this updates the name of
the existing pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L47">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol used by the pool members, you can use
either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L54">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L60">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L65">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the member. Required if admin wants to
create a pool member for another tenant. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Vip">
<a class="pdoc-member-name" href="/loadbalancer/vip.ts#L9">class Vip</a>
</h2>

Manages a V1 load balancer vip resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L97">constructor</a>
</h3>

```typescript
new Vip(name: string, args: VipArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Vip resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VipState): Vip
```


Get an existing Vip resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L26">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The IP address of the vip. Changing this creates a new
vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L32">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean>;
```


The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L38">property connLimit</a>
</h3>

```typescript
public connLimit: pulumi.Output<number>;
```


The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L43">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


Human-readable description for the vip. Changing
this updates the description of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L48">property floatingIp</a>
</h3>

```typescript
public floatingIp: pulumi.Output<string | undefined>;
```


A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the vip. Changing this updates the name of
the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L59">property persistence</a>
</h3>

```typescript
public persistence: pulumi.Output<{ ... } | undefined>;
```


Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L64">property poolId</a>
</h3>

```typescript
public poolId: pulumi.Output<string>;
```


The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L69">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The port on which to listen for client traffic. Changing
this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L73">property portId</a>
</h3>

```typescript
public portId: pulumi.Output<string>;
```


Port UUID for this VIP at associated floating IP (if any).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L78">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L85">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L92">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L97">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ListenerArgs">
<a class="pdoc-member-name" href="/loadbalancer/listener.ts#L218">interface ListenerArgs</a>
</h2>

The set of arguments for constructing a Listener resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L223">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L228">property connectionLimit</a>
</h3>

```typescript
connectionLimit?: pulumi.Input<number>;
```


The maximum number of connections allowed
for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L233">property defaultPoolId</a>
</h3>

```typescript
defaultPoolId?: pulumi.Input<string>;
```


The ID of the default pool with which the
Listener is associated. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L241">property defaultTlsContainerRef</a>
</h3>

```typescript
defaultTlsContainerRef?: pulumi.Input<string>;
```


A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L245">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L250">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The load balancer on which to provision this
Listener. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L255">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the Listener. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L260">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol - can either be TCP, HTTP, HTTPS or TERMINATED_HTTPS.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L265">property protocolPort</a>
</h3>

```typescript
protocolPort: pulumi.Input<number>;
```


The port on which to listen for client traffic.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L272">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L279">property sniContainerRefs</a>
</h3>

```typescript
sniContainerRefs?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L285">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.

<h2 class="pdoc-module-header" id="ListenerState">
<a class="pdoc-member-name" href="/loadbalancer/listener.ts#L145">interface ListenerState</a>
</h2>

Input properties used for looking up and filtering Listener resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L150">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L155">property connectionLimit</a>
</h3>

```typescript
connectionLimit?: pulumi.Input<number>;
```


The maximum number of connections allowed
for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L160">property defaultPoolId</a>
</h3>

```typescript
defaultPoolId?: pulumi.Input<string>;
```


The ID of the default pool with which the
Listener is associated. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L168">property defaultTlsContainerRef</a>
</h3>

```typescript
defaultTlsContainerRef?: pulumi.Input<string>;
```


A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L172">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L177">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The load balancer on which to provision this
Listener. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L182">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the Listener. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L187">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol - can either be TCP, HTTP, HTTPS or TERMINATED_HTTPS.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L192">property protocolPort</a>
</h3>

```typescript
protocolPort?: pulumi.Input<number>;
```


The port on which to listen for client traffic.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L199">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L206">property sniContainerRefs</a>
</h3>

```typescript
sniContainerRefs?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L212">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.

<h2 class="pdoc-module-header" id="LoadBalancerArgs">
<a class="pdoc-member-name" href="/loadbalancer/loadBalancer.ts#L194">interface LoadBalancerArgs</a>
</h2>

The set of arguments for constructing a LoadBalancer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L199">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L203">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the Loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L208">property flavor</a>
</h3>

```typescript
flavor?: pulumi.Input<string>;
```


The UUID of a flavor. Changing this creates a new
loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L213">property loadbalancerProvider</a>
</h3>

```typescript
loadbalancerProvider?: pulumi.Input<string>;
```


The name of the provider. Changing this
creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L218">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the Loadbalancer. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L225">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L231">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L237">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the Loadbalancer.  Only administrative users can specify a tenant UUID
other than their own.  Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L242">property vipAddress</a>
</h3>

```typescript
vipAddress?: pulumi.Input<string>;
```


The ip address of the load balancer.
Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L249">property vipSubnetId</a>
</h3>

```typescript
vipSubnetId: pulumi.Input<string>;
```


The network on which to allocate the
Loadbalancer's address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.

<h2 class="pdoc-module-header" id="LoadBalancerState">
<a class="pdoc-member-name" href="/loadbalancer/loadBalancer.ts#L129">interface LoadBalancerState</a>
</h2>

Input properties used for looking up and filtering LoadBalancer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L134">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L138">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the Loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L143">property flavor</a>
</h3>

```typescript
flavor?: pulumi.Input<string>;
```


The UUID of a flavor. Changing this creates a new
loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L148">property loadbalancerProvider</a>
</h3>

```typescript
loadbalancerProvider?: pulumi.Input<string>;
```


The name of the provider. Changing this
creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L153">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the Loadbalancer. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L160">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L166">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L172">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the Loadbalancer.  Only administrative users can specify a tenant UUID
other than their own.  Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L177">property vipAddress</a>
</h3>

```typescript
vipAddress?: pulumi.Input<string>;
```


The ip address of the load balancer.
Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L181">property vipPortId</a>
</h3>

```typescript
vipPortId?: pulumi.Input<string>;
```


The Port ID of the Load Balancer IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L188">property vipSubnetId</a>
</h3>

```typescript
vipSubnetId?: pulumi.Input<string>;
```


The network on which to allocate the
Loadbalancer's address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.

<h2 class="pdoc-module-header" id="MemberArgs">
<a class="pdoc-member-name" href="/loadbalancer/member.ts#L174">interface MemberArgs</a>
</h2>

The set of arguments for constructing a Member resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L179">property address</a>
</h3>

```typescript
address: pulumi.Input<string>;
```


The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L184">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the member.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L188">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L193">property poolId</a>
</h3>

```typescript
poolId: pulumi.Input<string>;
```


The id of the pool that this member will be
assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L198">property protocolPort</a>
</h3>

```typescript
protocolPort: pulumi.Input<number>;
```


The port on which to listen for client traffic.
Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L205">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L209">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The subnet in which to access the member

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L215">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the member.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L222">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.

<h2 class="pdoc-module-header" id="MemberState">
<a class="pdoc-member-name" href="/loadbalancer/member.ts#L120">interface MemberState</a>
</h2>

Input properties used for looking up and filtering Member resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L125">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L130">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the member.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L134">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L139">property poolId</a>
</h3>

```typescript
poolId?: pulumi.Input<string>;
```


The id of the pool that this member will be
assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L144">property protocolPort</a>
</h3>

```typescript
protocolPort?: pulumi.Input<number>;
```


The port on which to listen for client traffic.
Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L151">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L155">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The subnet in which to access the member

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L161">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the member.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L168">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.

<h2 class="pdoc-module-header" id="MemberV1Args">
<a class="pdoc-member-name" href="/loadbalancer/memberV1.ts#L150">interface MemberV1Args</a>
</h2>

The set of arguments for constructing a MemberV1 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L155">property address</a>
</h3>

```typescript
address: pulumi.Input<string>;
```


The IP address of the member. Changing this creates a
new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L161">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the member.
Acceptable values are 'true' and 'false'. Changing this value updates the
state of the existing member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L166">property poolId</a>
</h3>

```typescript
poolId: pulumi.Input<string>;
```


The ID of the LB pool. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L171">property port</a>
</h3>

```typescript
port: pulumi.Input<number>;
```


An integer representing the port on which the member is
hosted. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L178">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L183">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the member. Required if admin wants to
create a member for another tenant. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L188">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


The load balancing weight of the member. This is currently unable
to be set through Terraform.

<h2 class="pdoc-module-header" id="MemberV1State">
<a class="pdoc-member-name" href="/loadbalancer/memberV1.ts#L106">interface MemberV1State</a>
</h2>

Input properties used for looking up and filtering MemberV1 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L111">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address of the member. Changing this creates a
new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L117">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the member.
Acceptable values are 'true' and 'false'. Changing this value updates the
state of the existing member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L122">property poolId</a>
</h3>

```typescript
poolId?: pulumi.Input<string>;
```


The ID of the LB pool. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L127">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


An integer representing the port on which the member is
hosted. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L134">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L139">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the member. Required if admin wants to
create a member for another tenant. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L144">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


The load balancing weight of the member. This is currently unable
to be set through Terraform.

<h2 class="pdoc-module-header" id="MonitorArgs">
<a class="pdoc-member-name" href="/loadbalancer/monitor.ts#L220">interface MonitorArgs</a>
</h2>

The set of arguments for constructing a Monitor resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L225">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L229">property delay</a>
</h3>

```typescript
delay: pulumi.Input<number>;
```


The time, in seconds, between sending probes to members.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L235">property expectedCodes</a>
</h3>

```typescript
expectedCodes?: pulumi.Input<string>;
```


Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L241">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it
defaults to "GET".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L247">property maxRetries</a>
</h3>

```typescript
maxRetries: pulumi.Input<number>;
```


Number of permissible ping failures before
changing the member's status to INACTIVE. Must be a number between 1
and 10..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L251">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the Monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L255">property poolId</a>
</h3>

```typescript
poolId: pulumi.Input<string>;
```


The id of the pool that this monitor will be assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L262">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L268">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L274">property timeout</a>
</h3>

```typescript
timeout: pulumi.Input<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L280">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the load balancer to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L285">property urlPath</a>
</h3>

```typescript
urlPath?: pulumi.Input<string>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS.

<h2 class="pdoc-module-header" id="MonitorState">
<a class="pdoc-member-name" href="/loadbalancer/monitor.ts#L149">interface MonitorState</a>
</h2>

Input properties used for looking up and filtering Monitor resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L154">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L158">property delay</a>
</h3>

```typescript
delay?: pulumi.Input<number>;
```


The time, in seconds, between sending probes to members.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L164">property expectedCodes</a>
</h3>

```typescript
expectedCodes?: pulumi.Input<string>;
```


Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L170">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it
defaults to "GET".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L176">property maxRetries</a>
</h3>

```typescript
maxRetries?: pulumi.Input<number>;
```


Number of permissible ping failures before
changing the member's status to INACTIVE. Must be a number between 1
and 10..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L180">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the Monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L184">property poolId</a>
</h3>

```typescript
poolId?: pulumi.Input<string>;
```


The id of the pool that this monitor will be assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L191">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L197">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L203">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L209">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the load balancer to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L214">property urlPath</a>
</h3>

```typescript
urlPath?: pulumi.Input<string>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS.

<h2 class="pdoc-module-header" id="MonitorV1Args">
<a class="pdoc-member-name" href="/loadbalancer/monitorV1.ts#L203">interface MonitorV1Args</a>
</h2>

The set of arguments for constructing a MonitorV1 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L209">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<string>;
```


The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L214">property delay</a>
</h3>

```typescript
delay: pulumi.Input<number>;
```


The time, in seconds, between sending probes to members.
Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L221">property expectedCodes</a>
</h3>

```typescript
expectedCodes?: pulumi.Input<string>;
```


equired for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L227">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L233">property maxRetries</a>
</h3>

```typescript
maxRetries: pulumi.Input<number>;
```


Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L240">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L245">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L251">property timeout</a>
</h3>

```typescript
timeout: pulumi.Input<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L257">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L263">property urlPath</a>
</h3>

```typescript
urlPath?: pulumi.Input<string>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.

<h2 class="pdoc-module-header" id="MonitorV1State">
<a class="pdoc-member-name" href="/loadbalancer/monitorV1.ts#L137">interface MonitorV1State</a>
</h2>

Input properties used for looking up and filtering MonitorV1 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L143">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<string>;
```


The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L148">property delay</a>
</h3>

```typescript
delay?: pulumi.Input<number>;
```


The time, in seconds, between sending probes to members.
Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L155">property expectedCodes</a>
</h3>

```typescript
expectedCodes?: pulumi.Input<string>;
```


equired for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L161">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L167">property maxRetries</a>
</h3>

```typescript
maxRetries?: pulumi.Input<number>;
```


Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L174">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L179">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L185">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L191">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L197">property urlPath</a>
</h3>

```typescript
urlPath?: pulumi.Input<string>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.

<h2 class="pdoc-module-header" id="PoolArgs">
<a class="pdoc-member-name" href="/loadbalancer/pool.ts#L185">interface PoolArgs</a>
</h2>

The set of arguments for constructing a Pool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L190">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the pool.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L194">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L200">property lbMethod</a>
</h3>

```typescript
lbMethod: pulumi.Input<string>;
```


The load balancing algorithm to
distribute traffic to the pool's members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L206">property listenerId</a>
</h3>

```typescript
listenerId?: pulumi.Input<string>;
```


The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L212">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L216">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L222">property persistences</a>
</h3>

```typescript
persistences?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L226">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L233">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L239">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the pool.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new pool.

<h2 class="pdoc-module-header" id="PoolState">
<a class="pdoc-member-name" href="/loadbalancer/pool.ts#L125">interface PoolState</a>
</h2>

Input properties used for looking up and filtering Pool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L130">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the pool.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L134">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L140">property lbMethod</a>
</h3>

```typescript
lbMethod?: pulumi.Input<string>;
```


The load balancing algorithm to
distribute traffic to the pool's members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L146">property listenerId</a>
</h3>

```typescript
listenerId?: pulumi.Input<string>;
```


The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L152">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L162">property persistences</a>
</h3>

```typescript
persistences?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L166">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L173">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L179">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the pool.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new pool.

<h2 class="pdoc-module-header" id="PoolV1Args">
<a class="pdoc-member-name" href="/loadbalancer/poolV1.ts#L164">interface PoolV1Args</a>
</h2>

The set of arguments for constructing a PoolV1 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L170">property lbMethod</a>
</h3>

```typescript
lbMethod: pulumi.Input<string>;
```


The algorithm used to distribute load between the
members of the pool. The current specification supports 'ROUND_ROBIN' and
'LEAST_CONNECTIONS' as valid values for this attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L175">property lbProvider</a>
</h3>

```typescript
lbProvider?: pulumi.Input<string>;
```


The backend load balancing provider. For example:
`haproxy`, `F5`, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L180">property monitorIds</a>
</h3>

```typescript
monitorIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IDs of monitors to associate with the
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L185">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the pool. Changing this updates the name of
the existing pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L190">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol used by the pool members, you can use
either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L197">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L203">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L208">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the member. Required if admin wants to
create a pool member for another tenant. Changing this creates a new member.

<h2 class="pdoc-module-header" id="PoolV1State">
<a class="pdoc-member-name" href="/loadbalancer/poolV1.ts#L114">interface PoolV1State</a>
</h2>

Input properties used for looking up and filtering PoolV1 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L120">property lbMethod</a>
</h3>

```typescript
lbMethod?: pulumi.Input<string>;
```


The algorithm used to distribute load between the
members of the pool. The current specification supports 'ROUND_ROBIN' and
'LEAST_CONNECTIONS' as valid values for this attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L125">property lbProvider</a>
</h3>

```typescript
lbProvider?: pulumi.Input<string>;
```


The backend load balancing provider. For example:
`haproxy`, `F5`, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L130">property monitorIds</a>
</h3>

```typescript
monitorIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IDs of monitors to associate with the
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the pool. Changing this updates the name of
the existing pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L140">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol used by the pool members, you can use
either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L147">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L153">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L158">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the member. Required if admin wants to
create a pool member for another tenant. Changing this creates a new member.

<h2 class="pdoc-module-header" id="VipArgs">
<a class="pdoc-member-name" href="/loadbalancer/vip.ts#L243">interface VipArgs</a>
</h2>

The set of arguments for constructing a Vip resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L248">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address of the vip. Changing this creates a new
vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L254">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L260">property connLimit</a>
</h3>

```typescript
connLimit?: pulumi.Input<number>;
```


The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L265">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the vip. Changing
this updates the description of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L270">property floatingIp</a>
</h3>

```typescript
floatingIp?: pulumi.Input<string>;
```


A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L275">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the vip. Changing this updates the name of
the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L281">property persistence</a>
</h3>

```typescript
persistence?: pulumi.Input<{ ... }>;
```


Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L286">property poolId</a>
</h3>

```typescript
poolId: pulumi.Input<string>;
```


The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L291">property port</a>
</h3>

```typescript
port: pulumi.Input<number>;
```


The port on which to listen for client traffic. Changing
this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L296">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L303">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L310">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L315">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.

<h2 class="pdoc-module-header" id="VipState">
<a class="pdoc-member-name" href="/loadbalancer/vip.ts#L161">interface VipState</a>
</h2>

Input properties used for looking up and filtering Vip resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L166">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address of the vip. Changing this creates a new
vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L172">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L178">property connLimit</a>
</h3>

```typescript
connLimit?: pulumi.Input<number>;
```


The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L183">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the vip. Changing
this updates the description of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L188">property floatingIp</a>
</h3>

```typescript
floatingIp?: pulumi.Input<string>;
```


A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L193">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the vip. Changing this updates the name of
the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L199">property persistence</a>
</h3>

```typescript
persistence?: pulumi.Input<{ ... }>;
```


Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L204">property poolId</a>
</h3>

```typescript
poolId?: pulumi.Input<string>;
```


The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L209">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which to listen for client traffic. Changing
this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L213">property portId</a>
</h3>

```typescript
portId?: pulumi.Input<string>;
```


Port UUID for this VIP at associated floating IP (if any).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L218">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L225">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L232">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L237">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.

