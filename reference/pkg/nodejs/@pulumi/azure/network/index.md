---
title: Module network
---

<a href="../index.html">@pulumi/azure</a> &gt; network

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ApplicationGateway">class ApplicationGateway</a>
* <a href="#ApplicationSecurityGroup">class ApplicationSecurityGroup</a>
* <a href="#ExpressRouteCircuit">class ExpressRouteCircuit</a>
* <a href="#ExpressRouteCircuitAuthorization">class ExpressRouteCircuitAuthorization</a>
* <a href="#ExpressRouteCircuitPeering">class ExpressRouteCircuitPeering</a>
* <a href="#LocalNetworkGateway">class LocalNetworkGateway</a>
* <a href="#NetworkInterface">class NetworkInterface</a>
* <a href="#NetworkSecurityGroup">class NetworkSecurityGroup</a>
* <a href="#NetworkSecurityRule">class NetworkSecurityRule</a>
* <a href="#NetworkWatcher">class NetworkWatcher</a>
* <a href="#PacketCapture">class PacketCapture</a>
* <a href="#PublicIp">class PublicIp</a>
* <a href="#Route">class Route</a>
* <a href="#RouteTable">class RouteTable</a>
* <a href="#Subnet">class Subnet</a>
* <a href="#VirtualNetwork">class VirtualNetwork</a>
* <a href="#VirtualNetworkGateway">class VirtualNetworkGateway</a>
* <a href="#VirtualNetworkGatewayConnection">class VirtualNetworkGatewayConnection</a>
* <a href="#VirtualNetworkPeering">class VirtualNetworkPeering</a>
* <a href="#getApplicationSecurityGroup">function getApplicationSecurityGroup</a>
* <a href="#getNetworkInterface">function getNetworkInterface</a>
* <a href="#getNetworkSecurityGroup">function getNetworkSecurityGroup</a>
* <a href="#getPublicIP">function getPublicIP</a>
* <a href="#getPublicIPs">function getPublicIPs</a>
* <a href="#getRouteTable">function getRouteTable</a>
* <a href="#getSubnet">function getSubnet</a>
* <a href="#getVirtualNetwork">function getVirtualNetwork</a>
* <a href="#getVirtualNetworkGateway">function getVirtualNetworkGateway</a>
* <a href="#ApplicationGatewayArgs">interface ApplicationGatewayArgs</a>
* <a href="#ApplicationGatewayState">interface ApplicationGatewayState</a>
* <a href="#ApplicationSecurityGroupArgs">interface ApplicationSecurityGroupArgs</a>
* <a href="#ApplicationSecurityGroupState">interface ApplicationSecurityGroupState</a>
* <a href="#ExpressRouteCircuitArgs">interface ExpressRouteCircuitArgs</a>
* <a href="#ExpressRouteCircuitAuthorizationArgs">interface ExpressRouteCircuitAuthorizationArgs</a>
* <a href="#ExpressRouteCircuitAuthorizationState">interface ExpressRouteCircuitAuthorizationState</a>
* <a href="#ExpressRouteCircuitPeeringArgs">interface ExpressRouteCircuitPeeringArgs</a>
* <a href="#ExpressRouteCircuitPeeringState">interface ExpressRouteCircuitPeeringState</a>
* <a href="#ExpressRouteCircuitState">interface ExpressRouteCircuitState</a>
* <a href="#GetApplicationSecurityGroupArgs">interface GetApplicationSecurityGroupArgs</a>
* <a href="#GetApplicationSecurityGroupResult">interface GetApplicationSecurityGroupResult</a>
* <a href="#GetNetworkInterfaceArgs">interface GetNetworkInterfaceArgs</a>
* <a href="#GetNetworkInterfaceResult">interface GetNetworkInterfaceResult</a>
* <a href="#GetNetworkSecurityGroupArgs">interface GetNetworkSecurityGroupArgs</a>
* <a href="#GetNetworkSecurityGroupResult">interface GetNetworkSecurityGroupResult</a>
* <a href="#GetPublicIPArgs">interface GetPublicIPArgs</a>
* <a href="#GetPublicIPResult">interface GetPublicIPResult</a>
* <a href="#GetPublicIPsArgs">interface GetPublicIPsArgs</a>
* <a href="#GetPublicIPsResult">interface GetPublicIPsResult</a>
* <a href="#GetRouteTableArgs">interface GetRouteTableArgs</a>
* <a href="#GetRouteTableResult">interface GetRouteTableResult</a>
* <a href="#GetSubnetArgs">interface GetSubnetArgs</a>
* <a href="#GetSubnetResult">interface GetSubnetResult</a>
* <a href="#GetVirtualNetworkArgs">interface GetVirtualNetworkArgs</a>
* <a href="#GetVirtualNetworkGatewayArgs">interface GetVirtualNetworkGatewayArgs</a>
* <a href="#GetVirtualNetworkGatewayResult">interface GetVirtualNetworkGatewayResult</a>
* <a href="#GetVirtualNetworkResult">interface GetVirtualNetworkResult</a>
* <a href="#LocalNetworkGatewayArgs">interface LocalNetworkGatewayArgs</a>
* <a href="#LocalNetworkGatewayState">interface LocalNetworkGatewayState</a>
* <a href="#NetworkInterfaceArgs">interface NetworkInterfaceArgs</a>
* <a href="#NetworkInterfaceState">interface NetworkInterfaceState</a>
* <a href="#NetworkSecurityGroupArgs">interface NetworkSecurityGroupArgs</a>
* <a href="#NetworkSecurityGroupState">interface NetworkSecurityGroupState</a>
* <a href="#NetworkSecurityRuleArgs">interface NetworkSecurityRuleArgs</a>
* <a href="#NetworkSecurityRuleState">interface NetworkSecurityRuleState</a>
* <a href="#NetworkWatcherArgs">interface NetworkWatcherArgs</a>
* <a href="#NetworkWatcherState">interface NetworkWatcherState</a>
* <a href="#PacketCaptureArgs">interface PacketCaptureArgs</a>
* <a href="#PacketCaptureState">interface PacketCaptureState</a>
* <a href="#PublicIpArgs">interface PublicIpArgs</a>
* <a href="#PublicIpState">interface PublicIpState</a>
* <a href="#RouteArgs">interface RouteArgs</a>
* <a href="#RouteState">interface RouteState</a>
* <a href="#RouteTableArgs">interface RouteTableArgs</a>
* <a href="#RouteTableState">interface RouteTableState</a>
* <a href="#SubnetArgs">interface SubnetArgs</a>
* <a href="#SubnetState">interface SubnetState</a>
* <a href="#VirtualNetworkArgs">interface VirtualNetworkArgs</a>
* <a href="#VirtualNetworkGatewayArgs">interface VirtualNetworkGatewayArgs</a>
* <a href="#VirtualNetworkGatewayConnectionArgs">interface VirtualNetworkGatewayConnectionArgs</a>
* <a href="#VirtualNetworkGatewayConnectionState">interface VirtualNetworkGatewayConnectionState</a>
* <a href="#VirtualNetworkGatewayState">interface VirtualNetworkGatewayState</a>
* <a href="#VirtualNetworkPeeringArgs">interface VirtualNetworkPeeringArgs</a>
* <a href="#VirtualNetworkPeeringState">interface VirtualNetworkPeeringState</a>
* <a href="#VirtualNetworkState">interface VirtualNetworkState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts">network/applicationGateway.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts">network/applicationSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts">network/expressRouteCircuit.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts">network/expressRouteCircuitAuthorization.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts">network/expressRouteCircuitPeering.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts">network/getApplicationSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts">network/getNetworkInterface.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts">network/getNetworkSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts">network/getPublicIP.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts">network/getPublicIPs.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts">network/getRouteTable.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts">network/getSubnet.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts">network/getVirtualNetwork.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts">network/getVirtualNetworkGateway.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts">network/localNetworkGateway.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts">network/networkInterface.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts">network/networkSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts">network/networkSecurityRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts">network/networkWatcher.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts">network/packetCapture.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts">network/publicIp.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts">network/route.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts">network/routeTable.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts">network/subnet.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts">network/virtualNetwork.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts">network/virtualNetworkGateway.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts">network/virtualNetworkGatewayConnection.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts">network/virtualNetworkPeering.ts</a> 


<h2 class="pdoc-module-header" id="ApplicationGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L6">class ApplicationGateway</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L36">constructor</a>
</h3>

```typescript
new ApplicationGateway(name: string, args: ApplicationGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ApplicationGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationGatewayState): ApplicationGateway
```


Get an existing ApplicationGateway resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L19">property authenticationCertificates</a>
</h3>

```typescript
public authenticationCertificates: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L20">property backendAddressPools</a>
</h3>

```typescript
public backendAddressPools: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L21">property backendHttpSettings</a>
</h3>

```typescript
public backendHttpSettings: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L22">property disabledSslProtocols</a>
</h3>

```typescript
public disabledSslProtocols: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L23">property frontendIpConfigurations</a>
</h3>

```typescript
public frontendIpConfigurations: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L24">property frontendPorts</a>
</h3>

```typescript
public frontendPorts: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L25">property gatewayIpConfigurations</a>
</h3>

```typescript
public gatewayIpConfigurations: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L26">property httpListeners</a>
</h3>

```typescript
public httpListeners: pulumi.Output<{ ... }[]>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L27">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L28">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L29">property probes</a>
</h3>

```typescript
public probes: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L30">property requestRoutingRules</a>
</h3>

```typescript
public requestRoutingRules: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L31">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L32">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L33">property sslCertificates</a>
</h3>

```typescript
public sslCertificates: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L34">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L35">property urlPathMaps</a>
</h3>

```typescript
public urlPathMaps: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L36">property wafConfiguration</a>
</h3>

```typescript
public wafConfiguration: pulumi.Output<{ ... } | undefined>;
```

<h2 class="pdoc-module-header" id="ApplicationSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L9">class ApplicationSecurityGroup</a>
</h2>

Create an Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L37">constructor</a>
</h3>

```typescript
new ApplicationSecurityGroup(name: string, args: ApplicationSecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ApplicationSecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationSecurityGroupState): ApplicationSecurityGroup
```


Get an existing ApplicationSecurityGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Application Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L37">property tags</a>
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

<h2 class="pdoc-module-header" id="ExpressRouteCircuit">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L9">class ExpressRouteCircuit</a>
</h2>

