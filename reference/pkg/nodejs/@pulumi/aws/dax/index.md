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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L9">class Cluster</a>
</h2>

Provides a DAX Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L107">constructor</a>
</h3>

```typescript
new Cluster(name: string, args: ClusterArgs, opts?: pulumi.ResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState): Cluster
```


Get an existing Cluster resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L30">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[] | undefined>;
```


List of Availability Zones in which the
nodes will be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L34">property clusterAddress</a>
</h3>

```typescript
public clusterAddress: pulumi.Output<string>;
```


The DNS name of the DAX cluster without the port appended

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L39">property clusterName</a>
</h3>

```typescript
public clusterName: pulumi.Output<string>;
```


Group identifier. DAX converts this name to
lowercase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L44">property configurationEndpoint</a>
</h3>

```typescript
public configurationEndpoint: pulumi.Output<string>;
```


The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L48">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L54">property iamRoleArn</a>
</h3>

```typescript
public iamRoleArn: pulumi.Output<string>;
```


A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role's
permissions to access DynamoDB on your behalf

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L61">property maintenanceWindow</a>
</h3>

```typescript
public maintenanceWindow: pulumi.Output<string>;
```


Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L66">property nodeType</a>
</h3>

```typescript
public nodeType: pulumi.Output<string>;
```


The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L72">property nodes</a>
</h3>

```typescript
public nodes: pulumi.Output<{ ... }[]>;
```


List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L78">property notificationTopicArn</a>
</h3>

```typescript
public notificationTopicArn: pulumi.Output<string | undefined>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L83">property parameterGroupName</a>
</h3>

```typescript
public parameterGroupName: pulumi.Output<string>;
```


Name of the parameter group to associate
with this DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L87">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The port used by the configuration endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L93">property replicationFactor</a>
</h3>

```typescript
public replicationFactor: pulumi.Output<number>;
```


The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L98">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[]>;
```


One or more VPC security groups associated
with the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L103">property subnetGroupName</a>
</h3>

```typescript
public subnetGroupName: pulumi.Output<string>;
```


Name of the subnet group to be used for the
cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L107">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L9">class ParameterGroup</a>
</h2>

Provides a DAX Parameter Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L33">constructor</a>
</h3>

```typescript
new ParameterGroup(name: string, args?: ParameterGroupArgs, opts?: pulumi.ResourceOptions)
```


Create a ParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ParameterGroupState): ParameterGroup
```


Get an existing ParameterGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L33">property parameters</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L9">class SubnetGroup</a>
</h2>

Provides a DAX Subnet Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L37">constructor</a>
</h3>

```typescript
new SubnetGroup(name: string, args: SubnetGroupArgs, opts?: pulumi.ResourceOptions)
```


Create a SubnetGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetGroupState): SubnetGroup
```


Get an existing SubnetGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L33">property subnetIds</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L37">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


VPC ID of the subnet group.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L269">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L274">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


List of Availability Zones in which the
nodes will be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L279">property clusterName</a>
</h3>

```typescript
clusterName: pulumi.Input<string>;
```


Group identifier. DAX converts this name to
lowercase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L283">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L289">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn: pulumi.Input<string>;
```


A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role's
permissions to access DynamoDB on your behalf

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L296">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L301">property nodeType</a>
</h3>

```typescript
nodeType: pulumi.Input<string>;
```


The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L307">property notificationTopicArn</a>
</h3>

```typescript
notificationTopicArn?: pulumi.Input<string>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L312">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the parameter group to associate
with this DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L318">property replicationFactor</a>
</h3>

```typescript
replicationFactor: pulumi.Input<number>;
```


The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L323">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more VPC security groups associated
with the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L328">property subnetGroupName</a>
</h3>

```typescript
subnetGroupName?: pulumi.Input<string>;
```


Name of the subnet group to be used for the
cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L332">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L177">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L181">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L186">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


List of Availability Zones in which the
nodes will be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L190">property clusterAddress</a>
</h3>

```typescript
clusterAddress?: pulumi.Input<string>;
```


The DNS name of the DAX cluster without the port appended

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L195">property clusterName</a>
</h3>

```typescript
clusterName?: pulumi.Input<string>;
```


Group identifier. DAX converts this name to
lowercase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L200">property configurationEndpoint</a>
</h3>

```typescript
configurationEndpoint?: pulumi.Input<string>;
```


The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L204">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description for the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L210">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn?: pulumi.Input<string>;
```


A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role's
permissions to access DynamoDB on your behalf

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L217">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L222">property nodeType</a>
</h3>

```typescript
nodeType?: pulumi.Input<string>;
```


The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L228">property nodes</a>
</h3>

```typescript
nodes?: pulumi.Input<{ ... }[]>;
```


List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L234">property notificationTopicArn</a>
</h3>

```typescript
notificationTopicArn?: pulumi.Input<string>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L239">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the parameter group to associate
with this DAX cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L243">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port used by the configuration endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L249">property replicationFactor</a>
</h3>

```typescript
replicationFactor?: pulumi.Input<number>;
```


The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L254">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more VPC security groups associated
with the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L259">property subnetGroupName</a>
</h3>

```typescript
subnetGroupName?: pulumi.Input<string>;
```


Name of the subnet group to be used for the
cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/cluster.ts#L263">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource

<h2 class="pdoc-module-header" id="ParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L81">interface ParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L85">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L89">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L93">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }[]>;
```


The parameters of the parameter group.

<h2 class="pdoc-module-header" id="ParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L63">interface ParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L67">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L71">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/parameterGroup.ts#L75">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }[]>;
```


The parameters of the parameter group.

<h2 class="pdoc-module-header" id="SubnetGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L94">interface SubnetGroupArgs</a>
</h2>

The set of arguments for constructing a SubnetGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L98">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L102">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L106">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs for the subnet group.

<h2 class="pdoc-module-header" id="SubnetGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L72">interface SubnetGroupState</a>
</h2>

Input properties used for looking up and filtering SubnetGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L76">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L80">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L84">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs for the subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dax/subnetGroup.ts#L88">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


VPC ID of the subnet group.

