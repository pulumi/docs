---
title: Module directconnect
---

<a href="../index.html">@pulumi/aws</a> &gt; directconnect

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Connection">class Connection</a>
* <a href="#ConnectionAssociation">class ConnectionAssociation</a>
* <a href="#Gateway">class Gateway</a>
* <a href="#GatewayAssociation">class GatewayAssociation</a>
* <a href="#HostedPrivateVirtualInterface">class HostedPrivateVirtualInterface</a>
* <a href="#HostedPrivateVirtualInterfaceAccepter">class HostedPrivateVirtualInterfaceAccepter</a>
* <a href="#HostedPublicVirtualInterface">class HostedPublicVirtualInterface</a>
* <a href="#HostedPublicVirtualInterfaceAccepter">class HostedPublicVirtualInterfaceAccepter</a>
* <a href="#LinkAggregationGroup">class LinkAggregationGroup</a>
* <a href="#PrivateVirtualInterface">class PrivateVirtualInterface</a>
* <a href="#PublicVirtualInterface">class PublicVirtualInterface</a>
* <a href="#getGateway">function getGateway</a>
* <a href="#ConnectionArgs">interface ConnectionArgs</a>
* <a href="#ConnectionAssociationArgs">interface ConnectionAssociationArgs</a>
* <a href="#ConnectionAssociationState">interface ConnectionAssociationState</a>
* <a href="#ConnectionState">interface ConnectionState</a>
* <a href="#GatewayArgs">interface GatewayArgs</a>
* <a href="#GatewayAssociationArgs">interface GatewayAssociationArgs</a>
* <a href="#GatewayAssociationState">interface GatewayAssociationState</a>
* <a href="#GatewayState">interface GatewayState</a>
* <a href="#GetGatewayArgs">interface GetGatewayArgs</a>
* <a href="#GetGatewayResult">interface GetGatewayResult</a>
* <a href="#HostedPrivateVirtualInterfaceAccepterArgs">interface HostedPrivateVirtualInterfaceAccepterArgs</a>
* <a href="#HostedPrivateVirtualInterfaceAccepterState">interface HostedPrivateVirtualInterfaceAccepterState</a>
* <a href="#HostedPrivateVirtualInterfaceArgs">interface HostedPrivateVirtualInterfaceArgs</a>
* <a href="#HostedPrivateVirtualInterfaceState">interface HostedPrivateVirtualInterfaceState</a>
* <a href="#HostedPublicVirtualInterfaceAccepterArgs">interface HostedPublicVirtualInterfaceAccepterArgs</a>
* <a href="#HostedPublicVirtualInterfaceAccepterState">interface HostedPublicVirtualInterfaceAccepterState</a>
* <a href="#HostedPublicVirtualInterfaceArgs">interface HostedPublicVirtualInterfaceArgs</a>
* <a href="#HostedPublicVirtualInterfaceState">interface HostedPublicVirtualInterfaceState</a>
* <a href="#LinkAggregationGroupArgs">interface LinkAggregationGroupArgs</a>
* <a href="#LinkAggregationGroupState">interface LinkAggregationGroupState</a>
* <a href="#PrivateVirtualInterfaceArgs">interface PrivateVirtualInterfaceArgs</a>
* <a href="#PrivateVirtualInterfaceState">interface PrivateVirtualInterfaceState</a>
* <a href="#PublicVirtualInterfaceArgs">interface PublicVirtualInterfaceArgs</a>
* <a href="#PublicVirtualInterfaceState">interface PublicVirtualInterfaceState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts">directconnect/connection.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts">directconnect/connectionAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts">directconnect/gateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts">directconnect/gatewayAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/getGateway.ts">directconnect/getGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts">directconnect/hostedPrivateVirtualInterface.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts">directconnect/hostedPrivateVirtualInterfaceAccepter.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts">directconnect/hostedPublicVirtualInterface.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts">directconnect/hostedPublicVirtualInterfaceAccepter.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts">directconnect/linkAggregationGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts">directconnect/privateVirtualInterface.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts">directconnect/publicVirtualInterface.ts</a> 


