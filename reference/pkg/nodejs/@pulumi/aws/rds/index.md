---
title: Module rds
---

<a href="../index.html">@pulumi/aws</a> &gt; rds

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#ClusterInstance">class ClusterInstance</a>
* <a href="#ClusterParameterGroup">class ClusterParameterGroup</a>
* <a href="#EventSubscription">class EventSubscription</a>
* <a href="#Instance">class Instance</a>
* <a href="#OptionGroup">class OptionGroup</a>
* <a href="#ParameterGroup">class ParameterGroup</a>
* <a href="#SecurityGroup">class SecurityGroup</a>
* <a href="#Snapshot">class Snapshot</a>
* <a href="#SubnetGroup">class SubnetGroup</a>
* <a href="#getCluster">function getCluster</a>
* <a href="#getInstance">function getInstance</a>
* <a href="#getSnapshot">function getSnapshot</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterInstanceArgs">interface ClusterInstanceArgs</a>
* <a href="#ClusterInstanceState">interface ClusterInstanceState</a>
* <a href="#ClusterParameterGroupArgs">interface ClusterParameterGroupArgs</a>
* <a href="#ClusterParameterGroupState">interface ClusterParameterGroupState</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#EventSubscriptionArgs">interface EventSubscriptionArgs</a>
* <a href="#EventSubscriptionState">interface EventSubscriptionState</a>
* <a href="#GetClusterArgs">interface GetClusterArgs</a>
* <a href="#GetClusterResult">interface GetClusterResult</a>
* <a href="#GetInstanceArgs">interface GetInstanceArgs</a>
* <a href="#GetInstanceResult">interface GetInstanceResult</a>
* <a href="#GetSnapshotArgs">interface GetSnapshotArgs</a>
* <a href="#GetSnapshotResult">interface GetSnapshotResult</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceState">interface InstanceState</a>
* <a href="#OptionGroupArgs">interface OptionGroupArgs</a>
* <a href="#OptionGroupState">interface OptionGroupState</a>
* <a href="#ParameterGroupArgs">interface ParameterGroupArgs</a>
* <a href="#ParameterGroupState">interface ParameterGroupState</a>
* <a href="#SecurityGroupArgs">interface SecurityGroupArgs</a>
* <a href="#SecurityGroupState">interface SecurityGroupState</a>
* <a href="#SnapshotArgs">interface SnapshotArgs</a>
* <a href="#SnapshotState">interface SnapshotState</a>
* <a href="#SubnetGroupArgs">interface SubnetGroupArgs</a>
* <a href="#SubnetGroupState">interface SubnetGroupState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts">rds/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts">rds/clusterInstance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts">rds/clusterParameterGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts">rds/eventSubscription.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts">rds/getCluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts">rds/getInstance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts">rds/getSnapshot.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts">rds/instance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts">rds/optionGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts">rds/parameterGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts">rds/securityGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts">rds/snapshot.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts">rds/subnetGroup.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L34">class Cluster</a>
</h2>

Provides an RDS Cluster Resource. A Cluster Resource defines attributes that are
applied to the entire cluster of [RDS Cluster Instances][3]. Use the RDS Cluster
resource and RDS Cluster Instances to create and use Amazon Aurora, a MySQL-compatible
database engine.

For more information on Amazon Aurora, see [Aurora on Amazon RDS][2] in the Amazon RDS User Guide.

For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

Changes to a RDS Cluster can occur when you manually change a
parameter, such as `port`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change immediately
(see documentation below).

~> **Note:** using `apply_immediately` can result in a
brief downtime as the server reboots. See the AWS Docs on [RDS Maintenance][4]
for more information.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L193">constructor</a>
</h3>

```typescript
new Cluster(name: string, args?: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L43">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L52">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean>;
```


Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L56">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L61">property availabilityZones</a>
</h3>

```typescript
public availabilityZones: pulumi.Output<string[]>;
```


A list of EC2 Availability Zones that
instances in the DB cluster can be created in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L65">property backtrackWindow</a>
</h3>

```typescript
public backtrackWindow: pulumi.Output<number | undefined>;
```


The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L69">property backupRetentionPeriod</a>
</h3>

```typescript
public backupRetentionPeriod: pulumi.Output<number | undefined>;
```


The days to retain backups for. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L73">property clusterIdentifier</a>
</h3>

```typescript
public clusterIdentifier: pulumi.Output<string>;
```


The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L77">property clusterIdentifierPrefix</a>
</h3>

```typescript
public clusterIdentifierPrefix: pulumi.Output<string>;
```


Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L81">property clusterMembers</a>
</h3>

```typescript
public clusterMembers: pulumi.Output<string[]>;
```


List of RDS Instances that are a part of this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L85">property clusterResourceId</a>
</h3>

```typescript
public clusterResourceId: pulumi.Output<string>;
```


The RDS Cluster Resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L89">property databaseName</a>
</h3>

```typescript
public databaseName: pulumi.Output<string>;
```


Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L93">property dbClusterParameterGroupName</a>
</h3>

```typescript
public dbClusterParameterGroupName: pulumi.Output<string>;
```


A cluster parameter group to associate with the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L97">property dbSubnetGroupName</a>
</h3>

