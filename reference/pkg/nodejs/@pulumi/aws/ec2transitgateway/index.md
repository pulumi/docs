---
title: Module ec2transitgateway
---

<a href="../index.html">@pulumi/aws</a> &gt; ec2transitgateway

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Route">class Route</a>
* <a href="#RouteTable">class RouteTable</a>
* <a href="#RouteTableAssociation">class RouteTableAssociation</a>
* <a href="#RouteTablePropagation">class RouteTablePropagation</a>
* <a href="#TransitGateway">class TransitGateway</a>
* <a href="#VpcAttachment">class VpcAttachment</a>
* <a href="#getRouteTable">function getRouteTable</a>
* <a href="#getTransitGateway">function getTransitGateway</a>
* <a href="#getVpcAttachment">function getVpcAttachment</a>
* <a href="#GetRouteTableArgs">interface GetRouteTableArgs</a>
* <a href="#GetRouteTableResult">interface GetRouteTableResult</a>
* <a href="#GetTransitGatewayArgs">interface GetTransitGatewayArgs</a>
* <a href="#GetTransitGatewayResult">interface GetTransitGatewayResult</a>
* <a href="#GetVpcAttachmentArgs">interface GetVpcAttachmentArgs</a>
* <a href="#GetVpcAttachmentResult">interface GetVpcAttachmentResult</a>
* <a href="#RouteArgs">interface RouteArgs</a>
* <a href="#RouteState">interface RouteState</a>
* <a href="#RouteTableArgs">interface RouteTableArgs</a>
* <a href="#RouteTableAssociationArgs">interface RouteTableAssociationArgs</a>
* <a href="#RouteTableAssociationState">interface RouteTableAssociationState</a>
* <a href="#RouteTablePropagationArgs">interface RouteTablePropagationArgs</a>
* <a href="#RouteTablePropagationState">interface RouteTablePropagationState</a>
* <a href="#RouteTableState">interface RouteTableState</a>
* <a href="#TransitGatewayArgs">interface TransitGatewayArgs</a>
* <a href="#TransitGatewayState">interface TransitGatewayState</a>
* <a href="#VpcAttachmentArgs">interface VpcAttachmentArgs</a>
* <a href="#VpcAttachmentState">interface VpcAttachmentState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts">ec2transitgateway/getRouteTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts">ec2transitgateway/getTransitGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts">ec2transitgateway/getVpcAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts">ec2transitgateway/route.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts">ec2transitgateway/routeTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts">ec2transitgateway/routeTableAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts">ec2transitgateway/routeTablePropagation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts">ec2transitgateway/transitGateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts">ec2transitgateway/vpcAttachment.ts</a> 


<h2 class="pdoc-module-header" id="Route">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L10">class Route</a>
</h2>

Manages an EC2 Transit Gateway Route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L34">constructor</a>
</h3>

```typescript
new Route(name: string, args: RouteArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Route resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteState): Route
```


Get an existing Route resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L26">property destinationCidrBlock</a>
</h3>

```typescript
public destinationCidrBlock: pulumi.Output<string>;
```


IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L30">property transitGatewayAttachmentId</a>
</h3>

```typescript
public transitGatewayAttachmentId: pulumi.Output<string>;
```


Identifier of EC2 Transit Gateway Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L34">property transitGatewayRouteTableId</a>
</h3>

```typescript
public transitGatewayRouteTableId: pulumi.Output<string>;
```


Identifier of EC2 Transit Gateway Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RouteTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L12">class RouteTable</a>
</h2>

Manages an EC2 Transit Gateway Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L40">constructor</a>
</h3>

```typescript
new RouteTable(name: string, args: RouteTableArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RouteTable resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteTableState): RouteTable
```


Get an existing RouteTable resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L28">property defaultAssociationRouteTable</a>
</h3>

```typescript
public defaultAssociationRouteTable: pulumi.Output<boolean>;
```


Boolean whether this is the default association route table for the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L32">property defaultPropagationRouteTable</a>
</h3>

```typescript
public defaultPropagationRouteTable: pulumi.Output<boolean>;
```


Boolean whether this is the default propagation route table for the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L36">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Key-value tags for the EC2 Transit Gateway Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L40">property transitGatewayId</a>
</h3>