<h2 class="pdoc-module-header" id="Connection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L12">class Connection</a>
</h2>

Provides a Connection of Direct Connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L44">constructor</a>
</h3>

```typescript
new Connection(name: string, args: ConnectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Connection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConnectionState): Connection
```


Get an existing Connection resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L32">property bandwidth</a>
</h3>

```typescript
public bandwidth: pulumi.Output<string>;
```


The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L36">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L40">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L44">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ConnectionAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L10">class ConnectionAssociation</a>
</h2>

Associates a Direct Connect Connection with a LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L30">constructor</a>
</h3>

```typescript
new ConnectionAssociation(name: string, args: ConnectionAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ConnectionAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConnectionAssociationState): ConnectionAssociation
```


Get an existing ConnectionAssociation resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L26">property connectionId</a>
</h3>

```typescript
public connectionId: pulumi.Output<string>;
```


The ID of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L30">property lagId</a>
</h3>

```typescript
public lagId: pulumi.Output<string>;
```


The ID of the LAG with which to associate the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Gateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L10">class Gateway</a>
</h2>

Provides a Direct Connect Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L30">constructor</a>
</h3>

```typescript
new Gateway(name: string, args: GatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Gateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GatewayState): Gateway
```


Get an existing Gateway resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L26">property amazonSideAsn</a>
</h3>

```typescript
public amazonSideAsn: pulumi.Output<string>;
```


The ASN to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="GatewayAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L10">class GatewayAssociation</a>
</h2>

Associates a Direct Connect Gateway with a VGW.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L30">constructor</a>
</h3>

```typescript
new GatewayAssociation(name: string, args: GatewayAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GatewayAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GatewayAssociationState): GatewayAssociation
```


Get an existing GatewayAssociation resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L26">property dxGatewayId</a>
</h3>

```typescript
public dxGatewayId: pulumi.Output<string>;
```


The ID of the Direct Connect Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L30">property vpnGatewayId</a>
</h3>

```typescript
public vpnGatewayId: pulumi.Output<string>;
```


The ID of the VGW with which to associate the gateway.

<h2 class="pdoc-module-header" id="HostedPrivateVirtualInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L11">class HostedPrivateVirtualInterface</a>
</h2>

Provides a Direct Connect hosted private virtual interface resource. This resource represents the allocator's side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L63">constructor</a>
</h3>

```typescript
new HostedPrivateVirtualInterface(name: string, args: HostedPrivateVirtualInterfaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HostedPrivateVirtualInterface resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HostedPrivateVirtualInterfaceState): HostedPrivateVirtualInterface
```


Get an existing HostedPrivateVirtualInterface resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L27">property addressFamily</a>
</h3>

```typescript
public addressFamily: pulumi.Output<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L31">property amazonAddress</a>
</h3>

```typescript
public amazonAddress: pulumi.Output<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L35">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L39">property bgpAsn</a>
</h3>

```typescript
public bgpAsn: pulumi.Output<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L43">property bgpAuthKey</a>
</h3>

```typescript
public bgpAuthKey: pulumi.Output<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L47">property connectionId</a>
</h3>

```typescript
public connectionId: pulumi.Output<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L51">property customerAddress</a>
</h3>

```typescript
public customerAddress: pulumi.Output<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L55">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L59">property ownerAccountId</a>
</h3>

```typescript
public ownerAccountId: pulumi.Output<string>;
```


The AWS account that will own the new virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L63">property vlan</a>
</h3>

```typescript
public vlan: pulumi.Output<number>;
```


The VLAN ID.

<h2 class="pdoc-module-header" id="HostedPrivateVirtualInterfaceAccepter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L13">class HostedPrivateVirtualInterfaceAccepter</a>
</h2>

Provides a resource to manage the accepter's side of a Direct Connect hosted private virtual interface.
This resource accepts ownership of a private virtual interface created by another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L45">constructor</a>
</h3>

```typescript
new HostedPrivateVirtualInterfaceAccepter(name: string, args: HostedPrivateVirtualInterfaceAccepterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HostedPrivateVirtualInterfaceAccepter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HostedPrivateVirtualInterfaceAccepterState): HostedPrivateVirtualInterfaceAccepter
```


