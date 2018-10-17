---
title: Module dax
---

<a href="../index.html">@pulumi/aws</a> &gt; dax

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#ParameterGroup">class ParameterGroup</a>
* <a href="#SubnetGroup">class SubnetGroup</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#ParameterGroupArgs">interface ParameterGroupArgs</a>
* <a href="#ParameterGroupState">interface ParameterGroupState</a>
* <a href="#SubnetGroupArgs">interface SubnetGroupArgs</a>
* <a href="#SubnetGroupState">interface SubnetGroupState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts">dax/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts">dax/parameterGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts">dax/subnetGroup.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L12">class Cluster</a>
</h2>

Provides a DAX Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L114">constructor</a>
</h3>

```typescript
new Cluster(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState): Cluster
```


Get an existing Cluster resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L33">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[] | undefined>;
```


List of Availability Zones in which the
nodes will be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L37">property clusterAddress</a>
</h3>

```typescript
public clusterAddress: pulumi.Output<string>;
```


The DNS name of the DAX cluster without the port appended

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L42">property clusterName</a>
</h3>

```typescript
public clusterName: pulumi.Output<string>;
```


Group identifier. DAX converts this name to
lowercase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L47">property configurationEndpoint</a>
</h3>

```typescript
public configurationEndpoint: pulumi.Output<string>;
```


The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L51">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L57">property iamRoleArn</a>
</h3>

```typescript
public iamRoleArn: pulumi.Output<string>;
```


A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role's
permissions to access DynamoDB on your behalf

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L64">property maintenanceWindow</a>
</h3>

```typescript
public maintenanceWindow: pulumi.Output<string>;
```


Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L69">property nodeType</a>
</h3>

```typescript
public nodeType: pulumi.Output<string>;
```


The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L75">property nodes</a>
</h3>

```typescript
public nodes: pulumi.Output<{ ... }[]>;
```


List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L81">property notificationTopicArn</a>
</h3>

```typescript
public notificationTopicArn: pulumi.Output<string | undefined>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L86">property parameterGroupName</a>
</h3>

```typescript
public parameterGroupName: pulumi.Output<string>;
```


Name of the parameter group to associate
with this DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L90">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The port used by the configuration endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L96">property replicationFactor</a>
</h3>

```typescript
public replicationFactor: pulumi.Output<number>;
```


The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L101">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[]>;
```


One or more VPC security groups associated
with the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L105">property serverSideEncryption</a>
</h3>

```typescript
public serverSideEncryption: pulumi.Output<{ ... } | undefined>;
```


Encrypt at rest options

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L110">property subnetGroupName</a>
</h3>

```typescript
public subnetGroupName: pulumi.Output<string>;
```


Name of the subnet group to be used for the
cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L114">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ParameterGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L10">class ParameterGroup</a>
</h2>

Provides a DAX Parameter Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L34">constructor</a>
</h3>

```typescript
new ParameterGroup(name: string, args?: ParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ParameterGroupState): ParameterGroup
```


Get an existing ParameterGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L34">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[]>;
```


The parameters of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubnetGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L10">class SubnetGroup</a>
</h2>

Provides a DAX Subnet Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L38">constructor</a>
</h3>

```typescript
new SubnetGroup(name: string, args: SubnetGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetGroupState): SubnetGroup
```


Get an existing SubnetGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L34">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


A list of VPC subnet IDs for the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L38">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


VPC ID of the subnet group.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L282">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L287">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


List of Availability Zones in which the
nodes will be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L292">property clusterName</a>
</h3>

```typescript
clusterName: pulumi.Input<string>;
```


Group identifier. DAX converts this name to
lowercase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L296">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L302">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn: pulumi.Input<string>;
```


A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role's
permissions to access DynamoDB on your behalf

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L309">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L314">property nodeType</a>
</h3>

```typescript
nodeType: pulumi.Input<string>;
```


The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L320">property notificationTopicArn</a>
</h3>

```typescript
notificationTopicArn?: pulumi.Input<string>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L325">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the parameter group to associate
with this DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L331">property replicationFactor</a>
</h3>

```typescript
replicationFactor: pulumi.Input<number>;
```


The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L336">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more VPC security groups associated
with the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L340">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: pulumi.Input<{ ... }>;
```


Encrypt at rest options

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L345">property subnetGroupName</a>
</h3>

```typescript
subnetGroupName?: pulumi.Input<string>;
```


Name of the subnet group to be used for the
cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L349">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L186">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L190">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L195">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


List of Availability Zones in which the
nodes will be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L199">property clusterAddress</a>
</h3>

```typescript
clusterAddress?: pulumi.Input<string>;
```


The DNS name of the DAX cluster without the port appended

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L204">property clusterName</a>
</h3>

```typescript
clusterName?: pulumi.Input<string>;
```


Group identifier. DAX converts this name to
lowercase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L209">property configurationEndpoint</a>
</h3>

```typescript
configurationEndpoint?: pulumi.Input<string>;
```


The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L213">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L219">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn?: pulumi.Input<string>;
```


A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role's
permissions to access DynamoDB on your behalf

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L226">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L231">property nodeType</a>
</h3>

```typescript
nodeType?: pulumi.Input<string>;
```


The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L237">property nodes</a>
</h3>

```typescript
nodes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L243">property notificationTopicArn</a>
</h3>

```typescript
notificationTopicArn?: pulumi.Input<string>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L248">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the parameter group to associate
with this DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L252">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port used by the configuration endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L258">property replicationFactor</a>
</h3>

```typescript
replicationFactor?: pulumi.Input<number>;
```


The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L263">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more VPC security groups associated
with the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L267">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: pulumi.Input<{ ... }>;
```


Encrypt at rest options

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L272">property subnetGroupName</a>
</h3>

```typescript
subnetGroupName?: pulumi.Input<string>;
```


Name of the subnet group to be used for the
cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L276">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource

<h2 class="pdoc-module-header" id="ParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L82">interface ParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L86">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L90">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L94">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The parameters of the parameter group.

<h2 class="pdoc-module-header" id="ParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L64">interface ParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L68">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L72">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L76">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The parameters of the parameter group.

<h2 class="pdoc-module-header" id="SubnetGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L95">interface SubnetGroupArgs</a>
</h2>

The set of arguments for constructing a SubnetGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L107">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs for the subnet group.

<h2 class="pdoc-module-header" id="SubnetGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L73">interface SubnetGroupState</a>
</h2>

Input properties used for looking up and filtering SubnetGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L77">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L85">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs for the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L89">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


VPC ID of the subnet group.

