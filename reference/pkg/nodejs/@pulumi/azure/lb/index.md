---
title: Module lb
---

<a href="../index.html">@pulumi/azure</a> &gt; lb

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

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts">lb/backendAddressPool.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts">lb/loadBalancer.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts">lb/natPool.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts">lb/natRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts">lb/probe.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts">lb/rule.ts</a> 


<h2 class="pdoc-module-header" id="BackendAddressPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L12">class BackendAddressPool</a>
</h2>

Manage a Load Balancer Backend Address Pool.

~> **NOTE:** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L39">constructor</a>
</h3>

```typescript
new BackendAddressPool(name: string, args: BackendAddressPoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a BackendAddressPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BackendAddressPoolState): BackendAddressPool
```


Get an existing BackendAddressPool resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L25">property backendIpConfigurations</a>
</h3>

```typescript
public backendIpConfigurations: pulumi.Output<string[]>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L26">property loadBalancingRules</a>
</h3>

```typescript
public loadBalancingRules: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L30">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the Load Balancer in which to create the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L31">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L39">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LoadBalancer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L10">class LoadBalancer</a>
</h2>

Manage a Load Balancer Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L54">constructor</a>
</h3>

```typescript
new LoadBalancer(name: string, args: LoadBalancerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LoadBalancer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerState): LoadBalancer
```


Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L26">property frontendIpConfigurations</a>
</h3>

```typescript
public frontendIpConfigurations: pulumi.Output<{ ... }[] | undefined>;
```


A frontend ip configuration block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the frontend ip configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L38">property privateIpAddress</a>
</h3>

```typescript
public privateIpAddress: pulumi.Output<string>;
```


Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L42">property privateIpAddresses</a>
</h3>

```typescript
public privateIpAddresses: pulumi.Output<string[]>;
```


The list of private IP address assigned to the load balancer in `frontend_ip_configuration` blocks, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L46">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the LoadBalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L50">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string | undefined>;
```


The SKU of the Azure Load Balancer. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L54">property tags</a>
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

<h2 class="pdoc-module-header" id="NatPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L12">class NatPool</a>
</h2>

Manages a Load Balancer NAT pool.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L58">constructor</a>
</h3>

```typescript
new NatPool(name: string, args: NatPoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NatPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NatPoolState): NatPool
```


Get an existing NatPool resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L28">property backendPort</a>
</h3>

```typescript
public backendPort: pulumi.Output<number>;
```


The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L29">property frontendIpConfigurationId</a>
</h3>

```typescript
public frontendIpConfigurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L33">property frontendIpConfigurationName</a>
</h3>

```typescript
public frontendIpConfigurationName: pulumi.Output<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L37">property frontendPortEnd</a>
</h3>

```typescript
public frontendPortEnd: pulumi.Output<number>;
```


The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L41">property frontendPortStart</a>
</h3>

```typescript
public frontendPortStart: pulumi.Output<number>;
```


The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L45">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the Load Balancer in which to create the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L46">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L54">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L58">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NatRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L12">class NatRule</a>
</h2>

Manages a Load Balancer NAT Rule.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L59">constructor</a>
</h3>

```typescript
new NatRule(name: string, args: NatRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NatRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NatRuleState): NatRule
```


Get an existing NatRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L25">property backendIpConfigurationId</a>
</h3>

```typescript
public backendIpConfigurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L29">property backendPort</a>
</h3>

```typescript
public backendPort: pulumi.Output<number>;
```


The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L33">property enableFloatingIp</a>
</h3>

```typescript
public enableFloatingIp: pulumi.Output<boolean>;
```


Enables the Floating IP Capacity, required to configure a SQL AlwaysOn Availability Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L34">property frontendIpConfigurationId</a>
</h3>

```typescript
public frontendIpConfigurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L38">property frontendIpConfigurationName</a>
</h3>

```typescript
public frontendIpConfigurationName: pulumi.Output<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L42">property frontendPort</a>
</h3>

```typescript
public frontendPort: pulumi.Output<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L46">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the Load Balancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L47">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L55">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp`, `Tcp` or `All`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L59">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Probe">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L12">class Probe</a>
</h2>

