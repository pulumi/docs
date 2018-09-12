---
title: Module elasticache
---

<a href="../index.html">@pulumi/aws</a> &gt; elasticache

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#ParameterGroup">class ParameterGroup</a>
* <a href="#ReplicationGroup">class ReplicationGroup</a>
* <a href="#SecurityGroup">class SecurityGroup</a>
* <a href="#SubnetGroup">class SubnetGroup</a>
* <a href="#getCluster">function getCluster</a>
* <a href="#getReplicationGroup">function getReplicationGroup</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#GetClusterArgs">interface GetClusterArgs</a>
* <a href="#GetClusterResult">interface GetClusterResult</a>
* <a href="#GetReplicationGroupArgs">interface GetReplicationGroupArgs</a>
* <a href="#GetReplicationGroupResult">interface GetReplicationGroupResult</a>
* <a href="#ParameterGroupArgs">interface ParameterGroupArgs</a>
* <a href="#ParameterGroupState">interface ParameterGroupState</a>
* <a href="#ReplicationGroupArgs">interface ReplicationGroupArgs</a>
* <a href="#ReplicationGroupState">interface ReplicationGroupState</a>
* <a href="#SecurityGroupArgs">interface SecurityGroupArgs</a>
* <a href="#SecurityGroupState">interface SecurityGroupState</a>
* <a href="#SubnetGroupArgs">interface SubnetGroupArgs</a>
* <a href="#SubnetGroupState">interface SubnetGroupState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts">elasticache/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts">elasticache/getCluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts">elasticache/getReplicationGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts">elasticache/parameterGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts">elasticache/replicationGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts">elasticache/securityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts">elasticache/subnetGroup.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L21">class Cluster</a>
</h2>

Provides an ElastiCache Cluster resource, which manages a Memcached cluster or Redis instance.
For working with Redis (Cluster Mode Enabled) replication groups, see the
[`aws_elasticache_replication_group` resource](https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group.html).

~> **Note:** When you change an attribute, such as `node_type`, by default
it is applied in the next maintenance window. Because of this, Terraform may report
a difference in its planning phase because the actual modification has not yet taken
place. You can use the `apply_immediately` flag to instruct the service to apply the
change immediately. Using `apply_immediately` can result in a brief downtime as the server reboots.
See the AWS Docs on [Modifying an ElastiCache Cache Cluster][2] for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L165">constructor</a>
</h3>

```typescript
new Cluster(name: string, args?: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L30">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L40">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L44">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L48">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[] | undefined>;
```


Use `preferred_availability_zones` instead unless you want to create cache nodes in single-az, then use `availability_zone`. Set of Availability Zones in which the cache nodes will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L52">property azMode</a>
</h3>

```typescript
public azMode: pulumi.Output<string>;
```


Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L57">property cacheNodes</a>
</h3>

```typescript
public cacheNodes: pulumi.Output<{ ... }[]>;
```


List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L61">property clusterAddress</a>
</h3>

```typescript
public clusterAddress: pulumi.Output<string>;
```


(Memcached only) The DNS name of the cache cluster without the port appended.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L66">property clusterId</a>
</h3>

```typescript
public clusterId: pulumi.Output<string>;
```


Group identifier. ElastiCache converts
this name to lowercase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L70">property configurationEndpoint</a>
</h3>

```typescript
public configurationEndpoint: pulumi.Output<string>;
```


(Memcached only) The configuration endpoint to allow host discovery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L75">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string>;
```


Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L81">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L87">property maintenanceWindow</a>
</h3>

```typescript
public maintenanceWindow: pulumi.Output<string>;
```


Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L93">property nodeType</a>
</h3>

```typescript
public nodeType: pulumi.Output<string>;
```


The compute and memory capacity of the nodes. See
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L99">property notificationTopicArn</a>
</h3>

```typescript
public notificationTopicArn: pulumi.Output<string | undefined>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L106">property numCacheNodes</a>
</h3>

```typescript
public numCacheNodes: pulumi.Output<number>;
```


The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L111">property parameterGroupName</a>
</h3>

