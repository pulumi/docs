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
* <a href="#Firewall">class Firewall</a>
* <a href="#FirewallNetworkRuleCollection">class FirewallNetworkRuleCollection</a>
* <a href="#LocalNetworkGateway">class LocalNetworkGateway</a>
* <a href="#NetworkInterface">class NetworkInterface</a>
* <a href="#NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation">class NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation</a>
* <a href="#NetworkInterfaceBackendAddressPoolAssociation">class NetworkInterfaceBackendAddressPoolAssociation</a>
* <a href="#NetworkInterfaceNatRuleAssociation">class NetworkInterfaceNatRuleAssociation</a>
* <a href="#NetworkSecurityGroup">class NetworkSecurityGroup</a>
* <a href="#NetworkSecurityRule">class NetworkSecurityRule</a>
* <a href="#NetworkWatcher">class NetworkWatcher</a>
* <a href="#PacketCapture">class PacketCapture</a>
* <a href="#PublicIp">class PublicIp</a>
* <a href="#Route">class Route</a>
* <a href="#RouteTable">class RouteTable</a>
* <a href="#Subnet">class Subnet</a>
* <a href="#SubnetNetworkSecurityGroupAssociation">class SubnetNetworkSecurityGroupAssociation</a>
* <a href="#SubnetRouteTableAssociation">class SubnetRouteTableAssociation</a>
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
* <a href="#FirewallArgs">interface FirewallArgs</a>
* <a href="#FirewallNetworkRuleCollectionArgs">interface FirewallNetworkRuleCollectionArgs</a>
* <a href="#FirewallNetworkRuleCollectionState">interface FirewallNetworkRuleCollectionState</a>
* <a href="#FirewallState">interface FirewallState</a>
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
* <a href="#NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationArgs">interface NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationArgs</a>
* <a href="#NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationState">interface NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationState</a>
* <a href="#NetworkInterfaceArgs">interface NetworkInterfaceArgs</a>
* <a href="#NetworkInterfaceBackendAddressPoolAssociationArgs">interface NetworkInterfaceBackendAddressPoolAssociationArgs</a>
* <a href="#NetworkInterfaceBackendAddressPoolAssociationState">interface NetworkInterfaceBackendAddressPoolAssociationState</a>
* <a href="#NetworkInterfaceNatRuleAssociationArgs">interface NetworkInterfaceNatRuleAssociationArgs</a>
* <a href="#NetworkInterfaceNatRuleAssociationState">interface NetworkInterfaceNatRuleAssociationState</a>
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
* <a href="#SubnetNetworkSecurityGroupAssociationArgs">interface SubnetNetworkSecurityGroupAssociationArgs</a>
* <a href="#SubnetNetworkSecurityGroupAssociationState">interface SubnetNetworkSecurityGroupAssociationState</a>
* <a href="#SubnetRouteTableAssociationArgs">interface SubnetRouteTableAssociationArgs</a>
* <a href="#SubnetRouteTableAssociationState">interface SubnetRouteTableAssociationState</a>
* <a href="#SubnetState">interface SubnetState</a>
* <a href="#VirtualNetworkArgs">interface VirtualNetworkArgs</a>
* <a href="#VirtualNetworkGatewayArgs">interface VirtualNetworkGatewayArgs</a>
* <a href="#VirtualNetworkGatewayConnectionArgs">interface VirtualNetworkGatewayConnectionArgs</a>
* <a href="#VirtualNetworkGatewayConnectionState">interface VirtualNetworkGatewayConnectionState</a>
* <a href="#VirtualNetworkGatewayState">interface VirtualNetworkGatewayState</a>
* <a href="#VirtualNetworkPeeringArgs">interface VirtualNetworkPeeringArgs</a>
* <a href="#VirtualNetworkPeeringState">interface VirtualNetworkPeeringState</a>
* <a href="#VirtualNetworkState">interface VirtualNetworkState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts">network/applicationGateway.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts">network/applicationSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts">network/expressRouteCircuit.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts">network/expressRouteCircuitAuthorization.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts">network/expressRouteCircuitPeering.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts">network/firewall.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts">network/firewallNetworkRuleCollection.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts">network/getApplicationSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts">network/getNetworkInterface.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts">network/getNetworkSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts">network/getPublicIP.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts">network/getPublicIPs.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts">network/getRouteTable.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts">network/getSubnet.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts">network/getVirtualNetwork.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts">network/getVirtualNetworkGateway.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts">network/localNetworkGateway.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts">network/networkInterface.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts">network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts">network/networkInterfaceBackendAddressPoolAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts">network/networkInterfaceNatRuleAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts">network/networkSecurityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts">network/networkSecurityRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts">network/networkWatcher.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts">network/packetCapture.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts">network/publicIp.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts">network/route.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts">network/routeTable.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts">network/subnet.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts">network/subnetNetworkSecurityGroupAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts">network/subnetRouteTableAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts">network/virtualNetwork.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts">network/virtualNetworkGateway.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts">network/virtualNetworkGatewayConnection.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts">network/virtualNetworkPeering.ts</a> 


<h2 class="pdoc-module-header" id="ApplicationGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L7">class ApplicationGateway</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L37">constructor</a>
</h3>

```typescript
new ApplicationGateway(name: string, args: ApplicationGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ApplicationGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L16">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L20">property authenticationCertificates</a>
</h3>

```typescript
public authenticationCertificates: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L21">property backendAddressPools</a>
</h3>

```typescript
public backendAddressPools: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L22">property backendHttpSettings</a>
</h3>

```typescript
public backendHttpSettings: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L23">property disabledSslProtocols</a>
</h3>

```typescript
public disabledSslProtocols: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L24">property frontendIpConfigurations</a>
</h3>

```typescript
public frontendIpConfigurations: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L25">property frontendPorts</a>
</h3>

```typescript
public frontendPorts: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L26">property gatewayIpConfigurations</a>
</h3>

```typescript
public gatewayIpConfigurations: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L27">property httpListeners</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L28">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L30">property probes</a>
</h3>

```typescript
public probes: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L31">property requestRoutingRules</a>
</h3>

```typescript
public requestRoutingRules: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L32">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L33">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L34">property sslCertificates</a>
</h3>

