---
title: Module directconnect
---

<a href="../index.html">@pulumi/aws</a> &gt; directconnect

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Connection">class Connection</a>
* <a href="#ConnectionAssociation">class ConnectionAssociation</a>
* <a href="#LinkAggregationGroup">class LinkAggregationGroup</a>
* <a href="#ConnectionArgs">interface ConnectionArgs</a>
* <a href="#ConnectionAssociationArgs">interface ConnectionAssociationArgs</a>
* <a href="#ConnectionAssociationState">interface ConnectionAssociationState</a>
* <a href="#ConnectionState">interface ConnectionState</a>
* <a href="#LinkAggregationGroupArgs">interface LinkAggregationGroupArgs</a>
* <a href="#LinkAggregationGroupState">interface LinkAggregationGroupState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts">directconnect/connection.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts">directconnect/connectionAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts">directconnect/linkAggregationGroup.ts</a> 


<h2 class="pdoc-module-header" id="Connection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L9">class Connection</a>
</h2>

Provides a Connection of Direct Connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L41">constructor</a>
</h3>

```typescript
new Connection(name: string, args: ConnectionArgs, opts?: pulumi.ResourceOptions)
```


Create a Connection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConnectionState): Connection
```


Get an existing Connection resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L29">property bandwidth</a>
</h3>

```typescript
public bandwidth: pulumi.Output<string>;
```


The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L33">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L41">property tags</a>
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

<h2 class="pdoc-module-header" id="ConnectionAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L9">class ConnectionAssociation</a>
</h2>

Associates a Direct Connect Connection with a LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L29">constructor</a>
</h3>

```typescript
new ConnectionAssociation(name: string, args: ConnectionAssociationArgs, opts?: pulumi.ResourceOptions)
```


Create a ConnectionAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConnectionAssociationState): ConnectionAssociation
```


Get an existing ConnectionAssociation resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L25">property connectionId</a>
</h3>

```typescript
public connectionId: pulumi.Output<string>;
```


The ID of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L29">property lagId</a>
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

<h2 class="pdoc-module-header" id="LinkAggregationGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L9">class LinkAggregationGroup</a>
</h2>

Provides a Direct Connect LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L49">constructor</a>
</h3>

```typescript
new LinkAggregationGroup(name: string, args: LinkAggregationGroupArgs, opts?: pulumi.ResourceOptions)
```


Create a LinkAggregationGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LinkAggregationGroupState): LinkAggregationGroup
```


Get an existing LinkAggregationGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L29">property connectionsBandwidth</a>
</h3>

```typescript
public connectionsBandwidth: pulumi.Output<string>;
```


The bandwidth of the individual physical connections bundled by the LAG. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L33">property forceDestroy</a>
</h3>

```typescript
public forceDestroy: pulumi.Output<boolean | undefined>;
```


A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L37">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The AWS Direct Connect location in which the LAG should be allocated. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L45">property numberOfConnections</a>
</h3>

```typescript
public numberOfConnections: pulumi.Output<number>;
```


The number of physical connections initially provisioned and bundled by the LAG. Use `aws_dx_connection` and `aws_dx_connection_association` resources instead. Default connections will be removed as part of LAG creation automatically in future versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L49">property tags</a>
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

<h2 class="pdoc-module-header" id="ConnectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L107">interface ConnectionArgs</a>
</h2>

The set of arguments for constructing a Connection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L111">property bandwidth</a>
</h3>

```typescript
bandwidth: pulumi.Input<string>;
```


The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L115">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L123">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ConnectionAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L77">interface ConnectionAssociationArgs</a>
</h2>

The set of arguments for constructing a ConnectionAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L81">property connectionId</a>
</h3>

```typescript
connectionId: pulumi.Input<string>;
```


The ID of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L85">property lagId</a>
</h3>

```typescript
lagId: pulumi.Input<string>;
```


The ID of the LAG with which to associate the connection.

<h2 class="pdoc-module-header" id="ConnectionAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L63">interface ConnectionAssociationState</a>
</h2>

Input properties used for looking up and filtering ConnectionAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L67">property connectionId</a>
</h3>

```typescript
connectionId?: pulumi.Input<string>;
```


The ID of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connectionAssociation.ts#L71">property lagId</a>
</h3>

```typescript
lagId?: pulumi.Input<string>;
```


The ID of the LAG with which to associate the connection.

<h2 class="pdoc-module-header" id="ConnectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L81">interface ConnectionState</a>
</h2>

Input properties used for looking up and filtering Connection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L85">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L89">property bandwidth</a>
</h3>

```typescript
bandwidth?: pulumi.Input<string>;
```


The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L93">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/connection.ts#L101">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LinkAggregationGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L127">interface LinkAggregationGroupArgs</a>
</h2>

The set of arguments for constructing a LinkAggregationGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L131">property connectionsBandwidth</a>
</h3>

```typescript
connectionsBandwidth: pulumi.Input<string>;
```


The bandwidth of the individual physical connections bundled by the LAG. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L135">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L139">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The AWS Direct Connect location in which the LAG should be allocated. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L143">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L147">property numberOfConnections</a>
</h3>

```typescript
numberOfConnections?: pulumi.Input<number>;
```


The number of physical connections initially provisioned and bundled by the LAG. Use `aws_dx_connection` and `aws_dx_connection_association` resources instead. Default connections will be removed as part of LAG creation automatically in future versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L151">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LinkAggregationGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L93">interface LinkAggregationGroupState</a>
</h2>

Input properties used for looking up and filtering LinkAggregationGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L97">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L101">property connectionsBandwidth</a>
</h3>

```typescript
connectionsBandwidth?: pulumi.Input<string>;
```


The bandwidth of the individual physical connections bundled by the LAG. Available values: 1Gbps, 10Gbps. Case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L105">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L109">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The AWS Direct Connect location in which the LAG should be allocated. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the LAG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L117">property numberOfConnections</a>
</h3>

```typescript
numberOfConnections?: pulumi.Input<number>;
```


The number of physical connections initially provisioned and bundled by the LAG. Use `aws_dx_connection` and `aws_dx_connection_association` resources instead. Default connections will be removed as part of LAG creation automatically in future versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directconnect/linkAggregationGroup.ts#L121">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

