---
title: Module neptune
---

<a href="../index.html">@pulumi/aws</a> &gt; neptune

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#ClusterInstance">class ClusterInstance</a>
* <a href="#ClusterParameterGroup">class ClusterParameterGroup</a>
* <a href="#ClusterSnapshot">class ClusterSnapshot</a>
* <a href="#EventSubscription">class EventSubscription</a>
* <a href="#ParameterGroup">class ParameterGroup</a>
* <a href="#SubnetGroup">class SubnetGroup</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterInstanceArgs">interface ClusterInstanceArgs</a>
* <a href="#ClusterInstanceState">interface ClusterInstanceState</a>
* <a href="#ClusterParameterGroupArgs">interface ClusterParameterGroupArgs</a>
* <a href="#ClusterParameterGroupState">interface ClusterParameterGroupState</a>
* <a href="#ClusterSnapshotArgs">interface ClusterSnapshotArgs</a>
* <a href="#ClusterSnapshotState">interface ClusterSnapshotState</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#EventSubscriptionArgs">interface EventSubscriptionArgs</a>
* <a href="#EventSubscriptionState">interface EventSubscriptionState</a>
* <a href="#ParameterGroupArgs">interface ParameterGroupArgs</a>
* <a href="#ParameterGroupState">interface ParameterGroupState</a>
* <a href="#SubnetGroupArgs">interface SubnetGroupArgs</a>
* <a href="#SubnetGroupState">interface SubnetGroupState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts">neptune/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts">neptune/clusterInstance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts">neptune/clusterParameterGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts">neptune/clusterSnapshot.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts">neptune/eventSubscription.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts">neptune/parameterGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts">neptune/subnetGroup.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L18">class Cluster</a>
</h2>

Provides an Neptune Cluster Resource. A Cluster Resource defines attributes that are
applied to the entire cluster of Neptune Cluster Instances.