```typescript
public sslCertificates: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L35">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L36">property urlPathMaps</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L37">property wafConfiguration</a>
</h3>

```typescript
public wafConfiguration: pulumi.Output<{ ... } | undefined>;
```

<h2 class="pdoc-module-header" id="ApplicationSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L10">class ApplicationSecurityGroup</a>
</h2>

Manage an Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L38">constructor</a>
</h3>

```typescript
new ApplicationSecurityGroup(name: string, args: ApplicationSecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ApplicationSecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Application Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L38">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L10">class ExpressRouteCircuit</a>
</h2>

Manages an ExpressRoute circuit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L66">constructor</a>
</h3>

```typescript
new ExpressRouteCircuit(name: string, args: ExpressRouteCircuitArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ExpressRouteCircuit resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L26">property allowClassicOperations</a>
</h3>

```typescript
public allowClassicOperations: pulumi.Output<boolean | undefined>;
```


Allow the circuit to interact with classic (RDFE) resources. The default value is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L30">property bandwidthInMbps</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L34">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L42">property peeringLocation</a>
</h3>

```typescript
public peeringLocation: pulumi.Output<string>;
```


The name of the peering location and **not** the Azure resource location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L46">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L50">property serviceKey</a>
</h3>

```typescript
public serviceKey: pulumi.Output<string>;
```


The string needed by the service provider to provision the ExpressRoute circuit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L54">property serviceProviderName</a>
</h3>

```typescript
public serviceProviderName: pulumi.Output<string>;
```


The name of the ExpressRoute Service Provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L58">property serviceProviderProvisioningState</a>
</h3>

```typescript
public serviceProviderProvisioningState: pulumi.Output<string>;
```


The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L62">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block for the ExpressRoute circuit as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L66">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L10">class ExpressRouteCircuitAuthorization</a>
</h2>

Manages an ExpressRoute Circuit Authorization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L44">constructor</a>
</h3>

```typescript
new ExpressRouteCircuitAuthorization(name: string, args: ExpressRouteCircuitAuthorizationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ExpressRouteCircuitAuthorization resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L26">property authorizationKey</a>
</h3>

```typescript
public authorizationKey: pulumi.Output<string>;
```


The Authorization Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L30">property authorizationUseStatus</a>
</h3>

```typescript
public authorizationUseStatus: pulumi.Output<string>;
```


The authorization use status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L34">property expressRouteCircuitName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L44">property resourceGroupName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L10">class ExpressRouteCircuitPeering</a>
</h2>

Manages an ExpressRoute Circuit Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L71">constructor</a>
</h3>

```typescript
new ExpressRouteCircuitPeering(name: string, args: ExpressRouteCircuitPeeringArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ExpressRouteCircuitPeering resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L26">property azureAsn</a>
</h3>

```typescript
public azureAsn: pulumi.Output<number>;
```


The ASN used by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L30">property expressRouteCircuitName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L34">property microsoftPeeringConfig</a>
</h3>

```typescript
public microsoftPeeringConfig: pulumi.Output<{ ... } | undefined>;
```


A `microsoft_peering_config` block as defined below. Required when `peering_type` is set to `MicrosoftPeering`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L38">property peerAsn</a>
</h3>

```typescript
public peerAsn: pulumi.Output<number>;
```


The Either a 16-bit or a 32-bit ASN. Can either be public or private..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L42">property peeringType</a>
</h3>

```typescript
public peeringType: pulumi.Output<string>;
```


The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L46">property primaryAzurePort</a>
</h3>

```typescript
public primaryAzurePort: pulumi.Output<string>;
```


The Primary Port used by Azure for this Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L50">property primaryPeerAddressPrefix</a>
</h3>

```typescript
public primaryPeerAddressPrefix: pulumi.Output<string>;
```


A `/30` subnet for the primary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L55">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L59">property secondaryAzurePort</a>
</h3>

```typescript
public secondaryAzurePort: pulumi.Output<string>;
```


The Secondary Port used by Azure for this Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L63">property secondaryPeerAddressPrefix</a>
</h3>

```typescript
public secondaryPeerAddressPrefix: pulumi.Output<string>;
```


A `/30` subnet for the secondary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L67">property sharedKey</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L71">property vlanId</a>
</h3>

```typescript
public vlanId: pulumi.Output<number>;
```


A valid VLAN ID to establish this peering on.

<h2 class="pdoc-module-header" id="Firewall">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L12">class Firewall</a>
</h2>

Manages an Azure Firewall.

-> **NOTE** Azure Firewall is currently in Public Preview.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L44">constructor</a>
</h3>

```typescript
new Firewall(name: string, args: FirewallArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Firewall resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallState): Firewall
```


Get an existing Firewall resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L28">property ipConfiguration</a>
</h3>

```typescript
public ipConfiguration: pulumi.Output<{ ... }>;
```


A `ip_configuration` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L32">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Firewall. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L40">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L44">property tags</a>
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

<h2 class="pdoc-module-header" id="FirewallNetworkRuleCollection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L12">class FirewallNetworkRuleCollection</a>
</h2>

Manages a Network Rule Collection within an Azure Firewall.

-> **NOTE** Azure Firewall is currently in Public Preview.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L48">constructor</a>
</h3>

```typescript
new FirewallNetworkRuleCollection(name: string, args: FirewallNetworkRuleCollectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FirewallNetworkRuleCollection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallNetworkRuleCollectionState): FirewallNetworkRuleCollection
```


Get an existing FirewallNetworkRuleCollection resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L28">property action</a>
</h3>

```typescript
public action: pulumi.Output<string>;
```


Specifies the action the rule will apply to matching traffic. Possible values are `Allow` and `Deny`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L32">property azureFirewallName</a>
</h3>

```typescript
public azureFirewallName: pulumi.Output<string>;
```


Specifies the name of the Firewall in which to the Network Rule Collection should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L40">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<number>;
```


Specifies the priority of the rule collection. Possible values are between `100` - `65000`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L44">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L48">property rules</a>
</h3>

```typescript
public rules: pulumi.Output<{ ... }[]>;
```


One or more `rule` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LocalNetworkGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L10">class LocalNetworkGateway</a>
</h2>

Manages a local network gateway connection over which specific connections can be configured.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L56">constructor</a>
</h3>

```typescript
new LocalNetworkGateway(name: string, args: LocalNetworkGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LocalNetworkGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L27">property addressSpaces</a>
</h3>

```typescript
public addressSpaces: pulumi.Output<string[]>;
```


The list of string CIDRs representing the
address spaces the gateway exposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L32">property bgpSettings</a>
</h3>

```typescript
public bgpSettings: pulumi.Output<{ ... } | undefined>;
```


A `bgp_settings` block as defined below containing the
Local Network Gateway's BGP speaker settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L37">property gatewayAddress</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L42">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the local network gateway is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L47">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the local network gateway. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L52">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the local network gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L56">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L10">class NetworkInterface</a>
</h2>

Manages a Network Interface located in a Virtual Network, usually attached to a Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L80">constructor</a>
</h3>

```typescript
new NetworkInterface(name: string, args: NetworkInterfaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkInterface resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L26">property appliedDnsServers</a>
</h3>

```typescript
public appliedDnsServers: pulumi.Output<string[]>;
```


If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L30">property dnsServers</a>
</h3>

```typescript
public dnsServers: pulumi.Output<string[]>;
```


List of DNS servers IP addresses to use for this NIC, overrides the VNet-level server list

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L34">property enableAcceleratedNetworking</a>
</h3>

```typescript
public enableAcceleratedNetworking: pulumi.Output<boolean | undefined>;
```


Enables Azure Accelerated Networking using SR-IOV. Only certain VM instance sizes are supported. Refer to [Create a Virtual Machine with Accelerated Networking](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli). Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L38">property enableIpForwarding</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L42">property internalDnsNameLabel</a>
</h3>

```typescript
public internalDnsNameLabel: pulumi.Output<string>;
```


Relative DNS name for this NIC used for internal communications between VMs in the same VNet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L43">property internalFqdn</a>
</h3>

```typescript
public internalFqdn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L47">property ipConfigurations</a>
</h3>

```typescript
public ipConfigurations: pulumi.Output<{ ... }[]>;
```


One or more `ip_configuration` associated with this NIC as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L51">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the network interface is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L55">property macAddress</a>
</h3>

```typescript
public macAddress: pulumi.Output<string>;
```


The media access control (MAC) address of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L59">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the network interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L63">property networkSecurityGroupId</a>
</h3>

```typescript
public networkSecurityGroupId: pulumi.Output<string | undefined>;
```


The ID of the Network Security Group to associate with the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L67">property privateIpAddress</a>
</h3>

```typescript
public privateIpAddress: pulumi.Output<string>;
```


The private ip address of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L68">property privateIpAddresses</a>
</h3>

```typescript
public privateIpAddresses: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L72">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the network interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L76">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L80">property virtualMachineId</a>
</h3>

```typescript
public virtualMachineId: pulumi.Output<string>;
```


Reference to a VM with which this NIC has been associated.

<h2 class="pdoc-module-header" id="NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L10">class NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation</a>
</h2>

Manages the association between a Network Interface and a Application Gateway's Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L34">constructor</a>
</h3>

```typescript
new NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation(name: string, args: NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationState): NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation
```


Get an existing NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L26">property backendAddressPoolId</a>
</h3>

```typescript
public backendAddressPoolId: pulumi.Output<string>;
```


The ID of the Application Gateway's Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L30">property ipConfigurationName</a>
</h3>

```typescript
public ipConfigurationName: pulumi.Output<string>;
```


The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L34">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


The ID of the Network Interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NetworkInterfaceBackendAddressPoolAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L10">class NetworkInterfaceBackendAddressPoolAssociation</a>
</h2>

Manages the association between a Network Interface and a Load Balancer's Backend Address Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L34">constructor</a>
</h3>

```typescript
new NetworkInterfaceBackendAddressPoolAssociation(name: string, args: NetworkInterfaceBackendAddressPoolAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkInterfaceBackendAddressPoolAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfaceBackendAddressPoolAssociationState): NetworkInterfaceBackendAddressPoolAssociation
```


Get an existing NetworkInterfaceBackendAddressPoolAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L26">property backendAddressPoolId</a>
</h3>

```typescript
public backendAddressPoolId: pulumi.Output<string>;
```


The ID of the Load Balancer Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L30">property ipConfigurationName</a>
</h3>

```typescript
public ipConfigurationName: pulumi.Output<string>;
```


The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L34">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


The ID of the Network Interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NetworkInterfaceNatRuleAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L10">class NetworkInterfaceNatRuleAssociation</a>
</h2>

Manages the association between a Network Interface and a Load Balancer's NAT Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L34">constructor</a>
</h3>

```typescript
new NetworkInterfaceNatRuleAssociation(name: string, args: NetworkInterfaceNatRuleAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkInterfaceNatRuleAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfaceNatRuleAssociationState): NetworkInterfaceNatRuleAssociation
```


Get an existing NetworkInterfaceNatRuleAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L26">property ipConfigurationName</a>
</h3>

```typescript
public ipConfigurationName: pulumi.Output<string>;
```


The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L30">property natRuleId</a>
</h3>

```typescript
public natRuleId: pulumi.Output<string>;
```


The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L34">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


The ID of the Network Interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NetworkSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L14">class NetworkSecurityGroup</a>
</h2>

Manages a network security group that contains a list of network security rules.  Network security groups enable inbound or outbound traffic to be enabled or denied.

~> **NOTE on Network Security Groups and Network Security Rules:** Terraform currently
provides both a standalone Network Security Rule resource, and allows for Network Security Rules to be defined in-line within the Network Security Group resource.
At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L46">constructor</a>
</h3>

```typescript
new NetworkSecurityGroup(name: string, args: NetworkSecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkSecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the network security group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L42">property securityRules</a>
</h3>

```typescript
public securityRules: pulumi.Output<{ ... }[]>;
```


One or more `security_rule` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L46">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L14">class NetworkSecurityRule</a>
</h2>

Manages a Network Security Rule.

~> **NOTE on Network Security Groups and Network Security Rules:** Terraform currently
provides both a standalone Network Security Rule resource, and allows for Network Security Rules to be defined in-line within the Network Security Group resource.
At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L98">constructor</a>
</h3>

```typescript
new NetworkSecurityRule(name: string, args: NetworkSecurityRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkSecurityRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L30">property access</a>
</h3>

```typescript
public access: pulumi.Output<string>;
```


Specifies whether network traffic is allowed or denied. Possible values are `Allow` and `Deny`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for this rule. Restricted to 140 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L38">property destinationAddressPrefix</a>
</h3>

```typescript
public destinationAddressPrefix: pulumi.Output<string | undefined>;
```


CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `destination_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L42">property destinationAddressPrefixes</a>
</h3>

```typescript
public destinationAddressPrefixes: pulumi.Output<string[] | undefined>;
```


List of destination address prefixes. Tags may not be used. This is required if `destination_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L46">property destinationApplicationSecurityGroupIds</a>
</h3>

```typescript
public destinationApplicationSecurityGroupIds: pulumi.Output<string | undefined>;
```


A List of destination Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L50">property destinationPortRange</a>
</h3>

```typescript
public destinationPortRange: pulumi.Output<string | undefined>;
```


Destination Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `destination_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L54">property destinationPortRanges</a>
</h3>

```typescript
public destinationPortRanges: pulumi.Output<string[] | undefined>;
```


List of destination ports or port ranges. This is required if `destination_port_range` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L58">property direction</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L62">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L66">property networkSecurityGroupName</a>
</h3>

```typescript
public networkSecurityGroupName: pulumi.Output<string>;
```


The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L70">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<number>;
```


Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L74">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


Network protocol this rule applies to. Possible values include `Tcp`, `Udp` or `*` (which matches both).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L78">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L82">property sourceAddressPrefix</a>
</h3>

```typescript
public sourceAddressPrefix: pulumi.Output<string | undefined>;
```


CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `source_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L86">property sourceAddressPrefixes</a>
</h3>

```typescript
public sourceAddressPrefixes: pulumi.Output<string[] | undefined>;
```


List of source address prefixes. Tags may not be used. This is required if `source_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L90">property sourceApplicationSecurityGroupIds</a>
</h3>

```typescript
public sourceApplicationSecurityGroupIds: pulumi.Output<string | undefined>;
```


A List of source Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L94">property sourcePortRange</a>
</h3>

```typescript
public sourcePortRange: pulumi.Output<string | undefined>;
```


Source Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `source_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L98">property sourcePortRanges</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L10">class NetworkWatcher</a>
</h2>

Manages a Network Watcher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L38">constructor</a>
</h3>

```typescript
new NetworkWatcher(name: string, args: NetworkWatcherArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NetworkWatcher resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L38">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L10">class PacketCapture</a>
</h2>

Configures Packet Capturing against a Virtual Machine using a Network Watcher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L58">constructor</a>
</h3>

```typescript
new PacketCapture(name: string, args: PacketCaptureArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PacketCapture resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L26">property filters</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L30">property maximumBytesPerPacket</a>
</h3>

```typescript
public maximumBytesPerPacket: pulumi.Output<number | undefined>;
```


The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L34">property maximumBytesPerSession</a>
</h3>

```typescript
public maximumBytesPerSession: pulumi.Output<number | undefined>;
```


Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L38">property maximumCaptureDuration</a>
</h3>

```typescript
public maximumCaptureDuration: pulumi.Output<number | undefined>;
```


The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name to use for this Packet Capture. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L46">property networkWatcherName</a>
</h3>

```typescript
public networkWatcherName: pulumi.Output<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L50">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L54">property storageLocation</a>
</h3>

```typescript
public storageLocation: pulumi.Output<{ ... }>;
```


A `storage_location` block as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L58">property targetResourceId</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L10">class PublicIp</a>
</h2>

Manage a Public IP Address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L76">constructor</a>
</h3>

```typescript
new PublicIp(name: string, args: PublicIpArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PublicIp resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L26">property domainNameLabel</a>
</h3>

```typescript
public domainNameLabel: pulumi.Output<string | undefined>;
```


Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L30">property fqdn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L34">property idleTimeoutInMinutes</a>
</h3>

```typescript
public idleTimeoutInMinutes: pulumi.Output<number | undefined>;
```


Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L38">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


The IP address value that was allocated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L42">property ipVersion</a>
</h3>

```typescript
public ipVersion: pulumi.Output<string | undefined>;
```


The IP Version to use, IPv6 or IPv4.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L46">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L55">property publicIpAddressAllocation</a>
</h3>

```typescript
public publicIpAddressAllocation: pulumi.Output<string>;
```


Defines whether the IP address is static or dynamic. Options are Static or Dynamic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L60">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the public ip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L64">property reverseFqdn</a>
</h3>

```typescript
public reverseFqdn: pulumi.Output<string | undefined>;
```


A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L68">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string | undefined>;
```


The SKU of the Public IP. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L72">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L76">property zones</a>
</h3>

```typescript
public zones: pulumi.Output<string | undefined>;
```


A collection containing the availability zone to allocate the Public IP in.

<h2 class="pdoc-module-header" id="Route">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L10">class Route</a>
</h2>

Manages a Route within a Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L46">constructor</a>
</h3>

```typescript
new Route(name: string, args: RouteArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Route resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L26">property addressPrefix</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L34">property nextHopInIpAddress</a>
</h3>

```typescript
public nextHopInIpAddress: pulumi.Output<string | undefined>;
```


Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is `VirtualAppliance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L38">property nextHopType</a>
</h3>

```typescript
public nextHopType: pulumi.Output<string>;
```


The type of Azure hop the packet should be sent to. Possible values are `VirtualNetworkGateway`, `VnetLocal`, `Internet`, `VirtualAppliance` and `None`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L42">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L46">property routeTableName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L10">class RouteTable</a>
</h2>

Manages a Route Table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L50">constructor</a>
</h3>

```typescript
new RouteTable(name: string, args: RouteTableArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RouteTable resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L26">property disableBgpRoutePropagation</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the route table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the route table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L42">property routes</a>
</h3>

```typescript
public routes: pulumi.Output<{ ... }[]>;
```


Can be specified multiple times to define multiple routes. Each `route` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L46">property subnets</a>
</h3>

```typescript
public subnets: pulumi.Output<string[]>;
```


The collection of Subnets associated with this route table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L50">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L14">class Subnet</a>
</h2>

Manages a subnet. Subnets represent network segments within the IP space defined by the virtual network.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone Subnet resource, and allows for Subnets to be defined in-line within the Virtual Network resource.
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet's.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L58">constructor</a>
</h3>

```typescript
new Subnet(name: string, args: SubnetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Subnet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L30">property addressPrefix</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L34">property ipConfigurations</a>
</h3>

```typescript
public ipConfigurations: pulumi.Output<string[]>;
```


The collection of IP Configurations with IPs within this subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L42">property networkSecurityGroupId</a>
</h3>

```typescript
public networkSecurityGroupId: pulumi.Output<string | undefined>;
```


The ID of the Network Security Group to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L46">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L50">property routeTableId</a>
</h3>

```typescript
public routeTableId: pulumi.Output<string | undefined>;
```


The ID of the Route Table to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L54">property serviceEndpoints</a>
</h3>

```typescript
public serviceEndpoints: pulumi.Output<string[] | undefined>;
```


The list of Service endpoints to associate with the subnet. Possible values include: `Microsoft.AzureActiveDirectory`, `Microsoft.AzureCosmosDB`, `Microsoft.EventHub`, `Microsoft.KeyVault`, `Microsoft.ServiceBus`, `Microsoft.Sql` and `Microsoft.Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L58">property virtualNetworkName</a>
</h3>

```typescript
public virtualNetworkName: pulumi.Output<string>;
```


The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubnetNetworkSecurityGroupAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L12">class SubnetNetworkSecurityGroupAssociation</a>
</h2>

Associates a Network Security Group with a Subnet within a Virtual Network.

-> **NOTE:** Subnet `<->` Network Security Group associations currently need to be configured on both this resource and using the `network_security_group_id` field on the `azurerm_subnet` resource. The next major version of the AzureRM Provider (2.0) will remove the `network_security_group_id` field from the `azurerm_subnet` resource such that this resource is used to link resources in future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L32">constructor</a>
</h3>

```typescript
new SubnetNetworkSecurityGroupAssociation(name: string, args: SubnetNetworkSecurityGroupAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetNetworkSecurityGroupAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetNetworkSecurityGroupAssociationState): SubnetNetworkSecurityGroupAssociation
```


Get an existing SubnetNetworkSecurityGroupAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L28">property networkSecurityGroupId</a>
</h3>

```typescript
public networkSecurityGroupId: pulumi.Output<string>;
```


The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L32">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The ID of the Subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubnetRouteTableAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L12">class SubnetRouteTableAssociation</a>
</h2>

Associates a Route Table with a Subnet within a Virtual Network.

-> **NOTE:** Subnet `<->` Route Table associations currently need to be configured on both this resource and using the `route_table_id` field on the `azurerm_subnet` resource. The next major version of the AzureRM Provider (2.0) will remove the `route_table_id` field from the `azurerm_subnet` resource such that this resource is used to link resources in future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L32">constructor</a>
</h3>

```typescript
new SubnetRouteTableAssociation(name: string, args: SubnetRouteTableAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetRouteTableAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetRouteTableAssociationState): SubnetRouteTableAssociation
```


Get an existing SubnetRouteTableAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L28">property routeTableId</a>
</h3>

```typescript
public routeTableId: pulumi.Output<string>;
```


The ID of the Route Table which should be associated with the Subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L32">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The ID of the Subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VirtualNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L15">class VirtualNetwork</a>
</h2>

Manages a virtual network including any configured subnets. Each subnet can
optionally be configured with a security group to be associated with the subnet.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone Subnet resource, and allows for Subnets to be defined in-line within the Virtual Network resource.
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet's.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L61">constructor</a>
</h3>

```typescript
new VirtualNetwork(name: string, args: VirtualNetworkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNetwork resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L24">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L33">property addressSpaces</a>
</h3>

```typescript
public addressSpaces: pulumi.Output<string[]>;
```


The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L37">property dnsServers</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L42">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the virtual network is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L47">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the virtual network. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L52">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L57">property subnets</a>
</h3>

```typescript
public subnets: pulumi.Output<{ ... }[]>;
```


Can be specified multiple times to define multiple
subnets. Each `subnet` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L61">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L12">class VirtualNetworkGateway</a>
</h2>

Manages a Virtual Network Gateway to establish secure, cross-premises connectivity.

-> **Note:** Please be aware that provisioning a Virtual Network Gateway takes a long time (between 30 minutes and 1 hour)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L96">constructor</a>
</h3>

```typescript
new VirtualNetworkGateway(name: string, args: VirtualNetworkGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNetworkGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L31">property activeActive</a>
</h3>

```typescript
public activeActive: pulumi.Output<boolean>;
```


If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L32">property bgpSettings</a>
</h3>

```typescript
public bgpSettings: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L40">property defaultLocalNetworkGatewayId</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L45">property enableBgp</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L51">property ipConfigurations</a>
</h3>

```typescript
public ipConfigurations: pulumi.Output<{ ... }[]>;
```


One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L56">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L67">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L76">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2` and `VpnGw3`
and depend on the `type` and `vpn_type` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L80">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L85">property type</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L91">property vpnClientConfiguration</a>
</h3>

```typescript
public vpnClientConfiguration: pulumi.Output<{ ... } | undefined>;
```


A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L96">property vpnType</a>
</h3>

```typescript
public vpnType: pulumi.Output<string | undefined>;
```


The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayConnection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L10">class VirtualNetworkGatewayConnection</a>
</h2>

Manages a connection in an existing Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L106">constructor</a>
</h3>

```typescript
new VirtualNetworkGatewayConnection(name: string, args: VirtualNetworkGatewayConnectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNetworkGatewayConnection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L28">property authorizationKey</a>
</h3>

```typescript
public authorizationKey: pulumi.Output<string | undefined>;
```


The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L33">property enableBgp</a>
</h3>

```typescript
public enableBgp: pulumi.Output<boolean>;
```


If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L39">property expressRouteCircuitId</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L45">property ipsecPolicy</a>
</h3>

```typescript
public ipsecPolicy: pulumi.Output<{ ... } | undefined>;
```


A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L50">property localNetworkGatewayId</a>
</h3>

```typescript
public localNetworkGatewayId: pulumi.Output<string | undefined>;
```


The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L55">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location/region where the connection is
located. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the connection. Changing the name forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L67">property peerVirtualNetworkGatewayId</a>
</h3>

```typescript
public peerVirtualNetworkGatewayId: pulumi.Output<string | undefined>;
```


The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L72">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L76">property routingWeight</a>
</h3>

```typescript
public routingWeight: pulumi.Output<number>;
```


The routing weight. Defaults to `10`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L82">property sharedKey</a>
</h3>

```typescript
public sharedKey: pulumi.Output<string | undefined>;
```


The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L86">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L94">property type</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L100">property usePolicyBasedTrafficSelectors</a>
</h3>

```typescript
public usePolicyBasedTrafficSelectors: pulumi.Output<boolean>;
```


If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L106">property virtualNetworkGatewayId</a>
</h3>

```typescript
public virtualNetworkGatewayId: pulumi.Output<string>;
```


The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkPeering">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L11">class VirtualNetworkPeering</a>
</h2>

Manages a virtual network peering which allows resources to access other
resources in the linked virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L69">constructor</a>
</h3>

```typescript
new VirtualNetworkPeering(name: string, args: VirtualNetworkPeeringArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNetworkPeering resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L28">property allowForwardedTraffic</a>
</h3>

```typescript
public allowForwardedTraffic: pulumi.Output<boolean>;
```


Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L33">property allowGatewayTransit</a>
</h3>

```typescript
public allowGatewayTransit: pulumi.Output<boolean>;
```


Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L39">property allowVirtualNetworkAccess</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the virtual network peering. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L49">property remoteVirtualNetworkId</a>
</h3>

```typescript
public remoteVirtualNetworkId: pulumi.Output<string>;
```


The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L55">property resourceGroupName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L64">property useRemoteGateways</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L69">property virtualNetworkName</a>
</h3>

```typescript
public virtualNetworkName: pulumi.Output<string>;
```


The name of the virtual network. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="getApplicationSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L10">function getApplicationSecurityGroup</a>
</h2>

```typescript
getApplicationSecurityGroup(args: GetApplicationSecurityGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetApplicationSecurityGroupResult>
```


Use this data source to access information about an existing Application Security Group.

<h2 class="pdoc-module-header" id="getNetworkInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L10">function getNetworkInterface</a>
</h2>

```typescript
getNetworkInterface(args: GetNetworkInterfaceArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkInterfaceResult>
```


Use this data source to access information about an existing Network Interface.

<h2 class="pdoc-module-header" id="getNetworkSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L10">function getNetworkSecurityGroup</a>
</h2>

```typescript
getNetworkSecurityGroup(args: GetNetworkSecurityGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkSecurityGroupResult>
```


Use this data source to access information about an existing Network Security Group.

<h2 class="pdoc-module-header" id="getPublicIP">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L10">function getPublicIP</a>
</h2>

```typescript
getPublicIP(args: GetPublicIPArgs, opts?: pulumi.InvokeOptions): Promise<GetPublicIPResult>
```


Use this data source to access information about an existing Public IP Address.

<h2 class="pdoc-module-header" id="getPublicIPs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L10">function getPublicIPs</a>
</h2>

```typescript
getPublicIPs(args: GetPublicIPsArgs, opts?: pulumi.InvokeOptions): Promise<GetPublicIPsResult>
```


Use this data source to access information about a set of existing Public IP Addresses.

<h2 class="pdoc-module-header" id="getRouteTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L10">function getRouteTable</a>
</h2>

```typescript
getRouteTable(args: GetRouteTableArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteTableResult>
```


Use this data source to access information about an existing Route Table.

<h2 class="pdoc-module-header" id="getSubnet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L10">function getSubnet</a>
</h2>

```typescript
getSubnet(args: GetSubnetArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetResult>
```


Use this data source to access information about an existing Subnet within a Virtual Network.

<h2 class="pdoc-module-header" id="getVirtualNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L10">function getVirtualNetwork</a>
</h2>

```typescript
getVirtualNetwork(args: GetVirtualNetworkArgs, opts?: pulumi.InvokeOptions): Promise<GetVirtualNetworkResult>
```


Use this data source to access information about an existing Virtual Network.

<h2 class="pdoc-module-header" id="getVirtualNetworkGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L10">function getVirtualNetworkGateway</a>
</h2>

```typescript
getVirtualNetworkGateway(args: GetVirtualNetworkGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetVirtualNetworkGatewayResult>
```


Use this data source to access information about an existing Virtual Network Gateway.

<h2 class="pdoc-module-header" id="ApplicationGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L151">interface ApplicationGatewayArgs</a>
</h2>

The set of arguments for constructing a ApplicationGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L152">property authenticationCertificates</a>
</h3>

```typescript
authenticationCertificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L153">property backendAddressPools</a>
</h3>

```typescript
backendAddressPools: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L154">property backendHttpSettings</a>
</h3>

```typescript
backendHttpSettings: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L155">property disabledSslProtocols</a>
</h3>

```typescript
disabledSslProtocols?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L156">property frontendIpConfigurations</a>
</h3>

```typescript
frontendIpConfigurations: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L157">property frontendPorts</a>
</h3>

```typescript
frontendPorts: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L158">property gatewayIpConfigurations</a>
</h3>

```typescript
gatewayIpConfigurations: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L159">property httpListeners</a>
</h3>

```typescript
httpListeners: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L160">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L161">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L162">property probes</a>
</h3>

```typescript
probes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L163">property requestRoutingRules</a>
</h3>

```typescript
requestRoutingRules: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L164">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L165">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L166">property sslCertificates</a>
</h3>

```typescript
sslCertificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L167">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L168">property urlPathMaps</a>
</h3>

```typescript
urlPathMaps?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L169">property wafConfiguration</a>
</h3>

```typescript
wafConfiguration?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ApplicationGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L127">interface ApplicationGatewayState</a>
</h2>

Input properties used for looking up and filtering ApplicationGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L128">property authenticationCertificates</a>
</h3>

```typescript
authenticationCertificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L129">property backendAddressPools</a>
</h3>

```typescript
backendAddressPools?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L130">property backendHttpSettings</a>
</h3>

```typescript
backendHttpSettings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L131">property disabledSslProtocols</a>
</h3>

```typescript
disabledSslProtocols?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L132">property frontendIpConfigurations</a>
</h3>

```typescript
frontendIpConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L133">property frontendPorts</a>
</h3>

```typescript
frontendPorts?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L134">property gatewayIpConfigurations</a>
</h3>

```typescript
gatewayIpConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L135">property httpListeners</a>
</h3>

```typescript
httpListeners?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L136">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L138">property probes</a>
</h3>

```typescript
probes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L139">property requestRoutingRules</a>
</h3>

```typescript
requestRoutingRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L140">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L141">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L142">property sslCertificates</a>
</h3>

```typescript
sslCertificates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L143">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L144">property urlPathMaps</a>
</h3>

```typescript
urlPathMaps?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationGateway.ts#L145">property wafConfiguration</a>
</h3>

```typescript
wafConfiguration?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ApplicationSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L98">interface ApplicationSecurityGroupArgs</a>
</h2>

The set of arguments for constructing a ApplicationSecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L102">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Application Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L110">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L114">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ApplicationSecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L76">interface ApplicationSecurityGroupState</a>
</h2>

Input properties used for looking up and filtering ApplicationSecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L80">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Application Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L88">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/applicationSecurityGroup.ts#L92">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L180">interface ExpressRouteCircuitArgs</a>
</h2>

The set of arguments for constructing a ExpressRouteCircuit resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L184">property allowClassicOperations</a>
</h3>

```typescript
allowClassicOperations?: pulumi.Input<boolean>;
```


Allow the circuit to interact with classic (RDFE) resources. The default value is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L188">property bandwidthInMbps</a>
</h3>

```typescript
bandwidthInMbps: pulumi.Input<number>;
```


The bandwidth in Mbps of the circuit being created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L192">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L196">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L200">property peeringLocation</a>
</h3>

```typescript
peeringLocation: pulumi.Input<string>;
```


The name of the peering location and **not** the Azure resource location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L204">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L208">property serviceProviderName</a>
</h3>

```typescript
serviceProviderName: pulumi.Input<string>;
```


The name of the ExpressRoute Service Provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L212">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block for the ExpressRoute circuit as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L216">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitAuthorizationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L112">interface ExpressRouteCircuitAuthorizationArgs</a>
</h2>

The set of arguments for constructing a ExpressRouteCircuitAuthorization resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L116">property expressRouteCircuitName</a>
</h3>

```typescript
expressRouteCircuitName: pulumi.Input<string>;
```


The name of the Express Route Circuit in which to create the Authorization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L126">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitAuthorizationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L84">interface ExpressRouteCircuitAuthorizationState</a>
</h2>

Input properties used for looking up and filtering ExpressRouteCircuitAuthorization resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L88">property authorizationKey</a>
</h3>

```typescript
authorizationKey?: pulumi.Input<string>;
```


The Authorization Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L92">property authorizationUseStatus</a>
</h3>

```typescript
authorizationUseStatus?: pulumi.Input<string>;
```


The authorization use status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L96">property expressRouteCircuitName</a>
</h3>

```typescript
expressRouteCircuitName?: pulumi.Input<string>;
```


The name of the Express Route Circuit in which to create the Authorization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitAuthorization.ts#L106">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitPeeringArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L192">interface ExpressRouteCircuitPeeringArgs</a>
</h2>

The set of arguments for constructing a ExpressRouteCircuitPeering resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L196">property expressRouteCircuitName</a>
</h3>

```typescript
expressRouteCircuitName: pulumi.Input<string>;
```


The name of the ExpressRoute Circuit in which to create the Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L200">property microsoftPeeringConfig</a>
</h3>

```typescript
microsoftPeeringConfig?: pulumi.Input<{ ... }>;
```


A `microsoft_peering_config` block as defined below. Required when `peering_type` is set to `MicrosoftPeering`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L204">property peerAsn</a>
</h3>

```typescript
peerAsn?: pulumi.Input<number>;
```


The Either a 16-bit or a 32-bit ASN. Can either be public or private..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L208">property peeringType</a>
</h3>

```typescript
peeringType: pulumi.Input<string>;
```


The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L212">property primaryPeerAddressPrefix</a>
</h3>

```typescript
primaryPeerAddressPrefix: pulumi.Input<string>;
```


A `/30` subnet for the primary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L217">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L221">property secondaryPeerAddressPrefix</a>
</h3>

```typescript
secondaryPeerAddressPrefix: pulumi.Input<string>;
```


A `/30` subnet for the secondary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L225">property sharedKey</a>
</h3>

```typescript
sharedKey?: pulumi.Input<string>;
```


The shared key. Can be a maximum of 25 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L229">property vlanId</a>
</h3>

```typescript
vlanId: pulumi.Input<number>;
```


A valid VLAN ID to establish this peering on.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitPeeringState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L137">interface ExpressRouteCircuitPeeringState</a>
</h2>

Input properties used for looking up and filtering ExpressRouteCircuitPeering resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L141">property azureAsn</a>
</h3>

```typescript
azureAsn?: pulumi.Input<number>;
```


The ASN used by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L145">property expressRouteCircuitName</a>
</h3>

```typescript
expressRouteCircuitName?: pulumi.Input<string>;
```


The name of the ExpressRoute Circuit in which to create the Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L149">property microsoftPeeringConfig</a>
</h3>

```typescript
microsoftPeeringConfig?: pulumi.Input<{ ... }>;
```


A `microsoft_peering_config` block as defined below. Required when `peering_type` is set to `MicrosoftPeering`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L153">property peerAsn</a>
</h3>

```typescript
peerAsn?: pulumi.Input<number>;
```


The Either a 16-bit or a 32-bit ASN. Can either be public or private..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L157">property peeringType</a>
</h3>

```typescript
peeringType?: pulumi.Input<string>;
```


The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L161">property primaryAzurePort</a>
</h3>

```typescript
primaryAzurePort?: pulumi.Input<string>;
```


The Primary Port used by Azure for this Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L165">property primaryPeerAddressPrefix</a>
</h3>

```typescript
primaryPeerAddressPrefix?: pulumi.Input<string>;
```


A `/30` subnet for the primary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L170">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L174">property secondaryAzurePort</a>
</h3>

```typescript
secondaryAzurePort?: pulumi.Input<string>;
```


The Secondary Port used by Azure for this Peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L178">property secondaryPeerAddressPrefix</a>
</h3>

```typescript
secondaryPeerAddressPrefix?: pulumi.Input<string>;
```


A `/30` subnet for the secondary link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L182">property sharedKey</a>
</h3>

```typescript
sharedKey?: pulumi.Input<string>;
```


The shared key. Can be a maximum of 25 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuitPeering.ts#L186">property vlanId</a>
</h3>

```typescript
vlanId?: pulumi.Input<number>;
```


A valid VLAN ID to establish this peering on.

<h2 class="pdoc-module-header" id="ExpressRouteCircuitState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L130">interface ExpressRouteCircuitState</a>
</h2>

Input properties used for looking up and filtering ExpressRouteCircuit resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L134">property allowClassicOperations</a>
</h3>

```typescript
allowClassicOperations?: pulumi.Input<boolean>;
```


Allow the circuit to interact with classic (RDFE) resources. The default value is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L138">property bandwidthInMbps</a>
</h3>

```typescript
bandwidthInMbps?: pulumi.Input<number>;
```


The bandwidth in Mbps of the circuit being created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L142">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L146">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L150">property peeringLocation</a>
</h3>

```typescript
peeringLocation?: pulumi.Input<string>;
```


The name of the peering location and **not** the Azure resource location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L154">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L158">property serviceKey</a>
</h3>

```typescript
serviceKey?: pulumi.Input<string>;
```


The string needed by the service provider to provision the ExpressRoute circuit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L162">property serviceProviderName</a>
</h3>

```typescript
serviceProviderName?: pulumi.Input<string>;
```


The name of the ExpressRoute Service Provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L166">property serviceProviderProvisioningState</a>
</h3>

```typescript
serviceProviderProvisioningState?: pulumi.Input<string>;
```


The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L170">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block for the ExpressRoute circuit as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/expressRouteCircuit.ts#L174">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="FirewallArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L113">interface FirewallArgs</a>
</h2>

The set of arguments for constructing a Firewall resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L117">property ipConfiguration</a>
</h3>

```typescript
ipConfiguration: pulumi.Input<{ ... }>;
```


A `ip_configuration` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L121">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Firewall. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L129">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L133">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="FirewallNetworkRuleCollectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L129">interface FirewallNetworkRuleCollectionArgs</a>
</h2>

The set of arguments for constructing a FirewallNetworkRuleCollection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L133">property action</a>
</h3>

```typescript
action: pulumi.Input<string>;
```


Specifies the action the rule will apply to matching traffic. Possible values are `Allow` and `Deny`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L137">property azureFirewallName</a>
</h3>

```typescript
azureFirewallName: pulumi.Input<string>;
```


Specifies the name of the Firewall in which to the Network Rule Collection should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L145">property priority</a>
</h3>

```typescript
priority: pulumi.Input<number>;
```


Specifies the priority of the rule collection. Possible values are between `100` - `65000`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L149">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L153">property rules</a>
</h3>

```typescript
rules: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `rule` blocks as defined below.

<h2 class="pdoc-module-header" id="FirewallNetworkRuleCollectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L99">interface FirewallNetworkRuleCollectionState</a>
</h2>

Input properties used for looking up and filtering FirewallNetworkRuleCollection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L103">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


Specifies the action the rule will apply to matching traffic. Possible values are `Allow` and `Deny`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L107">property azureFirewallName</a>
</h3>

```typescript
azureFirewallName?: pulumi.Input<string>;
```


Specifies the name of the Firewall in which to the Network Rule Collection should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L115">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


Specifies the priority of the rule collection. Possible values are between `100` - `65000`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L119">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewallNetworkRuleCollection.ts#L123">property rules</a>
</h3>

```typescript
rules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `rule` blocks as defined below.

<h2 class="pdoc-module-header" id="FirewallState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L87">interface FirewallState</a>
</h2>

Input properties used for looking up and filtering Firewall resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L91">property ipConfiguration</a>
</h3>

```typescript
ipConfiguration?: pulumi.Input<{ ... }>;
```


A `ip_configuration` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L95">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Firewall. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L103">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/firewall.ts#L107">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="GetApplicationSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L20">interface GetApplicationSecurityGroupArgs</a>
</h2>

A collection of arguments for invoking getApplicationSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the Application Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the resource group in which the Application Security Group exists.

<h2 class="pdoc-module-header" id="GetApplicationSecurityGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L34">interface GetApplicationSecurityGroupResult</a>
</h2>

A collection of values returned by getApplicationSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L46">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L38">property location</a>
</h3>

```typescript
location: string;
```


The supported Azure location where the Application Security Group exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getApplicationSecurityGroup.ts#L42">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="GetNetworkInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L20">interface GetNetworkInterfaceArgs</a>
</h2>

A collection of arguments for invoking getNetworkInterface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Network Interface is located in.

<h2 class="pdoc-module-header" id="GetNetworkInterfaceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L34">interface GetNetworkInterfaceResult</a>
</h2>

A collection of values returned by getNetworkInterface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L38">property appliedDnsServers</a>
</h3>

```typescript
appliedDnsServers: string[];
```


List of DNS servers applied to the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L42">property dnsServers</a>
</h3>

```typescript
dnsServers: string[];
```


The list of DNS servers used by the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L46">property enableAcceleratedNetworking</a>
</h3>

```typescript
enableAcceleratedNetworking: boolean;
```


Indicates if accelerated networking is set on the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L50">property enableIpForwarding</a>
</h3>

```typescript
enableIpForwarding: boolean;
```


Indicate if IP forwarding is set on the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L91">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L54">property internalDnsNameLabel</a>
</h3>

```typescript
internalDnsNameLabel: string;
```


The internal dns name label of the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L55">property internalFqdn</a>
</h3>

```typescript
internalFqdn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L59">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: { ... }[];
```


One or more `ip_configuration` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L63">property location</a>
</h3>

```typescript
location: string;
```


The location of the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L67">property macAddress</a>
</h3>

```typescript
macAddress: string;
```


The MAC address used by the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L71">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId: string;
```


The ID of the network security group associated to the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L75">property privateIpAddress</a>
</h3>

```typescript
privateIpAddress: string;
```


The Private IP Address assigned to this Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L79">property privateIpAddresses</a>
</h3>

```typescript
privateIpAddresses: string[];
```


The list of private ip addresses associates to the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L83">property tags</a>
</h3>

```typescript
tags: { ... };
```


List the tags associated to the specified Network Interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkInterface.ts#L87">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId: string;
```


The ID of the virtual machine that the specified Network Interface is attached to.

<h2 class="pdoc-module-header" id="GetNetworkSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L20">interface GetNetworkSecurityGroupArgs</a>
</h2>

A collection of arguments for invoking getNetworkSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the Name of the Network Security Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the Name of the Resource Group within which the Network Security Group exists

<h2 class="pdoc-module-header" id="GetNetworkSecurityGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L34">interface GetNetworkSecurityGroupResult</a>
</h2>

A collection of values returned by getNetworkSecurityGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L50">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L38">property location</a>
</h3>

```typescript
location: string;
```


The supported Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L42">property securityRules</a>
</h3>

```typescript
securityRules: { ... }[];
```


One or more `security_rule` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getNetworkSecurityGroup.ts#L46">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="GetPublicIPArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L21">interface GetPublicIPArgs</a>
</h2>

A collection of arguments for invoking getPublicIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L25">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the public IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L29">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L30">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetPublicIPResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L36">interface GetPublicIPResult</a>
</h2>

A collection of values returned by getPublicIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L40">property domainNameLabel</a>
</h3>

```typescript
domainNameLabel: string;
```


The label for the Domain Name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L44">property fqdn</a>
</h3>

```typescript
fqdn: string;
```


Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L64">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L48">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes: number;
```


Specifies the timeout for the TCP idle connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L52">property ipAddress</a>
</h3>

```typescript
ipAddress: string;
```


The IP address value that was allocated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L56">property ipVersion</a>
</h3>

```typescript
ipVersion: string;
```


The IP version being used, for example `IPv4` or `IPv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIP.ts#L60">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assigned to the resource.

<h2 class="pdoc-module-header" id="GetPublicIPsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L22">interface GetPublicIPsArgs</a>
</h2>

A collection of arguments for invoking getPublicIPs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L26">property allocationType</a>
</h3>

```typescript
allocationType?: string;
```


The Allocation Type for the Public IP Address. Possible values include `Static` or `Dynamic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L30">property attached</a>
</h3>

```typescript
attached?: boolean;
```


Filter to include IP Addresses which are attached to a device, such as a VM/LB (`true`) or unattached (`false`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L34">property namePrefix</a>
</h3>

```typescript
namePrefix?: string;
```


A prefix match used for the IP Addresses `name` field, case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L38">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group.

<h2 class="pdoc-module-header" id="GetPublicIPsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L44">interface GetPublicIPsResult</a>
</h2>

A collection of values returned by getPublicIPs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L52">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getPublicIPs.ts#L48">property publicIps</a>
</h3>

```typescript
publicIps: { ... }[];
```


A List of `public_ips` blocks as defined below filtered by the criteria above.

<h2 class="pdoc-module-header" id="GetRouteTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L20">interface GetRouteTableArgs</a>
</h2>

A collection of arguments for invoking getRouteTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the Route Table exists.

<h2 class="pdoc-module-header" id="GetRouteTableResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L34">interface GetRouteTableResult</a>
</h2>

A collection of values returned by getRouteTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L54">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L38">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region in which the Route Table exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L42">property routes</a>
</h3>

```typescript
routes: { ... }[];
```


One or more `route` blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L46">property subnets</a>
</h3>

```typescript
subnets: string[];
```


The collection of Subnets associated with this route table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getRouteTable.ts#L50">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the Route Table.

<h2 class="pdoc-module-header" id="GetSubnetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L21">interface GetSubnetArgs</a>
</h2>

A collection of arguments for invoking getSubnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L25">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L29">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Virtual Network is located in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L33">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName: string;
```


Specifies the name of the Virtual Network this Subnet is located within.

<h2 class="pdoc-module-header" id="GetSubnetResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L39">interface GetSubnetResult</a>
</h2>

A collection of values returned by getSubnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L43">property addressPrefix</a>
</h3>

```typescript
addressPrefix: string;
```


The address prefix used for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L59">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L47">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: string[];
```


The collection of IP Configurations with IPs within this subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L51">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId: string;
```


The ID of the Network Security Group associated with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getSubnet.ts#L55">property routeTableId</a>
</h3>

```typescript
routeTableId: string;
```


The ID of the Route Table associated with this subnet.

<h2 class="pdoc-module-header" id="GetVirtualNetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L20">interface GetVirtualNetworkArgs</a>
</h2>

A collection of arguments for invoking getVirtualNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Virtual Network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Virtual Network is located in.

<h2 class="pdoc-module-header" id="GetVirtualNetworkGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L20">interface GetVirtualNetworkGatewayArgs</a>
</h2>

A collection of arguments for invoking getVirtualNetworkGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Virtual Network Gateway is located in.

<h2 class="pdoc-module-header" id="GetVirtualNetworkGatewayResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L34">interface GetVirtualNetworkGatewayResult</a>
</h2>

A collection of values returned by getVirtualNetworkGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L38">property activeActive</a>
</h3>

```typescript
activeActive: boolean;
```


(Optional) Is this an Active-Active Gateway?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L39">property bgpSettings</a>
</h3>

```typescript
bgpSettings: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L46">property defaultLocalNetworkGatewayId</a>
</h3>

```typescript
defaultLocalNetworkGatewayId: string;
```


The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L51">property enableBgp</a>
</h3>

```typescript
enableBgp: boolean;
```


Will BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L83">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L55">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: { ... }[];
```


One or two `ip_configuration` blocks documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L59">property location</a>
</h3>

```typescript
location: string;
```


The location/region where the Virtual Network Gateway is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L63">property sku</a>
</h3>

```typescript
sku: string;
```


Configuration of the size and capacity of the Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L67">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L71">property type</a>
</h3>

```typescript
type: string;
```


The type of the Virtual Network Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L75">property vpnClientConfigurations</a>
</h3>

```typescript
vpnClientConfigurations: { ... }[];
```


A `vpn_client_configuration` block which is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetworkGateway.ts#L79">property vpnType</a>
</h3>

```typescript
vpnType: string;
```


The routing type of the Virtual Network Gateway.

<h2 class="pdoc-module-header" id="GetVirtualNetworkResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L34">interface GetVirtualNetworkResult</a>
</h2>

A collection of values returned by getVirtualNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L38">property addressSpaces</a>
</h3>

```typescript
addressSpaces: string[];
```


The list of address spaces used by the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L42">property dnsServers</a>
</h3>

```typescript
dnsServers: string[];
```


The list of DNS servers used by the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L54">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L46">property subnets</a>
</h3>

```typescript
subnets: string[];
```


The list of name of the subnets that are attached to this virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/getVirtualNetwork.ts#L50">property vnetPeerings</a>
</h3>

```typescript
vnetPeerings: { ... };
```


A mapping of name - virtual network id of the virtual network peerings.

<h2 class="pdoc-module-header" id="LocalNetworkGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L146">interface LocalNetworkGatewayArgs</a>
</h2>

The set of arguments for constructing a LocalNetworkGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L151">property addressSpaces</a>
</h3>

```typescript
addressSpaces: pulumi.Input<pulumi.Input<string>[]>;
```


The list of string CIDRs representing the
address spaces the gateway exposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L156">property bgpSettings</a>
</h3>

```typescript
bgpSettings?: pulumi.Input<{ ... }>;
```


A `bgp_settings` block as defined below containing the
Local Network Gateway's BGP speaker settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L161">property gatewayAddress</a>
</h3>

```typescript
gatewayAddress: pulumi.Input<string>;
```


The IP address of the gateway to which to
connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L166">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the local network gateway is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the local network gateway. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L176">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the local network gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L180">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LocalNetworkGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L106">interface LocalNetworkGatewayState</a>
</h2>

Input properties used for looking up and filtering LocalNetworkGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L111">property addressSpaces</a>
</h3>

```typescript
addressSpaces?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of string CIDRs representing the
address spaces the gateway exposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L116">property bgpSettings</a>
</h3>

```typescript
bgpSettings?: pulumi.Input<{ ... }>;
```


A `bgp_settings` block as defined below containing the
Local Network Gateway's BGP speaker settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L121">property gatewayAddress</a>
</h3>

```typescript
gatewayAddress?: pulumi.Input<string>;
```


The IP address of the gateway to which to
connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L126">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the local network gateway is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L131">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the local network gateway. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L136">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the local network gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/localNetworkGateway.ts#L140">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L91">interface NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationArgs</a>
</h2>

The set of arguments for constructing a NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L95">property backendAddressPoolId</a>
</h3>

```typescript
backendAddressPoolId: pulumi.Input<string>;
```


The ID of the Application Gateway's Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L99">property ipConfigurationName</a>
</h3>

```typescript
ipConfigurationName: pulumi.Input<string>;
```


The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L103">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: pulumi.Input<string>;
```


The ID of the Network Interface. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L73">interface NetworkInterfaceApplicationGatewayBackendAddressPoolAssociationState</a>
</h2>

Input properties used for looking up and filtering NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L77">property backendAddressPoolId</a>
</h3>

```typescript
backendAddressPoolId?: pulumi.Input<string>;
```


The ID of the Application Gateway's Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L81">property ipConfigurationName</a>
</h3>

```typescript
ipConfigurationName?: pulumi.Input<string>;
```


The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation.ts#L85">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The ID of the Network Interface. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NetworkInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L209">interface NetworkInterfaceArgs</a>
</h2>

The set of arguments for constructing a NetworkInterface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L213">property appliedDnsServers</a>
</h3>

```typescript
appliedDnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L217">property dnsServers</a>
</h3>

```typescript
dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of DNS servers IP addresses to use for this NIC, overrides the VNet-level server list

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L221">property enableAcceleratedNetworking</a>
</h3>

```typescript
enableAcceleratedNetworking?: pulumi.Input<boolean>;
```


Enables Azure Accelerated Networking using SR-IOV. Only certain VM instance sizes are supported. Refer to [Create a Virtual Machine with Accelerated Networking](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli). Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L225">property enableIpForwarding</a>
</h3>

```typescript
enableIpForwarding?: pulumi.Input<boolean>;
```


Enables IP Forwarding on the NIC. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L229">property internalDnsNameLabel</a>
</h3>

```typescript
internalDnsNameLabel?: pulumi.Input<string>;
```


Relative DNS name for this NIC used for internal communications between VMs in the same VNet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L230">property internalFqdn</a>
</h3>

```typescript
internalFqdn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L234">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `ip_configuration` associated with this NIC as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L238">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the network interface is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L242">property macAddress</a>
</h3>

```typescript
macAddress?: pulumi.Input<string>;
```


The media access control (MAC) address of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L246">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the network interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L250">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId?: pulumi.Input<string>;
```


The ID of the Network Security Group to associate with the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L254">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the network interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L258">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L262">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId?: pulumi.Input<string>;
```


Reference to a VM with which this NIC has been associated.

<h2 class="pdoc-module-header" id="NetworkInterfaceBackendAddressPoolAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L91">interface NetworkInterfaceBackendAddressPoolAssociationArgs</a>
</h2>

The set of arguments for constructing a NetworkInterfaceBackendAddressPoolAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L95">property backendAddressPoolId</a>
</h3>

```typescript
backendAddressPoolId: pulumi.Input<string>;
```


The ID of the Load Balancer Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L99">property ipConfigurationName</a>
</h3>

```typescript
ipConfigurationName: pulumi.Input<string>;
```


The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L103">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: pulumi.Input<string>;
```


The ID of the Network Interface. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NetworkInterfaceBackendAddressPoolAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L73">interface NetworkInterfaceBackendAddressPoolAssociationState</a>
</h2>

Input properties used for looking up and filtering NetworkInterfaceBackendAddressPoolAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L77">property backendAddressPoolId</a>
</h3>

```typescript
backendAddressPoolId?: pulumi.Input<string>;
```


The ID of the Load Balancer Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L81">property ipConfigurationName</a>
</h3>

```typescript
ipConfigurationName?: pulumi.Input<string>;
```


The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceBackendAddressPoolAssociation.ts#L85">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The ID of the Network Interface. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NetworkInterfaceNatRuleAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L91">interface NetworkInterfaceNatRuleAssociationArgs</a>
</h2>

The set of arguments for constructing a NetworkInterfaceNatRuleAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L95">property ipConfigurationName</a>
</h3>

```typescript
ipConfigurationName: pulumi.Input<string>;
```


The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L99">property natRuleId</a>
</h3>

```typescript
natRuleId: pulumi.Input<string>;
```


The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L103">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: pulumi.Input<string>;
```


The ID of the Network Interface. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NetworkInterfaceNatRuleAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L73">interface NetworkInterfaceNatRuleAssociationState</a>
</h2>

Input properties used for looking up and filtering NetworkInterfaceNatRuleAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L77">property ipConfigurationName</a>
</h3>

```typescript
ipConfigurationName?: pulumi.Input<string>;
```


The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L81">property natRuleId</a>
</h3>

```typescript
natRuleId?: pulumi.Input<string>;
```


The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterfaceNatRuleAssociation.ts#L85">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The ID of the Network Interface. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NetworkInterfaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L145">interface NetworkInterfaceState</a>
</h2>

Input properties used for looking up and filtering NetworkInterface resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L149">property appliedDnsServers</a>
</h3>

```typescript
appliedDnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L153">property dnsServers</a>
</h3>

```typescript
dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of DNS servers IP addresses to use for this NIC, overrides the VNet-level server list

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L157">property enableAcceleratedNetworking</a>
</h3>

```typescript
enableAcceleratedNetworking?: pulumi.Input<boolean>;
```


Enables Azure Accelerated Networking using SR-IOV. Only certain VM instance sizes are supported. Refer to [Create a Virtual Machine with Accelerated Networking](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli). Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L161">property enableIpForwarding</a>
</h3>

```typescript
enableIpForwarding?: pulumi.Input<boolean>;
```


Enables IP Forwarding on the NIC. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L165">property internalDnsNameLabel</a>
</h3>

```typescript
internalDnsNameLabel?: pulumi.Input<string>;
```


Relative DNS name for this NIC used for internal communications between VMs in the same VNet

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L166">property internalFqdn</a>
</h3>

```typescript
internalFqdn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L170">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `ip_configuration` associated with this NIC as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L174">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the network interface is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L178">property macAddress</a>
</h3>

```typescript
macAddress?: pulumi.Input<string>;
```


The media access control (MAC) address of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L182">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the network interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L186">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId?: pulumi.Input<string>;
```


The ID of the Network Security Group to associate with the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L190">property privateIpAddress</a>
</h3>

```typescript
privateIpAddress?: pulumi.Input<string>;
```


The private ip address of the network interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L191">property privateIpAddresses</a>
</h3>

```typescript
privateIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L195">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the network interface. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L199">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkInterface.ts#L203">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId?: pulumi.Input<string>;
```


Reference to a VM with which this NIC has been associated.

<h2 class="pdoc-module-header" id="NetworkSecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L112">interface NetworkSecurityGroupArgs</a>
</h2>

The set of arguments for constructing a NetworkSecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L116">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the network security group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L124">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L128">property securityRules</a>
</h3>

```typescript
securityRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `security_rule` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L132">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkSecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L86">interface NetworkSecurityGroupState</a>
</h2>

Input properties used for looking up and filtering NetworkSecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L90">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the network security group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L98">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L102">property securityRules</a>
</h3>

```typescript
securityRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `security_rule` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityGroup.ts#L106">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkSecurityRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L254">interface NetworkSecurityRuleArgs</a>
</h2>

The set of arguments for constructing a NetworkSecurityRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L258">property access</a>
</h3>

```typescript
access: pulumi.Input<string>;
```


Specifies whether network traffic is allowed or denied. Possible values are `Allow` and `Deny`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L262">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this rule. Restricted to 140 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L266">property destinationAddressPrefix</a>
</h3>

```typescript
destinationAddressPrefix?: pulumi.Input<string>;
```


CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `destination_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L270">property destinationAddressPrefixes</a>
</h3>

```typescript
destinationAddressPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of destination address prefixes. Tags may not be used. This is required if `destination_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L274">property destinationApplicationSecurityGroupIds</a>
</h3>

```typescript
destinationApplicationSecurityGroupIds?: pulumi.Input<string>;
```


A List of destination Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L278">property destinationPortRange</a>
</h3>

```typescript
destinationPortRange?: pulumi.Input<string>;
```


Destination Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `destination_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L282">property destinationPortRanges</a>
</h3>

```typescript
destinationPortRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


List of destination ports or port ranges. This is required if `destination_port_range` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L286">property direction</a>
</h3>

```typescript
direction: pulumi.Input<string>;
```


The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are `Inbound` and `Outbound`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L290">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L294">property networkSecurityGroupName</a>
</h3>

```typescript
networkSecurityGroupName: pulumi.Input<string>;
```


The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L298">property priority</a>
</h3>

```typescript
priority: pulumi.Input<number>;
```


Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L302">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


Network protocol this rule applies to. Possible values include `Tcp`, `Udp` or `*` (which matches both).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L306">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L310">property sourceAddressPrefix</a>
</h3>

```typescript
sourceAddressPrefix?: pulumi.Input<string>;
```


CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `source_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L314">property sourceAddressPrefixes</a>
</h3>

```typescript
sourceAddressPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of source address prefixes. Tags may not be used. This is required if `source_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L318">property sourceApplicationSecurityGroupIds</a>
</h3>

```typescript
sourceApplicationSecurityGroupIds?: pulumi.Input<string>;
```


A List of source Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L322">property sourcePortRange</a>
</h3>

```typescript
sourcePortRange?: pulumi.Input<string>;
```


Source Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `source_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L326">property sourcePortRanges</a>
</h3>

```typescript
sourcePortRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


List of source ports or port ranges. This is required if `source_port_range` is not specified.

<h2 class="pdoc-module-header" id="NetworkSecurityRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L176">interface NetworkSecurityRuleState</a>
</h2>

Input properties used for looking up and filtering NetworkSecurityRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L180">property access</a>
</h3>

```typescript
access?: pulumi.Input<string>;
```


Specifies whether network traffic is allowed or denied. Possible values are `Allow` and `Deny`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L184">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this rule. Restricted to 140 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L188">property destinationAddressPrefix</a>
</h3>

```typescript
destinationAddressPrefix?: pulumi.Input<string>;
```


CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `destination_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L192">property destinationAddressPrefixes</a>
</h3>

```typescript
destinationAddressPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of destination address prefixes. Tags may not be used. This is required if `destination_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L196">property destinationApplicationSecurityGroupIds</a>
</h3>

```typescript
destinationApplicationSecurityGroupIds?: pulumi.Input<string>;
```


A List of destination Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L200">property destinationPortRange</a>
</h3>

```typescript
destinationPortRange?: pulumi.Input<string>;
```


Destination Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `destination_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L204">property destinationPortRanges</a>
</h3>

```typescript
destinationPortRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


List of destination ports or port ranges. This is required if `destination_port_range` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L208">property direction</a>
</h3>

```typescript
direction?: pulumi.Input<string>;
```


The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are `Inbound` and `Outbound`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L212">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L216">property networkSecurityGroupName</a>
</h3>

```typescript
networkSecurityGroupName?: pulumi.Input<string>;
```


The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L220">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L224">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


Network protocol this rule applies to. Possible values include `Tcp`, `Udp` or `*` (which matches both).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L228">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L232">property sourceAddressPrefix</a>
</h3>

```typescript
sourceAddressPrefix?: pulumi.Input<string>;
```


CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `source_address_prefixes` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L236">property sourceAddressPrefixes</a>
</h3>

```typescript
sourceAddressPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of source address prefixes. Tags may not be used. This is required if `source_address_prefix` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L240">property sourceApplicationSecurityGroupIds</a>
</h3>

```typescript
sourceApplicationSecurityGroupIds?: pulumi.Input<string>;
```


A List of source Application Security Group ID's

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L244">property sourcePortRange</a>
</h3>

```typescript
sourcePortRange?: pulumi.Input<string>;
```


Source Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `source_port_ranges` is not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkSecurityRule.ts#L248">property sourcePortRanges</a>
</h3>

```typescript
sourcePortRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


List of source ports or port ranges. This is required if `source_port_range` is not specified.

<h2 class="pdoc-module-header" id="NetworkWatcherArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L98">interface NetworkWatcherArgs</a>
</h2>

The set of arguments for constructing a NetworkWatcher resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L102">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L110">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L114">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NetworkWatcherState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L76">interface NetworkWatcherState</a>
</h2>

Input properties used for looking up and filtering NetworkWatcher resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L80">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L88">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/networkWatcher.ts#L92">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="PacketCaptureArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L154">interface PacketCaptureArgs</a>
</h2>

The set of arguments for constructing a PacketCapture resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L158">property filters</a>
</h3>

```typescript
filters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `filter` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L162">property maximumBytesPerPacket</a>
</h3>

```typescript
maximumBytesPerPacket?: pulumi.Input<number>;
```


The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L166">property maximumBytesPerSession</a>
</h3>

```typescript
maximumBytesPerSession?: pulumi.Input<number>;
```


Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L170">property maximumCaptureDuration</a>
</h3>

```typescript
maximumCaptureDuration?: pulumi.Input<number>;
```


The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L174">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for this Packet Capture. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L178">property networkWatcherName</a>
</h3>

```typescript
networkWatcherName: pulumi.Input<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L182">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L186">property storageLocation</a>
</h3>

```typescript
storageLocation: pulumi.Input<{ ... }>;
```


A `storage_location` block as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L190">property targetResourceId</a>
</h3>

```typescript
targetResourceId: pulumi.Input<string>;
```


The ID of the Resource to capture packets from. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PacketCaptureState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L112">interface PacketCaptureState</a>
</h2>

Input properties used for looking up and filtering PacketCapture resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L116">property filters</a>
</h3>

```typescript
filters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `filter` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L120">property maximumBytesPerPacket</a>
</h3>

```typescript
maximumBytesPerPacket?: pulumi.Input<number>;
```


The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L124">property maximumBytesPerSession</a>
</h3>

```typescript
maximumBytesPerSession?: pulumi.Input<number>;
```


Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L128">property maximumCaptureDuration</a>
</h3>

```typescript
maximumCaptureDuration?: pulumi.Input<number>;
```


The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L132">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for this Packet Capture. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L136">property networkWatcherName</a>
</h3>

```typescript
networkWatcherName?: pulumi.Input<string>;
```


The name of the Network Watcher. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L140">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L144">property storageLocation</a>
</h3>

```typescript
storageLocation?: pulumi.Input<{ ... }>;
```


A `storage_location` block as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/packetCapture.ts#L148">property targetResourceId</a>
</h3>

```typescript
targetResourceId?: pulumi.Input<string>;
```


The ID of the Resource to capture packets from. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PublicIpArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L195">interface PublicIpArgs</a>
</h2>

The set of arguments for constructing a PublicIp resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L199">property domainNameLabel</a>
</h3>

```typescript
domainNameLabel?: pulumi.Input<string>;
```


Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L203">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes?: pulumi.Input<number>;
```


Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L207">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<string>;
```


The IP Version to use, IPv6 or IPv4.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L211">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L216">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L220">property publicIpAddressAllocation</a>
</h3>

```typescript
publicIpAddressAllocation: pulumi.Input<string>;
```


Defines whether the IP address is static or dynamic. Options are Static or Dynamic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L225">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the public ip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L229">property reverseFqdn</a>
</h3>

```typescript
reverseFqdn?: pulumi.Input<string>;
```


A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L233">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU of the Public IP. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L237">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L241">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<string>;
```


A collection containing the availability zone to allocate the Public IP in.

<h2 class="pdoc-module-header" id="PublicIpState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L135">interface PublicIpState</a>
</h2>

Input properties used for looking up and filtering PublicIp resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L139">property domainNameLabel</a>
</h3>

```typescript
domainNameLabel?: pulumi.Input<string>;
```


Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L143">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L147">property idleTimeoutInMinutes</a>
</h3>

```typescript
idleTimeoutInMinutes?: pulumi.Input<number>;
```


Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L151">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address value that was allocated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L155">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<string>;
```


The IP Version to use, IPv6 or IPv4.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L159">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L164">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L168">property publicIpAddressAllocation</a>
</h3>

```typescript
publicIpAddressAllocation?: pulumi.Input<string>;
```


Defines whether the IP address is static or dynamic. Options are Static or Dynamic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L173">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the public ip.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L177">property reverseFqdn</a>
</h3>

```typescript
reverseFqdn?: pulumi.Input<string>;
```


A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L181">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU of the Public IP. Accepted values are `Basic` and `Standard`. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L185">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/publicIp.ts#L189">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<string>;
```


A collection containing the availability zone to allocate the Public IP in.

<h2 class="pdoc-module-header" id="RouteArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L124">interface RouteArgs</a>
</h2>

The set of arguments for constructing a Route resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L128">property addressPrefix</a>
</h3>

```typescript
addressPrefix: pulumi.Input<string>;
```


The destination CIDR to which the route applies, such as `10.1.0.0/16`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L132">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L136">property nextHopInIpAddress</a>
</h3>

```typescript
nextHopInIpAddress?: pulumi.Input<string>;
```


Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is `VirtualAppliance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L140">property nextHopType</a>
</h3>

```typescript
nextHopType: pulumi.Input<string>;
```


The type of Azure hop the packet should be sent to. Possible values are `VirtualNetworkGateway`, `VnetLocal`, `Internet`, `VirtualAppliance` and `None`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L144">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L148">property routeTableName</a>
</h3>

```typescript
routeTableName: pulumi.Input<string>;
```


The name of the route table within which create the route. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="RouteState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L94">interface RouteState</a>
</h2>

Input properties used for looking up and filtering Route resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L98">property addressPrefix</a>
</h3>

```typescript
addressPrefix?: pulumi.Input<string>;
```


The destination CIDR to which the route applies, such as `10.1.0.0/16`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L102">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L106">property nextHopInIpAddress</a>
</h3>

```typescript
nextHopInIpAddress?: pulumi.Input<string>;
```


Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is `VirtualAppliance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L110">property nextHopType</a>
</h3>

```typescript
nextHopType?: pulumi.Input<string>;
```


The type of Azure hop the packet should be sent to. Possible values are `VirtualNetworkGateway`, `VnetLocal`, `Internet`, `VirtualAppliance` and `None`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L114">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the route. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/route.ts#L118">property routeTableName</a>
</h3>

```typescript
routeTableName?: pulumi.Input<string>;
```


The name of the route table within which create the route. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="RouteTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L128">interface RouteTableArgs</a>
</h2>

The set of arguments for constructing a RouteTable resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L132">property disableBgpRoutePropagation</a>
</h3>

```typescript
disableBgpRoutePropagation?: pulumi.Input<boolean>;
```


Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L136">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the route table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L144">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the route table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L148">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to define multiple routes. Each `route` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L152">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="RouteTableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L94">interface RouteTableState</a>
</h2>

Input properties used for looking up and filtering RouteTable resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L98">property disableBgpRoutePropagation</a>
</h3>

```typescript
disableBgpRoutePropagation?: pulumi.Input<boolean>;
```


Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L102">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the route table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L110">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the route table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L114">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to define multiple routes. Each `route` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L118">property subnets</a>
</h3>

```typescript
subnets?: pulumi.Input<pulumi.Input<string>[]>;
```


The collection of Subnets associated with this route table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/routeTable.ts#L122">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SubnetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L145">interface SubnetArgs</a>
</h2>

The set of arguments for constructing a Subnet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L149">property addressPrefix</a>
</h3>

```typescript
addressPrefix: pulumi.Input<string>;
```


The address prefix to use for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L153">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations?: pulumi.Input<pulumi.Input<string>[]>;
```


The collection of IP Configurations with IPs within this subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L157">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L161">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId?: pulumi.Input<string>;
```


The ID of the Network Security Group to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L165">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L169">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The ID of the Route Table to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L173">property serviceEndpoints</a>
</h3>

```typescript
serviceEndpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of Service endpoints to associate with the subnet. Possible values include: `Microsoft.AzureActiveDirectory`, `Microsoft.AzureCosmosDB`, `Microsoft.EventHub`, `Microsoft.KeyVault`, `Microsoft.ServiceBus`, `Microsoft.Sql` and `Microsoft.Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L177">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName: pulumi.Input<string>;
```


The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubnetNetworkSecurityGroupAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L80">interface SubnetNetworkSecurityGroupAssociationArgs</a>
</h2>

The set of arguments for constructing a SubnetNetworkSecurityGroupAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L84">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId: pulumi.Input<string>;
```


The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L88">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The ID of the Subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubnetNetworkSecurityGroupAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L66">interface SubnetNetworkSecurityGroupAssociationState</a>
</h2>

Input properties used for looking up and filtering SubnetNetworkSecurityGroupAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L70">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId?: pulumi.Input<string>;
```


The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetNetworkSecurityGroupAssociation.ts#L74">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The ID of the Subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubnetRouteTableAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L80">interface SubnetRouteTableAssociationArgs</a>
</h2>

The set of arguments for constructing a SubnetRouteTableAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L84">property routeTableId</a>
</h3>

```typescript
routeTableId: pulumi.Input<string>;
```


The ID of the Route Table which should be associated with the Subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L88">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The ID of the Subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubnetRouteTableAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L66">interface SubnetRouteTableAssociationState</a>
</h2>

Input properties used for looking up and filtering SubnetRouteTableAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L70">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The ID of the Route Table which should be associated with the Subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnetRouteTableAssociation.ts#L74">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The ID of the Subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubnetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L107">interface SubnetState</a>
</h2>

Input properties used for looking up and filtering Subnet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L111">property addressPrefix</a>
</h3>

```typescript
addressPrefix?: pulumi.Input<string>;
```


The address prefix to use for the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L115">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations?: pulumi.Input<pulumi.Input<string>[]>;
```


The collection of IP Configurations with IPs within this subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L123">property networkSecurityGroupId</a>
</h3>

```typescript
networkSecurityGroupId?: pulumi.Input<string>;
```


The ID of the Network Security Group to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L127">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L131">property routeTableId</a>
</h3>

```typescript
routeTableId?: pulumi.Input<string>;
```


The ID of the Route Table to associate with the subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L135">property serviceEndpoints</a>
</h3>

```typescript
serviceEndpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of Service endpoints to associate with the subnet. Possible values include: `Microsoft.AzureActiveDirectory`, `Microsoft.AzureCosmosDB`, `Microsoft.EventHub`, `Microsoft.KeyVault`, `Microsoft.ServiceBus`, `Microsoft.Sql` and `Microsoft.Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/subnet.ts#L139">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName?: pulumi.Input<string>;
```


The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L148">interface VirtualNetworkArgs</a>
</h2>

The set of arguments for constructing a VirtualNetwork resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L154">property addressSpaces</a>
</h3>

```typescript
addressSpaces: pulumi.Input<pulumi.Input<string>[]>;
```


The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L158">property dnsServers</a>
</h3>

```typescript
dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IP addresses of DNS servers

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L163">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the virtual network is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L168">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual network. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L173">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L178">property subnets</a>
</h3>

```typescript
subnets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to define multiple
subnets. Each `subnet` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L182">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L239">interface VirtualNetworkGatewayArgs</a>
</h2>

The set of arguments for constructing a VirtualNetworkGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L246">property activeActive</a>
</h3>

```typescript
activeActive?: pulumi.Input<boolean>;
```


If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L247">property bgpSettings</a>
</h3>

```typescript
bgpSettings?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L255">property defaultLocalNetworkGatewayId</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L260">property enableBgp</a>
</h3>

```typescript
enableBgp?: pulumi.Input<boolean>;
```


If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L266">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L271">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L276">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L282">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L291">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2` and `VpnGw3`
and depend on the `type` and `vpn_type` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L295">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L300">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L306">property vpnClientConfiguration</a>
</h3>

```typescript
vpnClientConfiguration?: pulumi.Input<{ ... }>;
```


A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L311">property vpnType</a>
</h3>

```typescript
vpnType?: pulumi.Input<string>;
```


The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayConnectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L262">interface VirtualNetworkGatewayConnectionArgs</a>
</h2>

The set of arguments for constructing a VirtualNetworkGatewayConnection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L268">property authorizationKey</a>
</h3>

```typescript
authorizationKey?: pulumi.Input<string>;
```


The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L273">property enableBgp</a>
</h3>

```typescript
enableBgp?: pulumi.Input<boolean>;
```


If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L279">property expressRouteCircuitId</a>
</h3>

```typescript
expressRouteCircuitId?: pulumi.Input<string>;
```


The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L285">property ipsecPolicy</a>
</h3>

```typescript
ipsecPolicy?: pulumi.Input<{ ... }>;
```


A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L290">property localNetworkGatewayId</a>
</h3>

```typescript
localNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L295">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location/region where the connection is
located. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L300">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection. Changing the name forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L307">property peerVirtualNetworkGatewayId</a>
</h3>

```typescript
peerVirtualNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L312">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L316">property routingWeight</a>
</h3>

```typescript
routingWeight?: pulumi.Input<number>;
```


The routing weight. Defaults to `10`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L322">property sharedKey</a>
</h3>

```typescript
sharedKey?: pulumi.Input<string>;
```


The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L326">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L334">property type</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L340">property usePolicyBasedTrafficSelectors</a>
</h3>

```typescript
usePolicyBasedTrafficSelectors?: pulumi.Input<boolean>;
```


If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L346">property virtualNetworkGatewayId</a>
</h3>

```typescript
virtualNetworkGatewayId: pulumi.Input<string>;
```


The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayConnectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L172">interface VirtualNetworkGatewayConnectionState</a>
</h2>

Input properties used for looking up and filtering VirtualNetworkGatewayConnection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L178">property authorizationKey</a>
</h3>

```typescript
authorizationKey?: pulumi.Input<string>;
```


The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L183">property enableBgp</a>
</h3>

```typescript
enableBgp?: pulumi.Input<boolean>;
```


If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L189">property expressRouteCircuitId</a>
</h3>

```typescript
expressRouteCircuitId?: pulumi.Input<string>;
```


The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L195">property ipsecPolicy</a>
</h3>

```typescript
ipsecPolicy?: pulumi.Input<{ ... }>;
```


A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L200">property localNetworkGatewayId</a>
</h3>

```typescript
localNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L205">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the connection is
located. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L210">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection. Changing the name forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L217">property peerVirtualNetworkGatewayId</a>
</h3>

```typescript
peerVirtualNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L222">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L226">property routingWeight</a>
</h3>

```typescript
routingWeight?: pulumi.Input<number>;
```


The routing weight. Defaults to `10`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L232">property sharedKey</a>
</h3>

```typescript
sharedKey?: pulumi.Input<string>;
```


The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L236">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L244">property type</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L250">property usePolicyBasedTrafficSelectors</a>
</h3>

```typescript
usePolicyBasedTrafficSelectors?: pulumi.Input<boolean>;
```


If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGatewayConnection.ts#L256">property virtualNetworkGatewayId</a>
</h3>

```typescript
virtualNetworkGatewayId?: pulumi.Input<string>;
```


The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L161">interface VirtualNetworkGatewayState</a>
</h2>

Input properties used for looking up and filtering VirtualNetworkGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L168">property activeActive</a>
</h3>

```typescript
activeActive?: pulumi.Input<boolean>;
```


If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L169">property bgpSettings</a>
</h3>

```typescript
bgpSettings?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L177">property defaultLocalNetworkGatewayId</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L182">property enableBgp</a>
</h3>

```typescript
enableBgp?: pulumi.Input<boolean>;
```


If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L188">property ipConfigurations</a>
</h3>

```typescript
ipConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L193">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L198">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L204">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L213">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2` and `VpnGw3`
and depend on the `type` and `vpn_type` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L217">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L222">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L228">property vpnClientConfiguration</a>
</h3>

```typescript
vpnClientConfiguration?: pulumi.Input<{ ... }>;
```


A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkGateway.ts#L233">property vpnType</a>
</h3>

```typescript
vpnType?: pulumi.Input<string>;
```


The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.

<h2 class="pdoc-module-header" id="VirtualNetworkPeeringArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L170">interface VirtualNetworkPeeringArgs</a>
</h2>

The set of arguments for constructing a VirtualNetworkPeering resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L175">property allowForwardedTraffic</a>
</h3>

```typescript
allowForwardedTraffic?: pulumi.Input<boolean>;
```


Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L180">property allowGatewayTransit</a>
</h3>

```typescript
allowGatewayTransit?: pulumi.Input<boolean>;
```


Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L186">property allowVirtualNetworkAccess</a>
</h3>

```typescript
allowVirtualNetworkAccess?: pulumi.Input<boolean>;
```


Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L191">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual network peering. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L196">property remoteVirtualNetworkId</a>
</h3>

```typescript
remoteVirtualNetworkId: pulumi.Input<string>;
```


The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L202">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L211">property useRemoteGateways</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L216">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName: pulumi.Input<string>;
```


The name of the virtual network. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkPeeringState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L118">interface VirtualNetworkPeeringState</a>
</h2>

Input properties used for looking up and filtering VirtualNetworkPeering resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L123">property allowForwardedTraffic</a>
</h3>

```typescript
allowForwardedTraffic?: pulumi.Input<boolean>;
```


Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L128">property allowGatewayTransit</a>
</h3>

```typescript
allowGatewayTransit?: pulumi.Input<boolean>;
```


Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L134">property allowVirtualNetworkAccess</a>
</h3>

```typescript
allowVirtualNetworkAccess?: pulumi.Input<boolean>;
```


Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual network peering. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L144">property remoteVirtualNetworkId</a>
</h3>

```typescript
remoteVirtualNetworkId?: pulumi.Input<string>;
```


The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L150">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L159">property useRemoteGateways</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetworkPeering.ts#L164">property virtualNetworkName</a>
</h3>

```typescript
virtualNetworkName?: pulumi.Input<string>;
```


The name of the virtual network. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="VirtualNetworkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L108">interface VirtualNetworkState</a>
</h2>

Input properties used for looking up and filtering VirtualNetwork resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L114">property addressSpaces</a>
</h3>

```typescript
addressSpaces?: pulumi.Input<pulumi.Input<string>[]>;
```


The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L118">property dnsServers</a>
</h3>

```typescript
dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IP addresses of DNS servers

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L123">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location/region where the virtual network is
created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual network. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L133">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L138">property subnets</a>
</h3>

```typescript
subnets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to define multiple
subnets. Each `subnet` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/network/virtualNetwork.ts#L142">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

