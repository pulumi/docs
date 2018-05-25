---
title: Module lb
---

<a href="..">@pulumi/azure</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#BackendAddressPool">class BackendAddressPool</a>
* <a href="#LoadBalancer">class LoadBalancer</a>
* <a href="#NatPool">class NatPool</a>
* <a href="#NatRule">class NatRule</a>
* <a href="#Probe">class Probe</a>
* <a href="#Rule">class Rule</a>
* <a href="#BackendAddressPoolArgs">interface BackendAddressPoolArgs</a>
* <a href="#BackendAddressPoolState">interface BackendAddressPoolState</a>
* <a href="#LoadBalancerArgs">interface LoadBalancerArgs</a>
* <a href="#LoadBalancerState">interface LoadBalancerState</a>
* <a href="#NatPoolArgs">interface NatPoolArgs</a>
* <a href="#NatPoolState">interface NatPoolState</a>
* <a href="#NatRuleArgs">interface NatRuleArgs</a>
* <a href="#NatRuleState">interface NatRuleState</a>
* <a href="#ProbeArgs">interface ProbeArgs</a>
* <a href="#ProbeState">interface ProbeState</a>
* <a href="#RuleArgs">interface RuleArgs</a>
* <a href="#RuleState">interface RuleState</a>

<a href="/lb/backendAddressPool.ts">lb/backendAddressPool.ts</a> <a href="/lb/loadBalancer.ts">lb/loadBalancer.ts</a> <a href="/lb/natPool.ts">lb/natPool.ts</a> <a href="/lb/natRule.ts">lb/natRule.ts</a> <a href="/lb/probe.ts">lb/probe.ts</a> <a href="/lb/rule.ts">lb/rule.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="BackendAddressPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L11">class BackendAddressPool</a>
</h2>

Create a LoadBalancer Backend Address Pool.

~> **NOTE:** When using this resource, the LoadBalancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L38">constructor</a>
</h3>

```typescript
new BackendAddressPool(name: string, args: BackendAddressPoolArgs, opts?: pulumi.ResourceOptions)
```


Create a BackendAddressPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new BackendAddressPool(name: string, state?: BackendAddressPoolState, opts?: pulumi.ResourceOptions)
```


Create a BackendAddressPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BackendAddressPoolState): BackendAddressPool
```


Get an existing BackendAddressPool resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L24">property backendIpConfigurations</a>
</h3>

```typescript
public backendIpConfigurations: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L25">property loadBalancingRules</a>
</h3>

```typescript
public loadBalancingRules: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L29">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the LoadBalancer in which to create the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LoadBalancer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L9">class LoadBalancer</a>
</h2>

Create a LoadBalancer Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L53">constructor</a>
</h3>

```typescript
new LoadBalancer(name: string, args: LoadBalancerArgs, opts?: pulumi.ResourceOptions)
```


Create a LoadBalancer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new LoadBalancer(name: string, state?: LoadBalancerState, opts?: pulumi.ResourceOptions)
```


Create a LoadBalancer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerState): LoadBalancer
```


Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L25">property frontendIpConfigurations</a>
</h3>

```typescript
public frontendIpConfigurations: pulumi.Output<{ ... }[] | undefined>;
```


A frontend ip configuration block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L29">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the frontend ip configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L37">property privateIpAddress</a>
</h3>

```typescript
public privateIpAddress: pulumi.Output<string>;
```


Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L41">property privateIpAddresses</a>
</h3>

```typescript
public privateIpAddresses: pulumi.Output<string[]>;
```


The list of private IP address assigned to the load balancer in `frontend_ip_configuration` blocks, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the LoadBalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L49">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string | undefined>;
```


The SKU of the Azure Load Balancer. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L53">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NatPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L11">class NatPool</a>
</h2>

Create a LoadBalancer NAT pool.

~> **NOTE** When using this resource, the LoadBalancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L57">constructor</a>
</h3>

```typescript
new NatPool(name: string, args: NatPoolArgs, opts?: pulumi.ResourceOptions)
```


Create a NatPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new NatPool(name: string, state?: NatPoolState, opts?: pulumi.ResourceOptions)
```


Create a NatPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NatPoolState): NatPool
```


Get an existing NatPool resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L27">property backendPort</a>
</h3>

```typescript
public backendPort: pulumi.Output<number>;
```


The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L28">property frontendIpConfigurationId</a>
</h3>

```typescript
public frontendIpConfigurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L32">property frontendIpConfigurationName</a>
</h3>

