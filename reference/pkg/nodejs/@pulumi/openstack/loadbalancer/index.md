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
<a class="pdoc-member-name" href="/loadbalancer/listener.ts#L10">class Listener</a>
</h2>

Manages a V2 listener resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L89">constructor</a>
</h3>

```typescript
new Listener(name: string, args: ListenerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Listener resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L32">property connectionLimit</a>
</h3>

```typescript
public connectionLimit: pulumi.Output<number>;
```


The maximum number of connections allowed
for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L37">property defaultPoolId</a>
</h3>

```typescript
public defaultPoolId: pulumi.Output<string>;
```


The ID of the default pool with which the
Listener is associated. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L45">property defaultTlsContainerRef</a>
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
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L49">property description</a>
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
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L54">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The load balancer on which to provision this
Listener. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L59">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Human-readable name for the Listener. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L64">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol - can either be TCP, HTTP, HTTPS or TERMINATED_HTTPS.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L69">property protocolPort</a>
</h3>

```typescript
public protocolPort: pulumi.Output<number>;
```


The port on which to listen for client traffic.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L76">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L83">property sniContainerRefs</a>
</h3>

```typescript
public sniContainerRefs: pulumi.Output<string[] | undefined>;
```


A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L89">property tenantId</a>
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
<a class="pdoc-member-name" href="/loadbalancer/loadBalancer.ts#L10">class LoadBalancer</a>
</h2>

Manages a V2 loadbalancer resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L81">constructor</a>
</h3>

```typescript
new LoadBalancer(name: string, args: LoadBalancerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LoadBalancer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Human-readable description for the Loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L36">property flavor</a>
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
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L41">property loadbalancerProvider</a>
</h3>

```typescript
public loadbalancerProvider: pulumi.Output<string>;
```


The name of the provider. Changing this
creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Human-readable name for the Loadbalancer. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L53">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L59">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[]>;
```


A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L65">property tenantId</a>
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
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L70">property vipAddress</a>
</h3>

```typescript
public vipAddress: pulumi.Output<string>;
```


The ip address of the load balancer.
Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L74">property vipPortId</a>
</h3>

```typescript
public vipPortId: pulumi.Output<string>;
```


The Port ID of the Load Balancer IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L81">property vipSubnetId</a>
</h3>

```typescript
public vipSubnetId: pulumi.Output<string>;
```


The network on which to allocate the
Loadbalancer's address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.

<h2 class="pdoc-module-header" id="Member">
<a class="pdoc-member-name" href="/loadbalancer/member.ts#L10">class Member</a>
</h2>

Manages a V2 member resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L70">constructor</a>
</h3>

```typescript
new Member(name: string, args: MemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Member resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L27">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L32">property adminStateUp</a>
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
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Human-readable name for the member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L41">property poolId</a>
</h3>

```typescript
public poolId: pulumi.Output<string>;
```


The id of the pool that this member will be
assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L46">property protocolPort</a>
</h3>

```typescript
public protocolPort: pulumi.Output<number>;
```


The port on which to listen for client traffic.
Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L53">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L57">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string | undefined>;
```


The subnet in which to access the member

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L63">property tenantId</a>
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
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L70">property weight</a>
</h3>

```typescript
public weight: pulumi.Output<number>;
```


A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.

<h2 class="pdoc-module-header" id="MemberV1">
<a class="pdoc-member-name" href="/loadbalancer/memberV1.ts#L10">class MemberV1</a>
</h2>

Manages a V1 load balancer member resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L60">constructor</a>
</h3>

```typescript
new MemberV1(name: string, args: MemberV1Args, opts?: pulumi.CustomResourceOptions)
```


Create a MemberV1 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L27">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The IP address of the member. Changing this creates a
new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L33">property adminStateUp</a>
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
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L38">property poolId</a>
</h3>

```typescript
public poolId: pulumi.Output<string>;
```


The ID of the LB pool. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L43">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


An integer representing the port on which the member is
hosted. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L50">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L55">property tenantId</a>
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
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L60">property weight</a>
</h3>

```typescript
public weight: pulumi.Output<number>;
```


The load balancing weight of the member. This is currently unable
to be set through Terraform.

<h2 class="pdoc-module-header" id="Monitor">
<a class="pdoc-member-name" href="/loadbalancer/monitor.ts#L10">class Monitor</a>
</h2>

Manages a V2 monitor resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L87">constructor</a>
</h3>

```typescript
new Monitor(name: string, args: MonitorArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Monitor resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L31">property delay</a>
</h3>

```typescript
public delay: pulumi.Output<number>;
```


The time, in seconds, between sending probes to members.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L37">property expectedCodes</a>
</h3>

```typescript
public expectedCodes: pulumi.Output<string>;
```


Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L43">property httpMethod</a>
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
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L49">property maxRetries</a>
</h3>

```typescript
public maxRetries: pulumi.Output<number>;
```


Number of permissible ping failures before
changing the member's status to INACTIVE. Must be a number between 1
and 10..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The Name of the Monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L57">property poolId</a>
</h3>

```typescript
public poolId: pulumi.Output<string>;
```


The id of the pool that this monitor will be assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L64">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L70">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L76">property timeout</a>
</h3>

```typescript
public timeout: pulumi.Output<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L82">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the load balancer to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L87">property urlPath</a>
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
<a class="pdoc-member-name" href="/loadbalancer/monitorV1.ts#L10">class MonitorV1</a>
</h2>

Manages a V1 load balancer monitor resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L82">constructor</a>
</h3>

```typescript
new MonitorV1(name: string, args: MonitorV1Args, opts?: pulumi.CustomResourceOptions)
```


Create a MonitorV1 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L28">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<string>;
```


The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L33">property delay</a>
</h3>

```typescript
public delay: pulumi.Output<number>;
```


The time, in seconds, between sending probes to members.
Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L40">property expectedCodes</a>
</h3>

```typescript
public expectedCodes: pulumi.Output<string | undefined>;
```


equired for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L46">property httpMethod</a>
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
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L52">property maxRetries</a>
</h3>

```typescript
public maxRetries: pulumi.Output<number>;
```


Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L59">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L64">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L70">property timeout</a>
</h3>

```typescript
public timeout: pulumi.Output<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L76">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L82">property urlPath</a>
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
<a class="pdoc-member-name" href="/loadbalancer/pool.ts#L10">class Pool</a>
</h2>

Manages a V2 pool resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L76">constructor</a>
</h3>

```typescript
new Pool(name: string, args: PoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Pool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


The administrative state of the pool.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L31">property description</a>
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
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L37">property lbMethod</a>
</h3>

```typescript
public lbMethod: pulumi.Output<string>;
```


The load balancing algorithm to
distribute traffic to the pool's members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L43">property listenerId</a>
</h3>

```typescript
public listenerId: pulumi.Output<string | undefined>;
```


The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L49">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string | undefined>;
```


The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Human-readable name for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L59">property persistences</a>
</h3>

```typescript
public persistences: pulumi.Output<{ ... }[] | undefined>;
```


Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L63">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L70">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L76">property tenantId</a>
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
<a class="pdoc-member-name" href="/loadbalancer/poolV1.ts#L10">class PoolV1</a>
</h2>

Manages a V1 load balancer pool resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L66">constructor</a>
</h3>

```typescript
new PoolV1(name: string, args: PoolV1Args, opts?: pulumi.CustomResourceOptions)
```


Create a PoolV1 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L28">property lbMethod</a>
</h3>

```typescript
public lbMethod: pulumi.Output<string>;
```


The algorithm used to distribute load between the
members of the pool. The current specification supports 'ROUND_ROBIN' and
'LEAST_CONNECTIONS' as valid values for this attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L33">property lbProvider</a>
</h3>

```typescript
public lbProvider: pulumi.Output<string>;
```


The backend load balancing provider. For example:
`haproxy`, `F5`, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L38">property monitorIds</a>
</h3>

```typescript
public monitorIds: pulumi.Output<string[] | undefined>;
```


A list of IDs of monitors to associate with the
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the pool. Changing this updates the name of
the existing pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L48">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol used by the pool members, you can use
either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L55">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L61">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L66">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the pool. Required if admin wants to
create a pool member for another tenant. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Vip">
<a class="pdoc-member-name" href="/loadbalancer/vip.ts#L10">class Vip</a>
</h2>

Manages a V1 load balancer vip resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L98">constructor</a>
</h3>

```typescript
new Vip(name: string, args: VipArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Vip resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L27">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The IP address of the vip. Changing this creates a new
vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L33">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean>;
```


The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L39">property connLimit</a>
</h3>

```typescript
public connLimit: pulumi.Output<number>;
```


The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L44">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


Human-readable description for the vip. Changing
this updates the description of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L49">property floatingIp</a>
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
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the vip. Changing this updates the name of
the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L60">property persistence</a>
</h3>

```typescript
public persistence: pulumi.Output<{ ... } | undefined>;
```


Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L65">property poolId</a>
</h3>

```typescript
public poolId: pulumi.Output<string>;
```


The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L70">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The port on which to listen for client traffic. Changing
this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L74">property portId</a>
</h3>

```typescript
public portId: pulumi.Output<string>;
```


Port UUID for this VIP at associated floating IP (if any).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L79">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L86">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L93">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L98">property tenantId</a>
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
<a class="pdoc-member-name" href="/loadbalancer/listener.ts#L219">interface ListenerArgs</a>
</h2>

The set of arguments for constructing a Listener resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L224">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L229">property connectionLimit</a>
</h3>

```typescript
connectionLimit?: pulumi.Input<number>;
```


The maximum number of connections allowed
for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L234">property defaultPoolId</a>
</h3>

```typescript
defaultPoolId?: pulumi.Input<string>;
```


The ID of the default pool with which the
Listener is associated. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L242">property defaultTlsContainerRef</a>
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
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L246">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L251">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The load balancer on which to provision this
Listener. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L256">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the Listener. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L261">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol - can either be TCP, HTTP, HTTPS or TERMINATED_HTTPS.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L266">property protocolPort</a>
</h3>

```typescript
protocolPort: pulumi.Input<number>;
```


The port on which to listen for client traffic.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L273">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L280">property sniContainerRefs</a>
</h3>

```typescript
sniContainerRefs?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L286">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.

<h2 class="pdoc-module-header" id="ListenerState">
<a class="pdoc-member-name" href="/loadbalancer/listener.ts#L146">interface ListenerState</a>
</h2>

Input properties used for looking up and filtering Listener resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L151">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L156">property connectionLimit</a>
</h3>

```typescript
connectionLimit?: pulumi.Input<number>;
```


The maximum number of connections allowed
for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L161">property defaultPoolId</a>
</h3>

```typescript
defaultPoolId?: pulumi.Input<string>;
```


The ID of the default pool with which the
Listener is associated. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L169">property defaultTlsContainerRef</a>
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
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L173">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L178">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The load balancer on which to provision this
Listener. Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L183">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the Listener. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L188">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol - can either be TCP, HTTP, HTTPS or TERMINATED_HTTPS.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L193">property protocolPort</a>
</h3>

```typescript
protocolPort?: pulumi.Input<number>;
```


The port on which to listen for client traffic.
Changing this creates a new Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L200">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L207">property sniContainerRefs</a>
</h3>

```typescript
sniContainerRefs?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/listener.ts#L213">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.

<h2 class="pdoc-module-header" id="LoadBalancerArgs">
<a class="pdoc-member-name" href="/loadbalancer/loadBalancer.ts#L195">interface LoadBalancerArgs</a>
</h2>

The set of arguments for constructing a LoadBalancer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L200">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L204">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the Loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L209">property flavor</a>
</h3>

```typescript
flavor?: pulumi.Input<string>;
```


The UUID of a flavor. Changing this creates a new
loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L214">property loadbalancerProvider</a>
</h3>

```typescript
loadbalancerProvider?: pulumi.Input<string>;
```


The name of the provider. Changing this
creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L219">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the Loadbalancer. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L226">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L232">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L238">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the Loadbalancer.  Only administrative users can specify a tenant UUID
other than their own.  Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L243">property vipAddress</a>
</h3>

```typescript
vipAddress?: pulumi.Input<string>;
```


The ip address of the load balancer.
Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L250">property vipSubnetId</a>
</h3>

```typescript
vipSubnetId: pulumi.Input<string>;
```


The network on which to allocate the
Loadbalancer's address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.

<h2 class="pdoc-module-header" id="LoadBalancerState">
<a class="pdoc-member-name" href="/loadbalancer/loadBalancer.ts#L130">interface LoadBalancerState</a>
</h2>

Input properties used for looking up and filtering LoadBalancer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L135">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L139">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the Loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L144">property flavor</a>
</h3>

```typescript
flavor?: pulumi.Input<string>;
```


The UUID of a flavor. Changing this creates a new
loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L149">property loadbalancerProvider</a>
</h3>

```typescript
loadbalancerProvider?: pulumi.Input<string>;
```


The name of the provider. Changing this
creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L154">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the Loadbalancer. Does not have
to be unique.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L161">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L167">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L173">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the Loadbalancer.  Only administrative users can specify a tenant UUID
other than their own.  Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L178">property vipAddress</a>
</h3>

```typescript
vipAddress?: pulumi.Input<string>;
```


The ip address of the load balancer.
Changing this creates a new loadbalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L182">property vipPortId</a>
</h3>

```typescript
vipPortId?: pulumi.Input<string>;
```


The Port ID of the Load Balancer IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/loadBalancer.ts#L189">property vipSubnetId</a>
</h3>

```typescript
vipSubnetId?: pulumi.Input<string>;
```


The network on which to allocate the
Loadbalancer's address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.

<h2 class="pdoc-module-header" id="MemberArgs">
<a class="pdoc-member-name" href="/loadbalancer/member.ts#L175">interface MemberArgs</a>
</h2>

The set of arguments for constructing a Member resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L180">property address</a>
</h3>

```typescript
address: pulumi.Input<string>;
```


The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L185">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the member.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L189">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L194">property poolId</a>
</h3>

```typescript
poolId: pulumi.Input<string>;
```


The id of the pool that this member will be
assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L199">property protocolPort</a>
</h3>

```typescript
protocolPort: pulumi.Input<number>;
```


The port on which to listen for client traffic.
Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L206">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L210">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The subnet in which to access the member

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L216">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the member.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L223">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.

<h2 class="pdoc-module-header" id="MemberState">
<a class="pdoc-member-name" href="/loadbalancer/member.ts#L121">interface MemberState</a>
</h2>

Input properties used for looking up and filtering Member resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L126">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L131">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the member.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L140">property poolId</a>
</h3>

```typescript
poolId?: pulumi.Input<string>;
```


The id of the pool that this member will be
assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L145">property protocolPort</a>
</h3>

```typescript
protocolPort?: pulumi.Input<number>;
```


The port on which to listen for client traffic.
Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L152">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L156">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The subnet in which to access the member

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L162">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the member.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/member.ts#L169">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.

<h2 class="pdoc-module-header" id="MemberV1Args">
<a class="pdoc-member-name" href="/loadbalancer/memberV1.ts#L151">interface MemberV1Args</a>
</h2>

The set of arguments for constructing a MemberV1 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L156">property address</a>
</h3>

```typescript
address: pulumi.Input<string>;
```


The IP address of the member. Changing this creates a
new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L162">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the member.
Acceptable values are 'true' and 'false'. Changing this value updates the
state of the existing member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L167">property poolId</a>
</h3>

```typescript
poolId: pulumi.Input<string>;
```


The ID of the LB pool. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L172">property port</a>
</h3>

```typescript
port: pulumi.Input<number>;
```


An integer representing the port on which the member is
hosted. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L179">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L184">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the member. Required if admin wants to
create a member for another tenant. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L189">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


The load balancing weight of the member. This is currently unable
to be set through Terraform.

<h2 class="pdoc-module-header" id="MemberV1State">
<a class="pdoc-member-name" href="/loadbalancer/memberV1.ts#L107">interface MemberV1State</a>
</h2>

Input properties used for looking up and filtering MemberV1 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L112">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address of the member. Changing this creates a
new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L118">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the member.
Acceptable values are 'true' and 'false'. Changing this value updates the
state of the existing member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L123">property poolId</a>
</h3>

```typescript
poolId?: pulumi.Input<string>;
```


The ID of the LB pool. Changing this creates a new
member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L128">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


An integer representing the port on which the member is
hosted. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L135">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L140">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the member. Required if admin wants to
create a member for another tenant. Changing this creates a new member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/memberV1.ts#L145">property weight</a>
</h3>

```typescript
weight?: pulumi.Input<number>;
```


The load balancing weight of the member. This is currently unable
to be set through Terraform.

<h2 class="pdoc-module-header" id="MonitorArgs">
<a class="pdoc-member-name" href="/loadbalancer/monitor.ts#L221">interface MonitorArgs</a>
</h2>

The set of arguments for constructing a Monitor resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L226">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L230">property delay</a>
</h3>

```typescript
delay: pulumi.Input<number>;
```


The time, in seconds, between sending probes to members.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L236">property expectedCodes</a>
</h3>

```typescript
expectedCodes?: pulumi.Input<string>;
```


Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L242">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it
defaults to "GET".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L248">property maxRetries</a>
</h3>

```typescript
maxRetries: pulumi.Input<number>;
```


Number of permissible ping failures before
changing the member's status to INACTIVE. Must be a number between 1
and 10..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L252">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the Monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L256">property poolId</a>
</h3>

```typescript
poolId: pulumi.Input<string>;
```


The id of the pool that this monitor will be assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L263">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L269">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L275">property timeout</a>
</h3>

```typescript
timeout: pulumi.Input<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L281">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the load balancer to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L286">property urlPath</a>
</h3>

```typescript
urlPath?: pulumi.Input<string>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS.

<h2 class="pdoc-module-header" id="MonitorState">
<a class="pdoc-member-name" href="/loadbalancer/monitor.ts#L150">interface MonitorState</a>
</h2>

Input properties used for looking up and filtering Monitor resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L155">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L159">property delay</a>
</h3>

```typescript
delay?: pulumi.Input<number>;
```


The time, in seconds, between sending probes to members.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L165">property expectedCodes</a>
</h3>

```typescript
expectedCodes?: pulumi.Input<string>;
```


Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L171">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it
defaults to "GET".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L177">property maxRetries</a>
</h3>

```typescript
maxRetries?: pulumi.Input<number>;
```


Number of permissible ping failures before
changing the member's status to INACTIVE. Must be a number between 1
and 10..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L181">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the Monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L185">property poolId</a>
</h3>

```typescript
poolId?: pulumi.Input<string>;
```


The id of the pool that this monitor will be assigned to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L192">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L198">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L204">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L210">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the load balancer to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitor.ts#L215">property urlPath</a>
</h3>

```typescript
urlPath?: pulumi.Input<string>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS.

<h2 class="pdoc-module-header" id="MonitorV1Args">
<a class="pdoc-member-name" href="/loadbalancer/monitorV1.ts#L204">interface MonitorV1Args</a>
</h2>

The set of arguments for constructing a MonitorV1 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L210">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<string>;
```


The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L215">property delay</a>
</h3>

```typescript
delay: pulumi.Input<number>;
```


The time, in seconds, between sending probes to members.
Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L222">property expectedCodes</a>
</h3>

```typescript
expectedCodes?: pulumi.Input<string>;
```


equired for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L228">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L234">property maxRetries</a>
</h3>

```typescript
maxRetries: pulumi.Input<number>;
```


Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L241">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L246">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L252">property timeout</a>
</h3>

```typescript
timeout: pulumi.Input<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L258">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L264">property urlPath</a>
</h3>

```typescript
urlPath?: pulumi.Input<string>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.

<h2 class="pdoc-module-header" id="MonitorV1State">
<a class="pdoc-member-name" href="/loadbalancer/monitorV1.ts#L138">interface MonitorV1State</a>
</h2>

Input properties used for looking up and filtering MonitorV1 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L144">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<string>;
```


The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L149">property delay</a>
</h3>

```typescript
delay?: pulumi.Input<number>;
```


The time, in seconds, between sending probes to members.
Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L156">property expectedCodes</a>
</h3>

```typescript
expectedCodes?: pulumi.Input<string>;
```


equired for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L162">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L168">property maxRetries</a>
</h3>

```typescript
maxRetries?: pulumi.Input<number>;
```


Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L175">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L180">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L186">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L192">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/monitorV1.ts#L198">property urlPath</a>
</h3>

```typescript
urlPath?: pulumi.Input<string>;
```


Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.

<h2 class="pdoc-module-header" id="PoolArgs">
<a class="pdoc-member-name" href="/loadbalancer/pool.ts#L186">interface PoolArgs</a>
</h2>

The set of arguments for constructing a Pool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L191">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the pool.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L195">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L201">property lbMethod</a>
</h3>

```typescript
lbMethod: pulumi.Input<string>;
```


The load balancing algorithm to
distribute traffic to the pool's members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L207">property listenerId</a>
</h3>

```typescript
listenerId?: pulumi.Input<string>;
```


The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L213">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L217">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L223">property persistences</a>
</h3>

```typescript
persistences?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L227">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L234">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L240">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the pool.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new pool.

<h2 class="pdoc-module-header" id="PoolState">
<a class="pdoc-member-name" href="/loadbalancer/pool.ts#L126">interface PoolState</a>
</h2>

Input properties used for looking up and filtering Pool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L131">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the pool.
A valid value is true (UP) or false (DOWN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L135">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L141">property lbMethod</a>
</h3>

```typescript
lbMethod?: pulumi.Input<string>;
```


The load balancing algorithm to
distribute traffic to the pool's members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L147">property listenerId</a>
</h3>

```typescript
listenerId?: pulumi.Input<string>;
```


The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L153">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L157">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human-readable name for the pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L163">property persistences</a>
</h3>

```typescript
persistences?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L167">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L174">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/pool.ts#L180">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


Required for admins. The UUID of the tenant who owns
the pool.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new pool.

<h2 class="pdoc-module-header" id="PoolV1Args">
<a class="pdoc-member-name" href="/loadbalancer/poolV1.ts#L165">interface PoolV1Args</a>
</h2>

The set of arguments for constructing a PoolV1 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L171">property lbMethod</a>
</h3>

```typescript
lbMethod: pulumi.Input<string>;
```


The algorithm used to distribute load between the
members of the pool. The current specification supports 'ROUND_ROBIN' and
'LEAST_CONNECTIONS' as valid values for this attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L176">property lbProvider</a>
</h3>

```typescript
lbProvider?: pulumi.Input<string>;
```


The backend load balancing provider. For example:
`haproxy`, `F5`, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L181">property monitorIds</a>
</h3>

```typescript
monitorIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IDs of monitors to associate with the
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L186">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the pool. Changing this updates the name of
the existing pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L191">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol used by the pool members, you can use
either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L198">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L204">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L209">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the pool. Required if admin wants to
create a pool member for another tenant. Changing this creates a new pool.

<h2 class="pdoc-module-header" id="PoolV1State">
<a class="pdoc-member-name" href="/loadbalancer/poolV1.ts#L115">interface PoolV1State</a>
</h2>

Input properties used for looking up and filtering PoolV1 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L121">property lbMethod</a>
</h3>

```typescript
lbMethod?: pulumi.Input<string>;
```


The algorithm used to distribute load between the
members of the pool. The current specification supports 'ROUND_ROBIN' and
'LEAST_CONNECTIONS' as valid values for this attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L126">property lbProvider</a>
</h3>

```typescript
lbProvider?: pulumi.Input<string>;
```


The backend load balancing provider. For example:
`haproxy`, `F5`, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L131">property monitorIds</a>
</h3>

```typescript
monitorIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IDs of monitors to associate with the
pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the pool. Changing this updates the name of
the existing pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L141">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol used by the pool members, you can use
either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L148">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L154">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/poolV1.ts#L159">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the pool. Required if admin wants to
create a pool member for another tenant. Changing this creates a new pool.

<h2 class="pdoc-module-header" id="VipArgs">
<a class="pdoc-member-name" href="/loadbalancer/vip.ts#L244">interface VipArgs</a>
</h2>

The set of arguments for constructing a Vip resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L249">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address of the vip. Changing this creates a new
vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L255">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L261">property connLimit</a>
</h3>

```typescript
connLimit?: pulumi.Input<number>;
```


The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L266">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the vip. Changing
this updates the description of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L271">property floatingIp</a>
</h3>

```typescript
floatingIp?: pulumi.Input<string>;
```


A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L276">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the vip. Changing this updates the name of
the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L282">property persistence</a>
</h3>

```typescript
persistence?: pulumi.Input<{ ... }>;
```


Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L287">property poolId</a>
</h3>

```typescript
poolId: pulumi.Input<string>;
```


The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L292">property port</a>
</h3>

```typescript
port: pulumi.Input<number>;
```


The port on which to listen for client traffic. Changing
this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L297">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L304">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L311">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L316">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.

<h2 class="pdoc-module-header" id="VipState">
<a class="pdoc-member-name" href="/loadbalancer/vip.ts#L162">interface VipState</a>
</h2>

Input properties used for looking up and filtering Vip resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L167">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address of the vip. Changing this creates a new
vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L173">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L179">property connLimit</a>
</h3>

```typescript
connLimit?: pulumi.Input<number>;
```


The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L184">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description for the vip. Changing
this updates the description of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L189">property floatingIp</a>
</h3>

```typescript
floatingIp?: pulumi.Input<string>;
```


A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L194">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the vip. Changing this updates the name of
the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L200">property persistence</a>
</h3>

```typescript
persistence?: pulumi.Input<{ ... }>;
```


Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L205">property poolId</a>
</h3>

```typescript
poolId?: pulumi.Input<string>;
```


The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L210">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which to listen for client traffic. Changing
this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L214">property portId</a>
</h3>

```typescript
portId?: pulumi.Input<string>;
```


Port UUID for this VIP at associated floating IP (if any).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L219">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L226">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L233">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/loadbalancer/vip.ts#L238">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.