Get an existing HostedPrivateVirtualInterfaceAccepter resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L33">property dxGatewayId</a>
</h3>

```typescript
public dxGatewayId: pulumi.Output<string | undefined>;
```


The ID of the Direct Connect gateway to which to connect the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L41">property virtualInterfaceId</a>
</h3>

```typescript
public virtualInterfaceId: pulumi.Output<string>;
```


The ID of the Direct Connect virtual interface to accept.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L45">property vpnGatewayId</a>
</h3>

```typescript
public vpnGatewayId: pulumi.Output<string | undefined>;
```


The ID of the virtual private gateway to which to connect the virtual interface.

<h2 class="pdoc-module-header" id="HostedPublicVirtualInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L11">class HostedPublicVirtualInterface</a>
</h2>

Provides a Direct Connect hosted public virtual interface resource. This resource represents the allocator's side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L67">constructor</a>
</h3>

```typescript
new HostedPublicVirtualInterface(name: string, args: HostedPublicVirtualInterfaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HostedPublicVirtualInterface resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HostedPublicVirtualInterfaceState): HostedPublicVirtualInterface
```


Get an existing HostedPublicVirtualInterface resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L27">property addressFamily</a>
</h3>

```typescript
public addressFamily: pulumi.Output<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L31">property amazonAddress</a>
</h3>

```typescript
public amazonAddress: pulumi.Output<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L35">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L39">property bgpAsn</a>
</h3>

```typescript
public bgpAsn: pulumi.Output<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L43">property bgpAuthKey</a>
</h3>

```typescript
public bgpAuthKey: pulumi.Output<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L47">property connectionId</a>
</h3>

```typescript
public connectionId: pulumi.Output<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L51">property customerAddress</a>
</h3>

```typescript
public customerAddress: pulumi.Output<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L55">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L59">property ownerAccountId</a>
</h3>

```typescript
public ownerAccountId: pulumi.Output<string>;
```


The AWS account that will own the new virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L63">property routeFilterPrefixes</a>
</h3>

```typescript
public routeFilterPrefixes: pulumi.Output<string[]>;
```


A list of routes to be advertised to the AWS network in this region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L67">property vlan</a>
</h3>

```typescript
public vlan: pulumi.Output<number>;
```


The VLAN ID.

<h2 class="pdoc-module-header" id="HostedPublicVirtualInterfaceAccepter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L13">class HostedPublicVirtualInterfaceAccepter</a>
</h2>

Provides a resource to manage the accepter's side of a Direct Connect hosted public virtual interface.
This resource accepts ownership of a public virtual interface created by another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L37">constructor</a>
</h3>

```typescript
new HostedPublicVirtualInterfaceAccepter(name: string, args: HostedPublicVirtualInterfaceAccepterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HostedPublicVirtualInterfaceAccepter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HostedPublicVirtualInterfaceAccepterState): HostedPublicVirtualInterfaceAccepter
```


Get an existing HostedPublicVirtualInterfaceAccepter resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L33">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L37">property virtualInterfaceId</a>
</h3>

```typescript
public virtualInterfaceId: pulumi.Output<string>;
```


The ID of the Direct Connect virtual interface to accept.

<h2 class="pdoc-module-header" id="LinkAggregationGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L12">class LinkAggregationGroup</a>
</h2>

Provides a Direct Connect LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L52">constructor</a>
</h3>

```typescript
new LinkAggregationGroup(name: string, args: LinkAggregationGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LinkAggregationGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LinkAggregationGroupState): LinkAggregationGroup
```


Get an existing LinkAggregationGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L32">property connectionsBandwidth</a>
</h3>

```typescript
public connectionsBandwidth: pulumi.Output<string>;
```


The bandwidth of the individual physical connections bundled by the LAG. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L36">property forceDestroy</a>
</h3>

```typescript
public forceDestroy: pulumi.Output<boolean | undefined>;
```


A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L40">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The AWS Direct Connect location in which the LAG should be allocated. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L48">property numberOfConnections</a>
</h3>