```typescript
public dbSubnetGroupName: pulumi.Output<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws_rds_cluster_instance`](/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L102">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
public enabledCloudwatchLogsExports: pulumi.Output<string[] | undefined>;
```


List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L106">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The DNS address of the RDS instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L110">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string | undefined>;
```


The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L114">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L120">property finalSnapshotIdentifier</a>
</h3>

```typescript
public finalSnapshotIdentifier: pulumi.Output<string | undefined>;
```


The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L124">property hostedZoneId</a>
</h3>

```typescript
public hostedZoneId: pulumi.Output<string>;
```


The Route53 Hosted Zone ID of the endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L128">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
public iamDatabaseAuthenticationEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L132">property iamRoles</a>
</h3>

```typescript
public iamRoles: pulumi.Output<string[] | undefined>;
```


A List of ARNs for the IAM roles to associate to the RDS Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L136">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L141">property masterPassword</a>
</h3>

```typescript
public masterPassword: pulumi.Output<string | undefined>;
```


Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L145">property masterUsername</a>
</h3>

```typescript
public masterUsername: pulumi.Output<string>;
```


Username for the master DB user. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L149">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The port on which the DB accepts connections

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L154">property preferredBackupWindow</a>
</h3>

```typescript
public preferredBackupWindow: pulumi.Output<string>;
```


The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L158">property preferredMaintenanceWindow</a>
</h3>

```typescript
public preferredMaintenanceWindow: pulumi.Output<string>;
```


The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L163">property readerEndpoint</a>
</h3>

```typescript
public readerEndpoint: pulumi.Output<string>;
```


A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L167">property replicationSourceIdentifier</a>
</h3>

```typescript
public replicationSourceIdentifier: pulumi.Output<string | undefined>;
```


ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L168">property s3Import</a>
</h3>

```typescript
public s3Import: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L172">property skipFinalSnapshot</a>
</h3>

```typescript
public skipFinalSnapshot: pulumi.Output<boolean | undefined>;
```


Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L176">property snapshotIdentifier</a>
</h3>

```typescript
public snapshotIdentifier: pulumi.Output<string | undefined>;
```


Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L180">property sourceRegion</a>
</h3>

```typescript
public sourceRegion: pulumi.Output<string | undefined>;
```


The source region for an encrypted replica DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L184">property storageEncrypted</a>
</h3>

```typescript
public storageEncrypted: pulumi.Output<boolean | undefined>;
```


Specifies whether the DB cluster is encrypted. The default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L188">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L193">property vpcSecurityGroupIds</a>
</h3>

```typescript
public vpcSecurityGroupIds: pulumi.Output<string[]>;
```


List of VPC security groups to associate
with the Cluster

<h2 class="pdoc-module-header" id="ClusterInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L22">class ClusterInstance</a>
</h2>

Provides an RDS Cluster Resource Instance. A Cluster Instance Resource defines
attributes that are specific to a single instance in a [RDS Cluster][3],
specifically running Amazon Aurora.

Unlike other RDS resources that support replication, with Amazon Aurora you do
not designate a primary and subsequent replicas. Instead, you simply add RDS
Instances and Aurora manages the replication. You can use the [count][5]
meta-parameter to make multiple instances and join them all to the same RDS
Cluster, or you may specify different Cluster Instance resources with various
`instance_class` sizes.

For more information on Amazon Aurora, see [Aurora on Amazon RDS][2] in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L167">constructor</a>
</h3>

```typescript
new ClusterInstance(name: string, args: ClusterInstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClusterInstance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L31">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L39">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L43">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of cluster instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L47">property autoMinorVersionUpgrade</a>
</h3>

```typescript
public autoMinorVersionUpgrade: pulumi.Output<boolean | undefined>;
```


Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L51">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) about the details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L55">property clusterIdentifier</a>
</h3>

```typescript
public clusterIdentifier: pulumi.Output<string>;
```


The identifier of the [`aws_rds_cluster`](/docs/providers/aws/r/rds_cluster.html) in which to launch this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L59">property dbParameterGroupName</a>
</h3>

```typescript
public dbParameterGroupName: pulumi.Output<string>;
```


The name of the DB parameter group to associate with this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L63">property dbSubnetGroupName</a>
</h3>

```typescript
public dbSubnetGroupName: pulumi.Output<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` of the attached [`aws_rds_cluster`](/docs/providers/aws/r/rds_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L67">property dbiResourceId</a>
</h3>

```typescript
public dbiResourceId: pulumi.Output<string>;
```


The region-unique, immutable identifier for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L71">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The DNS address for this instance. May not be writable

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L78">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string | undefined>;
```


The name of the database engine to be used for the RDS instance. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L82">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L86">property identifier</a>
</h3>

```typescript
public identifier: pulumi.Output<string>;
```


The indentifier for the RDS instance, if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L90">property identifierPrefix</a>
</h3>

```typescript
public identifierPrefix: pulumi.Output<string>;
```


Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L109">property instanceClass</a>
</h3>

```typescript
public instanceClass: pulumi.Output<string>;
```


The instance class to use. For details on CPU
and memory, see [Scaling Aurora DB Instances][4]. Aurora currently
supports the below instance classes.
- db.t2.small
- db.t2.medium
- db.r3.large
- db.r3.xlarge
- db.r3.2xlarge
- db.r3.4xlarge
- db.r3.8xlarge
- db.r4.large
- db.r4.xlarge
- db.r4.2xlarge
- db.r4.4xlarge
- db.r4.8xlarge
- db.r4.16xlarge

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L113">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS encryption key if one is set to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L117">property monitoringInterval</a>
</h3>

```typescript
public monitoringInterval: pulumi.Output<number | undefined>;
```


The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L123">property monitoringRoleArn</a>
</h3>

```typescript
public monitoringRoleArn: pulumi.Output<string>;
```


The ARN for the IAM role that permits RDS to send
enhanced monitoring metrics to CloudWatch Logs. You can find more information on the [AWS Documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L127">property performanceInsightsEnabled</a>
</h3>

```typescript
public performanceInsightsEnabled: pulumi.Output<boolean>;
```


Specifies whether Performance Insights is enabled or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L131">property performanceInsightsKmsKeyId</a>
</h3>

```typescript
public performanceInsightsKmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L135">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The database port

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L140">property preferredBackupWindow</a>
</h3>

```typescript
public preferredBackupWindow: pulumi.Output<string>;
```


The daily time range during which automated backups are created if automated backups are enabled.
Eg: "04:00-09:00"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L145">property preferredMaintenanceWindow</a>
</h3>

```typescript
public preferredMaintenanceWindow: pulumi.Output<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L149">property promotionTier</a>
</h3>

```typescript
public promotionTier: pulumi.Output<number | undefined>;
```


Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L155">property publiclyAccessible</a>
</h3>

```typescript
public publiclyAccessible: pulumi.Output<boolean | undefined>;
```


Bool to control if instance is publicly accessible.
Default `false`. See the documentation on [Creating DB Instances][6] for more
details on controlling this property.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L159">property storageEncrypted</a>
</h3>

```typescript
public storageEncrypted: pulumi.Output<boolean>;
```


Specifies whether the DB cluster is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L163">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L167">property writer</a>
</h3>

```typescript
public writer: pulumi.Output<boolean>;
```


Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.

<h2 class="pdoc-module-header" id="ClusterParameterGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L13">class ClusterParameterGroup</a>
</h2>

Provides an RDS DB cluster parameter group resource. Documentation of the available parameters for various Aurora engines can be found at:
* [Aurora MySQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Reference.html)
* [Aurora PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L53">constructor</a>
</h3>

```typescript
new ClusterParameterGroup(name: string, args: ClusterParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClusterParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L22">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the db cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the DB cluster parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L37">property family</a>
</h3>

```typescript
public family: pulumi.Output<string>;
```


The family of the DB cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L45">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L49">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[] | undefined>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-cluster-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L53">property tags</a>
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

<h2 class="pdoc-module-header" id="EventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L11">class EventSubscription</a>
</h2>

Provides a DB event subscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L57">constructor</a>
</h3>

```typescript
new EventSubscription(name: string, args: EventSubscriptionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventSubscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L24">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L25">property customerAwsId</a>
</h3>

```typescript
public customerAwsId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L29">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


A boolean flag to enable/disable the subscription. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L33">property eventCategories</a>
</h3>

```typescript
public eventCategories: pulumi.Output<string[] | undefined>;
```


A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB event subscription. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L41">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


The name of the DB event subscription. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L45">property snsTopic</a>
</h3>

```typescript
public snsTopic: pulumi.Output<string>;
```


The SNS topic to send events to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L49">property sourceIds</a>
</h3>

```typescript
public sourceIds: pulumi.Output<string[] | undefined>;
```


A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L53">property sourceType</a>
</h3>

```typescript
public sourceType: pulumi.Output<string | undefined>;
```


The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L57">property tags</a>
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

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L30">class Instance</a>
</h2>

Provides an RDS instance resource.  A DB instance is an isolated database
environment in the cloud.  A DB instance can contain multiple user-created
databases.

Changes to a DB instance can occur when you manually change a parameter, such as
`allocated_storage`, and are reflected in the next maintenance window. Because
of this, Terraform may report a difference in its planning phase because a
modification has not yet taken place. You can use the `apply_immediately` flag
to instruct the service to apply the change immediately (see documentation
below).

When upgrading the major version of an engine, `allow_major_version_upgrade`
must be set to `true`.

~> **Note:** using `apply_immediately` can result in a brief downtime as the
server reboots. See the AWS Docs on [RDS Maintenance][2] for more information.

~> **Note:** All arguments including the username and password will be stored in
the raw state as plain-text. [Read more about sensitive data in
state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L324">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L39">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L46">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The hostname of the RDS instance. See also `endpoint` and `port`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L51">property allocatedStorage</a>
</h3>

```typescript
public allocatedStorage: pulumi.Output<number>;
```


(Required unless a `snapshot_identifier` or
`replicate_source_db` is provided) The allocated storage in gibibytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L57">property allowMajorVersionUpgrade</a>
</h3>

```typescript
public allowMajorVersionUpgrade: pulumi.Output<boolean | undefined>;
```


Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L65">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L69">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L75">property autoMinorVersionUpgrade</a>
</h3>

```typescript
public autoMinorVersionUpgrade: pulumi.Output<boolean | undefined>;
```


Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L79">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The AZ for the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L84">property backupRetentionPeriod</a>
</h3>

```typescript
public backupRetentionPeriod: pulumi.Output<number>;
```


The days to retain backups for. Must be
`1` or greater to be a source for a [Read Replica][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L90">property backupWindow</a>
</h3>

```typescript
public backupWindow: pulumi.Output<string>;
```


The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: "09:46-10:16". Must
not overlap with `maintenance_window`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L95">property caCertIdentifier</a>
</h3>

```typescript
public caCertIdentifier: pulumi.Output<string>;
```


Specifies the identifier of the CA certificate for the
DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L103">property characterSetName</a>
</h3>

```typescript
public characterSetName: pulumi.Output<string>;
```


The character set name to use for DB
encoding in Oracle instances. This can't be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L109">property copyTagsToSnapshot</a>
</h3>

```typescript
public copyTagsToSnapshot: pulumi.Output<boolean | undefined>;
```


On delete, copy all Instance
`tags` to the final snapshot (if `final_snapshot_identifier` is specified).
Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L119">property dbSubnetGroupName</a>
</h3>

```typescript
public dbSubnetGroupName: pulumi.Output<string>;
```


Name of [DB subnet group](/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it needs to be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additonal read replica contraints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L124">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
public enabledCloudwatchLogsExports: pulumi.Output<string[] | undefined>;
```


Name list of enable log type for exporting to cloudwatch logs. If omitted, any logs will not be exported to cloudwatch logs.
Either of the following is supported: `audit`, `error`, `general`, `slowquery`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L128">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The connection endpoint in `address:port` format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L137">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](/docs/providers/aws/r/rds_cluster.html)'s engine'.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L145">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](/docs/providers/aws/r/rds_cluster.html)'s engine version'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L150">property finalSnapshotIdentifier</a>
</h3>

```typescript
public finalSnapshotIdentifier: pulumi.Output<string | undefined>;
```


The name of your final DB snapshot
when this DB instance is deleted. If omitted, no final snapshot will be made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L155">property hostedZoneId</a>
</h3>

```typescript
public hostedZoneId: pulumi.Output<string>;
```


The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L161">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
public iamDatabaseAuthenticationEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L166">property identifier</a>
</h3>

```typescript
public identifier: pulumi.Output<string>;
```


The name of the RDS instance,
if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L171">property identifierPrefix</a>
</h3>

```typescript
public identifierPrefix: pulumi.Output<string>;
```


Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L175">property instanceClass</a>
</h3>

```typescript
public instanceClass: pulumi.Output<string>;
```


The instance type of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L180">property iops</a>
</h3>

```typescript
public iops: pulumi.Output<number | undefined>;
```


The amount of provisioned IOPS. Setting this implies a
storage_type of "io1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L185">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L190">property licenseModel</a>
</h3>

```typescript
public licenseModel: pulumi.Output<string>;
```


(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L198">property maintenanceWindow</a>
</h3>

```typescript
public maintenanceWindow: pulumi.Output<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00". See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L205">property monitoringInterval</a>
</h3>

```typescript
public monitoringInterval: pulumi.Output<number | undefined>;
```


The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L213">property monitoringRoleArn</a>
</h3>

```typescript
public monitoringRoleArn: pulumi.Output<string>;
```


The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L217">property multiAz</a>
</h3>

```typescript
public multiAz: pulumi.Output<boolean>;
```


Specifies if the RDS instance is multi-AZ

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L221">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L225">property optionGroupName</a>
</h3>

```typescript
public optionGroupName: pulumi.Output<string>;
```


Name of the DB option group to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L230">property parameterGroupName</a>
</h3>

```typescript
public parameterGroupName: pulumi.Output<string>;
```


Name of the DB parameter group to
associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L236">property password</a>
</h3>

```typescript
public password: pulumi.Output<string | undefined>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L240">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```


The port on which the DB accepts connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L245">property publiclyAccessible</a>
</h3>

```typescript
public publiclyAccessible: pulumi.Output<boolean | undefined>;
```


Bool to control if instance is publicly
accessible. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L246">property replicas</a>
</h3>

```typescript
public replicas: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L256">property replicateSourceDb</a>
</h3>

```typescript
public replicateSourceDb: pulumi.Output<string | undefined>;
```


Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L260">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The RDS Resource ID of this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L264">property s3Import</a>
</h3>

```typescript
public s3Import: pulumi.Output<{ ... } | undefined>;
```


Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L270">property securityGroupNames</a>
</h3>

```typescript
public securityGroupNames: pulumi.Output<string[] | undefined>;
```


List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L278">property skipFinalSnapshot</a>
</h3>

```typescript
public skipFinalSnapshot: pulumi.Output<boolean | undefined>;
```


Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L284">property snapshotIdentifier</a>
</h3>

```typescript
public snapshotIdentifier: pulumi.Output<string | undefined>;
```


Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you'd find in the
RDS console, e.g: rds:production-2015-06-26-06-05.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L288">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The RDS instance status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L295">property storageEncrypted</a>
</h3>

```typescript
public storageEncrypted: pulumi.Output<boolean | undefined>;
```


Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L302">property storageType</a>
</h3>

```typescript
public storageType: pulumi.Output<string>;
```


One of "standard" (magnetic), "gp2" (general
purpose SSD), or "io1" (provisioned IOPS SSD). The default is "io1" if `iops` is
specified, "standard" if not. Note that this behaviour is different from the AWS
web console, where the default is "gp2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L306">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L314">property timezone</a>
</h3>

```typescript
public timezone: pulumi.Output<string>;
```


Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L319">property username</a>
</h3>

```typescript
public username: pulumi.Output<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L324">property vpcSecurityGroupIds</a>
</h3>

```typescript
public vpcSecurityGroupIds: pulumi.Output<string[]>;
```


List of VPC security groups to
associate.

<h2 class="pdoc-module-header" id="OptionGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L15">class OptionGroup</a>
</h2>

Provides an RDS DB option group resource. Documentation of the available options for various RDS engines can be found at:
* [MariaDB Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Options.html)
* [Microsoft SQL Server Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)
* [MySQL Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.html)
* [Oracle Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L59">constructor</a>
</h3>

```typescript
new OptionGroup(name: string, args: OptionGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a OptionGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OptionGroupState): OptionGroup
```


Get an existing OptionGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L31">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the db option group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L35">property engineName</a>
</h3>

```typescript
public engineName: pulumi.Output<string>;
```


Specifies the name of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L39">property majorEngineVersion</a>
</h3>

```typescript
public majorEngineVersion: pulumi.Output<string>;
```


Specifies the major version of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The Name of the setting.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L47">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L55">property optionGroupDescription</a>
</h3>

```typescript
public optionGroupDescription: pulumi.Output<string>;
```


The description of the option group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L51">property options</a>
</h3>

```typescript
public options: pulumi.Output<{ ... }[] | undefined>;
```


A list of Options to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L59">property tags</a>
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

<h2 class="pdoc-module-header" id="ParameterGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L16">class ParameterGroup</a>
</h2>

Provides an RDS DB parameter group resource .Documentation of the available parameters for various RDS engines can be found at:
* [Aurora MySQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Reference.html)
* [Aurora PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html)
* [MariaDB Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Parameters.html)
* [Oracle Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.Oracle.html#USER_ModifyInstance.Oracle.sqlnet)
* [PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html#Appendix.PostgreSQL.CommonDBATasks.Parameters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L56">constructor</a>
</h3>

```typescript
new ParameterGroup(name: string, args: ParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ParameterGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L25">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L32">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the db parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L36">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the DB parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L40">property family</a>
</h3>

```typescript
public family: pulumi.Output<string>;
```


The family of the DB parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L48">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L52">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[] | undefined>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L56">property tags</a>
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

<h2 class="pdoc-module-header" id="SecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L14">class SecurityGroup</a>
</h2>

Provides an RDS security group resource. This is only for DB instances in the
EC2-Classic Platform. For instances inside a VPC, use the
[`aws_db_instance.vpc_security_group_ids`](/docs/providers/aws/r/db_instance.html#vpc_security_group_ids)
attribute instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L46">constructor</a>
</h3>

```typescript
new SecurityGroup(name: string, args: SecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecurityGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The arn of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the DB security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L38">property ingress</a>
</h3>

```typescript
public ingress: pulumi.Output<{ ... }[]>;
```


A list of ingress rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L46">property tags</a>
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

<h2 class="pdoc-module-header" id="Snapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L9">class Snapshot</a>
</h2>

Creates a Snapshot of an DB Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L91">constructor</a>
</h3>

```typescript
new Snapshot(name: string, args: SnapshotArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Snapshot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SnapshotState): Snapshot
```


Get an existing Snapshot resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L25">property allocatedStorage</a>
</h3>

```typescript
public allocatedStorage: pulumi.Output<number>;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L29">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L33">property dbInstanceIdentifier</a>
</h3>

```typescript
public dbInstanceIdentifier: pulumi.Output<string>;
```


The DB Instance Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L37">property dbSnapshotArn</a>
</h3>

```typescript
public dbSnapshotArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L41">property dbSnapshotIdentifier</a>
</h3>

```typescript
public dbSnapshotIdentifier: pulumi.Output<string>;
```


The Identifier for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L45">property encrypted</a>
</h3>

```typescript
public encrypted: pulumi.Output<boolean>;
```


Specifies whether the DB snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L49">property engine</a>
</h3>

```typescript
public engine: pulumi.Output<string>;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L53">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


Specifies the version of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L57">property iops</a>
</h3>

```typescript
public iops: pulumi.Output<number>;
```


Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L61">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L65">property licenseModel</a>
</h3>

```typescript
public licenseModel: pulumi.Output<string>;
```


License model information for the restored DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L69">property optionGroupName</a>
</h3>

```typescript
public optionGroupName: pulumi.Output<string>;
```


Provides the option group name for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L70">property port</a>
</h3>

```typescript
public port: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L71">property snapshotType</a>
</h3>

```typescript
public snapshotType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L75">property sourceDbSnapshotIdentifier</a>
</h3>

```typescript
public sourceDbSnapshotIdentifier: pulumi.Output<string>;
```


The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L79">property sourceRegion</a>
</h3>

```typescript
public sourceRegion: pulumi.Output<string>;
```


The region that the DB snapshot was created in or copied from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L83">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


Specifies the status of this DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L87">property storageType</a>
</h3>

```typescript
public storageType: pulumi.Output<string>;
```


Specifies the storage type associated with DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L91">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


Specifies the storage type associated with DB snapshot.

<h2 class="pdoc-module-header" id="SubnetGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L11">class SubnetGroup</a>
</h2>

Provides an RDS DB subnet group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L47">constructor</a>
</h3>

```typescript
new SubnetGroup(name: string, args: SubnetGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubnetGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the db subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the DB subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DB subnet group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L39">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L43">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


A list of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L47">property tags</a>
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

<h2 class="pdoc-module-header" id="getCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L9">function getCluster</a>
</h2>

```typescript
getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult>
```


Provides information about a RDS cluster.

<h2 class="pdoc-module-header" id="getInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L9">function getInstance</a>
</h2>

```typescript
getInstance(args: GetInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceResult>
```


Use this data source to get information about an RDS instance

<h2 class="pdoc-module-header" id="getSnapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L11">function getSnapshot</a>
</h2>

```typescript
getSnapshot(args?: GetSnapshotArgs, opts?: pulumi.InvokeOptions): Promise<GetSnapshotResult>
```


Use this data source to get information about a DB Snapshot for use when provisioning DB instances

~> **NOTE:** This data source does not apply to snapshots created on Aurora DB clusters.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L440">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L446">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L451">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of EC2 Availability Zones that
instances in the DB cluster can be created in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L455">property backtrackWindow</a>
</h3>

```typescript
backtrackWindow?: pulumi.Input<number>;
```


The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L459">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L463">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L467">property clusterIdentifierPrefix</a>
</h3>

```typescript
clusterIdentifierPrefix?: pulumi.Input<string>;
```


Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L471">property clusterMembers</a>
</h3>

```typescript
clusterMembers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of RDS Instances that are a part of this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L475">property databaseName</a>
</h3>

```typescript
databaseName?: pulumi.Input<string>;
```


Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L479">property dbClusterParameterGroupName</a>
</h3>

```typescript
dbClusterParameterGroupName?: pulumi.Input<string>;
```


A cluster parameter group to associate with the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L483">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws_rds_cluster_instance`](/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L488">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
```


List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L492">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L496">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L502">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L506">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L510">property iamRoles</a>
</h3>

```typescript
iamRoles?: pulumi.Input<pulumi.Input<string>[]>;
```


A List of ARNs for the IAM roles to associate to the RDS Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L514">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L519">property masterPassword</a>
</h3>

```typescript
masterPassword?: pulumi.Input<string>;
```


Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L523">property masterUsername</a>
</h3>

```typescript
masterUsername?: pulumi.Input<string>;
```


Username for the master DB user. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L527">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L532">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L536">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L540">property replicationSourceIdentifier</a>
</h3>

```typescript
replicationSourceIdentifier?: pulumi.Input<string>;
```


ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L541">property s3Import</a>
</h3>

```typescript
s3Import?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L545">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L549">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L553">property sourceRegion</a>
</h3>

```typescript
sourceRegion?: pulumi.Input<string>;
```


The source region for an encrypted replica DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L557">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB cluster is encrypted. The default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L561">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L566">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to associate
with the Cluster

<h2 class="pdoc-module-header" id="ClusterInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L390">interface ClusterInstanceArgs</a>
</h2>

The set of arguments for constructing a ClusterInstance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L395">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L399">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L403">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) about the details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L407">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier: pulumi.Input<string>;
```


The identifier of the [`aws_rds_cluster`](/docs/providers/aws/r/rds_cluster.html) in which to launch this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L411">property dbParameterGroupName</a>
</h3>

```typescript
dbParameterGroupName?: pulumi.Input<string>;
```


The name of the DB parameter group to associate with this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L415">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` of the attached [`aws_rds_cluster`](/docs/providers/aws/r/rds_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L422">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for the RDS instance. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L426">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L430">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The indentifier for the RDS instance, if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L434">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L453">property instanceClass</a>
</h3>

```typescript
instanceClass: pulumi.Input<string>;
```


The instance class to use. For details on CPU
and memory, see [Scaling Aurora DB Instances][4]. Aurora currently
supports the below instance classes.
- db.t2.small
- db.t2.medium
- db.r3.large
- db.r3.xlarge
- db.r3.2xlarge
- db.r3.4xlarge
- db.r3.8xlarge
- db.r4.large
- db.r4.xlarge
- db.r4.2xlarge
- db.r4.4xlarge
- db.r4.8xlarge
- db.r4.16xlarge

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L457">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval?: pulumi.Input<number>;
```


The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L463">property monitoringRoleArn</a>
</h3>

```typescript
monitoringRoleArn?: pulumi.Input<string>;
```


The ARN for the IAM role that permits RDS to send
enhanced monitoring metrics to CloudWatch Logs. You can find more information on the [AWS Documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L467">property performanceInsightsEnabled</a>
</h3>

```typescript
performanceInsightsEnabled?: pulumi.Input<boolean>;
```


Specifies whether Performance Insights is enabled or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L471">property performanceInsightsKmsKeyId</a>
</h3>

```typescript
performanceInsightsKmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L476">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled.
Eg: "04:00-09:00"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L481">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L485">property promotionTier</a>
</h3>

```typescript
promotionTier?: pulumi.Input<number>;
```


Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L491">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly accessible.
Default `false`. See the documentation on [Creating DB Instances][6] for more
details on controlling this property.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L495">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the instance.

<h2 class="pdoc-module-header" id="ClusterInstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L251">interface ClusterInstanceState</a>
</h2>

Input properties used for looking up and filtering ClusterInstance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L256">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L260">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of cluster instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L264">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L268">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) about the details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L272">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The identifier of the [`aws_rds_cluster`](/docs/providers/aws/r/rds_cluster.html) in which to launch this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L276">property dbParameterGroupName</a>
</h3>

```typescript
dbParameterGroupName?: pulumi.Input<string>;
```


The name of the DB parameter group to associate with this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L280">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` of the attached [`aws_rds_cluster`](/docs/providers/aws/r/rds_cluster.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L284">property dbiResourceId</a>
</h3>

```typescript
dbiResourceId?: pulumi.Input<string>;
```


The region-unique, immutable identifier for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L288">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The DNS address for this instance. May not be writable

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L295">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for the RDS instance. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L299">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L303">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The indentifier for the RDS instance, if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L307">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L326">property instanceClass</a>
</h3>

```typescript
instanceClass?: pulumi.Input<string>;
```


The instance class to use. For details on CPU
and memory, see [Scaling Aurora DB Instances][4]. Aurora currently
supports the below instance classes.
- db.t2.small
- db.t2.medium
- db.r3.large
- db.r3.xlarge
- db.r3.2xlarge
- db.r3.4xlarge
- db.r3.8xlarge
- db.r4.large
- db.r4.xlarge
- db.r4.2xlarge
- db.r4.4xlarge
- db.r4.8xlarge
- db.r4.16xlarge

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L330">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key if one is set to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L334">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval?: pulumi.Input<number>;
```


The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L340">property monitoringRoleArn</a>
</h3>

```typescript
monitoringRoleArn?: pulumi.Input<string>;
```


The ARN for the IAM role that permits RDS to send
enhanced monitoring metrics to CloudWatch Logs. You can find more information on the [AWS Documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L344">property performanceInsightsEnabled</a>
</h3>

```typescript
performanceInsightsEnabled?: pulumi.Input<boolean>;
```


Specifies whether Performance Insights is enabled or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L348">property performanceInsightsKmsKeyId</a>
</h3>

```typescript
performanceInsightsKmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS key to encrypt Performance Insights data. When specifying `performance_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L352">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The database port

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L357">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled.
Eg: "04:00-09:00"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L362">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L366">property promotionTier</a>
</h3>

```typescript
promotionTier?: pulumi.Input<number>;
```


Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L372">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly accessible.
Default `false`. See the documentation on [Creating DB Instances][6] for more
details on controlling this property.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L376">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB cluster is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L380">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterInstance.ts#L384">property writer</a>
</h3>

```typescript
writer?: pulumi.Input<boolean>;
```


Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.

<h2 class="pdoc-module-header" id="ClusterParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L128">interface ClusterParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ClusterParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L132">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB cluster parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L136">property family</a>
</h3>

```typescript
family: pulumi.Input<string>;
```


The family of the DB cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L144">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L148">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-cluster-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L152">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ClusterParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L94">interface ClusterParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ClusterParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L98">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the db cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L102">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB cluster parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L106">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The family of the DB cluster parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L114">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L118">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-cluster-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/clusterParameterGroup.ts#L122">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L287">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L293">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L297">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L302">property availabilityZones</a>
</h3>

```typescript
availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of EC2 Availability Zones that
instances in the DB cluster can be created in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L306">property backtrackWindow</a>
</h3>

```typescript
backtrackWindow?: pulumi.Input<number>;
```


The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L310">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L314">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier?: pulumi.Input<string>;
```


The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L318">property clusterIdentifierPrefix</a>
</h3>

```typescript
clusterIdentifierPrefix?: pulumi.Input<string>;
```


Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L322">property clusterMembers</a>
</h3>

```typescript
clusterMembers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of RDS Instances that are a part of this cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L326">property clusterResourceId</a>
</h3>

```typescript
clusterResourceId?: pulumi.Input<string>;
```


The RDS Cluster Resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L330">property databaseName</a>
</h3>

```typescript
databaseName?: pulumi.Input<string>;
```


Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L334">property dbClusterParameterGroupName</a>
</h3>

```typescript
dbClusterParameterGroupName?: pulumi.Input<string>;
```


A cluster parameter group to associate with the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L338">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws_rds_cluster_instance`](/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L343">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
```


List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L347">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The DNS address of the RDS instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L351">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L355">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L361">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L365">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId?: pulumi.Input<string>;
```


The Route53 Hosted Zone ID of the endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L369">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L373">property iamRoles</a>
</h3>

```typescript
iamRoles?: pulumi.Input<pulumi.Input<string>[]>;
```


A List of ARNs for the IAM roles to associate to the RDS Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L377">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L382">property masterPassword</a>
</h3>

```typescript
masterPassword?: pulumi.Input<string>;
```


Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L386">property masterUsername</a>
</h3>

```typescript
masterUsername?: pulumi.Input<string>;
```


Username for the master DB user. Please refer to the [RDS Naming Constraints][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L390">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L395">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow?: pulumi.Input<string>;
```


The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L399">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow?: pulumi.Input<string>;
```


The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L404">property readerEndpoint</a>
</h3>

```typescript
readerEndpoint?: pulumi.Input<string>;
```


A read-only endpoint for the Aurora cluster, automatically
load-balanced across replicas

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L408">property replicationSourceIdentifier</a>
</h3>

```typescript
replicationSourceIdentifier?: pulumi.Input<string>;
```


ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L409">property s3Import</a>
</h3>

```typescript
s3Import?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L413">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L417">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L421">property sourceRegion</a>
</h3>

```typescript
sourceRegion?: pulumi.Input<string>;
```


The source region for an encrypted replica DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L425">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB cluster is encrypted. The default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L429">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the DB cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/cluster.ts#L434">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to associate
with the Cluster

<h2 class="pdoc-module-header" id="EventSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L144">interface EventSubscriptionArgs</a>
</h2>

The set of arguments for constructing a EventSubscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L148">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable the subscription. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L152">property eventCategories</a>
</h3>

```typescript
eventCategories?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB event subscription. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L160">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The name of the DB event subscription. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L164">property snsTopic</a>
</h3>

```typescript
snsTopic: pulumi.Input<string>;
```


The SNS topic to send events to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L168">property sourceIds</a>
</h3>

```typescript
sourceIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L172">property sourceType</a>
</h3>

```typescript
sourceType?: pulumi.Input<string>;
```


The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L176">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventSubscriptionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L104">interface EventSubscriptionState</a>
</h2>

Input properties used for looking up and filtering EventSubscription resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L105">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L106">property customerAwsId</a>
</h3>

```typescript
customerAwsId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L110">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


A boolean flag to enable/disable the subscription. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L114">property eventCategories</a>
</h3>

```typescript
eventCategories?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB event subscription. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L122">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The name of the DB event subscription. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L126">property snsTopic</a>
</h3>

```typescript
snsTopic?: pulumi.Input<string>;
```


The SNS topic to send events to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L130">property sourceIds</a>
</h3>

```typescript
sourceIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L134">property sourceType</a>
</h3>

```typescript
sourceType?: pulumi.Input<string>;
```


The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/eventSubscription.ts#L138">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="GetClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L19">interface GetClusterArgs</a>
</h2>

A collection of arguments for invoking getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L23">property clusterIdentifier</a>
</h3>

```typescript
clusterIdentifier: string;
```


The cluster identifier of the RDS cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L24">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L30">interface GetClusterResult</a>
</h2>

A collection of values returned by getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L31">property arn</a>
</h3>

```typescript
arn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L32">property availabilityZones</a>
</h3>

```typescript
availabilityZones: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L33">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L34">property clusterMembers</a>
</h3>

```typescript
clusterMembers: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L35">property clusterResourceId</a>
</h3>

```typescript
clusterResourceId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L36">property databaseName</a>
</h3>

```typescript
databaseName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L37">property dbClusterParameterGroupName</a>
</h3>

```typescript
dbClusterParameterGroupName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L38">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L39">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L40">property endpoint</a>
</h3>

```typescript
endpoint: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L41">property engine</a>
</h3>

```typescript
engine: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L42">property engineVersion</a>
</h3>

```typescript
engineVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L43">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L44">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L45">property iamRoles</a>
</h3>

```typescript
iamRoles: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L59">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L46">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L47">property masterUsername</a>
</h3>

```typescript
masterUsername: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L48">property port</a>
</h3>

```typescript
port: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L49">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L50">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L51">property readerEndpoint</a>
</h3>

```typescript
readerEndpoint: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L52">property replicationSourceIdentifier</a>
</h3>

```typescript
replicationSourceIdentifier: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L53">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L54">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getCluster.ts#L55">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds: string[];
```

<h2 class="pdoc-module-header" id="GetInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L18">interface GetInstanceArgs</a>
</h2>

A collection of arguments for invoking getInstance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L22">property dbInstanceIdentifier</a>
</h3>

```typescript
dbInstanceIdentifier: string;
```


The name of the RDS instance

<h2 class="pdoc-module-header" id="GetInstanceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L28">interface GetInstanceResult</a>
</h2>

A collection of values returned by getInstance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L32">property address</a>
</h3>

```typescript
address: string;
```


The hostname of the RDS instance. See also `endpoint` and `port`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L36">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage: number;
```


Specifies the allocated storage size specified in gigabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L40">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade: boolean;
```


Indicates that minor version patches are applied automatically.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L44">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```


Specifies the name of the Availability Zone the DB instance is located in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L48">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod: number;
```


Specifies the number of days for which automatic DB snapshots are retained.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L52">property caCertIdentifier</a>
</h3>

```typescript
caCertIdentifier: string;
```


Specifies the identifier of the CA certificate for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L56">property dbClusterIdentifier</a>
</h3>

```typescript
dbClusterIdentifier: string;
```


If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L60">property dbInstanceArn</a>
</h3>

```typescript
dbInstanceArn: string;
```


The Amazon Resource Name (ARN) for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L64">property dbInstanceClass</a>
</h3>

```typescript
dbInstanceClass: string;
```


Contains the name of the compute and memory capacity class of the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L68">property dbInstancePort</a>
</h3>

```typescript
dbInstancePort: number;
```


Specifies the port that the DB instance listens on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L72">property dbName</a>
</h3>

```typescript
dbName: string;
```


Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L76">property dbParameterGroups</a>
</h3>

```typescript
dbParameterGroups: string[];
```


Provides the list of DB parameter groups applied to this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L80">property dbSecurityGroups</a>
</h3>

```typescript
dbSecurityGroups: string[];
```


Provides List of DB security groups associated to this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L84">property dbSubnetGroup</a>
</h3>

```typescript
dbSubnetGroup: string;
```


Specifies the name of the subnet group associated with the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L88">property endpoint</a>
</h3>

```typescript
endpoint: string;
```


The connection endpoint in `address:port` format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L92">property engine</a>
</h3>

```typescript
engine: string;
```


Provides the name of the database engine to be used for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L96">property engineVersion</a>
</h3>

```typescript
engineVersion: string;
```


Indicates the database engine version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L100">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId: string;
```


The canonical hosted zone ID of the DB instance (to be used in a Route 53 Alias record).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L172">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L104">property iops</a>
</h3>

```typescript
iops: number;
```


Specifies the Provisioned IOPS (I/O operations per second) value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L108">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```


If StorageEncrypted is true, the KMS key identifier for the encrypted DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L112">property licenseModel</a>
</h3>

```typescript
licenseModel: string;
```


License model information for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L116">property masterUsername</a>
</h3>

```typescript
masterUsername: string;
```


Contains the master username for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L120">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval: number;
```


The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L124">property monitoringRoleArn</a>
</h3>

```typescript
monitoringRoleArn: string;
```


The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to CloudWatch Logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L128">property multiAz</a>
</h3>

```typescript
multiAz: boolean;
```


Specifies if the DB instance is a Multi-AZ deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L132">property optionGroupMemberships</a>
</h3>

```typescript
optionGroupMemberships: string[];
```


Provides the list of option group memberships for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L136">property port</a>
</h3>

```typescript
port: number;
```


The database port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L140">property preferredBackupWindow</a>
</h3>

```typescript
preferredBackupWindow: string;
```


Specifies the daily time range during which automated backups are created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L144">property preferredMaintenanceWindow</a>
</h3>

```typescript
preferredMaintenanceWindow: string;
```


Specifies the weekly time range during which system maintenance can occur in UTC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L148">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible: boolean;
```


Specifies the accessibility options for the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L152">property replicateSourceDb</a>
</h3>

```typescript
replicateSourceDb: string;
```


The identifier of the source DB that this is a replica of.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L156">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted: boolean;
```


Specifies whether the DB instance is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L160">property storageType</a>
</h3>

```typescript
storageType: string;
```


Specifies the storage type associated with DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L164">property timezone</a>
</h3>

```typescript
timezone: string;
```


The time zone of the DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getInstance.ts#L168">property vpcSecurityGroups</a>
</h3>

```typescript
vpcSecurityGroups: string[];
```


Provides a list of VPC security group elements that the DB instance belongs to.

<h2 class="pdoc-module-header" id="GetSnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L26">interface GetSnapshotArgs</a>
</h2>

A collection of arguments for invoking getSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L30">property dbInstanceIdentifier</a>
</h3>

```typescript
dbInstanceIdentifier?: string;
```


Returns the list of snapshots created by the specific db_instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L34">property dbSnapshotIdentifier</a>
</h3>

```typescript
dbSnapshotIdentifier?: string;
```


Returns information on a specific snapshot_id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L39">property includePublic</a>
</h3>

```typescript
includePublic?: boolean;
```


Set this value to true to include manual DB snapshots that are public and can be
copied or restored by any AWS account, otherwise set this value to false. The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L45">property includeShared</a>
</h3>

```typescript
includeShared?: boolean;
```


Set this value to true to include shared manual DB snapshots from other
AWS accounts that this AWS account has been given permission to copy or restore, otherwise set this value to false.
The default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L50">property mostRecent</a>
</h3>

```typescript
mostRecent?: boolean;
```


If more than one result is returned, use the most
recent Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L56">property snapshotType</a>
</h3>

```typescript
snapshotType?: string;
```


The type of snapshots to be returned. If you don't specify a SnapshotType
value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not
included in the returned results by default. Possible values are, `automated`, `manual`, `shared` and `public`.

<h2 class="pdoc-module-header" id="GetSnapshotResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L62">interface GetSnapshotResult</a>
</h2>

A collection of values returned by getSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L66">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage: number;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L70">property availabilityZone</a>
</h3>

```typescript
availabilityZone: string;
```


Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L74">property dbSnapshotArn</a>
</h3>

```typescript
dbSnapshotArn: string;
```


The Amazon Resource Name (ARN) for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L78">property encrypted</a>
</h3>

```typescript
encrypted: boolean;
```


Specifies whether the DB snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L82">property engine</a>
</h3>

```typescript
engine: string;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L86">property engineVersion</a>
</h3>

```typescript
engineVersion: string;
```


Specifies the version of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L131">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L90">property iops</a>
</h3>

```typescript
iops: number;
```


Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L94">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L98">property licenseModel</a>
</h3>

```typescript
licenseModel: string;
```


License model information for the restored DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L102">property optionGroupName</a>
</h3>

```typescript
optionGroupName: string;
```


Provides the option group name for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L103">property port</a>
</h3>

```typescript
port: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L107">property snapshotCreateTime</a>
</h3>

```typescript
snapshotCreateTime: string;
```


Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L111">property sourceDbSnapshotIdentifier</a>
</h3>

```typescript
sourceDbSnapshotIdentifier: string;
```


The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L115">property sourceRegion</a>
</h3>

```typescript
sourceRegion: string;
```


The region that the DB snapshot was created in or copied from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L119">property status</a>
</h3>

```typescript
status: string;
```


Specifies the status of this DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L123">property storageType</a>
</h3>

```typescript
storageType: string;
```


Specifies the storage type associated with DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/getSnapshot.ts#L127">property vpcId</a>
</h3>

```typescript
vpcId: string;
```


Specifies the ID of the VPC associated with the DB snapshot.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L739">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L744">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage?: pulumi.Input<number>;
```


(Required unless a `snapshot_identifier` or
`replicate_source_db` is provided) The allocated storage in gibibytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L750">property allowMajorVersionUpgrade</a>
</h3>

```typescript
allowMajorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L758">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L764">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L768">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The AZ for the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L773">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Must be
`1` or greater to be a source for a [Read Replica][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L779">property backupWindow</a>
</h3>

```typescript
backupWindow?: pulumi.Input<string>;
```


The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: "09:46-10:16". Must
not overlap with `maintenance_window`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L787">property characterSetName</a>
</h3>

```typescript
characterSetName?: pulumi.Input<string>;
```


The character set name to use for DB
encoding in Oracle instances. This can't be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L793">property copyTagsToSnapshot</a>
</h3>

```typescript
copyTagsToSnapshot?: pulumi.Input<boolean>;
```


On delete, copy all Instance
`tags` to the final snapshot (if `final_snapshot_identifier` is specified).
Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L803">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


Name of [DB subnet group](/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it needs to be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additonal read replica contraints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L808">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
```


Name list of enable log type for exporting to cloudwatch logs. If omitted, any logs will not be exported to cloudwatch logs.
Either of the following is supported: `audit`, `error`, `general`, `slowquery`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L817">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](/docs/providers/aws/r/rds_cluster.html)'s engine'.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L825">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](/docs/providers/aws/r/rds_cluster.html)'s engine version'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L830">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final DB snapshot
when this DB instance is deleted. If omitted, no final snapshot will be made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L836">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L841">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The name of the RDS instance,
if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L846">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L850">property instanceClass</a>
</h3>

```typescript
instanceClass: pulumi.Input<string>;
```


The instance type of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L855">property iops</a>
</h3>

```typescript
iops?: pulumi.Input<number>;
```


The amount of provisioned IOPS. Setting this implies a
storage_type of "io1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L860">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L865">property licenseModel</a>
</h3>

```typescript
licenseModel?: pulumi.Input<string>;
```


(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L873">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00". See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L880">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval?: pulumi.Input<number>;
```


The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L888">property monitoringRoleArn</a>
</h3>

```typescript
monitoringRoleArn?: pulumi.Input<string>;
```


The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L892">property multiAz</a>
</h3>

```typescript
multiAz?: pulumi.Input<boolean>;
```


Specifies if the RDS instance is multi-AZ

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L896">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L900">property optionGroupName</a>
</h3>

```typescript
optionGroupName?: pulumi.Input<string>;
```


Name of the DB option group to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L905">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the DB parameter group to
associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L911">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L915">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L920">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly
accessible. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L930">property replicateSourceDb</a>
</h3>

```typescript
replicateSourceDb?: pulumi.Input<string>;
```


Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L934">property s3Import</a>
</h3>

```typescript
s3Import?: pulumi.Input<{ ... }>;
```


Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L940">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L948">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L954">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you'd find in the
RDS console, e.g: rds:production-2015-06-26-06-05.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L961">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L968">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


One of "standard" (magnetic), "gp2" (general
purpose SSD), or "io1" (provisioned IOPS SSD). The default is "io1" if `iops` is
specified, "standard" if not. Note that this behaviour is different from the AWS
web console, where the default is "gp2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L972">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L980">property timezone</a>
</h3>

```typescript
timezone?: pulumi.Input<string>;
```


Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L985">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L990">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to
associate.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L451">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L455">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The hostname of the RDS instance. See also `endpoint` and `port`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L460">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage?: pulumi.Input<number>;
```


(Required unless a `snapshot_identifier` or
`replicate_source_db` is provided) The allocated storage in gibibytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L466">property allowMajorVersionUpgrade</a>
</h3>

```typescript
allowMajorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that major version
upgrades are allowed. Changing this parameter does not result in an outage and
the change is asynchronously applied as soon as possible.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L474">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more
information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L478">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L484">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Indicates that minor engine upgrades
will be applied automatically to the DB instance during the maintenance window.
Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L488">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The AZ for the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L493">property backupRetentionPeriod</a>
</h3>

```typescript
backupRetentionPeriod?: pulumi.Input<number>;
```


The days to retain backups for. Must be
`1` or greater to be a source for a [Read Replica][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L499">property backupWindow</a>
</h3>

```typescript
backupWindow?: pulumi.Input<string>;
```


The daily time range (in UTC) during which
automated backups are created if they are enabled. Example: "09:46-10:16". Must
not overlap with `maintenance_window`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L504">property caCertIdentifier</a>
</h3>

```typescript
caCertIdentifier?: pulumi.Input<string>;
```


Specifies the identifier of the CA certificate for the
DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L512">property characterSetName</a>
</h3>

```typescript
characterSetName?: pulumi.Input<string>;
```


The character set name to use for DB
encoding in Oracle instances. This can't be changed. See [Oracle Character Sets
Supported in Amazon
RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L518">property copyTagsToSnapshot</a>
</h3>

```typescript
copyTagsToSnapshot?: pulumi.Input<boolean>;
```


On delete, copy all Instance
`tags` to the final snapshot (if `final_snapshot_identifier` is specified).
Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L528">property dbSubnetGroupName</a>
</h3>

```typescript
dbSubnetGroupName?: pulumi.Input<string>;
```


Name of [DB subnet group](/docs/providers/aws/r/db_subnet_group.html). DB instance will
be created in the VPC associated with the DB subnet group. If unspecified, will
be created in the `default` VPC, or in EC2 Classic, if available. When working
with read replicas, it needs to be specified only if the source database
specifies an instance in another AWS Region. See [DBSubnetGroupName in API
action CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)
for additonal read replica contraints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L533">property enabledCloudwatchLogsExports</a>
</h3>

```typescript
enabledCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
```


Name list of enable log type for exporting to cloudwatch logs. If omitted, any logs will not be exported to cloudwatch logs.
Either of the following is supported: `audit`, `error`, `general`, `slowquery`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L537">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The connection endpoint in `address:port` format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L546">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) The database engine to use.  For supported values, see the Engine parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine must match the [DB cluster](/docs/providers/aws/r/rds_cluster.html)'s engine'.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L554">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The engine version to use. If `auto_minor_version_upgrade`
is enabled, you can provide a prefix of the version such as `5.7` (for `5.7.10`) and
this attribute will ignore differences in the patch version automatically (e.g. `5.7.17`).
For supported values, see the EngineVersion parameter in [API action CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html).
Note that for Amazon Aurora instances the engine version must match the [DB cluster](/docs/providers/aws/r/rds_cluster.html)'s engine version'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L559">property finalSnapshotIdentifier</a>
</h3>

```typescript
finalSnapshotIdentifier?: pulumi.Input<string>;
```


The name of your final DB snapshot
when this DB instance is deleted. If omitted, no final snapshot will be made.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L564">property hostedZoneId</a>
</h3>

```typescript
hostedZoneId?: pulumi.Input<string>;
```


The canonical hosted zone ID of the DB instance (to be used
in a Route 53 Alias record).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L570">property iamDatabaseAuthenticationEnabled</a>
</h3>

```typescript
iamDatabaseAuthenticationEnabled?: pulumi.Input<boolean>;
```


Specifies whether or
mappings of AWS Identity and Access Management (IAM) accounts to database
accounts is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L575">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


The name of the RDS instance,
if omitted, Terraform will assign a random, unique identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L580">property identifierPrefix</a>
</h3>

```typescript
identifierPrefix?: pulumi.Input<string>;
```


Creates a unique
identifier beginning with the specified prefix. Conflicts with `identifer`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L584">property instanceClass</a>
</h3>

```typescript
instanceClass?: pulumi.Input<string>;
```


The instance type of the RDS instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L589">property iops</a>
</h3>

```typescript
iops?: pulumi.Input<number>;
```


The amount of provisioned IOPS. Setting this implies a
storage_type of "io1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L594">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key. If creating an
encrypted replica, set this to the destination KMS ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L599">property licenseModel</a>
</h3>

```typescript
licenseModel?: pulumi.Input<string>;
```


(Optional, but required for some DB engines, i.e. Oracle
SE1) License model information for this DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L607">property maintenanceWindow</a>
</h3>

```typescript
maintenanceWindow?: pulumi.Input<string>;
```


The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00". See [RDS
Maintenance Window
docs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L614">property monitoringInterval</a>
</h3>

```typescript
monitoringInterval?: pulumi.Input<number>;
```


The interval, in seconds, between points
when Enhanced Monitoring metrics are collected for the DB instance. To disable
collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid
Values: 0, 1, 5, 10, 15, 30, 60.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L622">property monitoringRoleArn</a>
</h3>

```typescript
monitoringRoleArn?: pulumi.Input<string>;
```


The ARN for the IAM role that permits RDS
to send enhanced monitoring metrics to CloudWatch Logs. You can find more
information on the [AWS
Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L626">property multiAz</a>
</h3>

```typescript
multiAz?: pulumi.Input<boolean>;
```


Specifies if the RDS instance is multi-AZ

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L630">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance. Note that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](http://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) for more details on what applies for those engines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L634">property optionGroupName</a>
</h3>

```typescript
optionGroupName?: pulumi.Input<string>;
```


Name of the DB option group to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L639">property parameterGroupName</a>
</h3>

```typescript
parameterGroupName?: pulumi.Input<string>;
```


Name of the DB parameter group to
associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L645">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Password for the master DB user. Note that this may show up in
logs, and it will be stored in the state file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L649">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port on which the DB accepts connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L654">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Bool to control if instance is publicly
accessible. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L655">property replicas</a>
</h3>

```typescript
replicas?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L665">property replicateSourceDb</a>
</h3>

```typescript
replicateSourceDb?: pulumi.Input<string>;
```


Specifies that this resource is a Replicate
database, and to use this value as the source database. This correlates to the
`identifier` of another Amazon RDS Database to replicate. Note that if you are
creating a cross-region replica of an encrypted database you will also need to
specify a `kms_key_id`. See [DB Instance Replication][1] and [Working with
PostgreSQL and MySQL Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
for more information on using Replication.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L669">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The RDS Resource ID of this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L673">property s3Import</a>
</h3>

```typescript
s3Import?: pulumi.Input<{ ... }>;
```


Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L679">property securityGroupNames</a>
</h3>

```typescript
securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
```


List of DB Security Groups to
associate. Only used for [DB Instances on the _EC2-Classic_
Platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.FindDefaultVPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L687">property skipFinalSnapshot</a>
</h3>

```typescript
skipFinalSnapshot?: pulumi.Input<boolean>;
```


Determines whether a final DB snapshot is
created before the DB instance is deleted. If true is specified, no DBSnapshot
is created. If false is specified, a DB snapshot is created before the DB
instance is deleted, using the value from `final_snapshot_identifier`. Default
is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L693">property snapshotIdentifier</a>
</h3>

```typescript
snapshotIdentifier?: pulumi.Input<string>;
```


Specifies whether or not to create this
database from a snapshot. This correlates to the snapshot ID you'd find in the
RDS console, e.g: rds:production-2015-06-26-06-05.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L697">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The RDS instance status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L704">property storageEncrypted</a>
</h3>

```typescript
storageEncrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB instance is
encrypted. Note that if you are creating a cross-region read replica this field
is ignored and you should instead declare `kms_key_id` with a valid ARN. The
default is `false` if not specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L711">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


One of "standard" (magnetic), "gp2" (general
purpose SSD), or "io1" (provisioned IOPS SSD). The default is "io1" if `iops` is
specified, "standard" if not. Note that this behaviour is different from the AWS
web console, where the default is "gp2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L715">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L723">property timezone</a>
</h3>

```typescript
timezone?: pulumi.Input<string>;
```


Time zone of the DB instance. `timezone` is currently
only supported by Microsoft SQL Server. The `timezone` can only be set on
creation. See [MSSQL User
Guide](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L728">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


(Required unless a `snapshot_identifier` or `replicate_source_db`
is provided) Username for the master DB user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/instance.ts#L733">property vpcSecurityGroupIds</a>
</h3>

```typescript
vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


List of VPC security groups to
associate.

<h2 class="pdoc-module-header" id="OptionGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L143">interface OptionGroupArgs</a>
</h2>

The set of arguments for constructing a OptionGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L147">property engineName</a>
</h3>

```typescript
engineName: pulumi.Input<string>;
```


Specifies the name of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L151">property majorEngineVersion</a>
</h3>

```typescript
majorEngineVersion: pulumi.Input<string>;
```


Specifies the major version of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L155">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the setting.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L159">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L167">property optionGroupDescription</a>
</h3>

```typescript
optionGroupDescription?: pulumi.Input<string>;
```


The description of the option group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L163">property options</a>
</h3>

```typescript
options?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Options to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L171">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="OptionGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L105">interface OptionGroupState</a>
</h2>

Input properties used for looking up and filtering OptionGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L109">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the db option group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L113">property engineName</a>
</h3>

```typescript
engineName?: pulumi.Input<string>;
```


Specifies the name of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L117">property majorEngineVersion</a>
</h3>

```typescript
majorEngineVersion?: pulumi.Input<string>;
```


Specifies the major version of the engine that this option group should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the setting.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L125">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L133">property optionGroupDescription</a>
</h3>

```typescript
optionGroupDescription?: pulumi.Input<string>;
```


The description of the option group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L129">property options</a>
</h3>

```typescript
options?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Options to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/optionGroup.ts#L137">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ParameterGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L131">interface ParameterGroupArgs</a>
</h2>

The set of arguments for constructing a ParameterGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L135">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L139">property family</a>
</h3>

```typescript
family: pulumi.Input<string>;
```


The family of the DB parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L143">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L147">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L151">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L155">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ParameterGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L97">interface ParameterGroupState</a>
</h2>

Input properties used for looking up and filtering ParameterGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L101">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the db parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L105">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB parameter group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L109">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The family of the DB parameter group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L117">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L121">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) after initial creation of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/parameterGroup.ts#L125">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SecurityGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L109">interface SecurityGroupArgs</a>
</h2>

The set of arguments for constructing a SecurityGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L113">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L117">property ingress</a>
</h3>

```typescript
ingress: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of ingress rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L125">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SecurityGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L83">interface SecurityGroupState</a>
</h2>

Input properties used for looking up and filtering SecurityGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L87">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The arn of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L91">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB security group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L95">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of ingress rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/securityGroup.ts#L103">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L235">interface SnapshotArgs</a>
</h2>

The set of arguments for constructing a Snapshot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L239">property dbInstanceIdentifier</a>
</h3>

```typescript
dbInstanceIdentifier: pulumi.Input<string>;
```


The DB Instance Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L243">property dbSnapshotIdentifier</a>
</h3>

```typescript
dbSnapshotIdentifier: pulumi.Input<string>;
```


The Identifier for the snapshot.

<h2 class="pdoc-module-header" id="SnapshotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L159">interface SnapshotState</a>
</h2>

Input properties used for looking up and filtering Snapshot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L163">property allocatedStorage</a>
</h3>

```typescript
allocatedStorage?: pulumi.Input<number>;
```


Specifies the allocated storage size in gigabytes (GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L167">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L171">property dbInstanceIdentifier</a>
</h3>

```typescript
dbInstanceIdentifier?: pulumi.Input<string>;
```


The DB Instance Identifier from which to take the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L175">property dbSnapshotArn</a>
</h3>

```typescript
dbSnapshotArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L179">property dbSnapshotIdentifier</a>
</h3>

```typescript
dbSnapshotIdentifier?: pulumi.Input<string>;
```


The Identifier for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L183">property encrypted</a>
</h3>

```typescript
encrypted?: pulumi.Input<boolean>;
```


Specifies whether the DB snapshot is encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L187">property engine</a>
</h3>

```typescript
engine?: pulumi.Input<string>;
```


Specifies the name of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L191">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


Specifies the version of the database engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L195">property iops</a>
</h3>

```typescript
iops?: pulumi.Input<number>;
```


Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L199">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L203">property licenseModel</a>
</h3>

```typescript
licenseModel?: pulumi.Input<string>;
```


License model information for the restored DB instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L207">property optionGroupName</a>
</h3>

```typescript
optionGroupName?: pulumi.Input<string>;
```


Provides the option group name for the DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L208">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L209">property snapshotType</a>
</h3>

```typescript
snapshotType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L213">property sourceDbSnapshotIdentifier</a>
</h3>

```typescript
sourceDbSnapshotIdentifier?: pulumi.Input<string>;
```


The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L217">property sourceRegion</a>
</h3>

```typescript
sourceRegion?: pulumi.Input<string>;
```


The region that the DB snapshot was created in or copied from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L221">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


Specifies the status of this DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L225">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


Specifies the storage type associated with DB snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/snapshot.ts#L229">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


Specifies the storage type associated with DB snapshot.

<h2 class="pdoc-module-header" id="SubnetGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L116">interface SubnetGroupArgs</a>
</h2>

The set of arguments for constructing a SubnetGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L120">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB subnet group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L128">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L132">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L136">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="SubnetGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L86">interface SubnetGroupState</a>
</h2>

Input properties used for looking up and filtering SubnetGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L90">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the db subnet group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L94">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the DB subnet group. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DB subnet group. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L102">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L106">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of VPC subnet IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/rds/subnetGroup.ts#L110">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