Manages an ExpressRoute circuit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L65">constructor</a>
</h3>

```typescript
new ExpressRouteCircuit(name: string, args: ExpressRouteCircuitArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ExpressRouteCircuit resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ExpressRouteCircuitState): ExpressRouteCircuit
```


Get an existing ExpressRouteCircuit resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L25">property allowClassicOperations</a>
</h3>

```typescript
public allowClassicOperations: pulumi.Output<boolean | undefined>;
```


Allow the circuit to interact with classic (RDFE) resources. The default value is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L29">property bandwidthInMbps</a>
</h3>

```typescript
public bandwidthInMbps: pulumi.Output<number>;
```


The bandwidth in Mbps of the circuit being created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L33">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L41">property peeringLocation</a>
</h3>

```typescript
public peeringLocation: pulumi.Output<string>;
```


The name of the peering location and **not** the Azure resource location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L49">property serviceKey</a>
</h3>

```typescript
public serviceKey: pulumi.Output<string>;
```


The string needed by the service provider to provision the ExpressRoute circuit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L53">property serviceProviderName</a>
</h3>

```typescript
public serviceProviderName: pulumi.Output<string>;
```


The name of the ExpressRoute Service Provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L57">property serviceProviderProvisioningState</a>
</h3>

```typescript
public serviceProviderProvisioningState: pulumi.Output<string>;
```


The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L61">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block for the ExpressRoute circuit as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L65">property tags</a>
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

<h2 class="pdoc-module-header" id="ExpressRouteCircuitAuthorization">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L9">class ExpressRouteCircuitAuthorization</a>
</h2>

Manages an ExpressRoute Circuit Authorization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L43">constructor</a>
</h3>

```typescript
new ExpressRouteCircuitAuthorization(name: string, args: ExpressRouteCircuitAuthorizationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ExpressRouteCircuitAuthorization resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ExpressRouteCircuitAuthorizationState): ExpressRouteCircuitAuthorization
```


Get an existing ExpressRouteCircuitAuthorization resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L25">property authorizationKey</a>
</h3>

```typescript
public authorizationKey: pulumi.Output<string>;
```


The Authorization Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L29">property authorizationUseStatus</a>
</h3>

```typescript
public authorizationUseStatus: pulumi.Output<string>;
```


The authorization use status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L33">property expressRouteCircuitName</a>
</h3>

```typescript
public expressRouteCircuitName: pulumi.Output<string>;
```


The name of the Express Route Circuit in which to create the Authorization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L43">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitPeering">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L9">class ExpressRouteCircuitPeering</a>
</h2>

Manages an ExpressRoute Circuit Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L70">constructor</a>
</h3>

```typescript
new ExpressRouteCircuitPeering(name: string, args: ExpressRouteCircuitPeeringArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ExpressRouteCircuitPeering resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ExpressRouteCircuitPeeringState): ExpressRouteCircuitPeering
```


Get an existing ExpressRouteCircuitPeering resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L25">property azureAsn</a>
</h3>

```typescript
public azureAsn: pulumi.Output<number>;
```


The ASN used by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L29">property expressRouteCircuitName</a>
</h3>

```typescript
public expressRouteCircuitName: pulumi.Output<string>;
```


The name of the ExpressRoute Circuit in which to create the Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L33">property microsoftPeeringConfig</a>
</h3>

```typescript
public microsoftPeeringConfig: pulumi.Output<{ ... } | undefined>;
```


A `microsoft_peering_config` block as defined below. Required when `peering_type` is set to `MicrosoftPeering`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L37">property peerAsn</a>
</h3>

```typescript
public peerAsn: pulumi.Output<number>;
```


The Either a 16-bit or a 32-bit ASN. Can either be public or private..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L41">property peeringType</a>
</h3>

```typescript
public peeringType: pulumi.Output<string>;
```


The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L45">property primaryAzurePort</a>
</h3>

```typescript
public primaryAzurePort: pulumi.Output<string>;
```


The Primary Port used by Azure for this Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L49">property primaryPeerAddressPrefix</a>
</h3>

```typescript
public primaryPeerAddressPrefix: pulumi.Output<string>;
```


A `/30` subnet for the primary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L54">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L58">property secondaryAzurePort</a>
</h3>

```typescript
public secondaryAzurePort: pulumi.Output<string>;
```


The Secondary Port used by Azure for this Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L62">property secondaryPeerAddressPrefix</a>
</h3>

```typescript
public secondaryPeerAddressPrefix: pulumi.Output<string>;
```


A `/30` subnet for the secondary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L66">property sharedKey</a>
</h3>

```typescript
public sharedKey: pulumi.Output<string | undefined>;
```


The shared key. Can be a maximum of 25 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L70">property vlanId</a>
</h3>

```typescript
public vlanId: pulumi.Output<number>;
```


A valid VLAN ID to establish this peering on.

<h2 class="pdoc-module-header" id="LocalNetworkGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L9">class LocalNetworkGateway</a>
</h2>

Manages a local network gateway connection over which specific connections can be configured.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L55">constructor</a>
</h3>

```typescript
new LocalNetworkGateway(name: string, args: LocalNetworkGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LocalNetworkGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LocalNetworkGatewayState): LocalNetworkGateway
```


Get an existing LocalNetworkGateway resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L26">property addressSpaces</a>
</h3>

```typescript
public addressSpaces: pulumi.Output<string[]>;
```


The list of string CIDRs representing the
address spaces the gateway exposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L31">property bgpSettings</a>
</h3>

```typescript
public bgpSettings: pulumi.Output<{ ... } | undefined>;
```


A `bgp_settings` block as defined below containing the
Local Network Gateway's BGP speaker settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L36">property gatewayAddress</a>
</h3>

```typescript
public gatewayAddress: pulumi.Output<string>;
```


The IP address of the gateway to which to
connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L41">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the local network gateway is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the local network gateway. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L51">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the local network gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L55">property tags</a>
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

<h2 class="pdoc-module-header" id="NetworkInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L9">class NetworkInterface</a>
</h2>

Manages a Network Interface located in a Virtual Network, usually attached to a Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L82">constructor</a>
</h3>

```typescript
new NetworkInterface(name: string, args: NetworkInterfaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkInterface resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfaceState): NetworkInterface
```


Get an existing NetworkInterface resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L25">property appliedDnsServers</a>
</h3>

```typescript
public appliedDnsServers: pulumi.Output<string[]>;
```


If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L29">property dnsServers</a>
</h3>

```typescript
public dnsServers: pulumi.Output<string[]>;
```


List of DNS servers IP addresses to use for this NIC, overrides the VNet-level server list

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L33">property enableAcceleratedNetworking</a>
</h3>

```typescript
public enableAcceleratedNetworking: pulumi.Output<boolean | undefined>;
```


Enables Azure Accelerated Networking using SR-IOV. Only certain VM instance sizes are supported. Refer to [Create a Virtual Machine with Accelerated Networking](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli). Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L37">property enableIpForwarding</a>
</h3>

```typescript
public enableIpForwarding: pulumi.Output<boolean | undefined>;
```


Enables IP Forwarding on the NIC. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L41">property internalDnsNameLabel</a>
</h3>

```typescript
public internalDnsNameLabel: pulumi.Output<string>;
```


Relative DNS name for this NIC used for internal communications between VMs in the same VNet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L45">property internalFqdn</a>
</h3>

```typescript
public internalFqdn: pulumi.Output<string>;
```


Fully qualified DNS name supporting internal communications between VMs in the same VNet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L49">property ipConfigurations</a>
</h3>

```typescript
public ipConfigurations: pulumi.Output<{ ... }[]>;
```


One or more `ip_configuration` associated with this NIC as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L53">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the network interface is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L57">property macAddress</a>
</h3>

```typescript
public macAddress: pulumi.Output<string>;
```


The media access control (MAC) address of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


User-defined name of the IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L65">property networkSecurityGroupId</a>
</h3>

```typescript
public networkSecurityGroupId: pulumi.Output<string | undefined>;
```


The ID of the Network Security Group to associate with the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L69">property privateIpAddress</a>
</h3>

```typescript
public privateIpAddress: pulumi.Output<string>;
```


Static IP Address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L70">property privateIpAddresses</a>
</h3>

```typescript
public privateIpAddresses: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L74">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the network interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L78">property tags</a>
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

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L82">property virtualMachineId</a>
</h3>

```typescript
public virtualMachineId: pulumi.Output<string>;
```


Reference to a VM with which this NIC has been associated.

<h2 class="pdoc-module-header" id="NetworkSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L13">class NetworkSecurityGroup</a>
</h2>

Manages a network security group that contains a list of network security rules.  Network security groups enable inbound or outbound traffic to be enabled or denied.

~> **NOTE on Network Security Groups and Network Security Rules:** Terraform currently
provides both a standalone [Network Security Rule resource](network_security_rule.html), and allows for Network Security Rules to be defined in-line within the [Network Security Group resource](network_security_group.html).
At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L45">constructor</a>
</h3>

```typescript
new NetworkSecurityGroup(name: string, args: NetworkSecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkSecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkSecurityGroupState): NetworkSecurityGroup
```


Get an existing NetworkSecurityGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L29">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the security rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L37">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L41">property securityRules</a>
</h3>

```typescript
public securityRules: pulumi.Output<{ ... }[]>;
```


One or more `security_rule` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L45">property tags</a>
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

<h2 class="pdoc-module-header" id="NetworkSecurityRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L13">class NetworkSecurityRule</a>
</h2>

Manages a Network Security Rule.

~> **NOTE on Network Security Groups and Network Security Rules:** Terraform currently
provides both a standalone [Network Security Rule resource](network_security_rule.html), and allows for Network Security Rules to be defined in-line within the [Network Security Group resource](network_security_group.html).
At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L97">constructor</a>
</h3>

```typescript
new NetworkSecurityRule(name: string, args: NetworkSecurityRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkSecurityRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkSecurityRuleState): NetworkSecurityRule
```


Get an existing NetworkSecurityRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L29">property access</a>
</h3>

```typescript
public access: pulumi.Output<string>;
```


Specifies whether network traffic is allowed or denied. Possible values are `Allow` and `Deny`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for this rule. Restricted to 140 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L37">property destinationAddressPrefix</a>
</h3>

```typescript
public destinationAddressPrefix: pulumi.Output<string | undefined>;
```


CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `destination_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L41">property destinationAddressPrefixes</a>
</h3>