```typescript
public numberOfConnections: pulumi.Output<number>;
```


The number of physical connections initially provisioned and bundled by the LAG. Use `aws_dx_connection` and `aws_dx_connection_association` resources instead. Default connections will be removed as part of LAG creation automatically in future versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L52">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PrivateVirtualInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L12">class PrivateVirtualInterface</a>
</h2>

Provides a Direct Connect private virtual interface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L72">constructor</a>
</h3>

```typescript
new PrivateVirtualInterface(name: string, args: PrivateVirtualInterfaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PrivateVirtualInterface resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PrivateVirtualInterfaceState): PrivateVirtualInterface
```


Get an existing PrivateVirtualInterface resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L28">property addressFamily</a>
</h3>

```typescript
public addressFamily: pulumi.Output<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L32">property amazonAddress</a>
</h3>

```typescript
public amazonAddress: pulumi.Output<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L36">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L40">property bgpAsn</a>
</h3>

```typescript
public bgpAsn: pulumi.Output<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L44">property bgpAuthKey</a>
</h3>

```typescript
public bgpAuthKey: pulumi.Output<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L48">property connectionId</a>
</h3>

```typescript
public connectionId: pulumi.Output<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L52">property customerAddress</a>
</h3>

```typescript
public customerAddress: pulumi.Output<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L56">property dxGatewayId</a>
</h3>

```typescript
public dxGatewayId: pulumi.Output<string | undefined>;
```


The ID of the Direct Connect gateway to which to connect the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L64">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L68">property vlan</a>
</h3>

```typescript
public vlan: pulumi.Output<number>;
```


The VLAN ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L72">property vpnGatewayId</a>
</h3>

```typescript
public vpnGatewayId: pulumi.Output<string | undefined>;
```


The ID of the virtual private gateway to which to connect the virtual interface.

<h2 class="pdoc-module-header" id="PublicVirtualInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L10">class PublicVirtualInterface</a>
</h2>

Provides a Direct Connect public virtual interface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L66">constructor</a>
</h3>

```typescript
new PublicVirtualInterface(name: string, args: PublicVirtualInterfaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PublicVirtualInterface resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PublicVirtualInterfaceState): PublicVirtualInterface
```


Get an existing PublicVirtualInterface resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L26">property addressFamily</a>
</h3>

```typescript
public addressFamily: pulumi.Output<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L30">property amazonAddress</a>
</h3>

```typescript
public amazonAddress: pulumi.Output<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L34">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L38">property bgpAsn</a>
</h3>

```typescript
public bgpAsn: pulumi.Output<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L42">property bgpAuthKey</a>
</h3>

```typescript
public bgpAuthKey: pulumi.Output<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L46">property connectionId</a>
</h3>

```typescript
public connectionId: pulumi.Output<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L50">property customerAddress</a>
</h3>

```typescript
public customerAddress: pulumi.Output<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L58">property routeFilterPrefixes</a>
</h3>

```typescript
public routeFilterPrefixes: pulumi.Output<string[]>;
```


A list of routes to be advertised to the AWS network in this region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L62">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L66">property vlan</a>
</h3>

```typescript
public vlan: pulumi.Output<number>;
```


The VLAN ID.

<h2 class="pdoc-module-header" id="getGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/getGateway.ts#L10">function getGateway</a>
</h2>

```typescript
getGateway(args: GetGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetGatewayResult>
```


Retrieve information about a Direct Connect Gateway.

<h2 class="pdoc-module-header" id="ConnectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L110">interface ConnectionArgs</a>
</h2>

The set of arguments for constructing a Connection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L114">property bandwidth</a>
</h3>

```typescript
bandwidth: pulumi.Input<string>;
```


The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L118">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L126">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ConnectionAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L78">interface ConnectionAssociationArgs</a>
</h2>

The set of arguments for constructing a ConnectionAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L82">property connectionId</a>
</h3>

```typescript
connectionId: pulumi.Input<string>;
```


The ID of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L86">property lagId</a>
</h3>

```typescript
lagId: pulumi.Input<string>;
```


The ID of the LAG with which to associate the connection.