```typescript
public frontendIpConfigurationName: pulumi.Output<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L36">property frontendPortEnd</a>
</h3>

```typescript
public frontendPortEnd: pulumi.Output<number>;
```


The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L40">property frontendPortStart</a>
</h3>

```typescript
public frontendPortStart: pulumi.Output<number>;
```


The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L44">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the LoadBalancer in which to create the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L45">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L53">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L57">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NatRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L11">class NatRule</a>
</h2>

Create a LoadBalancer NAT Rule.

~> **NOTE** When using this resource, the LoadBalancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L58">constructor</a>
</h3>

```typescript
new NatRule(name: string, args: NatRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a NatRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new NatRule(name: string, state?: NatRuleState, opts?: pulumi.ResourceOptions)
```


Create a NatRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NatRuleState): NatRule
```


Get an existing NatRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L24">property backendIpConfigurationId</a>
</h3>

```typescript
public backendIpConfigurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L28">property backendPort</a>
</h3>

```typescript
public backendPort: pulumi.Output<number>;
```


The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L32">property enableFloatingIp</a>
</h3>

```typescript
public enableFloatingIp: pulumi.Output<boolean>;
```


Enables the Floating IP Capacity, required to configure a SQL AlwaysOn Availability Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L33">property frontendIpConfigurationId</a>
</h3>

```typescript
public frontendIpConfigurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L37">property frontendIpConfigurationName</a>
</h3>

```typescript
public frontendIpConfigurationName: pulumi.Output<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L41">property frontendPort</a>
</h3>

```typescript
public frontendPort: pulumi.Output<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L45">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the LoadBalancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L46">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L54">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L58">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Probe">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L11">class Probe</a>
</h2>

Create a LoadBalancer Probe Resource.

~> **NOTE** When using this resource, the LoadBalancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L57">constructor</a>
</h3>

```typescript
new Probe(name: string, args: ProbeArgs, opts?: pulumi.ResourceOptions)
```


Create a Probe resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Probe(name: string, state?: ProbeState, opts?: pulumi.ResourceOptions)
```


Create a Probe resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProbeState): Probe
```


Get an existing Probe resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L27">property intervalInSeconds</a>
</h3>

```typescript
public intervalInSeconds: pulumi.Output<number | undefined>;
```


The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L28">property loadBalancerRules</a>
</h3>

```typescript
public loadBalancerRules: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L32">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the LoadBalancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L33">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Probe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L41">property numberOfProbes</a>
</h3>

```typescript
public numberOfProbes: pulumi.Output<number | undefined>;
```


The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L45">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L49">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


Specifies the protocol of the end point. Possible values are `Http` or `Tcp`. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L53">property requestPath</a>
</h3>

```typescript
public requestPath: pulumi.Output<string | undefined>;
```


The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L57">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Rule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L11">class Rule</a>
</h2>

Create a LoadBalancer Rule.

~> **NOTE** When using this resource, the LoadBalancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L73">constructor</a>
</h3>

```typescript
new Rule(name: string, args: RuleArgs, opts?: pulumi.ResourceOptions)
```


Create a Rule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Rule(name: string, state?: RuleState, opts?: pulumi.ResourceOptions)
```


Create a Rule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RuleState): Rule
```


Get an existing Rule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L27">property backendAddressPoolId</a>
</h3>

```typescript
public backendAddressPoolId: pulumi.Output<string>;
```


A reference to a Backend Address Pool over which this Load Balancing Rule operates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L31">property backendPort</a>
</h3>

```typescript
public backendPort: pulumi.Output<number>;
```


The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L35">property enableFloatingIp</a>
</h3>

```typescript
public enableFloatingIp: pulumi.Output<boolean | undefined>;
```


Floating IP is pertinent to failover scenarios: a "floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L36">property frontendIpConfigurationId</a>
</h3>

```typescript
public frontendIpConfigurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L40">property frontendIpConfigurationName</a>
</h3>

```typescript
public frontendIpConfigurationName: pulumi.Output<string>;
```


The name of the frontend IP configuration to which the rule is associated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L44">property frontendPort</a>
</h3>