Changes to a Neptune Cluster can occur when you manually change a
parameter, such as `backup_retention_period`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change immediately
(see documentation below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L142">constructor</a>
</h3>

```typescript
new Cluster(name: string, args?: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L27">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L34">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean>;
```


Specifies whether any cluster modifications are applied immediately, or during the next maintenance window. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L38">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Neptune Cluster Amazon Resource Name (ARN)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L42">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[]>;
```


A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L46">property backupRetentionPeriod</a>
</h3>

```typescript
public backupRetentionPeriod: pulumi.Output<number | undefined>;
```


The days to retain backups for. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L50">property clusterIdentifier</a>
</h3>

```typescript
public clusterIdentifier: pulumi.Output<string>;
```


The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L54">property clusterIdentifierPrefix</a>
</h3>

```typescript
public clusterIdentifierPrefix: pulumi.Output<string>;
```


Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L58">property clusterMembers</a>
</h3>

```typescript
public clusterMembers: pulumi.Output<string[]>;
```


List of Neptune Instances that are a part of this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L62">property clusterResourceId</a>
</h3>

```typescript
public clusterResourceId: pulumi.Output<string>;
```


The Neptune Cluster Resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L66">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The DNS address of the Neptune instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L70">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string | undefined>;
```


The name of the database engine to be used for this Neptune cluster. Defaults to `neptune`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L74">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L78">property finalSnapshotIdentifier</a>
</h3>

```typescript
public finalSnapshotIdentifier: pulumi.Output<string | undefined>;
```


The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted, no final snapshot will be made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L82">property hostedZoneId</a>
</h3>

```typescript
public hostedZoneId: pulumi.Output<string>;
```


The Route53 Hosted Zone ID of the endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L86">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
public iamDatabaseAuthenticationEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L90">property iamRoles</a>
</h3>

```typescript
public iamRoles: pulumi.Output<string[] | undefined>;
```


A List of ARNs for the IAM roles to associate to the Neptune Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L94">property kmsKeyArn</a>
</h3>

```typescript
public kmsKeyArn: pulumi.Output<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_arn`, `storage_encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L98">property neptuneClusterParameterGroupName</a>
</h3>

```typescript
public neptuneClusterParameterGroupName: pulumi.Output<string | undefined>;
```


A cluster parameter group to associate with the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L102">property neptuneSubnetGroupName</a>
</h3>

```typescript
public neptuneSubnetGroupName: pulumi.Output<string>;
```


A Neptune subnet group to associate with this Neptune instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L106">property port</a>
</h3>

```typescript
public port: pulumi.Output<number | undefined>;
```


The port on which the Neptune accepts connections. Default is `8182`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L110">property preferredBackupWindow</a>
</h3>

```typescript
public preferredBackupWindow: pulumi.Output<string>;
```


The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L114">property preferredMaintenanceWindow</a>
</h3>

```typescript
public preferredMaintenanceWindow: pulumi.Output<string>;
```


The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L118">property readerEndpoint</a>
</h3>

```typescript
public readerEndpoint: pulumi.Output<string>;
```


A read-only endpoint for the Neptune cluster, automatically load-balanced across replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L122">property replicationSourceIdentifier</a>
</h3>

```typescript
public replicationSourceIdentifier: pulumi.Output<string | undefined>;
```


ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be created as a Read Replica.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L126">property skipFinalSnapshot</a>
</h3>

```typescript
public skipFinalSnapshot: pulumi.Output<boolean | undefined>;
```


Determines whether a final Neptune snapshot is created before the Neptune cluster is deleted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot is created before the Neptune cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L130">property snapshotIdentifier</a>
</h3>

```typescript
public snapshotIdentifier: pulumi.Output<string | undefined>;
```


Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L134">property storageEncrypted</a>
</h3>

```typescript
public storageEncrypted: pulumi.Output<boolean | undefined>;
```


Specifies whether the Neptune cluster is encrypted. The default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L138">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the Neptune cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L142">property vpcSecurityGroupIds</a>
</h3>

```typescript
public vpcSecurityGroupIds: pulumi.Output<string[]>;
```


List of VPC security groups to associate with the Cluster

<h2 class="pdoc-module-header" id="ClusterInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L14">class ClusterInstance</a>
</h2>

A Cluster Instance Resource defines attributes that are specific to a single instance in a Neptune Cluster.

You can simply add neptune instances and Neptune manages the replication. You can use the [count][1]
meta-parameter to make multiple instances and join them all to the same Neptune Cluster, or you may specify different Cluster Instance resources with various `instance_class` sizes.


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L124">constructor</a>
</h3>

```typescript
new ClusterInstance(name: string, args: ClusterInstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClusterInstance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterInstanceState): ClusterInstance
```


Get an existing ClusterInstance resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L30">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The hostname of the instance. See also `endpoint` and `port`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L35">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean>;
```


Specifies whether any instance modifications
are applied immediately, or during the next maintenance window. Default is`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L39">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of neptune instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L43">property autoMinorVersionUpgrade</a>
</h3>

```typescript
public autoMinorVersionUpgrade: pulumi.Output<boolean | undefined>;
```


Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L47">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The EC2 Availability Zone that the neptune instance is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L51">property clusterIdentifier</a>
</h3>

```typescript
public clusterIdentifier: pulumi.Output<string>;
```


The identifier of the [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L55">property dbiResourceId</a>
</h3>

```typescript
public dbiResourceId: pulumi.Output<string>;
```


The region-unique, immutable identifier for the neptune instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L59">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The connection endpoint in `address:port` format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L63">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string | undefined>;
```


The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L67">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The neptune engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L71">property identifier</a>
</h3>

```typescript
public identifier: pulumi.Output<string>;
```


The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L75">property identifierPrefix</a>
</h3>

```typescript
public identifierPrefix: pulumi.Output<string>;
```


Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L79">property instanceClass</a>
</h3>

```typescript
public instanceClass: pulumi.Output<string>;
```


The instance class to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L83">property kmsKeyArn</a>
</h3>

```typescript
public kmsKeyArn: pulumi.Output<string>;
```


The ARN for the KMS encryption key if one is set to the neptune cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L87">property neptuneParameterGroupName</a>
</h3>

```typescript
public neptuneParameterGroupName: pulumi.Output<string | undefined>;
```


The name of the neptune parameter group to associate with this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L91">property neptuneSubnetGroupName</a>
</h3>

```typescript
public neptuneSubnetGroupName: pulumi.Output<string>;
```


A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L95">property port</a>
</h3>

```typescript
public port: pulumi.Output<number | undefined>;
```


The port on which the DB accepts connections. Defaults to `8182`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L99">property preferredBackupWindow</a>
</h3>

```typescript
public preferredBackupWindow: pulumi.Output<string>;
```


The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L104">property preferredMaintenanceWindow</a>
</h3>

```typescript
public preferredMaintenanceWindow: pulumi.Output<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L108">property promotionTier</a>
</h3>

```typescript
public promotionTier: pulumi.Output<number | undefined>;
```


Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L112">property publiclyAccessible</a>
</h3>

```typescript
public publiclyAccessible: pulumi.Output<boolean | undefined>;
```


Bool to control if instance is publicly accessible. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L116">property storageEncrypted</a>
</h3>

```typescript
public storageEncrypted: pulumi.Output<boolean>;
```


Specifies whether the neptune cluster is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L120">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L124">property writer</a>
</h3>

```typescript
public writer: pulumi.Output<boolean>;
```


Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.

<h2 class="pdoc-module-header" id="ClusterParameterGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L10">class ClusterParameterGroup</a>
</h2>

Manages a Neptune Cluster Parameter Group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L50">constructor</a>
</h3>

```typescript
new ClusterParameterGroup(name: string, args: ClusterParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClusterParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterParameterGroupState): ClusterParameterGroup
```


Get an existing ClusterParameterGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the neptune cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the neptune cluster parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L34">property family</a>
</h3>

```typescript
public family: pulumi.Output<string>;
```


The family of the neptune cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the neptune parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L42">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L46">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[] | undefined>;
```


A list of neptune parameters to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L50">property tags</a>
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

<h2 class="pdoc-module-header" id="ClusterSnapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L10">class ClusterSnapshot</a>
</h2>

Manages a Neptune database cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L76">constructor</a>
</h3>

```typescript
new ClusterSnapshot(name: string, args: ClusterSnapshotArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClusterSnapshot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterSnapshotState): ClusterSnapshot
```


Get an existing ClusterSnapshot resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L26">property allocatedStorage</a>
</h3>

```typescript
public allocatedStorage: pulumi.Output<number>;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L30">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[]>;
```


List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L34">property dbClusterIdentifier</a>
</h3>

```typescript
public dbClusterIdentifier: pulumi.Output<string>;
```


The DB Cluster Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L38">property dbClusterSnapshotArn</a>
</h3>

```typescript
public dbClusterSnapshotArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) for the DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L42">property dbClusterSnapshotIdentifier</a>
</h3>

```typescript
public dbClusterSnapshotIdentifier: pulumi.Output<string>;
```


The Identifier for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L46">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string>;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L50">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


Version of the database engine for this DB cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L54">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L58">property licenseModel</a>
</h3>

```typescript
public licenseModel: pulumi.Output<string>;
```


License model information for the restored DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L62">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


Port that the DB cluster was listening on at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L63">property snapshotType</a>
</h3>

```typescript
public snapshotType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L64">property sourceDbClusterSnapshotArn</a>
</h3>

```typescript
public sourceDbClusterSnapshotArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L68">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The status of this DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L72">property storageEncrypted</a>
</h3>

```typescript
public storageEncrypted: pulumi.Output<boolean>;
```


Specifies whether the DB cluster snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L76">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC ID associated with the DB cluster snapshot.

<h2 class="pdoc-module-header" id="EventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L7">class EventSubscription</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L53">constructor</a>
</h3>

```typescript
new EventSubscription(name: string, args: EventSubscriptionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventSubscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventSubscriptionState): EventSubscription
```


Get an existing EventSubscription resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L20">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L21">property customerAwsId</a>
</h3>

```typescript
public customerAwsId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L25">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


A boolean flag to enable/disable the subscription. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L29">property eventCategories</a>
</h3>

```typescript
public eventCategories: pulumi.Output<string[] | undefined>;
```


A list of event categories for a `source_type` that you want to subscribe to. Run `aws neptune describe-event-categories` to find all the event categories.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Neptune event subscription. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L37">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


The name of the Neptune event subscription. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L41">property snsTopicArn</a>
</h3>

```typescript
public snsTopicArn: pulumi.Output<string>;
```


The ARN of the SNS topic to send events to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L45">property sourceIds</a>
</h3>

```typescript
public sourceIds: pulumi.Output<string[] | undefined>;
```


A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a `source_type` must also be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L49">property sourceType</a>
</h3>

```typescript
public sourceType: pulumi.Output<string | undefined>;
```


The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L53">property tags</a>
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

<h2 class="pdoc-module-header" id="ParameterGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L12">class ParameterGroup</a>
</h2>

Manages a Neptune Parameter Group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L48">constructor</a>
</h3>

```typescript
new ParameterGroup(name: string, args: ParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Neptune parameter group Amazon Resource Name (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the Neptune parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L36">property family</a>
</h3>

```typescript
public family: pulumi.Output<string>;
```


The family of the Neptune parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L40">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Neptune parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L44">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[] | undefined>;
```


A list of Neptune parameters to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L48">property tags</a>
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

<h2 class="pdoc-module-header" id="SubnetGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L12">class SubnetGroup</a>
</h2>

Provides an Neptune subnet group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L48">constructor</a>
</h3>

```typescript
new SubnetGroup(name: string, args: SubnetGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the neptune subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the neptune subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the neptune subnet group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L40">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L44">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


A list of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L48">property tags</a>
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

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L340">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L344">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any cluster modifications are applied immediately, or during the next maintenance window. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L348">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L352">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L356">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L360">property clusterIdentifierPrefix</a>
</h3>

```typescript
clusterIdentifierPrefix?: pulumi.Input<string>;
```


Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L364">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for this Neptune cluster. Defaults to `neptune`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L368">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L372">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted, no final snapshot will be made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L376">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L380">property iamRoles</a>
</h3>

```typescript
iamRoles?: pulumi.Input<pulumi.Input<string>[]>;
```


A List of ARNs for the IAM roles to associate to the Neptune Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L384">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_arn`, `storage_encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L388">property neptuneClusterParameterGroupName</a>
</h3>

```typescript
neptuneClusterParameterGroupName?: pulumi.Input<string>;
```


A cluster parameter group to associate with the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L392">property neptuneSubnetGroupName</a>
</h3>

```typescript
neptuneSubnetGroupName?: pulumi.Input<string>;
```


A Neptune subnet group to associate with this Neptune instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L396">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the Neptune accepts connections. Default is `8182`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L400">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L404">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L408">property replicationSourceIdentifier</a>
</h3>

```typescript
replicationSourceIdentifier?: pulumi.Input<string>;
```


ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be created as a Read Replica.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L412">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final Neptune snapshot is created before the Neptune cluster is deleted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot is created before the Neptune cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L416">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L420">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the Neptune cluster is encrypted. The default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L424">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the Neptune cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L428">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to associate with the Cluster

<h2 class="pdoc-module-header" id="ClusterInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L306">interface ClusterInstanceArgs</a>
</h2>

The set of arguments for constructing a ClusterInstance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L311">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any instance modifications
are applied immediately, or during the next maintenance window. Default is`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L315">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L319">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The EC2 Availability Zone that the neptune instance is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L323">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier: pulumi.Input<string>;
```


The identifier of the [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L327">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L331">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The neptune engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L335">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L339">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L343">property instanceClass</a>
</h3>

```typescript
instanceClass: pulumi.Input<string>;
```


The instance class to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L347">property neptuneParameterGroupName</a>
</h3>

```typescript
neptuneParameterGroupName?: pulumi.Input<string>;
```


The name of the neptune parameter group to associate with this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L351">property neptuneSubnetGroupName</a>
</h3>

```typescript
neptuneSubnetGroupName?: pulumi.Input<string>;
```


A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L355">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections. Defaults to `8182`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L359">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L364">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L368">property promotionTier</a>
</h3>

```typescript
promotionTier?: pulumi.Input<number>;
```


Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L372">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly accessible. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L376">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the instance.

<h2 class="pdoc-module-header" id="ClusterInstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L202">interface ClusterInstanceState</a>
</h2>

Input properties used for looking up and filtering ClusterInstance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L206">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The hostname of the instance. See also `endpoint` and `port`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L211">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any instance modifications
are applied immediately, or during the next maintenance window. Default is`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L215">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of neptune instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L219">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L223">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The EC2 Availability Zone that the neptune instance is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L227">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The identifier of the [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L231">property dbiResourceId</a>
</h3>

```typescript
dbiResourceId?: pulumi.Input<string>;
```


The region-unique, immutable identifier for the neptune instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L235">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The connection endpoint in `address:port` format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L239">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L243">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The neptune engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L247">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L251">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L255">property instanceClass</a>
</h3>

```typescript
instanceClass?: pulumi.Input<string>;
```


The instance class to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L259">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


The ARN for the KMS encryption key if one is set to the neptune cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L263">property neptuneParameterGroupName</a>
</h3>

```typescript
neptuneParameterGroupName?: pulumi.Input<string>;
```


The name of the neptune parameter group to associate with this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L267">property neptuneSubnetGroupName</a>
</h3>

```typescript
neptuneSubnetGroupName?: pulumi.Input<string>;
```


A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L271">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections. Defaults to `8182`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L275">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L280">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L284">property promotionTier</a>
</h3>

```typescript
promotionTier?: pulumi.Input<number>;
```


Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L288">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly accessible. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L292">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the neptune cluster is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L296">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterInstance.ts#L300">property writer</a>
</h3>

```typescript
writer?: pulumi.Input<boolean>;
```


Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.

<h2 class="pdoc-module-header" id="ClusterParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L125">interface ClusterParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ClusterParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L129">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the neptune cluster parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L133">property family</a>
</h3>

```typescript
family: pulumi.Input<string>;
```


The family of the neptune cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the neptune parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L141">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L145">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of neptune parameters to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L149">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ClusterParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L91">interface ClusterParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ClusterParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L95">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the neptune cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the neptune cluster parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L103">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The family of the neptune cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L107">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the neptune parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L111">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L115">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of neptune parameters to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterParameterGroup.ts#L119">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ClusterSnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L196">interface ClusterSnapshotArgs</a>
</h2>

The set of arguments for constructing a ClusterSnapshot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L200">property dbClusterIdentifier</a>
</h3>

```typescript
dbClusterIdentifier: pulumi.Input<string>;
```


The DB Cluster Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L204">property dbClusterSnapshotIdentifier</a>
</h3>

```typescript
dbClusterSnapshotIdentifier: pulumi.Input<string>;
```


The Identifier for the snapshot.

<h2 class="pdoc-module-header" id="ClusterSnapshotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L136">interface ClusterSnapshotState</a>
</h2>

Input properties used for looking up and filtering ClusterSnapshot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L140">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage?: pulumi.Input<number>;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L144">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L148">property dbClusterIdentifier</a>
</h3>

```typescript
dbClusterIdentifier?: pulumi.Input<string>;
```


The DB Cluster Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L152">property dbClusterSnapshotArn</a>
</h3>

```typescript
dbClusterSnapshotArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) for the DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L156">property dbClusterSnapshotIdentifier</a>
</h3>

```typescript
dbClusterSnapshotIdentifier?: pulumi.Input<string>;
```


The Identifier for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L160">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L164">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


Version of the database engine for this DB cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L168">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L172">property licenseModel</a>
</h3>

```typescript
licenseModel?: pulumi.Input<string>;
```


License model information for the restored DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L176">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


Port that the DB cluster was listening on at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L177">property snapshotType</a>
</h3>

```typescript
snapshotType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L178">property sourceDbClusterSnapshotArn</a>
</h3>

```typescript
sourceDbClusterSnapshotArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L182">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The status of this DB Cluster Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L186">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB cluster snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/clusterSnapshot.ts#L190">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC ID associated with the DB cluster snapshot.

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L222">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L226">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any cluster modifications are applied immediately, or during the next maintenance window. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L230">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Neptune Cluster Amazon Resource Name (ARN)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L234">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L238">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L242">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L246">property clusterIdentifierPrefix</a>
</h3>

```typescript
clusterIdentifierPrefix?: pulumi.Input<string>;
```


Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L250">property clusterMembers</a>
</h3>

```typescript
clusterMembers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of Neptune Instances that are a part of this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L254">property clusterResourceId</a>
</h3>

```typescript
clusterResourceId?: pulumi.Input<string>;
```


The Neptune Cluster Resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L258">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The DNS address of the Neptune instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L262">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for this Neptune cluster. Defaults to `neptune`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L266">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L270">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted, no final snapshot will be made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L274">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId?: pulumi.Input<string>;
```


The Route53 Hosted Zone ID of the endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L278">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L282">property iamRoles</a>
</h3>

```typescript
iamRoles?: pulumi.Input<pulumi.Input<string>[]>;
```


A List of ARNs for the IAM roles to associate to the Neptune Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L286">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_arn`, `storage_encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L290">property neptuneClusterParameterGroupName</a>
</h3>

```typescript
neptuneClusterParameterGroupName?: pulumi.Input<string>;
```


A cluster parameter group to associate with the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L294">property neptuneSubnetGroupName</a>
</h3>

```typescript
neptuneSubnetGroupName?: pulumi.Input<string>;
```


A Neptune subnet group to associate with this Neptune instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L298">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the Neptune accepts connections. Default is `8182`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L302">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L306">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L310">property readerEndpoint</a>
</h3>

```typescript
readerEndpoint?: pulumi.Input<string>;
```


A read-only endpoint for the Neptune cluster, automatically load-balanced across replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L314">property replicationSourceIdentifier</a>
</h3>

```typescript
replicationSourceIdentifier?: pulumi.Input<string>;
```


ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be created as a Read Replica.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L318">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final Neptune snapshot is created before the Neptune cluster is deleted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot is created before the Neptune cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L322">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L326">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the Neptune cluster is encrypted. The default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L330">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the Neptune cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/cluster.ts#L334">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to associate with the Cluster

<h2 class="pdoc-module-header" id="EventSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L140">interface EventSubscriptionArgs</a>
</h2>

The set of arguments for constructing a EventSubscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L144">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable the subscription. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L148">property eventCategories</a>
</h3>

```typescript
eventCategories?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of event categories for a `source_type` that you want to subscribe to. Run `aws neptune describe-event-categories` to find all the event categories.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L152">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Neptune event subscription. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L156">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The name of the Neptune event subscription. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L160">property snsTopicArn</a>
</h3>

```typescript
snsTopicArn: pulumi.Input<string>;
```


The ARN of the SNS topic to send events to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L164">property sourceIds</a>
</h3>

```typescript
sourceIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a `source_type` must also be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L168">property sourceType</a>
</h3>

```typescript
sourceType?: pulumi.Input<string>;
```


The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L172">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventSubscriptionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L100">interface EventSubscriptionState</a>
</h2>

Input properties used for looking up and filtering EventSubscription resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L101">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L102">property customerAwsId</a>
</h3>

```typescript
customerAwsId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L106">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable the subscription. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L110">property eventCategories</a>
</h3>

```typescript
eventCategories?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of event categories for a `source_type` that you want to subscribe to. Run `aws neptune describe-event-categories` to find all the event categories.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L114">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Neptune event subscription. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L118">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The name of the Neptune event subscription. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L122">property snsTopicArn</a>
</h3>

```typescript
snsTopicArn?: pulumi.Input<string>;
```


The ARN of the SNS topic to send events to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L126">property sourceIds</a>
</h3>

```typescript
sourceIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a `source_type` must also be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L130">property sourceType</a>
</h3>

```typescript
sourceType?: pulumi.Input<string>;
```


The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/eventSubscription.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L117">interface ParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L121">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the Neptune parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L125">property family</a>
</h3>

```typescript
family: pulumi.Input<string>;
```


The family of the Neptune parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Neptune parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L133">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Neptune parameters to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L137">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L87">interface ParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L91">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Neptune parameter group Amazon Resource Name (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L95">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the Neptune parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L99">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The family of the Neptune parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Neptune parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L107">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Neptune parameters to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/parameterGroup.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SubnetGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L117">interface SubnetGroupArgs</a>
</h2>

The set of arguments for constructing a SubnetGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L121">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the neptune subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the neptune subnet group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L129">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L133">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L137">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SubnetGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L87">interface SubnetGroupState</a>
</h2>

Input properties used for looking up and filtering SubnetGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L91">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the neptune subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L95">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the neptune subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the neptune subnet group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L103">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L107">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/neptune/subnetGroup.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