<h2 class="pdoc-module-header" id="ConnectionAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L64">interface ConnectionAssociationState</a>
</h2>

Input properties used for looking up and filtering ConnectionAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L68">property connectionId</a>
</h3>

```typescript
connectionId?: pulumi.Input<string>;
```


The ID of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L72">property lagId</a>
</h3>

```typescript
lagId?: pulumi.Input<string>;
```


The ID of the LAG with which to associate the connection.

<h2 class="pdoc-module-header" id="ConnectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L84">interface ConnectionState</a>
</h2>

Input properties used for looking up and filtering Connection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L88">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L92">property bandwidth</a>
</h3>

```typescript
bandwidth?: pulumi.Input<string>;
```


The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L96">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L104">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="GatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L75">interface GatewayArgs</a>
</h2>

The set of arguments for constructing a Gateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L79">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn: pulumi.Input<string>;
```


The ASN to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L83">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection.

<h2 class="pdoc-module-header" id="GatewayAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L78">interface GatewayAssociationArgs</a>
</h2>

The set of arguments for constructing a GatewayAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L82">property dxGatewayId</a>
</h3>

```typescript
dxGatewayId: pulumi.Input<string>;
```


The ID of the Direct Connect Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L86">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId: pulumi.Input<string>;
```


The ID of the VGW with which to associate the gateway.

<h2 class="pdoc-module-header" id="GatewayAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L64">interface GatewayAssociationState</a>
</h2>

Input properties used for looking up and filtering GatewayAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L68">property dxGatewayId</a>
</h3>

```typescript
dxGatewayId?: pulumi.Input<string>;
```


The ID of the Direct Connect Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gatewayAssociation.ts#L72">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId?: pulumi.Input<string>;
```


The ID of the VGW with which to associate the gateway.

<h2 class="pdoc-module-header" id="GatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L61">interface GatewayState</a>
</h2>

Input properties used for looking up and filtering Gateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L65">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn?: pulumi.Input<string>;
```


The ASN to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/gateway.ts#L69">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection.

<h2 class="pdoc-module-header" id="GetGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/getGateway.ts#L19">interface GetGatewayArgs</a>
</h2>

A collection of arguments for invoking getGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/getGateway.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


The name of the gateway to retrieve.

<h2 class="pdoc-module-header" id="GetGatewayResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/getGateway.ts#L29">interface GetGatewayResult</a>
</h2>

A collection of values returned by getGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/getGateway.ts#L33">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn: string;
```


The ASN on the Amazon side of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/getGateway.ts#L37">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="HostedPrivateVirtualInterfaceAccepterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L108">interface HostedPrivateVirtualInterfaceAccepterArgs</a>
</h2>

The set of arguments for constructing a HostedPrivateVirtualInterfaceAccepter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L112">property dxGatewayId</a>
</h3>

```typescript
dxGatewayId?: pulumi.Input<string>;
```


The ID of the Direct Connect gateway to which to connect the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L116">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L120">property virtualInterfaceId</a>
</h3>

```typescript
virtualInterfaceId: pulumi.Input<string>;
```


The ID of the Direct Connect virtual interface to accept.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L124">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId?: pulumi.Input<string>;
```


The ID of the virtual private gateway to which to connect the virtual interface.

<h2 class="pdoc-module-header" id="HostedPrivateVirtualInterfaceAccepterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L82">interface HostedPrivateVirtualInterfaceAccepterState</a>
</h2>

Input properties used for looking up and filtering HostedPrivateVirtualInterfaceAccepter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L86">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L90">property dxGatewayId</a>
</h3>

```typescript
dxGatewayId?: pulumi.Input<string>;
```


The ID of the Direct Connect gateway to which to connect the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L94">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L98">property virtualInterfaceId</a>
</h3>

```typescript
virtualInterfaceId?: pulumi.Input<string>;
```


The ID of the Direct Connect virtual interface to accept.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterfaceAccepter.ts#L102">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId?: pulumi.Input<string>;
```


The ID of the virtual private gateway to which to connect the virtual interface.

<h2 class="pdoc-module-header" id="HostedPrivateVirtualInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L168">interface HostedPrivateVirtualInterfaceArgs</a>
</h2>

The set of arguments for constructing a HostedPrivateVirtualInterface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L172">property addressFamily</a>
</h3>

```typescript
addressFamily: pulumi.Input<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L176">property amazonAddress</a>
</h3>