```typescript
public destinationAddressPrefixes: pulumi.Output<string[] | undefined>;
```


List of destination address prefixes. Tags may not be used. This is required if `destination_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L45">property destinationApplicationSecurityGroupIds</a>
</h3>

```typescript
public destinationApplicationSecurityGroupIds: pulumi.Output<string | undefined>;
```


A List of destination Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L49">property destinationPortRange</a>
</h3>

```typescript
public destinationPortRange: pulumi.Output<string | undefined>;
```


Destination Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `destination_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L53">property destinationPortRanges</a>
</h3>

```typescript
public destinationPortRanges: pulumi.Output<string[] | undefined>;
```


List of destination ports or port ranges. This is required if `destination_port_range` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L57">property direction</a>
</h3>

```typescript
public direction: pulumi.Output<string>;
```


The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are `Inbound` and `Outbound`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L65">property networkSecurityGroupName</a>
</h3>

```typescript
public networkSecurityGroupName: pulumi.Output<string>;
```


The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L69">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<number>;
```


Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L73">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


Network protocol this rule applies to. Possible values include `Tcp`, `Udp` or `*` (which matches both).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L77">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L81">property sourceAddressPrefix</a>
</h3>

```typescript
public sourceAddressPrefix: pulumi.Output<string | undefined>;
```


CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `source_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L85">property sourceAddressPrefixes</a>
</h3>

```typescript
public sourceAddressPrefixes: pulumi.Output<string[] | undefined>;
```


List of source address prefixes. Tags may not be used. This is required if `source_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L89">property sourceApplicationSecurityGroupIds</a>
</h3>

```typescript
public sourceApplicationSecurityGroupIds: pulumi.Output<string | undefined>;
```


A List of source Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L93">property sourcePortRange</a>
</h3>

```typescript
public sourcePortRange: pulumi.Output<string | undefined>;
```


Source Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `source_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L97">property sourcePortRanges</a>
</h3>

```typescript
public sourcePortRanges: pulumi.Output<string[] | undefined>;
```


List of source ports or port ranges. This is required if `source_port_range` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NetworkWatcher">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L9">class NetworkWatcher</a>
</h2>

Manages a Network Watcher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L37">constructor</a>
</h3>

```typescript
new NetworkWatcher(name: string, args: NetworkWatcherArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkWatcher resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkWatcherState): NetworkWatcher
```


Get an existing NetworkWatcher resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L37">property tags</a>
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

<h2 class="pdoc-module-header" id="PacketCapture">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L9">class PacketCapture</a>
</h2>

Configures Packet Capturing against a Virtual Machine using a Network Watcher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L57">constructor</a>
</h3>

```typescript
new PacketCapture(name: string, args: PacketCaptureArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PacketCapture resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PacketCaptureState): PacketCapture
```


Get an existing PacketCapture resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L25">property filters</a>
</h3>

```typescript
public filters: pulumi.Output<{ ... }[] | undefined>;
```


One or more `filter` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L29">property maximumBytesPerPacket</a>
</h3>

```typescript
public maximumBytesPerPacket: pulumi.Output<number | undefined>;
```


The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L33">property maximumBytesPerSession</a>
</h3>

```typescript
public maximumBytesPerSession: pulumi.Output<number | undefined>;
```


Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L37">property maximumCaptureDuration</a>
</h3>

```typescript
public maximumCaptureDuration: pulumi.Output<number | undefined>;
```


The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name to use for this Packet Capture. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L45">property networkWatcherName</a>
</h3>

```typescript
public networkWatcherName: pulumi.Output<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L49">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L53">property storageLocation</a>
</h3>

```typescript
public storageLocation: pulumi.Output<{ ... }>;
```


A `storage_location` block as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L57">property targetResourceId</a>
</h3>

```typescript
public targetResourceId: pulumi.Output<string>;
```


The ID of the Resource to capture packets from. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PublicIp">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L9">class PublicIp</a>
</h2>

Create a Public IP Address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L71">constructor</a>
</h3>

```typescript
new PublicIp(name: string, args: PublicIpArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PublicIp resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PublicIpState): PublicIp
```


Get an existing PublicIp resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L25">property domainNameLabel</a>
</h3>

```typescript
public domainNameLabel: pulumi.Output<string | undefined>;
```


Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L29">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L33">property idleTimeoutInMinutes</a>
</h3>

```typescript
public idleTimeoutInMinutes: pulumi.Output<number | undefined>;
```


Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L37">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


The IP address value that was allocated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L41">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L50">property publicIpAddressAllocation</a>
</h3>

```typescript
public publicIpAddressAllocation: pulumi.Output<string>;
```


Defines whether the IP address is static or dynamic. Options are Static or Dynamic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L55">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the public ip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L59">property reverseFqdn</a>
</h3>

```typescript
public reverseFqdn: pulumi.Output<string | undefined>;
```


A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L63">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string | undefined>;
```


The SKU of the Public IP. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L67">property tags</a>
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

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L71">property zones</a>
</h3>

```typescript
public zones: pulumi.Output<string | undefined>;
```


A collection containing the availability zone to allocate the Public IP in.

<h2 class="pdoc-module-header" id="Route">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L9">class Route</a>
</h2>

Manages a Route within a Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L45">constructor</a>
</h3>

```typescript
new Route(name: string, args: RouteArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Route resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteState): Route
```


Get an existing Route resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L25">property addressPrefix</a>
</h3>

```typescript
public addressPrefix: pulumi.Output<string>;
```


The destination CIDR to which the route applies, such as `10.1.0.0/16`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L33">property nextHopInIpAddress</a>
</h3>

```typescript
public nextHopInIpAddress: pulumi.Output<string>;
```


Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is `VirtualAppliance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L37">property nextHopType</a>
</h3>

```typescript
public nextHopType: pulumi.Output<string>;
```


The type of Azure hop the packet should be sent to. Possible values are `VirtualNetworkGateway`, `VnetLocal`, `Internet`, `VirtualAppliance` and `None`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L41">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L45">property routeTableName</a>
</h3>

```typescript
public routeTableName: pulumi.Output<string>;
```


The name of the route table within which create the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RouteTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L9">class RouteTable</a>
</h2>

Manages a Route Table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L49">constructor</a>
</h3>

```typescript
new RouteTable(name: string, args: RouteTableArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RouteTable resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteTableState): RouteTable
```


Get an existing RouteTable resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L25">property disableBgpRoutePropagation</a>
</h3>

```typescript
public disableBgpRoutePropagation: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L29">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L37">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the route table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L41">property routes</a>
</h3>

```typescript
public routes: pulumi.Output<{ ... }[]>;
```


Can be specified multiple times to define multiple routes. Each `route` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L45">property subnets</a>
</h3>

```typescript
public subnets: pulumi.Output<string[]>;
```


The collection of Subnets associated with this route table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L49">property tags</a>
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

<h2 class="pdoc-module-header" id="Subnet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L13">class Subnet</a>
</h2>

Manages a subnet. Subnets represent network segments within the IP space defined by the virtual network.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone [Subnet resource](subnet.html), and allows for Subnets to be defined in-line within the [Virtual Network resource](virtual_network.html).
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet's.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L57">constructor</a>
</h3>

```typescript
new Subnet(name: string, args: SubnetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Subnet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetState): Subnet
```


Get an existing Subnet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L29">property addressPrefix</a>
</h3>

```typescript
public addressPrefix: pulumi.Output<string>;
```


The address prefix to use for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L33">property ipConfigurations</a>
</h3>

```typescript
public ipConfigurations: pulumi.Output<string[]>;
```


The collection of IP Configurations with IPs within this subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L41">property networkSecurityGroupId</a>
</h3>

```typescript
public networkSecurityGroupId: pulumi.Output<string | undefined>;
```


The ID of the Network Security Group to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L49">property routeTableId</a>
</h3>

```typescript
public routeTableId: pulumi.Output<string | undefined>;
```


The ID of the Route Table to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L53">property serviceEndpoints</a>
</h3>

```typescript
public serviceEndpoints: pulumi.Output<string[] | undefined>;
```


The list of Service endpoints to associate with the subnet. Possible values include: `Microsoft.Storage`, `Microsoft.Sql`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L57">property virtualNetworkName</a>
</h3>

```typescript
public virtualNetworkName: pulumi.Output<string>;
```


The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L14">class VirtualNetwork</a>
</h2>

Manages a virtual network including any configured subnets. Each subnet can
optionally be configured with a security group to be associated with the subnet.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone [Subnet resource](subnet.html), and allows for Subnets to be defined in-line within the [Virtual Network resource](virtual_network.html).
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet's.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L59">constructor</a>
</h3>

```typescript
new VirtualNetwork(name: string, args: VirtualNetworkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNetwork resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualNetworkState): VirtualNetwork
```


Get an existing VirtualNetwork resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L32">property addressSpaces</a>
</h3>

```typescript
public addressSpaces: pulumi.Output<string[]>;
```


The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L36">property dnsServers</a>
</h3>

```typescript
public dnsServers: pulumi.Output<string[] | undefined>;
```


List of IP addresses of DNS servers

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L41">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the virtual network is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L50">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L55">property subnets</a>
</h3>

```typescript
public subnets: pulumi.Output<{ ... }[]>;
```


Can be specified multiple times to define multiple
subnets. Each `subnet` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L59">property tags</a>
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

<h2 class="pdoc-module-header" id="VirtualNetworkGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L11">class VirtualNetworkGateway</a>
</h2>

Manages a Virtual Network Gateway to establish secure, cross-premises connectivity.

-> **Note:** Please be aware that provisioning a Virtual Network Gateway takes a long time (between 30 minutes and 1 hour)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L93">constructor</a>
</h3>

```typescript
new VirtualNetworkGateway(name: string, args: VirtualNetworkGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNetworkGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualNetworkGatewayState): VirtualNetworkGateway
```


Get an existing VirtualNetworkGateway resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L30">property activeActive</a>
</h3>

```typescript
public activeActive: pulumi.Output<boolean>;
```


If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L31">property bgpSettings</a>
</h3>