```typescript
public frontendPort: pulumi.Output<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L48">property idleTimeoutInMinutes</a>
</h3>

```typescript
public idleTimeoutInMinutes: pulumi.Output<number>;
```


Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L52">property loadDistribution</a>
</h3>

```typescript
public loadDistribution: pulumi.Output<string>;
```


Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: Default – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. SourceIP – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. SourceIPProtocol – The load balancer is configured to use a 3 tuple hash to map traffic to available servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L56">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the LoadBalancer in which to create the Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L57">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the LB Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L65">property probeId</a>
</h3>

```typescript
public probeId: pulumi.Output<string>;
```


A reference to a Probe used by this Load Balancing Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L69">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L73">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BackendAddressPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L103">interface BackendAddressPoolArgs</a>
</h2>

The set of arguments for constructing a BackendAddressPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L107">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L108">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L116">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="BackendAddressPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L82">interface BackendAddressPoolState</a>
</h2>

Input properties used for looking up and filtering BackendAddressPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L83">property backendIpConfigurations</a>
</h3>

```typescript
backendIpConfigurations?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L84">property loadBalancingRules</a>
</h3>

```typescript
loadBalancingRules?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L88">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L89">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/backendAddressPool.ts#L97">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="LoadBalancerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L139">interface LoadBalancerArgs</a>
</h2>

The set of arguments for constructing a LoadBalancer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L143">property frontendIpConfigurations</a>
</h3>

```typescript
frontendIpConfigurations?: pulumi.Input<{ ... }[]>;
```


A frontend ip configuration block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L147">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L151">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the frontend ip configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L155">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the LoadBalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L159">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU of the Azure Load Balancer. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L163">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LoadBalancerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L101">interface LoadBalancerState</a>
</h2>

Input properties used for looking up and filtering LoadBalancer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L105">property frontendIpConfigurations</a>
</h3>

```typescript
frontendIpConfigurations?: pulumi.Input<{ ... }[]>;
```


A frontend ip configuration block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L109">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the frontend ip configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L117">property privateIpAddress</a>
</h3>

```typescript
privateIpAddress?: pulumi.Input<string>;
```


Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L121">property privateIpAddresses</a>
</h3>

```typescript
privateIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of private IP address assigned to the load balancer in `frontend_ip_configuration` blocks, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L125">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the LoadBalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L129">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU of the Azure Load Balancer. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/loadBalancer.ts#L133">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NatPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L164">interface NatPoolArgs</a>
</h2>

The set of arguments for constructing a NatPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L168">property backendPort</a>
</h3>

```typescript
backendPort: pulumi.Input<number>;
```


The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L172">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName: pulumi.Input<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L176">property frontendPortEnd</a>
</h3>

```typescript
frontendPortEnd: pulumi.Input<number>;
```


The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L180">property frontendPortStart</a>
</h3>

```typescript
frontendPortStart: pulumi.Input<number>;
```


The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L184">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L185">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L189">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L193">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L197">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="NatPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L124">interface NatPoolState</a>
</h2>

Input properties used for looking up and filtering NatPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L128">property backendPort</a>
</h3>

```typescript
backendPort?: pulumi.Input<number>;
```


The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L129">property frontendIpConfigurationId</a>
</h3>

```typescript
frontendIpConfigurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L133">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName?: pulumi.Input<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L137">property frontendPortEnd</a>
</h3>

```typescript
frontendPortEnd?: pulumi.Input<number>;
```


The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L141">property frontendPortStart</a>
</h3>

```typescript
frontendPortStart?: pulumi.Input<number>;
```


The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L145">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L146">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L154">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natPool.ts#L158">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="NatRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L165">interface NatRuleArgs</a>
</h2>

The set of arguments for constructing a NatRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L169">property backendPort</a>
</h3>

```typescript
backendPort: pulumi.Input<number>;
```


The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L173">property enableFloatingIp</a>
</h3>

```typescript
enableFloatingIp?: pulumi.Input<boolean>;
```


Enables the Floating IP Capacity, required to configure a SQL AlwaysOn Availability Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L177">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName: pulumi.Input<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L181">property frontendPort</a>
</h3>

```typescript
frontendPort: pulumi.Input<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L185">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L186">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L190">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L194">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L198">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="NatRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L124">interface NatRuleState</a>
</h2>

Input properties used for looking up and filtering NatRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L125">property backendIpConfigurationId</a>
</h3>

```typescript
backendIpConfigurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L129">property backendPort</a>
</h3>

```typescript
backendPort?: pulumi.Input<number>;
```


The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L133">property enableFloatingIp</a>
</h3>

```typescript
enableFloatingIp?: pulumi.Input<boolean>;
```


Enables the Floating IP Capacity, required to configure a SQL AlwaysOn Availability Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L134">property frontendIpConfigurationId</a>
</h3>

```typescript
frontendIpConfigurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L138">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName?: pulumi.Input<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L142">property frontendPort</a>
</h3>