```typescript
amazonAddress?: pulumi.Input<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L180">property bgpAsn</a>
</h3>

```typescript
bgpAsn: pulumi.Input<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L184">property bgpAuthKey</a>
</h3>

```typescript
bgpAuthKey?: pulumi.Input<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L188">property connectionId</a>
</h3>

```typescript
connectionId: pulumi.Input<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L192">property customerAddress</a>
</h3>

```typescript
customerAddress?: pulumi.Input<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L196">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L200">property ownerAccountId</a>
</h3>

```typescript
ownerAccountId: pulumi.Input<string>;
```


The AWS account that will own the new virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L204">property vlan</a>
</h3>

```typescript
vlan: pulumi.Input<number>;
```


The VLAN ID.

<h2 class="pdoc-module-header" id="HostedPrivateVirtualInterfaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L122">interface HostedPrivateVirtualInterfaceState</a>
</h2>

Input properties used for looking up and filtering HostedPrivateVirtualInterface resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L126">property addressFamily</a>
</h3>

```typescript
addressFamily?: pulumi.Input<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L130">property amazonAddress</a>
</h3>

```typescript
amazonAddress?: pulumi.Input<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L134">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L138">property bgpAsn</a>
</h3>

```typescript
bgpAsn?: pulumi.Input<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L142">property bgpAuthKey</a>
</h3>

```typescript
bgpAuthKey?: pulumi.Input<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L146">property connectionId</a>
</h3>

```typescript
connectionId?: pulumi.Input<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L150">property customerAddress</a>
</h3>

```typescript
customerAddress?: pulumi.Input<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L154">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L158">property ownerAccountId</a>
</h3>

```typescript
ownerAccountId?: pulumi.Input<string>;
```


The AWS account that will own the new virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPrivateVirtualInterface.ts#L162">property vlan</a>
</h3>

```typescript
vlan?: pulumi.Input<number>;
```


The VLAN ID.

<h2 class="pdoc-module-header" id="HostedPublicVirtualInterfaceAccepterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L88">interface HostedPublicVirtualInterfaceAccepterArgs</a>
</h2>

The set of arguments for constructing a HostedPublicVirtualInterfaceAccepter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L92">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L96">property virtualInterfaceId</a>
</h3>

```typescript
virtualInterfaceId: pulumi.Input<string>;
```


The ID of the Direct Connect virtual interface to accept.

<h2 class="pdoc-module-header" id="HostedPublicVirtualInterfaceAccepterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L70">interface HostedPublicVirtualInterfaceAccepterState</a>
</h2>

Input properties used for looking up and filtering HostedPublicVirtualInterfaceAccepter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L74">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L78">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterfaceAccepter.ts#L82">property virtualInterfaceId</a>
</h3>

```typescript
virtualInterfaceId?: pulumi.Input<string>;
```


The ID of the Direct Connect virtual interface to accept.

<h2 class="pdoc-module-header" id="HostedPublicVirtualInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L181">interface HostedPublicVirtualInterfaceArgs</a>
</h2>

The set of arguments for constructing a HostedPublicVirtualInterface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L185">property addressFamily</a>
</h3>

```typescript
addressFamily: pulumi.Input<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L189">property amazonAddress</a>
</h3>

```typescript
amazonAddress?: pulumi.Input<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L193">property bgpAsn</a>
</h3>

```typescript
bgpAsn: pulumi.Input<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L197">property bgpAuthKey</a>
</h3>

```typescript
bgpAuthKey?: pulumi.Input<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L201">property connectionId</a>
</h3>

```typescript
connectionId: pulumi.Input<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L205">property customerAddress</a>
</h3>