```typescript
public bgpSettings: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L39">property defaultLocalNetworkGatewayId</a>
</h3>

```typescript
public defaultLocalNetworkGatewayId: pulumi.Output<string | undefined>;
```


The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L44">property enableBgp</a>
</h3>

```typescript
public enableBgp: pulumi.Output<boolean>;
```


If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L50">property ipConfigurations</a>
</h3>

```typescript
public ipConfigurations: pulumi.Output<{ ... }[]>;
```


One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L55">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L59">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A user-defined name of the revoked certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L65">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L73">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`VpnGw1`, `VpnGw2` and `VpnGw3` and depend on the `type` and `vpn_type` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L77">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L82">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L88">property vpnClientConfiguration</a>
</h3>

```typescript
public vpnClientConfiguration: pulumi.Output<{ ... } | undefined>;
```


A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L93">property vpnType</a>
</h3>

```typescript
public vpnType: pulumi.Output<string | undefined>;
```


The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayConnection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L9">class VirtualNetworkGatewayConnection</a>
</h2>

Manages a connection in an existing Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L105">constructor</a>
</h3>

```typescript
new VirtualNetworkGatewayConnection(name: string, args: VirtualNetworkGatewayConnectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNetworkGatewayConnection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualNetworkGatewayConnectionState): VirtualNetworkGatewayConnection
```


Get an existing VirtualNetworkGatewayConnection resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L27">property authorizationKey</a>
</h3>

```typescript
public authorizationKey: pulumi.Output<string | undefined>;
```


The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L32">property enableBgp</a>
</h3>

```typescript
public enableBgp: pulumi.Output<boolean>;
```


If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L38">property expressRouteCircuitId</a>
</h3>

```typescript
public expressRouteCircuitId: pulumi.Output<string | undefined>;
```


The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L44">property ipsecPolicy</a>
</h3>

```typescript
public ipsecPolicy: pulumi.Output<{ ... } | undefined>;
```


A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L49">property localNetworkGatewayId</a>
</h3>

```typescript
public localNetworkGatewayId: pulumi.Output<string | undefined>;
```


The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L54">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the connection is
located. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L59">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the connection. Changing the name forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L66">property peerVirtualNetworkGatewayId</a>
</h3>

```typescript
public peerVirtualNetworkGatewayId: pulumi.Output<string | undefined>;
```


The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L71">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L75">property routingWeight</a>
</h3>

```typescript
public routingWeight: pulumi.Output<number>;
```


The routing weight. Defaults to `10`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L81">property sharedKey</a>
</h3>

```typescript
public sharedKey: pulumi.Output<string | undefined>;
```


The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L85">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L93">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L99">property usePolicyBasedTrafficSelectors</a>
</h3>

```typescript
public usePolicyBasedTrafficSelectors: pulumi.Output<boolean>;
```


If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L105">property virtualNetworkGatewayId</a>
</h3>

```typescript
public virtualNetworkGatewayId: pulumi.Output<string>;
```


The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkPeering">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L10">class VirtualNetworkPeering</a>
</h2>

Manages a virtual network peering which allows resources to access other
resources in the linked virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L68">constructor</a>
</h3>

```typescript
new VirtualNetworkPeering(name: string, args: VirtualNetworkPeeringArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNetworkPeering resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualNetworkPeeringState): VirtualNetworkPeering
```


Get an existing VirtualNetworkPeering resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L27">property allowForwardedTraffic</a>
</h3>

```typescript
public allowForwardedTraffic: pulumi.Output<boolean>;
```


Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L32">property allowGatewayTransit</a>
</h3>

```typescript
public allowGatewayTransit: pulumi.Output<boolean>;
```


Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L38">property allowVirtualNetworkAccess</a>
</h3>

```typescript
public allowVirtualNetworkAccess: pulumi.Output<boolean>;
```


Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the virtual network peering. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L48">property remoteVirtualNetworkId</a>
</h3>

```typescript
public remoteVirtualNetworkId: pulumi.Output<string>;
```


The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L54">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L63">property useRemoteGateways</a>
</h3>

```typescript
public useRemoteGateways: pulumi.Output<boolean>;
```


Controls if remote gateways can be used on
the local virtual network. If the flag is set to `true`, and
`allow_gateway_transit` on the remote peering is also `true`, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to `true`. This flag cannot be set if virtual network
already has a gateway. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L68">property virtualNetworkName</a>
</h3>

```typescript
public virtualNetworkName: pulumi.Output<string>;
```


The name of the virtual network. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="getApplicationSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L9">function getApplicationSecurityGroup</a>
</h2>

```typescript
getApplicationSecurityGroup(args: GetApplicationSecurityGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetApplicationSecurityGroupResult>
```


Get information about an Application Security Group.

<h2 class="pdoc-module-header" id="getNetworkInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L9">function getNetworkInterface</a>
</h2>

```typescript
getNetworkInterface(args: GetNetworkInterfaceArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkInterfaceResult>
```


Use this data source to access the properties of an Azure Network Interface.

<h2 class="pdoc-module-header" id="getNetworkSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L9">function getNetworkSecurityGroup</a>
</h2>

```typescript
getNetworkSecurityGroup(args: GetNetworkSecurityGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkSecurityGroupResult>
```


Use this data source to access the properties of a Network Security Group.

<h2 class="pdoc-module-header" id="getPublicIP">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L9">function getPublicIP</a>
</h2>

```typescript
getPublicIP(args: GetPublicIPArgs, opts?: pulumi.InvokeOptions): Promise<GetPublicIPResult>
```


Use this data source to access the properties of an existing Azure Public IP Address.

<h2 class="pdoc-module-header" id="getPublicIPs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L9">function getPublicIPs</a>
</h2>

```typescript
getPublicIPs(args: GetPublicIPsArgs, opts?: pulumi.InvokeOptions): Promise<GetPublicIPsResult>
```


Use this data source to access a filtered list of Public IP Addresses

<h2 class="pdoc-module-header" id="getRouteTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L9">function getRouteTable</a>
</h2>

```typescript
getRouteTable(args: GetRouteTableArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteTableResult>
```


Gets information about a Route Table

<h2 class="pdoc-module-header" id="getSubnet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L9">function getSubnet</a>
</h2>

```typescript
getSubnet(args: GetSubnetArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetResult>
```


Use this data source to access the properties of an Azure Subnet located within a Virtual Network.

<h2 class="pdoc-module-header" id="getVirtualNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L9">function getVirtualNetwork</a>
</h2>

```typescript
getVirtualNetwork(args: GetVirtualNetworkArgs, opts?: pulumi.InvokeOptions): Promise<GetVirtualNetworkResult>
```


Use this data source to access the properties of an Azure Virtual Network.

<h2 class="pdoc-module-header" id="getVirtualNetworkGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L9">function getVirtualNetworkGateway</a>
</h2>

```typescript
getVirtualNetworkGateway(args: GetVirtualNetworkGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetVirtualNetworkGatewayResult>
```


Use this data source to access the properties of an Azure Virtual Network Gateway.

<h2 class="pdoc-module-header" id="ApplicationGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L150">interface ApplicationGatewayArgs</a>
</h2>

The set of arguments for constructing a ApplicationGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L151">property authenticationCertificates</a>
</h3>

```typescript
authenticationCertificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L152">property backendAddressPools</a>
</h3>

```typescript
backendAddressPools: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L153">property backendHttpSettings</a>
</h3>

```typescript
backendHttpSettings: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L154">property disabledSslProtocols</a>
</h3>

```typescript
disabledSslProtocols?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L155">property frontendIpConfigurations</a>
</h3>

```typescript
frontendIpConfigurations: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L156">property frontendPorts</a>
</h3>

```typescript
frontendPorts: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L157">property gatewayIpConfigurations</a>
</h3>

```typescript
gatewayIpConfigurations: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L158">property httpListeners</a>
</h3>

```typescript
httpListeners: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L159">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L160">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L161">property probes</a>
</h3>

```typescript
probes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L162">property requestRoutingRules</a>
</h3>

```typescript
requestRoutingRules: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L163">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L164">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L165">property sslCertificates</a>
</h3>

```typescript
sslCertificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L166">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L167">property urlPathMaps</a>
</h3>

```typescript
urlPathMaps?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L168">property wafConfiguration</a>
</h3>

```typescript
wafConfiguration?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ApplicationGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L126">interface ApplicationGatewayState</a>
</h2>

Input properties used for looking up and filtering ApplicationGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L127">property authenticationCertificates</a>
</h3>

```typescript
authenticationCertificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L128">property backendAddressPools</a>
</h3>

```typescript
backendAddressPools?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L129">property backendHttpSettings</a>
</h3>

```typescript
backendHttpSettings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L130">property disabledSslProtocols</a>
</h3>

```typescript
disabledSslProtocols?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L131">property frontendIpConfigurations</a>
</h3>

```typescript
frontendIpConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L132">property frontendPorts</a>
</h3>

```typescript
frontendPorts?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L133">property gatewayIpConfigurations</a>
</h3>

```typescript
gatewayIpConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L134">property httpListeners</a>
</h3>

```typescript
httpListeners?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L135">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L137">property probes</a>
</h3>

```typescript
probes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L138">property requestRoutingRules</a>
</h3>

```typescript
requestRoutingRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L139">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L140">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L141">property sslCertificates</a>
</h3>

```typescript
sslCertificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L142">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L143">property urlPathMaps</a>
</h3>

```typescript
urlPathMaps?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L144">property wafConfiguration</a>
</h3>

```typescript
wafConfiguration?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ApplicationSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L97">interface ApplicationSecurityGroupArgs</a>
</h2>

The set of arguments for constructing a ApplicationSecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L101">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Application Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L109">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L113">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ApplicationSecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L75">interface ApplicationSecurityGroupState</a>
</h2>

Input properties used for looking up and filtering ApplicationSecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L79">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L83">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Application Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L87">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L91">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L179">interface ExpressRouteCircuitArgs</a>
</h2>

The set of arguments for constructing a ExpressRouteCircuit resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L183">property allowClassicOperations</a>
</h3>

```typescript
allowClassicOperations?: pulumi.Input<boolean>;
```


Allow the circuit to interact with classic (RDFE) resources. The default value is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L187">property bandwidthInMbps</a>
</h3>

```typescript
bandwidthInMbps: pulumi.Input<number>;
```


The bandwidth in Mbps of the circuit being created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L191">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L195">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L199">property peeringLocation</a>
</h3>

```typescript
peeringLocation: pulumi.Input<string>;
```


The name of the peering location and **not** the Azure resource location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L203">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L207">property serviceProviderName</a>
</h3>

```typescript
serviceProviderName: pulumi.Input<string>;
```


The name of the ExpressRoute Service Provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L211">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block for the ExpressRoute circuit as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L215">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitAuthorizationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L111">interface ExpressRouteCircuitAuthorizationArgs</a>
</h2>

The set of arguments for constructing a ExpressRouteCircuitAuthorization resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L115">property expressRouteCircuitName</a>
</h3>

```typescript
expressRouteCircuitName: pulumi.Input<string>;
```


The name of the Express Route Circuit in which to create the Authorization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L125">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitAuthorizationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L83">interface ExpressRouteCircuitAuthorizationState</a>
</h2>

Input properties used for looking up and filtering ExpressRouteCircuitAuthorization resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L87">property authorizationKey</a>
</h3>

```typescript
authorizationKey?: pulumi.Input<string>;
```


The Authorization Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L91">property authorizationUseStatus</a>
</h3>

```typescript
authorizationUseStatus?: pulumi.Input<string>;
```


The authorization use status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L95">property expressRouteCircuitName</a>
</h3>

```typescript
expressRouteCircuitName?: pulumi.Input<string>;
```


The name of the Express Route Circuit in which to create the Authorization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L105">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitPeeringArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L191">interface ExpressRouteCircuitPeeringArgs</a>
</h2>

The set of arguments for constructing a ExpressRouteCircuitPeering resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L195">property expressRouteCircuitName</a>
</h3>

```typescript
expressRouteCircuitName: pulumi.Input<string>;
```


The name of the ExpressRoute Circuit in which to create the Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L199">property microsoftPeeringConfig</a>
</h3>

```typescript
microsoftPeeringConfig?: pulumi.Input<{ ... }>;
```


A `microsoft_peering_config` block as defined below. Required when `peering_type` is set to `MicrosoftPeering`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L203">property peerAsn</a>
</h3>

```typescript
peerAsn?: pulumi.Input<number>;
```


The Either a 16-bit or a 32-bit ASN. Can either be public or private..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L207">property peeringType</a>
</h3>

```typescript
peeringType: pulumi.Input<string>;
```


The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L211">property primaryPeerAddressPrefix</a>
</h3>

```typescript
primaryPeerAddressPrefix: pulumi.Input<string>;
```


A `/30` subnet for the primary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L216">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L220">property secondaryPeerAddressPrefix</a>
</h3>

```typescript
secondaryPeerAddressPrefix: pulumi.Input<string>;
```


A `/30` subnet for the secondary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L224">property sharedKey</a>
</h3>

```typescript
sharedKey?: pulumi.Input<string>;
```


The shared key. Can be a maximum of 25 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L228">property vlanId</a>
</h3>

```typescript
vlanId: pulumi.Input<number>;
```


A valid VLAN ID to establish this peering on.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitPeeringState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L136">interface ExpressRouteCircuitPeeringState</a>
</h2>

Input properties used for looking up and filtering ExpressRouteCircuitPeering resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L140">property azureAsn</a>
</h3>

```typescript
azureAsn?: pulumi.Input<number>;
```


The ASN used by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L144">property expressRouteCircuitName</a>
</h3>

```typescript
expressRouteCircuitName?: pulumi.Input<string>;
```


The name of the ExpressRoute Circuit in which to create the Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L148">property microsoftPeeringConfig</a>
</h3>

```typescript
microsoftPeeringConfig?: pulumi.Input<{ ... }>;
```


A `microsoft_peering_config` block as defined below. Required when `peering_type` is set to `MicrosoftPeering`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L152">property peerAsn</a>
</h3>

```typescript
peerAsn?: pulumi.Input<number>;
```


The Either a 16-bit or a 32-bit ASN. Can either be public or private..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L156">property peeringType</a>
</h3>

```typescript
peeringType?: pulumi.Input<string>;
```


The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L160">property primaryAzurePort</a>
</h3>

```typescript
primaryAzurePort?: pulumi.Input<string>;
```


The Primary Port used by Azure for this Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L164">property primaryPeerAddressPrefix</a>
</h3>

```typescript
primaryPeerAddressPrefix?: pulumi.Input<string>;
```


A `/30` subnet for the primary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L169">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L173">property secondaryAzurePort</a>
</h3>

```typescript
secondaryAzurePort?: pulumi.Input<string>;
```


The Secondary Port used by Azure for this Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L177">property secondaryPeerAddressPrefix</a>
</h3>

```typescript
secondaryPeerAddressPrefix?: pulumi.Input<string>;
```


A `/30` subnet for the secondary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L181">property sharedKey</a>
</h3>

```typescript
sharedKey?: pulumi.Input<string>;
```


The shared key. Can be a maximum of 25 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L185">property vlanId</a>
</h3>

```typescript
vlanId?: pulumi.Input<number>;
```


A valid VLAN ID to establish this peering on.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L129">interface ExpressRouteCircuitState</a>
</h2>

Input properties used for looking up and filtering ExpressRouteCircuit resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L133">property allowClassicOperations</a>
</h3>

```typescript
allowClassicOperations?: pulumi.Input<boolean>;
```


Allow the circuit to interact with classic (RDFE) resources. The default value is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L137">property bandwidthInMbps</a>
</h3>

```typescript
bandwidthInMbps?: pulumi.Input<number>;
```


The bandwidth in Mbps of the circuit being created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L141">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L145">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L149">property peeringLocation</a>
</h3>

```typescript
peeringLocation?: pulumi.Input<string>;
```


The name of the peering location and **not** the Azure resource location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L153">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L157">property serviceKey</a>
</h3>

```typescript
serviceKey?: pulumi.Input<string>;
```


The string needed by the service provider to provision the ExpressRoute circuit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L161">property serviceProviderName</a>
</h3>

```typescript
serviceProviderName?: pulumi.Input<string>;
```


The name of the ExpressRoute Service Provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L165">property serviceProviderProvisioningState</a>
</h3>

```typescript
serviceProviderProvisioningState?: pulumi.Input<string>;
```


The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L169">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block for the ExpressRoute circuit as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L173">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="GetApplicationSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L19">interface GetApplicationSecurityGroupArgs</a>
</h2>

A collection of arguments for invoking getApplicationSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


The name of the Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the resource group in which the Application Security Group exists.

<h2 class="pdoc-module-header" id="GetApplicationSecurityGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L33">interface GetApplicationSecurityGroupResult</a>
</h2>

A collection of values returned by getApplicationSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L45">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L37">property location</a>
</h3>

```typescript
location: string;
```


The supported Azure location where the Application Security Group exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L41">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="GetNetworkInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L19">interface GetNetworkInterfaceArgs</a>
</h2>

A collection of arguments for invoking getNetworkInterface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Network Interface is located in.

<h2 class="pdoc-module-header" id="GetNetworkInterfaceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L33">interface GetNetworkInterfaceResult</a>
</h2>

A collection of values returned by getNetworkInterface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L37">property appliedDnsServers</a>
</h3>

```typescript
appliedDnsServers: string[];
```


List of DNS servers applied to the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L41">property dnsServers</a>
</h3>

```typescript
dnsServers: string[];
```


The list of DNS servers used by the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L45">property enableAcceleratedNetworking</a>
</h3>

```typescript
enableAcceleratedNetworking: boolean;
```


Indicates if accelerated networking is set on the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L49">property enableIpForwarding</a>
</h3>

```typescript
enableIpForwarding: boolean;
```


Indicate if IP forwarding is set on the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L93">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L53">property internalDnsNameLabel</a>
</h3>

```typescript
internalDnsNameLabel: string;
```


The internal dns name label of the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L57">property internalFqdn</a>
</h3>

```typescript
internalFqdn: string;
```


The internal FQDN associated to the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L61">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: { ... }[];
```


One or more `ip_configuration` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L65">property location</a>
</h3>

```typescript
location: string;
```


The location of the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L69">property macAddress</a>
</h3>

```typescript
macAddress: string;
```


The MAC address used by the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L73">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId: string;
```


The ID of the network security group associated to the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L77">property privateIpAddress</a>
</h3>

```typescript
privateIpAddress: string;
```


The Private IP Address assigned to this Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L81">property privateIpAddresses</a>
</h3>

```typescript
privateIpAddresses: string[];
```


The list of private ip addresses associates to the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L85">property tags</a>
</h3>

```typescript
tags: { ... };
```


List the tags associated to the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L89">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId: string;
```


The ID of the virtual machine that the specified Network Interface is attached to.

<h2 class="pdoc-module-header" id="GetNetworkSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L19">interface GetNetworkSecurityGroupArgs</a>
</h2>

A collection of arguments for invoking getNetworkSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the Name of the Network Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the Name of the Resource Group within which the Network Security Group exists

<h2 class="pdoc-module-header" id="GetNetworkSecurityGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L33">interface GetNetworkSecurityGroupResult</a>
</h2>

A collection of values returned by getNetworkSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L49">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L37">property location</a>
</h3>

```typescript
location: string;
```


The supported Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L41">property securityRules</a>
</h3>

```typescript
securityRules: { ... }[];
```


One or more `security_rule` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L45">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="GetPublicIPArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L20">interface GetPublicIPArgs</a>
</h2>

A collection of arguments for invoking getPublicIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the public IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L29">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetPublicIPResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L35">interface GetPublicIPResult</a>
</h2>

A collection of values returned by getPublicIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L39">property domainNameLabel</a>
</h3>

```typescript
domainNameLabel: string;
```


The label for the Domain Name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L43">property fqdn</a>
</h3>

```typescript
fqdn: string;
```


Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L59">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L47">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes: number;
```


Specifies the timeout for the TCP idle connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L51">property ipAddress</a>
</h3>

```typescript
ipAddress: string;
```


The IP address value that was allocated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L55">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assigned to the resource.

<h2 class="pdoc-module-header" id="GetPublicIPsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L21">interface GetPublicIPsArgs</a>
</h2>

A collection of arguments for invoking getPublicIPs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L25">property allocationType</a>
</h3>

```typescript
allocationType?: string;
```


The Allocation Type for the Public IP Address. Possible values include `Static` or `Dynamic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L29">property attached</a>
</h3>

```typescript
attached?: boolean;
```


Filter to include IP Addresses which are attached to a device, such as a VM/LB (`true`) or unattached (`false`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L33">property namePrefix</a>
</h3>

```typescript
namePrefix?: string;
```


A prefix match used for the IP Addresses `name` field, case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L37">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group.

<h2 class="pdoc-module-header" id="GetPublicIPsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L43">interface GetPublicIPsResult</a>
</h2>

A collection of values returned by getPublicIPs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L51">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L47">property publicIps</a>
</h3>

```typescript
publicIps: { ... }[];
```


A List of `public_ips` blocks as defined below filtered by the criteria above.

<h2 class="pdoc-module-header" id="GetRouteTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L19">interface GetRouteTableArgs</a>
</h2>

A collection of arguments for invoking getRouteTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


The name of the Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the Route Table exists.

<h2 class="pdoc-module-header" id="GetRouteTableResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L33">interface GetRouteTableResult</a>
</h2>

A collection of values returned by getRouteTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L53">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L37">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region in which the Route Table exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L41">property routes</a>
</h3>

```typescript
routes: { ... }[];
```


One or more `route` blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L45">property subnets</a>
</h3>

```typescript
subnets: string[];
```


The collection of Subnets associated with this route table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L49">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the Route Table.

<h2 class="pdoc-module-header" id="GetSubnetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L20">interface GetSubnetArgs</a>
</h2>

A collection of arguments for invoking getSubnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Virtual Network is located in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L32">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName: string;
```


Specifies the name of the Virtual Network this Subnet is located within.

<h2 class="pdoc-module-header" id="GetSubnetResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L38">interface GetSubnetResult</a>
</h2>

A collection of values returned by getSubnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L42">property addressPrefix</a>
</h3>

```typescript
addressPrefix: string;
```


The address prefix used for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L58">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L46">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: string[];
```


The collection of IP Configurations with IPs within this subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L50">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId: string;
```


The ID of the Network Security Group associated with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L54">property routeTableId</a>
</h3>

```typescript
routeTableId: string;
```


The ID of the Route Table associated with this subnet.

<h2 class="pdoc-module-header" id="GetVirtualNetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L19">interface GetVirtualNetworkArgs</a>
</h2>

A collection of arguments for invoking getVirtualNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Virtual Network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Virtual Network is located in.

<h2 class="pdoc-module-header" id="GetVirtualNetworkGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L19">interface GetVirtualNetworkGatewayArgs</a>
</h2>

A collection of arguments for invoking getVirtualNetworkGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Virtual Network Gateway is located in.

<h2 class="pdoc-module-header" id="GetVirtualNetworkGatewayResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L33">interface GetVirtualNetworkGatewayResult</a>
</h2>

A collection of values returned by getVirtualNetworkGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L37">property activeActive</a>
</h3>

```typescript
activeActive: boolean;
```


(Optional) Is this an Active-Active Gateway?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L38">property bgpSettings</a>
</h3>

```typescript
bgpSettings: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L45">property defaultLocalNetworkGatewayId</a>
</h3>

```typescript
defaultLocalNetworkGatewayId: string;
```


The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L50">property enableBgp</a>
</h3>

```typescript
enableBgp: boolean;
```


Will BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L82">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L54">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: { ... }[];
```


One or two `ip_configuration` blocks documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L58">property location</a>
</h3>

```typescript
location: string;
```


The location/region where the Virtual Network Gateway is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L62">property sku</a>
</h3>

```typescript
sku: string;
```


Configuration of the size and capacity of the Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L66">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L70">property type</a>
</h3>

```typescript
type: string;
```


The type of the Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L74">property vpnClientConfigurations</a>
</h3>

```typescript
vpnClientConfigurations: { ... }[];
```


A `vpn_client_configuration` block which is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L78">property vpnType</a>
</h3>

```typescript
vpnType: string;
```


The routing type of the Virtual Network Gateway.

<h2 class="pdoc-module-header" id="GetVirtualNetworkResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L33">interface GetVirtualNetworkResult</a>
</h2>

A collection of values returned by getVirtualNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L37">property addressSpaces</a>
</h3>

```typescript
addressSpaces: string[];
```


The list of address spaces used by the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L41">property dnsServers</a>
</h3>

```typescript
dnsServers: string[];
```


The list of DNS servers used by the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L53">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L45">property subnets</a>
</h3>

```typescript
subnets: string[];
```


The list of name of the subnets that are attached to this virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L49">property vnetPeerings</a>
</h3>

```typescript
vnetPeerings: { ... };
```


A mapping of name - virtual network id of the virtual network peerings.

<h2 class="pdoc-module-header" id="LocalNetworkGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L145">interface LocalNetworkGatewayArgs</a>
</h2>

The set of arguments for constructing a LocalNetworkGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L150">property addressSpaces</a>
</h3>

```typescript
addressSpaces: pulumi.Input<pulumi.Input<string>[]>;
```


The list of string CIDRs representing the
address spaces the gateway exposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L155">property bgpSettings</a>
</h3>

```typescript
bgpSettings?: pulumi.Input<{ ... }>;
```


A `bgp_settings` block as defined below containing the
Local Network Gateway's BGP speaker settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L160">property gatewayAddress</a>
</h3>

```typescript
gatewayAddress: pulumi.Input<string>;
```


The IP address of the gateway to which to
connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L165">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the local network gateway is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L170">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the local network gateway. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L175">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the local network gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L179">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LocalNetworkGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L105">interface LocalNetworkGatewayState</a>
</h2>

Input properties used for looking up and filtering LocalNetworkGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L110">property addressSpaces</a>
</h3>

```typescript
addressSpaces?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of string CIDRs representing the
address spaces the gateway exposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L115">property bgpSettings</a>
</h3>

```typescript
bgpSettings?: pulumi.Input<{ ... }>;
```


A `bgp_settings` block as defined below containing the
Local Network Gateway's BGP speaker settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L120">property gatewayAddress</a>
</h3>

```typescript
gatewayAddress?: pulumi.Input<string>;
```


The IP address of the gateway to which to
connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L125">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the local network gateway is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the local network gateway. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L135">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the local network gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L139">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L214">interface NetworkInterfaceArgs</a>
</h2>

The set of arguments for constructing a NetworkInterface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L218">property appliedDnsServers</a>
</h3>

```typescript
appliedDnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L222">property dnsServers</a>
</h3>

```typescript
dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of DNS servers IP addresses to use for this NIC, overrides the VNet-level server list

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L226">property enableAcceleratedNetworking</a>
</h3>

```typescript
enableAcceleratedNetworking?: pulumi.Input<boolean>;
```


Enables Azure Accelerated Networking using SR-IOV. Only certain VM instance sizes are supported. Refer to [Create a Virtual Machine with Accelerated Networking](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli). Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L230">property enableIpForwarding</a>
</h3>

```typescript
enableIpForwarding?: pulumi.Input<boolean>;
```


Enables IP Forwarding on the NIC. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L234">property internalDnsNameLabel</a>
</h3>

```typescript
internalDnsNameLabel?: pulumi.Input<string>;
```


Relative DNS name for this NIC used for internal communications between VMs in the same VNet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L238">property internalFqdn</a>
</h3>

```typescript
internalFqdn?: pulumi.Input<string>;
```


Fully qualified DNS name supporting internal communications between VMs in the same VNet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L242">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `ip_configuration` associated with this NIC as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L246">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the network interface is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L250">property macAddress</a>
</h3>

```typescript
macAddress?: pulumi.Input<string>;
```


The media access control (MAC) address of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L254">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


User-defined name of the IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L258">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId?: pulumi.Input<string>;
```


The ID of the Network Security Group to associate with the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L262">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the network interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L266">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L270">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId?: pulumi.Input<string>;
```


Reference to a VM with which this NIC has been associated.

<h2 class="pdoc-module-header" id="NetworkInterfaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L147">interface NetworkInterfaceState</a>
</h2>

Input properties used for looking up and filtering NetworkInterface resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L151">property appliedDnsServers</a>
</h3>

```typescript
appliedDnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L155">property dnsServers</a>
</h3>

```typescript
dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of DNS servers IP addresses to use for this NIC, overrides the VNet-level server list

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L159">property enableAcceleratedNetworking</a>
</h3>

```typescript
enableAcceleratedNetworking?: pulumi.Input<boolean>;
```


Enables Azure Accelerated Networking using SR-IOV. Only certain VM instance sizes are supported. Refer to [Create a Virtual Machine with Accelerated Networking](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli). Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L163">property enableIpForwarding</a>
</h3>

```typescript
enableIpForwarding?: pulumi.Input<boolean>;
```


Enables IP Forwarding on the NIC. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L167">property internalDnsNameLabel</a>
</h3>

```typescript
internalDnsNameLabel?: pulumi.Input<string>;
```


Relative DNS name for this NIC used for internal communications between VMs in the same VNet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L171">property internalFqdn</a>
</h3>

```typescript
internalFqdn?: pulumi.Input<string>;
```


Fully qualified DNS name supporting internal communications between VMs in the same VNet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L175">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `ip_configuration` associated with this NIC as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L179">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the network interface is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L183">property macAddress</a>
</h3>

```typescript
macAddress?: pulumi.Input<string>;
```


The media access control (MAC) address of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L187">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


User-defined name of the IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L191">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId?: pulumi.Input<string>;
```


The ID of the Network Security Group to associate with the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L195">property privateIpAddress</a>
</h3>

```typescript
privateIpAddress?: pulumi.Input<string>;
```


Static IP Address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L196">property privateIpAddresses</a>
</h3>

```typescript
privateIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L200">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the network interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L204">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L208">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId?: pulumi.Input<string>;
```


Reference to a VM with which this NIC has been associated.

<h2 class="pdoc-module-header" id="NetworkSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L111">interface NetworkSecurityGroupArgs</a>
</h2>

The set of arguments for constructing a NetworkSecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L115">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the security rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L123">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L127">property securityRules</a>
</h3>

```typescript
securityRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `security_rule` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L131">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkSecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L85">interface NetworkSecurityGroupState</a>
</h2>

Input properties used for looking up and filtering NetworkSecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L89">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the security rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L97">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L101">property securityRules</a>
</h3>

```typescript
securityRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `security_rule` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L105">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkSecurityRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L253">interface NetworkSecurityRuleArgs</a>
</h2>

The set of arguments for constructing a NetworkSecurityRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L257">property access</a>
</h3>

```typescript
access: pulumi.Input<string>;
```


Specifies whether network traffic is allowed or denied. Possible values are `Allow` and `Deny`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L261">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this rule. Restricted to 140 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L265">property destinationAddressPrefix</a>
</h3>

```typescript
destinationAddressPrefix?: pulumi.Input<string>;
```


CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `destination_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L269">property destinationAddressPrefixes</a>
</h3>

```typescript
destinationAddressPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of destination address prefixes. Tags may not be used. This is required if `destination_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L273">property destinationApplicationSecurityGroupIds</a>
</h3>

```typescript
destinationApplicationSecurityGroupIds?: pulumi.Input<string>;
```


A List of destination Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L277">property destinationPortRange</a>
</h3>

```typescript
destinationPortRange?: pulumi.Input<string>;
```


Destination Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `destination_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L281">property destinationPortRanges</a>
</h3>

```typescript
destinationPortRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


List of destination ports or port ranges. This is required if `destination_port_range` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L285">property direction</a>
</h3>

```typescript
direction: pulumi.Input<string>;
```


The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are `Inbound` and `Outbound`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L289">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L293">property networkSecurityGroupName</a>
</h3>

```typescript
networkSecurityGroupName: pulumi.Input<string>;
```


The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L297">property priority</a>
</h3>

```typescript
priority: pulumi.Input<number>;
```


Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L301">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


Network protocol this rule applies to. Possible values include `Tcp`, `Udp` or `*` (which matches both).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L305">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L309">property sourceAddressPrefix</a>
</h3>

```typescript
sourceAddressPrefix?: pulumi.Input<string>;
```


CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `source_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L313">property sourceAddressPrefixes</a>
</h3>

```typescript
sourceAddressPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of source address prefixes. Tags may not be used. This is required if `source_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L317">property sourceApplicationSecurityGroupIds</a>
</h3>

```typescript
sourceApplicationSecurityGroupIds?: pulumi.Input<string>;
```


A List of source Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L321">property sourcePortRange</a>
</h3>

```typescript
sourcePortRange?: pulumi.Input<string>;
```


Source Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `source_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L325">property sourcePortRanges</a>
</h3>

```typescript
sourcePortRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


List of source ports or port ranges. This is required if `source_port_range` is not specified.

<h2 class="pdoc-module-header" id="NetworkSecurityRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L175">interface NetworkSecurityRuleState</a>
</h2>

Input properties used for looking up and filtering NetworkSecurityRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L179">property access</a>
</h3>

```typescript
access?: pulumi.Input<string>;
```


Specifies whether network traffic is allowed or denied. Possible values are `Allow` and `Deny`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L183">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this rule. Restricted to 140 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L187">property destinationAddressPrefix</a>
</h3>

```typescript
destinationAddressPrefix?: pulumi.Input<string>;
```


CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `destination_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L191">property destinationAddressPrefixes</a>
</h3>

```typescript
destinationAddressPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of destination address prefixes. Tags may not be used. This is required if `destination_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L195">property destinationApplicationSecurityGroupIds</a>
</h3>

```typescript
destinationApplicationSecurityGroupIds?: pulumi.Input<string>;
```


A List of destination Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L199">property destinationPortRange</a>
</h3>

```typescript
destinationPortRange?: pulumi.Input<string>;
```


Destination Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `destination_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L203">property destinationPortRanges</a>
</h3>

```typescript
destinationPortRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


List of destination ports or port ranges. This is required if `destination_port_range` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L207">property direction</a>
</h3>

```typescript
direction?: pulumi.Input<string>;
```


The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are `Inbound` and `Outbound`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L211">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L215">property networkSecurityGroupName</a>
</h3>

```typescript
networkSecurityGroupName?: pulumi.Input<string>;
```


The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L219">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L223">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


Network protocol this rule applies to. Possible values include `Tcp`, `Udp` or `*` (which matches both).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L227">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L231">property sourceAddressPrefix</a>
</h3>

```typescript
sourceAddressPrefix?: pulumi.Input<string>;
```


CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `source_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L235">property sourceAddressPrefixes</a>
</h3>

```typescript
sourceAddressPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of source address prefixes. Tags may not be used. This is required if `source_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L239">property sourceApplicationSecurityGroupIds</a>
</h3>

```typescript
sourceApplicationSecurityGroupIds?: pulumi.Input<string>;
```


A List of source Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L243">property sourcePortRange</a>
</h3>

```typescript
sourcePortRange?: pulumi.Input<string>;
```


Source Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `source_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L247">property sourcePortRanges</a>
</h3>

```typescript
sourcePortRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


List of source ports or port ranges. This is required if `source_port_range` is not specified.

<h2 class="pdoc-module-header" id="NetworkWatcherArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L97">interface NetworkWatcherArgs</a>
</h2>

The set of arguments for constructing a NetworkWatcher resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L101">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L109">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L113">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkWatcherState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L75">interface NetworkWatcherState</a>
</h2>

Input properties used for looking up and filtering NetworkWatcher resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L79">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L83">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L87">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L91">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="PacketCaptureArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L153">interface PacketCaptureArgs</a>
</h2>

The set of arguments for constructing a PacketCapture resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L157">property filters</a>
</h3>

```typescript
filters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `filter` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L161">property maximumBytesPerPacket</a>
</h3>

```typescript
maximumBytesPerPacket?: pulumi.Input<number>;
```


The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L165">property maximumBytesPerSession</a>
</h3>

```typescript
maximumBytesPerSession?: pulumi.Input<number>;
```


Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L169">property maximumCaptureDuration</a>
</h3>

```typescript
maximumCaptureDuration?: pulumi.Input<number>;
```


The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L173">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for this Packet Capture. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L177">property networkWatcherName</a>
</h3>

```typescript
networkWatcherName: pulumi.Input<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L181">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L185">property storageLocation</a>
</h3>

```typescript
storageLocation: pulumi.Input<{ ... }>;
```


A `storage_location` block as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L189">property targetResourceId</a>
</h3>

```typescript
targetResourceId: pulumi.Input<string>;
```


The ID of the Resource to capture packets from. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PacketCaptureState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L111">interface PacketCaptureState</a>
</h2>

Input properties used for looking up and filtering PacketCapture resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L115">property filters</a>
</h3>

```typescript
filters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `filter` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L119">property maximumBytesPerPacket</a>
</h3>

```typescript
maximumBytesPerPacket?: pulumi.Input<number>;
```


The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L123">property maximumBytesPerSession</a>
</h3>

```typescript
maximumBytesPerSession?: pulumi.Input<number>;
```


Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L127">property maximumCaptureDuration</a>
</h3>

```typescript
maximumCaptureDuration?: pulumi.Input<number>;
```


The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L131">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for this Packet Capture. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L135">property networkWatcherName</a>
</h3>

```typescript
networkWatcherName?: pulumi.Input<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L139">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L143">property storageLocation</a>
</h3>

```typescript
storageLocation?: pulumi.Input<{ ... }>;
```


A `storage_location` block as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L147">property targetResourceId</a>
</h3>

```typescript
targetResourceId?: pulumi.Input<string>;
```


The ID of the Resource to capture packets from. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PublicIpArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L184">interface PublicIpArgs</a>
</h2>

The set of arguments for constructing a PublicIp resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L188">property domainNameLabel</a>
</h3>

```typescript
domainNameLabel?: pulumi.Input<string>;
```


Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L192">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes?: pulumi.Input<number>;
```


Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L196">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L201">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L205">property publicIpAddressAllocation</a>
</h3>

```typescript
publicIpAddressAllocation: pulumi.Input<string>;
```


Defines whether the IP address is static or dynamic. Options are Static or Dynamic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L210">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the public ip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L214">property reverseFqdn</a>
</h3>

```typescript
reverseFqdn?: pulumi.Input<string>;
```


A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L218">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU of the Public IP. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L222">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L226">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<string>;
```


A collection containing the availability zone to allocate the Public IP in.

<h2 class="pdoc-module-header" id="PublicIpState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L128">interface PublicIpState</a>
</h2>

Input properties used for looking up and filtering PublicIp resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L132">property domainNameLabel</a>
</h3>

```typescript
domainNameLabel?: pulumi.Input<string>;
```


Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L136">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L140">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes?: pulumi.Input<number>;
```


Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L144">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address value that was allocated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L148">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L153">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L157">property publicIpAddressAllocation</a>
</h3>

```typescript
publicIpAddressAllocation?: pulumi.Input<string>;
```


Defines whether the IP address is static or dynamic. Options are Static or Dynamic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L162">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the public ip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L166">property reverseFqdn</a>
</h3>

```typescript
reverseFqdn?: pulumi.Input<string>;
```


A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L170">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU of the Public IP. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L174">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L178">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<string>;
```


A collection containing the availability zone to allocate the Public IP in.

<h2 class="pdoc-module-header" id="RouteArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L123">interface RouteArgs</a>
</h2>

The set of arguments for constructing a Route resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L127">property addressPrefix</a>
</h3>

```typescript
addressPrefix: pulumi.Input<string>;
```


The destination CIDR to which the route applies, such as `10.1.0.0/16`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L131">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L135">property nextHopInIpAddress</a>
</h3>

```typescript
nextHopInIpAddress?: pulumi.Input<string>;
```


Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is `VirtualAppliance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L139">property nextHopType</a>
</h3>

```typescript
nextHopType: pulumi.Input<string>;
```


The type of Azure hop the packet should be sent to. Possible values are `VirtualNetworkGateway`, `VnetLocal`, `Internet`, `VirtualAppliance` and `None`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L143">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L147">property routeTableName</a>
</h3>

```typescript
routeTableName: pulumi.Input<string>;
```


The name of the route table within which create the route. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="RouteState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L93">interface RouteState</a>
</h2>

Input properties used for looking up and filtering Route resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L97">property addressPrefix</a>
</h3>

```typescript
addressPrefix?: pulumi.Input<string>;
```


The destination CIDR to which the route applies, such as `10.1.0.0/16`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L105">property nextHopInIpAddress</a>
</h3>

```typescript
nextHopInIpAddress?: pulumi.Input<string>;
```


Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is `VirtualAppliance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L109">property nextHopType</a>
</h3>

```typescript
nextHopType?: pulumi.Input<string>;
```


The type of Azure hop the packet should be sent to. Possible values are `VirtualNetworkGateway`, `VnetLocal`, `Internet`, `VirtualAppliance` and `None`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L113">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L117">property routeTableName</a>
</h3>

```typescript
routeTableName?: pulumi.Input<string>;
```


The name of the route table within which create the route. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="RouteTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L127">interface RouteTableArgs</a>
</h2>

The set of arguments for constructing a RouteTable resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L131">property disableBgpRoutePropagation</a>
</h3>

```typescript
disableBgpRoutePropagation?: pulumi.Input<boolean>;
```


Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L135">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L143">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the route table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L147">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to define multiple routes. Each `route` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L151">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="RouteTableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L93">interface RouteTableState</a>
</h2>

Input properties used for looking up and filtering RouteTable resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L97">property disableBgpRoutePropagation</a>
</h3>

```typescript
disableBgpRoutePropagation?: pulumi.Input<boolean>;
```


Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L101">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L109">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the route table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L113">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to define multiple routes. Each `route` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L117">property subnets</a>
</h3>

```typescript
subnets?: pulumi.Input<pulumi.Input<string>[]>;
```


The collection of Subnets associated with this route table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L121">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SubnetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L144">interface SubnetArgs</a>
</h2>

The set of arguments for constructing a Subnet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L148">property addressPrefix</a>
</h3>

```typescript
addressPrefix: pulumi.Input<string>;
```


The address prefix to use for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L152">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations?: pulumi.Input<pulumi.Input<string>[]>;
```


The collection of IP Configurations with IPs within this subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L160">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId?: pulumi.Input<string>;
```


The ID of the Network Security Group to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L164">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L168">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The ID of the Route Table to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L172">property serviceEndpoints</a>
</h3>

```typescript
serviceEndpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of Service endpoints to associate with the subnet. Possible values include: `Microsoft.Storage`, `Microsoft.Sql`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L176">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName: pulumi.Input<string>;
```


The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubnetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L106">interface SubnetState</a>
</h2>

Input properties used for looking up and filtering Subnet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L110">property addressPrefix</a>
</h3>

```typescript
addressPrefix?: pulumi.Input<string>;
```


The address prefix to use for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L114">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations?: pulumi.Input<pulumi.Input<string>[]>;
```


The collection of IP Configurations with IPs within this subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L122">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId?: pulumi.Input<string>;
```


The ID of the Network Security Group to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L126">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L130">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The ID of the Route Table to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L134">property serviceEndpoints</a>
</h3>

```typescript
serviceEndpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of Service endpoints to associate with the subnet. Possible values include: `Microsoft.Storage`, `Microsoft.Sql`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L138">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName?: pulumi.Input<string>;
```


The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L145">interface VirtualNetworkArgs</a>
</h2>

The set of arguments for constructing a VirtualNetwork resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L151">property addressSpaces</a>
</h3>

```typescript
addressSpaces: pulumi.Input<pulumi.Input<string>[]>;
```


The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L155">property dnsServers</a>
</h3>

```typescript
dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IP addresses of DNS servers

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L160">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the virtual network is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L164">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L169">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L174">property subnets</a>
</h3>

```typescript
subnets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to define multiple
subnets. Each `subnet` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L178">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L234">interface VirtualNetworkGatewayArgs</a>
</h2>

The set of arguments for constructing a VirtualNetworkGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L241">property activeActive</a>
</h3>

```typescript
activeActive?: pulumi.Input<boolean>;
```


If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L242">property bgpSettings</a>
</h3>

```typescript
bgpSettings?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L250">property defaultLocalNetworkGatewayId</a>
</h3>

```typescript
defaultLocalNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L255">property enableBgp</a>
</h3>

```typescript
enableBgp?: pulumi.Input<boolean>;
```


If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L261">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L266">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L270">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-defined name of the revoked certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L276">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L284">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`VpnGw1`, `VpnGw2` and `VpnGw3` and depend on the `type` and `vpn_type` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L288">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L293">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L299">property vpnClientConfiguration</a>
</h3>

```typescript
vpnClientConfiguration?: pulumi.Input<{ ... }>;
```


A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L304">property vpnType</a>
</h3>

```typescript
vpnType?: pulumi.Input<string>;
```


The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayConnectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L261">interface VirtualNetworkGatewayConnectionArgs</a>
</h2>

The set of arguments for constructing a VirtualNetworkGatewayConnection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L267">property authorizationKey</a>
</h3>

```typescript
authorizationKey?: pulumi.Input<string>;
```


The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L272">property enableBgp</a>
</h3>

```typescript
enableBgp?: pulumi.Input<boolean>;
```


If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L278">property expressRouteCircuitId</a>
</h3>

```typescript
expressRouteCircuitId?: pulumi.Input<string>;
```


The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L284">property ipsecPolicy</a>
</h3>

```typescript
ipsecPolicy?: pulumi.Input<{ ... }>;
```


A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L289">property localNetworkGatewayId</a>
</h3>

```typescript
localNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L294">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the connection is
located. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L299">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection. Changing the name forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L306">property peerVirtualNetworkGatewayId</a>
</h3>

```typescript
peerVirtualNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L311">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L315">property routingWeight</a>
</h3>

```typescript
routingWeight?: pulumi.Input<number>;
```


The routing weight. Defaults to `10`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L321">property sharedKey</a>
</h3>

```typescript
sharedKey?: pulumi.Input<string>;
```


The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L325">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L333">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L339">property usePolicyBasedTrafficSelectors</a>
</h3>

```typescript
usePolicyBasedTrafficSelectors?: pulumi.Input<boolean>;
```


If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L345">property virtualNetworkGatewayId</a>
</h3>

```typescript
virtualNetworkGatewayId: pulumi.Input<string>;
```


The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayConnectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L171">interface VirtualNetworkGatewayConnectionState</a>
</h2>

Input properties used for looking up and filtering VirtualNetworkGatewayConnection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L177">property authorizationKey</a>
</h3>

```typescript
authorizationKey?: pulumi.Input<string>;
```


The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L182">property enableBgp</a>
</h3>

```typescript
enableBgp?: pulumi.Input<boolean>;
```


If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L188">property expressRouteCircuitId</a>
</h3>

```typescript
expressRouteCircuitId?: pulumi.Input<string>;
```


The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L194">property ipsecPolicy</a>
</h3>

```typescript
ipsecPolicy?: pulumi.Input<{ ... }>;
```


A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L199">property localNetworkGatewayId</a>
</h3>

```typescript
localNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L204">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the connection is
located. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L209">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection. Changing the name forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L216">property peerVirtualNetworkGatewayId</a>
</h3>

```typescript
peerVirtualNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L221">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L225">property routingWeight</a>
</h3>

```typescript
routingWeight?: pulumi.Input<number>;
```


The routing weight. Defaults to `10`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L231">property sharedKey</a>
</h3>

```typescript
sharedKey?: pulumi.Input<string>;
```


The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L235">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L243">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L249">property usePolicyBasedTrafficSelectors</a>
</h3>

```typescript
usePolicyBasedTrafficSelectors?: pulumi.Input<boolean>;
```


If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L255">property virtualNetworkGatewayId</a>
</h3>

```typescript
virtualNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L158">interface VirtualNetworkGatewayState</a>
</h2>

Input properties used for looking up and filtering VirtualNetworkGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L165">property activeActive</a>
</h3>

```typescript
activeActive?: pulumi.Input<boolean>;
```


If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L166">property bgpSettings</a>
</h3>

```typescript
bgpSettings?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L174">property defaultLocalNetworkGatewayId</a>
</h3>

```typescript
defaultLocalNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L179">property enableBgp</a>
</h3>

```typescript
enableBgp?: pulumi.Input<boolean>;
```


If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L185">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L190">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L194">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-defined name of the revoked certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L200">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L208">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`VpnGw1`, `VpnGw2` and `VpnGw3` and depend on the `type` and `vpn_type` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L212">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L217">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L223">property vpnClientConfiguration</a>
</h3>

```typescript
vpnClientConfiguration?: pulumi.Input<{ ... }>;
```


A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L228">property vpnType</a>
</h3>

```typescript
vpnType?: pulumi.Input<string>;
```


The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.

<h2 class="pdoc-module-header" id="VirtualNetworkPeeringArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L169">interface VirtualNetworkPeeringArgs</a>
</h2>

The set of arguments for constructing a VirtualNetworkPeering resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L174">property allowForwardedTraffic</a>
</h3>

```typescript
allowForwardedTraffic?: pulumi.Input<boolean>;
```


Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L179">property allowGatewayTransit</a>
</h3>

```typescript
allowGatewayTransit?: pulumi.Input<boolean>;
```


Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L185">property allowVirtualNetworkAccess</a>
</h3>

```typescript
allowVirtualNetworkAccess?: pulumi.Input<boolean>;
```


Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L190">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual network peering. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L195">property remoteVirtualNetworkId</a>
</h3>

```typescript
remoteVirtualNetworkId: pulumi.Input<string>;
```


The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L201">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L210">property useRemoteGateways</a>
</h3>

```typescript
useRemoteGateways?: pulumi.Input<boolean>;
```


Controls if remote gateways can be used on
the local virtual network. If the flag is set to `true`, and
`allow_gateway_transit` on the remote peering is also `true`, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to `true`. This flag cannot be set if virtual network
already has a gateway. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L215">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName: pulumi.Input<string>;
```


The name of the virtual network. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkPeeringState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L117">interface VirtualNetworkPeeringState</a>
</h2>

Input properties used for looking up and filtering VirtualNetworkPeering resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L122">property allowForwardedTraffic</a>
</h3>

```typescript
allowForwardedTraffic?: pulumi.Input<boolean>;
```


Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L127">property allowGatewayTransit</a>
</h3>

```typescript
allowGatewayTransit?: pulumi.Input<boolean>;
```


Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L133">property allowVirtualNetworkAccess</a>
</h3>

```typescript
allowVirtualNetworkAccess?: pulumi.Input<boolean>;
```


Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L138">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual network peering. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L143">property remoteVirtualNetworkId</a>
</h3>

```typescript
remoteVirtualNetworkId?: pulumi.Input<string>;
```


The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L149">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L158">property useRemoteGateways</a>
</h3>

```typescript
useRemoteGateways?: pulumi.Input<boolean>;
```


Controls if remote gateways can be used on
the local virtual network. If the flag is set to `true`, and
`allow_gateway_transit` on the remote peering is also `true`, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to `true`. This flag cannot be set if virtual network
already has a gateway. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L163">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName?: pulumi.Input<string>;
```


The name of the virtual network. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L106">interface VirtualNetworkState</a>
</h2>

Input properties used for looking up and filtering VirtualNetwork resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L112">property addressSpaces</a>
</h3>

```typescript
addressSpaces?: pulumi.Input<pulumi.Input<string>[]>;
```


The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L116">property dnsServers</a>
</h3>

```typescript
dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IP addresses of DNS servers

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L121">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the virtual network is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L135">property subnets</a>
</h3>

```typescript
subnets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to define multiple
subnets. Each `subnet` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L139">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