```typescript
public transitGatewayId: pulumi.Output<string>;
```


Identifier of EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RouteTableAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L10">class RouteTableAssociation</a>
</h2>

Manages an EC2 Transit Gateway Route Table association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L38">constructor</a>
</h3>

```typescript
new RouteTableAssociation(name: string, args: RouteTableAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RouteTableAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteTableAssociationState): RouteTableAssociation
```


Get an existing RouteTableAssociation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L26">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


Identifier of the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L30">property resourceType</a>
</h3>

```typescript
public resourceType: pulumi.Output<string>;
```


Type of the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L34">property transitGatewayAttachmentId</a>
</h3>

```typescript
public transitGatewayAttachmentId: pulumi.Output<string>;
```


Identifier of EC2 Transit Gateway Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L38">property transitGatewayRouteTableId</a>
</h3>

```typescript
public transitGatewayRouteTableId: pulumi.Output<string>;
```


Identifier of EC2 Transit Gateway Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RouteTablePropagation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L10">class RouteTablePropagation</a>
</h2>

Manages an EC2 Transit Gateway Route Table propagation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L38">constructor</a>
</h3>

```typescript
new RouteTablePropagation(name: string, args: RouteTablePropagationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RouteTablePropagation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteTablePropagationState): RouteTablePropagation
```


Get an existing RouteTablePropagation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L26">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


Identifier of the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L30">property resourceType</a>
</h3>

```typescript
public resourceType: pulumi.Output<string>;
```


Type of the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L34">property transitGatewayAttachmentId</a>
</h3>

```typescript
public transitGatewayAttachmentId: pulumi.Output<string>;
```


Identifier of EC2 Transit Gateway Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L38">property transitGatewayRouteTableId</a>
</h3>

```typescript
public transitGatewayRouteTableId: pulumi.Output<string>;
```


Identifier of EC2 Transit Gateway Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TransitGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L12">class TransitGateway</a>
</h2>

Manages an EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L72">constructor</a>
</h3>

```typescript
new TransitGateway(name: string, args?: TransitGatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TransitGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TransitGatewayState): TransitGateway
```


Get an existing TransitGateway resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L28">property amazonSideAsn</a>
</h3>

```typescript
public amazonSideAsn: pulumi.Output<number | undefined>;
```


Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is `64512` to `65534` for 16-bit ASNs and `4200000000` to `4294967294` for 32-bit ASNs. Default value: `64512`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L32">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<ARN>;
```


EC2 Transit Gateway Amazon Resource Name (ARN)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L36">property associationDefaultRouteTableId</a>
</h3>

```typescript
public associationDefaultRouteTableId: pulumi.Output<string>;
```


Identifier of the default association route table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L40">property autoAcceptSharedAttachments</a>
</h3>

```typescript
public autoAcceptSharedAttachments: pulumi.Output<string | undefined>;
```


Whether resource attachment requests are automatically accepted. Valid values: `disable`, `enable`. Default value: `disable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L44">property defaultRouteTableAssociation</a>
</h3>

```typescript
public defaultRouteTableAssociation: pulumi.Output<string | undefined>;
```


Whether resource attachments are automatically associated with the default association route table. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L48">property defaultRouteTablePropagation</a>
</h3>

```typescript
public defaultRouteTablePropagation: pulumi.Output<string | undefined>;
```


Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L52">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L56">property dnsSupport</a>
</h3>

```typescript
public dnsSupport: pulumi.Output<string | undefined>;
```


Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L60">property ownerId</a>
</h3>

```typescript
public ownerId: pulumi.Output<string>;
```


Identifier of the AWS account that owns the EC2 Transit Gateway

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L64">property propagationDefaultRouteTableId</a>
</h3>

```typescript
public propagationDefaultRouteTableId: pulumi.Output<string>;
```


Identifier of the default propagation route table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L68">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Key-value tags for the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L72">property vpnEcmpSupport</a>
</h3>

```typescript
public vpnEcmpSupport: pulumi.Output<string | undefined>;
```


Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

<h2 class="pdoc-module-header" id="VpcAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L12">class VpcAttachment</a>
</h2>

Manages an EC2 Transit Gateway VPC Attachment. For examples of custom route table association and propagation, see the EC2 Transit Gateway Networking Examples Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L60">constructor</a>
</h3>