```typescript
customerAddress?: pulumi.Input<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L209">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L213">property ownerAccountId</a>
</h3>

```typescript
ownerAccountId: pulumi.Input<string>;
```


The AWS account that will own the new virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L217">property routeFilterPrefixes</a>
</h3>

```typescript
routeFilterPrefixes: pulumi.Input<pulumi.Input<string>[]>;
```


A list of routes to be advertised to the AWS network in this region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L221">property vlan</a>
</h3>

```typescript
vlan: pulumi.Input<number>;
```


The VLAN ID.

<h2 class="pdoc-module-header" id="HostedPublicVirtualInterfaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L131">interface HostedPublicVirtualInterfaceState</a>
</h2>

Input properties used for looking up and filtering HostedPublicVirtualInterface resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L135">property addressFamily</a>
</h3>

```typescript
addressFamily?: pulumi.Input<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L139">property amazonAddress</a>
</h3>

```typescript
amazonAddress?: pulumi.Input<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L143">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L147">property bgpAsn</a>
</h3>

```typescript
bgpAsn?: pulumi.Input<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L151">property bgpAuthKey</a>
</h3>

```typescript
bgpAuthKey?: pulumi.Input<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L155">property connectionId</a>
</h3>

```typescript
connectionId?: pulumi.Input<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L159">property customerAddress</a>
</h3>

```typescript
customerAddress?: pulumi.Input<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L163">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L167">property ownerAccountId</a>
</h3>

```typescript
ownerAccountId?: pulumi.Input<string>;
```


The AWS account that will own the new virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L171">property routeFilterPrefixes</a>
</h3>

```typescript
routeFilterPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of routes to be advertised to the AWS network in this region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/hostedPublicVirtualInterface.ts#L175">property vlan</a>
</h3>

```typescript
vlan?: pulumi.Input<number>;
```


The VLAN ID.

<h2 class="pdoc-module-header" id="LinkAggregationGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L130">interface LinkAggregationGroupArgs</a>
</h2>

The set of arguments for constructing a LinkAggregationGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L134">property connectionsBandwidth</a>
</h3>

```typescript
connectionsBandwidth: pulumi.Input<string>;
```


The bandwidth of the individual physical connections bundled by the LAG. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L138">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L142">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The AWS Direct Connect location in which the LAG should be allocated. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L146">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L150">property numberOfConnections</a>
</h3>

```typescript
numberOfConnections?: pulumi.Input<number>;
```


The number of physical connections initially provisioned and bundled by the LAG. Use `aws_dx_connection` and `aws_dx_connection_association` resources instead. Default connections will be removed as part of LAG creation automatically in future versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L154">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LinkAggregationGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L96">interface LinkAggregationGroupState</a>
</h2>

Input properties used for looking up and filtering LinkAggregationGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L100">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L104">property connectionsBandwidth</a>
</h3>

```typescript
connectionsBandwidth?: pulumi.Input<string>;
```


The bandwidth of the individual physical connections bundled by the LAG. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L108">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L112">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The AWS Direct Connect location in which the LAG should be allocated. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L116">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L120">property numberOfConnections</a>
</h3>

```typescript
numberOfConnections?: pulumi.Input<number>;
```


The number of physical connections initially provisioned and bundled by the LAG. Use `aws_dx_connection` and `aws_dx_connection_association` resources instead. Default connections will be removed as part of LAG creation automatically in future versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L124">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="PrivateVirtualInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L186">interface PrivateVirtualInterfaceArgs</a>
</h2>

The set of arguments for constructing a PrivateVirtualInterface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L190">property addressFamily</a>
</h3>

```typescript
addressFamily: pulumi.Input<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L194">property amazonAddress</a>
</h3>

```typescript
amazonAddress?: pulumi.Input<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L198">property bgpAsn</a>
</h3>

```typescript
bgpAsn: pulumi.Input<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L202">property bgpAuthKey</a>
</h3>

```typescript
bgpAuthKey?: pulumi.Input<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L206">property connectionId</a>
</h3>

```typescript
connectionId: pulumi.Input<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L210">property customerAddress</a>
</h3>

```typescript
customerAddress?: pulumi.Input<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L214">property dxGatewayId</a>
</h3>

```typescript
dxGatewayId?: pulumi.Input<string>;
```