```typescript
public parameterGroupName: pulumi.Output<string>;
```


Name of the parameter group to associate
with this cache cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L115">property port</a>
</h3>

```typescript
public port: pulumi.Output<number | undefined>;
```


The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L119">property preferredAvailabilityZones</a>
</h3>

```typescript
public preferredAvailabilityZones: pulumi.Output<string[] | undefined>;
```


A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L123">property replicationGroupId</a>
</h3>

```typescript
public replicationGroupId: pulumi.Output<string>;
```


The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L128">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[]>;
```


One or more VPC security groups associated
with the cache cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L133">property securityGroupNames</a>
</h3>

```typescript
public securityGroupNames: pulumi.Output<string[]>;
```


List of security group
names to associate with this cache cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L139">property snapshotArns</a>
</h3>

```typescript
public snapshotArns: pulumi.Output<string[] | undefined>;
```


A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L143">property snapshotName</a>
</h3>

```typescript
public snapshotName: pulumi.Output<string | undefined>;
```


The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L151">property snapshotRetentionLimit</a>
</h3>

```typescript
public snapshotRetentionLimit: pulumi.Output<number | undefined>;
```


The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L156">property snapshotWindow</a>
</h3>

```typescript
public snapshotWindow: pulumi.Output<string>;
```


The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L161">property subnetGroupName</a>
</h3>

```typescript
public subnetGroupName: pulumi.Output<string>;
```


Name of the subnet group to be used
for the cache cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L165">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L10">class ParameterGroup</a>
</h2>

Provides an ElastiCache parameter group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L38">constructor</a>
</h3>

```typescript
new ParameterGroup(name: string, args: ParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the ElastiCache parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L30">property family</a>
</h3>

```typescript
public family: pulumi.Output<string>;
```


The family of the ElastiCache parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the ElastiCache parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L38">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[] | undefined>;
```


A list of ElastiCache parameters to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ReplicationGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L14">class ReplicationGroup</a>
</h2>

Provides an ElastiCache Replication Group resource.
For working with Memcached or single primary Redis instances (Cluster Mode Disabled), see the
[`aws_elasticache_cluster` resource](https://www.terraform.io/docs/providers/aws/r/elasticache_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L153">constructor</a>
</h3>

```typescript
new ReplicationGroup(name: string, args: ReplicationGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ReplicationGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ReplicationGroupState): ReplicationGroup
```


Get an existing ReplicationGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L30">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean>;
```


Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L34">property atRestEncryptionEnabled</a>
</h3>

```typescript
public atRestEncryptionEnabled: pulumi.Output<boolean | undefined>;
```


Whether to enable encryption at rest.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L38">property authToken</a>
</h3>

```typescript
public authToken: pulumi.Output<string | undefined>;
```


The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L42">property autoMinorVersionUpgrade</a>
</h3>

```typescript
public autoMinorVersionUpgrade: pulumi.Output<boolean | undefined>;
```


Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L46">property automaticFailoverEnabled</a>
</h3>

```typescript
public automaticFailoverEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L50">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[] | undefined>;
```


A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L54">property clusterMode</a>
</h3>

```typescript
public clusterMode: pulumi.Output<{ ... }>;
```


Create a native redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode documented below. Only 1 `cluster_mode` block is allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L58">property configurationEndpointAddress</a>
</h3>

```typescript
public configurationEndpointAddress: pulumi.Output<string>;
```


The address of the replication group configuration endpoint when cluster mode is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L62">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string | undefined>;
```


The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L66">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The version number of the cache engine to be used for the cache clusters in this replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L72">property maintenanceWindow</a>
</h3>

```typescript
public maintenanceWindow: pulumi.Output<string>;
```


Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L76">property memberClusters</a>
</h3>

```typescript
public memberClusters: pulumi.Output<string[]>;
```


The identifiers of all the nodes that are part of this replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L80">property nodeType</a>
</h3>

```typescript
public nodeType: pulumi.Output<string>;
```


The compute and memory capacity of the nodes in the node group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L86">property notificationTopicArn</a>
</h3>

```typescript
public notificationTopicArn: pulumi.Output<string | undefined>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L90">property numberCacheClusters</a>
</h3>

```typescript
public numberCacheClusters: pulumi.Output<number>;
```


The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L94">property parameterGroupName</a>
</h3>

```typescript
public parameterGroupName: pulumi.Output<string>;
```


The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L98">property port</a>
</h3>

```typescript
public port: pulumi.Output<number | undefined>;
```


The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L102">property primaryEndpointAddress</a>
</h3>

```typescript
public primaryEndpointAddress: pulumi.Output<string>;
```


(Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L106">property replicationGroupDescription</a>
</h3>

```typescript
public replicationGroupDescription: pulumi.Output<string>;
```


A user-created description for the replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L110">property replicationGroupId</a>
</h3>

```typescript
public replicationGroupId: pulumi.Output<string>;
```


The replication group identifier. This parameter is stored as a lowercase string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L114">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[]>;
```


One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L118">property securityGroupNames</a>
</h3>

```typescript
public securityGroupNames: pulumi.Output<string[]>;
```


A list of cache security group names to associate with this replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L124">property snapshotArns</a>
</h3>

```typescript
public snapshotArns: pulumi.Output<string[] | undefined>;
```


A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L128">property snapshotName</a>
</h3>

```typescript
public snapshotName: pulumi.Output<string | undefined>;
```


The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L136">property snapshotRetentionLimit</a>
</h3>

```typescript
public snapshotRetentionLimit: pulumi.Output<number | undefined>;
```


The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L141">property snapshotWindow</a>
</h3>

```typescript
public snapshotWindow: pulumi.Output<string>;
```


The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L145">property subnetGroupName</a>
</h3>

```typescript
public subnetGroupName: pulumi.Output<string>;
```


The name of the cache subnet group to be used for the replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L149">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L153">property transitEncryptionEnabled</a>
</h3>

```typescript
public transitEncryptionEnabled: pulumi.Output<boolean | undefined>;
```


Whether to enable encryption in transit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L15">class SecurityGroup</a>
</h2>

Provides an ElastiCache Security Group to control access to one or more cache
clusters.

~> **NOTE:** ElastiCache Security Groups are for use only when working with an
ElastiCache cluster **outside** of a VPC. If you are using a VPC, see the
ElastiCache Subnet Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L40">constructor</a>
</h3>

```typescript
new SecurityGroup(name: string, args: SecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecurityGroupState): SecurityGroup
```


Get an existing SecurityGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


description for the cache security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name for the cache security group. This value is stored as a lowercase string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L40">property securityGroupNames</a>
</h3>

```typescript
public securityGroupNames: pulumi.Output<string[]>;
```


List of EC2 security group names to be
authorized for ingress to the cache security group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubnetGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L14">class SubnetGroup</a>
</h2>

Provides an ElastiCache Subnet Group resource.

~> **NOTE:** ElastiCache Subnet Groups are only for use when working with an
ElastiCache cluster **inside** of a VPC. If you are on EC2 Classic, see the
ElastiCache Security Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L38">constructor</a>
</h3>

```typescript
new SubnetGroup(name: string, args: SubnetGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


Description for the cache subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name for the cache subnet group. Elasticache converts this name to lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L38">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


List of VPC Subnet IDs for the cache subnet group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L10">function getCluster</a>
</h2>

```typescript
getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult>
```


Use this data source to get information about an Elasticache Cluster

<h2 class="pdoc-module-header" id="getReplicationGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L10">function getReplicationGroup</a>
</h2>

```typescript
getReplicationGroup(args: GetReplicationGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetReplicationGroupResult>
```


Use this data source to get information about an Elasticache Replication Group.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L379">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L386">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L390">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L394">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


Use `preferred_availability_zones` instead unless you want to create cache nodes in single-az, then use `availability_zone`. Set of Availability Zones in which the cache nodes will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L398">property azMode</a>
</h3>

```typescript
azMode?: pulumi.Input<string>;
```


Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L403">property clusterId</a>
</h3>

```typescript
clusterId?: pulumi.Input<string>;
```


Group identifier. ElastiCache converts
this name to lowercase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L408">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L414">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L420">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L426">property nodeType</a>
</h3>

```typescript
nodeType?: pulumi.Input<string>;
```


The compute and memory capacity of the nodes. See
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L432">property notificationTopicArn</a>
</h3>

```typescript
notificationTopicArn?: pulumi.Input<string>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L439">property numCacheNodes</a>
</h3>

```typescript
numCacheNodes?: pulumi.Input<number>;
```


The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L444">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the parameter group to associate
with this cache cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L448">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L452">property preferredAvailabilityZones</a>
</h3>

```typescript
preferredAvailabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L456">property replicationGroupId</a>
</h3>

```typescript
replicationGroupId?: pulumi.Input<string>;
```


The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L461">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more VPC security groups associated
with the cache cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L466">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


List of security group
names to associate with this cache cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L472">property snapshotArns</a>
</h3>

```typescript
snapshotArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L476">property snapshotName</a>
</h3>

```typescript
snapshotName?: pulumi.Input<string>;
```


The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L484">property snapshotRetentionLimit</a>
</h3>

```typescript
snapshotRetentionLimit?: pulumi.Input<number>;
```


The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L489">property snapshotWindow</a>
</h3>

```typescript
snapshotWindow?: pulumi.Input<string>;
```


The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L494">property subnetGroupName</a>
</h3>

```typescript
subnetGroupName?: pulumi.Input<string>;
```


Name of the subnet group to be used
for the cache cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L498">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L241">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L248">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L252">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L256">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


Use `preferred_availability_zones` instead unless you want to create cache nodes in single-az, then use `availability_zone`. Set of Availability Zones in which the cache nodes will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L260">property azMode</a>
</h3>

```typescript
azMode?: pulumi.Input<string>;
```


Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L265">property cacheNodes</a>
</h3>

```typescript
cacheNodes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L269">property clusterAddress</a>
</h3>

```typescript
clusterAddress?: pulumi.Input<string>;
```


(Memcached only) The DNS name of the cache cluster without the port appended.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L274">property clusterId</a>
</h3>

```typescript
clusterId?: pulumi.Input<string>;
```


Group identifier. ElastiCache converts
this name to lowercase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L278">property configurationEndpoint</a>
</h3>

```typescript
configurationEndpoint?: pulumi.Input<string>;
```


(Memcached only) The configuration endpoint to allow host discovery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L283">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L289">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L295">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L301">property nodeType</a>
</h3>

```typescript
nodeType?: pulumi.Input<string>;
```


The compute and memory capacity of the nodes. See
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L307">property notificationTopicArn</a>
</h3>

```typescript
notificationTopicArn?: pulumi.Input<string>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L314">property numCacheNodes</a>
</h3>

```typescript
numCacheNodes?: pulumi.Input<number>;
```


The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L319">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the parameter group to associate
with this cache cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L323">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L327">property preferredAvailabilityZones</a>
</h3>

```typescript
preferredAvailabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L331">property replicationGroupId</a>
</h3>

```typescript
replicationGroupId?: pulumi.Input<string>;
```


The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L336">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more VPC security groups associated
with the cache cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L341">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


List of security group
names to associate with this cache cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L347">property snapshotArns</a>
</h3>

```typescript
snapshotArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L351">property snapshotName</a>
</h3>

```typescript
snapshotName?: pulumi.Input<string>;
```


The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L359">property snapshotRetentionLimit</a>
</h3>

```typescript
snapshotRetentionLimit?: pulumi.Input<number>;
```


The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L364">property snapshotWindow</a>
</h3>

```typescript
snapshotWindow?: pulumi.Input<string>;
```


The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L369">property subnetGroupName</a>
</h3>

```typescript
subnetGroupName?: pulumi.Input<string>;
```


Name of the subnet group to be used
for the cache cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/cluster.ts#L373">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource

<h2 class="pdoc-module-header" id="GetClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L20">interface GetClusterArgs</a>
</h2>

A collection of arguments for invoking getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L24">property clusterId</a>
</h3>

```typescript
clusterId: string;
```


Group identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L25">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L31">interface GetClusterResult</a>
</h2>

A collection of values returned by getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L32">property arn</a>
</h3>

```typescript
arn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L36">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```


The Availability Zone for the cache cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L41">property cacheNodes</a>
</h3>

```typescript
cacheNodes: { ... }[];
```


List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${data.aws_elasticache_cluster.bar.cache_nodes.0.address}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L45">property clusterAddress</a>
</h3>

```typescript
clusterAddress: string;
```


(Memcached only) The DNS name of the cache cluster without the port appended.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L49">property configurationEndpoint</a>
</h3>

```typescript
configurationEndpoint: string;
```


(Memcached only) The configuration endpoint to allow host discovery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L53">property engine</a>
</h3>

```typescript
engine: string;
```


Name of the cache engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L57">property engineVersion</a>
</h3>

```typescript
engineVersion: string;
```


Version number of the cache engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L118">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L62">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow: string;
```


Specifies the weekly time range for when maintenance
on the cache cluster is performed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L66">property nodeType</a>
</h3>

```typescript
nodeType: string;
```


The cluster node type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L71">property notificationTopicArn</a>
</h3>

```typescript
notificationTopicArn: string;
```


An Amazon Resource Name (ARN) of an
SNS topic that ElastiCache notifications get sent to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L75">property numCacheNodes</a>
</h3>

```typescript
numCacheNodes: number;
```


The number of cache nodes that the cache cluster has.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L79">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName: string;
```


Name of the parameter group associated with this cache cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L84">property port</a>
</h3>

```typescript
port: number;
```


The port number on which each of the cache nodes will
accept connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L88">property replicationGroupId</a>
</h3>

```typescript
replicationGroupId: string;
```


The replication group to which this cache cluster belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L92">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds: string[];
```


List VPC security groups associated with the cache cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L96">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames: string[];
```


List of security group names associated with this cache cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L101">property snapshotRetentionLimit</a>
</h3>

```typescript
snapshotRetentionLimit: number;
```


The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L106">property snapshotWindow</a>
</h3>

```typescript
snapshotWindow: string;
```


The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of the cache cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L110">property subnetGroupName</a>
</h3>

```typescript
subnetGroupName: string;
```


Name of the subnet group associated to the cache cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getCluster.ts#L114">property tags</a>
</h3>

```typescript
tags: { ... };
```


The tags assigned to the resource

<h2 class="pdoc-module-header" id="GetReplicationGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L19">interface GetReplicationGroupArgs</a>
</h2>

A collection of arguments for invoking getReplicationGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L23">property replicationGroupId</a>
</h3>

```typescript
replicationGroupId: string;
```


The identifier for the replication group.

<h2 class="pdoc-module-header" id="GetReplicationGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L29">interface GetReplicationGroupResult</a>
</h2>

A collection of values returned by getReplicationGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L33">property authTokenEnabled</a>
</h3>

```typescript
authTokenEnabled: boolean;
```


A flag that enables using an AuthToken (password) when issuing Redis commands.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L37">property automaticFailoverEnabled</a>
</h3>

```typescript
automaticFailoverEnabled: boolean;
```


A flag whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L41">property configurationEndpointAddress</a>
</h3>

```typescript
configurationEndpointAddress: string;
```


The configuration endpoint address to allow host discovery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L77">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L45">property memberClusters</a>
</h3>

```typescript
memberClusters: string[];
```


The identifiers of all the nodes that are part of this replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L49">property nodeType</a>
</h3>

```typescript
nodeType: string;
```


The cluster node type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L53">property numberCacheClusters</a>
</h3>

```typescript
numberCacheClusters: number;
```


The number of cache clusters that the replication group has.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L57">property port</a>
</h3>

```typescript
port: number;
```


The port number on which the configuration endpoint will accept connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L61">property primaryEndpointAddress</a>
</h3>

```typescript
primaryEndpointAddress: string;
```


The endpoint of the primary node in this node group (shard).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L65">property replicationGroupDescription</a>
</h3>

```typescript
replicationGroupDescription: string;
```


The description of the replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L69">property snapshotRetentionLimit</a>
</h3>

```typescript
snapshotRetentionLimit: number;
```


The number of days for which ElastiCache retains automatic cache cluster snapshots before deleting them.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/getReplicationGroup.ts#L73">property snapshotWindow</a>
</h3>

```typescript
snapshotWindow: string;
```


The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

<h2 class="pdoc-module-header" id="ParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L95">interface ParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the ElastiCache parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L103">property family</a>
</h3>

```typescript
family: pulumi.Input<string>;
```


The family of the ElastiCache parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L107">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ElastiCache parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L111">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of ElastiCache parameters to apply.

<h2 class="pdoc-module-header" id="ParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L73">interface ParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L77">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the ElastiCache parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L81">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The family of the ElastiCache parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the ElastiCache parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/parameterGroup.ts#L89">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of ElastiCache parameters to apply.

<h2 class="pdoc-module-header" id="ReplicationGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L374">interface ReplicationGroupArgs</a>
</h2>

The set of arguments for constructing a ReplicationGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L378">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L382">property atRestEncryptionEnabled</a>
</h3>

```typescript
atRestEncryptionEnabled?: pulumi.Input<boolean>;
```


Whether to enable encryption at rest.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L386">property authToken</a>
</h3>

```typescript
authToken?: pulumi.Input<string>;
```


The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L390">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L394">property automaticFailoverEnabled</a>
</h3>

```typescript
automaticFailoverEnabled?: pulumi.Input<boolean>;
```


Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L398">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L402">property clusterMode</a>
</h3>

```typescript
clusterMode?: pulumi.Input<{ ... }>;
```


Create a native redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode documented below. Only 1 `cluster_mode` block is allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L406">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L410">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The version number of the cache engine to be used for the cache clusters in this replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L416">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L420">property nodeType</a>
</h3>

```typescript
nodeType?: pulumi.Input<string>;
```


The compute and memory capacity of the nodes in the node group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L426">property notificationTopicArn</a>
</h3>

```typescript
notificationTopicArn?: pulumi.Input<string>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L430">property numberCacheClusters</a>
</h3>

```typescript
numberCacheClusters?: pulumi.Input<number>;
```


The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L434">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L438">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L442">property replicationGroupDescription</a>
</h3>

```typescript
replicationGroupDescription: pulumi.Input<string>;
```


A user-created description for the replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L446">property replicationGroupId</a>
</h3>

```typescript
replicationGroupId: pulumi.Input<string>;
```


The replication group identifier. This parameter is stored as a lowercase string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L450">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L454">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of cache security group names to associate with this replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L460">property snapshotArns</a>
</h3>

```typescript
snapshotArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L464">property snapshotName</a>
</h3>

```typescript
snapshotName?: pulumi.Input<string>;
```


The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L472">property snapshotRetentionLimit</a>
</h3>

```typescript
snapshotRetentionLimit?: pulumi.Input<number>;
```


The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L477">property snapshotWindow</a>
</h3>

```typescript
snapshotWindow?: pulumi.Input<string>;
```


The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L481">property subnetGroupName</a>
</h3>

```typescript
subnetGroupName?: pulumi.Input<string>;
```


The name of the cache subnet group to be used for the replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L485">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L489">property transitEncryptionEnabled</a>
</h3>

```typescript
transitEncryptionEnabled?: pulumi.Input<boolean>;
```


Whether to enable encryption in transit.

<h2 class="pdoc-module-header" id="ReplicationGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L241">interface ReplicationGroupState</a>
</h2>

Input properties used for looking up and filtering ReplicationGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L245">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L249">property atRestEncryptionEnabled</a>
</h3>

```typescript
atRestEncryptionEnabled?: pulumi.Input<boolean>;
```


Whether to enable encryption at rest.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L253">property authToken</a>
</h3>

```typescript
authToken?: pulumi.Input<string>;
```


The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L257">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L261">property automaticFailoverEnabled</a>
</h3>

```typescript
automaticFailoverEnabled?: pulumi.Input<boolean>;
```


Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L265">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L269">property clusterMode</a>
</h3>

```typescript
clusterMode?: pulumi.Input<{ ... }>;
```


Create a native redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode documented below. Only 1 `cluster_mode` block is allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L273">property configurationEndpointAddress</a>
</h3>

```typescript
configurationEndpointAddress?: pulumi.Input<string>;
```


The address of the replication group configuration endpoint when cluster mode is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L277">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L281">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The version number of the cache engine to be used for the cache clusters in this replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L287">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L291">property memberClusters</a>
</h3>

```typescript
memberClusters?: pulumi.Input<pulumi.Input<string>[]>;
```


The identifiers of all the nodes that are part of this replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L295">property nodeType</a>
</h3>

```typescript
nodeType?: pulumi.Input<string>;
```


The compute and memory capacity of the nodes in the node group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L301">property notificationTopicArn</a>
</h3>

```typescript
notificationTopicArn?: pulumi.Input<string>;
```


An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L305">property numberCacheClusters</a>
</h3>

```typescript
numberCacheClusters?: pulumi.Input<number>;
```


The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L309">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L313">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L317">property primaryEndpointAddress</a>
</h3>

```typescript
primaryEndpointAddress?: pulumi.Input<string>;
```


(Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L321">property replicationGroupDescription</a>
</h3>

```typescript
replicationGroupDescription?: pulumi.Input<string>;
```


A user-created description for the replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L325">property replicationGroupId</a>
</h3>

```typescript
replicationGroupId?: pulumi.Input<string>;
```


The replication group identifier. This parameter is stored as a lowercase string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L329">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L333">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of cache security group names to associate with this replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L339">property snapshotArns</a>
</h3>

```typescript
snapshotArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L343">property snapshotName</a>
</h3>

```typescript
snapshotName?: pulumi.Input<string>;
```


The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L351">property snapshotRetentionLimit</a>
</h3>

```typescript
snapshotRetentionLimit?: pulumi.Input<number>;
```


The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L356">property snapshotWindow</a>
</h3>

```typescript
snapshotWindow?: pulumi.Input<string>;
```


The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L360">property subnetGroupName</a>
</h3>

```typescript
subnetGroupName?: pulumi.Input<string>;
```


The name of the cache subnet group to be used for the replication group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L364">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/replicationGroup.ts#L368">property transitEncryptionEnabled</a>
</h3>

```typescript
transitEncryptionEnabled?: pulumi.Input<boolean>;
```


Whether to enable encryption in transit.

<h2 class="pdoc-module-header" id="SecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L92">interface SecurityGroupArgs</a>
</h2>

The set of arguments for constructing a SecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L96">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


description for the cache security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the cache security group. This value is stored as a lowercase string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L105">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames: pulumi.Input<pulumi.Input<string>[]>;
```


List of EC2 security group names to be
authorized for ingress to the cache security group

<h2 class="pdoc-module-header" id="SecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L73">interface SecurityGroupState</a>
</h2>

Input properties used for looking up and filtering SecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L77">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


description for the cache security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the cache security group. This value is stored as a lowercase string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/securityGroup.ts#L86">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


List of EC2 security group names to be
authorized for ingress to the cache security group

<h2 class="pdoc-module-header" id="SubnetGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L89">interface SubnetGroupArgs</a>
</h2>

The set of arguments for constructing a SubnetGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L93">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description for the cache subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the cache subnet group. Elasticache converts this name to lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L101">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC Subnet IDs for the cache subnet group

<h2 class="pdoc-module-header" id="SubnetGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L71">interface SubnetGroupState</a>
</h2>

Input properties used for looking up and filtering SubnetGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L75">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description for the cache subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the cache subnet group. Elasticache converts this name to lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticache/subnetGroup.ts#L83">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC Subnet IDs for the cache subnet group