```typescript
new VpcAttachment(name: string, args: VpcAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcAttachmentState): VpcAttachment
```


Get an existing VpcAttachment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L28">property dnsSupport</a>
</h3>

```typescript
public dnsSupport: pulumi.Output<string | undefined>;
```


Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L32">property ipv6Support</a>
</h3>

```typescript
public ipv6Support: pulumi.Output<string | undefined>;
```


Whether IPv6 support is enabled. Valid values: `disable`, `enable`. Default value: `disable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L36">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


Identifiers of EC2 Subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L40">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Key-value tags for the EC2 Transit Gateway VPC Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L44">property transitGatewayDefaultRouteTableAssociation</a>
</h3>

```typescript
public transitGatewayDefaultRouteTableAssociation: pulumi.Output<boolean | undefined>;
```


Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. Default value: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L48">property transitGatewayDefaultRouteTablePropagation</a>
</h3>

```typescript
public transitGatewayDefaultRouteTablePropagation: pulumi.Output<boolean | undefined>;
```


Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. Default value: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L52">property transitGatewayId</a>
</h3>

```typescript
public transitGatewayId: pulumi.Output<string>;
```


Identifier of EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L56">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


Identifier of EC2 VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L60">property vpcOwnerId</a>
</h3>

```typescript
public vpcOwnerId: pulumi.Output<string>;
```


Identifier of the AWS account that owns the EC2 VPC.

<h2 class="pdoc-module-header" id="getRouteTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L10">function getRouteTable</a>
</h2>

```typescript
getRouteTable(args?: GetRouteTableArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteTableResult>
```


Get information on an EC2 Transit Gateway Route Table.

<h2 class="pdoc-module-header" id="getTransitGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L10">function getTransitGateway</a>
</h2>

```typescript
getTransitGateway(args?: GetTransitGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetTransitGatewayResult>
```


Get information on an EC2 Transit Gateway.

<h2 class="pdoc-module-header" id="getVpcAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L10">function getVpcAttachment</a>
</h2>

```typescript
getVpcAttachment(args?: GetVpcAttachmentArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcAttachmentResult>
```


Get information on an EC2 Transit Gateway VPC Attachment.

<h2 class="pdoc-module-header" id="GetRouteTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L22">interface GetRouteTableArgs</a>
</h2>

A collection of arguments for invoking getRouteTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L26">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more configuration blocks containing name-values filters. Detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L30">property id</a>
</h3>

```typescript
id?: string;
```


Identifier of the EC2 Transit Gateway Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L31">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetRouteTableResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L37">interface GetRouteTableResult</a>
</h2>

A collection of values returned by getRouteTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L41">property defaultAssociationRouteTable</a>
</h3>

```typescript
defaultAssociationRouteTable: boolean;
```


Boolean whether this is the default association route table for the EC2 Transit Gateway

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L45">property defaultPropagationRouteTable</a>
</h3>

```typescript
defaultPropagationRouteTable: boolean;
```


Boolean whether this is the default propagation route table for the EC2 Transit Gateway

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L49">property tags</a>
</h3>

```typescript
tags: { ... };
```


Key-value tags for the EC2 Transit Gateway Route Table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getRouteTable.ts#L53">property transitGatewayId</a>
</h3>

```typescript
transitGatewayId: string;
```


EC2 Transit Gateway identifier

<h2 class="pdoc-module-header" id="GetTransitGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L22">interface GetTransitGatewayArgs</a>
</h2>

A collection of arguments for invoking getTransitGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L26">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more configuration blocks containing name-values filters. Detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L30">property id</a>
</h3>

```typescript
id?: string;
```


Identifier of the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L31">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetTransitGatewayResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L37">interface GetTransitGatewayResult</a>
</h2>

A collection of values returned by getTransitGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L41">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn: number;
```


Private Autonomous System Number (ASN) for the Amazon side of a BGP session

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L45">property arn</a>
</h3>

```typescript
arn: string;
```


EC2 Transit Gateway Amazon Resource Name (ARN)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L49">property associationDefaultRouteTableId</a>
</h3>

```typescript
associationDefaultRouteTableId: string;
```


Identifier of the default association route table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L53">property autoAcceptSharedAttachments</a>
</h3>

```typescript
autoAcceptSharedAttachments: string;
```


Whether resource attachment requests are automatically accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L57">property defaultRouteTableAssociation</a>
</h3>

```typescript
defaultRouteTableAssociation: string;
```


Whether resource attachments are automatically associated with the default association route table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L61">property defaultRouteTablePropagation</a>
</h3>

```typescript
defaultRouteTablePropagation: string;
```


Whether resource attachments automatically propagate routes to the default propagation route table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L65">property description</a>
</h3>

```typescript
description: string;
```


Description of the EC2 Transit Gateway

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L69">property dnsSupport</a>
</h3>

```typescript
dnsSupport: string;
```


Whether DNS support is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L73">property ownerId</a>
</h3>

```typescript
ownerId: string;
```


Identifier of the AWS account that owns the EC2 Transit Gateway

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L77">property propagationDefaultRouteTableId</a>
</h3>

```typescript
propagationDefaultRouteTableId: string;
```


Identifier of the default propagation route table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L81">property tags</a>
</h3>

```typescript
tags: { ... };
```


Key-value tags for the EC2 Transit Gateway

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getTransitGateway.ts#L85">property vpnEcmpSupport</a>
</h3>

```typescript
vpnEcmpSupport: string;
```


Whether VPN Equal Cost Multipath Protocol support is enabled.

<h2 class="pdoc-module-header" id="GetVpcAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L22">interface GetVpcAttachmentArgs</a>
</h2>

A collection of arguments for invoking getVpcAttachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L26">property filters</a>
</h3>

```typescript
filters?: { ... }[];
```


One or more configuration blocks containing name-values filters. Detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L30">property id</a>
</h3>

```typescript
id?: string;
```


Identifier of the EC2 Transit Gateway VPC Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L31">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetVpcAttachmentResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L37">interface GetVpcAttachmentResult</a>
</h2>

A collection of values returned by getVpcAttachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L41">property dnsSupport</a>
</h3>

```typescript
dnsSupport: string;
```


Whether DNS support is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L45">property ipv6Support</a>
</h3>

```typescript
ipv6Support: string;
```


Whether IPv6 support is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L49">property subnetIds</a>
</h3>

```typescript
subnetIds: string[];
```


Identifiers of EC2 Subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L53">property tags</a>
</h3>

```typescript
tags: { ... };
```


Key-value tags for the EC2 Transit Gateway VPC Attachment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L57">property transitGatewayId</a>
</h3>

```typescript
transitGatewayId: string;
```


EC2 Transit Gateway identifier

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L61">property vpcId</a>
</h3>

```typescript
vpcId: string;
```


Identifier of EC2 VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/getVpcAttachment.ts#L65">property vpcOwnerId</a>
</h3>

```typescript
vpcOwnerId: string;
```


Identifier of the AWS account that owns the EC2 VPC.

<h2 class="pdoc-module-header" id="RouteArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L91">interface RouteArgs</a>
</h2>

The set of arguments for constructing a Route resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L95">property destinationCidrBlock</a>
</h3>

```typescript
destinationCidrBlock: pulumi.Input<string>;
```


IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L99">property transitGatewayAttachmentId</a>
</h3>

```typescript
transitGatewayAttachmentId: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L103">property transitGatewayRouteTableId</a>
</h3>

```typescript
transitGatewayRouteTableId: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Route Table.

<h2 class="pdoc-module-header" id="RouteState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L73">interface RouteState</a>
</h2>

Input properties used for looking up and filtering Route resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L77">property destinationCidrBlock</a>
</h3>

```typescript
destinationCidrBlock?: pulumi.Input<string>;
```


IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L81">property transitGatewayAttachmentId</a>
</h3>

```typescript
transitGatewayAttachmentId?: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/route.ts#L85">property transitGatewayRouteTableId</a>
</h3>

```typescript
transitGatewayRouteTableId?: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Route Table.

<h2 class="pdoc-module-header" id="RouteTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L97">interface RouteTableArgs</a>
</h2>

The set of arguments for constructing a RouteTable resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L101">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value tags for the EC2 Transit Gateway Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L105">property transitGatewayId</a>
</h3>

```typescript
transitGatewayId: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway.

<h2 class="pdoc-module-header" id="RouteTableAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L98">interface RouteTableAssociationArgs</a>
</h2>

The set of arguments for constructing a RouteTableAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L102">property transitGatewayAttachmentId</a>
</h3>

```typescript
transitGatewayAttachmentId: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L106">property transitGatewayRouteTableId</a>
</h3>

```typescript
transitGatewayRouteTableId: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Route Table.

<h2 class="pdoc-module-header" id="RouteTableAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L76">interface RouteTableAssociationState</a>
</h2>

Input properties used for looking up and filtering RouteTableAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L80">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


Identifier of the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L84">property resourceType</a>
</h3>

```typescript
resourceType?: pulumi.Input<string>;
```


Type of the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L88">property transitGatewayAttachmentId</a>
</h3>

```typescript
transitGatewayAttachmentId?: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTableAssociation.ts#L92">property transitGatewayRouteTableId</a>
</h3>

```typescript
transitGatewayRouteTableId?: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Route Table.

<h2 class="pdoc-module-header" id="RouteTablePropagationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L98">interface RouteTablePropagationArgs</a>
</h2>

The set of arguments for constructing a RouteTablePropagation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L102">property transitGatewayAttachmentId</a>
</h3>

```typescript
transitGatewayAttachmentId: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L106">property transitGatewayRouteTableId</a>
</h3>

```typescript
transitGatewayRouteTableId: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Route Table.

<h2 class="pdoc-module-header" id="RouteTablePropagationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L76">interface RouteTablePropagationState</a>
</h2>

Input properties used for looking up and filtering RouteTablePropagation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L80">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


Identifier of the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L84">property resourceType</a>
</h3>

```typescript
resourceType?: pulumi.Input<string>;
```


Type of the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L88">property transitGatewayAttachmentId</a>
</h3>

```typescript
transitGatewayAttachmentId?: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTablePropagation.ts#L92">property transitGatewayRouteTableId</a>
</h3>

```typescript
transitGatewayRouteTableId?: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway Route Table.

<h2 class="pdoc-module-header" id="RouteTableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L75">interface RouteTableState</a>
</h2>

Input properties used for looking up and filtering RouteTable resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L79">property defaultAssociationRouteTable</a>
</h3>

```typescript
defaultAssociationRouteTable?: pulumi.Input<boolean>;
```


Boolean whether this is the default association route table for the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L83">property defaultPropagationRouteTable</a>
</h3>

```typescript
defaultPropagationRouteTable?: pulumi.Input<boolean>;
```


Boolean whether this is the default propagation route table for the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L87">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value tags for the EC2 Transit Gateway Route Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/routeTable.ts#L91">property transitGatewayId</a>
</h3>

```typescript
transitGatewayId?: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway.

<h2 class="pdoc-module-header" id="TransitGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L174">interface TransitGatewayArgs</a>
</h2>

The set of arguments for constructing a TransitGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L178">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn?: pulumi.Input<number>;
```


Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is `64512` to `65534` for 16-bit ASNs and `4200000000` to `4294967294` for 32-bit ASNs. Default value: `64512`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L182">property autoAcceptSharedAttachments</a>
</h3>

```typescript
autoAcceptSharedAttachments?: pulumi.Input<string>;
```


Whether resource attachment requests are automatically accepted. Valid values: `disable`, `enable`. Default value: `disable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L186">property defaultRouteTableAssociation</a>
</h3>

```typescript
defaultRouteTableAssociation?: pulumi.Input<string>;
```


Whether resource attachments are automatically associated with the default association route table. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L190">property defaultRouteTablePropagation</a>
</h3>

```typescript
defaultRouteTablePropagation?: pulumi.Input<string>;
```


Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L194">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L198">property dnsSupport</a>
</h3>

```typescript
dnsSupport?: pulumi.Input<string>;
```


Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L202">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value tags for the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L206">property vpnEcmpSupport</a>
</h3>

```typescript
vpnEcmpSupport?: pulumi.Input<string>;
```


Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

<h2 class="pdoc-module-header" id="TransitGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L120">interface TransitGatewayState</a>
</h2>

Input properties used for looking up and filtering TransitGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L124">property amazonSideAsn</a>
</h3>

```typescript
amazonSideAsn?: pulumi.Input<number>;
```


Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is `64512` to `65534` for 16-bit ASNs and `4200000000` to `4294967294` for 32-bit ASNs. Default value: `64512`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L128">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<ARN>;
```


EC2 Transit Gateway Amazon Resource Name (ARN)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L132">property associationDefaultRouteTableId</a>
</h3>

```typescript
associationDefaultRouteTableId?: pulumi.Input<string>;
```


Identifier of the default association route table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L136">property autoAcceptSharedAttachments</a>
</h3>

```typescript
autoAcceptSharedAttachments?: pulumi.Input<string>;
```


Whether resource attachment requests are automatically accepted. Valid values: `disable`, `enable`. Default value: `disable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L140">property defaultRouteTableAssociation</a>
</h3>

```typescript
defaultRouteTableAssociation?: pulumi.Input<string>;
```


Whether resource attachments are automatically associated with the default association route table. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L144">property defaultRouteTablePropagation</a>
</h3>

```typescript
defaultRouteTablePropagation?: pulumi.Input<string>;
```


Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L148">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L152">property dnsSupport</a>
</h3>

```typescript
dnsSupport?: pulumi.Input<string>;
```


Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L156">property ownerId</a>
</h3>

```typescript
ownerId?: pulumi.Input<string>;
```


Identifier of the AWS account that owns the EC2 Transit Gateway

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L160">property propagationDefaultRouteTableId</a>
</h3>

```typescript
propagationDefaultRouteTableId?: pulumi.Input<string>;
```


Identifier of the default propagation route table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L164">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value tags for the EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/transitGateway.ts#L168">property vpnEcmpSupport</a>
</h3>

```typescript
vpnEcmpSupport?: pulumi.Input<string>;
```


Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

<h2 class="pdoc-module-header" id="VpcAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L153">interface VpcAttachmentArgs</a>
</h2>

The set of arguments for constructing a VpcAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L157">property dnsSupport</a>
</h3>

```typescript
dnsSupport?: pulumi.Input<string>;
```


Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L161">property ipv6Support</a>
</h3>

```typescript
ipv6Support?: pulumi.Input<string>;
```


Whether IPv6 support is enabled. Valid values: `disable`, `enable`. Default value: `disable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L165">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<pulumi.Input<string>[]>;
```


Identifiers of EC2 Subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L169">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value tags for the EC2 Transit Gateway VPC Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L173">property transitGatewayDefaultRouteTableAssociation</a>
</h3>

```typescript
transitGatewayDefaultRouteTableAssociation?: pulumi.Input<boolean>;
```


Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. Default value: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L177">property transitGatewayDefaultRouteTablePropagation</a>
</h3>

```typescript
transitGatewayDefaultRouteTablePropagation?: pulumi.Input<boolean>;
```


Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. Default value: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L181">property transitGatewayId</a>
</h3>

```typescript
transitGatewayId: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L185">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


Identifier of EC2 VPC.

<h2 class="pdoc-module-header" id="VpcAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L111">interface VpcAttachmentState</a>
</h2>

Input properties used for looking up and filtering VpcAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L115">property dnsSupport</a>
</h3>

```typescript
dnsSupport?: pulumi.Input<string>;
```


Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L119">property ipv6Support</a>
</h3>

```typescript
ipv6Support?: pulumi.Input<string>;
```


Whether IPv6 support is enabled. Valid values: `disable`, `enable`. Default value: `disable`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L123">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Identifiers of EC2 Subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L127">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value tags for the EC2 Transit Gateway VPC Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L131">property transitGatewayDefaultRouteTableAssociation</a>
</h3>

```typescript
transitGatewayDefaultRouteTableAssociation?: pulumi.Input<boolean>;
```


Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. Default value: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L135">property transitGatewayDefaultRouteTablePropagation</a>
</h3>

```typescript
transitGatewayDefaultRouteTablePropagation?: pulumi.Input<boolean>;
```


Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. Default value: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L139">property transitGatewayId</a>
</h3>

```typescript
transitGatewayId?: pulumi.Input<string>;
```


Identifier of EC2 Transit Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L143">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


Identifier of EC2 VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ec2transitgateway/vpcAttachment.ts#L147">property vpcOwnerId</a>
</h3>

```typescript
vpcOwnerId?: pulumi.Input<string>;
```


Identifier of the AWS account that owns the EC2 VPC.