The ID of the Direct Connect gateway to which to connect the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L218">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L222">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L226">property vlan</a>
</h3>

```typescript
vlan: pulumi.Input<number>;
```


The VLAN ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L230">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId?: pulumi.Input<string>;
```


The ID of the virtual private gateway to which to connect the virtual interface.

<h2 class="pdoc-module-header" id="PrivateVirtualInterfaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L132">interface PrivateVirtualInterfaceState</a>
</h2>

Input properties used for looking up and filtering PrivateVirtualInterface resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L136">property addressFamily</a>
</h3>

```typescript
addressFamily?: pulumi.Input<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L140">property amazonAddress</a>
</h3>

```typescript
amazonAddress?: pulumi.Input<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L144">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L148">property bgpAsn</a>
</h3>

```typescript
bgpAsn?: pulumi.Input<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L152">property bgpAuthKey</a>
</h3>

```typescript
bgpAuthKey?: pulumi.Input<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L156">property connectionId</a>
</h3>

```typescript
connectionId?: pulumi.Input<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L160">property customerAddress</a>
</h3>

```typescript
customerAddress?: pulumi.Input<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L164">property dxGatewayId</a>
</h3>

```typescript
dxGatewayId?: pulumi.Input<string>;
```


The ID of the Direct Connect gateway to which to connect the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L168">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L172">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L176">property vlan</a>
</h3>

```typescript
vlan?: pulumi.Input<number>;
```


The VLAN ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/privateVirtualInterface.ts#L180">property vpnGatewayId</a>
</h3>

```typescript
vpnGatewayId?: pulumi.Input<string>;
```


The ID of the virtual private gateway to which to connect the virtual interface.

<h2 class="pdoc-module-header" id="PublicVirtualInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L177">interface PublicVirtualInterfaceArgs</a>
</h2>

The set of arguments for constructing a PublicVirtualInterface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L181">property addressFamily</a>
</h3>

```typescript
addressFamily: pulumi.Input<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L185">property amazonAddress</a>
</h3>

```typescript
amazonAddress?: pulumi.Input<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L189">property bgpAsn</a>
</h3>

```typescript
bgpAsn: pulumi.Input<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L193">property bgpAuthKey</a>
</h3>

```typescript
bgpAuthKey?: pulumi.Input<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L197">property connectionId</a>
</h3>

```typescript
connectionId: pulumi.Input<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L201">property customerAddress</a>
</h3>

```typescript
customerAddress?: pulumi.Input<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L205">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L209">property routeFilterPrefixes</a>
</h3>

```typescript
routeFilterPrefixes: pulumi.Input<pulumi.Input<string>[]>;
```


A list of routes to be advertised to the AWS network in this region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L213">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L217">property vlan</a>
</h3>

```typescript
vlan: pulumi.Input<number>;
```


The VLAN ID.

<h2 class="pdoc-module-header" id="PublicVirtualInterfaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L127">interface PublicVirtualInterfaceState</a>
</h2>

Input properties used for looking up and filtering PublicVirtualInterface resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L131">property addressFamily</a>
</h3>

```typescript
addressFamily?: pulumi.Input<string>;
```


The address family for the BGP peer. `ipv4 ` or `ipv6`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L135">property amazonAddress</a>
</h3>

```typescript
amazonAddress?: pulumi.Input<string>;
```


The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L139">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L143">property bgpAsn</a>
</h3>

```typescript
bgpAsn?: pulumi.Input<number>;
```


The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L147">property bgpAuthKey</a>
</h3>

```typescript
bgpAuthKey?: pulumi.Input<string>;
```


The authentication key for BGP configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L151">property connectionId</a>
</h3>

```typescript
connectionId?: pulumi.Input<string>;
```


The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L155">property customerAddress</a>
</h3>

```typescript
customerAddress?: pulumi.Input<string>;
```


The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name for the virtual interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L163">property routeFilterPrefixes</a>
</h3>

```typescript
routeFilterPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of routes to be advertised to the AWS network in this region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L167">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/publicVirtualInterface.ts#L171">property vlan</a>
</h3>

```typescript
vlan?: pulumi.Input<number>;
```


The VLAN ID.