Manages a LoadBalancer Probe Resource.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L58">constructor</a>
</h3>

```typescript
new Probe(name: string, args: ProbeArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Probe resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProbeState): Probe
```


Get an existing Probe resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L28">property intervalInSeconds</a>
</h3>

```typescript
public intervalInSeconds: pulumi.Output<number | undefined>;
```


The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L29">property loadBalancerRules</a>
</h3>

```typescript
public loadBalancerRules: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L33">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the LoadBalancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L34">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Probe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L42">property numberOfProbes</a>
</h3>

```typescript
public numberOfProbes: pulumi.Output<number | undefined>;
```


The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L46">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L50">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


Specifies the protocol of the end point. Possible values are `Http`, `Https` or `Tcp`. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L54">property requestPath</a>
</h3>

```typescript
public requestPath: pulumi.Output<string | undefined>;
```


The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L58">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Rule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L12">class Rule</a>
</h2>

Manages a Load Balancer Rule.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L74">constructor</a>
</h3>

```typescript
new Rule(name: string, args: RuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Rule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RuleState): Rule
```


Get an existing Rule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L28">property backendAddressPoolId</a>
</h3>

```typescript
public backendAddressPoolId: pulumi.Output<string>;
```


A reference to a Backend Address Pool over which this Load Balancing Rule operates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L32">property backendPort</a>
</h3>

```typescript
public backendPort: pulumi.Output<number>;
```


The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L36">property enableFloatingIp</a>
</h3>

```typescript
public enableFloatingIp: pulumi.Output<boolean | undefined>;
```


Floating IP is pertinent to failover scenarios: a "floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L37">property frontendIpConfigurationId</a>
</h3>

```typescript
public frontendIpConfigurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L41">property frontendIpConfigurationName</a>
</h3>

```typescript
public frontendIpConfigurationName: pulumi.Output<string>;
```


The name of the frontend IP configuration to which the rule is associated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L45">property frontendPort</a>
</h3>

```typescript
public frontendPort: pulumi.Output<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L49">property idleTimeoutInMinutes</a>
</h3>

```typescript
public idleTimeoutInMinutes: pulumi.Output<number>;
```


Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L53">property loadDistribution</a>
</h3>

```typescript
public loadDistribution: pulumi.Output<string>;
```


Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: `Default` – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. `SourceIP` – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. `SourceIPProtocol` – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called `None`, `Client IP` and `Client IP and Protocol` respectively.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L57">property loadbalancerId</a>
</h3>

```typescript
public loadbalancerId: pulumi.Output<string>;
```


The ID of the Load Balancer in which to create the Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L58">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L62">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the LB Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L66">property probeId</a>
</h3>

```typescript
public probeId: pulumi.Output<string>;
```


A reference to a Probe used by this Load Balancing Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L70">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The transport protocol for the external endpoint. Possible values are `Tcp`, `Udp` or `All`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L74">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BackendAddressPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L102">interface BackendAddressPoolArgs</a>
</h2>

The set of arguments for constructing a BackendAddressPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L106">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the Load Balancer in which to create the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L107">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L115">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="BackendAddressPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L81">interface BackendAddressPoolState</a>
</h2>

Input properties used for looking up and filtering BackendAddressPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L82">property backendIpConfigurations</a>
</h3>

```typescript
backendIpConfigurations?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L83">property loadBalancingRules</a>
</h3>

```typescript
loadBalancingRules?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L87">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the Load Balancer in which to create the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L88">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L92">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/backendAddressPool.ts#L96">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="LoadBalancerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L138">interface LoadBalancerArgs</a>
</h2>

The set of arguments for constructing a LoadBalancer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L142">property frontendIpConfigurations</a>
</h3>

```typescript
frontendIpConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A frontend ip configuration block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L146">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the frontend ip configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L154">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the LoadBalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L158">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU of the Azure Load Balancer. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L162">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LoadBalancerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L100">interface LoadBalancerState</a>
</h2>

Input properties used for looking up and filtering LoadBalancer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L104">property frontendIpConfigurations</a>
</h3>