```typescript
frontendPort?: pulumi.Input<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L146">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L147">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L151">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L155">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/natRule.ts#L159">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="ProbeArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L152">interface ProbeArgs</a>
</h2>

The set of arguments for constructing a Probe resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L156">property intervalInSeconds</a>
</h3>

```typescript
intervalInSeconds?: pulumi.Input<number>;
```


The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L160">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L161">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L165">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Probe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L169">property numberOfProbes</a>
</h3>

```typescript
numberOfProbes?: pulumi.Input<number>;
```


The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L173">property port</a>
</h3>

```typescript
port: pulumi.Input<number>;
```


Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L177">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


Specifies the protocol of the end point. Possible values are `Http` or `Tcp`. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L181">property requestPath</a>
</h3>

```typescript
requestPath?: pulumi.Input<string>;
```


The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L185">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="ProbeState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L112">interface ProbeState</a>
</h2>

Input properties used for looking up and filtering Probe resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L116">property intervalInSeconds</a>
</h3>

```typescript
intervalInSeconds?: pulumi.Input<number>;
```


The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L117">property loadBalancerRules</a>
</h3>

```typescript
loadBalancerRules?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L121">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L122">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Probe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L130">property numberOfProbes</a>
</h3>

```typescript
numberOfProbes?: pulumi.Input<number>;
```


The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L134">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L138">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


Specifies the protocol of the end point. Possible values are `Http` or `Tcp`. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L142">property requestPath</a>
</h3>

```typescript
requestPath?: pulumi.Input<string>;
```


The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/probe.ts#L146">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="RuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L201">interface RuleArgs</a>
</h2>

The set of arguments for constructing a Rule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L205">property backendAddressPoolId</a>
</h3>

```typescript
backendAddressPoolId?: pulumi.Input<string>;
```


A reference to a Backend Address Pool over which this Load Balancing Rule operates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L209">property backendPort</a>
</h3>

```typescript
backendPort: pulumi.Input<number>;
```


The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L213">property enableFloatingIp</a>
</h3>

```typescript
enableFloatingIp?: pulumi.Input<boolean>;
```


Floating IP is pertinent to failover scenarios: a "floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L217">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName: pulumi.Input<string>;
```


The name of the frontend IP configuration to which the rule is associated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L221">property frontendPort</a>
</h3>

```typescript
frontendPort: pulumi.Input<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L225">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes?: pulumi.Input<number>;
```


Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L229">property loadDistribution</a>
</h3>

```typescript
loadDistribution?: pulumi.Input<string>;
```


Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: Default – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. SourceIP – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. SourceIPProtocol – The load balancer is configured to use a 3 tuple hash to map traffic to available servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L233">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L234">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L238">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the LB Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L242">property probeId</a>
</h3>

```typescript
probeId?: pulumi.Input<string>;
```


A reference to a Probe used by this Load Balancing Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L246">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L250">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="RuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L145">interface RuleState</a>
</h2>

Input properties used for looking up and filtering Rule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L149">property backendAddressPoolId</a>
</h3>

```typescript
backendAddressPoolId?: pulumi.Input<string>;
```


A reference to a Backend Address Pool over which this Load Balancing Rule operates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L153">property backendPort</a>
</h3>

```typescript
backendPort?: pulumi.Input<number>;
```


The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L157">property enableFloatingIp</a>
</h3>

```typescript
enableFloatingIp?: pulumi.Input<boolean>;
```


Floating IP is pertinent to failover scenarios: a "floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L158">property frontendIpConfigurationId</a>
</h3>

```typescript
frontendIpConfigurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L162">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName?: pulumi.Input<string>;
```


The name of the frontend IP configuration to which the rule is associated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L166">property frontendPort</a>
</h3>

```typescript
frontendPort?: pulumi.Input<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L170">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes?: pulumi.Input<number>;
```


Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L174">property loadDistribution</a>
</h3>

```typescript
loadDistribution?: pulumi.Input<string>;
```


Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: Default – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. SourceIP – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. SourceIPProtocol – The load balancer is configured to use a 3 tuple hash to map traffic to available servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L178">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L179">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L183">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the LB Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L187">property probeId</a>
</h3>

```typescript
probeId?: pulumi.Input<string>;
```


A reference to a Probe used by this Load Balancing Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L191">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/lb/rule.ts#L195">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