```typescript
frontendIpConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A frontend ip configuration block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L108">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the frontend ip configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L116">property privateIpAddress</a>
</h3>

```typescript
privateIpAddress?: pulumi.Input<string>;
```


Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L120">property privateIpAddresses</a>
</h3>

```typescript
privateIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of private IP address assigned to the load balancer in `frontend_ip_configuration` blocks, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L124">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the LoadBalancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L128">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU of the Azure Load Balancer. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/loadBalancer.ts#L132">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NatPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L163">interface NatPoolArgs</a>
</h2>

The set of arguments for constructing a NatPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L167">property backendPort</a>
</h3>

```typescript
backendPort: pulumi.Input<number>;
```


The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L171">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName: pulumi.Input<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L175">property frontendPortEnd</a>
</h3>

```typescript
frontendPortEnd: pulumi.Input<number>;
```


The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L179">property frontendPortStart</a>
</h3>

```typescript
frontendPortStart: pulumi.Input<number>;
```


The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L183">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the Load Balancer in which to create the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L184">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L188">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L192">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L196">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="NatPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L123">interface NatPoolState</a>
</h2>

Input properties used for looking up and filtering NatPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L127">property backendPort</a>
</h3>

```typescript
backendPort?: pulumi.Input<number>;
```


The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L128">property frontendIpConfigurationId</a>
</h3>

```typescript
frontendIpConfigurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L132">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName?: pulumi.Input<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L136">property frontendPortEnd</a>
</h3>

```typescript
frontendPortEnd?: pulumi.Input<number>;
```


The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L140">property frontendPortStart</a>
</h3>

```typescript
frontendPortStart?: pulumi.Input<number>;
```


The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L144">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the Load Balancer in which to create the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L145">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L149">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the NAT pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L153">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natPool.ts#L157">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="NatRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L164">interface NatRuleArgs</a>
</h2>

The set of arguments for constructing a NatRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L168">property backendPort</a>
</h3>

```typescript
backendPort: pulumi.Input<number>;
```


The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L172">property enableFloatingIp</a>
</h3>

```typescript
enableFloatingIp?: pulumi.Input<boolean>;
```


Enables the Floating IP Capacity, required to configure a SQL AlwaysOn Availability Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L176">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName: pulumi.Input<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L180">property frontendPort</a>
</h3>

```typescript
frontendPort: pulumi.Input<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L184">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the Load Balancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L185">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L189">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L193">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp`, `Tcp` or `All`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L197">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="NatRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L123">interface NatRuleState</a>
</h2>

Input properties used for looking up and filtering NatRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L124">property backendIpConfigurationId</a>
</h3>

```typescript
backendIpConfigurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L128">property backendPort</a>
</h3>

```typescript
backendPort?: pulumi.Input<number>;
```


The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L132">property enableFloatingIp</a>
</h3>

```typescript
enableFloatingIp?: pulumi.Input<boolean>;
```


Enables the Floating IP Capacity, required to configure a SQL AlwaysOn Availability Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L133">property frontendIpConfigurationId</a>
</h3>

```typescript
frontendIpConfigurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L137">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName?: pulumi.Input<string>;
```


The name of the frontend IP configuration exposing this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L141">property frontendPort</a>
</h3>

```typescript
frontendPort?: pulumi.Input<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L145">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the Load Balancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L146">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L154">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Udp`, `Tcp` or `All`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/natRule.ts#L158">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="ProbeArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L151">interface ProbeArgs</a>
</h2>

The set of arguments for constructing a Probe resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L155">property intervalInSeconds</a>
</h3>

```typescript
intervalInSeconds?: pulumi.Input<number>;
```


The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L159">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L160">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L164">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Probe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L168">property numberOfProbes</a>
</h3>

```typescript
numberOfProbes?: pulumi.Input<number>;
```


The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L172">property port</a>
</h3>

```typescript
port: pulumi.Input<number>;
```


Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L176">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


Specifies the protocol of the end point. Possible values are `Http`, `Https` or `Tcp`. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L180">property requestPath</a>
</h3>

```typescript
requestPath?: pulumi.Input<string>;
```


The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L184">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="ProbeState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L111">interface ProbeState</a>
</h2>

Input properties used for looking up and filtering Probe resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L115">property intervalInSeconds</a>
</h3>

```typescript
intervalInSeconds?: pulumi.Input<number>;
```


The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L116">property loadBalancerRules</a>
</h3>

```typescript
loadBalancerRules?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L120">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the LoadBalancer in which to create the NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L121">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Probe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L129">property numberOfProbes</a>
</h3>

```typescript
numberOfProbes?: pulumi.Input<number>;
```


The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L133">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L137">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


Specifies the protocol of the end point. Possible values are `Http`, `Https` or `Tcp`. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L141">property requestPath</a>
</h3>

```typescript
requestPath?: pulumi.Input<string>;
```


The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/probe.ts#L145">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="RuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L200">interface RuleArgs</a>
</h2>

The set of arguments for constructing a Rule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L204">property backendAddressPoolId</a>
</h3>

```typescript
backendAddressPoolId?: pulumi.Input<string>;
```


A reference to a Backend Address Pool over which this Load Balancing Rule operates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L208">property backendPort</a>
</h3>

```typescript
backendPort: pulumi.Input<number>;
```


The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L212">property enableFloatingIp</a>
</h3>

```typescript
enableFloatingIp?: pulumi.Input<boolean>;
```


Floating IP is pertinent to failover scenarios: a "floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L216">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName: pulumi.Input<string>;
```


The name of the frontend IP configuration to which the rule is associated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L220">property frontendPort</a>
</h3>

```typescript
frontendPort: pulumi.Input<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L224">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes?: pulumi.Input<number>;
```


Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L228">property loadDistribution</a>
</h3>

```typescript
loadDistribution?: pulumi.Input<string>;
```


Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: `Default` – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. `SourceIP` – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. `SourceIPProtocol` – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called `None`, `Client IP` and `Client IP and Protocol` respectively.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L232">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId: pulumi.Input<string>;
```


The ID of the Load Balancer in which to create the Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L233">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L237">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the LB Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L241">property probeId</a>
</h3>

```typescript
probeId?: pulumi.Input<string>;
```


A reference to a Probe used by this Load Balancing Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L245">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Tcp`, `Udp` or `All`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L249">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

<h2 class="pdoc-module-header" id="RuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L144">interface RuleState</a>
</h2>

Input properties used for looking up and filtering Rule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L148">property backendAddressPoolId</a>
</h3>

```typescript
backendAddressPoolId?: pulumi.Input<string>;
```


A reference to a Backend Address Pool over which this Load Balancing Rule operates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L152">property backendPort</a>
</h3>

```typescript
backendPort?: pulumi.Input<number>;
```


The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L156">property enableFloatingIp</a>
</h3>

```typescript
enableFloatingIp?: pulumi.Input<boolean>;
```


Floating IP is pertinent to failover scenarios: a "floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L157">property frontendIpConfigurationId</a>
</h3>

```typescript
frontendIpConfigurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L161">property frontendIpConfigurationName</a>
</h3>

```typescript
frontendIpConfigurationName?: pulumi.Input<string>;
```


The name of the frontend IP configuration to which the rule is associated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L165">property frontendPort</a>
</h3>

```typescript
frontendPort?: pulumi.Input<number>;
```


The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L169">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes?: pulumi.Input<number>;
```


Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L173">property loadDistribution</a>
</h3>

```typescript
loadDistribution?: pulumi.Input<string>;
```


Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: `Default` – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. `SourceIP` – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. `SourceIPProtocol` – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called `None`, `Client IP` and `Client IP and Protocol` respectively.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L177">property loadbalancerId</a>
</h3>

```typescript
loadbalancerId?: pulumi.Input<string>;
```


The ID of the Load Balancer in which to create the Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L178">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L182">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the LB Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L186">property probeId</a>
</h3>

```typescript
probeId?: pulumi.Input<string>;
```


A reference to a Probe used by this Load Balancing Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L190">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The transport protocol for the external endpoint. Possible values are `Tcp`, `Udp` or `All`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/lb/rule.ts#L194">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource.

